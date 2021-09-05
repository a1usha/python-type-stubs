from matplotlib.tri import Triangulation as Triangulation
from matplotlib import _api as _api
from typing import Any
from typing import Union

from matplotlib.tri.trifinder import TrapezoidMapTriFinder
from matplotlib.tri.trifinder import TriFinder
from object import object


class TriFinder(object):
    _triangulation: Union[{get_cpp_triangulation}, Any]

    def __init__(self: TriFinder,
                 triangulation: Union[{get_cpp_triangulation}, Any]) -> None: ...


class TrapezoidMapTriFinder(TriFinder):
    _cpp_trifinder: Any

    def __init__(self: TrapezoidMapTriFinder,
                 triangulation: {get_cpp_triangulation}) -> None: ...

    def __call__(self: TrapezoidMapTriFinder,
                 x: Any,
                 y: Any) -> Any: ...

    def _get_tree_stats(self: TrapezoidMapTriFinder) -> Any: ...

    def _initialize(self: TrapezoidMapTriFinder) -> None: ...

    def _print_tree(self: TrapezoidMapTriFinder) -> None: ...
