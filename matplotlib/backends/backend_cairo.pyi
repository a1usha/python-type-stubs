from matplotlib.transforms import Affine2D as Affine2D
from matplotlib.path import Path as Path
from matplotlib.mathtext import MathTextParser as MathTextParser
from matplotlib.font_manager import ttfFontProperty as ttfFontProperty
from matplotlib.backend_bases import RendererBase as RendererBase
from matplotlib.backend_bases import GraphicsContextBase as GraphicsContextBase
from matplotlib.backend_bases import FigureManagerBase as FigureManagerBase
from matplotlib.backend_bases import FigureCanvasBase as FigureCanvasBase
from matplotlib.backend_bases import _check_savefig_extra_args as _check_savefig_extra_args
from matplotlib.backend_bases import _Backend as _Backend
from matplotlib import font_manager as font_manager
from matplotlib import cbook as cbook
from matplotlib import _api as _api
from typing import Any
from typing import ClassVar
from typing import Iterable
from typing import Optional
from typing import Tuple
from typing import Union

from matplotlib.backend_bases import FigureCanvasBase
from matplotlib.backend_bases import GraphicsContextBase
from matplotlib.backend_bases import RendererBase
from matplotlib.backend_bases import _Backend
from matplotlib.backends.backend_cairo import FigureCanvasCairo
from matplotlib.backends.backend_cairo import GraphicsContextCairo
from matplotlib.backends.backend_cairo import RendererCairo
from matplotlib.backends.backend_cairo import _CairoRegion
from matplotlib.font_manager import FontEntry
from matplotlib.font_manager import FontProperties
from matplotlib.text import Text
from matplotlib.transforms import CompositeAffine2D
from matplotlib.transforms import CompositeGenericTransform
from matplotlib.transforms import Transform
from object import object

backend_version: Any


def _append_path(ctx: Any,
                 path: {iter_segments},
                 transform: Union[Union[{input_dims, output_dims}, {output_dims,
                                                                    input_dims}, CompositeAffine2D, CompositeGenericTransform, _NotImplementedType], Any],
                 clip: Optional[Any] = None) -> None: ...


_f_weights: dict[Union[Union[int, str], Any], Any]

_f_angles: dict[str, Any]


def _cairo_font_args_from_font_prop(prop: Union[Union[FontProperties, FontEntry, {get_size_in_points}], Any]) -> Tuple[
    Any, Any, Any]: ...


class RendererCairo(RendererBase):
    fontweights: ClassVar[Union[_deprecated_property, Any]]
    fontangles: ClassVar[Union[_deprecated_property, Any]]
    mathtext_parser: ClassVar[Union[_deprecated_property, Any]]
    text_ctx: Any
    width: Union[int, Any]
    dpi: Any
    gc: GraphicsContextCairo
    height: Union[int, Any]

    def __init__(self: RendererCairo,
                 dpi: Any) -> None: ...

    def set_ctx_from_surface(self: RendererCairo,
                             surface: Any) -> None: ...

    def set_width_height(self: RendererCairo,
                         width: Union[int, Any],
                         height: Union[int, Any]) -> None: ...

    def _fill_and_stroke(self: RendererCairo,
                         ctx: {stroke},
                         fill_c: Optional[Any],
                         alpha: Any,
                         alpha_overrides: Any) -> None: ...

    def draw_path(self: RendererCairo,
                  gc: {ctx, get_hatch, get_alpha, get_forced_alpha},
                  path: {iter_segments},
                  transform: Any,
                  rgbFace: Any = None) -> None: ...

    def draw_markers(self: RendererCairo,
                     gc: {ctx},
                     marker_path: {iter_segments},
                     marker_trans: Transform,
                     path: {iter_segments},
                     transform: Any,
                     rgbFace: Any = None) -> None: ...

    def draw_image(self: RendererCairo,
                   gc: {ctx},
                   x: Union[int, float, complex],
                   y: Union[int, float, complex],
                   im: int) -> None: ...

    def draw_text(self: RendererCairo,
                  gc: Any,
                  x: float,
                  y: float,
                  s: str,
                  prop: FontProperties,
                  angle: float,
                  ismath: bool = False,
                  mtext: Text = None) -> None: ...

    def _draw_mathtext(self: RendererCairo,
                       gc: {ctx},
                       x: Any,
                       y: Any,
                       s: Any,
                       prop: Any,
                       angle: Any) -> None: ...

    def get_canvas_width_height(self: RendererCairo) -> Tuple[Union[int, Any], Union[int, Any]]: ...

    def get_text_width_height_descent(self: RendererCairo,
                                      s: Any,
                                      prop: {get_size_in_points},
                                      ismath: {__eq__}) -> Union[Tuple[Any, Any, Any], Any]: ...

    def new_gc(self: RendererCairo) -> GraphicsContextCairo: ...

    def points_to_pixels(self: RendererCairo,
                         points: Union[Union[float, Iterable, int], Any]) -> Union[float, Any]: ...


