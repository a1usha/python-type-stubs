from typing import Any
from typing import Iterable
from typing import Union
from typing import tuple


class Container(tuple):
    def __repr__(self: Container) -> str: ...

    def __new__(cls: Type[Container],
                *args,
                **kwargs) -> _T: ...

    def __init__(self: Container,
                 kl: Union[Iterable, tuple],
                 label: Any = None) -> None: ...

    def remove(self: Container) -> None: ...

    def get_children(self: Container) -> list[Optional[Any]]: ...


class StemContainer(Container):
    def __init__(self: StemContainer,
                 markerline_stemlines_baseline: Union[Iterable, tuple],
                 **kwargs) -> None: ...


class ErrorbarContainer(Container):
    def __init__(self: ErrorbarContainer,
                 lines: Any,
                 has_xerr: bool = False,
                 has_yerr: bool = False,
                 **kwargs) -> None: ...


class BarContainer(Container):
    def __init__(self: BarContainer,
                 patches: Any,
                 errorbar: Any = None,
                 datavalues: Any = None,
                 orientation: Any = None,
                 **kwargs) -> None: ...
