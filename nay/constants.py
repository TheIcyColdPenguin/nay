from typing import List

from custom_types import Runnable

from templates import html, readfile, package_json

projects: List[Runnable] = [
    {
        'names': ['glsl'],
        'help_str': 'A simple GLSL based project',
        'commands': [
            lambda:readfile('index.glsl'),
            lambda:readfile('bg.png', is_bin=True),
            lambda:readfile('GlslCanvas.js'),
            lambda:html(
                title='GLSL',
                style='''
            html,
            body {
                margin: 0;
                height: 100%;
            }
            body {
                display: grid;
                place-items: center;
            }
        ''',
                body='''
        <canvas
            class="glslCanvas"
            data-fragment-url="index.glsl"
            data-textures="bg.png"
            width="500"
            height="500"
        ></canvas>
        <script src="GlslCanvas.js"></script>
    '''
            ),
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

            'mkdir src',  # NOSONAR
            lambda:readfile('main.cpp', new_filename='src/main.cpp'),

            'mkdir src/includes',
        ],
    },
    {
        'names': ['typescript', 'ts'],
        'help_str':'A simple Typescript project',
        'commands':[
            lambda:package_json(
                scripts=[
                    '"build": "tsc"',
                    '"start": "node ."',
                    '"build:start": "tsc && node ."',
                    '"dev": "nodemon"'
                ]
            ),
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
    {
        'names': ['discord.py', 'd.py'],
        'help_str':'A starter discord.py project',
        'commands':[
            'python3 -m venv venv',
            (
                '. venv/bin/activate'
                ' && pip install python-dotenv discord.py'
                ' && pip freeze > requirements.txt'
            ),
            lambda:readfile('discord_main.py', new_filename='main.py'),
            lambda:(
                'envconfig.py',
                'from dotenv import load_dotenv\nload_dotenv()',
                False
            ),
            lambda:('.env', 'TOKEN=', False),
        ],
    },
    {
        'names': ['ts-web', 'ts-webpack'],
        'help_str':'A boilerplate typescript web project bundled by webpack',
        'commands':[
            'mkdir dist',
            'mkdir src',

            lambda:readfile('webpack.config.js'),
            lambda:readfile(
                'webpack-tsconfig.json',
                new_filename='tsconfig.json'
            ),
            lambda:package_json(
                main='',
                module=False,
                scripts=[
                    '"build": "webpack"',
                    '"dev": "webpack serve --open"'
                ]
            ),

            lambda:('src/index.ts', 'export {}', False),
            lambda:('.gitignore', 'dist/*\n!dist/index.html', False),

            lambda: html(
                name='dist/index.html',
                body='\n        <script src="./bundle.js"></script>\n    '
            ),

            'yarn add -D webpack webpack-dev-server webpack-cli typescript ts-loader',
        ],
    },
    {
        'names': ['rust-wasm-web'],
        'help_str':'A boilerplate Rust wasm web project bundled by vite',
        'commands': [
            'yarn create vite . --template vanilla-ts',
            'yarn',
            'yarn add vite vite-plugin-wasm-pack -D',
            'cargo init --lib innards',

            lambda:('Cargo.toml', '[workspace]\nmembers = ["innards"]', False),
            lambda:readfile('vite.config.ts'),
            lambda:readfile('main.ts', new_filename='src/main.ts'),
            lambda:readfile('lib.rs', new_filename='innards/src/lib.rs'),

            (
                '''cd innards && printf '\\n\\n[lib]\\ncrate-type = ["cdylib"]' >> Cargo.toml && '''
                'cargo add wasm-bindgen && cargo add console_error_panic_hook && cd ..'
            ),

            'printf "\\n\\ntarget" >> .gitignore',
            'rm public/vite.svg src/counter.ts src/typescript.svg',
            'wasm-pack build ./innards --target web'

        ],
    },
]
