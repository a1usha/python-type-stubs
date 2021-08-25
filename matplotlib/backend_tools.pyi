from matplotlib import cbook as cbook
from matplotlib import _api as _api
from matplotlib._pylab_helpers import Gcf as Gcf
from weakref import WeakKeyDictionary as WeakKeyDictionary
from types import SimpleNamespace as SimpleNamespace
from enum import IntEnum as IntEnum
from enum import IntEnum
from types import SimpleNamespace
from typing import Any
from typing import ClassVar
from typing import Iterable
from typing import Optional
from typing import Union

from matplotlib import _api
from matplotlib.axes._axes import Axes
from matplotlib.backend_tools import AxisScaleBase
from matplotlib.backend_tools import Cursors
from matplotlib.backend_tools import RubberbandBase
from matplotlib.backend_tools import SetCursorBase
from matplotlib.backend_tools import ToolBase
from matplotlib.backend_tools import ToolCopyToClipboardBase
from matplotlib.backend_tools import ToolCursorPosition
from matplotlib.backend_tools import ToolFullScreen
from matplotlib.backend_tools import ToolGrid
from matplotlib.backend_tools import ToolHelpBase
from matplotlib.backend_tools import ToolMinorGrid
from matplotlib.backend_tools import ToolPan
from matplotlib.backend_tools import ToolQuit
from matplotlib.backend_tools import ToolQuitAll
from matplotlib.backend_tools import ToolToggleBase
from matplotlib.backend_tools import ToolViewsPositions
from matplotlib.backend_tools import ToolXScale
from matplotlib.backend_tools import ToolYScale
from matplotlib.backend_tools import ToolZoom
from matplotlib.backend_tools import ViewsPositionsBase
from matplotlib.backend_tools import ZoomPanBase
from matplotlib.backend_tools import _ToolEnableAllNavigation
from matplotlib.backend_tools import _ToolEnableNavigation
from object import object

cursors: Type[Cursors]

_views_positions: str


class Cursors(IntEnum):
    HAND: ClassVar[Cursors]
    POINTER: ClassVar[Cursors]
    SELECT_REGION: ClassVar[Cursors]
    MOVE: ClassVar[Cursors]
    WAIT: ClassVar[Cursors]
    pass


class ToolBase(object):
    default_keymap: ClassVar[None]
    description: ClassVar[None]
    image: ClassVar[None]
    _name: Any
    _figure: None
    _toolmanager: Any

    def __init__(self: ToolBase,
                 toolmanager: Any,
                 name: Any) -> None: ...

    def figure(self: ToolBase) -> Any: ...

    def figure(self: ToolBase,
               figure: Any) -> None: ...

    def canvas(self: ToolBase) -> Optional[Any]: ...

    def toolmanager(self: ToolBase) -> Any: ...

    def _make_classic_style_pseudo_toolbar(self: ToolBase) -> SimpleNamespace: ...

    def set_figure(self: ToolBase,
                   figure: Any) -> None: ...

    def trigger(self: ToolBase,
                sender: object,
                event: Any,
                data: object = None) -> None: ...

    def name(self: ToolBase) -> Any: ...

    def destroy(self: ToolBase) -> None: ...


class ToolToggleBase(ToolBase):
    radio_group: ClassVar[None]
    cursor: ClassVar[None]
    default_toggled: ClassVar[bool]
    _toggled: Union[bool, Any]

    def __init__(self: ToolToggleBase,
                 *args,
                 **kwargs) -> None: ...

    def trigger(self: ToolToggleBase,
                sender: object,
                event: Union[Optional[{inaxes}], Any],
                data: object = None) -> None: ...

    def enable(self: ToolToggleBase,
               event: Union[Optional[{inaxes}], Any] = None) -> None: ...

    def disable(self: ToolToggleBase,
                event: Union[Optional[{inaxes}], Any] = None) -> None: ...

    def toggled(self: ToolToggleBase) -> Union[bool, Any]: ...

    def set_figure(self: ToolToggleBase,
                   figure: Any) -> None: ...


class SetCursorBase(ToolBase):
    _cursor: None
    _id_drag: None
    _last_cursor: Cursors
    _default_cursor: Cursors

    def __init__(self: SetCursorBase,
                 *args,
                 **kwargs) -> None: ...

    def set_figure(self: SetCursorBase,
                   figure: Any) -> None: ...

    def _tool_trigger_cbk(self: SetCursorBase,
                          event: {tool, canvasevent}) -> None: ...

    def _add_tool(self: SetCursorBase,
                  tool: Any) -> None: ...

    def _add_tool_cbk(self: SetCursorBase,
                      event: {tool}) -> None: ...

    def _set_cursor_cbk(self: SetCursorBase,
                        event: Any) -> None: ...

    def set_cursor(self: SetCursorBase,
                   cursor: Union[Cursors, Any]) -> Any: ...


