from typing import Any
from typing import Callable
from typing import Iterable
from typing import Optional
from typing import Tuple
from typing import Union

from matplotlib.artist import Artist
from matplotlib.collections import LineCollection
from matplotlib.legend_handler import HandlerBase
from matplotlib.legend_handler import HandlerCircleCollection
from matplotlib.legend_handler import HandlerErrorbar
from matplotlib.legend_handler import HandlerLine2D
from matplotlib.legend_handler import HandlerLineCollection
from matplotlib.legend_handler import HandlerNpoints
from matplotlib.legend_handler import HandlerNpointsYoffsets
from matplotlib.legend_handler import HandlerPatch
from matplotlib.legend_handler import HandlerPathCollection
from matplotlib.legend_handler import HandlerPolyCollection
from matplotlib.legend_handler import HandlerRegularPolyCollection
from matplotlib.legend_handler import HandlerStem
from matplotlib.legend_handler import HandlerStepPatch
from matplotlib.legend_handler import HandlerTuple
from matplotlib.lines import Line2D
from matplotlib.offsetbox import OffsetBox
from matplotlib.patches import Rectangle
from matplotlib.transforms import IdentityTransform
from numpy.core._multiarray_umath import ndarray
from object import object


def update_from_first_child(tgt: Any,
                            src: {get_children}) -> None: ...


class HandlerBase(object):
    def __init__(self: HandlerBase,
                 xpad: float = 0.,
                 ypad: float = 0.,
                 update_func: Any = None) -> None: ...

    def _update_prop(self: HandlerBase,
                     legend_handle: Union[
                         Union[Line2D, Rectangle, LineCollection, {set_figure, set_clip_box, set_clip_path}], Any],
                     orig_handle: Union[{get_fill, get_hatch}, Any]) -> None: ...

    def _default_update_prop(self: HandlerBase,
                             legend_handle: Union[Union[Line2D, Rectangle, LineCollection, {set_figure, set_clip_box,
                                                                                            set_clip_path}], Any],
                             orig_handle: Any) -> None: ...

    def update_prop(self: HandlerBase,
                    legend_handle: Union[Union[Line2D, Rectangle, LineCollection], Any],
                    orig_handle: Union[{get_fill, get_hatch}, Any],
                    legend: Union[{markerscale}, Any]) -> None: ...

    def adjust_drawing_area(self: HandlerBase,
                            legend: Any,
                            orig_handle: Any,
                            xdescent: Any,
                            ydescent: Any,
                            width: Any,
                            height: Any,
                            fontsize: Any) -> Tuple[
        Union[float, Any], Union[float, Any], Union[float, Any], Union[float, Any]]: ...

    def legend_artist(self: HandlerBase,
                      legend: Any,
                      orig_handle: Union[Artist, Any],
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
                      legend: Union[{markerscale}, Any]) -> Union[int, Any]: ...

    def get_xdata(self: HandlerNpoints,
                  legend: Union[{markerscale}, Any],
                  xdescent: Any,
                  ydescent: Any,
                  width: Any,
                  height: Union[float, Any],
                  fontsize: Any) -> Tuple[Union[ndarray, Tuple[ndarray, Optional[float]], list[Any]], Union[
        ndarray, Tuple[ndarray, Optional[float]], list[Union[float, Any]]]]: ...


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
                  height: Union[float, Any],
                  fontsize: Any) -> Union[Optional[float], Any]: ...


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
                      fontsize: Any) -> Union[Rectangle, Any]: ...

    def create_artists(self: HandlerPatch,
                       legend: Any,
                       orig_handle: Union[Artist, Any],
                       xdescent: Union[float, Any],
                       ydescent: Union[float, Any],
                       width: Union[float, Any],
                       height: Union[float, Any],
                       fontsize: Union[int, Any],
                       trans: Union[IdentityTransform, Any]) -> list[Union[Rectangle, Any]]: ...


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
                       orig_handle: Union[Artist, Any],
                       xdescent: Union[float, Any],
                       ydescent: Union[float, Any],
                       width: Union[float, Any],
                       height: Union[float, Any],
                       fontsize: Union[int, Any],
                       trans: Union[IdentityTransform, Any]) -> list[Union[Rectangle, Line2D]]: ...


