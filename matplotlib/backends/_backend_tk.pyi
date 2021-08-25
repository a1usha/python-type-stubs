from matplotlib import _tkagg as _tkagg
from matplotlib.widgets import SubplotTool as SubplotTool
from matplotlib.figure import Figure as Figure
from matplotlib._pylab_helpers import Gcf as Gcf
from matplotlib.backend_bases import _Mode as _Mode
from matplotlib.backend_bases import cursors as cursors
from matplotlib.backend_bases import ToolContainerBase as ToolContainerBase
from matplotlib.backend_bases import TimerBase as TimerBase
from matplotlib.backend_bases import StatusbarBase as StatusbarBase
from matplotlib.backend_bases import NavigationToolbar2 as NavigationToolbar2
from matplotlib.backend_bases import FigureManagerBase as FigureManagerBase
from matplotlib.backend_bases import FigureCanvasBase as FigureCanvasBase
from matplotlib.backend_bases import _Backend as _Backend
from matplotlib import _c_internal_utils as _c_internal_utils
from matplotlib import cbook as cbook
from matplotlib import backend_tools as backend_tools
from matplotlib import _api as _api
from tkinter.simpledialog import SimpleDialog as SimpleDialog
from contextlib import contextmanager as contextmanager
from tkinter import Button
from tkinter import Canvas
from tkinter import Checkbutton
from tkinter import Frame
from typing import ClassVar
from typing import Generator
from typing import Optional
from typing import Type
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
from matplotlib.backend_tools import ToolHelpBase
from matplotlib.backends._backend_tk import ConfigureSubplotsTk
from matplotlib.backends._backend_tk import FigureCanvasTk
from matplotlib.backends._backend_tk import FigureManagerTk
from matplotlib.backends._backend_tk import HelpTk
from matplotlib.backends._backend_tk import NavigationToolbar2Tk
from matplotlib.backends._backend_tk import RubberbandTk
from matplotlib.backends._backend_tk import SaveFigureTk
from matplotlib.backends._backend_tk import SetCursorTk
from matplotlib.backends._backend_tk import StatusbarTk
from matplotlib.backends._backend_tk import TimerTk
from matplotlib.backends._backend_tk import ToolTip
from matplotlib.backends._backend_tk import ToolbarTk
from matplotlib.backends._backend_tk import _BackendTk
from object import object

_log: Logger
backend_version: float
cursord: dict[Cursors, str]
from typing import Any

_blit_args: dict[Any, Any]

_blit_tcl_name: str


def _restore_foreground_window_at_end() -> Union[Generator[Any, Any, None], Any]: ...


def _blit(argsid: Any) -> None: ...


def blit(photoimage: {tk},
         aggimage: Any,
         offsets: Any,
         bbox: Any = None) -> Any: ...


class TimerTk(TimerBase):
    parent: Any
    _timer: None

    def __init__(self: TimerTk,
                 parent: Any,
                 *args,
                 **kwargs) -> None: ...

    def _timer_start(self: TimerTk) -> None: ...

    def _timer_stop(self: TimerTk) -> None: ...

    def _on_timer(self: TimerTk) -> None: ...


class FigureCanvasTk(FigureCanvasBase):
    required_interactive_framework: ClassVar[str]
    _idle_callback: None
    _idle: bool
    _tkphoto: PhotoImage
    _resize_callback: Any
    _event_loop_id: None
    _tkcanvas: Canvas
    _master: Any

    @_api.delete_parameter(
        "3.4", "resize_callback",
        alternative="get_tk_widget().bind('<Configure>', ..., True)")
    def __init__(self: FigureCanvasTk,
                 figure: Optional[{set_canvas}] = None,
                 master: Any = None,
                 resize_callback: Any = None) -> Optional[Any]: ...

    def resize(self: FigureCanvasTk,
               event: {width, height}) -> None: ...

    def draw_idle(self: FigureCanvasTk) -> None: ...

    def get_tk_widget(self: FigureCanvasTk) -> Canvas: ...

    def motion_notify_event(self: FigureCanvasTk,
                            event: {x, y}) -> None: ...

    def enter_notify_event(self: FigureCanvasTk,
                           event: {x, y}) -> None: ...

    def button_press_event(self: FigureCanvasTk,
                           event: {x, y},
                           dblclick: bool = False) -> None: ...

    def button_dblclick_event(self: FigureCanvasTk,
                              event: {x, y}) -> None: ...

    def button_release_event(self: FigureCanvasTk,
                             event: {x, y}) -> None: ...

    def scroll_event(self: FigureCanvasTk,
                     event: {x, y}) -> None: ...

    def scroll_event_windows(self: FigureCanvasTk,
                             event: {widget, x_root, y_root}) -> None: ...

    def _get_key(self: FigureCanvasTk,
                 event: {char, keysym}) -> Optional[str]: ...

    def key_press(self: FigureCanvasTk,
                  event: {char, keysym}) -> None: ...

    def key_release(self: FigureCanvasTk,
                    event: {char, keysym}) -> None: ...

    def new_timer(self: FigureCanvasTk,
                  *args,
                  **kwargs) -> TimerTk: ...

    def flush_events(self: FigureCanvasTk) -> None: ...

    def start_event_loop(self: FigureCanvasTk,
                         timeout: int = 0) -> None: ...

    def stop_event_loop(self: FigureCanvasTk) -> None: ...


