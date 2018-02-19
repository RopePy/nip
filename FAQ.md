NIP - FAQ
=========


How do I add more than one dependency at a time?
------------------------------------------------

Just list them on the command line, like so ..

```
    $ nip add click pygments crayons
```


How do I use this with pytest or tox?
-------------------------------------

Add them to your dev dependencies ..

```
    $ nip add -D pytest tox
```

- Create a `tox.ini` file with your defaults added..

```
    [tox]
    envlist = py36

    [testenv]
    deps =
        pytest

    commands =
        pip install -U pip
        py.test

    norecursedirs = python_modules .tox
```

Then add the test command to your nipfile ..


nip.json
```
    {
        ...
        "scripts": {
            ...
            "test": "tox"
        }
    }
```

And run like so ..

```
    $ nip test
```


**This FAQ is a work in Progress, feel free to make a PR with anything
you feel should be added**
