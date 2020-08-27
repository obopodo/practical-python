# report.py
#
# Exercise 2.4
import sys
import csv
from pprint import pprint
import fileparse as fp

if len(sys.argv) == 2:
    portfolio_filename = sys.argv[1]
else:
    portfolio_filename = 'Data/portfolio.csv'

prices_filename = 'Data/prices.csv'

def read_prices(prices_filename):
    '''Function that reads prices set'''
    prices = {name: price for name, price in fp.parse_csv(prices_filename, has_headers = False, types=[str, float])}
    # prices = fp.parse_csv(prices_filename, has_headers = False, types=[str, float])
    return prices

def read_portfolio(portfolio_filename):
    '''
    Function that reads portfolio dataset into a list of dicts
    '''
    portfolio = fp.parse_csv(portfolio_filename, select=['name', 'shares', 'price'], types=[str, int, float])
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

prices = read_prices(prices_filename)
portfolio = read_portfolio(portfolio_filename)
report = make_report(portfolio, prices)
# print_report(report)
