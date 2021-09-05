from matplotlib.tri.triangulation import Triangulation as Triangulation
from matplotlib.contour import ContourSet as ContourSet
from matplotlib import docstring as docstring
from typing import Any
from typing import Tuple
from typing import Union

from matplotlib.contour import ContourSet
from matplotlib.tri.tricontour import TriContourSet


class TriContourSet(ContourSet):
    zmin: float
    _maxs: list[Any]
    zmax: float
    _mins: list[Any]
    cppContourGenerator: Any
    levels: Any

    def __init__(self: TriContourSet,
                 ax: Any,
                 *args,
                 **kwargs) -> None: ...

    def _process_args(self: TriContourSet,
                      *args,
                      **kwargs) -> dict[str, Any]: ...

    def _get_allsegs_and_allkinds(self: TriContourSet) -> Tuple[
        list[Union[list[Any], Any]], Optional[list[list[Any]]]]: ...

    def _contour_args(self: TriContourSet,
                      args: Union[tuple[Any, ...], Any],
                      kwargs: Any) -> Tuple[Union[Triangulation, Any], Any]: ...


def tricontour(*args,
               ax: Any,
               **kwargs) -> Union[TriContourSet, Any]: ...


def tricontourf(*args,
                ax: Any,
                **kwargs) -> Union[TriContourSet, Any]: ...