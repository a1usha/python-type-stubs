from _enums import CapStyle as CapStyle
from _enums import JoinStyle as JoinStyle
from path import Path as Path
from bezier import split_path_inout as split_path_inout
from bezier import split_bezier_intersecting_with_closedpath as split_bezier_intersecting_with_closedpath
from bezier import make_wedged_bezier2 as make_wedged_bezier2
from bezier import inside_circle as inside_circle
from bezier import get_parallels as get_parallels
from bezier import get_intersection as get_intersection
from bezier import get_cos_sin as get_cos_sin
from bezier import NonIntersectingPathException as NonIntersectingPathException
from matplotlib import transforms as transforms
from matplotlib import lines as mlines
from matplotlib import hatch as mhatch
from matplotlib import docstring as docstring
from matplotlib import colors as colors
from matplotlib import cbook as cbook
from matplotlib import artist as artist
from matplotlib import _api as _api
from collections import namedtuple as namedtuple
from numbers import Number as Number
from functools import partial
from numbers import Number
from typing import Any
from typing import Callable
from typing import ClassVar
from typing import Generator
from typing import Iterable
from typing import Optional
from typing import StairData
from typing import Tuple
from typing import Type
from typing import Union

from matplotlib import _api
from matplotlib.artist import Artist
from matplotlib.backend_bases import MouseEvent
from matplotlib.patches import Arc
from matplotlib.patches import Arrow
from matplotlib.patches import ArrowStyle
from matplotlib.patches import BoxStyle
from matplotlib.patches import Circle
from matplotlib.patches import CirclePolygon
from matplotlib.patches import ConnectionPatch
from matplotlib.patches import Ellipse
from matplotlib.patches import FancyArrow
from matplotlib.patches import FancyArrowPatch
from matplotlib.patches import FancyBboxPatch
from matplotlib.patches import Patch
from matplotlib.patches import PathPatch
from matplotlib.patches import Polygon
from matplotlib.patches import Rectangle
from matplotlib.patches import RegularPolygon
from matplotlib.patches import Shadow
from matplotlib.patches import StepPatch
from matplotlib.patches import Wedge
from matplotlib.patches import _Style
from matplotlib.patches.ArrowStyle import _Base
from matplotlib.path import Path
from matplotlib.transforms import Affine2D
from matplotlib.transforms import Bbox
from matplotlib.transforms import CompositeAffine2D
from matplotlib.transforms import CompositeGenericTransform
from matplotlib.transforms import IdentityTransform
from object import object


