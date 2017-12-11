import re

__all__ = ['is_version']

VERSION_NUMBERS_RE = re.compile(r'^\d+(\.\d+){2,3}$')


def is_version(text):
    return VERSION_NUMBERS_RE.match(text)
