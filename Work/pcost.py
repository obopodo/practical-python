# pcost.py
#
# Exercise 1.27
def portfolio_cost(filename):
    total_price = 0
    line_number = 1
    with open(filename, 'rt') as f:
        header = next(f)
        for line in f:
            line_items = line.split(',')
            try:
                shares = int(line_items[1])
                price = float(line_items[2])
                price *= shares
                total_price += price
            except ValueError:
                print(f'Value in line {line_number} is missing!')
            finally:
                line_number += 1

        return total_price

cost = portfolio_cost('Data/portfolio.csv')
print('Total cost:', cost)
