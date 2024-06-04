# Lunettes Intelligentes pour l'Assistance Visuelle
## Description
Ce projet vise à développer des lunettes intelligentes pour assister les personnes malvoyantes en utilisant une Raspberry Pi et une application mobile. Les lunettes sont équipées d'une caméra pour la détection du texte, des couleurs et des objets, et convertissent ces informations en voix pour l'utilisateur.
## Table des Matières
- [Installation](#installation)
- [Usage](#usage)
- [Contribuer](#contribuer)
- [Auteurs et Reconnaissance](#auteurs-et-reconnaissance)
## Installation

### Configuration de la Raspberry Pi

1. Connecter la Raspberry Pi à un moniteur, clavier et souris.
2. Installer l'OS Raspberry Pi en utilisant Raspberry Pi Imager.
3. Configurer le Wi-Fi et mettre à jour le système avec les commandes suivantes :
    ```sh
    sudo apt-get update
    sudo apt-get upgrade
    ```

### Installation des Requirements

- **EasyOCR**
    ```sh
    pip install easyocr
    ```

- **YOLO pour la Détection d'Objets**
    ```sh
    pip install torch torchvision
    ```

- **OpenCV pour la Détection de Couleurs**
    ```sh
    pip install opencv-python
    ```

- **Pyttsx3 pour la Conversion en Voix (Français et Anglais)**
    ```sh
    pip install pyttsx3
    ```

- **Tacotron pour la Synthèse Vocale en Arabe**
    Suivre la documentation officielle de Tacotron.

- **Argos Translate pour la Traduction**
    ```sh
    pip install argostranslate
    ```

### Configuration de l'Application Mobile

1. Activer le débogage USB sur votre appareil Android.
2. Connecter l'appareil à l'ordinateur via USB.
3. Utiliser Android Studio ou adb pour installer l'application :
    ```sh
    adb install /path/to/your/application.apk
    ```
## Usage
1. Démarrer la Raspberry Pi et s'assurer que tous les services nécessaires sont en cours d'exécution.
2. Ouvrir l'application mobile sur votre appareil Android.
3. Connecter l'application mobile à la Raspberry Pi via l'interface utilisateur de l'application.
4. Utiliser les lunettes pour capturer des images, détecter du texte, des couleurs et des objets, et écouter les descriptions vocales fournies par le système.
   
## Contribuer
Les contributions sont les bienvenues! Pour contribuer, veuillez suivre les étapes suivantes :
1. Forker le dépôt.
2. Créer une branche pour votre fonctionnalité (`git checkout -b feature/ma-fonctionnalite`).
3. Commiter vos modifications (`git commit -am 'Ajouter ma fonctionnalité'`).
4. Pousser votre branche (`git push origin feature/ma-fonctionnalite`).
5. Ouvrir une Pull Request.

## Auteurs et Reconnaissance
- **Chef de Projet:** EL MOTAYIQ Hajar
- **Chef de Communication:** Ben-Yadi Ouijdane
- **Chef de Livrable:** AIT TALEB Hind
- **Chef de Qualité du Code:** AIT ELFATMI Najar

Encadré par : M. Said RAKRAK

