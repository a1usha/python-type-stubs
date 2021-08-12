from typing import Any
from typing import Any
from typing import Any
from typing import Any
from typing import Any
from typing import Any
from typing import Any
from typing import Any
from typing import Any
from typing import Any
from typing import Any
from typing import Any
from typing import Any
from typing import Any
from typing import Any
from typing import Any
from typing import Any
from typing import Any
from typing import Any
from typing import Any
from numpy.core._multiarray_umath import ndarray
from typing import Any


class BezierSegment(object):
    def __init__(self: BezierSegment, control_points: Any) -> None: ...

    def __call__(self: BezierSegment, t: Any) -> Any: ...

    def point_at_t(self: BezierSegment, t: Any) -> tuple: ...

    def control_points(self: BezierSegment) -> ndarray: ...

    def dimension(self: BezierSegment) -> Any: ...

    def degree(self: BezierSegment) -> int: ...

    def polynomial_coefficients(self: BezierSegment) -> Any: ...

    def axis_aligned_extrema(self: BezierSegment) -> array.pyi: ...


class NonIntersectingPathException(ValueError):
    pass


def concatenate_paths(paths: Any) -> Path: ...


def check_if_parallel(dx1: float, dy1: float, dx2: float, dy2: float, tolerance: float = 1.e-5) -> Any: ...


def split_path_inout(path: {iter_segments, codes}, inside: Any, tolerance: float = 0.01, reorder_inout: bool = False) -> \
tuple[Path, Path]: ...


def _de_casteljau1(beta: ndarray, t: float) -> Union[int, float]: ...


def find_bezier_t_intersecting_with_closedpath(bezier_point_at_t: Callable, inside_closedpath: Callable, t0: float = 0.,
                                               t1: float = 1., tolerance: float = 0.01) -> float: ...


def find_control_points(c1x: float, c1y: float, mmx: float, mmy: float, c2x: float, c2y: float) -> list[
    tuple[float, float]]: ...


def inside_circle(cx: Any, cy: Any, r: {__pow__}) -> (xy: Any) ->


def make_path_regular(p: {codes}) -> Union[Path, {codes}]: ...


def make_wedged_bezier2(bezier2: {__getitem__}, width: {__mul__}, w1: float = 1., wm: float = 0.5, w2: float = 0.) -> \
tuple[list[tuple[float, float]], list[tuple[float, float]]]: ...


def get_cos_sin(x0: float, y0: float, x1: float, y1: float) -> Union[tuple[float, float], tuple[float, float]]: ...


def get_normal_points(cx: float, cy: float, cos_t: {__neg__}, sin_t: {__neg__}, length: float) -> tuple[
    float, float, float, float]: ...


def split_de_casteljau(beta: int, t: float) -> tuple[list[None], list[None]]: ...


def split_bezier_intersecting_with_closedpath(bezier: int, inside_closedpath: Callable,
                                              tolerance: float = 0.01) -> Any: ...


def _comb(n: {__sub__, __add__}, k: {__gt__}) -> Union[int, ndarray]: ...


def get_intersection(cx1: float, cy1: float, cos_t1: {__mul__, __neg__}, sin_t1: {__mul__}, cx2: float, cy2: float,
                     cos_t2: {__mul__, __neg__}, sin_t2: {__mul__}) -> tuple[float, float]: ...


def get_parallels(bezier2: {__getitem__}, width: Any) -> tuple[
    list[tuple[float, float]], list[tuple[float, float]]]: ...