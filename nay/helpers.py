from .constants import projects

RED = '\033[0;31m'
GREEN = '\033[0;32m'
BLUE = '\033[0;34m'
BOLD = '\033[1m'
CLEAR = '\033[0m'


def red(*args):
    print(RED+' '.join(args)+CLEAR)


def green(*args):
    print(GREEN+' '.join(args)+CLEAR)


def blue(*args):
    print(BLUE+' '.join(args)+CLEAR)


def bold(*args):
    print(BOLD+' '.join(args)+CLEAR)


def usage():
    print('Usage -\n')
    print('nay -h | --help                     : This help message is displayed')
    print('nay <project-type> <path-to-folder> : The given project boilerplate will be generated')
    print('\nAll projects - \n')
    for k, v in projects.items():
        print(k, ':', v['help_str'])