class ToolCursorPosition(ToolBase):
    _id_drag: None

    def __init__(self: ToolCursorPosition,
                 *args,
                 **kwargs) -> None: ...

    def set_figure(self: ToolCursorPosition,
                   figure: Any) -> None: ...

    def send_message(self: ToolCursorPosition,
                     event: {inaxes}) -> None: ...


class RubberbandBase(ToolBase):
    def trigger(self: RubberbandBase,
                sender: object,
                event: Any,
                data: object) -> None: ...

    def draw_rubberband(self: RubberbandBase,
                        *args) -> Any: ...

    def remove_rubberband(self: RubberbandBase) -> None: ...


class ToolQuit(ToolBase):
    description: ClassVar[str]
    default_keymap: ClassVar[Optional[Any]]

    def trigger(self: ToolQuit,
                sender: object,
                event: Any,
                data: object = None) -> None: ...


class ToolQuitAll(ToolBase):
    description: ClassVar[str]
    default_keymap: ClassVar[Optional[Any]]

    def trigger(self: ToolQuitAll,
                sender: object,
                event: Any,
                data: object = None) -> None: ...


class _ToolEnableAllNavigation(ToolBase):
    description: ClassVar[str]
    default_keymap: ClassVar[Optional[Any]]

    def trigger(self: _ToolEnableAllNavigation,
                sender: object,
                event: Any,
                data: object = None) -> None: ...


@_api.deprecated("3.3")
class ToolEnableAllNavigation(_ToolEnableAllNavigation):
    pass


class _ToolEnableNavigation(ToolBase):
    description: ClassVar[str]
    default_keymap: ClassVar[tuple[str, str, str, str, str, str, str, str, str]]

    def trigger(self: _ToolEnableNavigation,
                sender: object,
                event: Any,
                data: object = None) -> None: ...


@_api.deprecated("3.3")
class ToolEnableNavigation(_ToolEnableNavigation):
    pass


class ToolGrid(ToolBase):
    description: ClassVar[str]
    default_keymap: ClassVar[Optional[Any]]

    def trigger(self: ToolGrid,
                sender: object,
                event: {__dict__},
                data: object = None) -> None: ...


class ToolMinorGrid(ToolBase):
    description: ClassVar[str]
    default_keymap: ClassVar[Optional[Any]]

    def trigger(self: ToolMinorGrid,
                sender: object,
                event: {__dict__},
                data: object = None) -> None: ...


class ToolFullScreen(ToolToggleBase):
    description: ClassVar[str]
    default_keymap: ClassVar[Optional[Any]]

    def enable(self: ToolFullScreen,
               event: Union[Optional[{inaxes}], Any]) -> None: ...

    def disable(self: ToolFullScreen,
                event: Union[Optional[{inaxes}], Any]) -> None: ...


class AxisScaleBase(ToolToggleBase):
    def trigger(self: AxisScaleBase,
                sender: object,
                event: Optional[Any],
                data: object = None) -> None: ...

    def enable(self: AxisScaleBase,
               event: Union[Optional[{inaxes}], Any]) -> None: ...

    def disable(self: AxisScaleBase,
                event: Union[Optional[{inaxes}], Any]) -> None: ...


class ToolYScale(AxisScaleBase):
    description: ClassVar[str]
    default_keymap: ClassVar[Optional[Any]]

    def set_scale(self: ToolYScale,
                  ax: {set_yscale},
                  scale: Any) -> None: ...


class ToolXScale(AxisScaleBase):
    description: ClassVar[str]
    default_keymap: ClassVar[Optional[Any]]

    def set_scale(self: ToolXScale,
                  ax: {set_xscale},
                  scale: Any) -> None: ...


class ToolViewsPositions(ToolBase):
    positions: WeakKeyDictionary
    home_views: WeakKeyDictionary
    views: WeakKeyDictionary

    def __init__(self: ToolViewsPositions,
                 *args,
                 **kwargs) -> None: ...

    def add_figure(self: ToolViewsPositions,
                   figure: Any) -> None: ...

    def clear(self: ToolViewsPositions,
              figure: Any) -> None: ...

    def update_view(self: ToolViewsPositions) -> None: ...

    def push_current(self: ToolViewsPositions,
                     figure: {get_axes} = None) -> None: ...

    def _axes_pos(self: ToolViewsPositions,
                  ax: Axes) -> Any: ...

    def update_home_views(self: ToolViewsPositions,
                          figure: {get_axes} = None) -> None: ...

    @_api.deprecated("3.3", alternative="self.figure.canvas.draw_idle()")
    def refresh_locators(self: ToolViewsPositions) -> Optional[Any]: ...

    def _refresh_locators(self: ToolViewsPositions) -> None: ...

    def home(self: ToolViewsPositions) -> None: ...

    def back(self: ToolViewsPositions) -> None: ...

    def forward(self: ToolViewsPositions) -> None: ...


class ViewsPositionsBase(ToolBase):
    _on_trigger: ClassVar[None]

    def trigger(self: ViewsPositionsBase,
                sender: object,
                event: Any,
                data: object = None) -> None: ...


