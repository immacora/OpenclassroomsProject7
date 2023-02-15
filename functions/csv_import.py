import csv


def get_stocks():
    """Ouvre le fichier csv dataset0_Python+P7.csv du dossier data, copie son contenu dans une liste et supprime la ligne d'entête.
    
    Retourne: 
        liste: Actions (noms, prix et profit)."""
    stocks = []
    try:
        print("\nImport du fichier dataset0_Python+P7.csv contenu dans le répertoire data.\n")
        with open('data/dataset0_Python+P7.csv', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                stocks.append(row)
        stocks.pop(0)
        return stocks
    except FileNotFoundError:
        print("ERREUR: Le fichier n'a pas été trouvé.")
