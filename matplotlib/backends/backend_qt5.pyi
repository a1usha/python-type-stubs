from qt_compat import _setDevicePixelRatio as _setDevicePixelRatio
from qt_compat import _isdeleted as _isdeleted
from qt_compat import _devicePixelRatioF as _devicePixelRatioF
from qt_compat import QT_API as QT_API
from qt_compat import __version__ as __version__
from qt_compat import QtWidgets as QtWidgets
from qt_compat import QtGui as QtGui
from qt_compat import QtCore as QtCore
from matplotlib import qt_compat as qt_compat
from matplotlib.backends.qt_editor._formsubplottool import UiSubplotTool as UiSubplotTool
from matplotlib.backend_bases import MouseButton as MouseButton
from matplotlib.backend_bases import StatusbarBase as StatusbarBase
from matplotlib.backend_bases import ToolContainerBase as ToolContainerBase
from matplotlib.backend_bases import cursors as cursors
from matplotlib.backend_bases import TimerBase as TimerBase
from matplotlib.backend_bases import NavigationToolbar2 as NavigationToolbar2
from matplotlib.backend_bases import FigureManagerBase as FigureManagerBase
from matplotlib.backend_bases import FigureCanvasBase as FigureCanvasBase
from matplotlib.backend_bases import _Backend as _Backend
from matplotlib._pylab_helpers import Gcf as Gcf
from matplotlib import cbook as cbook
from matplotlib import backend_tools as backend_tools
from matplotlib import _api as _api
from typing import Any
from typing import Callable
from typing import ClassVar
from typing import Optional
from typing import Tuple
from typing import Union

from matplotlib import _api
from matplotlib.backend_bases import FigureCanvasBase
from matplotlib.backend_bases import FigureManagerBase
from matplotlib.backend_bases import NavigationToolbar2
from matplotlib.backend_bases import StatusbarBase
from matplotlib.backend_bases import TimerBase
from matplotlib.backend_bases import ToolContainerBase
from matplotlib.backend_bases import _Backend
from matplotlib.backend_tools import ConfigureSubplotsBase
from matplotlib.backend_tools import RubberbandBase
from matplotlib.backend_tools import SaveFigureBase
from matplotlib.backend_tools import SetCursorBase
from matplotlib.backend_tools import ToolCopyToClipboardBase
from matplotlib.backend_tools import ToolHelpBase
from matplotlib.backends.backend_qt5 import ConfigureSubplotsQt
from matplotlib.backends.backend_qt5 import FigureCanvasQT
from matplotlib.backends.backend_qt5 import FigureManagerQT
from matplotlib.backends.backend_qt5 import HelpQt
from matplotlib.backends.backend_qt5 import MainWindow
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT
from matplotlib.backends.backend_qt5 import RubberbandQt
from matplotlib.backends.backend_qt5 import SaveFigureQt
from matplotlib.backends.backend_qt5 import SetCursorQt
from matplotlib.backends.backend_qt5 import StatusbarQt
from matplotlib.backends.backend_qt5 import SubplotToolQt
from matplotlib.backends.backend_qt5 import TimerQT
from matplotlib.backends.backend_qt5 import ToolCopyToClipboardQT
from matplotlib.backends.backend_qt5 import ToolbarQt
from matplotlib.backends.qt_editor._formsubplottool import UiSubplotTool

SPECIAL_KEYS: dict[Any, Union[str, Any]]
_MODIFIER_KEYS: list[tuple[Any, Any]]
cursord: dict[Cursors, Any]
SUPER: int
ALT: int
CTRL: int
SHIFT: int
MODIFIER_KEYS: list[tuple[Union[str, Any], Any, Any]]
qApp: None
backend_version: Any


def _create_qApp() -> Any: ...


def _allow_super_init(__init__: {__eq__}) -> Union[
    {__eq__}, Callable[[Any, Tuple[Any, ...], dict[str, Any]], None]]: ...


class TimerQT(TimerBase):
    _timer: Any

    def __init__(self: TimerQT,
                 *args,
                 **kwargs) -> None: ...

    def __del__(self: TimerQT) -> None: ...

    def _timer_set_single_shot(self: TimerQT) -> None: ...

    def _timer_set_interval(self: TimerQT) -> None: ...

    def _timer_start(self: TimerQT) -> None: ...

    def _timer_stop(self: TimerQT) -> None: ...


