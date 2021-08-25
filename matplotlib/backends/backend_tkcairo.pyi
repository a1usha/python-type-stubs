from _backend_tk import FigureCanvasTk as FigureCanvasTk
from _backend_tk import _BackendTk as _BackendTk
from backend_cairo import RendererCairo as RendererCairo
from backend_cairo import FigureCanvasCairo as FigureCanvasCairo
from backend_cairo import cairo as cairo
from matplotlib import _backend_tk as _backend_tk
from typing import ClassVar

from matplotlib.backends._backend_tk import FigureCanvasTk
from matplotlib.backends._backend_tk import _BackendTk
from matplotlib.backends.backend_cairo import FigureCanvasCairo
from matplotlib.backends.backend_tkcairo import FigureCanvasTkCairo


class FigureCanvasTkCairo(FigureCanvasCairo, FigureCanvasTk):
    _renderer: RendererCairo

    def __init__(self: FigureCanvasTkCairo,
                 *args,
                 **kwargs) -> None: ...

    def draw(self: FigureCanvasTkCairo) -> None: ...


class _BackendTkCairo(_BackendTk):
    FigureCanvas: ClassVar[Type[FigureCanvasTkCairo]]
    pass