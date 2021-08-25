from matplotlib import transforms as transforms
from backend_gtk3 import _BackendGTK3 as _BackendGTK3
from backend_gtk3 import Gtk as Gtk
from backend_cairo import cairo as cairo
from matplotlib import backend_gtk3 as backend_gtk3
from matplotlib import backend_agg as backend_agg
from matplotlib import backend_cairo as backend_cairo
from matplotlib import cbook as cbook
from typing import Any
from typing import ClassVar
from typing import Optional

from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.backends.backend_gtk3 import FigureCanvasGTK3
from matplotlib.backends.backend_gtk3 import FigureManagerGTK3
from matplotlib.backends.backend_gtk3 import _BackendGTK3
from matplotlib.backends.backend_gtk3agg import FigureCanvasGTK3Agg


class FigureCanvasGTK3Agg(FigureCanvasGTK3, FigureCanvasAgg):
    _bbox_queue: list[Any]

    def __init__(self: FigureCanvasGTK3Agg,
                 figure: Optional[{set_canvas}]) -> None: ...

    def on_draw_event(self: FigureCanvasGTK3Agg,
                      widget: Any,
                      ctx: Any) -> bool: ...

    def blit(self: FigureCanvasGTK3Agg,
             bbox: Optional[{x0, y1, x1, y0}] = None) -> None: ...

    def draw(self: FigureCanvasGTK3Agg) -> None: ...

    def print_png(self: FigureCanvasGTK3Agg,
                  filename: Any,
                  *args,
                  **kwargs) -> Any: ...


class FigureManagerGTK3Agg(FigureManagerGTK3):
    pass


class _BackendGTK3Cairo(_BackendGTK3):
    FigureCanvas: ClassVar[Type[FigureCanvasGTK3Agg]]
    FigureManager: ClassVar[Type[FigureManagerGTK3Agg]]
    pass