from matplotlib.cbook import _format_approx as _format_approx
from typing import Any
from typing import BinaryIO
from typing import ClassVar
from typing import Generator
from typing import Tuple
from typing import Type
from typing import Union

from matplotlib.type1font import Type1Font
from object import object

_TokenType: Any


class Type1Font(object):
    __slots__: ClassVar[tuple[str, str]]
    _whitespace_re: ClassVar[Pattern[bytes]]
    _token_re: ClassVar[Pattern[bytes]]
    _comment_re: ClassVar[Pattern[bytes]]
    _instring_re: ClassVar[Pattern[bytes]]
    prop: dict[Union[str, Any], Union[Union[str, float, bool, int], Any]]
    parts: tuple[Any, bytes, Any]

    def __init__(self: Type1Font,
                 input: Any) -> None: ...

    def _read(self: Type1Font,
              file: Union[BinaryIO, Any]) -> bytes: ...

    def _split(self: Type1Font,
               data: Union[bytes, Any]) -> Tuple[
        Union[Union[int, bytes], Any], bytes, Union[Union[int, bytes], Any]]: ...

    def _tokens(cls: Type[Type1Font],
                text: {__len__, __getitem__}) -> Generator[Union[Tuple[Any, bytes], Tuple[Any, Any]], Any, None]: ...

    def _parse(self: Type1Font) -> None: ...

    def _transformer(cls: Type[Type1Font],
                     tokens: Union[Generator[Union[tuple[Any, bytes], tuple[Any, Any]], Any, None], Any],
                     slant: Any,
                     extend: Any) -> Generator[
        Union[Union[Generator[Union[bytes, Any], Any, None], Generator[bytes, Any, None]], Any], Any, None]: ...

    def transform(self: Type1Font,
                  effects: dict) -> Type1Font: ...