class Patch(Artist):
    zorder: ClassVar[int]
    _edge_default: ClassVar[bool]
    fill: ClassVar[property]
    _capstyle: Any
    _hatch: Any
    _transformSet: Any
    _facecolor: Any
    _dashoffset: Any
    _fill: bool
    _hatch_color: Union[Iterable, tuple]
    _joinstyle: Any
    _us_dashes: None
    _linewidth: int
    _original_edgecolor: Any
    _antialiased: Optional[Any]
    stale: bool
    _linestyle: str
    _original_facecolor: Any
    _dashes: Any
    _edgecolor: Any

    @_api.deprecated("3.4")
    @_api.classproperty
    def validCap(cls: Patch) -> Union[_deprecated_property, Any]: ...

    @_api.deprecated("3.4")
    @_api.classproperty
    def validJoin(cls: Patch) -> Union[_deprecated_property, Any]: ...

    def __init__(self: Patch,
                 edgecolor: Any = None,
                 facecolor: Any = None,
                 color: Any = None,
                 linewidth: Any = None,
                 linestyle: Any = None,
                 antialiased: Any = None,
                 hatch: Any = None,
                 fill: bool = True,
                 capstyle: Any = None,
                 joinstyle: Any = None,
                 **kwargs) -> None: ...

    def get_verts(self: Patch) -> Union[list[Any], Any]: ...

    def _process_radius(self: Patch,
                        radius: Union[Optional[float], Any]) -> Union[float, Number, int]: ...

    def contains(self: Patch,
                 mouseevent: MouseEvent,
                 radius: Any = None) -> Any: ...

    def contains_point(self: Patch,
                       point: tuple[float, float],
                       radius: Optional[float] = None) -> bool: ...

    def contains_points(self: Patch,
                        points: int,
                        radius: Optional[float] = None) -> Any: ...

    def update_from(self: Patch,
                    other: {_transform, _transformSet, _visible, _alpha, clipbox, _clipon, _clippath, _label, _sketch,
                            _path_effects, sticky_edges}) -> None: ...

    def get_extents(self: Patch) -> Any: ...

    def get_transform(self: Patch) -> Union[Union[{input_dims, output_dims}, {output_dims,
                                                                              input_dims}, CompositeAffine2D, CompositeGenericTransform, _NotImplementedType], Any]: ...

    def get_data_transform(self: Patch) -> Union[IdentityTransform, Any]: ...

    def get_patch_transform(self: Patch) -> IdentityTransform: ...

    def get_antialiased(self: Patch) -> Optional[Any]: ...

    def get_edgecolor(self: Patch) -> Any: ...

    def get_facecolor(self: Patch) -> Any: ...

    def get_linewidth(self: Patch) -> int: ...

    def get_linestyle(self: Patch) -> str: ...

    def set_antialiased(self: Patch,
                        aa: Optional[Any]) -> None: ...

    def _set_edgecolor(self: Patch,
                       color: Any) -> None: ...

    def set_edgecolor(self: Patch,
                      color: Any) -> None: ...

    def _set_facecolor(self: Patch,
                       color: Optional[Any]) -> None: ...

    def set_facecolor(self: Patch,
                      color: Optional[Any]) -> None: ...

    def set_color(self: Patch,
                  c: Any) -> None: ...

    def set_alpha(self: Patch,
                  alpha: Union[int, float, complex, None]) -> None: ...

    def set_linewidth(self: Patch,
                      w: Optional[float]) -> None: ...

    def set_linestyle(self: Patch,
                      ls: str) -> None: ...

    def set_fill(self: Patch,
                 b: bool) -> None: ...

    def get_fill(self: Patch) -> bool: ...

    def set_capstyle(self: Patch,
                     s: Any) -> Optional[Any]: ...

    def get_capstyle(self: Patch) -> Any: ...

    def set_joinstyle(self: Patch,
                      s: Any) -> Optional[Any]: ...

    def get_joinstyle(self: Patch) -> Any: ...

    def set_hatch(self: Patch,
                  hatch: str) -> None: ...

    def get_hatch(self: Patch) -> Any: ...

    def _bind_draw_path_function(self: Patch,
                                 renderer: Optional[Any]) -> Union[Generator[partial[None], Any, None], Any]: ...

    def draw(self: Patch,
             renderer: Any) -> Optional[Any]: ...

    def get_path(self: Patch) -> Any: ...

    def get_window_extent(self: Patch,
                          renderer: Any = None) -> Any: ...

    def _convert_xy_units(self: Patch,
                          xy: {__getitem__}) -> Tuple[Any, Any]: ...


_patch_kwdoc: str


class Shadow(Patch):
    props: ClassVar[deprecate_privatize_attribute]
    patch: Any
    _oy: float
    _ox: float
    _shadow_transform: Affine2D
    _props: dict[Any, Any]

    def __str__(self: Shadow) -> str: ...

    @_api.delete_parameter("3.3", "props")
    def __init__(self: Shadow,
                 patch: Any,
                 ox: float,
                 oy: float,
                 props: dict = None,
                 **kwargs) -> Optional[Any]: ...

    def _update(self: Shadow) -> None: ...

    def _update_transform(self: Shadow,
                          renderer: Union[{get_rasterized, get_agg_filter, figure}, Any]) -> None: ...

    def get_path(self: Shadow) -> Any: ...

    def get_patch_transform(self: Shadow) -> Any: ...

    def draw(self: Shadow,
             renderer: {points_to_pixels, get_rasterized, get_agg_filter, figure}) -> None: ...


