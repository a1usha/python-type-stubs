from typing import Any
from typing import tuple


class TriContourSet(ContourSet):
    def __init__(self: TriContourSet,
                 ax: Any,
                 *args,
                 **kwargs) -> None: ...

    def _process_args(self: TriContourSet,
                      *args,
                      **kwargs) -> dict[str, Any]: ...

    def _get_allsegs_and_allkinds(self: TriContourSet) -> tuple[list[Optional[list]], Optional[list[list]]]: ...

    def _contour_args(self: TriContourSet,
                      args: tuple[Any, ...],
                      kwargs: Any) -> tuple[Triangulation, None]: ...


@docstring.Substitution
@docstring.dedent_interpd
def tricontour(*args,
               ax: Any,
               **kwargs) -> TriContourSet: ...


@docstring.Substitution
@docstring.dedent_interpd
def tricontourf(*args,
                ax: Any,
                **kwargs) -> TriContourSet: ...