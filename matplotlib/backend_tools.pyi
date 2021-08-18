from enum import IntEnum
from types import SimpleNamespace
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


class Cursors(IntEnum):
    pass


class ToolBase(object):
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
    def __init__(self: ToolToggleBase,
                 *args,
                 **kwargs) -> None: ...

    def trigger(self: ToolToggleBase,
                sender: object,
                event: Optional[{inaxes}],
                data: object = None) -> None: ...

    def enable(self: ToolToggleBase,
               event: Optional[{inaxes}] = None) -> None: ...

    def disable(self: ToolToggleBase,
                event: Optional[{inaxes}] = None) -> None: ...

    def toggled(self: ToolToggleBase) -> bool: ...

    def set_figure(self: ToolToggleBase,
                   figure: Any) -> None: ...


class SetCursorBase(ToolBase):
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
                   cursor: Cursors) -> Any: ...


class ToolCursorPosition(ToolBase):
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
    def trigger(self: ToolQuit,
                sender: object,
                event: Any,
                data: object = None) -> None: ...


class ToolQuitAll(ToolBase):
    def trigger(self: ToolQuitAll,
                sender: object,
                event: Any,
                data: object = None) -> None: ...


class _ToolEnableAllNavigation(ToolBase):
    def trigger(self: _ToolEnableAllNavigation,
                sender: object,
                event: Any,
                data: object = None) -> None: ...


@_api.deprecated("3.3")
class ToolEnableAllNavigation(_ToolEnableAllNavigation):
    pass


class _ToolEnableNavigation(ToolBase):
    def trigger(self: _ToolEnableNavigation,
                sender: object,
                event: Any,
                data: object = None) -> None: ...


@_api.deprecated("3.3")
class ToolEnableNavigation(_ToolEnableNavigation):
    pass


class ToolGrid(ToolBase):
    def trigger(self: ToolGrid,
                sender: object,
                event: {__dict__},
                data: object = None) -> None: ...


class ToolMinorGrid(ToolBase):
    def trigger(self: ToolMinorGrid,
                sender: object,
                event: {__dict__},
                data: object = None) -> None: ...


class ToolFullScreen(ToolToggleBase):
    def enable(self: ToolFullScreen,
               event: Optional[{inaxes}]) -> None: ...

    def disable(self: ToolFullScreen,
                event: Optional[{inaxes}]) -> None: ...


class AxisScaleBase(ToolToggleBase):
    def trigger(self: AxisScaleBase,
                sender: object,
                event: Optional[Any],
                data: object = None) -> None: ...

    def enable(self: AxisScaleBase,
               event: Optional[{inaxes}]) -> None: ...

    def disable(self: AxisScaleBase,
                event: Optional[{inaxes}]) -> None: ...


class ToolYScale(AxisScaleBase):
    def set_scale(self: ToolYScale,
                  ax: {set_yscale},
                  scale: Any) -> None: ...


class ToolXScale(AxisScaleBase):
    def set_scale(self: ToolXScale,
                  ax: {set_xscale},
                  scale: Any) -> None: ...


class ToolViewsPositions(ToolBase):
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
    def trigger(self: ViewsPositionsBase,
                sender: object,
                event: Any,
                data: object = None) -> None: ...


class ToolHome(ViewsPositionsBase):
    pass


class ToolBack(ViewsPositionsBase):
    pass


class ToolForward(ViewsPositionsBase):
    pass


class ConfigureSubplotsBase(ToolBase):
    pass


class SaveFigureBase(ToolBase):
    pass


class ZoomPanBase(ToolToggleBase):
    def __init__(self: ZoomPanBase,
                 *args) -> None: ...

    def enable(self: ZoomPanBase,
               event: Optional[{inaxes}]) -> None: ...

    def disable(self: ZoomPanBase,
                event: Optional[{inaxes}]) -> None: ...

    def trigger(self: ZoomPanBase,
                sender: object,
                event: Optional[{inaxes}],
                data: object = None) -> None: ...

    def scroll_zoom(self: ZoomPanBase,
                    event: {inaxes, button, x, y}) -> None: ...


class ToolZoom(ZoomPanBase):
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
                    event: {key}) -> None: ...

    def _release(self: ToolZoom,
                 event: {x, y}) -> None: ...


class ToolPan(ZoomPanBase):
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
    def format_shortcut(key_sequence: {__len__}) -> Union[{__len__}, str]: ...

    def _format_tool_keymap(self: ToolHelpBase,
                            name: Any) -> str: ...

    def _get_help_entries(self: ToolHelpBase) -> list[Tuple[Any, str, Any]]: ...

    def _get_help_text(self: ToolHelpBase) -> str: ...

    def _get_help_html(self: ToolHelpBase) -> str: ...


class ToolCopyToClipboardBase(ToolBase):
    def trigger(self: ToolCopyToClipboardBase,
                *args,
                **kwargs) -> None: ...


def add_tools_to_manager(toolmanager: Any,
                         tools: Any = default_tools) -> None: ...


def add_tools_to_container(container: Any,
                           tools: Optional[Iterable] = default_toolbar_tools) -> None: ...