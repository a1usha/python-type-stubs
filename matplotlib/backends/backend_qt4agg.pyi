from backend_qt5agg import NavigationToolbar2QT as NavigationToolbar2QT
from backend_qt5agg import FigureManagerQT as FigureManagerQT
from backend_qt5agg import FigureCanvasQTAgg as FigureCanvasQTAgg
from backend_qt5agg import _BackendQT5Agg as _BackendQT5Agg
from matplotlib import _api as _api
from matplotlib.backends.backend_qt5agg import _BackendQT5Agg


class _BackendQT4Agg(_BackendQT5Agg):
    pass