from matplotlib.backend_bases import MouseButton as MouseButton
from matplotlib import _api as _api
from numbers import Integral as Integral
from typing import Any
from typing import ClassVar
from typing import Union

from matplotlib.backend_bases import MouseButton
from matplotlib.blocking_input import BlockingContourLabeler
from matplotlib.blocking_input import BlockingInput
from matplotlib.blocking_input import BlockingKeyMouseInput
from matplotlib.blocking_input import BlockingMouseInput
from object import object


class BlockingInput(object):
    pop: ClassVar[Callable[[BlockingInput, int], None]]
    fig: Any
    eventslist: Union[tuple, Any]
    callbacks: list[Any]
    n: int
    events: list[Any]

    def __init__(self: BlockingInput,
                 fig: Any,
                 eventslist: Union[tuple, Any] = ()) -> None: ...

    def on_event(self: BlockingInput,
                 event: Any) -> None: ...

    def post_event(self: BlockingInput) -> None: ...

    def cleanup(self: BlockingInput) -> None: ...

    def add_event(self: BlockingInput,
                  event: Any) -> None: ...

    def pop_event(self: BlockingInput,
                  index: int = -1) -> None: ...

    def __call__(self: BlockingInput,
                 n: int = 1,
                 timeout: int = 30) -> list[Any]: ...


class BlockingMouseInput(BlockingInput):
    button_add: ClassVar[MouseButton]
    button_pop: ClassVar[MouseButton]
    button_stop: ClassVar[MouseButton]
    button_pop: MouseButton
    show_clicks: bool
    button_add: MouseButton
    clicks: list[Any]
    marks: list[Any]
    button_stop: MouseButton

    def __init__(self: BlockingMouseInput,
                 fig: Any,
                 mouse_add: MouseButton = MouseButton.LEFT,
                 mouse_pop: MouseButton = MouseButton.RIGHT,
                 mouse_stop: MouseButton = MouseButton.MIDDLE) -> None: ...

    def post_event(self: BlockingMouseInput) -> None: ...

    def mouse_event(self: BlockingMouseInput) -> None: ...

    def key_event(self: BlockingMouseInput) -> None: ...

    def mouse_event_add(self: BlockingMouseInput,
                        event: Any) -> None: ...

    def mouse_event_stop(self: BlockingMouseInput,
                         event: Any) -> None: ...

    def mouse_event_pop(self: BlockingMouseInput,
                        event: Any) -> None: ...

    def add_click(self: BlockingMouseInput,
                  event: Any) -> None: ...

    def pop_click(self: BlockingMouseInput,
                  event: Any,
                  index: int = -1) -> None: ...

    def pop(self: BlockingMouseInput,
            event: Any,
            index: int = -1) -> None: ...

    def cleanup(self: BlockingMouseInput,
                event: Any = None) -> None: ...

    def __call__(self: BlockingMouseInput,
                 n: int = 1,
                 timeout: int = 30,
                 show_clicks: bool = True) -> list[Any]: ...


class BlockingContourLabeler(BlockingMouseInput):
    cs: {axes}
    inline: Any
    inline_spacing: int

    def __init__(self: BlockingContourLabeler,
                 cs: {axes}) -> None: ...

    def add_click(self: BlockingContourLabeler,
                  event: Any) -> None: ...

    def pop_click(self: BlockingContourLabeler,
                  event: Any,
                  index: int = -1) -> None: ...

    def button1(self: BlockingContourLabeler,
                event: Any) -> None: ...

    def button3(self: BlockingContourLabeler,
                event: Any) -> None: ...

    def __call__(self: BlockingContourLabeler,
                 inline: Any,
                 inline_spacing: int = 5,
                 n: int = -1,
                 timeout: int = -1) -> None: ...


class BlockingKeyMouseInput(BlockingInput):
    keyormouse: Union[bool, Any]

    def __init__(self: BlockingKeyMouseInput,
                 fig: Any) -> None: ...

    def post_event(self: BlockingKeyMouseInput) -> None: ...

    def __call__(self: BlockingKeyMouseInput,
                 timeout: int = 30) -> None: ...
