from matplotlib.backends.backend_webagg_core import TimerTornado as TimerTornado
from matplotlib.backends.backend_webagg_core import NavigationToolbar2WebAgg as NavigationToolbar2WebAgg
from matplotlib.backends.backend_webagg_core import FigureManagerWebAgg as FigureManagerWebAgg
from matplotlib.backends.backend_webagg_core import FigureCanvasWebAggCore as FigureCanvasWebAggCore
from matplotlib.backend_bases import NavigationToolbar2 as NavigationToolbar2
from matplotlib.backend_bases import _Backend as _Backend
from matplotlib._pylab_helpers import Gcf as Gcf
from matplotlib import is_interactive as is_interactive
from IPython.kernel.comm import Comm as Comm
from ipykernel.comm import Comm as Comm
from IPython.display import HTML as HTML
from IPython.display import Javascript as Javascript
from IPython.display import display as display
from base64 import b64encode as b64encode
from typing import Any
from typing import ClassVar
from typing import Type

from matplotlib.backend_bases import _Backend
from matplotlib.backends.backend_nbagg import CommSocket
from matplotlib.backends.backend_nbagg import FigureManagerNbAgg
from matplotlib.backends.backend_webagg_core import FigureCanvasWebAggCore
from matplotlib.backends.backend_webagg_core import FigureManagerWebAgg
from matplotlib.backends.backend_webagg_core import NavigationToolbar2WebAgg
from object import object

_FONT_AWESOME_CLASSES: dict[Optional[str], Optional[str]]


def connection_info() -> str: ...


class NavigationIPy(NavigationToolbar2WebAgg):
    toolitems: ClassVar[list[tuple[Any, Any, Optional[str], Any]]]
    pass


class FigureManagerNbAgg(FigureManagerWebAgg):
    ToolbarCls: ClassVar[Type[NavigationIPy]]
    _shown: bool
    web_sockets: set

    def __init__(self: FigureManagerNbAgg,
                 canvas: {manager, figure},
                 num: Any) -> None: ...

    def display_js(self: FigureManagerNbAgg) -> None: ...

    def show(self: FigureManagerNbAgg) -> None: ...

    def reshow(self: FigureManagerNbAgg) -> None: ...

    def connected(self: FigureManagerNbAgg) -> bool: ...

    def get_javascript(cls: Type[FigureManagerNbAgg],
                       stream: Any = None) -> str: ...

    def _create_comm(self: FigureManagerNbAgg) -> CommSocket: ...

    def destroy(self: FigureManagerNbAgg) -> None: ...

    def clearup_closed(self: FigureManagerNbAgg) -> None: ...

    def remove_comm(self: FigureManagerNbAgg,
                    comm_id: Any) -> None: ...


class FigureCanvasNbAgg(FigureCanvasWebAggCore):
    pass


class CommSocket(object):
    comm: Any
    manager: Any
    _ext_close: bool
    supports_binary: None
    uuid: str

    def __init__(self: CommSocket,
                 manager: Any) -> Any: ...

    def is_open(self: CommSocket) -> bool: ...

    def on_close(self: CommSocket) -> None: ...

    def send_json(self: CommSocket,
                  content: Any) -> None: ...

    def send_binary(self: CommSocket,
                    blob: Any) -> None: ...

    def on_message(self: CommSocket,
                   message: Any) -> None: ...


class _BackendNbAgg(_Backend):
    FigureCanvas: ClassVar[Type[FigureCanvasNbAgg]]
    FigureManager: ClassVar[Type[FigureManagerNbAgg]]

    def new_figure_manager_given_figure(num: Any,
                                        figure: Any) -> FigureManagerNbAgg: ...

    def show(block: Any = None) -> None: ...
