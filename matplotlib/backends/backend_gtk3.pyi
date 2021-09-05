from gi.repository import Gdk as Gdk
from gi.repository import Gtk as Gtk
from gi.repository import GObject as GObject
from gi.repository import GLib as GLib
from gi.repository import Gio as Gio
from matplotlib.widgets import SubplotTool as SubplotTool
from matplotlib.figure import Figure as Figure
from matplotlib.backend_bases import cursors as cursors
from matplotlib.backend_bases import ToolContainerBase as ToolContainerBase
from matplotlib.backend_bases import TimerBase as TimerBase
from matplotlib.backend_bases import StatusbarBase as StatusbarBase
from matplotlib.backend_bases import NavigationToolbar2 as NavigationToolbar2
from matplotlib.backend_bases import FigureManagerBase as FigureManagerBase
from matplotlib.backend_bases import FigureCanvasBase as FigureCanvasBase
from matplotlib.backend_bases import _Backend as _Backend
from matplotlib._pylab_helpers import Gcf as Gcf
from matplotlib import cbook as cbook
from matplotlib import backend_tools as backend_tools
from matplotlib import _api as _api
from pathlib import Path as Path
from typing import Any
from typing import ClassVar
from typing import Optional
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
from matplotlib.backends.backend_gtk3 import ConfigureSubplotsGTK3
from matplotlib.backends.backend_gtk3 import FigureCanvasGTK3
from matplotlib.backends.backend_gtk3 import FigureManagerGTK3
from matplotlib.backends.backend_gtk3 import HelpGTK3
from matplotlib.backends.backend_gtk3 import NavigationToolbar2GTK3
from matplotlib.backends.backend_gtk3 import RubberbandGTK3
from matplotlib.backends.backend_gtk3 import SaveFigureGTK3
from matplotlib.backends.backend_gtk3 import SetCursorGTK3
from matplotlib.backends.backend_gtk3 import StatusbarGTK3
from matplotlib.backends.backend_gtk3 import TimerGTK3
from matplotlib.backends.backend_gtk3 import ToolCopyToClipboardGTK3
from matplotlib.backends.backend_gtk3 import ToolbarGTK3

backend_version: str


class TimerGTK3(TimerBase):
    _timer: None

    def __init__(self: TimerGTK3,
                 *args,
                 **kwargs) -> None: ...

    def _timer_start(self: TimerGTK3) -> None: ...

    def _timer_stop(self: TimerGTK3) -> None: ...

    def _timer_set_interval(self: TimerGTK3) -> None: ...

    def _on_timer(self: TimerGTK3) -> bool: ...


class FigureCanvasGTK3(FigureCanvasBase):
    required_interactive_framework: ClassVar[str]
    _timer_cls: ClassVar[Type[TimerGTK3]]
    event_mask: ClassVar[Any]
    _lastCursor: None
    _idle_draw_id: int
    _rubberband_rect: None

    def __init__(self: FigureCanvasGTK3,
                 figure: Optional[{set_canvas}] = None) -> None: ...

    @_api.deprecated("3.3", alternative="__init__")
    def _renderer_init(self: FigureCanvasGTK3) -> Optional[Any]: ...

    def destroy(self: FigureCanvasGTK3) -> None: ...

    def scroll_event(self: FigureCanvasGTK3,
                     widget: Any,
                     event: {x, y, direction}) -> bool: ...

    def button_press_event(self: FigureCanvasGTK3,
                           widget: Any,
                           event: {x, y, button}) -> bool: ...

    def button_release_event(self: FigureCanvasGTK3,
                             widget: Any,
                             event: {x, y, button}) -> bool: ...

    def key_press_event(self: FigureCanvasGTK3,
                        widget: Any,
                        event: {keyval, state}) -> bool: ...

    def key_release_event(self: FigureCanvasGTK3,
                          widget: Any,
                          event: {keyval, state}) -> bool: ...

    def motion_notify_event(self: FigureCanvasGTK3,
                            widget: Any,
                            event: {is_hint}) -> bool: ...

    def leave_notify_event(self: FigureCanvasGTK3,
                           widget: Any,
                           event: Any) -> None: ...

    def enter_notify_event(self: FigureCanvasGTK3,
                           widget: Any,
                           event: {x, y}) -> None: ...

    def size_allocate(self: FigureCanvasGTK3,
                      widget: Any,
                      allocation: {width, height}) -> None: ...

    def _get_key(self: FigureCanvasGTK3,
                 event: {keyval, state}) -> Union[Union[{isprintable}, str], Any]: ...

    def configure_event(self: FigureCanvasGTK3,
                        widget: {get_property},
                        event: {width, height}) -> Optional[bool]: ...

    def _draw_rubberband(self: FigureCanvasGTK3,
                         rect: Any) -> None: ...

    def _post_draw(self: FigureCanvasGTK3,
                   widget: Any,
                   ctx: {move_to, line_to, set_antialias, set_line_width, set_dash, set_source_rgb, stroke_preserve,
                         stroke}) -> None: ...

    def on_draw_event(self: FigureCanvasGTK3,
                      widget: Any,
                      ctx: Any) -> None: ...

    def draw(self: FigureCanvasGTK3) -> None: ...

    def draw_idle(self: FigureCanvasGTK3) -> None: ...

    def flush_events(self: FigureCanvasGTK3) -> None: ...


