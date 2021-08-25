from matplotlib import docstring as docstring
from matplotlib import cbook as cbook
from enum import auto as auto
from enum import Enum as Enum
from enum import Enum
from typing import Any
from typing import ClassVar

from matplotlib._enums import CapStyle
from matplotlib._enums import JoinStyle
from matplotlib._enums import _AutoStringNameEnum
from str import str


class _AutoStringNameEnum(Enum):
    def _generate_next_value_(name: _AutoStringNameEnum,
                              start: Any,
                              count: Any,
                              last_values: Any) -> _AutoStringNameEnum: ...

    def __hash__(self: _AutoStringNameEnum) -> int: ...


def _deprecate_case_insensitive_join_cap(s: {lower, __ne__}) -> Any: ...


class JoinStyle(str, _AutoStringNameEnum):
    miter: ClassVar[JoinStyle]
    round: ClassVar[JoinStyle]
    bevel: ClassVar[JoinStyle]

    def __init__(self: JoinStyle,
                 s: Any) -> None: ...

    def demo() -> None: ...


input_description: str
input_description: str


class CapStyle(str, _AutoStringNameEnum):
    butt: ClassVar[CapStyle]
    projecting: ClassVar[CapStyle]
    round: ClassVar[CapStyle]

    def __init__(self: CapStyle,
                 s: Any) -> None: ...

    def demo() -> None: ...


input_description: str
input_description: str
