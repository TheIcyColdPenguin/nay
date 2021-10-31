from typing import List, Callable, Literal, Tuple, TypedDict, Union

CommandReturnType = Union[
    Tuple[str, str, Literal[False]],
    Tuple[str, bytes, Literal[True]]
]


class Runnable(TypedDict):
    commands: List[Union[str, Callable[[], CommandReturnType]]]
    help_str: str