class Rectangle(Patch):
    xy: ClassVar[property]
    stale: bool
    _x0: float
    _y0: float
    angle: float
    _width: float
    _height: float

    def __str__(self: Rectangle) -> str: ...

    def __init__(self: Rectangle,
                 xy: tuple[float, float],
                 width: float,
                 height: float,
                 angle: float = 0.0,
                 edgecolor: Any = ...,
                 facecolor: Any = ...,
                 color: Any = ...,
                 linewidth: int = ...,
                 linestyle: str = ...,
                 antialiased: Optional[Any] = ...,
                 hatch: Any = ...,
                 fill: bool = ...,
                 capstyle: Any = ...,
                 joinstyle: Any = ...,
                 **kwargs) -> Optional[Any]: ...

    def get_path(self: Rectangle) -> Union[Path, Any]: ...

    def _convert_units(self: Rectangle) -> Tuple[Any, Any, Any, Any]: ...

    def get_patch_transform(self: Rectangle) -> Union[{input_dims, output_dims}, {output_dims,
                                                                                  input_dims}, CompositeAffine2D, CompositeGenericTransform, _NotImplementedType]: ...

    def get_x(self: Rectangle) -> float: ...

    def get_y(self: Rectangle) -> float: ...

    def get_xy(self: Rectangle) -> Tuple[float, float]: ...

    def get_width(self: Rectangle) -> float: ...

    def get_height(self: Rectangle) -> float: ...

    def set_x(self: Rectangle,
              x: Any) -> None: ...

    def set_y(self: Rectangle,
              y: Any) -> None: ...

    def set_xy(self: Rectangle,
               xy: tuple[float, float]) -> None: ...

    def set_width(self: Rectangle,
                  w: Any) -> None: ...

    def set_height(self: Rectangle,
                   h: Any) -> None: ...

    def set_bounds(self: Rectangle,
                   *args) -> None: ...

    def get_bbox(self: Rectangle) -> Bbox: ...


class RegularPolygon(Patch):
    xy: tuple[float, float]
    orientation: float
    _patch_transform: Affine2D
    numvertices: int
    _path: Union[Path, Any]
    radius: float

    def __str__(self: RegularPolygon) -> str: ...

    def __init__(self: RegularPolygon,
                 xy: tuple[float, float],
                 numVertices: int,
                 radius: float = 5,
                 orientation: float = 0,
                 **kwargs) -> Optional[Any]: ...

    def get_path(self: RegularPolygon) -> Union[Path, Any]: ...

    def get_patch_transform(self: RegularPolygon) -> Affine2D: ...


class PathPatch(Patch):
    _edge_default: ClassVar[bool]
    _path: Union[Path, Any]

    def __str__(self: PathPatch) -> str: ...

    def __init__(self: PathPatch,
                 path: Union[Path, Any],
                 **kwargs) -> Optional[Any]: ...

    def get_path(self: PathPatch) -> Union[Path, Any]: ...

    def set_path(self: PathPatch,
                 path: Any) -> None: ...


class StepPatch(PathPatch):
    _edge_default: ClassVar[bool]
    _baseline: Optional[Any]
    orientation: str
    stale: bool
    _values: Any
    _path: Path
    _edges: Any

    def __init__(self: StepPatch,
                 values: Union[Union[Iterable, int, float], Any],
                 edges: Union[Union[Iterable, int, float], Any],
                 *,
                 orientation: str = 'vertical',
                 baseline: Union[Union[float, Iterable, int, None], Any] = 0,
                 **kwargs) -> Optional[Any]: ...

    def _update_path(self: StepPatch) -> Any: ...

    def get_data(self: StepPatch) -> StairData: ...

    def set_data(self: StepPatch,
                 values: int = None,
                 edges: Optional[int] = None,
                 baseline: Union[float, int] = None) -> Any: ...


class Polygon(Patch):
    xy: ClassVar[property]
    stale: bool
    _path: Path
    _closed: bool

    def __str__(self: Polygon) -> str: ...

    def __init__(self: Polygon,
                 xy: Any,
                 closed: bool = True,
                 **kwargs) -> Optional[Any]: ...

    def get_path(self: Polygon) -> Path: ...

    def get_closed(self: Polygon) -> bool: ...

    def set_closed(self: Polygon,
                   closed: bool) -> None: ...

    def get_xy(self: Polygon) -> Any: ...

    def set_xy(self: Polygon,
               xy: int) -> None: ...


class Wedge(Patch):
    r: Any
    stale: bool
    _patch_transform: IdentityTransform
    center: Any
    width: Any
    theta1: Any
    _path: Path
    theta2: Any

    def __str__(self: Wedge) -> str: ...

    def __init__(self: Wedge,
                 center: Any,
                 r: Any,
                 theta1: Any,
                 theta2: Any,
                 width: Any = None,
                 **kwargs) -> Optional[Any]: ...

    def _recompute_path(self: Wedge) -> None: ...

    def set_center(self: Wedge,
                   center: Any) -> None: ...

    def set_radius(self: Wedge,
                   radius: Any) -> None: ...

    def set_theta1(self: Wedge,
                   theta1: Any) -> None: ...

    def set_theta2(self: Wedge,
                   theta2: Any) -> None: ...

    def set_width(self: Wedge,
                  width: Any) -> None: ...

    def get_path(self: Wedge) -> Optional[Path]: ...


