from typing import Any
from typing import Callable
from typing import Generator
from typing import Optional
from typing import Tuple
from typing import Union

from Exception import Exception
from IndexError import IndexError
from matplotlib.streamplot import DomainMap
from matplotlib.streamplot import Grid
from matplotlib.streamplot import StreamMask
from matplotlib.streamplot import StreamplotSet
from numpy.core._multiarray_umath import ndarray
from numpy.ma.core import MaskedConstant
from object import object


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


class StreamplotSet(object):
    def __init__(self: StreamplotSet,
                 lines: Any,
                 arrows: Any,
                 **kwargs) -> None: ...


class DomainMap(object):
    def __init__(self: DomainMap,
                 grid: {nx, ny, dx, dy},
                 mask: {nx, ny}) -> None: ...

    def grid2mask(self: DomainMap,
                  xi: {__mul__},
                  yi: {__mul__}) -> Tuple[int, int]: ...

    def mask2grid(self: DomainMap,
                  xm: Union[int, Any],
                  ym: {__mul__}) -> Tuple[Union[Union[int, float], Any], Union[float, Any]]: ...

    def data2grid(self: DomainMap,
                  xd: Optional[Any],
                  yd: Optional[Any]) -> Tuple[Union[float, Any], Union[float, Any]]: ...

    def grid2data(self: DomainMap,
                  xg: {__truediv__},
                  yg: {__truediv__}) -> Tuple[Union[float, Any], Union[float, Any]]: ...

    def start_trajectory(self: DomainMap,
                         xg: {__mul__},
                         yg: {__mul__}) -> None: ...

    def reset_start_point(self: DomainMap,
                          xg: {__mul__},
                          yg: {__mul__}) -> None: ...

    def update_trajectory(self: DomainMap,
                          xg: {__mul__},
                          yg: {__mul__}) -> Any: ...

    def undo_trajectory(self: DomainMap) -> None: ...


class Grid(object):
    def __init__(self: Grid,
                 x: {ndim, __len__, __getitem__},
                 y: {ndim, __len__, __getitem__}) -> Any: ...

    def shape(self: Grid) -> Tuple[int, int]: ...

    def within_grid(self: Grid,
                    xi: Any,
                    yi: Any) -> Union[bool, Any]: ...


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


class InvalidIndexError(Exception):
    pass


class TerminateTrajectory(Exception):
    pass


def get_integrator(u: Optional[Any],
                   v: Optional[Any],
                   dmap: Union[DomainMap, Any],
                   minlength: Union[float, Any],
                   maxlength: Union[float, Any],
                   integration_direction: Union[str, Any]) -> Callable[
    [{__mul__}, Any], Optional[Tuple[list[Any], list[Any]]]]: ...


class OutOfBounds(IndexError):
    pass


def _integrate_rk12(x0: Union[{__mul__}, Any],
                    y0: Any,
                    dmap: Union[DomainMap, Any],
                    f: Union[Union[Callable[[Any, Any], tuple[Union[None, int, float], Union[None, int, float]]],
                                   Callable[[Any, Any], tuple[
                                       Union[Union[_NotImplementedType, MaskedConstant, int, float], Any], Union[
                                           Union[_NotImplementedType, MaskedConstant, int, float], Any]]]], Any],
                    maxlength: Union[float, Any]) -> Tuple[
    int, Union[list[Union[{__mul__}, Any]], Any], Union[list[Any], Any]]: ...


def _euler_step(xf_traj: Union[list[Union[{__mul__}, Any]], Any],
                yf_traj: Union[list[Any], Any],
                dmap: Union[DomainMap, Any],
                f: Union[Union[Callable[[Any, Any], tuple[Union[None, int, float], Union[None, int, float]]], Callable[
                    [Any, Any], tuple[Union[Union[_NotImplementedType, MaskedConstant, int, float], Any], Union[
                        Union[_NotImplementedType, MaskedConstant, int, float], Any]]]], Any]) -> Tuple[
    Union[float, Any], Union[list[Union[{__mul__}, Any]], Any], Union[list[Any], Any]]: ...


def interpgrid(a: Union[Union[ndarray, None, MaskedConstant, float], Any],
               xi: Union[ndarray, Any],
               yi: Union[ndarray, Any]) -> Union[Union[_NotImplementedType, MaskedConstant, int], Any]: ...


def _gen_starting_points(shape: Union[tuple, Any]) -> Generator[Tuple[int, int], Any, None]: ...