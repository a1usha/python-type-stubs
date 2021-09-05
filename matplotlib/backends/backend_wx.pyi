from matplotlib.widgets import SubplotTool as SubplotTool
from matplotlib.transforms import Affine2D as Affine2D
from matplotlib.path import Path as Path
from matplotlib.figure import Figure as Figure
from matplotlib.backend_managers import ToolManager as ToolManager
from matplotlib._pylab_helpers import Gcf as Gcf
from matplotlib import backend_tools as backend_tools
from matplotlib import cbook as cbook
from matplotlib import _api as _api
from matplotlib.backend_bases import cursors as cursors
from matplotlib.backend_bases import ToolContainerBase as ToolContainerBase
from matplotlib.backend_bases import TimerBase as TimerBase
from matplotlib.backend_bases import StatusbarBase as StatusbarBase
from matplotlib.backend_bases import RendererBase as RendererBase
from matplotlib.backend_bases import NavigationToolbar2 as NavigationToolbar2
from matplotlib.backend_bases import MouseButton as MouseButton
from matplotlib.backend_bases import GraphicsContextBase as GraphicsContextBase
from matplotlib.backend_bases import FigureManagerBase as FigureManagerBase
from matplotlib.backend_bases import FigureCanvasBase as FigureCanvasBase
from matplotlib.backend_bases import _check_savefig_extra_args as _check_savefig_extra_args
from matplotlib.backend_bases import _Backend as _Backend
from typing import Any
from typing import ClassVar
from typing import Iterable
from typing import Optional
from typing import Tuple
from typing import Type
from typing import Union

from matplotlib import _api
from matplotlib.backend_bases import FigureCanvasBase
from matplotlib.backend_bases import FigureManagerBase
from matplotlib.backend_bases import GraphicsContextBase
from matplotlib.backend_bases import NavigationToolbar2
from matplotlib.backend_bases import RendererBase
from matplotlib.backend_bases import StatusbarBase
from matplotlib.backend_bases import TimerBase
from matplotlib.backend_bases import ToolContainerBase
from matplotlib.backend_bases import _Backend
from matplotlib.backend_managers import ToolManager
from matplotlib.backend_tools import ConfigureSubplotsBase
from matplotlib.backend_tools import RubberbandBase
from matplotlib.backend_tools import SaveFigureBase
from matplotlib.backend_tools import SetCursorBase
from matplotlib.backend_tools import ToolCopyToClipboardBase
from matplotlib.backend_tools import ToolHelpBase
from matplotlib.backends.backend_wx import ConfigureSubplotsWx
from matplotlib.backends.backend_wx import FigureCanvasWx
from matplotlib.backends.backend_wx import FigureFrameWx
from matplotlib.backends.backend_wx import FigureManagerWx
from matplotlib.backends.backend_wx import GraphicsContextWx
from matplotlib.backends.backend_wx import HelpWx
from matplotlib.backends.backend_wx import NavigationToolbar2Wx
from matplotlib.backends.backend_wx import RendererWx
from matplotlib.backends.backend_wx import RubberbandWx
from matplotlib.backends.backend_wx import SaveFigureWx
from matplotlib.backends.backend_wx import SetCursorWx
from matplotlib.backends.backend_wx import StatusBarWx
from matplotlib.backends.backend_wx import StatusbarWx
from matplotlib.backends.backend_wx import TimerWx
from matplotlib.backends.backend_wx import ToolCopyToClipboardWx
from matplotlib.backends.backend_wx import ToolbarWx
from matplotlib.backends.backend_wx import _BackendWx
from matplotlib.backends.backend_wx import _FigureCanvasWxBase
from matplotlib.backends.backend_wx import _HelpDialog
from matplotlib.font_manager import FontProperties
from matplotlib.text import Text

_DEBUG_lvls: dict[int, str]
_DEBUG: int

PIXELS_PER_INCH: int

IDLE_DELAY: int


@_api.deprecated("3.3")
def DEBUG_MSG(string: Any,
              lvl: int = 3,
              o: Any = None) -> Optional[Any]: ...


def error_msg_wx(msg: Union[str, Any],
                 parent: Any = None) -> None: ...


