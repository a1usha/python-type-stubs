from matplotlib.tri.trifinder import TrapezoidMapTriFinder
from matplotlib.tri.trifinder import TriFinder
from object import object


class TriFinder(object):
    def __init__(self: TriFinder,
                 triangulation: {get_cpp_triangulation}) -> None: ...


class TrapezoidMapTriFinder(TriFinder):
    def __init__(self: TrapezoidMapTriFinder,
                 triangulation: {get_cpp_triangulation}) -> None: ...

    def __call__(self: TrapezoidMapTriFinder,
                 x: Any,
                 y: Any) -> Any: ...

    def _get_tree_stats(self: TrapezoidMapTriFinder) -> None: ...

    def _initialize(self: TrapezoidMapTriFinder) -> None: ...

    def _print_tree(self: TrapezoidMapTriFinder) -> None: ...
