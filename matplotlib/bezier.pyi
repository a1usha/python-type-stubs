from matplotlib import _api as _api
from functools import lru_cache as lru_cache
from typing import Any
from typing import Callable
from typing import Tuple
from typing import Union

from ValueError import ValueError
from matplotlib import _api
from matplotlib.bezier import BezierSegment
from matplotlib.path import Path
from object import object


def _comb(n: {__sub__, __add__},
          k: {__gt__}) -> Union[int, Any]: ...


class NonIntersectingPathException(ValueError):
    pass


def get_intersection(cx1: Union[float, Any],
                     cy1: Union[float, Any],
                     cos_t1: {__mul__, __neg__},
                     sin_t1: {__mul__},
                     cx2: Union[float, Any],
                     cy2: Union[float, Any],
                     cos_t2: {__mul__, __neg__},
                     sin_t2: {__mul__}) -> Tuple[Union[float, Any], Union[float, Any]]: ...


def get_normal_points(cx: Union[float, Any],
                      cy: Union[float, Any],
                      cos_t: {__neg__},
                      sin_t: {__neg__},
                      length: Union[float, Any]) -> Tuple[
    Union[float, Any], Union[float, Any], Union[float, Any], Union[float, Any]]: ...


def _de_casteljau1(beta: Any,
                   t: Union[float, Any]) -> Union[Union[int, float], Any]: ...


def split_de_casteljau(beta: Union[int, Any],
                       t: Union[float, Any]) -> Tuple[list[Any], list[Any]]: ...


def find_bezier_t_intersecting_with_closedpath(bezier_point_at_t: Callable,
                                               inside_closedpath: Callable,
                                               t0: float = 0.,
                                               t1: float = 1.,
                                               tolerance: float = 0.01) -> float: ...


class BezierSegment(object):
    _cpoints: Any
    _d: Any
    _px: Any
    _orders: Any
    _N: Any

    def __init__(self: BezierSegment,
                 control_points: Any) -> None: ...

    def __call__(self: BezierSegment,
                 t: Any) -> Any: ...

    def point_at_t(self: BezierSegment,
                   t: Any) -> Tuple: ...

    def control_points(self: BezierSegment) -> Any: ...

    def dimension(self: BezierSegment) -> Any: ...

    def degree(self: BezierSegment) -> Union[int, Any]: ...

    def polynomial_coefficients(self: BezierSegment) -> Any: ...

    def axis_aligned_extrema(self: BezierSegment) -> array.pyi: ...


def split_bezier_intersecting_with_closedpath(bezier: int,
                                              inside_closedpath: Callable,
                                              tolerance: float = 0.01) -> Any: ...


def split_path_inout(path: {iter_segments, codes},
                     inside: Any,
                     tolerance: float = 0.01,
                     reorder_inout: bool = False) -> Tuple[Path, Path]: ...


def inside_circle(cx: Any,
                  cy: Any,
                  r: {__pow__}) -> Callable[[Any], bool]: ...


def get_cos_sin(x0: Union[float, Any],
                y0: Union[float, Any],
                x1: Union[float, Any],
                y1: Union[float, Any]) -> Union[Tuple[float, float], Tuple[Union[float, Any], Union[float, Any]]]: ...


def check_if_parallel(dx1: float,
                      dy1: float,
                      dx2: float,
                      dy2: float,
                      tolerance: float = 1.e-5) -> Any: ...


def get_parallels(bezier2: {__getitem__},
                  width: Any) -> Tuple[
    list[Tuple[Union[float, Any], Union[float, Any]]], list[Tuple[Union[float, Any], Union[float, Any]]]]: ...


def find_control_points(c1x: Union[float, Any],
                        c1y: Union[float, Any],
                        mmx: Union[float, Any],
                        mmy: Union[float, Any],
                        c2x: Union[float, Any],
                        c2y: Union[float, Any]) -> list[Tuple[Union[float, Any], Union[float, Any]]]: ...


def make_wedged_bezier2(bezier2: {__getitem__},
                        width: {__mul__},
                        w1: float = 1.,
                        wm: float = 0.5,
                        w2: float = 0.) -> Tuple[
    list[Tuple[Union[float, Any], Union[float, Any]]], list[Tuple[Union[float, Any], Union[float, Any]]]]: ...


@_api.deprecated(
    "3.3", alternative="Path.cleaned() and remove the final STOP if needed")
def make_path_regular(p: {codes}) -> Union[Union[Path, {codes}], Any]: ...


@_api.deprecated("3.3", alternative="Path.make_compound_path()")
def concatenate_paths(paths: Any) -> Union[Path, Any]: ...