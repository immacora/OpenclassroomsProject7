import time
import pandas as pd
import itertools
from data.data_functions import DATAFRAME_0, create_csv_result


def brute_force(df):
    """
    Algorithme de Force brute énumérant toutes les combinaisons possibles d'une liste d'actions
    et sélectionnant celle qui totalise le meilleur profit sur 2 ans selon certains critères:
    - Chaque action ne peut être achetée qu'une seule fois.
    - Il est impossible d'acheter une fraction d'action.
    - L'investissement maximal est de 500 euros.

    Itère sur le nombre d'actions de la liste pour créer, a chaque tour,
    la liste des combinaisons possibles de longueur i avec la fonction combinations du module itertools.
        Crée 1 dictionnaire pour chaque combinaison de la liste (+nombre d'actions, investissement et profit total).
        Ajoute chaque dictionnaire à la liste totale des combinaisons pour export en csv.
        Filtre les résultats par montant d'investissement (max: 500 euros).
        Sélectionne la meilleure combinaison par comparaison de profit max.
    Résultat :
        csv : liste de toutes les combinaisons
        csv : investissement optimal
    """
    total_combinations = []
    optimal_investment = {}
    total_investment_max = 500.0
    total_profit_max = 0.0

    try:
        stocks = df.values.tolist()
        print("\nListe des actions à analyser :\n", df,
              "\n\nDébut du calcul par algorithme de Force brute.")
        start_time = time.time()

        for i in range(1, len(stocks)+1):
            combinations = itertools.combinations(stocks, i)

            for combination in combinations:
                nb_stocks = len(combination)
                total_investment = sum(item[1] for item in combination)
                total_profit = sum(item[2] for item in combination)

                combination_dict = {
                    'stocks_combination': list(combination),
                    'nb_stocks': nb_stocks,
                    'total_investment': total_investment,
                    'total_profit': total_profit
                }
                total_combinations.append(combination_dict)

                if total_investment <= total_investment_max:
                    if total_profit > total_profit_max:
                        optimal_investment = combination_dict
                        total_profit_max = total_profit

        df_total_combinations = pd.DataFrame(total_combinations)
        csv_name = "brute_force_total_combinations"
        create_csv_result(csv_name, df_total_combinations)

        df_optimal_investment = pd.DataFrame(optimal_investment)
        csv_name = "BRUTE_FORCE_optimal_investment"
        create_csv_result(csv_name, df_optimal_investment)

        print(f"\nL'investissement optimal selon l'algorithme de force brute est :\
              \nCombinaison: {optimal_investment['stocks_combination']}\
              \nInvestissement total: {optimal_investment['total_investment']}\
              \nProfit total: {optimal_investment['total_profit']}"
              )

        end_time = time.time()
        run_time = end_time - start_time
        print(f"\nLa durée d'exécution de l'algorithme est de {run_time} secondes\n")

    except Exception as e:
        print(f"\nERREUR: L'algorithme n'a pas fonctionné.\n{str(e)}")


if __name__ == "__main__":
    brute_force(DATAFRAME_0)
