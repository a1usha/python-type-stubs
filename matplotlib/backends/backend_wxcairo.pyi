from backend_wx import NavigationToolbar2Wx as NavigationToolbar2WxCairo
from backend_wx import FigureFrameWx as FigureFrameWx
from backend_wx import _FigureCanvasWxBase as _FigureCanvasWxBase
from backend_wx import _BackendWx as _BackendWx
from backend_cairo import RendererCairo as RendererCairo
from backend_cairo import FigureCanvasCairo as FigureCanvasCairo
from backend_cairo import cairo as cairo
from typing import Any
from typing import ClassVar
from typing import Optional

from matplotlib.backends.backend_cairo import FigureCanvasCairo
from matplotlib.backends.backend_wx import FigureFrameWx
from matplotlib.backends.backend_wx import _BackendWx
from matplotlib.backends.backend_wx import _FigureCanvasWxBase
from matplotlib.backends.backend_wxcairo import FigureCanvasWxCairo
from matplotlib.backends.backend_wxcairo import FigureFrameWxCairo


class FigureFrameWxCairo(FigureFrameWx):
    def get_canvas(self: FigureFrameWxCairo,
                   fig: Any) -> FigureCanvasWxCairo: ...


class FigureCanvasWxCairo(_FigureCanvasWxBase, FigureCanvasCairo):
    _renderer: RendererCairo
    bitmap: Any
    _isDrawn: bool

    def __init__(self: FigureCanvasWxCairo,
                 parent: Any,
                 id: Any,
                 figure: Optional[{set_canvas}]) -> None: ...

    def draw(self: FigureCanvasWxCairo,
             drawDC: Any = None) -> None: ...


class _BackendWxCairo(_BackendWx):
    FigureCanvas: ClassVar[Type[FigureCanvasWxCairo]]
    _frame_class: ClassVar[Type[FigureFrameWxCairo]]
    pass