from typing import Any
from typing import Callable
from typing import Iterable
from typing import Optional
from typing import Union

from matplotlib.artist import Artist
from matplotlib.collections import LineCollection
from matplotlib.lines import Line2D
from matplotlib.patches import Rectangle
from numpy.core._multiarray_umath import ndarray


def update_from_first_child(tgt: Any,
                            src: {get_children}) -> None: ...


class HandlerBase(object):
    def __init__(self: HandlerBase,
                 xpad: float = 0.,
                 ypad: float = 0.,
                 update_func: Any = None) -> None: ...

    def _update_prop(self: HandlerBase,
                     legend_handle: Union[Line2D, Rectangle, LineCollection, {set_figure, set_clip_box, set_clip_path}],
                     orig_handle: {get_fill, get_hatch}) -> None: ...

    def _default_update_prop(self: HandlerBase,
                             legend_handle: Union[
                                 Line2D, Rectangle, LineCollection, {set_figure, set_clip_box, set_clip_path}],
                             orig_handle: Any) -> None: ...

    def update_prop(self: HandlerBase,
                    legend_handle: Union[Line2D, Rectangle, LineCollection],
                    orig_handle: {get_fill, get_hatch},
                    legend: {markerscale}) -> None: ...

    def adjust_drawing_area(self: HandlerBase,
                            legend: Any,
                            orig_handle: Any,
                            xdescent: Any,
                            ydescent: Any,
                            width: Any,
                            height: Any,
                            fontsize: Any) -> tuple[float, float, float, float]: ...

    def legend_artist(self: HandlerBase,
                      legend: Any,
                      orig_handle: Artist,
                      fontsize: int,
                      handlebox: OffsetBox) -> Any: ...

    def create_artists(self: HandlerBase,
                       legend: Any,
                       orig_handle: Any,
                       xdescent: Any,
                       ydescent: Any,
                       width: Any,
                       height: Any,
                       fontsize: Any,
                       trans: Any) -> Any: ...


class HandlerNpoints(HandlerBase):
    def __init__(self: HandlerNpoints,
                 marker_pad: float = 0.3,
                 numpoints: int = None,
                 **kwargs) -> None: ...

    def get_numpoints(self: HandlerNpoints,
                      legend: {markerscale}) -> int: ...

    def get_xdata(self: HandlerNpoints,
                  legend: {markerscale},
                  xdescent: Any,
                  ydescent: Any,
                  width: Any,
                  height: float,
                  fontsize: Any) -> tuple[Union[ndarray, tuple[ndarray, Optional[float]], list], Union[
        ndarray, tuple[ndarray, Optional[float]], list[float]]]: ...


class HandlerNpointsYoffsets(HandlerNpoints):
    def __init__(self: HandlerNpointsYoffsets,
                 numpoints: int = None,
                 yoffsets: Union[ndarray, Iterable, int, float] = None,
                 **kwargs) -> None: ...

    def get_ydata(self: HandlerNpointsYoffsets,
                  legend: Any,
                  xdescent: Any,
                  ydescent: Any,
                  width: Any,
                  height: float,
                  fontsize: Any) -> Optional[float]: ...


class HandlerLine2D(HandlerNpoints):
    def __init__(self: HandlerLine2D,
                 marker_pad: float = 0.3,
                 numpoints: int = None,
                 **kwargs) -> None: ...

    def create_artists(self: HandlerLine2D,
                       legend: {_set_artist_props, markerscale},
                       orig_handle: Any,
                       xdescent: Any,
                       ydescent: Any,
                       width: Any,
                       height: {__sub__},
                       fontsize: Any,
                       trans: Any) -> list[Line2D]: ...


class HandlerPatch(HandlerBase):
    def __init__(self: HandlerPatch,
                 patch_func: Optional[Callable] = None,
                 **kwargs) -> None: ...

    def _create_patch(self: HandlerPatch,
                      legend: Any,
                      orig_handle: Any,
                      xdescent: Any,
                      ydescent: Any,
                      width: Any,
                      height: Any,
                      fontsize: Any) -> Rectangle: ...

    def create_artists(self: HandlerPatch,
                       legend: Any,
                       orig_handle: Any,
                       xdescent: Any,
                       ydescent: Any,
                       width: Any,
                       height: Any,
                       fontsize: Any,
                       trans: Any) -> list[Rectangle]: ...


class HandlerStepPatch(HandlerBase):
    def __init__(self: HandlerStepPatch,
                 **kwargs) -> None: ...

    def _create_patch(self: HandlerStepPatch,
                      legend: Any,
                      orig_handle: {get_facecolor},
                      xdescent: {__neg__},
                      ydescent: {__neg__},
                      width: Any,
                      height: Any,
                      fontsize: Any) -> Rectangle: ...

    def _create_line(self: HandlerStepPatch,
                     legend: Any,
                     orig_handle: {get_edgecolor, get_linestyle, get_linewidth},
                     xdescent: Any,
                     ydescent: Any,
                     width: Any,
                     height: {__truediv__},
                     fontsize: Any) -> Line2D: ...

    def create_artists(self: HandlerStepPatch,
                       legend: Any,
                       orig_handle: {get_fill, get_hatch},
                       xdescent: Any,
                       ydescent: Any,
                       width: Any,
                       height: Any,
                       fontsize: Any,
                       trans: Any) -> list[Union[Rectangle, Line2D]]: ...


