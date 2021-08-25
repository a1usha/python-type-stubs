from matplotlib.figure import Figure as Figure
from matplotlib.backend_bases import RendererBase as RendererBase
from matplotlib.backend_bases import GraphicsContextBase as GraphicsContextBase
from matplotlib.backend_bases import FigureManagerBase as FigureManagerBase
from matplotlib.backend_bases import FigureCanvasBase as FigureCanvasBase
from matplotlib._pylab_helpers import Gcf as Gcf
from typing import Any
from typing import ClassVar
from typing import Iterable
from typing import Tuple
from typing import Type
from typing import Union

from matplotlib.backend_bases import FigureCanvasBase
from matplotlib.backend_bases import FigureManagerBase
from matplotlib.backend_bases import GraphicsContextBase
from matplotlib.backend_bases import RendererBase
from matplotlib.backends.backend_template import FigureCanvasTemplate
from matplotlib.backends.backend_template import FigureManagerTemplate
from matplotlib.backends.backend_template import GraphicsContextTemplate
from matplotlib.backends.backend_template import RendererTemplate
from matplotlib.figure import Figure
from matplotlib.font_manager import FontProperties
from matplotlib.text import Text
from numpy.core._multiarray_umath import ndarray


class RendererTemplate(RendererBase):
    dpi: Any

    def __init__(self: RendererTemplate,
                 dpi: Any) -> None: ...

    def draw_path(self: RendererTemplate,
                  gc: Any,
                  path: Any,
                  transform: Any,
                  rgbFace: Any = None) -> None: ...

    def draw_image(self: RendererTemplate,
                   gc: Any,
                   x: Union[int, float, complex],
                   y: Union[int, float, complex],
                   im: int) -> None: ...

    def draw_text(self: RendererTemplate,
                  gc: Any,
                  x: float,
                  y: float,
                  s: str,
                  prop: FontProperties,
                  angle: float,
                  ismath: bool = False,
                  mtext: Text = None) -> None: ...

    def flipy(self: RendererTemplate) -> bool: ...

    def get_canvas_width_height(self: RendererTemplate) -> Tuple[int, int]: ...

    def get_text_width_height_descent(self: RendererTemplate,
                                      s: Any,
                                      prop: {get_size_in_points},
                                      ismath: {__eq__}) -> Tuple[int, int, int]: ...

    def new_gc(self: RendererTemplate) -> GraphicsContextTemplate: ...

    def points_to_pixels(self: RendererTemplate,
                         points: Union[float, ndarray, Iterable, int]) -> Union[float, ndarray, Iterable, int]: ...


class GraphicsContextTemplate(GraphicsContextBase):
    pass


def draw_if_interactive() -> None: ...


def show(*,
         block: Any = None) -> None: ...


def new_figure_manager(*args,
                       num: Any,
                       FigureClass: Type[Figure] = Figure,
                       **kwargs) -> FigureManagerTemplate: ...


def new_figure_manager_given_figure(num: Any,
                                    figure: Union[Figure, Any]) -> FigureManagerTemplate: ...


class FigureCanvasTemplate(FigureCanvasBase):
    filetypes: ClassVar[dict[str, str]]

    def draw(self: FigureCanvasTemplate) -> None: ...

    def print_foo(self: FigureCanvasTemplate,
                  filename: Any,
                  *args,
                  **kwargs) -> None: ...

    def get_default_filetype(self: FigureCanvasTemplate) -> str: ...


FigureCanvas: Type[FigureCanvasTemplate]

FigureManager: Type[FigureManagerTemplate]


class FigureManagerTemplate(FigureManagerBase):
    pass