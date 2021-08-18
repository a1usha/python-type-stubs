from _typeshed import SupportsLessThan
from datetime import datetime
from datetime import tzinfo
from typing import Any
from typing import Iterable
from typing import Optional
from typing import Tuple
from typing import Union

from matplotlib import _api
from matplotlib.artist import Artist
from matplotlib.axes._axes import Axes
from matplotlib.axis import Axis
from matplotlib.axis import Tick
from matplotlib.axis import Ticker
from matplotlib.axis import XAxis
from matplotlib.axis import XTick
from matplotlib.axis import YAxis
from matplotlib.axis import YTick
from matplotlib.axis import _LazyTickList
from matplotlib.backend_bases import MouseEvent
from matplotlib.cbook import silent_list
from matplotlib.lines import Line2D
from matplotlib.scale import FuncTransform
from matplotlib.scale import LogTransform
from matplotlib.scale import LogitTransform
from matplotlib.scale import SymmetricalLogTransform
from matplotlib.text import Text
from matplotlib.transforms import Bbox
from matplotlib.transforms import CompositeAffine2D
from matplotlib.transforms import CompositeGenericTransform
from matplotlib.transforms import IdentityTransform
from numpy.core._multiarray_umath import ndarray
from object import object


class Tick(Artist):
    @_api.delete_parameter("3.3", "label")
    def __init__(self: Tick,
                 axes: {figure},
                 loc: Any,
                 label: Any = None,
                 size: Any = None,
                 width: Any = None,
                 color: Any = None,
                 tickdir: Any = None,
                 pad: Any = None,
                 labelsize: Any = None,
                 labelcolor: Optional[{__eq__}] = None,
                 zorder: Any = None,
                 gridOn: Any = None,
                 tick1On: bool = True,
                 tick2On: bool = True,
                 label1On: bool = True,
                 label2On: bool = False,
                 major: bool = True,
                 labelrotation: int = 0,
                 grid_color: Any = None,
                 grid_linestyle: Any = None,
                 grid_linewidth: Any = None,
                 grid_alpha: Any = None,
                 **kwargs) -> Optional[Any]: ...

    @_api.deprecated("3.1", alternative="Tick.label1", pending=True)
    def label(self: Tick) -> Text: ...

    def _set_labelrotation(self: Tick,
                           labelrotation: Union[int, Any]) -> None: ...

    def apply_tickdir(self: Tick,
                      tickdir: Any) -> None: ...

    def get_tickdir(self: Tick) -> Optional[Any]: ...

    def get_tick_padding(self: Tick) -> Union[float, Any]: ...

    def get_children(self: Tick) -> list[Union[Line2D, Text]]: ...

    def set_clip_path(self: Tick,
                      clippath: Any,
                      transform: Any = None) -> None: ...

    def get_pad_pixels(self: Tick) -> Union[float, Any]: ...

    def contains(self: Tick,
                 mouseevent: MouseEvent) -> Union[Tuple[Any, Any], Tuple[bool, dict[Any, Any]]]: ...

    def set_pad(self: Tick,
                val: float) -> None: ...

    def get_pad(self: Tick) -> Optional[Any]: ...

    def _get_text1(self: Tick) -> None: ...

    def _get_text2(self: Tick) -> None: ...

    def _get_tick1line(self: Tick) -> None: ...

    def _get_tick2line(self: Tick) -> None: ...

    def _get_gridline(self: Tick) -> None: ...

    def get_loc(self: Tick) -> Any: ...

    def draw(self: Tick,
             renderer: {open_group, get_rasterized, get_agg_filter, figure, close_group}) -> Optional[Any]: ...

    def set_label1(self: Tick,
                   s: str) -> None: ...

    def set_label2(self: Tick,
                   s: str) -> None: ...

    def set_url(self: Tick,
                url: str) -> None: ...

    def _set_artist_props(self: Tick,
                          a: Union[Union[Line2D, Text], Any]) -> None: ...

    def get_view_interval(self: Tick) -> Any: ...

    def _apply_params(self: Tick,
                      **kwargs) -> None: ...

    def update_position(self: Tick,
                        loc: Any) -> Any: ...

    def _get_text1_transform(self: Tick) -> Any: ...

    def _get_text2_transform(self: Tick) -> Any: ...


class XTick(Tick):
    def __init__(self: XTick,
                 *args,
                 **kwargs) -> None: ...

    def _get_text1_transform(self: XTick) -> Any: ...

    def _get_text2_transform(self: XTick) -> Any: ...

    def apply_tickdir(self: XTick,
                      tickdir: Any) -> None: ...

    def update_position(self: XTick,
                        loc: Any) -> None: ...

    def get_view_interval(self: XTick) -> Any: ...


