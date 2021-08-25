from qt_compat import _setDevicePixelRatio as _setDevicePixelRatio
from qt_compat import QT_API as QT_API
from backend_qt5 import backend_version as backend_version
from backend_qt5 import NavigationToolbar2QT as NavigationToolbar2QT
from backend_qt5 import FigureManagerQT as FigureManagerQT
from backend_qt5 import FigureCanvasQT as FigureCanvasQT
from backend_qt5 import _BackendQT5 as _BackendQT5
from backend_qt5 import QtWidgets as QtWidgets
from backend_qt5 import QtGui as QtGui
from backend_qt5 import QtCore as QtCore
from backend_agg import FigureCanvasAgg as FigureCanvasAgg
from matplotlib import cbook as cbook
from matplotlib.transforms import Bbox as Bbox
from typing import ClassVar
from typing import Optional

from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.backends.backend_qt5 import FigureCanvasQT
from matplotlib.backends.backend_qt5 import _BackendQT5
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg


class FigureCanvasQTAgg(FigureCanvasAgg, FigureCanvasQT):
    def __init__(self: FigureCanvasQTAgg,
                 figure: Optional[{set_canvas}] = None) -> None: ...

    def paintEvent(self: FigureCanvasQTAgg,
                   event: {rect}) -> None: ...

    def print_figure(self: FigureCanvasQTAgg,
                     *args,
                     **kwargs) -> None: ...


class _BackendQT5Agg(_BackendQT5):
    FigureCanvas: ClassVar[Type[FigureCanvasQTAgg]]
    pass