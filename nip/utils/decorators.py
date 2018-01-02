import os
import contextlib
from functools import wraps

from nip.utils.spinner import create_spinner

def log(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        print(f'[{f.__name__}], Args: {args}, KwArgs: {kwds}')
        return f(*args, **kwds)
    return wrapper


def supress_stdout(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        with open(os.devnull, 'w') as devnull:
            with contextlib.redirect_stdout(devnull):
                f(*args, **kwargs)
    return wrapper


def create_spinner_with_message(message):
    start, stop = create_spinner(message)

    def inner_wrapper(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start()
            try:
                func(*args, **kwargs)
            except Exception as error:
                raise error
            finally:
                stop()
        return wrapper
    return inner_wrapper
