from nip.utils.formatting import pformat_json
from nip.middleware.echo import echo_selector
from nip.middleware.nipfile import nipfile_selector


def logger(ctx, *args, **kwargs):
    """ Logging hook """
    nipfile = nipfile_selector(ctx)
    echo = echo_selector(ctx)

    echo('nipfile -> ', pformat_json(nipfile))
    echo('args -> ', args)
    echo('kwargs -> ', pformat_json(kwargs))
