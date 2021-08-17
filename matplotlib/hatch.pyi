from typing import Any
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
    def __init__(self: HorizontalHatch,
                 hatch: {count},
                 density: Any) -> None: ...

    def set_vertices_and_codes(self: HorizontalHatch,
                               vertices: Optional[Any],
                               codes: Any) -> None: ...


class VerticalHatch(HatchPatternBase):
    def __init__(self: VerticalHatch,
                 hatch: {count},
                 density: Any) -> None: ...

    def set_vertices_and_codes(self: VerticalHatch,
                               vertices: Optional[Any],
                               codes: Any) -> None: ...


class NorthEastHatch(HatchPatternBase):
    def __init__(self: NorthEastHatch,
                 hatch: {count},
                 density: Any) -> None: ...

    def set_vertices_and_codes(self: NorthEastHatch,
                               vertices: Optional[Any],
                               codes: Any) -> None: ...


class SouthEastHatch(HatchPatternBase):
    def __init__(self: SouthEastHatch,
                 hatch: {count},
                 density: Any) -> None: ...

    def set_vertices_and_codes(self: SouthEastHatch,
                               vertices: Optional[Any],
                               codes: Any) -> None: ...


class Shapes(HatchPatternBase):
    def __init__(self: Shapes,
                 hatch: Union[{count}, {count}, {count}],
                 density: Any) -> None: ...

    def set_vertices_and_codes(self: Shapes,
                               vertices: Optional[Any],
                               codes: Any) -> None: ...


class Circles(Shapes):
    def __init__(self: Circles,
                 hatch: {count},
                 density: Any) -> None: ...


class SmallCircles(Circles):
    def __init__(self: SmallCircles,
                 hatch: {count},
                 density: Any) -> None: ...


class LargeCircles(Circles):
    def __init__(self: LargeCircles,
                 hatch: {count},
                 density: Any) -> None: ...


class SmallFilledCircles(SmallCircles):
    def __init__(self: SmallFilledCircles,
                 hatch: {count},
                 density: Any) -> None: ...


class Stars(Shapes):
    def __init__(self: Stars,
                 hatch: Union[{count}, {count}],
                 density: Any) -> None: ...


def _validate_hatch_pattern(hatch: Any) -> None: ...


def get_path(hatchpattern: {count},
             density: int = 6) -> Path: ...