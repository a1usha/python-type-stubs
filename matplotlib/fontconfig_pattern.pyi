from typing import Any
from typing import Union

from matplotlib.fontconfig_pattern import FontconfigPatternParser
from object import object


class FontconfigPatternParser(object):
    def __init__(self: FontconfigPatternParser) -> None: ...

    def parse(self: FontconfigPatternParser,
              pattern: Any) -> dict: ...

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
                  tokens: Any) -> list: ...

    def _point_sizes(self: FontconfigPatternParser,
                     s: Any,
                     loc: Any,
                     tokens: Any) -> list: ...

    def _property(self: FontconfigPatternParser,
                  s: Any,
                  loc: Any,
                  tokens: {__len__}) -> list: ...


def _escape_val(val: Any,
                escape_func: Union[(repl: str, string: str, count: int)) -> str: ...


def generate_fontconfig_pattern(d: {get_family}) -> str: ...