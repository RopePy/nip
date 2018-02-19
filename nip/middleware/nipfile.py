from nip.nip import get_existing_nipfile_or_create_new


def register_nipfile(ctx):
    ctx.obj['NIPFILE'] = get_existing_nipfile_or_create_new()


def nipfile_selector(ctx):
    return ctx.obj['NIPFILE']


def name_selector(ctx):
    return ctx.obj['NIPFILE'].get('name', {})


def author_selector(ctx):
    return ctx.obj['NIPFILE'].get('author', {})


def version_selector(ctx):
    return ctx.obj['NIPFILE'].get('version', {})


def scripts_selector(ctx):
    return ctx.obj['NIPFILE'].get('scripts', {})


def dependencies_selector(ctx):
    return ctx.obj['NIPFILE'].get('dependencies', {})


def dev_dependencies_selector(ctx):
    return ctx.obj['NIPFILE'].get('dev_dependencies', {})