class FigureManagerGTK3(FigureManagerBase):
    _full_screen_flag: ClassVar[bool]
    toolbar: Union[ToolbarGTK3, NavigationToolbar2GTK3, None]
    vbox: Any
    _destroying: bool
    _full_screen_flag: bool
    window: Any

    def __init__(self: FigureManagerGTK3,
                 canvas: {manager, figure},
                 num: Any) -> None: ...

    def destroy(self: FigureManagerGTK3,
                *args) -> None: ...

    def show(self: FigureManagerGTK3) -> None: ...

    def full_screen_toggle(self: FigureManagerGTK3) -> None: ...

    def _get_toolbar(self: FigureManagerGTK3) -> Union[ToolbarGTK3, NavigationToolbar2GTK3, None]: ...

    def get_window_title(self: FigureManagerGTK3) -> Any: ...

    def set_window_title(self: FigureManagerGTK3,
                         title: Any) -> None: ...

    def resize(self: FigureManagerGTK3,
               width: Any,
               height: Any) -> None: ...


class NavigationToolbar2GTK3(NavigationToolbar2):
    ctx: ClassVar[Union[_deprecated_property, Any]]
    _gtk_ids: dict[Any, Any]
    message: Any
    win: Any

    def __init__(self: NavigationToolbar2GTK3,
                 canvas: {toolbar},
                 window: Any) -> None: ...

    def set_message(self: NavigationToolbar2GTK3,
                    s: Any) -> None: ...

    def set_cursor(self: NavigationToolbar2GTK3,
                   cursor: Any) -> None: ...

    def draw_rubberband(self: NavigationToolbar2GTK3,
                        event: Optional[Any],
                        x0: Any,
                        y0: Any,
                        x1: {__sub__},
                        y1: Any) -> None: ...

    def remove_rubberband(self: NavigationToolbar2GTK3) -> None: ...

    def _update_buttons_checked(self: NavigationToolbar2GTK3) -> None: ...

    def pan(self: NavigationToolbar2GTK3,
            *args) -> None: ...

    def zoom(self: NavigationToolbar2GTK3,
             *args) -> None: ...

    def save_figure(self: NavigationToolbar2GTK3,
                    *args) -> None: ...

    def set_history_buttons(self: NavigationToolbar2GTK3) -> None: ...


class ToolbarGTK3(ToolContainerBase):
    _icon_extension: ClassVar[str]
    _message: Any
    _toolitems: dict[Any, Any]
    _groups: dict[Any, Any]

    def __init__(self: ToolbarGTK3,
                 toolmanager: {toolmanager_connect}) -> None: ...

    def add_toolitem(self: ToolbarGTK3,
                     name: str,
                     group: str,
                     position: int,
                     image_file: Any,
                     description: str,
                     toggle: bool) -> None: ...

    def _add_button(self: ToolbarGTK3,
                    button: Any,
                    group: Any,
                    position: Any) -> None: ...

    def _call_tool(self: ToolbarGTK3,
                   btn: Any,
                   name: Any) -> None: ...

    def toggle_toolitem(self: ToolbarGTK3,
                        name: str,
                        toggled: bool) -> None: ...

    def remove_toolitem(self: ToolbarGTK3,
                        name: str) -> None: ...

    def _add_separator(self: ToolbarGTK3) -> None: ...

    def set_message(self: ToolbarGTK3,
                    s: str) -> None: ...


@_api.deprecated("3.3")
class StatusbarGTK3(StatusbarBase):
    _context: Any

    def __init__(self: StatusbarGTK3,
                 *args,
                 **kwargs) -> None: ...

    def set_message(self: StatusbarGTK3,
                    s: str) -> None: ...


class RubberbandGTK3(RubberbandBase):
    def draw_rubberband(self: RubberbandGTK3,
                        x0: Any,
                        y0: Any,
                        x1: {__sub__},
                        y1: Any) -> None: ...

    def remove_rubberband(self: RubberbandGTK3) -> None: ...


class SaveFigureGTK3(SaveFigureBase):
    def trigger(self: SaveFigureGTK3,
                *args,
                **kwargs) -> None: ...


class SetCursorGTK3(SetCursorBase):
    def set_cursor(self: SetCursorGTK3,
                   cursor: Any) -> None: ...


class ConfigureSubplotsGTK3(ConfigureSubplotsBase):
    def _get_canvas(self: ConfigureSubplotsGTK3,
                    fig: Any) -> Any: ...

    def trigger(self: ConfigureSubplotsGTK3,
                *args) -> None: ...


class HelpGTK3(ToolHelpBase):
    def _normalize_shortcut(self: HelpGTK3,
                            key: {split}) -> Union[str, Any]: ...

    def _is_valid_shortcut(self: HelpGTK3,
                           key: {startswith}) -> Union[bool, Any]: ...

    def _show_shortcuts_window(self: HelpGTK3) -> None: ...

    def _show_shortcuts_dialog(self: HelpGTK3) -> None: ...

    def trigger(self: HelpGTK3,
                *args) -> None: ...


class ToolCopyToClipboardGTK3(ToolCopyToClipboardBase):
    def trigger(self: ToolCopyToClipboardGTK3,
                *args,
                **kwargs) -> None: ...


window_icon: str

ToolSaveFigure: Type[SaveFigureGTK3]

ToolConfigureSubplots: Type[ConfigureSubplotsGTK3]

ToolSetCursor: Type[SetCursorGTK3]

ToolRubberband: Type[RubberbandGTK3]

ToolHelp: Type[HelpGTK3]

ToolCopyToClipboard: Type[ToolCopyToClipboardGTK3]

Toolbar: Type[ToolbarGTK3]


def error_msg_gtk(msg: Union[str, Any],
                  parent: Union[NavigationToolbar2GTK3, Any] = None) -> None: ...


class _BackendGTK3(_Backend):
    FigureCanvas: ClassVar[Type[FigureCanvasGTK3]]
    FigureManager: ClassVar[Type[FigureManagerGTK3]]

    def mainloop() -> None: ...
