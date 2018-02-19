NIP - nip isn't pip
===================

A fast way to start and use a python project within a virtual
environment.


Commands
--------

  > init -    Initialize a new Python project in the current folder.

  > install - Install all project dependencies and initialize a new venv if necessary.

  > add -     Install a new project dependency and add it to your nipfile. (like `pip install`)

  > remove -  Remove a dependency from your project. (like `pip uninstall`)

  > run -     Run a script from the nipfile


**Quick Start**

Enter an empty directory, type `nip init` and answer the questions.
this starts up a virtual environment for you under `./python_modules`.
You may also notice NIP has created these files in the cwd..

- `.gitignore` with the new `python_modules` included so you don't have to.
- `nip.json` file with you package details.
- `setup.py` file with a basic templated layout.

**Add a Dependency**

Run `nip add <package_name>` to install a new dependency. Nip creates a `requirements.txt` file and pins the version automatically.

*If it's a development dependency the use the option `-D`, ex: `nip add -D <package_name>` which creates a `dev_dependency.txt` file instead*

> PROTIP: Any binaries included with the added package also become available for use through nip `scripts` .. (see below)


**Scripts**

You can place shortcuts to commands in the `nipfile` under a scripts section (see example), which you can then run with
`nip run <script_name>` or just `nip <script_name>` and they will be started within the virtual environment. You can also
run any binaries installed to the `python_modules/bin` folder.

For example, if you have `tox` as a dependency, but not installed globally you can run it as a `script`, ex: 

```sh
nip.json ..

{
    ...
    "scripts": {
        "start": "python src/main.py",
        "db:migrate": "python manage.py migrate",
        ...
+       "test": "tox"
    },
    "dev_dependencies": {
+       "tox": "~=2.9.1",
        ...
    }
}

$ nip run test       // or just `nip test`
```



**Existing Projects**

Enter a directory with a `nipfile.json` and type `nip install` to
install any package requirements/virtual environments necessary for
the project and you're ready to go.


Example
-------

```sh
    $ nip init
    nip - v0.2.0 - Init - Made with Love, by Duroktar © 2018

    Package Name (nip-test):
    Author: Duroktar
    Version (0.1.0):
    License (MIT):
    ⠼ Initialising.... Done.
    Finished.
```

> nip.json

```sh
    {
        "name": "nip-test",
        "author": "Duroktar",
        "version": "0.1.0",
        "license": "MIT",
+       "scripts": {
+           "start": "python hello_world.py"
+       }
    }
```

```sh

    $ echo 'print("Hello world!!")' >> hello_world.py

    $ nip start
    nip - v0.2.0 - Run - Made with Love, by Duroktar © 2018

    Hello world!!

```


Why?
----

Starting a new Python project from scratch isn't hard, but you end up
using similar patterns and multiple tools each time. I wanted to script
away as much of that as possible without coupling everything together
into something that ended up being complicated and unmanageable.

At its core, NIP is a service based framework with a middleware and
hooks based strategy. It was built to take advantage of existing
Python tools instead of trying to replace them. It uses `pip` under
the hood, so if you want stop using `nip` just remove the `nip.json`
file and you're left with a standard python package.


Development
-----------

I tried to make nip really easy to understand and work on, there's a useful
guide [here](./nip/services/README.md) in the services section that tries to give a basic rundown of
what happens when nip runs, and serves as a decent starting point for those
interested in helping out.


Third Party Packages
--------------------

NIP was heavily inspired by NPM/Yarn and the FeathersJS Framework.

- Click - http://click.pocoo.org/5/ - three-clause BSD License
- PySpin - https://pypi.python.org/pypi/pyspin - MIT
- Tox - https://tox.readthedocs.io/en/latest/ - MIT
- pytest - https://docs.pytest.org/en/latest/ - MIT
- flake8 - http://flake8.pycqa.org/en/latest/ - MIT
- venv_tools - ... - ...

License
-------

MIT