class Arrow(Patch):
    _path: ClassVar[Path]
    _patch_transform: Affine2D

    def __str__(self: Arrow) -> str: ...

    def __init__(self: Arrow,
                 x: float,
                 y: float,
                 dx: float,
                 dy: float,
                 width: float = 1.0,
                 **kwargs) -> Optional[Any]: ...

    def get_path(self: Arrow) -> Path: ...

    def get_patch_transform(self: Arrow) -> Affine2D: ...


class FancyArrow(Polygon):
    _edge_default: ClassVar[bool]

    def __str__(self: FancyArrow) -> str: ...

    def __init__(self: FancyArrow,
                 x: Any,
                 y: Any,
                 dx: Any,
                 dy: Any,
                 width: float = 0.001,
                 length_includes_head: bool = False,
                 head_width: Optional[float] = None,
                 head_length: Optional[float] = None,
                 shape: str = 'full',
                 overhang: float = 0,
                 head_starts_at_zero: bool = False,
                 **kwargs) -> Any: ...


class CirclePolygon(RegularPolygon):
    def __str__(self: CirclePolygon) -> str: ...

    def __init__(self: CirclePolygon,
                 xy: tuple[float, float],
                 radius: float = 5,
                 resolution: int = 20,
                 **kwargs) -> Optional[Any]: ...


class Ellipse(Patch):
    center: ClassVar[property]
    width: ClassVar[property]
    height: ClassVar[property]
    angle: ClassVar[property]
    _angle: float
    stale: bool
    _patch_transform: IdentityTransform
    _center: tuple[float, float]
    _path: Union[Path, Any]
    _width: float
    _height: float

    def __str__(self: Ellipse) -> str: ...

    def __init__(self: Ellipse,
                 xy: tuple[float, float],
                 width: float,
                 height: float,
                 angle: float = 0,
                 **kwargs) -> Optional[Any]: ...

    def _recompute_transform(self: Ellipse) -> None: ...

    def get_path(self: Ellipse) -> Union[Path, Any]: ...

    def get_patch_transform(self: Ellipse) -> IdentityTransform: ...

    def set_center(self: Ellipse,
                   xy: tuple[float, float]) -> None: ...

    def get_center(self: Ellipse) -> Tuple[float, float]: ...

    def set_width(self: Ellipse,
                  width: float) -> None: ...

    def get_width(self: Ellipse) -> float: ...

    def set_height(self: Ellipse,
                   height: float) -> None: ...

    def get_height(self: Ellipse) -> float: ...

    def set_angle(self: Ellipse,
                  angle: float) -> None: ...

    def get_angle(self: Ellipse) -> float: ...


class Circle(Ellipse):
    radius: ClassVar[property]
    stale: bool
    width: float
    radius: int
    height: float

    def __str__(self: Circle) -> str: ...

    def __init__(self: Circle,
                 xy: tuple[float, float],
                 radius: int = 5,
                 **kwargs) -> Optional[Any]: ...

    def set_radius(self: Circle,
                   radius: float) -> None: ...

    def get_radius(self: Circle) -> float: ...


class Arc(Ellipse):
    theta1: Union[float, int]
    _path: Path
    theta2: Union[float, int]

    def __str__(self: Arc) -> str: ...

    def __init__(self: Arc,
                 xy: tuple[float, float],
                 width: float,
                 height: float,
                 angle: float = 0.0,
                 theta1: Union[float, int] = 0.0,
                 theta2: Union[float, int] = 360.0,
                 edgecolor: Any = ...,
                 facecolor: Any = ...,
                 color: Any = ...,
                 linewidth: int = ...,
                 linestyle: str = ...,
                 antialiased: Optional[Any] = ...,
                 hatch: Any = ...,
                 fill: bool = ...,
                 capstyle: Any = ...,
                 joinstyle: Any = ...,
                 **kwargs) -> Any: ...

    def draw(self: Arc,
             renderer: Any) -> Optional[Any]: ...


def bbox_artist(artist: {get_window_extent},
                renderer: {points_to_pixels, get_rasterized, get_agg_filter, figure},
                props: Any = None,
                fill: bool = True) -> None: ...


def draw_bbox(bbox: {x0, y0, width, height},
              renderer: {get_rasterized, get_agg_filter, figure},
              color: str = 'k',
              trans: Any = None) -> None: ...


