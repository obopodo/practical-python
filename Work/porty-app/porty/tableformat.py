class TableFormatter:
    def headings(self, headers):
        '''
        Emit the table headings.
        '''
        raise NotImplementedError()

    def row(self, rowdata):
        '''
        Emit a single row of table data.
        '''
        raise NotImplementedError()

class TextTableFormatter(TableFormatter):
    '''
    Emit a table in plain-text format
    '''
    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print(f'{d:>10s}', end=' ')
        print()

class CSVTableFormatter(TableFormatter):
    '''
    Output portfolio data in CSV format
    '''
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))

class HTMLTableformatter(TableFormatter):
    def headings(self, headers):
        print('<tr>', end='')
        for h in headers:
            print(f'<th>{h}</th>', end='')
        print('</tr>')

    def row(self, rowdata):
        print('<tr>', end='')
        for d in rowdata:
            print(f'<td>{d}</td>', end='')
        print('</tr>')

class FormatError(Exception):
    pass

def create_formatter(format='txt'):
    '''
    Assign a type to formatter
    '''
    if format.lower() == 'txt':
        formatter = TextTableFormatter()
    elif format.lower() == 'csv':
        formatter = CSVTableFormatter()
    elif format.lower() == 'html':
        formatter = HTMLTableformatter()
    else:
        raise FormatError(f'Sorry, format \'{format}\' is not supported')
    return formatter

def print_table(portfolio, headers, formatter):
    '''
    Print a nicely formated table from a list of (name, shares, price, change) tuples.
    '''
    formatter.headings(headers)
    for row in portfolio:
        rowdata = [str(getattr(row, h)) for h in headers]
        formatter.row(rowdata)
