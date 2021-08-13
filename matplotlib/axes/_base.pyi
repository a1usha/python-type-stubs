from typing import Any
from typing import Iterable
from typing import Optional
from typing import Union
from typing import tuple

from matplotlib.text import Text


class _AxesBase(Artist):
    def __str__(self: _AxesBase) -> str: ...

    @_api.make_keyword_only
    def __init__(self: _AxesBase,
                 fig: Any,
                 rect: Any,
                 facecolor: Any = None,
                 frameon: bool = True,
                 sharex: Any = None,
                 sharey: Any = None,
                 label: str = '',
                 xscale: Any = None,
                 yscale: Any = None,
                 box_aspect: Optional[float] = None,
                 **kwargs) -> Any: ...

    def __getstate__(self: _AxesBase) -> dict[str, Any]: ...

    def __setstate__(self: _AxesBase,
                     state: {pop}) -> None: ...

    def __repr__(self: _AxesBase) -> str: ...

    def get_window_extent(self: _AxesBase,
                          *args,
                          **kwargs) -> TransformedBbox: ...

    def _init_axis(self: _AxesBase) -> None: ...

    def set_figure(self: _AxesBase,
                   fig: {transSubfigure}) -> None: ...

    def _unstale_viewLim(self: _AxesBase) -> None: ...

    @property
    def viewLim(self: _AxesBase) -> Bbox: ...

    def _request_autoscale_view(self: _AxesBase,
                                tight: Optional[bool] = None,
                                scalex: bool = True,
                                scaley: bool = True) -> None: ...

    def _set_lim_and_transforms(self: _AxesBase) -> None: ...

    def get_xaxis_transform(self: _AxesBase,
                            which: str = 'grid') -> Union[BlendedAffine2D, BlendedGenericTransform]: ...

    def get_xaxis_text1_transform(self: _AxesBase,
                                  pad_points: Any) -> Any: ...

    def get_xaxis_text2_transform(self: _AxesBase,
                                  pad_points: {__truediv__}) -> Any: ...

    def get_yaxis_transform(self: _AxesBase,
                            which: str = 'grid') -> Union[BlendedAffine2D, BlendedGenericTransform]: ...

    def get_yaxis_text1_transform(self: _AxesBase,
                                  pad_points: Any) -> Any: ...

    def get_yaxis_text2_transform(self: _AxesBase,
                                  pad_points: {__truediv__}) -> Any: ...

    def _update_transScale(self: _AxesBase) -> None: ...

    def get_position(self: _AxesBase,
                     original: bool = False) -> Any: ...

    def set_position(self: _AxesBase,
                     pos: Any,
                     which: str = 'both') -> None: ...

    def _set_position(self: _AxesBase,
                      pos: Optional[{height, width}],
                      which: str = 'both') -> None: ...

    def reset_position(self: _AxesBase) -> None: ...

    def set_axes_locator(self: _AxesBase,
                         locator: Any) -> None: ...

    def get_axes_locator(self: _AxesBase) -> Any: ...

    def _set_artist_props(self: _AxesBase,
                          a: Union[
                              Text, {axes, _remove_method, set_clip_path}, {get_label, _remove_method, get_clip_path}, {
                                  get_label, _remove_method}, {get_clip_path, get_path, get_transform, get_label,
                                                               _remove_method}, {_remove_method}, {get_clip_path,
                                                                                                   get_width,
                                                                                                   get_height, get_path,
                                                                                                   _remove_method}, {
                                  set_clip_path, _remove_method}]) -> None: ...

    def _gen_axes_patch(self: _AxesBase) -> Any: ...

    def _gen_axes_spines(self: _AxesBase,
                         locations: Any = None,
                         offset: float = 0.0,
                         units: str = 'inches') -> dict: ...

    def sharex(self: _AxesBase,
               other: {xaxis, get_xlim, get_autoscalex_on}) -> Any: ...

    def sharey(self: _AxesBase,
               other: {yaxis, get_ylim, get_autoscaley_on}) -> Any: ...

    def cla(self: _AxesBase) -> None: ...

    def clear(self: _AxesBase) -> None: ...

    def get_facecolor(self: _AxesBase) -> Any: ...

    def set_facecolor(self: _AxesBase,
                      color: Any) -> Any: ...

    def _set_title_offset_trans(self: _AxesBase,
                                title_offset_points: Optional[Any]) -> None: ...

    def set_prop_cycle(self: _AxesBase,
                       *args,
                       **kwargs) -> Any: ...

    def get_aspect(self: _AxesBase) -> str: ...

    def set_aspect(self: _AxesBase,
                   aspect: str,
                   adjustable: Optional[str] = None,
                   anchor: Any = None,
                   share: bool = False) -> None: ...

    def get_adjustable(self: _AxesBase) -> str: ...

    def set_adjustable(self: _AxesBase,
                       adjustable: str,
                       share: bool = False) -> Any: ...

    def get_box_aspect(self: _AxesBase) -> Any: ...

    def set_box_aspect(self: _AxesBase,
                       aspect: Optional[float] = None) -> None: ...

    def get_anchor(self: _AxesBase) -> str: ...

    def set_anchor(self: _AxesBase,
                   anchor: str,
                   share: bool = False) -> Any: ...

    def get_data_ratio(self: _AxesBase) -> Any: ...

    def apply_aspect(self: _AxesBase,
                     position: Optional[{height, width}] = None) -> None: ...

    def axis(self: _AxesBase,
             emit: bool = True,
             *args,
             **kwargs) -> float: ...

    def get_legend(self: _AxesBase) -> Any: ...

    def get_images(self: _AxesBase) -> silent_list: ...

    def get_lines(self: _AxesBase) -> silent_list: ...

    def get_xaxis(self: _AxesBase) -> XAxis: ...

    def get_yaxis(self: _AxesBase) -> YAxis: ...

    def _sci(self: _AxesBase,
             im: Any) -> Any: ...

    def _gci(self: _AxesBase) -> Any: ...

    def has_data(self: _AxesBase) -> bool: ...

    def add_artist(self: _AxesBase,
                   a: {axes, _remove_method, set_clip_path}) -> {axes, _remove_method, set_clip_path}: ...

    def add_child_axes(self: _AxesBase,
                       ax: {_axes, stale_callback, _remove_method}) -> {_axes, stale_callback, _remove_method}: ...

    def add_collection(self: _AxesBase,
                       collection: {get_label, _remove_method, get_clip_path},
                       autolim: bool = True) -> {get_label, _remove_method, get_clip_path}: ...

    def add_image(self: _AxesBase,
                  image: {get_label, _remove_method}) -> {get_label, _remove_method}: ...

    def _update_image_limits(self: _AxesBase,
                             image: {get_extent}) -> None: ...

    def add_line(self: _AxesBase,
                 line: {get_clip_path, get_path, get_transform, get_label, _remove_method}) -> {get_clip_path, get_path,
                                                                                                get_transform,
                                                                                                get_label,
                                                                                                _remove_method}: ...

    def _add_text(self: _AxesBase,
                  txt: {_remove_method}) -> {_remove_method}: ...

    def _update_line_limits(self: _AxesBase,
                            line: {get_path, get_transform}) -> None: ...

    def add_patch(self: _AxesBase,
                  p: {get_clip_path, get_width, get_height, get_path, _remove_method}) -> {get_clip_path, get_width,
                                                                                           get_height, get_path,
                                                                                           _remove_method}: ...

    def _update_patch_limits(self: _AxesBase,
                             patch: {get_width, get_height, get_path}) -> None: ...

    def add_table(self: _AxesBase,
                  tab: {set_clip_path, _remove_method}) -> {set_clip_path, _remove_method}: ...

    def add_container(self: _AxesBase,
                      container: {get_label, _remove_method}) -> {get_label, _remove_method}: ...

    def _unit_change_handler(self: _AxesBase,
                             axis_name: str,
                             event: Any = None) -> partial: ...

    def relim(self: _AxesBase,
              visible_only: bool = False) -> None: ...

    def update_datalim(self: _AxesBase,
                       xys: int,
                       updatex: bool = True,
                       updatey: bool = True) -> None: ...

    @_api.deprecated
    def update_datalim_bounds(self: _AxesBase,
                              bounds: Any) -> Optional[Any]: ...

    def _process_unit_info(self: _AxesBase,
                           datasets: Iterable = None,
                           kwargs: dict = None,
                           convert: bool = True) -> list: ...

    def in_axes(self: _AxesBase,
                mouseevent: Any) -> Any: ...

    def get_autoscale_on(self: _AxesBase) -> bool: ...

    def get_autoscalex_on(self: _AxesBase) -> bool: ...

    def get_autoscaley_on(self: _AxesBase) -> bool: ...

    def set_autoscale_on(self: _AxesBase,
                         b: bool) -> None: ...

    def set_autoscalex_on(self: _AxesBase,
                          b: bool) -> None: ...

    def set_autoscaley_on(self: _AxesBase,
                          b: bool) -> None: ...

    @property
    def use_sticky_edges(self: _AxesBase) -> bool: ...

    @use_sticky_edges.setter
    def use_sticky_edges(self: _AxesBase,
                         b: Any) -> None: ...

    def set_xmargin(self: _AxesBase,
                    m: Any) -> Any: ...

    def set_ymargin(self: _AxesBase,
                    m: Any) -> Any: ...

    def margins(self: _AxesBase,
                x: Optional[float] = None,
                y: Optional[float] = None,
                tight: Optional[bool] = True,
                *args) -> float: ...

    def set_rasterization_zorder(self: _AxesBase,
                                 z: Optional[float]) -> None: ...

    def get_rasterization_zorder(self: _AxesBase) -> Any: ...

    def autoscale(self: _AxesBase,
                  enable: Optional[bool] = True,
                  axis: str = 'both',
                  tight: Optional[bool] = None) -> None: ...

    def autoscale_view(self: _AxesBase,
                       tight: Optional[bool] = None,
                       scalex: bool = True,
                       scaley: bool = True) -> None: ...

    def _get_axis_list(self: _AxesBase) -> tuple[XAxis, YAxis]: ...

    def _get_axis_map(self: _AxesBase) -> dict[str, Any]: ...

    def _update_title_position(self: _AxesBase,
                               renderer: Optional[{open_group, option_image_nocomposite, close_group}]) -> None: ...

    @martist.allow_rasterization
    @_api.delete_parameter
    def draw(self: _AxesBase,
             renderer: Optional[{open_group, option_image_nocomposite, close_group}] = None,
             inframe: bool = False) -> Optional[Any]: ...

    def draw_artist(self: _AxesBase,
                    a: {draw}) -> Any: ...

    def redraw_in_frame(self: _AxesBase) -> Any: ...

    def get_renderer_cache(self: _AxesBase) -> Any: ...

    def get_frame_on(self: _AxesBase) -> bool: ...

    def set_frame_on(self: _AxesBase,
                     b: bool) -> None: ...

    def get_axisbelow(self: _AxesBase) -> Any: ...

    def set_axisbelow(self: _AxesBase,
                      b: Any) -> Any: ...

    @docstring.dedent_interpd
    def grid(self: _AxesBase,
             b: Optional[bool] = None,
             which: Optional[str] = 'major',
             axis: Optional[str] = 'both',
             **kwargs) -> Optional[Any]: ...

    def ticklabel_format(self: _AxesBase,
                         axis: str = 'both',
                         style: str = '',
                         scilimits: Any = None,
                         useOffset: Union[bool, float] = None,
                         useLocale: bool = None,
                         useMathText: bool = None) -> Any: ...

    def locator_params(self: _AxesBase,
                       axis: str = 'both',
                       tight: Optional[bool] = None,
                       **kwargs) -> None: ...

    def tick_params(self: _AxesBase,
                    axis: str = 'both',
                    **kwargs) -> None: ...

    def set_axis_off(self: _AxesBase) -> None: ...

    def set_axis_on(self: _AxesBase) -> None: ...

    def get_xlabel(self: _AxesBase) -> str: ...

    def set_xlabel(self: _AxesBase,
                   xlabel: str,
                   fontdict: Any = None,
                   labelpad: float = None,
                   loc: str = None x: Any = ...,
                   y: Any = ...,
                   text: str = ...,
                   color: Any = ...,
                   verticalalignment: Any = ...,
                   horizontalalignment: Any = ...,
                   multialignment: Any = ...,
                   fontproperties: Any = ...,
                   rotation: float = ...,
                   linespacing: Any = ...,
                   rotation_mode: Optional[str] = ...,
                   usetex: Any = ...,
                   wrap: bool = ...,
                   transform_rotates_text: bool = ...,
                   **kwargs) -> Text: ...

    def invert_xaxis(self: _AxesBase) -> None: ...

    def get_xbound(self: _AxesBase) -> tuple[float, float]: ...

    def set_xbound(self: _AxesBase,
                   lower: Optional[float] = None,
                   upper: Optional[float] = None) -> None: ...

    def get_xlim(self: _AxesBase) -> tuple[float, float]: ...

    def _validate_converted_limits(self: _AxesBase,
                                   limit: Optional[float],
                                   convert: Union[(x: Any)) -> Any: ...

    def set_xlim(self: _AxesBase,
                 left: Optional[float] = None,
                 right: Optional[float] = None,
                 emit: bool = True,
                 auto: Optional[bool] = False,
                 xmin: Optional[float] = None,
                 xmax: Optional[float] = None) -> tuple[float, float]: ...

    def set_xscale(self: _AxesBase,
                   value: str,
                   **kwargs) -> None: ...

    def get_ylabel(self: _AxesBase) -> str: ...

    def set_ylabel(self: _AxesBase,
                   ylabel: str,
                   fontdict: Any = None,
                   labelpad: float = None,
                   loc: str = None x: Any = ...,
                   y: Any = ...,
                   text: str = ...,
                   color: Any = ...,
                   verticalalignment: Any = ...,
                   horizontalalignment: Any = ...,
                   multialignment: Any = ...,
                   fontproperties: Any = ...,
                   rotation: float = ...,
                   linespacing: Any = ...,
                   rotation_mode: Optional[str] = ...,
                   usetex: Any = ...,
                   wrap: bool = ...,
                   transform_rotates_text: bool = ...,
                   **kwargs) -> Text: ...

    def invert_yaxis(self: _AxesBase) -> None: ...

    def get_ybound(self: _AxesBase) -> tuple[float, float]: ...

    def set_ybound(self: _AxesBase,
                   lower: Optional[float] = None,
                   upper: Optional[float] = None) -> None: ...

    def get_ylim(self: _AxesBase) -> tuple[float, float]: ...

    def set_ylim(self: _AxesBase,
                 bottom: Optional[float] = None,
                 top: Optional[float] = None,
                 emit: bool = True,
                 auto: Optional[bool] = False,
                 ymin: Optional[float] = None,
                 ymax: Optional[float] = None) -> tuple[float, float]: ...

    def set_yscale(self: _AxesBase,
                   value: str,
                   **kwargs) -> None: ...

    def format_xdata(self: _AxesBase,
                     x: Any) -> Any: ...

    def format_ydata(self: _AxesBase,
                     y: Any) -> Any: ...

    def format_coord(self: _AxesBase,
                     x: Any,
                     y: Any) -> str: ...

    def minorticks_on(self: _AxesBase) -> None: ...

    def minorticks_off(self: _AxesBase) -> None: ...

    def can_zoom(self: _AxesBase) -> bool: ...

    def can_pan(self: _AxesBase) -> bool: ...

    def get_navigate(self: _AxesBase) -> bool: ...

    def set_navigate(self: _AxesBase,
                     b: bool) -> None: ...

    def get_navigate_mode(self: _AxesBase) -> Optional[Any]: ...

    def set_navigate_mode(self: _AxesBase,
                          b: Optional[Any]) -> None: ...

    def _get_view(self: _AxesBase) -> tuple[float, float, float, float]: ...

    def _set_view(self: _AxesBase,
                  view: Any) -> None: ...

    def _set_view_from_bbox(self: _AxesBase,
                            bbox: Any,
                            direction: str = 'in',
                            mode: Optional[str] = None,
                            twinx: bool = False,
                            twiny: bool = False) -> None: ...

    def start_pan(self: _AxesBase,
                  x: float,
                  y: float,
                  button: Any) -> None: ...

    def end_pan(self: _AxesBase) -> None: ...

    def drag_pan(self: _AxesBase,
                 button: Any,
                 key: Optional[str],
                 x: float,
                 y: float) -> None: ...

    def get_children(self: _AxesBase) -> list[Text]: ...

    def contains(self: _AxesBase,
                 mouseevent: MouseEvent) -> tuple[Any, Any]: ...

    def contains_point(self: _AxesBase,
                       point: Any) -> Any: ...

    def get_default_bbox_extra_artists(self: _AxesBase) -> list[Text]: ...

    def get_tightbbox(self: _AxesBase,
                      renderer: Any,
                      call_axes_locator: bool = True,
                      bbox_extra_artists: Any = None,
                      for_layout_only: Any = False) -> Any: ...

    def _make_twin_axes(self: _AxesBase,
                        *args,
                        **kwargs) -> Any: ...

    def twinx(self: _AxesBase) -> Any: ...

    def twiny(self: _AxesBase) -> Any: ...

    def get_shared_x_axes(self: _AxesBase) -> Grouper: ...

    def get_shared_y_axes(self: _AxesBase) -> Grouper: ...


class _process_plot_var_args(object):
    def __init__(self: _process_plot_var_args,
                 axes: Any,
                 command: str = 'plot') -> None: ...

    def __getstate__(self: _process_plot_var_args) -> dict[str, str]: ...

    def __setstate__(self: _process_plot_var_args,
                     state: {copy}) -> None: ...

    def set_prop_cycle(self: _process_plot_var_args,
                       *args,
                       **kwargs) -> None: ...

    def __call__(self: _process_plot_var_args,
                 data: Any = None,
                 *args,
                 **kwargs) -> Generator[Any, Any, None]: ...

    def get_next_color(self: _process_plot_var_args) -> str: ...

    def _getdefaults(self: _process_plot_var_args,
                     ignore: Union[set, set[str]],
                     kw: {get}) -> dict: ...

    def _setdefaults(self: _process_plot_var_args,
                     defaults: dict,
                     kw: {get}) -> None: ...

    def _makeline(self: _process_plot_var_args,
                  x: Any,
                  y: Any,
                  kw: Any,
                  kwargs: Any) -> tuple[Line2D, dict]: ...

    def _makefill(self: _process_plot_var_args,
                  x: Any,
                  y: Any,
                  kw: Any,
                  kwargs: Any) -> tuple[Polygon, Any]: ...

    def _plot_args(self: _process_plot_var_args,
                   tup: Union[Iterable, tuple],
                   kwargs: dict,
                   return_kwargs: bool = False) -> Any: ...


class _axis_method_wrapper(object):
    def __init__(self: _axis_method_wrapper,
                 attr_name: Any,
                 method_name: Any,
                 doc_sub: Any = None) -> None: ...

    def __set_name__(self: _axis_method_wrapper,
                     owner: {__module__, __qualname__},
                     name: Any) -> Any: ...


class _TransformedBoundsLocator(object):
    def __init__(self: _TransformedBoundsLocator,
                 bounds: Any,
                 transform: Any) -> None: ...

    def __call__(self: _TransformedBoundsLocator,
                 ax: {figure},
                 renderer: Any) -> TransformedBbox: ...


def _process_plot_format(fmt: {__ne__, __len__, __getitem__}) -> Union[
    tuple[None, None, Union[Iterable, tuple]], tuple[str, str, Union[Iterable, tuple, None]]]: ...