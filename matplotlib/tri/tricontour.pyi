from typing import Any
from typing import Tuple

from matplotlib.contour import ContourSet
from matplotlib.tri.tricontour import TriContourSet


class TriContourSet(ContourSet):
    def __init__(self: TriContourSet,
                 ax: Any,
                 *args,
                 **kwargs) -> None: ...

    def _process_args(self: TriContourSet,
                      *args,
                      **kwargs) -> dict[str, Any]: ...

    def _get_allsegs_and_allkinds(self: TriContourSet) -> Tuple[list[Optional[list]], Optional[list[list]]]: ...

    def _contour_args(self: TriContourSet,
                      args: tuple[Any, ...],
                      kwargs: Any) -> Tuple[Triangulation, None]: ...


def tricontour(*args,
               ax: Any,
               **kwargs) -> TriContourSet: ...


def tricontourf(*args,
                ax: Any,
                **kwargs) -> TriContourSet: ...