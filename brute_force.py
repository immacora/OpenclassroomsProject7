from functions import data_import
from functions import data_export


def combinations(stocks):
    """Boucle sur la liste d'actions pour créer les premières combinaisons.
    Boucle ensuite sur la liste des combinaisons pour créer les prochaines combinaisons
    en y ajoutant chaque action qui suit la dernière action de la combinaison.

    Retourne:
        liste: Combinaisons d'actions (liste de listes).
    """
    count = 0
    combinations = []

    try:
        print("\nCréation des combinaisons d'actions.")

        for i in range(0, len(stocks)):
            combination = [stocks[i]]
            combinations.append(combination)
            count += 1

            for j in range(0, (len(stocks) - count)):
                combination = [stocks[i], stocks[j + count]]
                combinations.append(combination)

                for stock in stocks:
                    if (stock == combination[-1]) and (combination[-1] != stocks[-1]):
                        stock_index = stocks.index(stock)
                        combination = combination + [stocks[stock_index + 1]]
                        combinations.append(combination)
        return combinations
    except Exception as e:
        print(f"ERREUR: Les combinaisons d'actions n'ont pas pu être créées.\n{str(e)}\n")


def create_combinations_result(combinations):
    """Crée un dictionnaire par combinaison d'action (id, name, len_combination, total_investment, total_profit)
    et la liste des dictionnaires.

    Retourne:
        liste: Résultats (dictionnaires) de la simulation d'investissement et de profit par combinaison d'actions.
    """
    combinations_result = []
    count = 0

    for combination in combinations:
        count += 1
        id = count
        name = f"combinaison_{count}"
        len_combination = len(combination)
        total_investment = 0.0
        total_profit = 0.0

        combination_result = {
            'id': id,
            'name': name,
            'actions_combination': combination,
            'nb_actions': len_combination,
        }

        for action in combination:
            action_price = float(action[1])
            total_investment += action_price

            action_profit = float(action[2])
            total_profit += action_profit

            combination_result['total_investment'] = total_investment
            combination_result['total_profit'] = total_profit

        combinations_result.append(combination_result)

    return combinations_result


def select_optimal_investment(combinations_result):
    """Trie les dictionnaires de chaque simulation financière et sélectionne celui qui offre
    le meilleur profit pour un montant maximal de 500 euros.
    Supprime les investissements de plus de 500€ puis effectue un tri par sélection pour trouver le profit maximal.

    Retourne:
        dict: Combinaison optimale détaillée.
    """
    combinations_max_invest = []

    for combination in combinations_result:
        if combination['total_investment'] <= 500.0:
            combinations_max_invest.append(combination)

    combination_total_profit_max = combinations_max_invest[0]['total_profit']
    optimal_investment = combinations_max_invest[0]

    for combination in combinations_max_invest:
        if combination['total_profit'] > combination_total_profit_max:
            combination_total_profit_max = combination['total_profit']
            optimal_investment = combination

    return optimal_investment


def brute_force():
    """Algorithme de Force brute énumérant toutes les combinaisons possibles d'une liste d'actions
    et sélectionnant celle qui totalise le meilleur profit sur 2 ans selon certains critères:
    - Chaque action ne peut être achetée qu'une seule fois.
    - Il est impossible d'acheter une fraction d'action.
    - L'investissement maximal est de 500 euros.
    Crée la liste des dictionnaires de chaque simulation financière par combinaison
    et l'exporte dans le répertoire result.
    Trie les dictionnaires, sélectionne la solution optimale selon les critères énoncés et l'affiche.
    """
    stocks = data_import.get_stocks()
    
    total_combinations = combinations(stocks)

    combinations_result = create_combinations_result(total_combinations)
    csv_name = 'brute_force_combinations_result'
    data_export.create_csv_result(csv_name, combinations_result)

    optimal_investment = [select_optimal_investment(combinations_result)]
    csv_name = 'brute_force_optimal_investment'
    data_export.create_csv_result(csv_name, optimal_investment)
    print(f"L'investissement optimal selon l'algorithme de force brute est :\n{optimal_investment}\n")


""" Appel de l'algorithme BRUTE FORCE"""
brute_force()
