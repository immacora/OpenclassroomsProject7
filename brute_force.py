import csv


stocks = ['Action-1', 'Action-2', 'Action-3', 'Action-4']

def combinations(stocks):
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



########## Main ##########

combinations = combinations(stocks)
print(combinations)