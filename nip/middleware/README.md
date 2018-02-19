NIP - Middleware
================

Each key in the `ctx.obj` is registered through `middleware`, and is available for _all_ commands.


Selectors
---------

There will be a provided `selector` for each key in the state that can be used to focus on a
specific key, simply pass it the ctx and it returns the part of the state you need, ex: 

Example:
```
from nip.middleware import echo_selector

def some_hook(ctx, *args, **kw):
    echo = echo_selector(ctx)
    echo('Hello world')
```
