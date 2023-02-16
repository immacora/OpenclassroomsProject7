import os
import csv


def create_csv_result(csv_name, result):
    """Crée le répertoire result s'il n'existe pas et y ajoute le fichier du résultat obtenu.
    """
    if not os.path.exists('result'):
        os.makedirs('result')
    
    print(f"\nCréation du fichier {csv_name}.")

    try:
        keys = result[0].keys()
    except KeyError:
        print("ERREUR: La clé est est incorrecte ou inexistante dans la liste de résultats.")
    else:
        with open(os.path.join('result/') + csv_name + '.csv', 'w', encoding='utf-8', newline='') as csvfile:
            dict_writer = csv.DictWriter(csvfile, keys, delimiter=';')
            dict_writer.writeheader()
            dict_writer.writerows(result)
        print(f"\nLe fichier {csv_name} a bien été créé, il est consultable depuis le répertoire result.\n")
