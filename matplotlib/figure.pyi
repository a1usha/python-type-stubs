from typing import Any
from typing import Optional
from typing import Tuple
from typing import Union

from matplotlib import _api
from matplotlib.artist import Artist
from matplotlib.axes._subplots import SubplotBase
from matplotlib.backend_bases import MouseEvent
from matplotlib.cbook import Stack
from matplotlib.colorbar import Colorbar
from matplotlib.colors import Colormap
from matplotlib.colors import Normalize
from matplotlib.figure import Figure
from matplotlib.figure import FigureBase
from matplotlib.figure import SubFigure
from matplotlib.figure import SubplotParams
from matplotlib.figure import _AxesStack
from matplotlib.image import FigureImage
from matplotlib.patches import Rectangle
from numpy.core._multiarray_umath import ndarray
from object import object


def _stale_figure_callback(self: {figure},
                           val: Any) -> None: ...


class _AxesStack(Stack):
    def __init__(self: _AxesStack) -> None: ...

    def as_list(self: _AxesStack) -> list[Any]: ...

    def _entry_from_axes(self: _AxesStack,
                         e: Union[{_shared_y_axes, _shared_x_axes}, Any]) -> Optional[Tuple[Any, Any]]: ...

    def remove(self: _AxesStack,
               a: Union[{_shared_y_axes, _shared_x_axes}, Any]) -> None: ...

    def bubble(self: _AxesStack,
               a: Any) -> Any: ...

    def add(self: _AxesStack,
            a: Any) -> None: ...

    def __call__(self: _AxesStack) -> Optional[Any]: ...

    def __contains__(self: _AxesStack,
                     a: Any) -> bool: ...


class SubplotParams(object):
    def __init__(self: SubplotParams,
                 left: float = None,
                 bottom: float = None,
                 right: float = None,
                 top: float = None,
                 wspace: float = None,
                 hspace: float = None) -> None: ...

    def update(self: SubplotParams,
               left: Union[float, Any] = None,
               bottom: Any = None,
               right: Any = None,
               top: Any = None,
               wspace: Any = None,
               hspace: Any = None) -> Any: ...