class TimerWx(TimerBase):
    _timer: Any

    def __init__(self: TimerWx,
                 *args,
                 **kwargs) -> None: ...

    def _timer_start(self: TimerWx) -> None: ...

    def _timer_stop(self: TimerWx) -> None: ...

    def _timer_set_interval(self: TimerWx) -> None: ...


class RendererWx(RendererBase):
    fontweights: ClassVar[dict[Union[Union[int, str], Any], Any]]
    fontangles: ClassVar[dict[str, Any]]
    fontnames: ClassVar[dict[str, Any]]
    fontd: dict[Any, Any]
    bitmap: {GetWidth, GetHeight}
    width: Any
    dpi: Any
    gc: None
    height: Any

    def __init__(self: RendererWx,
                 bitmap: {GetWidth, GetHeight},
                 dpi: Any) -> None: ...

    def flipy(self: RendererWx) -> bool: ...

    def offset_text_height(self: RendererWx) -> bool: ...

    def get_text_width_height_descent(self: RendererWx,
                                      s: Union[Union[{__len__, __getitem__}, str], Any],
                                      prop: {get_size_in_points},
                                      ismath: {__eq__}) -> Tuple[Any, Any, Any]: ...

    def get_canvas_width_height(self: RendererWx) -> Tuple[Any, Any]: ...

    def handle_clip_rectangle(self: RendererWx,
                              gc: Union[Union[{select, gfx_ctx, unselect}, {select, gfx_ctx, get_wxcolour, get_rgb,
                                                                            unselect}], Any]) -> None: ...

    def convert_path(gfx_ctx: {CreatePath},
                     path: {iter_segments},
                     transform: Any) -> Any: ...

    def draw_path(self: RendererWx,
                  gc: {select, gfx_ctx, unselect},
                  path: {iter_segments},
                  transform: Any,
                  rgbFace: Any = None) -> None: ...

    def draw_image(self: RendererWx,
                   gc: {get_clip_rectangle, select, gfx_ctx, unselect},
                   x: Union[int, float, complex],
                   y: Union[int, float, complex],
                   im: int) -> None: ...

    def draw_text(self: RendererWx,
                  gc: {select, gfx_ctx, get_wxcolour, get_rgb, unselect},
                  x: float,
                  y: float,
                  s: str,
                  prop: FontProperties,
                  angle: float,
                  ismath: bool = False,
                  mtext: Text = None) -> None: ...

    def new_gc(self: RendererWx) -> GraphicsContextWx: ...

    @_api.deprecated("3.3", alternative=".gc")
    def get_gc(self: RendererWx) -> Any: ...

    def get_wx_font(self: RendererWx,
                    s: Union[Union[{__len__, __getitem__}, str], Any],
                    prop: Union[FontProperties, Any]) -> Optional[Any]: ...

    def points_to_pixels(self: RendererWx,
                         points: Union[Union[float, Iterable, int], Any]) -> Union[Union[float, int], Any]: ...


class GraphicsContextWx(GraphicsContextBase):
    _capd: ClassVar[dict[str, Any]]
    _joind: ClassVar[dict[str, Any]]
    _cache: ClassVar[WeakKeyDictionary]
    renderer: Any
    gfx_ctx: Any
    _pen: Any
    bitmap: Any
    IsSelected: bool
    dc: Any

    def __init__(self: GraphicsContextWx,
                 bitmap: Any,
                 renderer: Any) -> None: ...

    def select(self: GraphicsContextWx) -> None: ...

    def unselect(self: GraphicsContextWx) -> None: ...

    def set_foreground(self: GraphicsContextWx,
                       fg: Any,
                       isRGBA: bool = None) -> None: ...

    def set_linewidth(self: GraphicsContextWx,
                      w: Any) -> None: ...

    def set_capstyle(self: GraphicsContextWx,
                     cs: Any) -> None: ...

    def set_joinstyle(self: GraphicsContextWx,
                      js: Any) -> None: ...

    def get_wxcolour(self: GraphicsContextWx,
                     color: Union[tuple[float, float, float, float], Any]) -> Any: ...