class FigureManagerTk(FigureManagerBase):
    _owns_mainloop: ClassVar[bool]
    toolbar: Union[ToolbarTk, NavigationToolbar2Tk, None]
    _shown: bool
    window: Any

    def __init__(self: FigureManagerTk,
                 canvas: {manager, figure},
                 num: Any,
                 window: Any) -> None: ...

    def _get_toolbar(self: FigureManagerTk) -> Union[ToolbarTk, NavigationToolbar2Tk, None]: ...

    def resize(self: FigureManagerTk,
               width: {__gt__},
               height: {__gt__}) -> Any: ...

    def show(self: FigureManagerTk) -> None: ...

    def destroy(self: FigureManagerTk,
                *args) -> None: ...

    def get_window_title(self: FigureManagerTk) -> Any: ...

    def set_window_title(self: FigureManagerTk,
                         title: Any) -> None: ...

    def full_screen_toggle(self: FigureManagerTk) -> None: ...


class NavigationToolbar2Tk(NavigationToolbar2, Frame):
    _buttons: dict[Any, Union[Button, Checkbutton]]
    lastrect: Any
    window: Any
    message: StringVar
    _message_label: Label

    def __init__(self: NavigationToolbar2Tk,
                 canvas: {toolbar},
                 window: Any,
                 *,
                 pack_toolbar: bool = True) -> None: ...

    def _update_buttons_checked(self: NavigationToolbar2Tk) -> None: ...

    def pan(self: NavigationToolbar2Tk,
            *args) -> None: ...

    def zoom(self: NavigationToolbar2Tk,
             *args) -> None: ...

    def set_message(self: NavigationToolbar2Tk,
                    s: Any) -> None: ...

    def draw_rubberband(self: NavigationToolbar2Tk,
                        event: Any,
                        x0: Any,
                        y0: Any,
                        x1: Any,
                        y1: Any) -> None: ...

    def release_zoom(self: NavigationToolbar2Tk,
                     event: {x, key, y}) -> None: ...

    def set_cursor(self: NavigationToolbar2Tk,
                   cursor: Any) -> None: ...

    def _Button(self: NavigationToolbar2Tk,
                text: Union[str, Any],
                image_file: Any,
                toggle: Any,
                command: Any) -> Union[Button, Checkbutton]: ...

    def _Spacer(self: NavigationToolbar2Tk) -> Frame: ...

    def save_figure(self: NavigationToolbar2Tk,
                    *args) -> None: ...

    def set_history_buttons(self: NavigationToolbar2Tk) -> None: ...


class ToolTip(object):
    widget: Any
    tipwindow: None
    x: int
    y: int
    id: None
    text: Union[str, Any]

    def createToolTip(widget: Union[Union[Button, Checkbutton], Any],
                      text: Union[str, Any]) -> None: ...

    def __init__(self: ToolTip,
                 widget: Any) -> None: ...

    def showtip(self: ToolTip,
                text: Union[str, Any]) -> None: ...

    def hidetip(self: ToolTip) -> None: ...


class RubberbandTk(RubberbandBase):
    lastrect: Any

    def draw_rubberband(self: RubberbandTk,
                        x0: Any,
                        y0: Any,
                        x1: Any,
                        y1: Any) -> None: ...

    def remove_rubberband(self: RubberbandTk) -> None: ...


class SetCursorTk(SetCursorBase):
    def set_cursor(self: SetCursorTk,
                   cursor: Any) -> None: ...


class ToolbarTk(ToolContainerBase, Frame):
    _message: StringVar
    _toolitems: dict[Any, Any]
    _message_label: Label
    _groups: dict[Any, Any]

    def __init__(self: ToolbarTk,
                 toolmanager: {toolmanager_connect},
                 window: Any) -> None: ...

    def add_toolitem(self: ToolbarTk,
                     name: str,
                     group: str,
                     position: int,
                     image_file: Any,
                     description: str,
                     toggle: bool) -> None: ...

    def _get_groupframe(self: ToolbarTk,
                        group: Union[str, Any]) -> Any: ...

    def _add_separator(self: ToolbarTk) -> Frame: ...

    def _button_click(self: ToolbarTk,
                      name: Union[str, Any]) -> None: ...

    def toggle_toolitem(self: ToolbarTk,
                        name: str,
                        toggled: bool) -> None: ...

    def remove_toolitem(self: ToolbarTk,
                        name: str) -> None: ...

    def set_message(self: ToolbarTk,
                    s: str) -> None: ...


@_api.deprecated("3.3")
class StatusbarTk(StatusbarBase, Frame):
    _message: StringVar
    _message_label: Label

    def __init__(self: StatusbarTk,
                 window: Any,
                 *args,
                 **kwargs) -> None: ...

    def set_message(self: StatusbarTk,
                    s: str) -> None: ...


class SaveFigureTk(SaveFigureBase):
    def trigger(self: SaveFigureTk,
                *args) -> None: ...


class ConfigureSubplotsTk(ConfigureSubplotsBase):
    window: None

    def __init__(self: ConfigureSubplotsTk,
                 *args,
                 **kwargs) -> None: ...

    def trigger(self: ConfigureSubplotsTk,
                *args) -> None: ...

    def init_window(self: ConfigureSubplotsTk) -> None: ...

    def destroy(self: ConfigureSubplotsTk,
                *args,
                **kwargs) -> None: ...


class HelpTk(ToolHelpBase):
    def trigger(self: HelpTk,
                *args) -> None: ...


ToolSaveFigure: Type[SaveFigureTk]
ToolConfigureSubplots: Type[ConfigureSubplotsTk]
ToolSetCursor: Type[SetCursorTk]
ToolRubberband: Type[RubberbandTk]
ToolHelp: Type[HelpTk]
ToolCopyToClipboard: Type[ToolCopyToClipboardBase]
Toolbar: Type[ToolbarTk]


class _BackendTk(_Backend):
    FigureManager: ClassVar[Type[FigureManagerTk]]

    def new_figure_manager_given_figure(cls: Type[_BackendTk],
                                        num: Any,
                                        figure: Any) -> FigureManagerTk: ...

    def mainloop() -> None: ...
