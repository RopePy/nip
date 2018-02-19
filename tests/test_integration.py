import os
import time
import json
import pexpect
import textwrap
from subprocess import Popen

from helpers import new_nip_project, tmpdir_context
from nip.utils.packaging import is_pinned_version


def test_nip_init(tmpdir):
    """ Creates a basic nip project """
    # Create our working directory ..
    p = tmpdir.mkdir("test-nip")

    # get our basepath
    t_path = p.dirpath()

    with tmpdir_context(t_path, "test-nip") as working_directory:

        # Create a new nip project
        project = new_nip_project(working_directory)

        # Wait for init to finish
        while project.isalive():
            time.sleep(0.2)

        # `python_modules` should exist
        actual = working_directory.join("python_modules").exists()

        expected = True
        assert actual == expected


def test_nip_init_doesnt_overwrite_files(tmpdir):
    """ Doesn't everwrite existing files in cwd """
    # Create a directory with a file in it ..
    p = tmpdir.mkdir("test-nip").join("somefile.txt")
    old_cwd = os.getcwd()

    # get our basepath
    t_path = p.dirpath()

    # chdir() to basepath
    os.chdir(t_path)

    os.system("nip init")

    # `python_modules` should _not_ exist ..
    actual = t_path.join("python_modules").exists()

    expected = False
    assert actual == expected

    # restore cwd
    os.chdir(old_cwd)


def test_nip_add(tmpdir):
    # Create our working directory ..
    p = tmpdir.mkdir("test-nip")

    # get our basepath
    t_path = p.dirpath()

    # with basepath as working_directory
    with tmpdir_context(t_path, "test-nip") as working_directory:

        # Create a new nip project
        new_nip_project(working_directory)

        ''' Add single package and wait to finish '''
        nip_add = Popen("nip add kuai".split(' '), cwd=working_directory)
        nip_add.wait()

        ''' Make sure it was added to the nipfile .. '''
        with open(t_path.join("test-nip").join("nip.json")) as fp:
            nipfile = json.load(fp)
            actual = is_pinned_version(nipfile['dependencies']['kuai'])

        expected = True
        assert actual == expected

        ''' Make sure it was added to the requirements.txt .. '''
        with open(t_path.join("test-nip").join("requirements.txt")) as fp:
            lines = fp.readlines()
            # filter out the correct line
            line = filter(lambda r: r.startswith('kuai'), lines)
            # clip the package name
            version = next(line)[len('kuai'):]
            actual = is_pinned_version(version)

        expected = True
        assert actual == expected

        ''' Run a script using the new dependency ... '''
        script = textwrap.dedent("""
            from kuai import Kuai

            def hello(to):
                print('Hello', to)

            Kuai.on('greet', hello)
            Kuai.emit('greet', 'testers!')

            exit(0)
        """.strip("\n"))

        # Create and write the script to file
        with open(os.path.join(working_directory, "test.py"), 'w+') as fp:
            fp.write(script)

        # Add the script to the nipfile
        with open(t_path.join("test-nip").join("nip.json"), 'w') as fp:
            nipfile['scripts'] = {"start": "python test.py"}
            fp.write(json.dumps(nipfile, indent=2))

        child = pexpect.spawn("nip run start", cwd=working_directory)
        e_code = child.wait()

        # Should be no error code
        assert e_code == 0

        # The shortcut version should also work
        child2 = pexpect.spawn("nip start", cwd=working_directory)
        e_code = child2.wait()

        # Should be no error code
        assert e_code == 0
        assert "Hello testers!" in str(child2.readlines())

        """ Add multiple packages in one command """
        nip_add = Popen("nip add flask falsy".split(' '),
                        cwd=working_directory)
        nip_add.wait()

        ''' Make sure they were added to the nipfile .. '''
        with open(t_path.join("test-nip").join("nip.json")) as fp:
            nipfile = fp.read()
            # do a string search for the package names
            predicate = "flask" in nipfile and "falsy" in nipfile
            actual = True if predicate else False

        expected = True
        assert actual == expected

        ''' Add a dev_dependency ... '''
        nip_add = Popen("nip add -D flake8".split(' '),
                        cwd=working_directory)
        nip_add.wait()

        ''' Make sure it was added to the nipfile .. '''
        with open(t_path.join("test-nip").join("nip.json")) as fp:
            nipfile = json.load(fp)
            actual = is_pinned_version(nipfile['dev_dependencies']['flake8'])

        expected = True
        assert actual == expected

        ''' Make sure it was added to the requirements_dev.txt .. '''
        with open(t_path.join("test-nip").join("requirements_dev.txt")) as f:
            lines = f.readlines()
            # filter out the correct line
            line = filter(lambda r: r.startswith('flake8'), lines)
            # clip the package name
            version = next(line)[len('flake8'):]
            actual = is_pinned_version(version)

        expected = True
        assert actual == expected
