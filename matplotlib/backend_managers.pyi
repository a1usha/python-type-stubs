from typing import Any
from typing import Iterable
from typing import Union

from matplotlib.backend_tools import ToolToggleBase


class ToolManagerMessageEvent(object):
    def __init__(self: ToolManagerMessageEvent,
                 name: Any,
                 sender: Any,
                 message: Any) -> None: ...


class ToolTriggerEvent(ToolEvent):
    def __init__(self: ToolTriggerEvent,
                 name: Any,
                 sender: Any,
                 tool: Any,
                 canvasevent: Any = None,
                 data: Any = None) -> None: ...


class ToolManager(object):
    def __init__(self: ToolManager,
                 figure: Any = None) -> None: ...

    @property
    def canvas(self: ToolManager) -> Optional[Any]: ...

    @property
    def figure(self: ToolManager) -> Any: ...

    @figure.setter
    def figure(self: ToolManager,
               figure: Any) -> None: ...

    def set_figure(self: ToolManager,
                   figure: Any,
                   update_tools: bool = True) -> None: ...

    def toolmanager_connect(self: ToolManager,
                            s: str,
                            func: Callable) -> Any: ...

    def toolmanager_disconnect(self: ToolManager,
                               cid: Any) -> None: ...

    def message_event(self: ToolManager,
                      message: Any,
                      sender: Any = None) -> None: ...

    @property
    def active_toggle(self: ToolManager) -> dict: ...

    def get_tool_keymap(self: ToolManager,
                        name: str) -> list: ...

    def _remove_keys(self: ToolManager,
                     name: str) -> None: ...

    @_api.delete_parameter("3.3", "args")
    def update_keymap(self: ToolManager,
                      name: str,
                      key: Union[str, Iterable[str]],
                      *args) -> Any: ...

    def remove_tool(self: ToolManager,
                    name: str) -> None: ...

    def add_tool(self: ToolManager,
                 name: str,
                 tool: type,
                 *args,
                 **kwargs) -> ToolToggleBase: ...

    def _tool_added_event(self: ToolManager,
                          tool: ToolToggleBase) -> None: ...

    def _handle_toggle(self: ToolManager,
                       tool: Any,
                       sender: object,
                       canvasevent: Any,
                       data: object) -> None: ...

    def _get_cls_to_instantiate(self: ToolManager,
                                callback_class: type) -> Union[Callable, Callable, Callable, None]: ...

    def trigger_tool(self: ToolManager,
                     name: str,
                     sender: object = None,
                     canvasevent: Any = None,
                     data: object = None) -> None: ...

    def _trigger_tool(self: ToolManager,
                      name: str,
                      sender: Any = None,
                      canvasevent: Any = None,
                      data: Any = None) -> None: ...

    def _key_press(self: ToolManager,
                   event: {key}) -> None: ...

    @property
    def tools(self: ToolManager) -> dict: ...

    def get_tool(self: ToolManager,
                 name: Any,
                 warn: bool = True) -> Any: ...


class ToolEvent(object):
    def __init__(self: ToolEvent,
                 name: Any,
                 sender: Any,
                 tool: Any,
                 data: Any = None) -> None: ...
