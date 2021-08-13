from typing import Any
from typing import Iterable
from typing import Optional
from typing import Union
from typing import tuple

from numpy.core._multiarray_umath import ndarray


class Line2D(Artist):
    @_api.deprecated
    @_api.classproperty
    def validCap(cls: Line2D) -> tuple[Any, ...]: ...

    @_api.deprecated
    @_api.classproperty
    def validJoin(cls: Line2D) -> tuple[Any, ...]: ...

    def __str__(self: Line2D) -> str: ...

    def __init__(self: Line2D,
                 xdata: list[int],
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

    def get_fillstyle(self: Line2D) -> Optional[str]: ...

    def set_fillstyle(self: Line2D,
                      fs: str) -> None: ...

    def set_markevery(self: Line2D,
                      every: Any) -> None: ...

    def get_markevery(self: Line2D) -> Any: ...

    def set_picker(self: Line2D,
                   p: Any) -> None: ...

    def get_window_extent(self: Line2D,
                          renderer: Any) -> Bbox: ...

    @Artist.axes.setter
    def axes(self: Line2D,
             ax: Any) -> Optional[Any]: ...

    def set_data(self: Line2D,
                 *args) -> None: ...

    def recache_always(self: Line2D) -> None: ...

    def recache(self: Line2D,
                always: bool = False) -> None: ...

    def _transform_path(self: Line2D,
                        subslice: Optional[slice] = None) -> None: ...

    def _get_transformed_path(self: Line2D) -> Optional[Any]: ...

    def set_transform(self: Line2D,
                      t: Transform) -> None: ...

    def _is_sorted(self: Line2D,
                   x: Optional[Any]) -> None: ...

    @allow_rasterization
    def draw(self: Line2D,
             renderer: {open_group, close_group}) -> Optional[Any]: ...

    def get_antialiased(self: Line2D) -> Any: ...

    def get_color(self: Line2D) -> Any: ...

    def get_drawstyle(self: Line2D) -> Any: ...

    def get_linestyle(self: Line2D) -> str: ...

    def get_linewidth(self: Line2D) -> Optional[Any]: ...

    def get_marker(self: Line2D) -> Union[ndarray, str, Path, Sized, Iterable, int, float]: ...

    def get_markeredgecolor(self: Line2D) -> str: ...

    def get_markeredgewidth(self: Line2D) -> Any: ...

    def _get_markerfacecolor(self: Line2D,
                             alt: bool = False) -> str: ...

    def get_markerfacecolor(self: Line2D) -> str: ...

    def get_markerfacecoloralt(self: Line2D) -> str: ...

    def get_markersize(self: Line2D) -> Any: ...

    def get_data(self: Line2D,
                 orig: bool = True) -> tuple[ndarray, ndarray]: ...

    def get_xdata(self: Line2D,
                  orig: bool = True) -> ndarray: ...

    def get_ydata(self: Line2D,
                  orig: bool = True) -> ndarray: ...

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

    @docstring.interpd
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

    @docstring.interpd
    def set_dash_joinstyle(self: Line2D,
                           s: Any) -> Optional[Any]: ...

    @docstring.interpd
    def set_solid_joinstyle(self: Line2D,
                            s: Any) -> Optional[Any]: ...

    def get_dash_joinstyle(self: Line2D) -> Any: ...

    def get_solid_joinstyle(self: Line2D) -> Any: ...

    @docstring.interpd
    def set_dash_capstyle(self: Line2D,
                          s: Any) -> Optional[Any]: ...

    @docstring.interpd
    def set_solid_capstyle(self: Line2D,
                           s: Any) -> Optional[Any]: ...

    def get_dash_capstyle(self: Line2D) -> Any: ...

    def get_solid_capstyle(self: Line2D) -> Any: ...

    def is_dashed(self: Line2D) -> bool: ...


class _AxLine(Line2D):
    def __init__(self: _AxLine,
                 xy1: Any,
                 xy2: Any,
                 slope: Any,
                 **kwargs) -> Any: ...

    def get_transform(self: _AxLine) -> Union[{input_dims, output_dims}, {output_dims,
                                                                          input_dims}, CompositeAffine2D, CompositeGenericTransform, _NotImplementedType]: ...

    def draw(self: _AxLine,
             renderer: {open_group, close_group}) -> None: ...


class VertexSelector(object):
    def __init__(self: VertexSelector,
                 line: {axes, get_picker}) -> Any: ...

    def process_selected(self: VertexSelector,
                         ind: Iterable[int],
                         xs: Union[ndarray, Iterable, int, float],
                         ys: Union[ndarray, Iterable, int, float]) -> None: ...

    def onpick(self: VertexSelector,
               event: {artist, ind}) -> None: ...


def _scale_dashes(offset: int,
                  dashes: Optional[tuple],
                  lw: Optional[float]) -> Union[
    tuple[int, Optional[tuple]], tuple[Union[int, float], Optional[list[Optional[float]]]]]: ...


def _mark_every_path(markevery: Any,
                     tpath: {codes, vertices},
                     affine: Any,
                     ax_transform: Any) -> Path: ...


def _get_dash_pattern(style: str) -> tuple[int, Optional[tuple]]: ...


def segment_hits(cx: int,
                 cy: int,
                 x: {__len__},
                 y: Any,
                 radius: float) -> ndarray: ...