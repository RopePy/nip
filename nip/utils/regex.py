import re

__all__ = ['is_version']

is_version = lambda text: re.compile(r'^\d+(\.\d+){2,3}$').match(text)
