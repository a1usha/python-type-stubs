from backend_gtk3 import _BackendGTK3 as _BackendGTK3
from backend_gtk3 import Gtk as Gtk
from matplotlib import backend_gtk3 as backend_gtk3
from matplotlib import backend_cairo as backend_cairo
from contextlib import nullcontext as nullcontext
from typing import Any
from typing import ClassVar
from typing import Optional

from matplotlib.backends.backend_cairo import FigureCanvasCairo
from matplotlib.backends.backend_cairo import RendererCairo
from matplotlib.backends.backend_gtk3 import FigureCanvasGTK3
from matplotlib.backends.backend_gtk3 import _BackendGTK3
from matplotlib.backends.backend_gtk3cairo import FigureCanvasGTK3Cairo
from matplotlib.backends.backend_gtk3cairo import RendererGTK3Cairo


class RendererGTK3Cairo(RendererCairo):
    def set_context(self: RendererGTK3Cairo,
                    ctx: Any) -> None: ...


class FigureCanvasGTK3Cairo(FigureCanvasGTK3, FigureCanvasCairo):
    _renderer: RendererGTK3Cairo

    def __init__(self: FigureCanvasGTK3Cairo,
                 figure: Optional[{set_canvas}]) -> None: ...

    def on_draw_event(self: FigureCanvasGTK3Cairo,
                      widget: Any,
                      ctx: Any) -> None: ...


class _BackendGTK3Cairo(_BackendGTK3):
    FigureCanvas: ClassVar[Type[FigureCanvasGTK3Cairo]]
    pass