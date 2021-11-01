def html(name: str = 'index.html', body: str = '', style: str = '', title: str = 'Document'):
    return (
        name,
        f'''<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>{title}</title>
        <style>{style}</style>
    </head>
    <body>{body}</body>
</html>
''',
        False
    )
