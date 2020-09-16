# fileparse.py
#
# Exercise 3.3
import csv
import logging

log = logging.getLogger(__name__)

def parse_csv(iterable, select=None, types=None, has_headers=True,
              delimiter=',', silence_errors=False):
    '''
    Parse a csv file into a list of records
    '''
    if isinstance(iterable, str):
        raise ValueError('First arg have to be iterable, eg list of lines of a file')
    rows = csv.reader(iterable, delimiter=delimiter)

    # create list of columns headers if needed
    if has_headers:
        headers = next(rows)

    # select indices of needed columns if they are specified in "select"
    if select and not has_headers:
        raise RuntimeError('select argument requires column headers')
    if select:
        indices = [headers.index(col) for col in select]
        headers = select
    else:
        indices = []

    records = []
    for i, row in enumerate(rows):
        if not row:
            continue
        if indices:
            row = [row[i] for i in indices]
        if types:
            try:
                row = [func(val) for func, val in zip(types, row)]
            except ValueError as e:
                if not silence_errors:
                    log.warning(f'Row {i}: Couldn`t convert {row}')
                    log.debug(f'Row {i}: Reason: {e}')
                continue

        if has_headers:
            record = dict(zip(headers, row))
        else:
            record = tuple(row)

        records.append(record)

    return records
