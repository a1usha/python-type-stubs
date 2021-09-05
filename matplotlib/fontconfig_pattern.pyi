from pyparsing import Suppress as Suppress
from pyparsing import ParseException as ParseException
from pyparsing import StringEnd as StringEnd
from pyparsing import Regex as Regex
from pyparsing import Optional as Optional
from pyparsing import ZeroOrMore as ZeroOrMore
from pyparsing import Literal as Literal
from functools import lru_cache as lru_cache
from typing import Any
from typing import Callable
from typing import ClassVar
from typing import Union

from matplotlib.fontconfig_pattern import FontconfigPatternParser
from object import object

family_unescape: Union[Callable[[str, str, int], str], Callable[[Callable[[Match[str]], str], str, int], str]]
family_escape: Union[Callable[[str, str, int], str], Callable[[Callable[[Match[str]], str], str, int], str]]
value_punc: str
value_unescape: Union[Callable[[str, str, int], str], Callable[[Callable[[Match[str]], str], str, int], str]]
value_escape: Union[Callable[[str, str, int], str], Callable[[Callable[[Match[str]], str], str, int], str]]
family_punc: str


class FontconfigPatternParser(object):
    _constants: ClassVar[dict[Union[str, Any], Union[tuple[str, str], Any]]]
    _parser: Union[Union[_PendingSkip, None, And], Any]
    _properties: dict[Any, Any]
    ParseException: Type[ParseException]

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


parse_fontconfig_pattern: _lru_cache_wrapper[dict[Any, Any]]


def _escape_val(val: Any,
                escape_func: Union[Union[Callable[[str, str, int], str], Callable[
                    [Callable[[Match[str]], str], str, int], str], Callable[[str, str, int], str], Callable[
                                             [Callable[[Match[str]], str], str, int], str]], Any]) -> str: ...


def generate_fontconfig_pattern(d: {get_family}) -> str: ...