NIP - Commands
==============

These are the cli commands provided to nip. Each service is wrapped in a utility function
that calls a list of hooks `before` and `after` the command function is called. As well as
a special list of hooks that fire if an `exception` is thrown anywhere along the line.


The idea is to build up the required state in the passed context object (`ctx.obj` or "state")
that all hooks receive as their first argument. The state can be mutated and queried by using
the provided selectors and setters, or directly (`ctx.obj` is essentially a basic python dict,
with more or less the same interface). The `nip.json` file itself is stored in the state under
the key `ctx.obj['NIPFILE']`, which can be transformed and written back out to file at the end
of the command.


Example
-------

So for example the `nip add` command is handled similar to this:

```
$ nip add -D flake8
```

- First, the incoming command get passed to the main `click` group, which sets up any middleware
to be used further down in any hooks (like the `nipfile` state, a `print` handler, `env` variables
etc..)

- Any [before](./add/hooks.py#L11) hooks are called in sequence. They create the cli greeting and make sure there's a pipfile in the cwd, etc..

- The command and arguments are parsed by click and passed to the [`add`](../cli.py#L55) wrapped handler function.

- The actual [`nip_add`](./add/hooks.py#L24) function is now called, which installs `flake8` and updates the `dev_dependencies` nipfile section in the state object with the new package info.

- Once finished, the [after](./add/hooks.py#L15) hooks are called. They write the updated state out to the `requirements_dev.txt` and `nipfile`, and print a success message to the screen.


> The other commands are more or less a variation on this theme, some with more hooks than others, some with a very minimal main function, etc.. The important part is any changes should be made to the state object, which can be thought of as the "single source of truth". (The goal is to eventually provide an immutable state object that supports time travel and other nice debugging and QOL features that can be implemented easily by using that approach.)
