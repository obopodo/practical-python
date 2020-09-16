# report.py
#
# Exercise 2.4
import csv
from pprint import pprint
from . import fileparse as fp
from . import stock
from .tableformat import create_formatter, print_table
from .portfolio import Portfolio

def read_prices(prices_filename):
    '''Function that reads prices set'''
    with open(prices_filename, 'rt') as inf:
        lines = fp.parse_csv(inf, has_headers = False, types=[str, float])
    prices = {name: price for name, price in lines}
    return prices


def read_portfolio(portfolio_filename, **opts):
    '''
    Function that reads portfolio dataset into a list of dicts
    '''
    with open(portfolio_filename, 'rt') as inf:
        port = Portfolio.from_csv(inf)
    return port


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

# This part sets up basic configuration of the logging module.
# Change settings here to adjust logging output as needed.
import logging
logging.basicConfig(
    filename = 'app.log',            # Name of the log file (omit to use stderr)
    filemode = 'w',                  # File mode (use 'a' to append)
    level    = logging.WARNING       # Logging level (DEBUG, INFO, WARNING, ERROR, or CRITICAL)
)
