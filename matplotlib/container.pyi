from matplotlib.artist import Artist as Artist
from typing import Any
from typing import ClassVar
from typing import Container
from typing import Iterable
from typing import Type
from typing import Union

from matplotlib.container import BarContainer
from matplotlib.container import Container
from matplotlib.container import ErrorbarContainer
from matplotlib.container import StemContainer
from tuple import tuple


class Container(tuple):
    get_label: ClassVar[Callable[[], str]]
    set_label: ClassVar[Callable[[object], None]]
    add_callback: ClassVar[Callable[[Callable], int]]
    remove_callback: ClassVar[Callable[[Any], None]]
    pchanged: ClassVar[Callable[[], None]]
    _remove_method: None
    _callbacks: CallbackRegistry

    def __repr__(self: Container) -> str: ...

    def __new__(cls: Type[Container],
                *args,
                **kwargs) -> _T: ...

    def __init__(self: Container,
                 kl: Union[Union[Iterable, tuple], Any],
                 label: Any = None) -> None: ...

    def remove(self: Container) -> None: ...

    def get_children(self: Container) -> list[Optional[Any]]: ...


class BarContainer(Container):
    orientation: Any
    datavalues: Any
    patches: Any
    errorbar: Any

    def __init__(self: BarContainer,
                 patches: Any,
                 errorbar: Any = None,
                 *,
                 datavalues: Any = None,
                 orientation: Any = None,
                 **kwargs) -> None: ...


class ErrorbarContainer(Container):
    has_xerr: bool
    has_yerr: bool
    lines: Any

    def __init__(self: ErrorbarContainer,
                 lines: Any,
                 has_xerr: bool = False,
                 has_yerr: bool = False,
                 **kwargs) -> None: ...


class StemContainer(Container):
    markerline: Any
    stemlines: Any
    baseline: Any

    def __init__(self: StemContainer,
                 markerline_stemlines_baseline: Union[Iterable, tuple],
                 **kwargs) -> None: ...
