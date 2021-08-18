from typing import Any
from typing import Optional
from typing import Tuple
from typing import Union

from matplotlib._tri import Triangulation
from matplotlib.tri.triangulation import Triangulation
from matplotlib.tri.trifinder import TrapezoidMapTriFinder
from numpy.core._multiarray_umath import ndarray
from object import object


class Triangulation(object):
    def __init__(self: Triangulation,
                 x: Any,
                 y: Any,
                 triangles: Optional[int] = None,
                 mask: Any = None) -> Any: ...

    def calculate_plane_coefficients(self: Triangulation,
                                     z: Any) -> None: ...

    def edges(self: Triangulation) -> Optional[Any]: ...

    def get_cpp_triangulation(self: Triangulation) -> Union[Triangulation, Any]: ...

    def get_masked_triangles(self: Triangulation) -> Optional[ndarray]: ...

    def get_from_args_and_kwargs(*args,
                                 **kwargs) -> Tuple[Union[Triangulation, Any], Any, dict[str, Any]]: ...

    def get_trifinder(self: Triangulation) -> Union[TrapezoidMapTriFinder, Any]: ...

    def neighbors(self: Triangulation) -> Optional[Any]: ...

    def set_mask(self: Triangulation,
                 mask: Any) -> Any: ...
