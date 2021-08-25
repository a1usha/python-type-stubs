from markers import TICKDOWN as TICKDOWN
from markers import TICKUP as TICKUP
from markers import TICKRIGHT as TICKRIGHT
from markers import TICKLEFT as TICKLEFT
from markers import CARETDOWNBASE as CARETDOWNBASE
from markers import CARETUPBASE as CARETUPBASE
from markers import CARETRIGHTBASE as CARETRIGHTBASE
from markers import CARETLEFTBASE as CARETLEFTBASE
from markers import CARETDOWN as CARETDOWN
from markers import CARETUP as CARETUP
from markers import CARETRIGHT as CARETRIGHT
from markers import CARETLEFT as CARETLEFT
from matplotlib import _path as _path
from _enums import CapStyle as CapStyle
from _enums import JoinStyle as JoinStyle
from transforms import TransformedPath as TransformedPath
from transforms import BboxTransformTo as BboxTransformTo
from transforms import Bbox as Bbox
from path import Path as Path
from markers import MarkerStyle as MarkerStyle
from cbook import STEP_LOOKUP_MAP as STEP_LOOKUP_MAP
from cbook import ls_mapper_r as ls_mapper_r
from cbook import ls_mapper as ls_mapper
from cbook import _to_unmasked_float_array as _to_unmasked_float_array
from artist import allow_rasterization as allow_rasterization
from artist import Artist as Artist
from matplotlib import rcParams as rcParams
from matplotlib import docstring as docstring
from matplotlib import colors as mcolors
from matplotlib import cbook as cbook
from matplotlib import artist as artist
from matplotlib import _api as _api
from numbers import Real as Real
from numbers import Number as Number
from numbers import Integral as Integral
from typing import ClassVar
from typing import Iterable
from typing import Optional
from typing import Sized
from typing import Tuple
from typing import Union

from matplotlib import _api
from matplotlib.artist import Artist
from matplotlib.backend_bases import MouseEvent
from matplotlib.lines import Line2D
from matplotlib.lines import VertexSelector
from matplotlib.lines import _AxLine
from matplotlib.path import Path
from matplotlib.transforms import Bbox
from matplotlib.transforms import CompositeAffine2D
from matplotlib.transforms import CompositeGenericTransform
from matplotlib.transforms import Transform
from numpy.core._multiarray_umath import ndarray
from object import object

_log: Logger
from typing import Any


def _get_dash_pattern(style: Union[str, Any]) -> Tuple[Union[int, Any], Optional[Tuple]]: ...


def _scale_dashes(offset: Union[int, Any],
                  dashes: Union[Optional[tuple], Any],
                  lw: Union[Optional[float], Any]) -> Union[Tuple[Union[int, Any], Union[Optional[Tuple], Any]], Tuple[
    Union[Union[int, float], Any], Optional[list[Union[Optional[float], Any]]]]]: ...


def segment_hits(cx: Union[int, Any],
                 cy: Union[int, Any],
                 x: {__len__},
                 y: Any,
                 radius: Union[float, Any]) -> Union[ndarray, Any]: ...


def _mark_every_path(markevery: Any,
                     tpath: {codes, vertices},
                     affine: Any,
                     ax_transform: Any) -> Path: ...


