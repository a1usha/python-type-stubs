from typing import Any
from typing import Callable
from typing import Union

from matplotlib.fontconfig_pattern import FontconfigPatternParser
from object import object


class FontconfigPatternParser(object):
    def __init__(self: FontconfigPatternParser) -> None: ...

    def parse(self: FontconfigPatternParser,
              pattern: Any) -> dict[Any, Any]: ...

    def _family(self: FontconfigPatternParser,
                s: Any,
                loc: Any,
                tokens: {__getitem__}) -> list[str]: ...

    def _size(self: FontconfigPatternParser,
              s: Any,
              loc: Any,
              tokens: {__getitem__}) -> list[float]: ...

    def _name(self: FontconfigPatternParser,
              s: Any,
              loc: Any,
              tokens: {__getitem__}) -> list[str]: ...

    def _value(self: FontconfigPatternParser,
               s: Any,
               loc: Any,
               tokens: {__getitem__}) -> list[str]: ...

    def _families(self: FontconfigPatternParser,
                  s: Any,
                  loc: Any,
                  tokens: Any) -> list[Any]: ...

    def _point_sizes(self: FontconfigPatternParser,
                     s: Any,
                     loc: Any,
                     tokens: Any) -> list[Any]: ...

    def _property(self: FontconfigPatternParser,
                  s: Any,
                  loc: Any,
                  tokens: {__len__}) -> list[Any]: ...


def _escape_val(val: Any,
                escape_func: Union[Union[Callable[[str, str, int], str], Callable[
                    [Callable[[Match[str]], str], str, int], str], Callable[[str, str, int], str], Callable[
                                             [Callable[[Match[str]], str], str, int], str]], Any]) -> str: ...


def generate_fontconfig_pattern(d: {get_family}) -> str: ...