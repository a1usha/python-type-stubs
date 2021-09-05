from matplotlib.backends._backend_agg import RendererAgg as _RendererAgg
from matplotlib.transforms import BboxBase as BboxBase
from matplotlib.transforms import Bbox as Bbox
from matplotlib.path import Path as Path
from matplotlib.mathtext import MathTextParser as MathTextParser
from matplotlib.ft2font import LOAD_NO_AUTOHINT as LOAD_NO_AUTOHINT
from matplotlib.ft2font import LOAD_DEFAULT as LOAD_DEFAULT
from matplotlib.ft2font import LOAD_NO_HINTING as LOAD_NO_HINTING
from matplotlib.ft2font import LOAD_FORCE_AUTOHINT as LOAD_FORCE_AUTOHINT
from matplotlib.font_manager import get_font as get_font
from matplotlib.font_manager import findfont as findfont
from matplotlib.backend_bases import RendererBase as RendererBase
from matplotlib.backend_bases import FigureManagerBase as FigureManagerBase
from matplotlib.backend_bases import FigureCanvasBase as FigureCanvasBase
from matplotlib.backend_bases import _check_savefig_extra_args as _check_savefig_extra_args
from matplotlib.backend_bases import _Backend as _Backend
from matplotlib import colors as mcolors
from matplotlib import cbook as cbook
from matplotlib import _api as _api
from PIL import Image as Image
from math import sin as sin
from math import cos as cos
from math import radians as radians
from contextlib import nullcontext as nullcontext
from typing import Any
from typing import ClassVar
from typing import Iterable
from typing import Optional
from typing import Tuple
from typing import Union

from matplotlib import _api
from matplotlib.backend_bases import FigureCanvasBase
from matplotlib.backend_bases import RendererBase
from matplotlib.backend_bases import _Backend
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.backends.backend_agg import RendererAgg
from matplotlib.font_manager import FontProperties
from matplotlib.text import Text

backend_version: str


def get_hinting_flag() -> Any: ...


class RendererAgg(RendererBase):
    lock: ClassVar[Union[_RLock, _RLock]]
    draw_quad_mesh: Any
    draw_gouraud_triangle: Any
    _renderer: Any
    _filter_renderers: list[Any]
    bbox: Bbox
    draw_markers: Any
    draw_gouraud_triangles: Any
    width: Any
    mathtext_parser: MathTextParser
    draw_image: Any
    copy_from_bbox: Any
    dpi: Any
    height: Any

    def __init__(self: RendererAgg,
                 width: Any,
                 height: Any,
                 dpi: Any) -> None: ...

    def __getstate__(self: RendererAgg) -> dict[str, Any]: ...

    def __setstate__(self: RendererAgg,
                     state: {__getitem__}) -> None: ...

    def _update_methods(self: RendererAgg) -> None: ...

    @_api.deprecated("3.4")
    def get_content_extents(self: RendererAgg) -> Union[Tuple[Any, Any, Any, Any], Any]: ...

    @_api.deprecated("3.4")
    def tostring_rgba_minimized(self: RendererAgg) -> Union[Tuple[Any, Union[Tuple[Any, Any, Any, Any], Any]], Any]: ...

    def draw_path(self: RendererAgg,
                  gc: {get_hatch},
                  path: {vertices, should_simplify},
                  transform: Any,
                  rgbFace: Any = None) -> Any: ...

    def draw_path_collection(self: RendererAgg,
                             gc: {_alpha, _forced_alpha, _antialiased, _capstyle, _cliprect, _clippath, _dashes,
                                  _joinstyle, _linestyle, _linewidth, _rgb, _hatch, _hatch_color, _hatch_linewidth,
                                  _url, _gid, _snap, _sketch},
                             master_transform: Any,
                             paths: {__len__, __getitem__},
                             all_transforms: {__len__},
                             offsets: {__len__},
                             offsetTrans: Any,
                             facecolors: {__len__},
                             edgecolors: {__len__},
                             linewidths: {__len__},
                             linestyles: {__len__},
                             antialiaseds: {__len__, __getitem__},
                             urls: {__len__},
                             offset_position: {__eq__}) -> Any: ...

    def draw_mathtext(self: RendererAgg,
                      gc: Any,
                      x: Any,
                      y: Any,
                      s: Any,
                      prop: Any,
                      angle: Any) -> None: ...

    def draw_text(self: RendererAgg,
                  gc: Any,
                  x: float,
                  y: float,
                  s: str,
                  prop: FontProperties,
                  angle: float,
                  ismath: bool = False,
                  mtext: Text = None) -> None: ...

    def get_text_width_height_descent(self: RendererAgg,
                                      s: Any,
                                      prop: {get_size_in_points},
                                      ismath: {__eq__}) -> Tuple[Any, Any, Any]: ...

    def draw_tex(self: RendererAgg,
                 gc: {get_rgb, set_linewidth},
                 x: Any,
                 y: Any,
                 s: Any,
                 prop: {get_size_in_points},
                 angle: Any,
                 *,
                 mtext: Any = None) -> None: ...

    def get_canvas_width_height(self: RendererAgg) -> Tuple[Any, Any]: ...

    def _get_agg_font(self: RendererAgg,
                      prop: Union[Union[FontProperties, {get_size_in_points}], Any]) -> Any: ...

    def points_to_pixels(self: RendererAgg,
                         points: Union[Union[float, Iterable, int], Any]) -> Union[float, Any]: ...

    def buffer_rgba(self: RendererAgg) -> memoryview: ...

    def tostring_argb(self: RendererAgg) -> Any: ...

    def tostring_rgb(self: RendererAgg) -> Any: ...

    def clear(self: RendererAgg) -> None: ...

    def option_image_nocomposite(self: RendererAgg) -> bool: ...

    def option_scale_image(self: RendererAgg) -> bool: ...

    def restore_region(self: RendererAgg,
                       region: Any,
                       bbox: Any = None,
                       xy: Any = None) -> None: ...

    def start_filter(self: RendererAgg) -> None: ...

    def stop_filter(self: RendererAgg,
                    post_processing: Any) -> None: ...


