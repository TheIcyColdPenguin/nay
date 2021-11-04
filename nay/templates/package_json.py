from typing import List


def package_json(
        name: str = 'package.json',
        main: str = 'build/index.js',
        module: bool = True,
        scripts: List[str] = []
):
    return (
        name,
        '''{
    "name": "app_name",
    "version": "1.0.0",
    "description": "app_description",
    ''' + (f'"main": "{main}",' if main else '') + '''
    ''' + ('"type": "module",' if module else '') + '''
    "repository": "repository_url",
    "author": "author",
    "license": "MIT",
    "private": true,
    "dependencies": {},
    "devDependencies": {},
    "scripts": {
        '''+',\n        '.join(scripts) + '''
    }
}
''',
        False
    )
