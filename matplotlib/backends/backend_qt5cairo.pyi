from qt_compat import _setDevicePixelRatio as _setDevicePixelRatio
from qt_compat import QT_API as QT_API
from backend_qt5 import FigureCanvasQT as FigureCanvasQT
from backend_qt5 import _BackendQT5 as _BackendQT5
from backend_qt5 import QtGui as QtGui
from backend_qt5 import QtCore as QtCore
from backend_cairo import RendererCairo as RendererCairo
from backend_cairo import FigureCanvasCairo as FigureCanvasCairo
from backend_cairo import cairo as cairo
from typing import ClassVar
from typing import Optional

from matplotlib.backends.backend_cairo import FigureCanvasCairo
from matplotlib.backends.backend_qt5 import FigureCanvasQT
from matplotlib.backends.backend_qt5 import _BackendQT5
from matplotlib.backends.backend_qt5cairo import FigureCanvasQTCairo


class FigureCanvasQTCairo(FigureCanvasQT, FigureCanvasCairo):
    _renderer: RendererCairo

    def __init__(self: FigureCanvasQTCairo,
                 figure: Optional[{set_canvas}] = None) -> None: ...

    def draw(self: FigureCanvasQTCairo) -> None: ...

    def paintEvent(self: FigureCanvasQTCairo,
                   event: {rect}) -> None: ...


class _BackendQT5Cairo(_BackendQT5):
    FigureCanvas: ClassVar[Type[FigureCanvasQTCairo]]
    pass