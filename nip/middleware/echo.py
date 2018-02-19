def register_echo(ctx, echo=print):
    ctx.obj['ECHO'] = echo


def echo_selector(ctx):
    return ctx.obj['ECHO']
