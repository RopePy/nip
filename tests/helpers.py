import os
import time
from contextlib import contextmanager

import pexpect


@contextmanager
def tmpdir_context(t_path, name):
    # store the original path
    old_cwd = os.getcwd()

    # chdir() to our working directory
    working_directory = t_path.join(name)
    os.chdir(working_directory)

    yield working_directory

    # restore the original path
    os.chdir(old_cwd)


def new_nip_project(working_directory):
    """ Helper for created a bare project """
    child = pexpect.spawn("nip init", cwd=working_directory)
    # 'Package Name (test-nip):'
    child.sendline("")
    # 'Author:'
    child.sendline("")
    # 'Version:'
    child.sendline("")
    # 'License (MIT):'
    child.sendline("")

    # Wait for init to finish
    while child.isalive():
        time.sleep(0.2)

    return child
