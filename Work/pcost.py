# pcost.py
#
# Exercise 1.27
import csv
from report import read_portfolio

def portfolio_cost(filename):
    total_cost = 0.0
    portfolio = read_portfolio(filename)

    for i, record in enumerate(portfolio):
        total_cost += record.shares * record.price

    return total_cost

def main(args:list):
    total_cost = portfolio_cost(args[1])
    print('Total cost:', total_cost)
    # return total_cost

if __name__ == '__main__':
    import sys
    main(sys.argv)
