from typing import Any
from typing import Iterable
from typing import Optional
from typing import Union

from matplotlib.axes._base import _AxesBase
from matplotlib.axes._secondary_axes import SecondaryAxis


class SecondaryAxis(_AxesBase):
    def __init__(self: SecondaryAxis,
                 parent: Any,
                 orientation: Any,
                 location: Any,
                 functions: Any,
                 **kwargs) -> None: ...

    def set_alignment(self: SecondaryAxis,
                      align: str) -> None: ...

    def set_location(self: SecondaryAxis,
                     location: str) -> Any: ...

    def apply_aspect(self: SecondaryAxis,
                     position: Optional[{height, width}] = None) -> None: ...

    def set_ticks(self: SecondaryAxis,
                  ticks: Iterable,
                  *,
                  minor: bool = False) -> Union[list[Any], Any]: ...

    def set_functions(self: SecondaryAxis,
                      functions: Any) -> Any: ...

    def draw(self: SecondaryAxis,
             *args,
             **kwargs) -> None: ...

    def _set_scale(self: SecondaryAxis) -> None: ...

    def _set_lims(self: SecondaryAxis) -> None: ...

    def set_aspect(self: SecondaryAxis,
                   *args,
                   **kwargs) -> None: ...

    def set_color(self: SecondaryAxis,
                  color: Any) -> None: ...
