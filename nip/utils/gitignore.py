import os
from nip.config import paths
import nip.templates as templates


def gitignore_exists():
    return os.path.exists(paths.GITIGNORE_PATH)

def create_nipfile_gitignore():
    with open(paths.GITIGNORE_PATH, 'w') as fs:
        fs.write(templates.GITIGNORE)

def add_line_to_gitignore(line):
    with open(paths.GITIGNORE_PATH, 'a') as fs:
        fs.writelines(line)

def read_gitignore_lines():
    with open(paths.GITIGNORE_PATH, 'r') as fs:
        return fs.readlines()


__all__ = [
    'gitignore_exists',
    'create_nipfile_gitignore',
    'add_line_to_gitignore',
    'read_gitignore_lines'
]
