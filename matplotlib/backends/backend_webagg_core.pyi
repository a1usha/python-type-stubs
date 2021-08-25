from matplotlib.backend_bases import _Backend as _Backend
from matplotlib.backends import backend_agg as backend_agg
from matplotlib import backend_bases as backend_bases
from matplotlib import _api as _api
from PIL import Image as Image
from pathlib import Path as Path
from io import StringIO as StringIO
from io import BytesIO as BytesIO
from typing import Any
from typing import ClassVar
from typing import Optional
from typing import Type
from typing import Union

from matplotlib.backend_bases import FigureManagerBase
from matplotlib.backend_bases import NavigationToolbar2
from matplotlib.backend_bases import TimerBase
from matplotlib.backend_bases import _Backend
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.backends.backend_agg import RendererAgg
from matplotlib.backends.backend_webagg_core import FigureCanvasWebAggCore
from matplotlib.backends.backend_webagg_core import FigureManagerWebAgg
from matplotlib.backends.backend_webagg_core import NavigationToolbar2WebAgg
from matplotlib.backends.backend_webagg_core import TimerTornado

_log: Logger
_SPECIAL_KEYS_LUT: dict[Union[str, Any], Union[str, Any]]
from typing import Any


def _handle_key(key: {index, __contains__}) -> Any: ...


class TimerTornado(TimerBase):
    _timer: None

    def __init__(self: TimerTornado,
                 *args,
                 **kwargs) -> None: ...

    def _timer_start(self: TimerTornado) -> None: ...

    def _timer_stop(self: TimerTornado) -> None: ...

    def _timer_set_interval(self: TimerTornado) -> None: ...


class FigureCanvasWebAggCore(FigureCanvasAgg):
    _timer_cls: ClassVar[Type[TimerTornado]]
    supports_blit: ClassVar[bool]
    handle_button_press: ClassVar[Callable[[FigureCanvasWebAggCore, {__getitem__, get}], None]]
    handle_button_release: ClassVar[Callable[[FigureCanvasWebAggCore, {__getitem__, get}], None]]
    handle_dblclick: ClassVar[Callable[[FigureCanvasWebAggCore, {__getitem__, get}], None]]
    handle_figure_enter: ClassVar[Callable[[FigureCanvasWebAggCore, {__getitem__, get}], None]]
    handle_figure_leave: ClassVar[Callable[[FigureCanvasWebAggCore, {__getitem__, get}], None]]
    handle_motion_notify: ClassVar[Callable[[FigureCanvasWebAggCore, {__getitem__, get}], None]]
    handle_scroll: ClassVar[Callable[[FigureCanvasWebAggCore, {__getitem__, get}], None]]
    handle_key_press: ClassVar[Callable[[FigureCanvasWebAggCore, {__getitem__, get}], None]]
    handle_key_release: ClassVar[Callable[[FigureCanvasWebAggCore, {__getitem__, get}], None]]
    _force_full: bool
    _dpi_ratio: int
    _renderer: RendererAgg
    _last_buff: ndarray
    _current_image_mode: str
    _png_is_old: bool
    _lastKey: tuple[Any, Any, Union[Optional[float], Any]]

    def __init__(self: FigureCanvasWebAggCore,
                 *args,
                 **kwargs) -> None: ...

    def show(self: FigureCanvasWebAggCore) -> None: ...

    def draw(self: FigureCanvasWebAggCore) -> None: ...

    def blit(self: FigureCanvasWebAggCore,
             bbox: Any = None) -> None: ...

    def draw_idle(self: FigureCanvasWebAggCore) -> None: ...

    def set_image_mode(self: FigureCanvasWebAggCore,
                       mode: Union[str, Any]) -> None: ...

    def get_diff_image(self: FigureCanvasWebAggCore) -> bytes: ...

    def get_renderer(self: FigureCanvasWebAggCore,
                     cleared: bool = None) -> RendererAgg: ...

    def handle_event(self: FigureCanvasWebAggCore,
                     event: {__getitem__}) -> None: ...

    def handle_unknown_event(self: FigureCanvasWebAggCore,
                             event: {__getitem__}) -> None: ...

    def handle_ack(self: FigureCanvasWebAggCore,
                   event: Any) -> None: ...

    def handle_draw(self: FigureCanvasWebAggCore,
                    event: Any) -> None: ...

    def _handle_mouse(self: FigureCanvasWebAggCore,
                      event: {__getitem__, get}) -> None: ...

    def _handle_key(self: FigureCanvasWebAggCore,
                    event: {__getitem__, get}) -> None: ...

    def handle_toolbar_button(self: FigureCanvasWebAggCore,
                              event: {__getitem__}) -> None: ...

    def handle_refresh(self: FigureCanvasWebAggCore,
                       event: Any) -> None: ...

    def handle_resize(self: FigureCanvasWebAggCore,
                      event: {get}) -> None: ...

    def handle_send_image_mode(self: FigureCanvasWebAggCore,
                               event: Optional[Any]) -> None: ...

    def handle_set_dpi_ratio(self: FigureCanvasWebAggCore,
                             event: {get}) -> None: ...

    def send_event(self: FigureCanvasWebAggCore,
                   event_type: Union[str, Any],
                   **kwargs) -> None: ...