class YTick(Tick):
    def __init__(self: YTick,
                 *args,
                 **kwargs) -> None: ...

    def _get_text1_transform(self: YTick) -> Any: ...

    def _get_text2_transform(self: YTick) -> Any: ...

    def apply_tickdir(self: YTick,
                      tickdir: Any) -> None: ...

    def update_position(self: YTick,
                        loc: Any) -> None: ...

    def get_view_interval(self: YTick) -> Any: ...


class Ticker(object):
    def __init__(self: Ticker) -> None: ...

    def locator(self: Ticker) -> Any: ...

    def locator(self: Ticker,
                locator: Any) -> Any: ...

    def formatter(self: Ticker) -> Any: ...

    def formatter(self: Ticker,
                  formatter: Any) -> Any: ...


class _LazyTickList(object):
    def __init__(self: _LazyTickList,
                 major: Any) -> None: ...

    def __get__(self: _LazyTickList,
                instance: Any,
                cls: Any) -> Union[_LazyTickList, list[Any]]: ...


class Axis(Artist):
    def __str__(self: Axis) -> str: ...

    def __init__(self: Axis,
                 axes: Axes,
                 pickradius: float = 15) -> None: ...

    def get_remove_overlapping_locs(self: Axis) -> bool: ...

    def set_remove_overlapping_locs(self: Axis,
                                    val: Any) -> None: ...

    def set_label_coords(self: Axis,
                         x: Any,
                         y: Any,
                         transform: Any = None) -> None: ...

    def get_transform(self: Axis) -> Union[
        IdentityTransform, LogTransform, SymmetricalLogTransform, LogitTransform, FuncTransform, {input_dims,
                                                                                                  output_dims}, {
            output_dims, input_dims}, CompositeAffine2D, CompositeGenericTransform, _NotImplementedType]: ...

    def get_scale(self: Axis) -> str: ...

    def _set_scale(self: Axis,
                   value: Union[str, Any],
                   **kwargs) -> None: ...

    def limit_range_for_scale(self: Axis,
                              vmin: {__le__},
                              vmax: {__le__, __ge__}) -> Union[
        Tuple[Any, Any], Tuple[Union[Union[float, {__le__}], Any], Union[Union[float, {__le__}], Any]], Tuple[
            Union[Union[float, {__le__}], Any], Union[Union[int, float, {__ge__}], Any]]]: ...

    def get_children(self: Axis) -> list[Union[Text, Any]]: ...

    def _reset_major_tick_kw(self: Axis) -> None: ...

    def _reset_minor_tick_kw(self: Axis) -> None: ...

    def clear(self: Axis) -> None: ...

    @_api.deprecated("3.4", alternative="Axis.clear()")
    def cla(self: Axis) -> Optional[Any]: ...

    def reset_ticks(self: Axis) -> None: ...

    def set_tick_params(self: Axis,
                        which: str = 'major',
                        reset: bool = False,
                        **kwargs) -> None: ...

    def _translate_tick_kw(kw: Union[dict[str, Any], Any]) -> dict[str, Any]: ...

    def set_clip_path(self: Axis,
                      clippath: Any,
                      transform: Any = None) -> None: ...

    def get_view_interval(self: Axis) -> Any: ...

    def set_view_interval(self: Axis,
                          vmin: Any,
                          vmax: Any,
                          ignore: bool = False) -> Any: ...

    def get_data_interval(self: Axis) -> Any: ...

    def set_data_interval(self: Axis,
                          vmin: Any,
                          vmax: Any,
                          ignore: bool = False) -> Any: ...

    def get_inverted(self: Axis) -> bool: ...

    def set_inverted(self: Axis,
                     inverted: Any) -> Any: ...

    def set_default_intervals(self: Axis) -> None: ...

    def _set_artist_props(self: Axis,
                          a: Union[Text, Any]) -> None: ...

    def get_ticklabel_extents(self: Axis,
                              renderer: Any) -> Tuple[Bbox, Bbox]: ...

    def _update_ticks(self: Axis) -> list[Any]: ...

    def _get_tick_bboxes(self: Axis,
                         ticks: Union[list[Any], Any],
                         renderer: Union[{open_group, get_rasterized, get_agg_filter, figure, close_group}, Any]) -> \
    Tuple[list[Any], list[Any]]: ...

    def get_tightbbox(self: Axis,
                      renderer: Any,
                      *,
                      for_layout_only: bool = False) -> Optional[Bbox]: ...

    def get_tick_padding(self: Axis) -> Union[Union[SupportsLessThan, int], Any]: ...

    def draw(self: Axis,
             renderer: {open_group, get_rasterized, get_agg_filter, figure, close_group},
             *args,
             **kwargs) -> Optional[Any]: ...

    def get_gridlines(self: Axis) -> silent_list: ...

    def get_label(self: Axis) -> Text: ...

    def get_offset_text(self: Axis) -> Text: ...

    def get_pickradius(self: Axis) -> float: ...

    def get_majorticklabels(self: Axis) -> list[Any]: ...

    def get_minorticklabels(self: Axis) -> list[Any]: ...

    def get_ticklabels(self: Axis,
                       minor: bool = False,
                       which: Optional[str] = None) -> Any: ...

    def get_majorticklines(self: Axis) -> silent_list: ...

    def get_minorticklines(self: Axis) -> silent_list: ...

    def get_ticklines(self: Axis,
                      minor: bool = False) -> silent_list: ...

    def get_majorticklocs(self: Axis) -> Any: ...

    def get_minorticklocs(self: Axis) -> Union[list[Any], Any]: ...

    @_api.make_keyword_only("3.3", "minor")
    def get_ticklocs(self: Axis,
                     minor: bool = False) -> Union[list[Any], Any]: ...

    def get_ticks_direction(self: Axis,
                            minor: bool = False) -> ndarray: ...

    def _get_tick(self: Axis,
                  major: Union[bool, Any]) -> Any: ...

    def _get_tick_label_size(self: Axis,
                             axis_name: Union[str, Any]) -> Optional[Any]: ...

    def _copy_tick_props(self: Axis,
                         src: Optional[{label1, label2, tick1line, tick2line, gridline}],
                         dest: Optional[{label1, label2, tick1line, tick2line, gridline}]) -> None: ...

    def get_label_text(self: Axis) -> str: ...

    def get_major_locator(self: Axis) -> Any: ...

    def get_minor_locator(self: Axis) -> Any: ...

    def get_major_formatter(self: Axis) -> Any: ...

    def get_minor_formatter(self: Axis) -> Any: ...

    def get_major_ticks(self: Axis,
                        numticks: Union[int, Any] = None) -> Union[list[Any], Any]: ...

    def get_minor_ticks(self: Axis,
                        numticks: Union[int, Any] = None) -> Union[list[Any], Any]: ...

    def grid(self: Axis,
             b: Optional[bool] = None,
             which: str = 'major',
             **kwargs) -> Any: ...

    def update_units(self: Axis,
                     data: Union[datetime, Any]) -> bool: ...

    def _update_axisinfo(self: Axis) -> None: ...

    def have_units(self: Axis) -> Any: ...

    def convert_units(self: Axis,
                      x: Union[Iterable, Any]) -> Union[Iterable, Any]: ...

    def set_units(self: Axis,
                  u: Any) -> None: ...

    def get_units(self: Axis) -> Any: ...

    def set_label_text(self: Axis,
                       label: str,
                       fontdict: dict = None,
                       **kwargs) -> Text: ...

    def set_major_formatter(self: Axis,
                            formatter: str) -> None: ...

    def set_minor_formatter(self: Axis,
                            formatter: str) -> None: ...

    def _set_formatter(self: Axis,
                       formatter: Union[str, Any],
                       level: Union[Ticker, Any]) -> None: ...

    def set_major_locator(self: Axis,
                          locator: Any) -> None: ...

    def set_minor_locator(self: Axis,
                          locator: Any) -> None: ...

    def set_pickradius(self: Axis,
                       pickradius: float) -> None: ...

    def _format_with_dict(tickd: {get},
                          x: Any,
                          pos: Any) -> Any: ...

    def set_ticklabels(self: Axis,
                       ticklabels: Any,
                       *,
                       minor: bool = False,
                       **kwargs) -> Any: ...

    @_api.make_keyword_only("3.3", "fontdict")
    def _set_ticklabels(self: Axis,
                        labels: Iterable[str],
                        fontdict: Optional[dict] = None,
                        minor: bool = False,
                        x: Any = ...,
                        y: Any = ...,
                        text: str = ...,
                        color: Any = ...,
                        verticalalignment: Any = ...,
                        horizontalalignment: Any = ...,
                        multialignment: Any = ...,
                        fontproperties: Any = ...,
                        rotation: Union[float, Any] = ...,
                        linespacing: Any = ...,
                        rotation_mode: Optional[str] = ...,
                        usetex: Any = ...,
                        wrap: bool = ...,
                        transform_rotates_text: bool = ...,
                        **kwargs) -> Any: ...

    def set_ticks(self: Axis,
                  ticks: Iterable,
                  *,
                  minor: bool = False) -> Union[list[Any], Any]: ...

    def _get_tick_boxes_siblings(self: Axis,
                                 renderer: Union[
                                     {open_group, get_rasterized, get_agg_filter, figure, close_group}, Any]) -> Tuple[
        list[Any], list[Any]]: ...

    def _update_label_position(self: Axis,
                               renderer: Union[
                                   {open_group, get_rasterized, get_agg_filter, figure, close_group}, Any]) -> Any: ...

    def _update_offset_text_position(self: Axis,
                                     bboxes: Union[list[Any], Any],
                                     bboxes2: Union[list[Any], Any]) -> Any: ...

    @_api.deprecated("3.3")
    def pan(self: Axis,
            numsteps: Any) -> Optional[Any]: ...

    @_api.deprecated("3.3")
    def zoom(self: Axis,
             direction: Any) -> Optional[Any]: ...

    def axis_date(self: Axis,
                  tz: Union[str, tzinfo] = None) -> None: ...

    def get_tick_space(self: Axis) -> Any: ...

    def _get_ticks_position(self: Axis) -> Union[int, str]: ...

    def get_label_position(self: Axis) -> Any: ...

    def set_label_position(self: Axis,
                           position: str) -> Any: ...

    def get_minpos(self: Axis) -> Any: ...


