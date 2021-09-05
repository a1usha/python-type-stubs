from matplotlib.rcsetup import validate_axisbelow as validate_axisbelow
from matplotlib.rcsetup import cycler as cycler
from matplotlib import docstring as docstring
from matplotlib.cbook import index_of as index_of
from matplotlib.cbook import _check_1d as _check_1d
from matplotlib.cbook import _OrderedSet as _OrderedSet
from matplotlib import cbook as cbook
from matplotlib import _api as _api
from operator import attrgetter as attrgetter
from numbers import Real as Real
from contextlib import ExitStack as ExitStack
from collections import OrderedDict as OrderedDict
from functools import partial
from typing import Any
from typing import Callable
from typing import ClassVar
from typing import Generator
from typing import Iterable
from typing import Optional
from typing import Tuple
from typing import Union

from matplotlib import _api
from matplotlib.artist import Artist
from matplotlib.axes._base import _AxesBase
from matplotlib.axes._base import _TransformedBoundsLocator
from matplotlib.axes._base import _axis_method_wrapper
from matplotlib.axes._base import _process_plot_var_args
from matplotlib.axis import XAxis
from matplotlib.axis import YAxis
from matplotlib.backend_bases import MouseEvent
from matplotlib.cbook import Grouper
from matplotlib.cbook import silent_list
from matplotlib.text import Text
from matplotlib.transforms import Bbox
from matplotlib.transforms import BlendedAffine2D
from matplotlib.transforms import BlendedGenericTransform
from matplotlib.transforms import TransformedBbox
from object import object


class _axis_method_wrapper(object):
    _missing_subs: list[str]
    method_name: Any
    attr_name: Any

    def __init__(self: _axis_method_wrapper,
                 attr_name: Any,
                 method_name: Any,
                 *,
                 doc_sub: Any = None) -> None: ...

    def __set_name__(self: _axis_method_wrapper,
                     owner: {__module__, __qualname__},
                     name: Any) -> Any: ...


class _TransformedBoundsLocator(object):
    _transform: Any
    _bounds: Any

    def __init__(self: _TransformedBoundsLocator,
                 bounds: Any,
                 transform: Any) -> None: ...

    def __call__(self: _TransformedBoundsLocator,
                 ax: {figure},
                 renderer: Any) -> TransformedBbox: ...


def _process_plot_format(fmt: {__ne__, __len__, __getitem__}) -> Union[Tuple[None, None, Union[Iterable, Tuple]], Tuple[
    Union[str, Any], Union[str, Any], Union[Union[Iterable, Tuple, None], Any]]]: ...


class _process_plot_var_args(object):
    prop_cycler: cycle[Any]
    _prop_keys: set[Any]
    axes: Any
    __dict__: dict[str, Any]
    command: str

    def __init__(self: _process_plot_var_args,
                 axes: Any,
                 command: str = 'plot') -> None: ...

    def __getstate__(self: _process_plot_var_args) -> dict[str, Union[str, Any]]: ...

    def __setstate__(self: _process_plot_var_args,
                     state: {copy}) -> None: ...

    def set_prop_cycle(self: _process_plot_var_args,
                       *args,
                       **kwargs) -> None: ...

    def __call__(self: _process_plot_var_args,
                 data: Any = None,
                 *args,
                 **kwargs) -> Generator[Any, Any, None]: ...

    def get_next_color(self: _process_plot_var_args) -> Union[str, Any]: ...

    def _getdefaults(self: _process_plot_var_args,
                     ignore: Union[Union[set[Any], set[Union[str, Any]]], Any],
                     kw: {get}) -> Union[dict[Any, Any], Any]: ...

    def _setdefaults(self: _process_plot_var_args,
                     defaults: Union[dict[Any, Any], Any],
                     kw: {get}) -> None: ...

    def _makeline(self: _process_plot_var_args,
                  x: Any,
                  y: Any,
                  kw: Any,
                  kwargs: Any) -> Tuple[Line2D, dict[Any, Any]]: ...

    def _makefill(self: _process_plot_var_args,
                  x: Any,
                  y: Any,
                  kw: Any,
                  kwargs: Any) -> Tuple[Polygon, Any]: ...

    def _plot_args(self: _process_plot_var_args,
                   tup: Union[Iterable, tuple],
                   kwargs: dict,
                   return_kwargs: bool = False) -> Any: ...


