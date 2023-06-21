import pyinputplus as pyip
import time
import pandas as pd
from data.data_functions import DATAFRAME_0, DATAFRAME_1, DATAFRAME_2, data_cleaning, create_csv_result


def optimized(original_df, df_name):
    """
    Algorithme (Glouton) effectuant les meilleurs choix d'action possible dans une liste d'actions
    pour trouver le meilleur profit sur 2 ans selon certains critères:
    - Chaque action ne peut être achetée qu'une seule fois.
    - Il est impossible d'acheter une fraction d'action.
    - L'investissement maximal est de 500 euros.

    Crée le rapport d'exploration des données, nettoie et trie les datas par bénéfice et profit (ordre descendant).
    Démarre le timer.
    Crée la liste d'actions et initialise la combinaison d'actions, leur nombre, l'investissement total et le profit.
    Parcourt la liste dans l'ordre descendant de bénéfice et profit (tri donné par data_cleaning)
    Ajoute l'action si son prix ajouté n'excède pas l'investissement maximal
    Continue jusqu'à ce que l'investissement maximal de 500 euros soit atteint.
    """
    try:
        print(f"\nFichier d'actions {df_name}, rapport d'exploration des données:")
        df = data_cleaning(original_df, df_name)

        print("\nDébut du calcul par algorithme glouton.")
        start_time = time.time()
        stocks = df.values.tolist()
        stocks_combination = []
        nb_stocks = 0
        total_investment = 0.0
        total_profit = 0.0

        for stock in stocks:
            if stock[1] + total_investment < 500:
                stocks_combination.append(stock)
                nb_stocks += 1
                total_investment += stock[1]
                total_profit += stock[2]
                stock.pop(3)

        optimal_investment = {
            'stocks_combination': stocks_combination,
            'nb_stocks': nb_stocks,
            'total_investment': total_investment,
            'total_profit': total_profit
        }

        df = pd.DataFrame(optimal_investment)
        csv_name = f"OPTIMIZED_optimal_investment_{df_name}"
        create_csv_result(csv_name, df)

        print(f"\nL'investissement optimal selon l'algorithme glouton est:\
              \nCombinaison: {optimal_investment['nb_stocks']} actions\
              \nInvestissement total: {optimal_investment['total_investment']}\
              \nProfit total: {optimal_investment['total_profit']}"
              )

        end_time = time.time()
        run_time = end_time - start_time
        print(f"\nLa durée d'exécution de l'algorithme est de {run_time} secondes\n")

    except Exception as e:
        print(f"\nERREUR: L'algorithme n'a pas fonctionné.\n{str(e)}")


def run_menu():
    """Affiche le menu et lance l'algorithme sur le fichier choisi."""
    menu = pyip.inputMenu(
        choices=["Dataset 1", "Dataset 2", "Dataset 0", "Quitter"],
        prompt="\n----- LANCER L'ALGORITHME OPTIMISE SUR LE FICHIER -----\n", numbered=True)
    if menu == "Dataset 1":
        optimized(DATAFRAME_1, "Dataset 1")
    elif menu == "Dataset 2":
        optimized(DATAFRAME_2, "Dataset 2")
    elif menu == "Dataset 0":
        optimized(DATAFRAME_0, "Dataset 0")
    else:
        exit()


if __name__ == "__main__":
    run_menu()