def _simpleprint_styles(_styles: Union[dict[Any, Any], Any]) -> str: ...


class _Style(object):
    _list: Any
    _name: Any
    _args: dict
    _cls: Any
    _args_pair: list[Any]

    def __new__(cls: Type[_Style],
                stylename: {replace},
                **kwargs) -> Any: ...

    def get_styles(cls: Type[_Style]) -> Any: ...

    def pprint_styles(cls: Type[_Style]) -> str: ...

    def register(cls: Type[_Style],
                 name: Any,
                 style: Any) -> Any: ...


def _register_style(style_list: Union[dict[Any, Any], Any],
                    cls: Optional[{__name__}] = None,
                    *,
                    name: Union[str, Any] = None) -> Union[partial[Any], {__name__}, None]: ...


class BoxStyle(_Style):
    _style_list: ClassVar[dict[Any, Any]]
    pass


class ConnectionStyle(_Style):
    _style_list: ClassVar[dict[Any, Any]]
    pass


def _point_along_a_line(x0: {__sub__},
                        y0: {__sub__},
                        x1: Any,
                        y1: Any,
                        d: Union[float, Any]) -> Tuple[Union[float, Any], Union[float, Any]]: ...


class ArrowStyle(_Style):
    _style_list: ClassVar[dict[Any, Any]]
    pass


class FancyBboxPatch(Patch):
    _edge_default: ClassVar[bool]
    stale: bool
    _bbox_transmuter: Any
    _x: Any
    _mutation_aspect: float
    _y: Any
    _width: float
    _height: float
    _mutation_scale: float

    def __str__(self: FancyBboxPatch) -> str: ...

    @_api.delete_parameter("3.4", "bbox_transmuter", alternative="boxstyle")
    def __init__(self: FancyBboxPatch,
                 xy: float,
                 width: float,
                 height: float,
                 boxstyle: Union[str, BoxStyle] = "round",
                 bbox_transmuter: Any = None,
                 mutation_scale: float = 1,
                 mutation_aspect: float = 1,
                 edgecolor: Any = ...,
                 facecolor: Any = ...,
                 color: Any = ...,
                 linewidth: int = ...,
                 linestyle: str = ...,
                 antialiased: Optional[Any] = ...,
                 hatch: Any = ...,
                 fill: bool = ...,
                 capstyle: Any = ...,
                 joinstyle: Any = ...,
                 **kwargs) -> Any: ...

    def set_boxstyle(self: FancyBboxPatch,
                     boxstyle: Union[str, BoxStyle] = None,
                     **kwargs) -> Union[str, Any]: ...

    def set_mutation_scale(self: FancyBboxPatch,
                           scale: float) -> None: ...

    def get_mutation_scale(self: FancyBboxPatch) -> float: ...

    def set_mutation_aspect(self: FancyBboxPatch,
                            aspect: float) -> None: ...

    def get_mutation_aspect(self: FancyBboxPatch) -> Union[float, int]: ...

    def get_boxstyle(self: FancyBboxPatch) -> Any: ...

    def get_path(self: FancyBboxPatch) -> Path: ...

    def get_x(self: FancyBboxPatch) -> Any: ...

    def get_y(self: FancyBboxPatch) -> Any: ...

    def get_width(self: FancyBboxPatch) -> float: ...

    def get_height(self: FancyBboxPatch) -> float: ...

    def set_x(self: FancyBboxPatch,
              x: float) -> None: ...

    def set_y(self: FancyBboxPatch,
              y: float) -> None: ...

    def set_width(self: FancyBboxPatch,
                  w: float) -> None: ...

    def set_height(self: FancyBboxPatch,
                   h: float) -> None: ...

    def set_bounds(self: FancyBboxPatch,
                   *args) -> None: ...

    def get_bbox(self: FancyBboxPatch) -> Bbox: ...


