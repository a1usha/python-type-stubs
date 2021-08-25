from backend_qt5 import exception_handler as exception_handler
from backend_qt5 import SubplotToolQt as SubplotToolQt
from backend_qt5 import NavigationToolbar2QT as NavigationToolbar2QT
from backend_qt5 import FigureManagerQT as FigureManagerQT
from backend_qt5 import FigureCanvasQT as FigureCanvasQT
from backend_qt5 import MainWindow as MainWindow
from backend_qt5 import TimerQT as TimerQT
from backend_qt5 import _BackendQT5 as _BackendQT5
from backend_qt5 import _create_qApp as _create_qApp
from backend_qt5 import cursord as cursord
from backend_qt5 import MODIFIER_KEYS as MODIFIER_KEYS
from backend_qt5 import SHIFT as SHIFT
from backend_qt5 import CTRL as CTRL
from backend_qt5 import ALT as ALT
from backend_qt5 import SUPER as SUPER
from backend_qt5 import SPECIAL_KEYS as SPECIAL_KEYS
from backend_qt5 import backend_version as backend_version
from matplotlib import _api as _api
from matplotlib.backends.backend_qt5 import _BackendQT5


class _BackendQT4(_BackendQT5):
    pass