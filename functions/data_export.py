import os
import csv


def create_csv_result(csv_name, result):
    """Crée le répertoire result s'il n'existe pas et y ajoute le fichier des résultats obtenus.
    """
    if not os.path.exists('result'):
        os.makedirs('result')
    keys = result[0].keys()
    with open(os.path.join('result/') + csv_name + '.csv', 'w', encoding='utf-8', newline='') as csvfile:
        dict_writer = csv.DictWriter(csvfile, keys, delimiter=';')
        dict_writer.writeheader()
        dict_writer.writerows(result)
