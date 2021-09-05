from ft2font import LOAD_NO_HINTING as LOAD_NO_HINTING
from ft2font import KERNING_DEFAULT as KERNING_DEFAULT
from typing import Any
from typing import Generator

LayoutItem: type


def layout(string: str,
           font: Any,
           *,
           kern_mode: int = KERNING_DEFAULT) -> Generator[Any, Any, None]: ...