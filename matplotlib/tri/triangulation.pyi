from typing import Any
from typing import Optional
from typing import Tuple
from typing import Union

from matplotlib.tri.triangulation import Triangulation
from matplotlib.tri.trifinder import TrapezoidMapTriFinder
from object import object


class Triangulation(object):
    triangles: Any
    _trifinder: None
    x: Any
    is_delaunay: bool
    y: Any
    _neighbors: Any
    _cpp_triangulation: None
    _edges: None
    mask: Any

    def __init__(self: Triangulation,
                 x: Any,
                 y: Any,
                 triangles: Optional[int] = None,
                 mask: Any = None) -> Any: ...

    def calculate_plane_coefficients(self: Triangulation,
                                     z: Any) -> Any: ...

    def edges(self: Triangulation) -> Any: ...

    def get_cpp_triangulation(self: Triangulation) -> Any: ...

    def get_masked_triangles(self: Triangulation) -> Any: ...

    def get_from_args_and_kwargs(*args,
                                 **kwargs) -> Tuple[Union[Triangulation, Any], Any, dict[str, Any]]: ...

    def get_trifinder(self: Triangulation) -> Union[TrapezoidMapTriFinder, Any]: ...

    def neighbors(self: Triangulation) -> Any: ...

    def set_mask(self: Triangulation,
                 mask: Any) -> Any: ...