class _FigureCanvasWxBase(FigureCanvasBase):
    required_interactive_framework: ClassVar[str]
    _timer_cls: ClassVar[Type[TimerWx]]
    keyvald: ClassVar[dict[Any, Union[str, Any]]]
    filetypes: ClassVar[dict[str, str]]
    _skipwheelevent: bool
    bitmap: Any
    _rubberband_rect: None
    _width: Any
    _event_loop: Any
    _height: Any
    _isDrawn: bool

    def __init__(self: _FigureCanvasWxBase,
                 parent: Any,
                 id: Any,
                 figure: Optional[{set_canvas}] = None) -> None: ...

    def Copy_to_Clipboard(self: _FigureCanvasWxBase,
                          event: Any = None) -> None: ...

    def draw_idle(self: _FigureCanvasWxBase) -> None: ...

    def flush_events(self: _FigureCanvasWxBase) -> None: ...

    def start_event_loop(self: _FigureCanvasWxBase,
                         timeout: int = 0) -> Any: ...

    def stop_event_loop(self: _FigureCanvasWxBase,
                        event: Any = None) -> None: ...

    def _get_imagesave_wildcards(self: _FigureCanvasWxBase) -> Tuple[str, list[Any], int]: ...

    @_api.delete_parameter("3.4", "origin")
    def gui_repaint(self: _FigureCanvasWxBase,
                    drawDC: {DrawBitmap} = None,
                    origin: str = 'WX') -> Optional[Any]: ...

    def print_figure(self: _FigureCanvasWxBase,
                     filename: Any,
                     *args,
                     **kwargs) -> None: ...

    def _onPaint(self: _FigureCanvasWxBase,
                 event: Any) -> None: ...

    def _onSize(self: _FigureCanvasWxBase,
                event: Any) -> None: ...

    def _get_key(self: _FigureCanvasWxBase,
                 event: {KeyCode, ControlDown, AltDown, ShiftDown}) -> Union[Optional[str], Any]: ...

    def _onKeyDown(self: _FigureCanvasWxBase,
                   event: {KeyCode, ControlDown, AltDown, ShiftDown}) -> None: ...

    def _onKeyUp(self: _FigureCanvasWxBase,
                 event: {KeyCode, ControlDown, AltDown, ShiftDown}) -> None: ...

    def _set_capture(self: _FigureCanvasWxBase,
                     capture: bool = True) -> None: ...

    def _onCaptureLost(self: _FigureCanvasWxBase,
                       event: Any) -> None: ...

    def _onMouseButton(self: _FigureCanvasWxBase,
                       event: {Skip, ButtonDown, ButtonDClick, X, Y, GetButton, ButtonUp}) -> None: ...

    def _onMouseWheel(self: _FigureCanvasWxBase,
                      event: {GetX, GetY, LinesPerAction, WheelRotation, WheelDelta, Skip}) -> None: ...

    def _onMotion(self: _FigureCanvasWxBase,
                  event: {GetX, GetY, Skip}) -> None: ...

    def _onLeave(self: _FigureCanvasWxBase,
                 event: {Skip}) -> None: ...

    def _onEnter(self: _FigureCanvasWxBase,
                 event: {GetX, GetY, Skip}) -> None: ...


class FigureCanvasWx(_FigureCanvasWxBase):
    print_jpg: ClassVar[Callable[[FigureCanvasWx, Any, tuple[Any, ...], dict[str, Any]], Any]]
    print_tif: ClassVar[Callable[[FigureCanvasWx, Any, tuple[Any, ...], dict[str, Any]], Any]]
    renderer: RendererWx
    bitmap: Any
    _isDrawn: bool

    def draw(self: FigureCanvasWx,
             drawDC: Any = None) -> None: ...

    def print_bmp(self: FigureCanvasWx,
                  filename: Any,
                  *args,
                  **kwargs) -> Any: ...

    def print_jpeg(self: FigureCanvasWx,
                   filename: Any,
                   *args,
                   **kwargs) -> Any: ...

    def print_pcx(self: FigureCanvasWx,
                  filename: Any,
                  *args,
                  **kwargs) -> Any: ...

    def print_png(self: FigureCanvasWx,
                  filename: Any,
                  *args,
                  **kwargs) -> Any: ...

    def print_tiff(self: FigureCanvasWx,
                   filename: Any,
                   *args,
                   **kwargs) -> Any: ...

    def print_xpm(self: FigureCanvasWx,
                  filename: Any,
                  *args,
                  **kwargs) -> Any: ...

    def _print_image(self: FigureCanvasWx,
                     filename: Any,
                     filetype: {__eq__},
                     *,
                     quality: Any = None) -> Any: ...


