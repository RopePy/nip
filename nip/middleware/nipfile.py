from nip.nip import get_existing_nipfile_or_create_new


def register_nipfile(ctx):
    ctx.obj['NIPFILE'] = get_existing_nipfile_or_create_new()

nipfile_selector = lambda ctx: ctx.obj['NIPFILE']

__all__ = ['register_nipfile', 'nipfile_selector']
