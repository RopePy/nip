import os
from nip import templates
from nip.config import defaults
from nip.utils.path import get_gitignore_path


def gitignore_exists(env=defaults):
    return os.path.exists(get_gitignore_path(env))


def create_gitignore(env=defaults):
    with open(get_gitignore_path(env), 'w') as fs:
        fs.write(templates.GITIGNORE)


def add_line_to_gitignore(line, env=defaults):
    with open(get_gitignore_path(env), 'a') as fs:
        fs.writelines(line)


def read_gitignore_lines(env=defaults):
    with open(get_gitignore_path(env), 'r') as fs:
        return fs.readlines()