class FigureFrameWx():
    toolbar: Union[ToolbarWx, NavigationToolbar2Wx, None]
    canvas: FigureCanvasWx
    figmgr: FigureManagerWx
    num: Any
    sizer: Any

    def __init__(self: FigureFrameWx,
                 num: Any,
                 fig: {bbox}) -> None: ...

    def toolmanager(self: FigureFrameWx) -> Optional[ToolManager]: ...

    def _get_toolbar(self: FigureFrameWx) -> Union[ToolbarWx, NavigationToolbar2Wx, None]: ...

    def get_canvas(self: FigureFrameWx,
                   fig: Union[{bbox}, Any]) -> FigureCanvasWx: ...

    def get_figure_manager(self: FigureFrameWx) -> FigureManagerWx: ...

    def _onClose(self: FigureFrameWx,
                 event: {Skip}) -> None: ...

    def GetToolBar(self: FigureFrameWx) -> Union[ToolbarWx, NavigationToolbar2Wx, None]: ...

    def Destroy(self: FigureFrameWx,
                *args,
                **kwargs) -> bool: ...


class FigureManagerWx(FigureManagerBase):
    _initializing: bool
    window: Any
    frame: Any

    def __init__(self: FigureManagerWx,
                 canvas: {manager, figure},
                 num: Any,
                 frame: Any) -> None: ...

    def toolbar(self: FigureManagerWx) -> Any: ...

    def toolbar(self: FigureManagerWx,
                value: Any) -> Any: ...

    def show(self: FigureManagerWx) -> None: ...

    def destroy(self: FigureManagerWx,
                *args) -> None: ...

    def full_screen_toggle(self: FigureManagerWx) -> None: ...

    def get_window_title(self: FigureManagerWx) -> Any: ...

    def set_window_title(self: FigureManagerWx,
                         title: Any) -> None: ...

    def resize(self: FigureManagerWx,
               width: Any,
               height: Any) -> None: ...


def _load_bitmap(filename: Union[str, Any]) -> Any: ...


cursord: dict[Cursors, Any]


def _set_frame_icon(frame: Union[FigureFrameWx, Any]) -> None: ...


class NavigationToolbar2Wx(NavigationToolbar2):
    prevZoomRect: ClassVar[deprecate_privatize_attribute]
    retinaFix: ClassVar[deprecate_privatize_attribute]
    savedRetinaImage: ClassVar[deprecate_privatize_attribute]
    wxoverlay: ClassVar[deprecate_privatize_attribute]
    zoomAxes: ClassVar[deprecate_privatize_attribute]
    zoomStartX: ClassVar[deprecate_privatize_attribute]
    zoomStartY: ClassVar[deprecate_privatize_attribute]
    _savedRetinaImage: Any
    _wxoverlay: Any
    wx_ids: dict[Any, Any]
    _coordinates: bool
    _zoomAxes: Any
    _retinaFix: bool
    _label_text: Any
    _prevZoomRect: None
    _zoomStartX: Any
    _zoomStartY: Any

    def __init__(self: NavigationToolbar2Wx,
                 canvas: {toolbar},
                 coordinates: bool = True) -> None: ...

    def _icon(name: Union[str, Any]) -> Any: ...

    @_api.deprecated("3.4")
    def get_canvas(self: NavigationToolbar2Wx,
                   frame: Any,
                   fig: Any) -> Any: ...

    def zoom(self: NavigationToolbar2Wx,
             *args) -> None: ...

    def pan(self: NavigationToolbar2Wx,
            *args) -> None: ...

    def save_figure(self: NavigationToolbar2Wx,
                    *args) -> None: ...

    def set_cursor(self: NavigationToolbar2Wx,
                   cursor: Any) -> None: ...

    def press_zoom(self: NavigationToolbar2Wx,
                   event: {button, x, y}) -> None: ...

    def release_zoom(self: NavigationToolbar2Wx,
                     event: {x, key, y}) -> None: ...

    def draw_rubberband(self: NavigationToolbar2Wx,
                        event: Optional[Any],
                        x0: Any,
                        y0: Any,
                        x1: Any,
                        y1: Any) -> None: ...

    def remove_rubberband(self: NavigationToolbar2Wx) -> None: ...

    def set_message(self: NavigationToolbar2Wx,
                    s: Any) -> None: ...

    def set_history_buttons(self: NavigationToolbar2Wx) -> None: ...


