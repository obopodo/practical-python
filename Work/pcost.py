# pcost.py
#
# Exercise 1.27
import csv
import sys

def portfolio_cost(filename):
    total_price = 0
    line_number = 1
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        header = next(rows)
        for row in rows:
            try:
                shares = int(row[1])
                price = float(row[2])
                price *= shares
                total_price += price
            except ValueError:
                print(f'Value in line {line_number} is missing!')
            finally:
                line_number += 1

        return total_price

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)