class HandlerLineCollection(HandlerLine2D):
    def get_numpoints(self: HandlerLineCollection,
                      legend: {markerscale}) -> int: ...

    def _default_update_prop(self: HandlerLineCollection,
                             legend_handle: Union[
                                 Line2D, Rectangle, LineCollection, {set_figure, set_clip_box, set_clip_path}],
                             orig_handle: {get_linewidths, _us_linestyles, get_colors}) -> None: ...

    def create_artists(self: HandlerLineCollection,
                       legend: {_set_artist_props, markerscale},
                       orig_handle: Any,
                       xdescent: Any,
                       ydescent: Any,
                       width: Any,
                       height: {__sub__},
                       fontsize: Any,
                       trans: Any) -> list[Line2D]: ...


class HandlerRegularPolyCollection(HandlerNpointsYoffsets):
    def __init__(self: HandlerRegularPolyCollection,
                 yoffsets: Union[ndarray, Iterable, int, float] = None,
                 sizes: Any = None,
                 **kwargs) -> None: ...

    def get_numpoints(self: HandlerRegularPolyCollection,
                      legend: {markerscale}) -> int: ...

    def get_sizes(self: HandlerRegularPolyCollection,
                  legend: Any,
                  orig_handle: Artist,
                  xdescent: Any,
                  ydescent: Any,
                  width: Any,
                  height: Any,
                  fontsize: Any) -> Union[list[float], tuple[Union[ndarray, float, None], ...], tuple[Any, ...]]: ...

    def update_prop(self: HandlerRegularPolyCollection,
                    legend_handle: Union[Line2D, Rectangle, LineCollection],
                    orig_handle: Any,
                    legend: {figure}) -> None: ...

    def create_collection(self: HandlerRegularPolyCollection,
                          orig_handle: Artist,
                          sizes: Any,
                          offsets: Any,
                          transOffset: Any) -> Any: ...

    def create_artists(self: HandlerRegularPolyCollection,
                       legend: {_set_artist_props},
                       orig_handle: {get_numsides, get_rotation},
                       xdescent: Any,
                       ydescent: Any,
                       width: Any,
                       height: Any,
                       fontsize: Any,
                       trans: Any) -> list: ...


class HandlerPathCollection(HandlerRegularPolyCollection):
    def create_collection(self: HandlerPathCollection,
                          orig_handle: Artist,
                          sizes: Any,
                          offsets: Any,
                          transOffset: Any) -> Any: ...


class HandlerCircleCollection(HandlerRegularPolyCollection):
    def create_collection(self: HandlerCircleCollection,
                          orig_handle: Artist,
                          sizes: Any,
                          offsets: Any,
                          transOffset: Any) -> Any: ...


class HandlerErrorbar(HandlerLine2D):
    def __init__(self: HandlerErrorbar,
                 xerr_size: float = 0.5,
                 yerr_size: Any = None,
                 marker_pad: float = 0.3,
                 numpoints: int = None,
                 **kwargs) -> None: ...

    def get_err_size(self: HandlerErrorbar,
                     legend: Any,
                     xdescent: Any,
                     ydescent: Any,
                     width: Any,
                     height: Any,
                     fontsize: int) -> tuple[float, Union[float, int]]: ...

    def create_artists(self: HandlerErrorbar,
                       legend: {_set_artist_props, markerscale},
                       orig_handle: {has_xerr, has_yerr},
                       xdescent: Any,
                       ydescent: Any,
                       width: Any,
                       height: {__sub__},
                       fontsize: Any,
                       trans: Any) -> list[Line2D]: ...


class HandlerStem(HandlerNpointsYoffsets):
    def __init__(self: HandlerStem,
                 marker_pad: float = 0.3,
                 numpoints: Optional[int] = None,
                 bottom: Optional[float] = None,
                 yoffsets: Union[ndarray, Iterable, int, float, None] = None,
                 **kwargs) -> None: ...

    def get_ydata(self: HandlerStem,
                  legend: {_set_artist_props},
                  xdescent: Any,
                  ydescent: Any,
                  width: Any,
                  height: float,
                  fontsize: Any) -> Optional[float]: ...

    def create_artists(self: HandlerStem,
                       legend: {_set_artist_props},
                       orig_handle: Any,
                       xdescent: Any,
                       ydescent: Any,
                       width: Any,
                       height: Any,
                       fontsize: Any,
                       trans: Any) -> list[Line2D]: ...

    def _copy_collection_props(self: HandlerStem,
                               legend_handle: {set_color, set_linestyle},
                               orig_handle: {get_color, get_linestyle}) -> None: ...


class HandlerTuple(HandlerBase):
    def __init__(self: HandlerTuple,
                 ndivide: int = 1,
                 pad: float = None,
                 **kwargs) -> None: ...

    def create_artists(self: HandlerTuple,
                       legend: {get_legend_handler_map, get_legend_handler},
                       orig_handle: {__iter__},
                       xdescent: {__sub__},
                       ydescent: Any,
                       width: {__add__},
                       height: Any,
                       fontsize: Any,
                       trans: Any) -> list: ...


class HandlerPolyCollection(HandlerBase):
    def _update_prop(self: HandlerPolyCollection,
                     legend_handle: Union[Line2D, Rectangle, LineCollection, {set_figure, set_clip_box, set_clip_path}],
                     orig_handle: {get_fill, get_hatch}) -> None: ...

    def create_artists(self: HandlerPolyCollection,
                       legend: Any,
                       orig_handle: Any,
                       xdescent: {__neg__},
                       ydescent: {__neg__},
                       width: Any,
                       height: Any,
                       fontsize: Any,
                       trans: Any) -> list[Rectangle]: ...
