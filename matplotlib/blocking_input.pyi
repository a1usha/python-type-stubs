from typing import Any
from typing import tuple


class BlockingInput(object):
    def __init__(self: BlockingInput,
                 fig: Any,
                 eventslist: tuple = ()) -> None: ...

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
                 timeout: int = 30) -> list: ...


class BlockingMouseInput(BlockingInput):
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
                 show_clicks: bool = True) -> list: ...


class BlockingContourLabeler(BlockingMouseInput):
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
    def __init__(self: BlockingKeyMouseInput,
                 fig: Any) -> None: ...

    def post_event(self: BlockingKeyMouseInput) -> None: ...

    def __call__(self: BlockingKeyMouseInput,
                 timeout: int = 30) -> None: ...
