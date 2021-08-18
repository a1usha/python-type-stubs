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
    def __init__(self: DraggableLegend,
                 legend: Any,
                 use_blit: Optional[bool] = False,
                 update: Optional[str] = "loc") -> None: ...

    def finalize_offset(self: DraggableLegend) -> None: ...

    def _update_loc(self: DraggableLegend,
                    loc_in_canvas: tuple[Any, Any]) -> None: ...

    def _update_bbox_to_anchor(self: DraggableLegend,
                               loc_in_canvas: Any) -> None: ...


class Legend(Artist):
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
                          a: FancyBboxPatch) -> None: ...

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

    def get_default_handler_map(cls: Type[Legend]) -> dict[Type[Union[
        StemContainer, ErrorbarContainer, Line2D, Patch, StepPatch, LineCollection, RegularPolyCollection, CircleCollection, BarContainer, Tuple]],
                                                           Union[
                                                               HandlerStem, HandlerErrorbar, HandlerLine2D, HandlerPatch, HandlerStepPatch, HandlerLineCollection, HandlerRegularPolyCollection, HandlerCircleCollection, HandlerTuple]]: ...

    def set_default_handler_map(cls: Type[Legend],
                                handler_map: Any) -> None: ...

    def update_default_handler_map(cls: Type[Legend],
                                   handler_map: Any) -> None: ...

    def get_legend_handler_map(self: Legend) -> dict[Type[Union[
        StemContainer, ErrorbarContainer, Line2D, Patch, StepPatch, LineCollection, RegularPolyCollection, CircleCollection, BarContainer, Tuple]],
                                                     Union[
                                                         HandlerStem, HandlerErrorbar, HandlerLine2D, HandlerPatch, HandlerStepPatch, HandlerLineCollection, HandlerRegularPolyCollection, HandlerCircleCollection, HandlerTuple]]: ...

    def get_legend_handler(legend_handler_map: dict[Type[Union[
        StemContainer, ErrorbarContainer, Line2D, Patch, StepPatch, LineCollection, RegularPolyCollection, CircleCollection, BarContainer, tuple]],
                                                    Union[
                                                        HandlerStem, HandlerErrorbar, HandlerLine2D, HandlerPatch, HandlerStepPatch, HandlerLineCollection, HandlerRegularPolyCollection, HandlerCircleCollection, HandlerTuple]],
                           orig_handle: Any) -> Union[
        HandlerStem, HandlerErrorbar, HandlerLine2D, HandlerPatch, HandlerStepPatch, HandlerLineCollection, HandlerRegularPolyCollection, HandlerCircleCollection, HandlerTuple, None]: ...

    def _init_legend_box(self: Legend,
                         handles: list,
                         labels: Any,
                         markerfirst: bool = True) -> None: ...

    def _auto_legend_data(self: Legend) -> Any: ...

    def get_children(self: Legend) -> list[FancyBboxPatch]: ...

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

    def get_bbox_to_anchor(self: Legend) -> TransformedBbox: ...

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
                 event: {canvas}) -> Tuple[Any, Any]: ...

    def set_draggable(self: Legend,
                      state: bool,
                      use_blit: Optional[bool] = False,
                      update: Optional[str] = 'loc') -> Any: ...

    def get_draggable(self: Legend) -> Any: ...


def _get_legend_handles(axs: {__iter__},
                        legend_handler_map: dict = None) -> Generator[Any, Any, None]: ...


def _get_legend_handles_labels(axs: Any,
                               legend_handler_map: dict = None) -> Tuple[list, list]: ...


def _parse_legend_args(*args,
                       axs: Any,
                       handles: Any = None,
                       labels: Any = None,
                       **kwargs) -> Any: ...