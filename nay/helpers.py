from typing import Union
from custom_types import Runnable

from constants import projects

RED = '\033[0;31m'
GREEN = '\033[0;32m'
BLUE = '\033[0;34m'
BOLD = '\033[1m'
CLEAR = '\033[0m'


def red(*args, **kwargs):
    print(RED+' '.join(args)+CLEAR, **kwargs)


def green(*args, **kwargs):
    print(GREEN+' '.join(args)+CLEAR, **kwargs)


def blue(*args, **kwargs):
    print(BLUE+' '.join(args)+CLEAR, **kwargs)


def bold(*args, **kwargs):
    print(BOLD+' '.join(args)+CLEAR, **kwargs)


def usage():
    bold('Usage -')

    green('nay -h | --help                     ', end='')
    print(': ', end='')
    bold('This help message is displayed')

    green('nay <project-type> <path-to-folder> ', end='')
    print(': ', end='')
    bold('The given project boilerplate will be generated')

    bold('\nAll projects -')
    for project in projects:
        green(
            f"{CLEAR} | {GREEN}".join(project["names"])
            if len(project['names']) > 1
            else project['names'][0],
            end=''
        )
        print(' : ', end='')
        bold(project['help_str'])


def find_project(projectname: str) -> Union[Runnable, None]:
    for project in projects:
        for name in project['names']:
            if name.lower() == projectname.lower():
                return project
    return None