class FigureCanvasQT(FigureCanvasBase):
    required_interactive_framework: ClassVar[str]
    _timer_cls: ClassVar[Type[TimerQT]]
    buttond: ClassVar[dict[Any, MouseButton]]
    _draw_rect_callback: Callable[[Any], None]
    _draw_pending: bool
    _dpi_ratio_prev: Union[int, Any]
    _is_drawing: bool
    _event_loop: Any

    def __init__(self: FigureCanvasQT,
                 figure: Optional[{set_canvas}] = None) -> Optional[Any]: ...

    def _update_figure_dpi(self: FigureCanvasQT) -> None: ...

    def _dpi_ratio(self: FigureCanvasQT) -> Union[int, Any]: ...

    def _update_pixel_ratio(self: FigureCanvasQT) -> None: ...

    def _update_screen(self: FigureCanvasQT,
                       screen: Any) -> None: ...

    def showEvent(self: FigureCanvasQT,
                  event: Any) -> None: ...

    def get_width_height(self: FigureCanvasQT) -> Tuple[int, int]: ...

    def enterEvent(self: FigureCanvasQT,
                   event: {pos}) -> None: ...

    def leaveEvent(self: FigureCanvasQT,
                   event: Any) -> None: ...

    def mouseEventCoords(self: FigureCanvasQT,
                         pos: Union[Union[{button}, {pixelDelta}], Any]) -> Tuple[
        Union[int, Any], Union[Union[float, int], Any]]: ...

    def mousePressEvent(self: FigureCanvasQT,
                        event: {pos, button}) -> None: ...

    def mouseDoubleClickEvent(self: FigureCanvasQT,
                              event: {pos, button}) -> None: ...

    def mouseMoveEvent(self: FigureCanvasQT,
                       event: Any) -> None: ...

    def mouseReleaseEvent(self: FigureCanvasQT,
                          event: {button}) -> None: ...

    def wheelEvent(self: FigureCanvasQT,
                   event: {pixelDelta}) -> None: ...

    def wheelEvent(self: FigureCanvasQT,
                   event: {x, y, delta, orientation}) -> None: ...

    def keyPressEvent(self: FigureCanvasQT,
                      event: {key, modifiers}) -> None: ...

    def keyReleaseEvent(self: FigureCanvasQT,
                        event: {key, modifiers}) -> None: ...

    def resizeEvent(self: FigureCanvasQT,
                    event: {size}) -> None: ...

    def sizeHint(self: FigureCanvasQT) -> Any: ...

    def minumumSizeHint(self: FigureCanvasQT) -> Any: ...

    def _get_key(self: FigureCanvasQT,
                 event: {key, modifiers}) -> Optional[str]: ...

    def flush_events(self: FigureCanvasQT) -> None: ...

    def start_event_loop(self: FigureCanvasQT,
                         timeout: int = 0) -> Any: ...

    def stop_event_loop(self: FigureCanvasQT,
                        event: Any = None) -> None: ...

    def draw(self: FigureCanvasQT) -> None: ...

    def draw_idle(self: FigureCanvasQT) -> None: ...

    def blit(self: FigureCanvasQT,
             bbox: Optional[{bounds}] = None) -> None: ...

    def _draw_idle(self: FigureCanvasQT) -> None: ...

    def drawRectangle(self: FigureCanvasQT,
                      rect: Any) -> None: ...


class MainWindow():
    closing: ClassVar[Any]

    def closeEvent(self: MainWindow,
                   event: Any) -> None: ...


class FigureManagerQT(FigureManagerBase):
    toolbar: Union[ToolbarQt, NavigationToolbar2QT, None]
    window: MainWindow

    def __init__(self: FigureManagerQT,
                 canvas: {manager, figure},
                 num: Any) -> None: ...

    def full_screen_toggle(self: FigureManagerQT) -> None: ...

    def _widgetclosed(self: FigureManagerQT) -> None: ...

    def _get_toolbar(self: FigureManagerQT,
                     canvas: Union[{manager, figure}, Any],
                     parent: Any) -> Union[ToolbarQt, NavigationToolbar2QT, None]: ...

    def resize(self: FigureManagerQT,
               width: {__add__},
               height: {__add__}) -> None: ...

    def show(self: FigureManagerQT) -> None: ...

    def destroy(self: FigureManagerQT,
                *args) -> None: ...

    def get_window_title(self: FigureManagerQT) -> Any: ...

    def set_window_title(self: FigureManagerQT,
                         title: Any) -> None: ...


