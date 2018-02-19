Assertions
----------

- ✓ Runs on Python ^3.6
- ✓ Installs without crashing
- Completes the Quick Start guide
- ✓ `nip init` doesn't everwrite existing files in cwd
- ✓ `nip add` handles multiple packages in one command
- ✓ Installed packages have their versions pinned in the `nipfile` and `requirements[_env].txt` file
- ✓ `nip add` puts packages in the correct `requirements[_env].txt`
- ✓ `nip_remove` removes packages from the correct `requirements[_env].txt` and `nipfile`

- Adds packages by specified version
- `nip install` ignores dev dependencies in `production` mode
- Runs scripts from the `nip.json` file in venv
- Passes along `run` args to script commands
- Runs `nip install` when no args provided
- Runs `nip <argument>` as `nip run <argument>` if `argument` is not an existing nip command.


Under Consideration
-------------------

- Runs on Python 2.7