class FigureBase(Artist):
    def __init__(self: FigureBase) -> None: ...

    def _get_draw_artists(self: FigureBase,
                          renderer: Union[Union[{open_group, get_rasterized, get_agg_filter, figure,
                                                 option_image_nocomposite, close_group}, {open_group, get_rasterized,
                                                                                          get_agg_filter, figure,
                                                                                          option_image_nocomposite,
                                                                                          close_group}], Any]) -> list[
        Any]: ...

    def autofmt_xdate(self: FigureBase,
                      bottom: float = 0.2,
                      rotation: float = 30,
                      ha: str = 'right',
                      which: str = 'major') -> None: ...

    def get_children(self: FigureBase) -> list[Any]: ...

    def contains(self: FigureBase,
                 mouseevent: MouseEvent) -> Any: ...

    def get_window_extent(self: FigureBase,
                          *args,
                          **kwargs) -> Any: ...

    def _suplabels(self: FigureBase,
                   t: str,
                   info: Union[Union[dict[str, Union[str, float, int]], dict[str, Union[str, float]]], Any],
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

    def suptitle(self: FigureBase,
                 t: Any,
                 **kwargs) -> Any: ...

    def supxlabel(self: FigureBase,
                  t: Any,
                  **kwargs) -> Any: ...

    def supylabel(self: FigureBase,
                  t: Any,
                  **kwargs) -> Any: ...

    def get_edgecolor(self: FigureBase) -> Any: ...

    def get_facecolor(self: FigureBase) -> Any: ...

    def get_frameon(self: FigureBase) -> Any: ...

    def set_linewidth(self: FigureBase,
                      linewidth: Union[int, float, complex]) -> None: ...

    def get_linewidth(self: FigureBase) -> Any: ...

    def set_edgecolor(self: FigureBase,
                      color: Any) -> None: ...

    def set_facecolor(self: FigureBase,
                      color: Any) -> None: ...

    def set_frameon(self: FigureBase,
                    b: bool) -> None: ...

    def add_artist(self: FigureBase,
                   artist: Any,
                   clip: bool = False) -> Any: ...

    def add_axes(self: FigureBase,
                 *args,
                 **kwargs) -> Optional[Any]: ...

    def add_subplot(self: FigureBase,
                    *args,
                    **kwargs) -> Any: ...

    def _add_axes_internal(self: FigureBase,
                           ax: Union[SubplotBase, Any],
                           key: Union[tuple[Any, dict[str, Any]], Any]) -> Union[SubplotBase, Any]: ...

    @_api.make_keyword_only("3.3", "sharex")
    def subplots(self: FigureBase,
                 nrows: int = 1,
                 ncols: int = 1,
                 sharex: str = False,
                 sharey: str = False,
                 squeeze: bool = True,
                 subplot_kw: Optional[dict] = None,
                 gridspec_kw: Optional[dict] = None) -> Any: ...

    def delaxes(self: FigureBase,
                ax: {_shared_y_axes, _shared_x_axes}) -> None: ...

    def legend(self: FigureBase,
               *args,
               **kwargs) -> Any: ...

    def text(self: FigureBase,
             x: float,
             y: float,
             s: str,
             fontdict: Optional[dict] = None,
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

    def colorbar(self: FigureBase,
                 mappable: {get_array, cmap, norm, colorbar, colorbar_cid, callbacksSM},
                 cax: Any = None,
                 ax: Any = None,
                 use_gridspec: bool = True,
                 **kwargs) -> Union[Colorbar, Any]: ...

    def subplots_adjust(self: FigureBase,
                        left: Optional[float] = None,
                        bottom: Optional[float] = None,
                        right: Optional[float] = None,
                        top: Optional[float] = None,
                        wspace: Optional[float] = None,
                        hspace: Optional[float] = None) -> None: ...

    def align_xlabels(self: FigureBase,
                      axs: Any = None) -> None: ...

    def align_ylabels(self: FigureBase,
                      axs: Any = None) -> None: ...

    def align_labels(self: FigureBase,
                     axs: Any = None) -> None: ...

    def add_gridspec(self: FigureBase,
                     nrows: int = 1,
                     ncols: int = 1,
                     figure: Any = ...,
                     left: Any = ...,
                     bottom: Any = ...,
                     right: Any = ...,
                     top: Any = ...,
                     wspace: Any = ...,
                     hspace: Any = ...,
                     width_ratios: Any = ...,
                     height_ratios: Any = ...,
                     **kwargs) -> Any: ...

    def subfigures(self: FigureBase,
                   nrows: int = 1,
                   ncols: int = 1,
                   squeeze: bool = True,
                   wspace: float = None,
                   hspace: float = None,
                   width_ratios: Any = None,
                   height_ratios: Any = None,
                   **kwargs) -> Union[Union[int, float, complex, None, ndarray], Any]: ...

    def add_subfigure(self: FigureBase,
                      subplotspec: Any,
                      parent: Any = ...,
                      facecolor: Any = ...,
                      edgecolor: Any = ...,
                      linewidth: Any = ...,
                      frameon: Any = ...,
                      **kwargs) -> Any: ...

    def sca(self: FigureBase,
            a: Union[SubplotBase, Any]) -> Union[SubplotBase, Any]: ...

    def gca(self: FigureBase,
            **kwargs) -> Any: ...

    def _gci(self: FigureBase) -> Optional[Any]: ...

    def _process_projection_requirements(self: FigureBase,
                                         axes_class: Any = None,
                                         polar: bool = False,
                                         projection: Any = None,
                                         *args,
                                         **kwargs) -> Tuple[Any, dict[str, Any]]: ...

    def get_default_bbox_extra_artists(self: FigureBase) -> list[Any]: ...

    def get_tightbbox(self: FigureBase,
                      renderer: Any,
                      bbox_extra_artists: Any = None) -> Any: ...

    def _normalize_grid_string(layout: Union[str, Any]) -> list[list[Any]]: ...

    def subplot_mosaic(self: FigureBase,
                       mosaic: Any,
                       *,
                       subplot_kw: Optional[dict] = None,
                       gridspec_kw: Optional[dict] = None,
                       empty_sentinel: Optional[object] = '.') -> dict[Any, Axes]: ...

    def _set_artist_props(self: FigureBase,
                          a: Union[Rectangle, Any]) -> None: ...


class SubFigure(FigureBase):
    def __init__(self: SubFigure,
                 parent: Any,
                 subplotspec: Any,
                 *,
                 facecolor: Any = None,
                 edgecolor: Any = None,
                 linewidth: float = 0.0,
                 frameon: bool = None) -> None: ...

    def _redo_transform_rel_fig(self: SubFigure,
                                bbox: Optional[Any] = None) -> None: ...

    def get_constrained_layout(self: SubFigure) -> Any: ...

    def get_constrained_layout_pads(self: SubFigure,
                                    relative: bool = False) -> Any: ...

    def init_layoutgrid(self: SubFigure) -> None: ...

    def get_axes(self: SubFigure) -> list[Any]: ...

    def draw(self: SubFigure,
             renderer: {open_group, get_rasterized, get_agg_filter, figure, option_image_nocomposite,
                        close_group}) -> None: ...


class Figure(FigureBase):
    def __str__(self: Figure) -> str: ...

    def __repr__(self: Figure) -> str: ...

    def __init__(self: Figure,
                 figsize: Any = None,
                 dpi: float = None,
                 facecolor: Any = None,
                 edgecolor: Any = None,
                 linewidth: float = 0.0,
                 frameon: bool = None,
                 subplotpars: SubplotParams = None,
                 tight_layout: Union[bool, dict] = None,
                 constrained_layout: bool = None) -> Any: ...

    def _repr_html_(self: Figure) -> Any: ...

    def show(self: Figure,
             warn: bool = True) -> Any: ...

    def get_axes(self: Figure) -> list[Any]: ...

    def _get_dpi(self: Figure) -> Union[Optional[float], Any]: ...

    def _set_dpi(self: Figure,
                 dpi: float,
                 forward: bool = True) -> None: ...

    def get_tight_layout(self: Figure) -> bool: ...

    def set_tight_layout(self: Figure,
                         tight: str) -> None: ...

    def get_constrained_layout(self: Figure) -> bool: ...

    def set_constrained_layout(self: Figure,
                               constrained: Union[bool, dict, None]) -> None: ...

    def set_constrained_layout_pads(self: Figure,
                                    **kwargs) -> None: ...

    def get_constrained_layout_pads(self: Figure,
                                    relative: bool = False) -> Tuple[Optional[Any], Optional[Any], None, None]: ...

    def set_canvas(self: Figure,
                   canvas: Any) -> None: ...

    def figimage(self: Figure,
                 X: Any,
                 xo: int = 0,
                 yo: int = 0,
                 alpha: Optional[float] = None,
                 norm: Normalize = None,
                 cmap: Union[str, Colormap] = None,
                 vmin: float = None,
                 vmax: float = None,
                 origin: str = None,
                 resize: bool = False,
                 **kwargs) -> FigureImage: ...

    def set_size_inches(self: Figure,
                        w: Union[tuple[float, float], float],
                        h: float = None,
                        forward: bool = True) -> Any: ...

    def get_size_inches(self: Figure) -> Any: ...

    def get_figwidth(self: Figure) -> Any: ...

    def get_figheight(self: Figure) -> Any: ...

    def get_dpi(self: Figure) -> Union[Optional[float], Any]: ...

    def set_dpi(self: Figure,
                val: float) -> None: ...

    def set_figwidth(self: Figure,
                     val: float,
                     forward: bool = True) -> None: ...

    def set_figheight(self: Figure,
                      val: float,
                      forward: bool = True) -> None: ...

    def clf(self: Figure,
            keep_observers: bool = False) -> None: ...

    def clear(self: Figure,
              keep_observers: bool = False) -> None: ...

    def draw(self: Figure,
             renderer: {open_group, get_rasterized, get_agg_filter, figure, option_image_nocomposite, close_group}) -> \
    Optional[Any]: ...

    def draw_artist(self: Figure,
                    a: {draw}) -> Any: ...

    def __getstate__(self: Figure) -> dict[str, Any]: ...

    def __setstate__(self: Figure,
                     state: {pop}) -> None: ...

    def add_axobserver(self: Figure,
                       func: Any) -> None: ...

    def savefig(self: Figure,
                fname: Any,
                *,
                transparent: Any = None,
                **kwargs) -> None: ...

    def ginput(self: Figure,
               n: int = 1,
               timeout: float = 30,
               show_clicks: bool = True,
               mouse_add: Any = MouseButton.LEFT,
               mouse_pop: Any = MouseButton.RIGHT,
               mouse_stop: Any = MouseButton.MIDDLE) -> list[Any]: ...

    def waitforbuttonpress(self: Figure,
                           timeout: int = -1) -> None: ...

    def init_layoutgrid(self: Figure) -> None: ...

    def execute_constrained_layout(self: Figure,
                                   renderer: Union[
                                       {open_group, get_rasterized, get_agg_filter, figure, option_image_nocomposite,
                                        close_group}, Any] = None) -> None: ...

    def tight_layout(self: Figure,
                     *,
                     pad: float = 1.08,
                     h_pad: float = None,
                     w_pad: float = None,
                     rect: int = None) -> None: ...


def figaspect(arg: Any) -> float: ...