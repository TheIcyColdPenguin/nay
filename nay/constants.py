from typing import Dict

from custom_types import Runnable

from templates import html, readfile

projects: Dict[str, Runnable] = {
    'glsl': {
        'help_str': 'Generates a simple GLSL based project',
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
''')
        ]
    },
    'c++': {
        'help_str': 'Generates a basic C++ project structure',
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

            'mkdir src/includes'
        ]
    },
}
