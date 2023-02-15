from functions import csv_import


def combinations(stocks):
    """Boucle sur la liste d'actions pour créer les premières combinaisons. Boucle ensuite sur la liste des combinaisons pour créer les prochaines combinaisons en y ajoutant chaque action qui suit la dernière action de la combinaison.

    Retourne:
        liste: Combinaisons d'actions (liste de listes).
    """
    count = 0
    combinations = []

    for i in range(0, len(stocks)):
        combination = stocks[i]
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

########## Main ##########

stocks = csv_import.get_stocks()
print('stocks', stocks)

combinations = combinations(stocks)
print('combinations', combinations)