from matplotlib import legend_handler as legend_handler
from matplotlib.container import StemContainer as StemContainer
from matplotlib.container import BarContainer as BarContainer
from matplotlib.container import ErrorbarContainer as ErrorbarContainer
from matplotlib.offsetbox import DraggableOffsetBox as DraggableOffsetBox
from matplotlib.offsetbox import DrawingArea as DrawingArea
from matplotlib.offsetbox import TextArea as TextArea
from matplotlib.offsetbox import VPacker as VPacker
from matplotlib.offsetbox import HPacker as HPacker
from matplotlib.transforms import BboxTransformFrom as BboxTransformFrom
from matplotlib.transforms import BboxTransformTo as BboxTransformTo
from matplotlib.transforms import TransformedBbox as TransformedBbox
from matplotlib.transforms import BboxBase as BboxBase
from matplotlib.transforms import Bbox as Bbox
from matplotlib.collections import PolyCollection as PolyCollection
from matplotlib.collections import PathCollection as PathCollection
from matplotlib.collections import CircleCollection as CircleCollection
from matplotlib.collections import RegularPolyCollection as RegularPolyCollection
from matplotlib.collections import LineCollection as LineCollection
from matplotlib.patches import StepPatch as StepPatch
from matplotlib.patches import FancyBboxPatch as FancyBboxPatch
from matplotlib.patches import Shadow as Shadow
from matplotlib.patches import Rectangle as Rectangle
from matplotlib.patches import Patch as Patch
from matplotlib.lines import Line2D as Line2D
from matplotlib.font_manager import FontProperties as FontProperties
from matplotlib.cbook import silent_list as silent_list
from matplotlib.artist import allow_rasterization as allow_rasterization
from matplotlib.artist import Artist as Artist
from matplotlib import colors as colors
from matplotlib import docstring as docstring
from matplotlib import _api as _api
from typing import Any
from typing import ClassVar
from typing import Generator
from typing import Iterable
from typing import Optional
from typing import Tuple
from typing import Type
from typing import Union

from matplotlib.artist import Artist
from matplotlib.cbook import silent_list
from matplotlib.legend import DraggableLegend
from matplotlib.legend import Legend
from matplotlib.legend_handler import HandlerCircleCollection
from matplotlib.legend_handler import HandlerErrorbar
from matplotlib.legend_handler import HandlerLine2D
from matplotlib.legend_handler import HandlerLineCollection
from matplotlib.legend_handler import HandlerPatch
from matplotlib.legend_handler import HandlerRegularPolyCollection
from matplotlib.legend_handler import HandlerStem
from matplotlib.legend_handler import HandlerStepPatch
from matplotlib.legend_handler import HandlerTuple
from matplotlib.offsetbox import DraggableOffsetBox
from matplotlib.patches import FancyBboxPatch
from matplotlib.transforms import TransformedBbox


class DraggableLegend(DraggableOffsetBox):
    legend: Any
    _update: Optional[str]

    def __init__(self: DraggableLegend,
                 legend: Any,
                 use_blit: Optional[bool] = False,
                 update: Optional[str] = "loc") -> None: ...

    def finalize_offset(self: DraggableLegend) -> None: ...

    def _update_loc(self: DraggableLegend,
                    loc_in_canvas: Union[tuple[Any, Any], Any]) -> None: ...

    def _update_bbox_to_anchor(self: DraggableLegend,
                               loc_in_canvas: Any) -> None: ...


