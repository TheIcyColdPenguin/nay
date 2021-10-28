from typing import Union

from pathlib import Path


def readfile(filename: str, is_bin: bool = False, new_filename: str = None):
    filepath = Path(__file__).parent.parent.absolute() / 'prefabbed' / filename

    with open(filepath, 'rb' if is_bin else 'r') as f:
        contents: Union[str, bytes] = f.read()

    return (new_filename if new_filename is not None else filename, contents, is_bin)