class Line2D(Artist):
    lineStyles: ClassVar[dict[str, str]]
    _lineStyles: ClassVar[dict[str, str]]
    _drawStyles_l: ClassVar[dict[str, str]]
    _drawStyles_s: ClassVar[dict[str, str]]
    drawStyles: ClassVar[dict[Any, Any]]
    drawStyleKeys: ClassVar[list[Any]]
    markers: ClassVar[dict[Union[str, Any], Union[str, Any]]]
    filled_markers: ClassVar[tuple[str, str, str, str, str, str, str, str, str, str, str, str, str, str, str]]
    fillStyles: ClassVar[tuple[str, str, str, str, str, str]]
    zorder: ClassVar[int]
    pickradius: ClassVar[property]
    _us_dashOffset: int
    _yorig: ndarray
    _x_filled: None
    _solidcapstyle: None
    _transformed_path: None
    _markerfacecoloralt: None
    _xorig: ndarray
    _invalidy: bool
    _linewidth: Optional[Any]
    _markerfacecolor: None
    _invalidx: bool
    stale: bool
    ind_offset: int
    _us_dashSeq: None
    _dashcapstyle: None
    _xy: None
    pickradius: Number
    _marker: MarkerStyle
    _dashSeq: None
    _color: None
    _picker: Union[Callable, Any]
    _path: None
    _dashOffset: int
    _contains: Callable
    _solidjoinstyle: None
    _linestyles: None
    _markersize: None
    _dashjoinstyle: None
    _antialiased: None
    _linestyle: Union[str, Any]
    _drawstyle: None
    _markevery: None
    _subslice: bool
    _x: None
    _y: None
    _markeredgecolor: None
    _pickradius: float
    _markeredgewidth: None

    @_api.deprecated("3.4")
    @_api.classproperty
    def validCap(cls: Line2D) -> Union[Tuple[Any, ...], Any]: ...

    @_api.deprecated("3.4")
    @_api.classproperty
    def validJoin(cls: Line2D) -> Union[Tuple[Any, ...], Any]: ...

    def __str__(self: Line2D) -> str: ...

    def __init__(self: Line2D,
                 xdata: Union[list[int], Any],
                 ydata: Any,
                 linewidth: Any = None,
                 linestyle: Any = None,
                 color: Any = None,
                 marker: Any = None,
                 markersize: Any = None,
                 markeredgewidth: Any = None,
                 markeredgecolor: Any = None,
                 markerfacecolor: Any = None,
                 markerfacecoloralt: str = 'none',
                 fillstyle: Any = None,
                 antialiased: Any = None,
                 dash_capstyle: Any = None,
                 solid_capstyle: Any = None,
                 dash_joinstyle: Any = None,
                 solid_joinstyle: Any = None,
                 pickradius: int = 5,
                 drawstyle: Any = None,
                 markevery: Any = None,
                 **kwargs) -> Any: ...

    def contains(self: Line2D,
                 mouseevent: MouseEvent) -> bool: ...

    def get_pickradius(self: Line2D) -> float: ...

    def set_pickradius(self: Line2D,
                       d: float) -> Any: ...

    def get_fillstyle(self: Line2D) -> Union[Optional[str], Any]: ...

    def set_fillstyle(self: Line2D,
                      fs: str) -> None: ...

    def set_markevery(self: Line2D,
                      every: Any) -> None: ...

    def get_markevery(self: Line2D) -> Any: ...

    def set_picker(self: Line2D,
                   p: Any) -> None: ...

    def get_window_extent(self: Line2D,
                          renderer: Any) -> Bbox: ...

    def axes(self: Line2D,
             ax: Any) -> Optional[Any]: ...

    def set_data(self: Line2D,
                 *args) -> None: ...

    def recache_always(self: Line2D) -> None: ...

    def recache(self: Line2D,
                always: bool = False) -> None: ...

    def _transform_path(self: Line2D,
                        subslice: Union[Optional[slice], Any] = None) -> None: ...

    def _get_transformed_path(self: Line2D) -> Optional[Any]: ...

    def set_transform(self: Line2D,
                      t: Transform) -> None: ...

    def _is_sorted(self: Line2D,
                   x: Optional[Any]) -> None: ...

    def draw(self: Line2D,
             renderer: {open_group, close_group}) -> Optional[Any]: ...

    def get_antialiased(self: Line2D) -> Any: ...

    def get_color(self: Line2D) -> Any: ...

    def get_drawstyle(self: Line2D) -> Any: ...

    def get_linestyle(self: Line2D) -> Union[str, Any]: ...

    def get_linewidth(self: Line2D) -> Optional[Any]: ...

    def get_marker(self: Line2D) -> Union[ndarray, str, Path, Sized, Iterable, int, float]: ...

    def get_markeredgecolor(self: Line2D) -> Union[str, Any]: ...

    def get_markeredgewidth(self: Line2D) -> Any: ...

    def _get_markerfacecolor(self: Line2D,
                             alt: bool = False) -> Union[str, Any]: ...

    def get_markerfacecolor(self: Line2D) -> Union[str, Any]: ...

    def get_markerfacecoloralt(self: Line2D) -> Union[str, Any]: ...

    def get_markersize(self: Line2D) -> Any: ...

    def get_data(self: Line2D,
                 orig: bool = True) -> Tuple[Union[ndarray, Any], Union[ndarray, Any]]: ...

    def get_xdata(self: Line2D,
                  orig: bool = True) -> Union[ndarray, Any]: ...

    def get_ydata(self: Line2D,
                  orig: bool = True) -> Union[ndarray, Any]: ...

    def get_path(self: Line2D) -> Any: ...

    def get_xydata(self: Line2D) -> Any: ...

    def set_antialiased(self: Line2D,
                        b: bool) -> None: ...

    def set_color(self: Line2D,
                  color: Any) -> None: ...

    def set_drawstyle(self: Line2D,
                      drawstyle: str) -> None: ...

    def set_linewidth(self: Line2D,
                      w: float) -> None: ...

    def set_linestyle(self: Line2D,
                      ls: str) -> None: ...

    def set_marker(self: Line2D,
                   marker: Any) -> Optional[Any]: ...

    def set_markeredgecolor(self: Line2D,
                            ec: Any) -> None: ...

    def set_markeredgewidth(self: Line2D,
                            ew: float) -> None: ...

    def set_markerfacecolor(self: Line2D,
                            fc: Any) -> None: ...

    def set_markerfacecoloralt(self: Line2D,
                               fc: Any) -> None: ...

    def set_markersize(self: Line2D,
                       sz: float) -> None: ...

    def set_xdata(self: Line2D,
                  x: int) -> None: ...

    def set_ydata(self: Line2D,
                  y: int) -> None: ...

    def set_dashes(self: Line2D,
                   seq: Any) -> None: ...

    def update_from(self: Line2D,
                    other: {_transform, _transformSet, _visible, _alpha, clipbox, _clipon, _clippath, _label, _sketch,
                            _path_effects, sticky_edges}) -> None: ...

    def set_dash_joinstyle(self: Line2D,
                           s: Any) -> Optional[Any]: ...

    def set_solid_joinstyle(self: Line2D,
                            s: Any) -> Optional[Any]: ...

    def get_dash_joinstyle(self: Line2D) -> Any: ...

    def get_solid_joinstyle(self: Line2D) -> Any: ...

    def set_dash_capstyle(self: Line2D,
                          s: Any) -> Optional[Any]: ...

    def set_solid_capstyle(self: Line2D,
                           s: Any) -> Optional[Any]: ...

    def get_dash_capstyle(self: Line2D) -> Any: ...

    def get_solid_capstyle(self: Line2D) -> Any: ...

    def is_dashed(self: Line2D) -> bool: ...


