from typing import Any
from typing import Union


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


def generate_fontconfig_pattern(d: {get_family}) -> str: ...


def _escape_val(val: Any,
                escape_func: Union[(repl: str, string: str, count: int)) -> str: ...