class GraphicsContextCairo(GraphicsContextBase):
    _joind: ClassVar[dict[str, Any]]
    _capd: ClassVar[dict[str, Any]]
    _capstyle: Any
    renderer: Any
    _linewidth: float
    _dashes: tuple[Any, Any]
    _joinstyle: Any

    def __init__(self: GraphicsContextCairo,
                 renderer: Any) -> None: ...

    def restore(self: GraphicsContextCairo) -> None: ...

    def set_alpha(self: GraphicsContextCairo,
                  alpha: Any) -> None: ...

    def set_antialiased(self: GraphicsContextCairo,
                        b: Any) -> None: ...

    def set_capstyle(self: GraphicsContextCairo,
                     cs: Any) -> None: ...

    def set_clip_rectangle(self: GraphicsContextCairo,
                           rectangle: {bounds}) -> None: ...

    def set_clip_path(self: GraphicsContextCairo,
                      path: {get_transformed_path_and_affine}) -> None: ...

    def set_dashes(self: GraphicsContextCairo,
                   offset: Any,
                   dashes: Any) -> None: ...

    def set_foreground(self: GraphicsContextCairo,
                       fg: Any,
                       isRGBA: bool = None) -> None: ...

    def get_rgb(self: GraphicsContextCairo) -> Any: ...

    def set_joinstyle(self: GraphicsContextCairo,
                      js: Any) -> None: ...

    def set_linewidth(self: GraphicsContextCairo,
                      w: Any) -> None: ...


class _CairoRegion(object):
    _slices: Any
    _data: Any

    def __init__(self: _CairoRegion,
                 slices: Any,
                 data: Any) -> None: ...


class FigureCanvasCairo(FigureCanvasBase):
    print_raw: ClassVar[Union[partial[Any], Callable[[tuple[Any, ...], dict[str, Any]], Any]]]

    def copy_from_bbox(self: FigureCanvasCairo,
                       bbox: {x0, x1, y1, y0}) -> _CairoRegion: ...

    def restore_region(self: FigureCanvasCairo,
                       region: {_slices, _data}) -> Any: ...

    def print_png(self: FigureCanvasCairo,
                  fobj: Any) -> Optional[Any]: ...

    def print_rgba(self: FigureCanvasCairo,
                   fobj: {write}) -> Optional[Any]: ...

    def _get_printed_image_surface(self: FigureCanvasCairo) -> Any: ...

    def print_pdf(self: FigureCanvasCairo,
                  fobj: Any,
                  *args,
                  **kwargs) -> Any: ...

    def print_ps(self: FigureCanvasCairo,
                 fobj: Any,
                 *args,
                 **kwargs) -> Any: ...

    def print_svg(self: FigureCanvasCairo,
                  fobj: Any,
                  *args,
                  **kwargs) -> Any: ...

    def print_svgz(self: FigureCanvasCairo,
                   fobj: Any,
                   *args,
                   **kwargs) -> Any: ...

    def _save(self: FigureCanvasCairo,
              fo: Any,
              fmt: Union[str, Any],
              *,
              orientation: str = 'portrait') -> Any: ...


class _BackendCairo(_Backend):
    FigureCanvas: ClassVar[Type[FigureCanvasCairo]]
    FigureManager: ClassVar[Type[FigureManagerBase]]
    pass