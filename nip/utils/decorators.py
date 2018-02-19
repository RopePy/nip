from functools import wraps

from nip.utils.spinner import create_spinner


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


def make_dot_accessible(py_dict):
    class ObjectView:
        def __init__(self, inner):
            super(ObjectView, self).__setattr__('data', inner)

        def __setattr__(self, k, v):
            self.__dict__[k] = v

        def __getattr__(self, k):
            try:
                return self.data[k]
            except KeyError:
                raise AttributeError
    return ObjectView(py_dict)


def log(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        print(f'[{f.__name__}], Args: {args}, KwArgs: {kwds}')
        return f(*args, **kwds)
    return wrapper