class _AxesBase(Artist):
    name: ClassVar[str]
    _shared_x_axes: ClassVar[Grouper]
    _shared_y_axes: ClassVar[Grouper]
    _twinned_axes: ClassVar[Grouper]
    get_xgridlines: ClassVar[_axis_method_wrapper]
    get_xticklines: ClassVar[_axis_method_wrapper]
    get_ygridlines: ClassVar[_axis_method_wrapper]
    get_yticklines: ClassVar[_axis_method_wrapper]
    xaxis_inverted: ClassVar[_axis_method_wrapper]
    get_xscale: ClassVar[_axis_method_wrapper]
    get_xticks: ClassVar[_axis_method_wrapper]
    set_xticks: ClassVar[_axis_method_wrapper]
    get_xmajorticklabels: ClassVar[_axis_method_wrapper]
    get_xminorticklabels: ClassVar[_axis_method_wrapper]
    get_xticklabels: ClassVar[_axis_method_wrapper]
    set_xticklabels: ClassVar[_axis_method_wrapper]
    yaxis_inverted: ClassVar[_axis_method_wrapper]
    get_yscale: ClassVar[_axis_method_wrapper]
    get_yticks: ClassVar[_axis_method_wrapper]
    set_yticks: ClassVar[_axis_method_wrapper]
    get_ymajorticklabels: ClassVar[_axis_method_wrapper]
    get_yminorticklabels: ClassVar[_axis_method_wrapper]
    get_yticklabels: ClassVar[_axis_method_wrapper]
    set_yticklabels: ClassVar[_axis_method_wrapper]
    xaxis_date: ClassVar[_axis_method_wrapper]
    yaxis_date: ClassVar[_axis_method_wrapper]
    dataLim: Bbox
    _autoscaleXon: bool
    bbox: TransformedBbox
    axes: _AxesBase
    _aspect: str
    callbacks: CallbackRegistry
    _sharex: Any
    titleOffsetTrans: ScaledTranslation
    _sharey: Any
    _xaxis_transform: Union[BlendedAffine2D, BlendedGenericTransform]
    _frameon: bool
    patch: Any
    tables: list[Any]
    axison: bool
    stale: bool
    _stale_viewlim_y: bool
    collections: list[Any]
    _rasterization_zorder: None
    _originalPosition: Bbox
    fmt_ydata: None
    images: list[Any]
    _use_sticky_edges: bool
    patches: list[Any]
    legend_: None
    _get_patches_for_fill: _process_plot_var_args
    _left_title: Text
    _stale_viewlim_x: bool
    _yaxis_transform: Union[BlendedAffine2D, BlendedGenericTransform]
    fmt_xdata: None
    _mouseover_set: _OrderedSet
    _tight: bool
    ignore_existing_data_limits: bool
    _adjustable: str
    containers: list[Any]
    _stale: bool
    transAxes: BboxTransformTo
    _autoscaleYon: bool
    _ymargin: Optional[Any]
    _facecolor: Optional[Any]
    title: Text
    yaxis: YAxis
    _axisbelow: Union[bool, str]
    _axes_locator: None
    _viewLim: Bbox
    _gridOn: Optional[Any]
    xaxis: XAxis
    artists: list[Any]
    child_axes: list[Any]
    _pan_start: SimpleNamespace
    _navigate_mode: Optional[Any]
    transData: Union[{input_dims, output_dims}, {output_dims,
                                                 input_dims}, CompositeAffine2D, CompositeGenericTransform, _NotImplementedType]
    lines: list[Any]
    _right_title: Text
    _xmargin: Optional[Any]
    _get_lines: _process_plot_var_args
    _anchor: str
    _navigate: bool
    spines: Spines
    __dict__: dict[str, Any]
    texts: list[Any]
    _projection_init: None
    _current_image: None
    _autotitlepos: bool
    transLimits: BboxTransformFrom
    _colorbars: list[Any]
    _position: Bbox
    transScale: TransformWrapper

    def __str__(self: _AxesBase) -> str: ...

    @_api.make_keyword_only("3.4", "facecolor")
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

    def viewLim(self: _AxesBase) -> Bbox: ...

    def _request_autoscale_view(self: _AxesBase,
                                tight: Union[Optional[bool], Any] = None,
                                scalex: bool = True,
                                scaley: bool = True) -> None: ...

    def _set_lim_and_transforms(self: _AxesBase) -> None: ...

    def get_xaxis_transform(self: _AxesBase,
                            which: str = 'grid') -> Union[Union[BlendedAffine2D, BlendedGenericTransform], Any]: ...

    def get_xaxis_text1_transform(self: _AxesBase,
                                  pad_points: Any) -> Any: ...

    def get_xaxis_text2_transform(self: _AxesBase,
                                  pad_points: {__truediv__}) -> Any: ...

    def get_yaxis_transform(self: _AxesBase,
                            which: str = 'grid') -> Union[Union[BlendedAffine2D, BlendedGenericTransform], Any]: ...

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
                      pos: Union[Optional[{height, width}], Any],
                      which: str = 'both') -> None: ...

    def reset_position(self: _AxesBase) -> None: ...

    def set_axes_locator(self: _AxesBase,
                         locator: Any) -> None: ...

    def get_axes_locator(self: _AxesBase) -> Any: ...

    def _set_artist_props(self: _AxesBase,
                          a: Union[Union[Text, {axes, _remove_method, set_clip_path}, {get_label, _remove_method,
                                                                                       get_clip_path}, {get_label,
                                                                                                        _remove_method}, {
                                             get_clip_path, get_path, get_transform, get_label, _remove_method}, {
                                             _remove_method}, {get_clip_path, get_width, get_height, get_path,
                                                               _remove_method}, {set_clip_path,
                                                                                 _remove_method}], Any]) -> None: ...

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
                            line: Union[{get_clip_path, get_label, _remove_method}, Any]) -> None: ...

    def add_patch(self: _AxesBase,
                  p: {get_clip_path, get_width, get_height, get_path, _remove_method}) -> {get_clip_path, get_width,
                                                                                           get_height, get_path,
                                                                                           _remove_method}: ...

    def _update_patch_limits(self: _AxesBase,
                             patch: Union[{get_clip_path, _remove_method}, Any]) -> None: ...

    def add_table(self: _AxesBase,
                  tab: {set_clip_path, _remove_method}) -> {set_clip_path, _remove_method}: ...

    def add_container(self: _AxesBase,
                      container: {get_label, _remove_method}) -> {get_label, _remove_method}: ...

    def _unit_change_handler(self: _AxesBase,
                             axis_name: Union[str, Any],
                             event: Any = None) -> partial[Any]: ...

    def relim(self: _AxesBase,
              visible_only: bool = False) -> None: ...

    def update_datalim(self: _AxesBase,
                       xys: int,
                       updatex: bool = True,
                       updatey: bool = True) -> None: ...

    @_api.deprecated(
        "3.3", alternative="ax.dataLim.set(Bbox.union([ax.dataLim, bounds]))")
    def update_datalim_bounds(self: _AxesBase,
                              bounds: Any) -> Optional[Any]: ...

    def _process_unit_info(self: _AxesBase,
                           datasets: Iterable = None,
                           kwargs: dict = None,
                           *,
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

    def use_sticky_edges(self: _AxesBase) -> bool: ...

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

    def _get_axis_list(self: _AxesBase) -> Tuple[XAxis, YAxis]: ...

    def _get_axis_map(self: _AxesBase) -> dict[str, Any]: ...

    def _update_title_position(self: _AxesBase,
                               renderer: Union[
                                   Optional[{open_group, option_image_nocomposite, close_group}], Any]) -> None: ...

    @_api.delete_parameter(
        "3.3", "inframe", alternative="Axes.redraw_in_frame()")
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

    def grid(self: _AxesBase,
             b: Optional[bool] = None,
             which: Optional[str] = 'major',
             axis: Optional[str] = 'both',
             **kwargs) -> Optional[Any]: ...

    def ticklabel_format(self: _AxesBase,
                         *,
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
                   *,
                   loc: str = None,
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
                   **kwargs) -> Text: ...

    def invert_xaxis(self: _AxesBase) -> None: ...

    def get_xbound(self: _AxesBase) -> Tuple[float, float]: ...

    def set_xbound(self: _AxesBase,
                   lower: Optional[float] = None,
                   upper: Optional[float] = None) -> None: ...

    def get_xlim(self: _AxesBase) -> Tuple[float, float]: ...

    def _validate_converted_limits(self: _AxesBase,
                                   limit: Union[Optional[float], Any],
                                   convert: Union[Union[
                                                      Callable[[Any], Any], Callable[[Any], Any], Callable[[Any], Any],
                                                      Callable[[Any], Any]], Any]) -> Any: ...

    def set_xlim(self: _AxesBase,
                 left: Optional[float] = None,
                 right: Optional[float] = None,
                 emit: bool = True,
                 auto: Optional[bool] = False,
                 *,
                 xmin: Optional[float] = None,
                 xmax: Optional[float] = None) -> Tuple[float, float]: ...

    def set_xscale(self: _AxesBase,
                   value: str,
                   **kwargs) -> None: ...

    def get_ylabel(self: _AxesBase) -> str: ...

    def set_ylabel(self: _AxesBase,
                   ylabel: str,
                   fontdict: Any = None,
                   labelpad: float = None,
                   *,
                   loc: str = None,
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
                   **kwargs) -> Text: ...

    def invert_yaxis(self: _AxesBase) -> None: ...

    def get_ybound(self: _AxesBase) -> Tuple[float, float]: ...

    def set_ybound(self: _AxesBase,
                   lower: Optional[float] = None,
                   upper: Optional[float] = None) -> None: ...

    def get_ylim(self: _AxesBase) -> Tuple[float, float]: ...

    def set_ylim(self: _AxesBase,
                 bottom: Optional[float] = None,
                 top: Optional[float] = None,
                 emit: bool = True,
                 auto: Optional[bool] = False,
                 *,
                 ymin: Optional[float] = None,
                 ymax: Optional[float] = None) -> Tuple[float, float]: ...

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

    def _get_view(self: _AxesBase) -> Tuple[float, float, float, float]: ...

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

    def get_children(self: _AxesBase) -> list[Union[Text, Any]]: ...

    def contains(self: _AxesBase,
                 mouseevent: MouseEvent) -> Union[Tuple[Any, Any], Any]: ...

    def contains_point(self: _AxesBase,
                       point: Any) -> Any: ...

    def get_default_bbox_extra_artists(self: _AxesBase) -> list[Union[Text, Any]]: ...

    def get_tightbbox(self: _AxesBase,
                      renderer: Any,
                      call_axes_locator: bool = True,
                      bbox_extra_artists: Any = None,
                      *,
                      for_layout_only: Any = False) -> Any: ...

    def _make_twin_axes(self: _AxesBase,
                        *args,
                        **kwargs) -> Any: ...

    def twinx(self: _AxesBase) -> Any: ...

    def twiny(self: _AxesBase) -> Any: ...

    def get_shared_x_axes(self: _AxesBase) -> Grouper: ...

    def get_shared_y_axes(self: _AxesBase) -> Grouper: ...
