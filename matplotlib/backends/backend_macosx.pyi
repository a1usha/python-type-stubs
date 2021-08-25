from matplotlib.widgets import SubplotTool as SubplotTool
from matplotlib.figure import Figure as Figure
from matplotlib.backend_bases import TimerBase as TimerBase
from matplotlib.backend_bases import NavigationToolbar2 as NavigationToolbar2
from matplotlib.backend_bases import FigureManagerBase as FigureManagerBase
from matplotlib.backend_bases import FigureCanvasBase as FigureCanvasBase
from matplotlib.backend_bases import _Backend as _Backend
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvasAgg
from matplotlib.backends import _macosx as _macosx
from matplotlib._pylab_helpers import Gcf as Gcf
from matplotlib import cbook as cbook
from typing import Any
from typing import ClassVar

from matplotlib.backend_bases import FigureManagerBase
from matplotlib.backend_bases import TimerBase
from matplotlib.backend_bases import _Backend
from matplotlib.backends._macosx import FigureCanvas
from matplotlib.backends._macosx import FigureManager
from matplotlib.backends._macosx import NavigationToolbar2
from matplotlib.backends._macosx import Timer
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.backends.backend_agg import RendererAgg
from matplotlib.backends.backend_macosx import FigureCanvasMac
from matplotlib.backends.backend_macosx import FigureManagerMac
from matplotlib.backends.backend_macosx import NavigationToolbar2Mac


class TimerMac(Timer, TimerBase):
    pass


class FigureCanvasMac(FigureCanvas, FigureCanvasAgg):
    required_interactive_framework: ClassVar[str]
    _timer_cls: ClassVar[Type[TimerMac]]
    _dpi_ratio: float

    def __init__(self: FigureCanvasMac,
                 figure: Any) -> None: ...

    def _set_device_scale(self: FigureCanvasMac,
                          value: Any) -> None: ...

    def _draw(self: FigureCanvasMac) -> RendererAgg: ...

    def draw(self: FigureCanvasMac) -> None: ...

    def blit(self: FigureCanvasMac,
             bbox: Any = None) -> None: ...

    def resize(self: FigureCanvasMac,
               width: {__mul__},
               height: {__mul__}) -> None: ...


class FigureManagerMac(FigureManager, FigureManagerBase):
    toolbar: None

    def __init__(self: FigureManagerMac,
                 canvas: {manager, figure},
                 num: Any) -> None: ...

    def close(self: FigureManagerMac) -> None: ...


class NavigationToolbar2Mac(NavigationToolbar2, NavigationToolbar2):
    canvas: {toolbar}

    def __init__(self: NavigationToolbar2Mac,
                 canvas: {toolbar}) -> None: ...

    def draw_rubberband(self: NavigationToolbar2Mac,
                        event: Any,
                        x0: Any,
                        y0: Any,
                        x1: Any,
                        y1: Any) -> None: ...

    def release_zoom(self: NavigationToolbar2Mac,
                     event: {x, key, y}) -> None: ...

    def set_cursor(self: NavigationToolbar2Mac,
                   cursor: Any) -> None: ...

    def save_figure(self: NavigationToolbar2Mac,
                    *args) -> None: ...

    def prepare_configure_subplots(self: NavigationToolbar2Mac) -> FigureCanvasMac: ...

    def set_message(self: NavigationToolbar2Mac,
                    message: {encode}) -> None: ...


class _BackendMac(_Backend):
    FigureCanvas: ClassVar[Type[FigureCanvasMac]]
    FigureManager: ClassVar[Type[FigureManagerMac]]

    def mainloop() -> None: ...
