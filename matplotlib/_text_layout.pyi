from ft2font import LOAD_NO_HINTING as LOAD_NO_HINTING
from ft2font import KERNING_DEFAULT as KERNING_DEFAULT
from typing import Generator

LayoutItem: Union[
    Callable[[{__module__, __mro__, __dict__}], {__module__, __mro__, __dict__}], {__module__, __mro__, __dict__}]
from typing import Any


def layout(string: str,
           font: Any,
           *,
           kern_mode: int = KERNING_DEFAULT) -> Generator[{__module__, __mro__, __dict__}, Any, None]: ...