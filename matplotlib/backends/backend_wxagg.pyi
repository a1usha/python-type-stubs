from backend_wx import NavigationToolbar2Wx as NavigationToolbar2WxAgg
from backend_wx import FigureFrameWx as FigureFrameWx
from backend_wx import _FigureCanvasWxBase as _FigureCanvasWxBase
from backend_wx import _BackendWx as _BackendWx
from backend_agg import FigureCanvasAgg as FigureCanvasAgg
from typing import Any
from typing import ClassVar
from typing import Optional
from typing import Union

from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.backends.backend_agg import RendererAgg
from matplotlib.backends.backend_wx import FigureFrameWx
from matplotlib.backends.backend_wx import _BackendWx
from matplotlib.backends.backend_wx import _FigureCanvasWxBase
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg
from matplotlib.backends.backend_wxagg import FigureFrameWxAgg


class FigureFrameWxAgg(FigureFrameWx):
    def get_canvas(self: FigureFrameWxAgg,
                   fig: Any) -> FigureCanvasWxAgg: ...


class FigureCanvasWxAgg(FigureCanvasAgg, _FigureCanvasWxBase):
    bitmap: Any
    _isDrawn: bool

    def draw(self: FigureCanvasWxAgg,
             drawDC: Any = None) -> None: ...

    def blit(self: FigureCanvasWxAgg,
             bbox: Optional[{x0, y1, width, height}] = None) -> None: ...


def _convert_agg_to_wx_bitmap(agg: Union[RendererAgg, Any],
                              bbox: Optional[Any]) -> Any: ...


class _BackendWxAgg(_BackendWx):
    FigureCanvas: ClassVar[Type[FigureCanvasWxAgg]]
    _frame_class: ClassVar[Type[FigureFrameWxAgg]]
    pass