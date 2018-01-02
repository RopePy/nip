from nip.config import paths
from nip.middleware.nipfile import nipfile_selector
from nip.middleware.echo import echo_selector
from nip.templates.setup import SETUP_PY_TEMPLATE


def write_setup_file(ctx, *args, echo=print, **kwargs):
    nipfile = nipfile_selector(ctx)
    context = {
        'name': nipfile['name'],
        'version': str(nipfile['version']),
    }
    echo = echo_selector(ctx)
    echo('Creating `setup.py` file.')
    with open(paths.PYTHON_SETUP_PY_PATH, 'w') as fobj:
        fobj.write(SETUP_PY_TEMPLATE % context)
