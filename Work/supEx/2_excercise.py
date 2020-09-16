# import follow
#
# lines = follow.follow('Data/stocklog.csv')
#
# ibm = follow.filematch(lines, 'IBM')
#
# for line in ibm:
#     print(line)

# from follow import follow
# import csv
#
# lines = follow('Data/stocklog.csv')
# rows = csv.reader(lines)
# for row in rows:
#     print(row)

# def avg(x, *args):
#     a = (x + sum(args)) / (1 + len(args))
#     return a

# import time
#
# def add(x, y):
#     def do_add():
#         print('adding', x, y)
#         return x + y
#     return do_add
#
# def after(seconds, func):
#     time.sleep(seconds)
#     func()

# def logged(func):
#     def wrapper(*args, **kwargs):
#         print('Calling', func.__name__)
#         return func(*args, **kwargs)
#     return wrapper
#
# def add(x, y):
#     print(x+y)