def _make_getset_interval(method_name: Union[str, Any],
                          lim_name: Union[str, Any],
                          attr_name: Union[str, Any]) -> Tuple[Callable[[Union[{stale}, Any]], Any], Callable[
    [{stale}, Union[SupportsLessThan, Any], Union[SupportsLessThan, Any], bool], None]]: ...


class XAxis(Axis):
    def __init__(self: XAxis,
                 *args,
                 **kwargs) -> None: ...

    def contains(self: XAxis,
                 mouseevent: MouseEvent) -> Union[
        Tuple[Any, Any], Tuple[bool, dict[Any, Any]], Tuple[Union[bool, Any], dict[Any, Any]]]: ...

    def _get_tick(self: XAxis,
                  major: Union[bool, Any]) -> XTick: ...

    def set_label_position(self: XAxis,
                           position: str) -> None: ...

    def _update_label_position(self: XAxis,
                               renderer: Union[
                                   {open_group, get_rasterized, get_agg_filter, figure, close_group}, Any]) -> None: ...

    def _update_offset_text_position(self: XAxis,
                                     bboxes: Union[list[Any], Any],
                                     bboxes2: Union[list[Any], Any]) -> None: ...

    def get_text_heights(self: XAxis,
                         renderer: Any) -> Tuple[float, float]: ...

    def set_ticks_position(self: XAxis,
                           position: str) -> None: ...

    def tick_top(self: XAxis) -> None: ...

    def tick_bottom(self: XAxis) -> None: ...

    def get_ticks_position(self: XAxis) -> str: ...

    def get_minpos(self: XAxis) -> Any: ...

    def set_inverted(self: XAxis,
                     inverted: Any) -> None: ...

    def set_default_intervals(self: XAxis) -> None: ...

    def get_tick_space(self: XAxis) -> Union[int, Any]: ...


