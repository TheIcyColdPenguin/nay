import sys
import os

from .helpers import bold, green, red, usage
from .constants import projects


def run(project_key: str, path: str):
    if project_key.lower() not in projects:
        red('Unkown project name\n')
        usage()
        return 1

    project = projects[project_key.lower()]

    target_dir = os.path.abspath(path)

    if os.path.exists(target_dir):
        if not os.path.isdir(target_dir):
            red('The given path is not a folder')
            return 1

        if any(os.scandir(target_dir)):
            red('The given path is a non-empty folder')
            return 1

    else:
        os.makedirs(target_dir)

    os.chdir(target_dir)

    for command in project['commands']:
        if isinstance(command, str):
            bold(f'Running `{command}` ....')
            os.system(command)
        else:
            filename, filecontents, is_bin = command()

            bold(f'Generating file `{filename}` ....')

            with open(filename, 'wb' if is_bin else 'w') as f:
                f.write(filecontents)

    green('Completed!')
    return 0


def nay():

    if len(sys.argv) > 1 and sys.argv[1].lower() in ('-h', '--help'):
        usage()
        return 1

    if len(sys.argv) < 3:
        usage()
        return 1

    return run(sys.argv[1], sys.argv[2])