class FigureCanvasAgg(FigureCanvasBase):
    print_rgba: ClassVar[Union[partial[Any], Callable[[tuple[Any, ...], dict[str, Any]], Any]]]
    print_jpeg: ClassVar[
        Callable[[FigureCanvasAgg, Any, tuple[Any, ...], Optional[{setdefault}], dict[str, Any]], Optional[Any]]]
    print_tiff: ClassVar[Union[partial[Any], Callable[[tuple[Any, ...], dict[str, Any]], Any]]]
    renderer: RendererAgg
    _lastKey: tuple[Any, Any, Union[Optional[float], Any]]

    def copy_from_bbox(self: FigureCanvasAgg,
                       bbox: Any) -> Any: ...

    def restore_region(self: FigureCanvasAgg,
                       region: Any,
                       bbox: Any = None,
                       xy: Any = None) -> None: ...

    def draw(self: FigureCanvasAgg) -> None: ...

    def get_renderer(self: FigureCanvasAgg,
                     cleared: bool = False) -> RendererAgg: ...

    def tostring_rgb(self: FigureCanvasAgg) -> Any: ...

    def tostring_argb(self: FigureCanvasAgg) -> Any: ...

    def buffer_rgba(self: FigureCanvasAgg) -> memoryview: ...

    def print_raw(self: FigureCanvasAgg,
                  filename_or_obj: Any,
                  *args) -> Optional[Any]: ...

    def print_png(self: FigureCanvasAgg,
                  filename_or_obj: Any,
                  metadata: Optional[dict] = None,
                  pil_kwargs: Optional[dict] = None,
                  *args) -> Optional[Any]: ...

    def print_to_buffer(self: FigureCanvasAgg) -> Tuple[bytes, Tuple[int, int]]: ...

    @_api.delete_parameter("3.3", "quality",
                           alternative="pil_kwargs={'quality': ...}")
    @_api.delete_parameter("3.3", "optimize",
                           alternative="pil_kwargs={'optimize': ...}")
    @_api.delete_parameter("3.3", "progressive",
                           alternative="pil_kwargs={'progressive': ...}")
    def print_jpg(self: FigureCanvasAgg,
                  filename_or_obj: Any,
                  pil_kwargs: Optional[{setdefault}] = None,
                  *args,
                  **kwargs) -> Optional[Any]: ...

    def print_tif(self: FigureCanvasAgg,
                  filename_or_obj: Any,
                  *,
                  pil_kwargs: Optional[{setdefault}] = None) -> Optional[Any]: ...


class _BackendAgg(_Backend):
    FigureCanvas: ClassVar[Type[FigureCanvasAgg]]
    FigureManager: ClassVar[Type[FigureManagerBase]]
    pass