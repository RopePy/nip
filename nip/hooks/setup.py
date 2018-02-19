from nip.middleware.nipfile import nipfile_selector
from nip.templates.setup import SETUP_PY_TEMPLATE
from nip.utils.path import get_python_setup_py_path


def write_setup_file(ctx, *args, **kwargs):
    """ Writes the created `setup.py` to file

    Usually used as an after hook.

    Arguments:
        ctx {[click.Context]} -- Click application context
        *args {[list]} -- Passed args
        **kwargs {[dict]} -- Passed kwargs

    """
    nipfile = nipfile_selector(ctx)
    context = {
        'name': nipfile['name'],
        'version': str(nipfile['version']),
    }
    with open(get_python_setup_py_path(), 'w') as fp:
        fp.write(SETUP_PY_TEMPLATE % context)