_ALLOWED_TOOL_ITEMS: set[Optional[str]]


class NavigationToolbar2WebAgg(NavigationToolbar2):
    toolitems: ClassVar[list[tuple[Any, Any, Any, Any]]]
    cursor: int
    message: str

    def __init__(self: NavigationToolbar2WebAgg,
                 canvas: {toolbar}) -> None: ...

    def set_message(self: NavigationToolbar2WebAgg,
                    message: {__ne__}) -> None: ...

    def set_cursor(self: NavigationToolbar2WebAgg,
                   cursor: {__ne__}) -> None: ...

    def draw_rubberband(self: NavigationToolbar2WebAgg,
                        event: Any,
                        x0: Any,
                        y0: Any,
                        x1: Any,
                        y1: Any) -> None: ...

    def release_zoom(self: NavigationToolbar2WebAgg,
                     event: {x, key, y}) -> None: ...

    def save_figure(self: NavigationToolbar2WebAgg,
                    *args) -> None: ...

    def pan(self: NavigationToolbar2WebAgg) -> None: ...

    def zoom(self: NavigationToolbar2WebAgg) -> None: ...

    def set_history_buttons(self: NavigationToolbar2WebAgg) -> None: ...


class FigureManagerWebAgg(FigureManagerBase):
    ToolbarCls: ClassVar[Type[NavigationToolbar2WebAgg]]
    toolbar: NavigationToolbar2WebAgg
    web_sockets: set[Any]

    def __init__(self: FigureManagerWebAgg,
                 canvas: {manager, figure},
                 num: Any) -> None: ...

    def show(self: FigureManagerWebAgg) -> None: ...

    def _get_toolbar(self: FigureManagerWebAgg,
                     canvas: Union[{manager, figure}, Any]) -> NavigationToolbar2WebAgg: ...

    def resize(self: FigureManagerWebAgg,
               w: {__truediv__},
               h: {__truediv__},
               forward: bool = True) -> None: ...

    def set_window_title(self: FigureManagerWebAgg,
                         title: Any) -> None: ...

    def add_web_socket(self: FigureManagerWebAgg,
                       web_socket: Any) -> None: ...

    def remove_web_socket(self: FigureManagerWebAgg,
                          web_socket: Any) -> None: ...

    def handle_json(self: FigureManagerWebAgg,
                    content: Any) -> None: ...

    def refresh_all(self: FigureManagerWebAgg) -> None: ...

    def get_javascript(cls: Type[FigureManagerWebAgg],
                       stream: Any = None) -> str: ...

    def get_static_file_path(cls: Type[FigureManagerWebAgg]) -> str: ...

    def _send_event(self: FigureManagerWebAgg,
                    event_type: Union[str, Any],
                    **kwargs) -> None: ...


class _BackendWebAggCoreAgg(_Backend):
    FigureCanvas: ClassVar[Type[FigureCanvasWebAggCore]]
    FigureManager: ClassVar[Type[FigureManagerWebAgg]]
    pass