class HandlerLineCollection(HandlerLine2D):
    def get_numpoints(self: HandlerLineCollection,
                      legend: Union[{markerscale}, Any]) -> Union[int, Any]: ...

    def _default_update_prop(self: HandlerLineCollection,
                             legend_handle: Union[Union[Line2D, Rectangle, LineCollection, {set_figure, set_clip_box,
                                                                                            set_clip_path}], Any],
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
                      legend: Union[{markerscale}, Any]) -> Union[int, Any]: ...

    def get_sizes(self: HandlerRegularPolyCollection,
                  legend: Any,
                  orig_handle: Union[Artist, Any],
                  xdescent: Any,
                  ydescent: Any,
                  width: Any,
                  height: Any,
                  fontsize: Any) -> Union[
        Union[list[Union[float, Any]], Tuple[Union[ndarray, float, None], ...], Tuple[Any, ...]], Any]: ...

    def update_prop(self: HandlerRegularPolyCollection,
                    legend_handle: Union[Union[Line2D, Rectangle, LineCollection], Any],
                    orig_handle: Any,
                    legend: {figure}) -> None: ...

    def create_collection(self: HandlerRegularPolyCollection,
                          orig_handle: Union[Artist, Any],
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
                       trans: Any) -> list[Any]: ...


class HandlerPathCollection(HandlerRegularPolyCollection):
    def create_collection(self: HandlerPathCollection,
                          orig_handle: Union[Artist, Any],
                          sizes: Any,
                          offsets: Any,
                          transOffset: Any) -> Any: ...


class HandlerCircleCollection(HandlerRegularPolyCollection):
    def create_collection(self: HandlerCircleCollection,
                          orig_handle: Union[Artist, Any],
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
                     fontsize: Union[int, Any]) -> Tuple[Union[float, Any], Union[Union[float, int], Any]]: ...

    def create_artists(self: HandlerErrorbar,
                       legend: {_set_artist_props, markerscale},
                       orig_handle: {has_xerr, has_yerr},
                       xdescent: Any,
                       ydescent: Any,
                       width: Any,
                       height: {__sub__},
                       fontsize: Any,
                       trans: Any) -> list[Union[Line2D, Any]]: ...


class HandlerStem(HandlerNpointsYoffsets):
    def __init__(self: HandlerStem,
                 marker_pad: float = 0.3,
                 numpoints: Optional[int] = None,
                 bottom: Optional[float] = None,
                 yoffsets: Union[ndarray, Iterable, int, float, None] = None,
                 **kwargs) -> None: ...

    def get_ydata(self: HandlerStem,
                  legend: Union[{_set_artist_props}, Any],
                  xdescent: Any,
                  ydescent: Any,
                  width: Any,
                  height: Union[float, Any],
                  fontsize: Any) -> Union[Optional[float], Any]: ...

    def create_artists(self: HandlerStem,
                       legend: {_set_artist_props},
                       orig_handle: Any,
                       xdescent: Any,
                       ydescent: Any,
                       width: Any,
                       height: Any,
                       fontsize: Any,
                       trans: Any) -> list[Union[Line2D, Any]]: ...

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
                       trans: Any) -> list[Any]: ...


class HandlerPolyCollection(HandlerBase):
    def _update_prop(self: HandlerPolyCollection,
                     legend_handle: Union[
                         Union[Line2D, Rectangle, LineCollection, {set_figure, set_clip_box, set_clip_path}], Any],
                     orig_handle: Union[{get_fill, get_hatch}, Any]) -> None: ...

    def create_artists(self: HandlerPolyCollection,
                       legend: Any,
                       orig_handle: Any,
                       xdescent: {__neg__},
                       ydescent: {__neg__},
                       width: Any,
                       height: Any,
                       fontsize: Any,
                       trans: Any) -> list[Rectangle]: ...