class _AxLine(Line2D):
    _xy1: Any
    _transformed_path: None
    _slope: None
    _xy2: None

    def __init__(self: _AxLine,
                 xy1: Any,
                 xy2: Any,
                 slope: Any,
                 **kwargs) -> Any: ...

    def get_transform(self: _AxLine) -> Union[Union[{input_dims, output_dims}, {output_dims,
                                                                                input_dims}, CompositeAffine2D, CompositeGenericTransform, _NotImplementedType], Any]: ...

    def draw(self: _AxLine,
             renderer: {open_group, close_group}) -> None: ...


class VertexSelector(object):
    canvas: Any
    line: {axes, get_picker}
    axes: Any
    ind: set[Any]
    cid: Any

    def __init__(self: VertexSelector,
                 line: {axes, get_picker}) -> Any: ...

    def process_selected(self: VertexSelector,
                         ind: Iterable[int],
                         xs: Union[ndarray, Iterable, int, float],
                         ys: Union[ndarray, Iterable, int, float]) -> None: ...

    def onpick(self: VertexSelector,
               event: {artist, ind}) -> None: ...


lineStyles: dict[str, str]
lineMarkers: dict[Union[str, Any], Union[str, Any]]
drawStyles: dict[Any, Any]
fillStyles: tuple[str, str, str, str, str, str]