class YAxis(Axis):
    def __init__(self: YAxis,
                 *args,
                 **kwargs) -> None: ...

    def contains(self: YAxis,
                 mouseevent: MouseEvent) -> Union[
        Tuple[Any, Any], Tuple[bool, dict[Any, Any]], Tuple[Union[bool, Any], dict[Any, Any]]]: ...

    def _get_tick(self: YAxis,
                  major: Union[bool, Any]) -> YTick: ...

    def set_label_position(self: YAxis,
                           position: str) -> None: ...

    def _update_label_position(self: YAxis,
                               renderer: Union[
                                   {open_group, get_rasterized, get_agg_filter, figure, close_group}, Any]) -> None: ...

    def _update_offset_text_position(self: YAxis,
                                     bboxes: Union[list[Any], Any],
                                     bboxes2: Union[list[Any], Any]) -> None: ...

    def set_offset_position(self: YAxis,
                            position: str) -> None: ...

    def get_text_widths(self: YAxis,
                        renderer: Any) -> Tuple[float, float]: ...

    def set_ticks_position(self: YAxis,
                           position: str) -> None: ...

    def tick_right(self: YAxis) -> None: ...

    def tick_left(self: YAxis) -> None: ...

    def get_ticks_position(self: YAxis) -> str: ...

    def get_minpos(self: YAxis) -> Any: ...

    def set_inverted(self: YAxis,
                     inverted: Any) -> None: ...

    def set_default_intervals(self: YAxis) -> None: ...

    def get_tick_space(self: YAxis) -> Union[int, Any]: ...
