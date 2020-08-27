# pcost.py
#
# Exercise 1.27
import csv
import sys
from report import read_portfolio

def portfolio_cost(filename):
    total_price = 0.0
    portfolio = read_portfolio(filename)

    for i, record in enumerate(portfolio):
        total_price += record['shares'] * record['price']

    return total_price

# if len(sys.argv) == 2:
#     filename = sys.argv[1]
# else:
#     filename = 'Data/missing.csv'
#
# cost = portfolio_cost(filename)
# print('Total cost:', cost)
