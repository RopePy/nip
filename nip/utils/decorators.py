import os
import contextlib
from functools import wraps


def log(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        print(f'[{f.__name__}], Args: {args}, KwArgs: {kwds}')
        return f(*args, **kwds)
    return wrapper


def supress_stdout(func, *_, **__):
    def wrapper(*args, **kwargs):
        with open(os.devnull, 'w') as devnull:
            with contextlib.redirect_stdout(devnull):
                func(*args, **kwargs)
    return wrapper

__all__ = ['log', 'supress_stdout']
