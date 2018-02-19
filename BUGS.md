BUGS
----

**1** - Handle non-existent packages

```
    nip add virtualenvapi                  0 < 17:49:40
    nip - v0.2.0 - Add - Made with Love, by Duroktar © 2018

    Installing dependencies - virtualenvapi
    ⠇ Installing virtualenvapi   Could not find a version that satisfies the requirement virtualenvapi (from versions: )
    No matching distribution found for virtualenvapi
    ⠏ Installing virtualenvapi .. Done.
    nip encountered a problem and had to quit.
    Traceback (most recent call last):
    File "/home/duroktar/nip/nip/hooks/__init__.py", line 23, in wrapper
        func(ctx, *args, **kwds)
    File "/home/duroktar/nip/nip/cli.py", line 57, in add
        commands.add.nip_add(ctx, packages, dev)
    File "/home/duroktar/nip/nip/commands/add/hooks.py", line 31, in nip_add
        name, version = pip_install_and_return_meta(package, silent)
    File "/home/duroktar/nip/nip/providers/pip.py", line 67, in pip_install_and_return_meta
        version_spec = get_version_of_venv_package(name)
    File "/home/duroktar/nip/nip/utils/version.py", line 22, in get_version_of_venv_package
        return package[0]
    IndexError: list index out of range

    During handling of the above exception, another exception occurred:

    Traceback (most recent call last):
    File "/home/duroktar/.pyenv/versions/3.6.1/bin/nip", line 11, in <module>
        load_entry_point('nip', 'console_scripts', 'nip')()
    File "/home/duroktar/nip/nip/cli.py", line 70, in main
        cli(obj={})
    File "/home/duroktar/.local/lib/python3.6/site-packages/click/core.py", line 716, in __call__
        return self.main(*args, **kwargs)
    File "/home/duroktar/.local/lib/python3.6/site-packages/click/core.py", line 696, in main
        rv = self.invoke(ctx)
    File "/home/duroktar/.local/lib/python3.6/site-packages/click/core.py", line 1060, in invoke
        return _process_result(sub_ctx.command.invoke(sub_ctx))
    File "/home/duroktar/.local/lib/python3.6/site-packages/click/core.py", line 889, in invoke
        return ctx.invoke(self.callback, **ctx.params)
    File "/home/duroktar/.local/lib/python3.6/site-packages/click/core.py", line 534, in invoke
        return callback(*args, **kwargs)
    File "/home/duroktar/.local/lib/python3.6/site-packages/click/decorators.py", line 17, in new_func
        return f(get_current_context(), *args, **kwargs)
    File "/home/duroktar/nip/nip/hooks/__init__.py", line 30, in wrapper
        raise hook_error
    File "/home/duroktar/nip/nip/hooks/__init__.py", line 25, in wrapper
        execute_hooks(hooks['error'], ctx, error, *args, **kwds)
    File "/home/duroktar/nip/nip/hooks/__init__.py", line 13, in execute_hooks
        hook(ctx, *args, **kwds)
    File "/home/duroktar/nip/nip/hooks/logger.py", line 11, in logger
        echo('nipfile -> ', pformat_json(nipfile))
    File "/home/duroktar/.local/lib/python3.6/site-packages/click/utils.py", line 259, in echo
        file.write(message)
    AttributeError: 'str' object has no attribute 'write'
```


**2** - Doesn't pin versions in `requirements*.txt` file
