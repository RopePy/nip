from nip.config import defaults
from nip.middleware.nipfile import (
    dependencies_selector, dev_dependencies_selector)
from nip.utils.path import file_write_lines


def write_requirements_file(ctx, *args, **kwargs):
    """ Writes project requirements out to `requirements[_dev].txt`
        - (uses the info found in the nipfile)

    Usually used as an after hook.

    Arguments:
        ctx {[click.Context]} -- Click application context
        *args {[list]} -- Passed args
        **kwargs {[dict]} -- Passed kwargs

    """

    dependencies = [f"{k}{v}" for k, v in dependencies_selector(ctx).items()]
    dev_dependencies = [f"{k}{v}" for k,
                        v in dev_dependencies_selector(ctx).items()]

    # TODO Read up on requirements files. I don't think I'm using them right..
    # FIXME This should _not_ be a destructive operation
    file_write_lines(dependencies, defaults.REQUIREMENTS_FILE)
    file_write_lines(dev_dependencies, defaults.DEV_REQUIREMENTS_FILE)
