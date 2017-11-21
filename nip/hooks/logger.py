from nip.utils.decorators import log
from nip.utils.formatting import pformat_json
from nip.middleware.nipfile import nipfile_selector

@log
def logger(ctx, *args, **kwargs):
    """ Logging hook """
    nipfile = nipfile_selector(ctx)
    print('ctx -> ', pformat_json(nipfile))
    print('args -> ', args)
    print('kwargs -> ', pformat_json(kwargs))


__all__ = ['logger']
