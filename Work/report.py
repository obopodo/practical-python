# report.py
#
# Exercise 2.4
import csv
from pprint import pprint
import fileparse as fp
import stock
from tableformat import create_formatter, print_table

def read_prices(prices_filename):
    '''Function that reads prices set'''
    with open(prices_filename, 'rt') as inf:
        lines = fp.parse_csv(inf, has_headers = False, types=[str, float])
    prices = {name: price for name, price in lines}
    return prices


def read_portfolio(portfolio_filename):
    '''
    Function that reads portfolio dataset into a list of dicts
    '''
    with open(portfolio_filename, 'rt') as inf:
        portdicts = fp.parse_csv(inf, select=['name', 'shares', 'price'], types=[str, int, float])
    portfolio = [stock.Stock(d['name'], d['shares'], d['price']) for d in portdicts]
    return portfolio


def make_report(portfolio, prices):
    report = []
    for row in portfolio:
        report.append((row.name, row.shares, prices[row.name], prices[row.name] - row.price))
    return report


def print_report(report, formatter):
    '''
    Print a nicely formated table from a list of (name, shares, price, change) tuples.
    '''
    formatter.headings(['Name', 'Shares', 'Price', 'Change'])
    for name, shares, price, change in report:
        rowdata = [name, str(shares), f'{price:0.2f}', f'{change:0.2f}']
        formatter.row(rowdata)


def portfolio_report(portfolio_filename, prices_filename, format='txt'):
    '''
    Make a stock report given portfolio and price data files.
    '''
    # Read data:
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    # Create report data:
    report = make_report(portfolio, prices)
    # Print it out:
    formatter = create_formatter(format)
    print_report(report, formatter)


def main(args:list):
    if len(args) == 3:
        portfolio_report(args[1], args[2])
    elif len(args) == 4:
        portfolio_report(args[1], args[2], args[3])


if __name__ == '__main__':
    import sys
    if sys.argv:
        main(sys.argv)
