from matplotlib.tri.triangulation import Triangulation as Triangulation
from matplotlib import _api as _api
from typing import Any
from typing import Tuple
from typing import Union

from matplotlib.tri.triangulation import Triangulation
from matplotlib.tri.trirefine import TriRefiner
from matplotlib.tri.trirefine import UniformTriRefiner
from object import object


class TriRefiner(object):
    _triangulation: Any

    def __init__(self: TriRefiner,
                 triangulation: Any) -> None: ...


class UniformTriRefiner(TriRefiner):
    def __init__(self: UniformTriRefiner,
                 triangulation: Any) -> None: ...

    def refine_triangulation(self: UniformTriRefiner,
                             return_tri_index: bool = False,
                             subdiv: int = 3) -> Any: ...

    def refine_field(self: UniformTriRefiner,
                     z: Any,
                     triinterpolator: Any = None,
                     subdiv: int = 3) -> Any: ...

    def _refine_triangulation_once(triangulation: {x, y, neighbors, triangles, mask},
                                   ancestors: Any = None) -> Union[Triangulation, Tuple[Triangulation, ndarray]]: ...
