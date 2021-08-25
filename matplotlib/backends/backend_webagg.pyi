from backend_webagg_core import TimerTornado as TimerTornado
from matplotlib import backend_webagg_core as core
from matplotlib._pylab_helpers import Gcf as Gcf
from matplotlib.backend_bases import _Backend as _Backend
from pathlib import Path as Path
from io import BytesIO as BytesIO
from contextlib import contextmanager as contextmanager
from threading import Thread
from typing import Any
from typing import ClassVar
from typing import Type

from matplotlib.backend_bases import _Backend
from matplotlib.backends.backend_webagg import ServerThread
from matplotlib.backends.backend_webagg import WebAggApplication
from matplotlib.backends.backend_webagg_core import FigureCanvasWebAggCore


class ServerThread(Thread):
    def run(self: ServerThread) -> None: ...


webagg_server_thread: ServerThread


class FigureCanvasWebAgg(FigureCanvasWebAggCore):
    pass


class WebAggApplication():
    initialized: ClassVar[bool]
    started: ClassVar[bool]
    address: Optional[Any]
    port: Optional[Any]
    initialized: bool
    started: bool
    url_prefix: str

    def __init__(self: WebAggApplication,
                 url_prefix: str = '') -> None: ...

    def initialize(cls: Type[WebAggApplication],
                   url_prefix: str = '',
                   port: Any = None,
                   address: Any = None) -> None: ...

    def start(cls: Type[WebAggApplication]) -> None: ...


def ipython_inline_display(figure: {number, canvas}) -> Any: ...


class _BackendWebAgg(_Backend):
    FigureCanvas: ClassVar[Type[FigureCanvasWebAgg]]
    FigureManager: ClassVar[Type[FigureManagerWebAgg]]

    def show() -> None: ...