class ToolHome(ViewsPositionsBase):
    description: ClassVar[str]
    image: ClassVar[str]
    default_keymap: ClassVar[Optional[Any]]
    _on_trigger: ClassVar[str]
    pass


class ToolBack(ViewsPositionsBase):
    description: ClassVar[str]
    image: ClassVar[str]
    default_keymap: ClassVar[Optional[Any]]
    _on_trigger: ClassVar[str]
    pass


class ToolForward(ViewsPositionsBase):
    description: ClassVar[str]
    image: ClassVar[str]
    default_keymap: ClassVar[Optional[Any]]
    _on_trigger: ClassVar[str]
    pass


class ConfigureSubplotsBase(ToolBase):
    description: ClassVar[str]
    image: ClassVar[str]
    pass


class SaveFigureBase(ToolBase):
    description: ClassVar[str]
    image: ClassVar[str]
    default_keymap: ClassVar[Optional[Any]]
    pass


class ZoomPanBase(ToolToggleBase):
    _xypress: None
    _idPress: None
    scrollthresh: float
    _button_pressed: None
    lastscroll: float
    base_scale: float
    _idRelease: None
    _idScroll: None

    def __init__(self: ZoomPanBase,
                 *args) -> None: ...

    def enable(self: ZoomPanBase,
               event: Union[Optional[{inaxes}], Any]) -> None: ...

    def disable(self: ZoomPanBase,
                event: Union[Optional[{inaxes}], Any]) -> None: ...

    def trigger(self: ZoomPanBase,
                sender: object,
                event: Union[Optional[{inaxes}], Any],
                data: object = None) -> None: ...

    def scroll_zoom(self: ZoomPanBase,
                    event: {inaxes, button, x, y}) -> None: ...


class ToolZoom(ZoomPanBase):
    description: ClassVar[str]
    image: ClassVar[str]
    default_keymap: ClassVar[Optional[Any]]
    cursor: ClassVar[Cursors]
    radio_group: ClassVar[str]
    _zoom_mode: Any
    _xypress: None
    _button_pressed: None
    _ids_zoom: list[Any]

    def __init__(self: ToolZoom,
                 *args) -> None: ...

    def _cancel_action(self: ToolZoom) -> None: ...

    def _press(self: ToolZoom,
               event: {button, x, y, key}) -> None: ...

    def _switch_on_zoom_mode(self: ToolZoom,
                             event: {key}) -> None: ...

    def _switch_off_zoom_mode(self: ToolZoom,
                              event: Any) -> None: ...

    def _mouse_move(self: ToolZoom,
                    event: Union[{key}, Any]) -> None: ...

    def _release(self: ToolZoom,
                 event: {x, y}) -> None: ...


class ToolPan(ZoomPanBase):
    default_keymap: ClassVar[Optional[Any]]
    description: ClassVar[str]
    image: ClassVar[str]
    cursor: ClassVar[Cursors]
    radio_group: ClassVar[str]
    _id_drag: None
    _xypress: list[Any]
    _button_pressed: None

    def __init__(self: ToolPan,
                 *args) -> None: ...

    def _cancel_action(self: ToolPan) -> None: ...

    def _press(self: ToolPan,
               event: {button, x, y}) -> None: ...

    def _release(self: ToolPan,
                 event: Any) -> None: ...

    def _mouse_move(self: ToolPan,
                    event: {key, x, y}) -> None: ...


class ToolHelpBase(ToolBase):
    description: ClassVar[str]
    default_keymap: ClassVar[Optional[Any]]
    image: ClassVar[str]

    def format_shortcut(key_sequence: {__len__}) -> Union[{__len__}, str]: ...

    def _format_tool_keymap(self: ToolHelpBase,
                            name: Any) -> str: ...

    def _get_help_entries(self: ToolHelpBase) -> list[Tuple[Any, str, Any]]: ...

    def _get_help_text(self: ToolHelpBase) -> str: ...

    def _get_help_html(self: ToolHelpBase) -> str: ...


class ToolCopyToClipboardBase(ToolBase):
    description: ClassVar[str]
    default_keymap: ClassVar[Optional[Any]]

    def trigger(self: ToolCopyToClipboardBase,
                *args,
                **kwargs) -> None: ...


default_tools: dict[Union[str, Any], Union[Union[
                                               Type[ToolHome], Type[ToolBack], Type[ToolForward], Type[ToolZoom], Type[
                                                   ToolPan], str, Type[ToolGrid], Type[ToolMinorGrid], Type[
                                                   ToolFullScreen]], Any]]
default_toolbar_tools: list[list[Union[str, list[str]]]]


def add_tools_to_manager(toolmanager: Any,
                         tools: Any = default_tools) -> None: ...


def add_tools_to_container(container: Any,
                           tools: Optional[Iterable] = default_toolbar_tools) -> None: ...