from matplotlib.transforms import Affine2DBase as Affine2DBase
from matplotlib.transforms import Affine2D as Affine2D
from matplotlib import _path as _path
from matplotlib.path import Path as Path
from matplotlib.mathtext import MathTextParser as MathTextParser
from matplotlib.ft2font import LOAD_NO_HINTING as LOAD_NO_HINTING
from matplotlib.font_manager import get_font as get_font
from matplotlib.font_manager import findfont as findfont
from matplotlib.dates import UTC as UTC
from matplotlib.colors import rgb2hex as rgb2hex
from matplotlib.backends.backend_mixed import MixedModeRenderer as MixedModeRenderer
from matplotlib.backend_bases import _no_output_draw as _no_output_draw
from matplotlib.backend_bases import RendererBase as RendererBase
from matplotlib.backend_bases import FigureManagerBase as FigureManagerBase
from matplotlib.backend_bases import FigureCanvasBase as FigureCanvasBase
from matplotlib.backend_bases import _check_savefig_extra_args as _check_savefig_extra_args
from matplotlib.backend_bases import _Backend as _Backend
from matplotlib import cbook as cbook
from matplotlib import _api as _api
from PIL import Image as Image
from io import TextIOWrapper as TextIOWrapper
from io import StringIO as StringIO
from io import BytesIO as BytesIO
from collections import OrderedDict as OrderedDict
from collections import OrderedDict
from io import TextIOWrapper
from typing import ClassVar
from typing import Optional
from typing import OrderedDict
from typing import Tuple
from typing import Union

from matplotlib import _api
from matplotlib.backend_bases import FigureCanvasBase
from matplotlib.backend_bases import GraphicsContextBase
from matplotlib.backend_bases import RendererBase
from matplotlib.backend_bases import _Backend
from matplotlib.backends.backend_svg import FigureCanvasSVG
from matplotlib.backends.backend_svg import RendererSVG
from matplotlib.backends.backend_svg import XMLWriter
from matplotlib.font_manager import FontProperties
from matplotlib.ft2font import FT2Font
from matplotlib.mathtext import MathTextParser
from matplotlib.path import Path
from matplotlib.text import Text
from matplotlib.transforms import Affine2D
from matplotlib.transforms import Affine2DBase
from matplotlib.transforms import CompositeAffine2D
from matplotlib.transforms import CompositeGenericTransform
from matplotlib.transforms import Transform
from object import object

_log: Logger
backend_version: str
from typing import Any

_escape_xml_comment: Pattern[str]


def escape_cdata(s: Union[str, Any]) -> str: ...


def escape_comment(s: Union[str, Any]) -> str: ...


def escape_attrib(s: Any) -> Any: ...


def short_float_fmt(x: Union[Union[float, int, complex], Any]) -> str: ...


class XMLWriter(object):
    __write: Any
    __open: int
    flush: Any
    __tags: list[Any]
    __data: list[Any]
    __indentation: str

    def __init__(self: XMLWriter,
                 file: Any) -> None: ...

    def __flush(self: XMLWriter,
                indent: bool = True) -> None: ...

    def start(self: XMLWriter,
              tag: Union[str, Any],
              attrib: dict[Any, Any] = {},
              **kwargs) -> int: ...

    def comment(self: XMLWriter,
                comment: str) -> None: ...

    def data(self: XMLWriter,
             text: str) -> None: ...

    def end(self: XMLWriter,
            tag: Union[str, Any] = None,
            indent: bool = True) -> None: ...

    def close(self: XMLWriter,
              id: Union[int, Any]) -> None: ...

    def element(self: XMLWriter,
                tag: Union[str, Any],
                text: Union[str, Any] = None,
                attrib: dict[Any, Any] = {},
                **kwargs) -> None: ...

    def flush(self: XMLWriter) -> None: ...


def generate_transform(transform_list: list[Any] = []) -> str: ...


_capstyle_d: dict[str, str]


def generate_css(attrib: dict[Any, Any] = {}) -> str: ...


