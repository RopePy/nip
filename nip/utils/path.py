import os

from nip.config import paths
__dirname = os.getcwd()


def directory_is_empty(target_dir: str):
    for _, _, files in os.walk(target_dir):
        return True if not files else False


def current_working_directory_is_empty():
    return directory_is_empty(__dirname)


def current_working_directory_has_venv():
    return os.path.exists(paths.PYTHON_MODULES_PATH)


def get_basename():
    return os.path.basename(__dirname.rstrip('/'))


def file_write_lines(lines, to):
    with open(to, 'w') as fs:
        fs.write("\n".join(lines))
