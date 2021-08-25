from matplotlib.path import Path as Path
from matplotlib import _api as _api
from typing import Any
from typing import ClassVar
from typing import Optional
from typing import Union

from matplotlib.hatch import Circles
from matplotlib.hatch import HorizontalHatch
from matplotlib.hatch import LargeCircles
from matplotlib.hatch import NorthEastHatch
from matplotlib.hatch import Shapes
from matplotlib.hatch import SmallCircles
from matplotlib.hatch import SmallFilledCircles
from matplotlib.hatch import SouthEastHatch
from matplotlib.hatch import Stars
from matplotlib.hatch import VerticalHatch
from matplotlib.path import Path
from object import object


class HatchPatternBase(object):
    pass


class HorizontalHatch(HatchPatternBase):
    num_vertices: int
    num_lines: int

    def __init__(self: HorizontalHatch,
                 hatch: {count},
                 density: Any) -> None: ...

    def set_vertices_and_codes(self: HorizontalHatch,
                               vertices: Optional[Any],
                               codes: Any) -> None: ...


class VerticalHatch(HatchPatternBase):
    num_vertices: int
    num_lines: int

    def __init__(self: VerticalHatch,
                 hatch: {count},
                 density: Any) -> None: ...

    def set_vertices_and_codes(self: VerticalHatch,
                               vertices: Optional[Any],
                               codes: Any) -> None: ...


class NorthEastHatch(HatchPatternBase):
    num_vertices: int
    num_lines: int

    def __init__(self: NorthEastHatch,
                 hatch: {count},
                 density: Any) -> None: ...

    def set_vertices_and_codes(self: NorthEastHatch,
                               vertices: Optional[Any],
                               codes: Any) -> None: ...


class SouthEastHatch(HatchPatternBase):
    num_vertices: int
    num_lines: int

    def __init__(self: SouthEastHatch,
                 hatch: {count},
                 density: Any) -> None: ...

    def set_vertices_and_codes(self: SouthEastHatch,
                               vertices: Optional[Any],
                               codes: Any) -> None: ...


class Shapes(HatchPatternBase):
    filled: ClassVar[bool]
    num_shapes: Union[int, Any]
    num_vertices: Union[int, Any]

    def __init__(self: Shapes,
                 hatch: Union[Union[{count}, {count}, {count}], Any],
                 density: Any) -> None: ...

    def set_vertices_and_codes(self: Shapes,
                               vertices: Optional[Any],
                               codes: Any) -> None: ...


class Circles(Shapes):
    shape_vertices: ndarray
    shape_codes: Optional[ndarray]

    def __init__(self: Circles,
                 hatch: Union[{count}, Any],
                 density: Any) -> None: ...


class SmallCircles(Circles):
    size: ClassVar[float]
    num_rows: Any

    def __init__(self: SmallCircles,
                 hatch: Union[{count}, Any],
                 density: Any) -> None: ...


class LargeCircles(Circles):
    size: ClassVar[float]
    num_rows: Any

    def __init__(self: LargeCircles,
                 hatch: Union[{count}, Any],
                 density: Any) -> None: ...


class SmallFilledCircles(SmallCircles):
    size: ClassVar[float]
    filled: ClassVar[bool]
    num_rows: Any

    def __init__(self: SmallFilledCircles,
                 hatch: Union[{count}, Any],
                 density: Any) -> None: ...


class Stars(Shapes):
    size: ClassVar[float]
    filled: ClassVar[bool]
    shape_vertices: ndarray
    shape_codes: ndarray
    num_rows: Any

    def __init__(self: Stars,
                 hatch: Union[Union[{count}, {count}], Any],
                 density: Any) -> None: ...


_hatch_types: list[Type[Union[
    HorizontalHatch, VerticalHatch, NorthEastHatch, SouthEastHatch, SmallCircles, LargeCircles, SmallFilledCircles, Stars]]]


def _validate_hatch_pattern(hatch: Any) -> None: ...


def get_path(hatchpattern: {count},
             density: int = 6) -> Path: ...