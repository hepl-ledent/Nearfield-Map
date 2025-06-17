## Installation de PyVISA

Dans un terminal, exécutez la commande suivante :

```bash
pip install pyvisa
```

Cela installe la bibliothèque nécessaire à la communication avec l’analyseur via **SCPI**.

---

## Installation et configuration de R&S VISA

1. Télécharger et installer **R&S VISA** depuis le site officiel :
   [R&S VISA – Rohde & Schwarz](https://www.rohde-schwarz.com/us/applications/r-s-visa-application-note_56280-148812.html)

2. Avant de lancer le logiciel, vérifier que l'analyseur de spectre apparait bien dans l'onglet 'USB Test and Measurment Devices' dans le gestionnaire de périphérique.
   Si il n'apparait pas, débrancher le câble USB. Redémarrer l'analyseur de spectre. Rebrancher le câble USB.
   
   ![image](https://github.com/user-attachments/assets/0023ef6a-3f06-4f0a-8a19-4551f05e928b)




4. Ouvrir le logiciel **RsVisaTester** installé avec R&S VISA.

5. Aller dans l’onglet **RSVisa Config**.

    ![image](https://github.com/user-attachments/assets/916d3eb2-2a31-4ad0-b099-8fb645057736)


6. Ajouter un nouvel appareil :
   - Cliquez sur le bouton **`+`**
  
      ![image](https://github.com/user-attachments/assets/3849a290-ef28-4921-b179-991fbb7c11b4)


   - Choisissez **USB** comme type d’interface
   - Cliquez sur l’icône de loupe pour rechercher les appareils disponibles
   - Sélectionnez l’analyseur FPC1000 dans la liste

      ![image](https://github.com/user-attachments/assets/74645f65-9748-48df-9898-e4de2ea8a80d)

7. Cliquer sur **Find Resource**, puis sélectionner la ressource correspondant à l’analyseur.  
   Exemple d’identifiant :  
   ```
   USB0::0x0AAD::0x01BB::204858
   ```
    ![image](https://github.com/user-attachments/assets/bc797fe8-87a1-4b73-ba55-a359d6bc7d1b)


8. Une fois connecté, vous pouvez utiliser cette ressource dans le script Python.

---

## Références

- Rohde & Schwarz. *HOW TO COMMUNICATE WITH R&S DEVICES USING VISA*.  
  [PDF](https://scdn.rohde-schwarz.com/ur/pws/dl_downloads/dl_application/application_notes/1sl374/1SL374_0e.pdf)

---

