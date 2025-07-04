# Guide d'utilisation du scprit python

Le script suivant assure :

- La configuration de la fréquence centrale et du span
- La communication avec l’analyseur via **SCPI**
- L’écoute d’un **port série USB** (par ex. `COM4`) pour recevoir les données du STM32
- L’affichage final sous forme de **carte thermique**


## Avant de lancer le scprit

- Vérifier l'ID de l'analyseur de spectre
- Vérifier le port COM sur lequel le STM32 communiquera
- Modifier le BaudRate n'est pas nécessaire

## Fonctionnement

- Lorsqu'on lance le code, rentrer la fréquence centrale et le span pour régler l'analyseur de spectre
- lancer le scan grid lorsqu'on a le message
    ```bash
    En attente de messages sur {USB_PORT}...
    ```
![image](https://github.com/user-attachments/assets/dd9f0be2-70d3-4a48-be43-879eb39171eb)
    
## Possibilité de modifier les couleurs des échelles de l'affichage avec MatPlotLib

Dans la ligne ci dessous, il est possible de modifier les couleurs de l'échelle en changeant le paramètre `cmap`.
    
Voici une documentation sur les [échelles disponibles](https://matplotlib.org/stable/users/explain/colors/colormaps.html).
```bash
plt.imshow(amp_matrix, origin='lower', cmap='plasma', extent=[0, x_points, 0, y_points])
```