class RendererSVG(RendererBase):
    _path_collection_id: int
    _fonts: OrderedDict[Any, Any]
    _groupd: dict[Any, Any]
    _n_gradients: int
    _markers: dict[Any, Any]
    _has_gouraud: bool
    _image_counter: count[int]
    basename: Any
    image_dpi: int
    _glyph_map: dict[Any, Any]
    _hatchd: OrderedDict[Any, Any]
    _start_id: int
    _clipd: OrderedDict[Any, Any]
    width: Any
    writer: XMLWriter
    height: Any

    def __init__(self: RendererSVG,
                 width: Any,
                 height: Any,
                 svgwriter: {write},
                 basename: Any = None,
                 image_dpi: int = 72,
                 *,
                 metadata: Any = None) -> None: ...

    @_api.deprecated("3.4")
    def mathtext_parser(self: RendererSVG) -> MathTextParser: ...

    def finalize(self: RendererSVG) -> None: ...

    def _write_metadata(self: RendererSVG,
                        metadata: Any) -> Any: ...

    def _write_default_style(self: RendererSVG) -> None: ...

    def _make_id(self: RendererSVG,
                 type: Union[str, Any],
                 content: Union[
                     Union[tuple[int, str], tuple[Any, Any, Any, Any], tuple[Any, str], bytes, str], Any]) -> str: ...

    def _make_flip_transform(self: RendererSVG,
                             transform: Union[Transform, Any]) -> Union[Union[{input_dims, output_dims}, {output_dims,
                                                                                                          input_dims}, CompositeAffine2D, CompositeGenericTransform, _NotImplementedType], Any]: ...

    def _get_font(self: RendererSVG,
                  prop: Union[FontProperties, Any]) -> FT2Font: ...

    def _get_hatch(self: RendererSVG,
                   gc: {get_hatch_color, get_hatch},
                   rgbFace: Any) -> Union[str, Any]: ...

    def _write_hatches(self: RendererSVG) -> None: ...

    def _get_style_dict(self: RendererSVG,
                        gc: {get_forced_alpha, get_hatch, get_alpha, get_dashes, get_linewidth},
                        rgbFace: Optional[Any]) -> dict[str, Union[str, Any]]: ...

    def _get_style(self: RendererSVG,
                   gc: Union[Union[{get_hatch_path, get_sketch_params, get_url}, GraphicsContextBase], Any],
                   rgbFace: Optional[Any]) -> str: ...

    def _get_clip(self: RendererSVG,
                  gc: Union[Union[{get_hatch_path, get_sketch_params, get_url}, {get_forced_alpha, get_hatch, get_alpha,
                                                                                 get_dashes,
                                                                                 get_linewidth}, GraphicsContextBase, {
                                      get_gid, get_url}, {get_url}], Any]) -> Union[Optional[str], Any]: ...

    def _write_clips(self: RendererSVG) -> None: ...

    def open_group(self: RendererSVG,
                   s: Any,
                   gid: Any = None) -> None: ...

    def close_group(self: RendererSVG,
                    s: Any) -> None: ...

    def option_image_nocomposite(self: RendererSVG) -> bool: ...

    def _convert_path(self: RendererSVG,
                      path: Union[Union[{should_simplify}, Path], Any],
                      transform: Union[Union[{input_dims, output_dims}, {output_dims,
                                                                         input_dims}, CompositeAffine2D, CompositeGenericTransform, _NotImplementedType, Affine2D], Any] = None,
                      clip: Any = None,
                      simplify: Union[bool, Any] = None,
                      sketch: Any = None) -> Any: ...

    def draw_path(self: RendererSVG,
                  gc: {get_hatch_path, get_sketch_params, get_url},
                  path: {should_simplify},
                  transform: Any,
                  rgbFace: Any = None) -> None: ...

    def draw_markers(self: RendererSVG,
                     gc: Any,
                     marker_path: Any,
                     marker_trans: Transform,
                     path: {iter_segments},
                     trans: Transform,
                     rgbFace: Any = None) -> None: ...

    def draw_path_collection(self: RendererSVG,
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
                             offset_position: {__eq__}) -> None: ...

    def draw_gouraud_triangle(self: RendererSVG,
                              gc: Any,
                              points: int,
                              colors: int,
                              trans: Any) -> None: ...

    def draw_gouraud_triangles(self: RendererSVG,
                               gc: Any,
                               triangles_array: Any,
                               colors_array: Any,
                               transform: Transform) -> None: ...

    def option_scale_image(self: RendererSVG) -> bool: ...

    def get_image_magnification(self: RendererSVG) -> float: ...

    def draw_image(self: RendererSVG,
                   gc: {get_gid, get_url},
                   x: Union[int, float, complex],
                   y: Union[int, float, complex],
                   im: int,
                   transform: Affine2DBase = None) -> None: ...

    def _update_glyph_map_defs(self: RendererSVG,
                               glyph_map_new: Union[
                                   Union[OrderedDict[str, Any], OrderedDict[Any, Any]], Any]) -> None: ...

    def _adjust_char_id(self: RendererSVG,
                        char_id: Union[str, Any]) -> str: ...

    def _draw_text_as_path(self: RendererSVG,
                           gc: {get_rgb, set_linewidth},
                           x: Union[float, Any],
                           y: Union[float, Any],
                           s: str,
                           prop: FontProperties,
                           angle: {__neg__},
                           ismath: bool,
                           mtext: Any = None) -> None: ...

    def _draw_text_as_text(self: RendererSVG,
                           gc: Union[{get_url}, Any],
                           x: Any,
                           y: Any,
                           s: Any,
                           prop: Any,
                           angle: Any,
                           ismath: Any,
                           mtext: Any = None) -> None: ...

    @_api.delete_parameter("3.3", "ismath")
    def draw_tex(self: RendererSVG,
                 gc: {get_rgb, set_linewidth},
                 x: Any,
                 y: Any,
                 s: Any,
                 prop: Any,
                 angle: {__neg__},
                 ismath: str = 'TeX!',
                 mtext: Any = None) -> Optional[Any]: ...

    def draw_text(self: RendererSVG,
                  gc: {get_url},
                  x: float,
                  y: float,
                  s: str,
                  prop: FontProperties,
                  angle: float,
                  ismath: bool = False,
                  mtext: Text = None) -> None: ...

    def flipy(self: RendererSVG) -> bool: ...

    def get_canvas_width_height(self: RendererSVG) -> Tuple[Any, Any]: ...

    def get_text_width_height_descent(self: RendererSVG,
                                      s: Any,
                                      prop: {get_size_in_points},
                                      ismath: {__eq__}) -> Union[
        Tuple[Any, Any, Any], Tuple[Union[float, Any], Union[float, Any], Union[float, Any]]]: ...


class FigureCanvasSVG(FigureCanvasBase):
    filetypes: ClassVar[dict[str, str]]
    fixed_dpi: ClassVar[int]

    def print_svg(self: FigureCanvasSVG,
                  filename: Any,
                  *args,
                  **kwargs) -> None: ...

    def print_svgz(self: FigureCanvasSVG,
                   filename: Any,
                   *args,
                   **kwargs) -> None: ...

    @_api.delete_parameter("3.4", "dpi")
    def _print_svg(self: FigureCanvasSVG,
                   filename: Union[str, Any],
                   fh: Union[TextIOWrapper, Any],
                   *,
                   dpi: Any = None,
                   bbox_inches_restore: Any = None,
                   metadata: Any = None) -> Optional[Any]: ...

    def get_default_filetype(self: FigureCanvasSVG) -> str: ...

    def draw(self: FigureCanvasSVG) -> None: ...


FigureManagerSVG: Type[FigureManagerBase]
svgProlog: str


class _BackendSVG(_Backend):
    FigureCanvas: ClassVar[Type[FigureCanvasSVG]]
    pass