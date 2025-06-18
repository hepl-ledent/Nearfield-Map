import pyvisa
import matplotlib.pyplot as plt
import serial
import numpy as np

# === Configuration port série USB ===
USB_PORT = 'COM4'  # À adapter selon le système
BAUDRATE = 115200

x_points = None
y_points = None
amp_matrix = None

# === Connexion à l'appareil de mesure ===
rm = pyvisa.ResourceManager()
instrument = rm.open_resource('USB0::0x0AAD::0x01BB::204858::2::INSTR')

print("Appareil :", instrument.query("*IDN?").strip())

Fcent = float(input("Entrez la fréquence centrale à mesurer (en MHz) : "))
Fspan = float(input("Entrez le span (en MHz) : "))

instrument.write("*RST")
instrument.write("INST:SEL SPEC")
instrument.write("INIT:CONT OFF")
instrument.write(f"FREQ:CENT {Fcent}MHz")
instrument.write(f"FREQ:SPAN {Fspan}MHz")
instrument.write("INIT;*WAI")
instrument.write("CALC:MARK1 ON")
instrument.write("CALC:MARK1:MAX")
instrument.write("CALC:MARK1:FUNC:STR OFF")

# === Fonction de décodage du message USB ===
def decode_message(line):
    try:
        line = line.strip().decode('utf-8')
        parts = line.split(',')
        if len(parts) != 3:
            return None

        label = parts[0]
        x = int(parts[1].split('=')[1])
        y = int(parts[2].split('=')[1])

        return (label, x, y)
    except Exception as e:
        print(f"Erreur de décodage : {e} -> ligne brute : {line}")
        return None

# === Boucle de gestion des messages ===
with serial.Serial(USB_PORT, BAUDRATE, timeout=1) as ser:
    print(f"En attente de messages sur {USB_PORT}...")

    while True:
        line = ser.readline()
        if not line:
            continue

        data = decode_message(line)
        if data is None:
            continue

        label, x, y = data

        if label == "Size":
            x_points = x
            y_points = y

            amp_matrix = np.zeros((y_points, x_points))
            print(f"Taille de grille reçue : x={x_points}, y={y_points}")

        elif label == "Pos":
            if amp_matrix is None:
                print("Erreur : matrice non initialisée. Attente du message Size.")
                continue

            if 0 <= x < x_points and 0 <= y < y_points:

                print(f"Mesure à la position ({x}, {y})...")

                instrument.write("INIT;*WAI")
                freq = float(instrument.query("CALC:MARK1:X?"))
                amp = float(instrument.query("CALC:MARK1:Y?"))
                amp_matrix[y, x] = amp

                print(f"  → {freq / 1e6:.3f} MHz, {amp:.2f} dBm")

        elif label == "endScan":
            print("Fin de scan reçue. Arrêt de la boucle.")
            break

instrument.close()

# === Affichage de la carte CEM ===
plt.figure(figsize=(8, 6))
plt.imshow(amp_matrix, origin='lower', cmap='plasma', extent=[0, x_points, 0, y_points])
plt.colorbar(label='Amplitude (dBm)')
plt.title('Carte CEM')
plt.xlabel('X')
plt.ylabel('Y')
plt.tight_layout()
plt.show()
