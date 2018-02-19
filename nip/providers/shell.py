import os
from subprocess import call


def call_command(command):
    return call(command, shell=True)


def call_command_from_cwd(command):
    return call(command, cwd=os.getcwd(), shell=True)
