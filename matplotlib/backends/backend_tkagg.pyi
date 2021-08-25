from _backend_tk import NavigationToolbar2Tk as NavigationToolbar2Tk
from _backend_tk import FigureManagerTk as FigureManagerTk
from _backend_tk import FigureCanvasTk as FigureCanvasTk
from _backend_tk import _BackendTk as _BackendTk
from backend_agg import FigureCanvasAgg as FigureCanvasAgg
from matplotlib import _backend_tk as _backend_tk
from typing import Any
from typing import ClassVar

from matplotlib.backends._backend_tk import FigureCanvasTk
from matplotlib.backends._backend_tk import _BackendTk
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class FigureCanvasTkAgg(FigureCanvasAgg, FigureCanvasTk):
    def draw(self: FigureCanvasTkAgg) -> None: ...

    def blit(self: FigureCanvasTkAgg,
             bbox: Any = None) -> None: ...


class _BackendTkAgg(_BackendTk):
    FigureCanvas: ClassVar[Type[FigureCanvasTkAgg]]
    pass