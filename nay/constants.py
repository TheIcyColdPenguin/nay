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
    }
}
