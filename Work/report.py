# report.py
#
# Exercise 2.4
import csv
from pprint import pprint
import fileparse as fp

def read_prices(prices_filename):
    '''Function that reads prices set'''
    with open(prices_filename, 'rt') as inf:
        lines = fp.parse_csv(inf, has_headers = False, types=[str, float])
    prices = {name: price for name, price in lines}
    # prices = fp.parse_csv(prices_filename, has_headers = False, types=[str, float])
    return prices

def read_portfolio(portfolio_filename):
    '''
    Function that reads portfolio dataset into a list of dicts
    '''
    with open(portfolio_filename, 'rt') as inf:
        portfolio = fp.parse_csv(inf, select=['name', 'shares', 'price'], types=[str, int, float])
    return portfolio


def make_report(portfolio, prices):
    report = []
    for row in portfolio:
        # report.append((row['name'], row['shares'], '$'+str(prices[row['name']]), prices[row['name']] - row['price']))
        report.append((row['name'], row['shares'], prices[row['name']], prices[row['name']] - row['price']))
    return report

def print_report(report, header=('Name', 'Shares', 'Price', 'Change')):
    print('%10s %10s %10s %10s' % header)
    print('%10s %10s %10s %10s' % tuple(['-'*10]*4))
    for r in report:
        print(f'%10s %10d %10s %10.2f' % r)

def main(args:list):
    portfolio = read_portfolio(args[1])
    prices = read_prices(args[2])
    report = make_report(portfolio, prices)
    print_report(report)
    # return portfolio, prices, report


if __name__ == '__main__':
    import sys
    if sys.argv:
        main(sys.argv)
