from typing import Any
from typing import BinaryIO
from typing import Generator
from typing import Tuple
from typing import Type

from matplotlib.type1font import Type1Font
from object import object


class Type1Font(object):
    def __init__(self: Type1Font,
                 input: Any) -> None: ...

    def _read(self: Type1Font,
              file: BinaryIO) -> bytes: ...

    def _split(self: Type1Font,
               data: bytes) -> Tuple[Union[int, bytes], bytes, Union[int, bytes]]: ...

    def _tokens(cls: Type[Type1Font],
                text: {__len__, __getitem__}) -> Generator[Union[Tuple[Any, bytes], Tuple[Any, Any]], Any, None]: ...

    def _parse(self: Type1Font) -> None: ...

    def _transformer(cls: Type[Type1Font],
                     tokens: Generator[Union[tuple[Any, bytes], tuple[Any, Any]], Any, None],
                     slant: Any,
                     extend: Any) -> Generator[
        Union[Generator[bytes, Any, None], Generator[bytes, Any, None]], Any, None]: ...

    def transform(self: Type1Font,
                  effects: dict) -> Type1Font: ...
