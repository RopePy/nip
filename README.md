nip isn't pip
=============

  NIP - nip isn't pip

Core framework for RopePy. NIP is a service based framework
used for quickly building applications with a middleware
and hooks based architecture using the Click CLI framework.

Heavily inspired by NPM/Yarn and the FeathersJS architecture.


What is it?
-----------

The fastest way to start and use a python project within a virtual
environment, providing a no config means to run and write Python
applications without the hassle of manually sourcing in and out
of the virtual environment yourself. Simply enter an empty directory,
type `nip init` and a virtual environment is spun up for you auto-
matically and put inside your directory under `python_modules`, a
`nip.json` file is also created with your package details provided
during the init script. You may now place shortcuts to scripts in
this `nipfile` under a scripts section (see example) which can be
started with `nip run <script_name>`, and will be run under your
virtual environment.


Why?
----

There are lots other package managers that do similar things, but
nip is created as a framework to make doing these things easier.
And to help improve the development cycle of adding and fixing
features/bugs, way faster than using standard APIs. While still
being able to use those same APIs under the hood to do the work
they were build to do.


Commands
--------

  > add -     Pip isn't bad but neither is nip add

  > init -    Not a bit like pip init

  > install - This ain't at all like the old pip install

  > remove -  Yeah, this one just removes packages ..

  > run -     Python is fun and so is nip run

Example
-------

```sh

    $ nip init
    nip - v0.1.0 - Init - Made with Love, by Duroktar © 2017

    Package Name: my_awesome_package
    Author: Scott Doucet
    License (MIT): MIT
    ⠋ Initialising.... Done.
    Finished.

    $ cat 'print("Hello world!!")' >> hello_world.py
```

> nip.json

```
    {
        "name": "my_awesome_package",
        "author": "Scott Doucet",
        "license": "MIT",
        "scripts": {
            "start": "python hello_world.py"
        }
    }
```

```sh
    $ nip run start
    nip - v0.1.0 - Run

    Hello world!!

    $
```


Third Party Packages
--------------------

Click - http://click.pocoo.org/5/ - three-clause BSD License
PySpin - https://pypi.python.org/pypi/pyspin - MIT
Tox - https://tox.readthedocs.io/en/latest/ - MIT
pytest - https://docs.pytest.org/en/latest/ - MIT
flake8 - http://flake8.pycqa.org/en/latest/ - MIT

License
-------

MIT