class NavigationToolbar2QT(NavigationToolbar2):
    message: ClassVar[Any]
    toolitems: ClassVar[list[tuple[str, str, str, str]]]
    _actions: dict[str, Any]
    coordinates: bool
    locLabel: Any

    def __init__(self: NavigationToolbar2QT,
                 canvas: {toolbar},
                 parent: Any,
                 coordinates: bool = True) -> None: ...

    @_api.deprecated("3.3", alternative="self.canvas.parent()")
    def parent(self: NavigationToolbar2QT) -> Any: ...

    @_api.deprecated("3.3", alternative="self.canvas.setParent()")
    def parent(self: NavigationToolbar2QT,
               value: Any) -> None: ...

    @_api.deprecated(
        "3.3", alternative="os.path.join(mpl.get_data_path(), 'images')")
    def basedir(self: NavigationToolbar2QT) -> str: ...

    def _icon(self: NavigationToolbar2QT,
              name: Union[str, Any]) -> Any: ...

    def edit_parameters(self: NavigationToolbar2QT) -> None: ...

    def _update_buttons_checked(self: NavigationToolbar2QT) -> None: ...

    def pan(self: NavigationToolbar2QT,
            *args) -> None: ...

    def zoom(self: NavigationToolbar2QT,
             *args) -> None: ...

    def set_message(self: NavigationToolbar2QT,
                    s: Any) -> None: ...

    def set_cursor(self: NavigationToolbar2QT,
                   cursor: Any) -> None: ...

    def draw_rubberband(self: NavigationToolbar2QT,
                        event: Optional[Any],
                        x0: Any,
                        y0: Any,
                        x1: {__sub__},
                        y1: Any) -> None: ...

    def remove_rubberband(self: NavigationToolbar2QT) -> None: ...

    def configure_subplots(self: NavigationToolbar2QT) -> None: ...

    def save_figure(self: NavigationToolbar2QT,
                    *args) -> None: ...

    def set_history_buttons(self: NavigationToolbar2QT) -> None: ...


class SubplotToolQt(UiSubplotTool):
    _figure: Any
    _attrs: list[str]
    _defaults: dict

    def __init__(self: SubplotToolQt,
                 targetfig: Any,
                 parent: Any) -> None: ...

    def _export_values(self: SubplotToolQt) -> None: ...

    def _on_value_changed(self: SubplotToolQt) -> None: ...

    def _tight_layout(self: SubplotToolQt) -> None: ...

    def _reset(self: SubplotToolQt) -> None: ...


class ToolbarQt(ToolContainerBase):
    _message_action: Any
    _toolitems: dict[Any, Any]
    _groups: dict[Any, Any]

    def __init__(self: ToolbarQt,
                 toolmanager: {toolmanager_connect},
                 parent: Any) -> None: ...

    def add_toolitem(self: ToolbarQt,
                     name: str,
                     group: str,
                     position: int,
                     image_file: Any,
                     description: str,
                     toggle: bool) -> None: ...

    def _add_to_group(self: ToolbarQt,
                      group: Union[str, Any],
                      name: Any,
                      button: Any,
                      position: Any) -> None: ...

    def toggle_toolitem(self: ToolbarQt,
                        name: str,
                        toggled: bool) -> None: ...

    def remove_toolitem(self: ToolbarQt,
                        name: str) -> None: ...

    def set_message(self: ToolbarQt,
                    s: str) -> None: ...


@_api.deprecated("3.3")
class StatusbarQt(StatusbarBase):
    def __init__(self: StatusbarQt,
                 window: {statusBar},
                 *args,
                 **kwargs) -> None: ...

    def set_message(self: StatusbarQt,
                    s: str) -> None: ...


class ConfigureSubplotsQt(ConfigureSubplotsBase):
    def trigger(self: ConfigureSubplotsQt,
                *args) -> None: ...


class SaveFigureQt(SaveFigureBase):
    def trigger(self: SaveFigureQt,
                *args) -> None: ...


class SetCursorQt(SetCursorBase):
    def set_cursor(self: SetCursorQt,
                   cursor: Any) -> None: ...


class RubberbandQt(RubberbandBase):
    def draw_rubberband(self: RubberbandQt,
                        x0: Any,
                        y0: Any,
                        x1: {__sub__},
                        y1: Any) -> None: ...

    def remove_rubberband(self: RubberbandQt) -> None: ...


class HelpQt(ToolHelpBase):
    def trigger(self: HelpQt,
                *args) -> None: ...


class ToolCopyToClipboardQT(ToolCopyToClipboardBase):
    def trigger(self: ToolCopyToClipboardQT,
                *args,
                **kwargs) -> None: ...


ToolSaveFigure: Type[SaveFigureQt]
ToolConfigureSubplots: Type[ConfigureSubplotsQt]
ToolSetCursor: Type[SetCursorQt]
ToolRubberband: Type[RubberbandQt]
ToolHelp: Type[HelpQt]
ToolCopyToClipboard: Type[ToolCopyToClipboardQT]


class _BackendQT5(_Backend):
    FigureCanvas: ClassVar[Type[FigureCanvasQT]]
    FigureManager: ClassVar[Type[FigureManagerQT]]

    def mainloop() -> None: ...
