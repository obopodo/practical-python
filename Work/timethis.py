def timethis(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        r = func(*args, **kwargs)
        end = time.time()
        print(f'%s.%s: %f' % (func.__module__, func.__name__, end-start))

    return wrapper
