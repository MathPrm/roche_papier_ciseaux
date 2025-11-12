# ✊✋✌️ Roche-Papier-Ciseaux

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/downloads/)

## 🌟 Aperçu du Projet

`roche_papier_ciseaux` est une implémentation simple et interactive du célèbre jeu de **Pierre-Papier-Ciseaux** (ou Roche-Papier-Ciseaux) en ligne de commande (CLI), développée en Python. Le jeu permet à l'utilisateur d'affronter un adversaire contrôlé par l'ordinateur (appelé **Georges le Malin**) sur plusieurs tours.

Ce projet utilise des techniques d'affichage en console avancées (séquences ANSI) pour une expérience utilisateur dynamique et propre.

## ✨ Fonctionnalités

* **Jeu Multi-Tours :** Continuez à jouer jusqu'à ce que vous décidiez de terminer la partie.
* **Affichage Dynamique :** Utilisation des séquences d'échappement ANSI pour effacer et mettre à jour l'écran, offrant une interface claire et interactive.
* **Scores :** Les scores du joueur et de Georges sont affichés et mis à jour après chaque tour.
* **Sélection au Clavier :** Le module `validate_choice` permet une sélection d'attaque via les flèches du clavier.

## 🛠️ Installation

### Prérequis

Assurez-vous d'avoir [Python 3.10](https://www.python.org/downloads/) ou une version supérieure installée sur votre machine.

### Étapes

1.  **Clonez le dépôt :**
    ```bash
    git clone [https://github.com/MathPrm/roche_papier_ciseaux.git](https://github.com/MathPrm/roche_papier_ciseaux.git)
    cd roche_papier_ciseaux
    ```

2.  **Créez et activez un environnement virtuel (recommandé) :**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # Sous Linux/macOS
    venv\Scripts\activate   # Sous Windows
    ```

3.  **Installez les dépendances :**
    ```bash
    pip install -r requirements.txt
    ```

## 🚀 Utilisation

Pour lancer le jeu, exécutez le fichier principal du projet `main.py` et suivez les instructions à l'écran :

```bash
python3 main.py
