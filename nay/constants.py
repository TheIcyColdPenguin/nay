from typing import List

from custom_types import Runnable

from templates import html, readfile

projects: List[Runnable] = [
    {
        'names': ['glsl'],
        'help_str': 'A simple GLSL based project',
        'commands': [
            lambda:readfile('index.glsl'),
            lambda:readfile('bg.png', is_bin=True),
            lambda:readfile('GlslCanvas.js'),
            lambda:html(title='GLSL', body='''
<canvas
    class="glslCanvas"
    data-fragment-url="index.glsl"
    data-textures="bg.png"
    width="500"
    height="500"
></canvas>
<script src="GlslCanvas.js"></script>
'''),
        ],
    },
    {
        'names': ['cpp', 'c++'],
        'help_str': 'A basic C++ project structure',
        'commands': [
            'mkdir .vscode',
            lambda:readfile(
                'c_cpp_properties.json',
                new_filename='.vscode/c_cpp_properties.json'
            ),
            lambda:readfile('launch.json', new_filename='.vscode/launch.json'),
            lambda:readfile('tasks.json', new_filename='.vscode/tasks.json'),

            'mkdir src',
            lambda:readfile('main.cpp', new_filename='src/main.cpp'),

            'mkdir src/includes',
        ],
    },
    {
        'names': ['typescript', 'ts'],
        'help_str':'A simple Typescript project',
        'commands':[
            lambda:readfile('package.json'),
            lambda:readfile('nodemon.json'),
            lambda:readfile('tsconfig.json'),

            'mkdir src',
            lambda:(
                'src/index.ts',
                'console.log("Hello world");\n export {}',
                False
            )
        ],
    },

]