@_api.deprecated("3.3")
class StatusBarWx():
    def __init__(self: StatusBarWx,
                 parent: Any,
                 *args,
                 **kwargs) -> None: ...

    def set_function(self: StatusBarWx,
                     string: Any) -> None: ...


class ToolbarWx(ToolContainerBase):
    _space: Any
    _label_text: Any
    _toolitems: dict[Any, Any]
    _groups: dict[Any, Any]

    def __init__(self: ToolbarWx,
                 toolmanager: {toolmanager_connect},
                 parent: Any,
                 style: Any = wx.TB_HORIZONTAL) -> None: ...

    def _get_tool_pos(self: ToolbarWx,
                      tool: Any) -> Any: ...

    def add_toolitem(self: ToolbarWx,
                     name: str,
                     group: str,
                     position: int,
                     image_file: Any,
                     description: str,
                     toggle: bool) -> None: ...

    def toggle_toolitem(self: ToolbarWx,
                        name: str,
                        toggled: bool) -> None: ...

    def remove_toolitem(self: ToolbarWx,
                        name: str) -> None: ...

    def set_message(self: ToolbarWx,
                    s: str) -> None: ...


@_api.deprecated("3.3")
class StatusbarWx(StatusbarBase):
    def __init__(self: StatusbarWx,
                 parent: Any,
                 *args,
                 **kwargs) -> None: ...

    def set_message(self: StatusbarWx,
                    s: str) -> None: ...


class ConfigureSubplotsWx(ConfigureSubplotsBase):
    def trigger(self: ConfigureSubplotsWx,
                *args) -> None: ...


class SaveFigureWx(SaveFigureBase):
    def trigger(self: SaveFigureWx,
                *args) -> None: ...


class SetCursorWx(SetCursorBase):
    def set_cursor(self: SetCursorWx,
                   cursor: Any) -> None: ...


class RubberbandWx(RubberbandBase):
    def draw_rubberband(self: RubberbandWx,
                        x0: Any,
                        y0: Any,
                        x1: Any,
                        y1: Any) -> None: ...

    def remove_rubberband(self: RubberbandWx) -> None: ...


class _HelpDialog():
    _instance: ClassVar[None]
    headers: ClassVar[list[tuple[str, str, str]]]
    widths: ClassVar[list[int]]
    _instance: _HelpDialog

    def __init__(self: _HelpDialog,
                 parent: Any,
                 help_entries: Any) -> None: ...

    def OnClose(self: _HelpDialog,
                event: {Skip}) -> None: ...

    def show(cls: Type[_HelpDialog],
             parent: Any,
             help_entries: Any) -> None: ...


class HelpWx(ToolHelpBase):
    def trigger(self: HelpWx,
                *args) -> None: ...


class ToolCopyToClipboardWx(ToolCopyToClipboardBase):
    def trigger(self: ToolCopyToClipboardWx,
                *args,
                **kwargs) -> None: ...


ToolSaveFigure: Type[SaveFigureWx]
ToolConfigureSubplots: Type[ConfigureSubplotsWx]
ToolSetCursor: Type[SetCursorWx]
ToolRubberband: Type[RubberbandWx]
ToolHelp: Type[HelpWx]
ToolCopyToClipboard: Type[ToolCopyToClipboardWx]


class _BackendWx(_Backend):
    FigureCanvas: ClassVar[Type[FigureCanvasWx]]
    FigureManager: ClassVar[Type[FigureManagerWx]]
    _frame_class: ClassVar[Type[FigureFrameWx]]

    def new_figure_manager(cls: Type[_BackendWx],
                           num: Any,
                           *args,
                           **kwargs) -> FigureManagerBase: ...

    def new_figure_manager_given_figure(cls: Type[_BackendWx],
                                        num: Any,
                                        figure: {bbox}) -> FigureManagerWx: ...

    def mainloop() -> None: ...