class Legend(Artist):
    codes: ClassVar[dict[Union[str, Any], Union[int, Any]]]
    zorder: ClassVar[int]
    _loc: ClassVar[property]
    _default_handler_map: ClassVar[dict[Union[Type[Union[
        StemContainer, ErrorbarContainer, Line2D, Patch, StepPatch, LineCollection, RegularPolyCollection, CircleCollection, BarContainer, tuple]], Any],
                                        Union[Union[
                                                  HandlerStem, HandlerErrorbar, HandlerLine2D, HandlerPatch, HandlerStepPatch, HandlerLineCollection, HandlerRegularPolyCollection, HandlerCircleCollection, HandlerTuple], Any]]]
    draw_frame: ClassVar[Callable[[Legend, bool], None]]
    isaxes: bool
    legendPatch: FancyBboxPatch
    parent: Union[Axes, Figure]
    _loc_used_default: Any
    _default_handler_map: Any
    _legend_title_box: None
    legendHandles: list[Any]
    axes: Axes
    _loc_real: Any
    _legend_handle_box: HPacker
    _bbox_to_anchor: None
    _mode: Any
    _fontsize: Optional[Any]
    _legend_box: None
    stale: bool
    texts: list[Any]
    _scatteryoffsets: None
    _draggable: None
    prop: FontProperties
    _custom_handler_map: Any
    _ncol: int

    def __str__(self: Legend) -> str: ...

    def __init__(self: Legend,
                 parent: Any,
                 handles: Any,
                 labels: Iterable[str],
                 loc: Optional[{__eq__}] = None,
                 numpoints: Any = None,
                 markerscale: Any = None,
                 markerfirst: bool = True,
                 scatterpoints: Any = None,
                 scatteryoffsets: Any = None,
                 prop: Any = None,
                 fontsize: Any = None,
                 labelcolor: Any = None,
                 borderpad: Any = None,
                 labelspacing: Any = None,
                 handlelength: Any = None,
                 handleheight: Any = None,
                 handletextpad: Any = None,
                 borderaxespad: Any = None,
                 columnspacing: Any = None,
                 ncol: int = 1,
                 mode: Any = None,
                 fancybox: Any = None,
                 shadow: Any = None,
                 title: Any = None,
                 title_fontsize: Any = None,
                 framealpha: Any = None,
                 edgecolor: Optional[{__eq__}] = None,
                 facecolor: Optional[{__eq__}] = None,
                 bbox_to_anchor: Any = None,
                 bbox_transform: Any = None,
                 frameon: Any = None,
                 handler_map: Any = None) -> Any: ...

    def _set_artist_props(self: Legend,
                          a: Union[FancyBboxPatch, Any]) -> None: ...

    def _set_loc(self: Legend,
                 loc: Any) -> None: ...

    def _get_loc(self: Legend) -> Any: ...

    def _findoffset(self: Legend,
                    width: Any,
                    height: Any,
                    xdescent: Any,
                    ydescent: Any,
                    renderer: Any) -> Tuple[Any, Any]: ...

    def draw(self: Legend,
             renderer: {open_group, points_to_pixels, get_rasterized, get_agg_filter, figure, close_group}) -> Optional[
        Any]: ...

    def get_default_handler_map(cls: Type[Legend]) -> dict[Union[Type[Union[
        StemContainer, ErrorbarContainer, Line2D, Patch, StepPatch, LineCollection, RegularPolyCollection, CircleCollection, BarContainer, Tuple]], Any],
                                                           Union[Union[
                                                                     HandlerStem, HandlerErrorbar, HandlerLine2D, HandlerPatch, HandlerStepPatch, HandlerLineCollection, HandlerRegularPolyCollection, HandlerCircleCollection, HandlerTuple], Any]]: ...

    def set_default_handler_map(cls: Type[Legend],
                                handler_map: Any) -> None: ...

    def update_default_handler_map(cls: Type[Legend],
                                   handler_map: Any) -> None: ...

    def get_legend_handler_map(self: Legend) -> dict[Union[Type[Union[
        StemContainer, ErrorbarContainer, Line2D, Patch, StepPatch, LineCollection, RegularPolyCollection, CircleCollection, BarContainer, Tuple]], Any],
                                                     Union[Union[
                                                               HandlerStem, HandlerErrorbar, HandlerLine2D, HandlerPatch, HandlerStepPatch, HandlerLineCollection, HandlerRegularPolyCollection, HandlerCircleCollection, HandlerTuple], Any]]: ...

    def get_legend_handler(legend_handler_map: Union[dict[Union[Type[Union[
        StemContainer, ErrorbarContainer, Line2D, Patch, StepPatch, LineCollection, RegularPolyCollection, CircleCollection, BarContainer, tuple]], Any],
                                                          Union[Union[
                                                                    HandlerStem, HandlerErrorbar, HandlerLine2D, HandlerPatch, HandlerStepPatch, HandlerLineCollection, HandlerRegularPolyCollection, HandlerCircleCollection, HandlerTuple], Any]], Any],
                           orig_handle: Any) -> Union[Union[
                                                          HandlerStem, HandlerErrorbar, HandlerLine2D, HandlerPatch, HandlerStepPatch, HandlerLineCollection, HandlerRegularPolyCollection, HandlerCircleCollection, HandlerTuple, None], Any]: ...

    def _init_legend_box(self: Legend,
                         handles: Union[list[Any], Any],
                         labels: Any,
                         markerfirst: bool = True) -> None: ...

    def _auto_legend_data(self: Legend) -> Any: ...

    def get_children(self: Legend) -> list[Union[FancyBboxPatch, Any]]: ...

    def get_frame(self: Legend) -> FancyBboxPatch: ...

    def get_lines(self: Legend) -> list[Line2D]: ...

    def get_patches(self: Legend) -> silent_list: ...

    def get_texts(self: Legend) -> silent_list: ...

    def set_title(self: Legend,
                  title: Any,
                  prop: Any = None) -> None: ...

    def get_title(self: Legend) -> Any: ...

    def get_window_extent(self: Legend,
                          renderer: Any = None) -> Any: ...

    def get_tightbbox(self: Legend,
                      renderer: Any) -> Any: ...

    def get_frame_on(self: Legend) -> bool: ...

    def set_frame_on(self: Legend,
                     b: bool) -> None: ...

    def get_bbox_to_anchor(self: Legend) -> Union[TransformedBbox, Any]: ...

    def set_bbox_to_anchor(self: Legend,
                           bbox: Any,
                           transform: Any = None) -> None: ...

    def _get_anchored_bbox(self: Legend,
                           loc: int,
                           bbox: Any,
                           parentbbox: Any,
                           renderer: {points_to_pixels}) -> Tuple[Any, Any]: ...

    def _find_best_position(self: Legend,
                            width: Any,
                            height: Any,
                            renderer: Any,
                            consider: Any = None) -> Tuple[Any, Any]: ...

    def contains(self: Legend,
                 event: {canvas}) -> Union[Tuple[Any, Any], Any]: ...

    def set_draggable(self: Legend,
                      state: bool,
                      use_blit: Optional[bool] = False,
                      update: Optional[str] = 'loc') -> Any: ...

    def get_draggable(self: Legend) -> Any: ...


def _get_legend_handles(axs: {__iter__},
                        legend_handler_map: Union[dict[Any, Any], Any] = None) -> Generator[Any, Any, None]: ...


def _get_legend_handles_labels(axs: Any,
                               legend_handler_map: Union[dict[Any, Any], Any] = None) -> Tuple[
    list[Any], list[Any]]: ...


def _parse_legend_args(*args,
                       axs: Any,
                       handles: Any = None,
                       labels: Any = None,
                       **kwargs) -> Any: ...