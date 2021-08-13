from typing import Any
from typing import Optional
from typing import Union
from typing import tuple

from matplotlib.streamplot import DomainMap
from numpy.core._multiarray_umath import ndarray
from numpy.ma.core import MaskedConstant


class StreamplotSet(object):
    def __init__(self: StreamplotSet,
                 lines: Any,
                 arrows: Any,
                 **kwargs) -> None: ...


class TerminateTrajectory(Exception):
    pass


class OutOfBounds(IndexError):
    pass


class InvalidIndexError(Exception):
    pass


class StreamMask(object):
    def __init__(self: StreamMask,
                 density: Any) -> Any: ...

    def __getitem__(self: StreamMask,
                    args: Any) -> None: ...

    def _start_trajectory(self: StreamMask,
                          xm: Any,
                          ym: Any) -> None: ...

    def _undo_trajectory(self: StreamMask) -> None: ...

    def _update_trajectory(self: StreamMask,
                           xm: Any,
                           ym: Any) -> Any: ...


class DomainMap(object):
    def __init__(self: DomainMap,
                 grid: {nx, ny, dx, dy},
                 mask: {nx, ny}) -> None: ...

    def grid2mask(self: DomainMap,
                  xi: {__mul__},
                  yi: {__mul__}) -> tuple[int, int]: ...

    def mask2grid(self: DomainMap,
                  xm: int,
                  ym: {__mul__}) -> tuple[Union[int, float], float]: ...

    def data2grid(self: DomainMap,
                  xd: Optional[Any],
                  yd: Optional[Any]) -> tuple[float, float]: ...

    def grid2data(self: DomainMap,
                  xg: {__truediv__},
                  yg: {__truediv__}) -> tuple[float, float]: ...

    def start_trajectory(self: DomainMap,
                         xg: {__mul__},
                         yg: {__mul__}) -> None: ...

    def reset_start_point(self: DomainMap,
                          xg: Any,
                          yg: {__mul__}) -> None: ...

    def update_trajectory(self: DomainMap,
                          xg: Any,
                          yg: Any) -> Any: ...

    def undo_trajectory(self: DomainMap) -> None: ...


class Grid(object):
    def __init__(self: Grid,
                 x: {ndim, __len__, __getitem__},
                 y: {ndim, __len__, __getitem__}) -> Any: ...

    @property
    def shape(self: Grid) -> tuple[int, int]: ...

    def within_grid(self: Grid,
                    xi: Any,
                    yi: Any) -> bool: ...


def _euler_step(xf_traj: list[{__mul__}],
                yf_traj: list,
                dmap: DomainMap,
                f: Union[(xi: Any, yi: Any)) -> tuple[float, list[{__mul__}], list]: ...


def _integrate_rk12(x0: {__mul__},
                    y0: Any,
                    dmap: DomainMap,
                    f: Union[(xi: Any, yi: Any),
                    maxlength: float) -> tuple[int, list[{__mul__}], list]: ...


def interpgrid(a: Union[ndarray, None, MaskedConstant, float],
               xi: ndarray,
               yi: ndarray) -> Union[_NotImplementedType, MaskedConstant, int]: ...


def _gen_starting_points(shape: tuple) -> Generator[tuple[int, int], Any, None]: ...


def get_integrator(u: Optional[Any],
                   v: Optional[Any],
                   dmap: DomainMap,
                   minlength: float,
                   maxlength: float,
                   integration_direction: str) -> (x0: {__mul__}, y0: Any) ->


def streamplot(axes: {add_patch, add_collection, autoscale_view},
               x: int,
               y: int,
               u: int,
               v: int,
               density: Union[float, tuple[float, float]] = 1,
               linewidth: Any = None,
               color: Any = None,
               cmap: Any = None,
               norm: Any = None,
               arrowsize: float = 1,
               arrowstyle: str = '-|>',
               minlength: float = 0.1,
               transform: Any = None,
               zorder: int = None,
               start_points: Any = None,
               maxlength: float = 4.0,
               integration_direction: str = 'both') -> StreamplotSet: ...