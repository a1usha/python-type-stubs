from typing import Any
from typing import Callable
from typing import Iterable
from typing import Optional
from typing import Union

from matplotlib import _api
from matplotlib.backend_managers import ToolEvent
from matplotlib.backend_managers import ToolManager
from matplotlib.backend_managers import ToolManagerMessageEvent
from matplotlib.backend_managers import ToolTriggerEvent
from matplotlib.backend_tools import ToolToggleBase
from object import object


class ToolEvent(object):
    def __init__(self: ToolEvent,
                 name: Any,
                 sender: Any,
                 tool: Any,
                 data: Any = None) -> None: ...


class ToolTriggerEvent(ToolEvent):
    def __init__(self: ToolTriggerEvent,
                 name: Any,
                 sender: Any,
                 tool: Any,
                 canvasevent: Any = None,
                 data: Any = None) -> None: ...


class ToolManagerMessageEvent(object):
    def __init__(self: ToolManagerMessageEvent,
                 name: Any,
                 sender: Any,
                 message: Any) -> None: ...


class ToolManager(object):
    def __init__(self: ToolManager,
                 figure: Any = None) -> None: ...

    def canvas(self: ToolManager) -> Optional[Any]: ...

    def figure(self: ToolManager) -> Any: ...

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

    def active_toggle(self: ToolManager) -> dict[Any, Any]: ...

    def get_tool_keymap(self: ToolManager,
                        name: str) -> list[Any]: ...

    def _remove_keys(self: ToolManager,
                     name: Union[str, Any]) -> None: ...

    @_api.delete_parameter("3.3", "args")
    def update_keymap(self: ToolManager,
                      name: str,
                      key: Union[str, Iterable[str]],
                      *args) -> Any: ...

    def remove_tool(self: ToolManager,
                    name: str) -> None: ...

    def add_tool(self: ToolManager,
                 name: str,
                 tool: Union[type, Any],
                 *args,
                 **kwargs) -> Union[ToolToggleBase, Any]: ...

    def _tool_added_event(self: ToolManager,
                          tool: Union[ToolToggleBase, Any]) -> None: ...

    def _handle_toggle(self: ToolManager,
                       tool: Any,
                       sender: object,
                       canvasevent: Any,
                       data: object) -> None: ...

    def _get_cls_to_instantiate(self: ToolManager,
                                callback_class: Union[type, Any]) -> Union[Callable, Callable, Callable, None]: ...

    def trigger_tool(self: ToolManager,
                     name: str,
                     sender: object = None,
                     canvasevent: Any = None,
                     data: object = None) -> None: ...

    def _trigger_tool(self: ToolManager,
                      name: Union[str, Any],
                      sender: Any = None,
                      canvasevent: Any = None,
                      data: Any = None) -> None: ...

    def _key_press(self: ToolManager,
                   event: {key}) -> None: ...

    def tools(self: ToolManager) -> dict[Any, Any]: ...

    def get_tool(self: ToolManager,
                 name: Any,
                 warn: bool = True) -> Any: ...
