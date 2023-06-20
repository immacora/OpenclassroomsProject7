# OpenclassroomsProject7
Résolvez des problèmes en utilisant des algorithmes en Python

Algorithme permettant de maximiser les bénéfices d'opérations financières selon les méthodes suivantes :

- Force brute (méthode naïve : énumérer toutes les combinaisons possibles et sélectionner la solution optimale)
- Gloutonne (Sélection par étape de la meilleure solution locale disponible à chaque itération)


## Prérequis :
    - python 3.11.2
    - pip

## Installation
    - Cloner le projet : `git clone https://github.com/immacora/OpenclassroomsProject7.git`
    - Créez l’environnement virtuel du projet : `py -m venv .venv`
    - Activez l’environnement virtuel : `.venv\Scripts\activate`
    - Installer les modules : `pip install -r requirements.txt`

## Contenu
    - Un répertoire data contenant les fichiers de données et fonctions associées
    - Un répertoire flake8 contenant le fichier HTML généré par flake8
    - Le répertoire result pour consultation des résultats et rapports d'exploration des données.
    - Le fichier brute_force.py permettant d'exécuter l'algorithme Brute force
    - Le fichier optimized.py permettant d'exécuter l'algorithme Glouton sur les 3 fichiers
    - Le fichier requirements
    - Le fichier flake8
    - Le fichier README

## Utilisation
    - Exécutez l'algorithme Brute force depuis la console, saisir : `py brute_force.py`
    - Exécutez l'algorithme optimisé (Glouton) depuis la console, saisir : `py optimized.py`

## Conformité PEP 8
    - Générer 1 rapport flake8 : `flake8 --format=html --htmldir=flake-report`