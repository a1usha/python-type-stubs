from _enums import CapStyle as CapStyle
from _enums import JoinStyle as JoinStyle
from transforms import Affine2D as Affine2D
from transforms import IdentityTransform as IdentityTransform
from path import Path as Path
from matplotlib import rcParams as rcParams
from matplotlib import cbook as cbook
from matplotlib import _api as _api
from collections.abc import Sized as Sized
from typing import ClassVar
from typing import Iterable
from typing import Optional
from typing import Sized
from typing import Union

from matplotlib import _api
from matplotlib._enums import CapStyle
from matplotlib._enums import JoinStyle
from matplotlib.markers import MarkerStyle
from matplotlib.path import Path
from matplotlib.transforms import IdentityTransform
from numpy.core._multiarray_umath import ndarray
from object import object

_empty_path: Path
from typing import Any


class MarkerStyle(object):
    markers: ClassVar[dict[Union[str, Any], Union[str, Any]]]
    filled_markers: ClassVar[tuple[str, str, str, str, str, str, str, str, str, str, str, str, str, str, str]]
    fillstyles: ClassVar[tuple[str, str, str, str, str, str]]
    _half_fillstyles: ClassVar[tuple[str, str, str, str]]
    _point_size_reduction: ClassVar[float]
    _triangle_path: ClassVar[Path]
    _triangle_path_u: ClassVar[Path]
    _triangle_path_d: ClassVar[Path]
    _triangle_path_l: ClassVar[Path]
    _triangle_path_r: ClassVar[Path]
    _line_marker_path: ClassVar[Path]
    _tickhoriz_path: ClassVar[Path]
    _tickvert_path: ClassVar[Path]
    _tri_path: ClassVar[Path]
    _caret_path: ClassVar[Path]
    _caret_path_base: ClassVar[Path]
    _plus_path: ClassVar[Path]
    _x_path: ClassVar[Path]
    _plus_filled_path: ClassVar[Path]
    _plus_filled_path_t: ClassVar[Path]
    _x_filled_path: ClassVar[Path]
    _x_filled_path_t: ClassVar[Path]
    _capstyle: CapStyle
    _transform: IdentityTransform
    _alt_transform: None
    _alt_path: None
    _marker: Union[ndarray, str, Path, Sized, Iterable, int, float]
    _fillstyle: Union[Optional[str], Any]
    _filled: Union[bool, Any]
    _snap: bool
    _path: Path
    _marker_function: None
    _snap_threshold: None
    _joinstyle: JoinStyle

    def __init__(self: MarkerStyle,
                 marker: Union[str, ndarray, Iterable, int, float, Path, MarkerStyle] = None,
                 fillstyle: str = None) -> None: ...

    def _recache(self: MarkerStyle) -> None: ...

    def __bool__(self: MarkerStyle) -> bool: ...

    def is_filled(self: MarkerStyle) -> Union[bool, Any]: ...

    def get_fillstyle(self: MarkerStyle) -> Union[Optional[str], Any]: ...

    @_api.deprecated("3.4", alternative="a new marker")
    def set_fillstyle(self: MarkerStyle,
                      fillstyle: Any) -> Optional[Any]: ...

    def _set_fillstyle(self: MarkerStyle,
                       fillstyle: str) -> None: ...

    def get_joinstyle(self: MarkerStyle) -> JoinStyle: ...

    def get_capstyle(self: MarkerStyle) -> CapStyle: ...

    def get_marker(self: MarkerStyle) -> Union[ndarray, str, Path, Sized, Iterable, int, float]: ...

    @_api.deprecated("3.4", alternative="a new marker")
    def set_marker(self: MarkerStyle,
                   marker: Any) -> Any: ...

    def _set_marker(self: MarkerStyle,
                    marker: Union[str, ndarray, Iterable, int, float, Path, MarkerStyle]) -> Any: ...

    def get_path(self: MarkerStyle) -> Path: ...

    def get_transform(self: MarkerStyle) -> IdentityTransform: ...

    def get_alt_path(self: MarkerStyle) -> Any: ...

    def get_alt_transform(self: MarkerStyle) -> Any: ...

    def get_snap_threshold(self: MarkerStyle) -> Any: ...

    def _set_nothing(self: MarkerStyle) -> None: ...

    def _set_custom_marker(self: MarkerStyle,
                           path: Union[Union[ndarray, str, Path, Sized, Iterable, int, float], Any]) -> None: ...

    def _set_path_marker(self: MarkerStyle) -> None: ...

    def _set_vertices(self: MarkerStyle) -> None: ...

    def _set_tuple_marker(self: MarkerStyle) -> Any: ...

    def _set_mathtext_path(self: MarkerStyle) -> None: ...

    def _half_fill(self: MarkerStyle) -> bool: ...

    def _set_circle(self: MarkerStyle,
                    reduction: float = 1.0) -> None: ...

    def _set_pixel(self: MarkerStyle) -> None: ...

    def _set_point(self: MarkerStyle) -> None: ...

    def _set_triangle(self: MarkerStyle,
                      rot: Union[float, Any],
                      skip: Union[int, Any]) -> None: ...

    def _set_triangle_up(self: MarkerStyle) -> None: ...

    def _set_triangle_down(self: MarkerStyle) -> None: ...

    def _set_triangle_left(self: MarkerStyle) -> None: ...

    def _set_triangle_right(self: MarkerStyle) -> None: ...

    def _set_square(self: MarkerStyle) -> None: ...

    def _set_diamond(self: MarkerStyle) -> None: ...

    def _set_thin_diamond(self: MarkerStyle) -> None: ...

    def _set_pentagon(self: MarkerStyle) -> None: ...

    def _set_star(self: MarkerStyle) -> None: ...

    def _set_hexagon1(self: MarkerStyle) -> None: ...

    def _set_hexagon2(self: MarkerStyle) -> None: ...

    def _set_octagon(self: MarkerStyle) -> None: ...

    def _set_vline(self: MarkerStyle) -> None: ...

    def _set_hline(self: MarkerStyle) -> None: ...

    def _set_tickleft(self: MarkerStyle) -> None: ...

    def _set_tickright(self: MarkerStyle) -> None: ...

    def _set_tickup(self: MarkerStyle) -> None: ...

    def _set_tickdown(self: MarkerStyle) -> None: ...

    def _set_tri_down(self: MarkerStyle) -> None: ...

    def _set_tri_up(self: MarkerStyle) -> None: ...

    def _set_tri_left(self: MarkerStyle) -> None: ...

    def _set_tri_right(self: MarkerStyle) -> None: ...

    def _set_caretdown(self: MarkerStyle) -> None: ...

    def _set_caretup(self: MarkerStyle) -> None: ...

    def _set_caretleft(self: MarkerStyle) -> None: ...

    def _set_caretright(self: MarkerStyle) -> None: ...

    def _set_caretdownbase(self: MarkerStyle) -> None: ...

    def _set_caretupbase(self: MarkerStyle) -> None: ...

    def _set_caretleftbase(self: MarkerStyle) -> None: ...

    def _set_caretrightbase(self: MarkerStyle) -> None: ...

    def _set_plus(self: MarkerStyle) -> None: ...

    def _set_x(self: MarkerStyle) -> None: ...

    def _set_plus_filled(self: MarkerStyle) -> None: ...

    def _set_x_filled(self: MarkerStyle) -> None: ...
