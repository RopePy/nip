def register_echo(ctx, echo=print):
    ctx.obj['ECHO'] = echo

echo_selector = lambda ctx: ctx.obj['ECHO']

__all__ = ['register_echo', 'echo_selector']