class FancyArrowPatch(Patch):
    _edge_default: ClassVar[bool]
    patchB: Any
    patchA: Any
    _path_original: Optional[Any]
    stale: bool
    shrinkA: int
    _dpi_cor: int
    _connector: Callable
    shrinkB: int
    _mutation_aspect: int
    _posA_posB: None
    _arrow_transmuter: _Base
    _mutation_scale: int

    def __str__(self: FancyArrowPatch) -> str: ...

    @_api.delete_parameter("3.4", "dpi_cor")
    def __init__(self: FancyArrowPatch,
                 posA: Any = None,
                 posB: Any = None,
                 path: Any = None,
                 arrowstyle: Any = "simple",
                 connectionstyle: Any = "arc3",
                 patchA: Any = None,
                 patchB: Any = None,
                 shrinkA: int = 2,
                 shrinkB: int = 2,
                 mutation_scale: int = 1,
                 mutation_aspect: int = 1,
                 dpi_cor: int = 1,
                 edgecolor: Any = ...,
                 facecolor: Any = ...,
                 color: Any = ...,
                 linewidth: int = ...,
                 linestyle: str = ...,
                 antialiased: Optional[Any] = ...,
                 hatch: Any = ...,
                 fill: bool = ...,
                 capstyle: Any = ...,
                 joinstyle: Any = ...,
                 **kwargs) -> Any: ...

    @_api.deprecated("3.4")
    def set_dpi_cor(self: FancyArrowPatch,
                    dpi_cor: float) -> Optional[Any]: ...

    @_api.deprecated("3.4")
    def get_dpi_cor(self: FancyArrowPatch) -> Any: ...

    def set_positions(self: FancyArrowPatch,
                      posA: Union[None, Iterable, tuple],
                      posB: Union[None, Iterable, tuple]) -> None: ...

    def set_patchA(self: FancyArrowPatch,
                   patchA: Any) -> None: ...

    def set_patchB(self: FancyArrowPatch,
                   patchB: Any) -> None: ...

    def set_connectionstyle(self: FancyArrowPatch,
                            connectionstyle: Any,
                            **kwargs) -> str: ...

    def get_connectionstyle(self: FancyArrowPatch) -> Callable: ...

    def set_arrowstyle(self: FancyArrowPatch,
                       arrowstyle: Union[None, ArrowStyle, str] = None,
                       **kwargs) -> str: ...

    def get_arrowstyle(self: FancyArrowPatch) -> _Base: ...

    def set_mutation_scale(self: FancyArrowPatch,
                           scale: float) -> None: ...

    def get_mutation_scale(self: FancyArrowPatch) -> Any: ...

    def set_mutation_aspect(self: FancyArrowPatch,
                            aspect: float) -> None: ...

    def get_mutation_aspect(self: FancyArrowPatch) -> int: ...

    def get_path(self: FancyArrowPatch) -> Union[Path, Any]: ...

    def get_path_in_displaycoord(self: FancyArrowPatch) -> Tuple[Any, Any]: ...

    def draw(self: FancyArrowPatch,
             renderer: {open_group, new_gc, draw_path, close_group}) -> None: ...


class ConnectionPatch(FancyArrowPatch):
    xy2: Any
    coords2: Any
    xy1: Any
    axesA: Any
    axesB: Any
    stale: bool
    _dpi_cor: int
    _renderer: {open_group, new_gc, draw_path, close_group}
    coords1: Any
    _annotation_clip: None

    def __str__(self: ConnectionPatch) -> str: ...

    @_api.delete_parameter("3.4", "dpi_cor")
    def __init__(self: ConnectionPatch,
                 xyA: Any,
                 xyB: Any,
                 coordsA: Any,
                 coordsB: Any = None,
                 axesA: Any = None,
                 axesB: Any = None,
                 arrowstyle: str = "-",
                 connectionstyle: str = "arc3",
                 patchA: Any = None,
                 patchB: Any = None,
                 shrinkA: int = 0.,
                 shrinkB: int = 0.,
                 mutation_scale: int = 10.,
                 mutation_aspect: int = None,
                 clip_on: bool = False,
                 dpi_cor: int = 1.,
                 **kwargs) -> Optional[Any]: ...

    def _get_xy(self: ConnectionPatch,
                xy: Any,
                s: {__eq__},
                axes: Any = None) -> Union[Union[float, Tuple[Any, Any], Iterable, int], Any]: ...

    def set_annotation_clip(self: ConnectionPatch,
                            b: Optional[bool]) -> None: ...

    def get_annotation_clip(self: ConnectionPatch) -> Any: ...

    def get_path_in_displaycoord(self: ConnectionPatch) -> Tuple[Any, Any]: ...

    def _check_xy(self: ConnectionPatch,
                  renderer: Union[Optional[{open_group, new_gc, draw_path, close_group}], Any]) -> bool: ...

    def draw(self: ConnectionPatch,
             renderer: {open_group, new_gc, draw_path, close_group}) -> None: ...
