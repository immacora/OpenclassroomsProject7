from functions import data_import
from functions import data_export


def combinations(stocks):
    """Boucle sur la liste d'actions pour créer les premières combinaisons.
    Boucle ensuite sur la liste des combinaisons pour créer les prochaines combinaisons en y ajoutant chaque action qui suit la dernière action de la combinaison.

    Retourne:
        liste: Combinaisons d'actions (liste de listes).
    """
    count = 0
    combinations = []

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


def combinations_result(combinations):
    """Crée un dictionnaire par combinaison d'action (id, name, len_combination, total_investment, total_profit) et la liste des dictionnaires.

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

