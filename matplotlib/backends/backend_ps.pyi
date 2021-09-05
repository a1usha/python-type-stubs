from matplotlib import _backend_pdf_ps as _backend_pdf_ps
from matplotlib.backends.backend_mixed import MixedModeRenderer as MixedModeRenderer
from matplotlib.transforms import Affine2D as Affine2D
from matplotlib.texmanager import TexManager as TexManager
from matplotlib.path import Path as Path
from matplotlib._mathtext_data import uni2type1 as uni2type1
from matplotlib.mathtext import MathTextParser as MathTextParser
from matplotlib._ttconv import convert_ttf_to_ps as convert_ttf_to_ps
from matplotlib.ft2font import LOAD_NO_SCALE as LOAD_NO_SCALE
from matplotlib.ft2font import LOAD_NO_HINTING as LOAD_NO_HINTING
from matplotlib.font_manager import get_font as get_font
from matplotlib.cbook import file_requires_unicode as file_requires_unicode
from matplotlib.cbook import is_writable_file_like as is_writable_file_like
from matplotlib.backend_bases import _no_output_draw as _no_output_draw
from matplotlib.backend_bases import RendererBase as RendererBase
from matplotlib.backend_bases import GraphicsContextBase as GraphicsContextBase
from matplotlib.backend_bases import FigureManagerBase as FigureManagerBase
from matplotlib.backend_bases import FigureCanvasBase as FigureCanvasBase
from matplotlib.backend_bases import _check_savefig_extra_args as _check_savefig_extra_args
from matplotlib.backend_bases import _Backend as _Backend
from matplotlib.afm import AFM as AFM
from matplotlib import _text_layout as _text_layout
from matplotlib import _path as _path
from matplotlib import cbook as cbook
from matplotlib import _api as _api
from tempfile import TemporaryDirectory as TemporaryDirectory
from io import TextIOWrapper as TextIOWrapper
from io import StringIO as StringIO
from enum import Enum as Enum
from enum import Enum
from typing import Any
from typing import Callable
from typing import ClassVar
from typing import Iterable
from typing import Optional
from typing import Tuple
from typing import Union

from matplotlib import _api
from matplotlib.backend_bases import FigureCanvasBase
from matplotlib.backend_bases import GraphicsContextBase
from matplotlib.backend_bases import _Backend
from matplotlib.backends._backend_pdf_ps import RendererPDFPSBase
from matplotlib.backends.backend_ps import FigureCanvasPS
from matplotlib.backends.backend_ps import GraphicsContextPS
from matplotlib.backends.backend_ps import PsBackendHelper
from matplotlib.backends.backend_ps import RendererPS
from matplotlib.backends.backend_ps import _Orientation
from matplotlib.font_manager import FontProperties
from matplotlib.path import Path
from matplotlib.text import Text
from matplotlib.transforms import Affine2DBase
from matplotlib.transforms import CompositeAffine2D
from matplotlib.transforms import CompositeGenericTransform
from matplotlib.transforms import Transform
from object import object

debugPS: int
backend_version: str


class PsBackendHelper(object):
    _cached: dict[Any, Any]

    def __init__(self: PsBackendHelper) -> None: ...


ps_backend_helper: PsBackendHelper
papersize: dict[Union[str, Any], Union[Union[tuple[float, int], tuple[int, int], tuple[float, float]], Any]]


def _get_papertype(w: {__lt__},
                   h: {__lt__}) -> Union[str, Any]: ...


def _num_to_str(val: {__eq__}) -> str: ...


def _nums_to_str(*args) -> str: ...


def quote_ps_string(s: Any) -> str: ...


def _move_path_to_path_or_stream(src: Union[str, Any],
                                 dst: Union[Union[str, bytes], Any]) -> None: ...


def _font_to_ps_type3(font_path: Any,
                      glyph_ids: Iterable[int]) -> str: ...


class RendererPS(RendererPDFPSBase):
    _afm_font_dir: ClassVar[Path]
    _use_afm_rc_name: ClassVar[str]
    mathtext_parser: ClassVar[Union[_deprecated_property, Any]]
    used_characters: ClassVar[Union[_deprecated_property, Any]]
    _hatches: dict[Any, Any]
    textcnt: int
    imagedpi: int
    _path_collection_id: int
    color: None
    linedash: None
    fontsize: None
    _pswriter: Any
    fontname: None
    linewidth: None
    image_magnification: float
    _clip_paths: dict[Any, Any]
    linecap: None
    psfrag: list[Any]
    _character_tracker: CharacterTracker
    linejoin: None

    def __init__(self: RendererPS,
                 width: Any,
                 height: Any,
                 pswriter: Any,
                 imagedpi: int = 72) -> None: ...

    @_api.deprecated("3.3")
    def track_characters(self: RendererPS,
                         *args,
                         **kwargs) -> Optional[Any]: ...

    @_api.deprecated("3.3")
    def merge_used_characters(self: RendererPS,
                              *args,
                              **kwargs) -> Optional[Any]: ...

    def set_color(self: RendererPS,
                  r: Any,
                  g: Any,
                  b: Any,
                  store: bool = True) -> None: ...

    def set_linewidth(self: RendererPS,
                      linewidth: Union[int, Any],
                      store: bool = True) -> None: ...

    def _linejoin_cmd(linejoin: Union[{__ne__}, Any]) -> str: ...

    def set_linejoin(self: RendererPS,
                     linejoin: {__ne__},
                     store: bool = True) -> None: ...

    def _linecap_cmd(linecap: Union[{__ne__}, Any]) -> str: ...

    def set_linecap(self: RendererPS,
                    linecap: {__ne__},
                    store: bool = True) -> None: ...

    def set_linedash(self: RendererPS,
                     offset: Any,
                     seq: Optional[{__len__}],
                     store: bool = True) -> None: ...

    def set_font(self: RendererPS,
                 fontname: Any,
                 fontsize: Any,
                 store: bool = True) -> None: ...

    def create_hatch(self: RendererPS,
                     hatch: Any) -> Union[str, Any]: ...

    def get_image_magnification(self: RendererPS) -> float: ...

    def _convert_path(self: RendererPS,
                      path: Union[Union[Path, None, {should_simplify}], Any],
                      transform: Union[Union[Transform, {input_dims, output_dims}, {output_dims,
                                                                                    input_dims}, CompositeAffine2D, CompositeGenericTransform, _NotImplementedType], Any],
                      clip: bool = False,
                      simplify: Union[bool, Any] = None) -> Any: ...

    def _get_clip_cmd(self: RendererPS,
                      gc: Union[Union[{get_rgb, set_linewidth}, {get_hatch_path}, {get_linewidth, get_alpha,
                                                                                   get_forced_alpha,
                                                                                   get_rgb}, GraphicsContextBase], Any]) -> str: ...

    def draw_image(self: RendererPS,
                   gc: Any,
                   x: Union[int, float, complex],
                   y: Union[int, float, complex],
                   im: int,
                   transform: Affine2DBase = None) -> None: ...

    def draw_path(self: RendererPS,
                  gc: {get_hatch_path},
                  path: {should_simplify},
                  transform: Any,
                  rgbFace: Any = None) -> None: ...

    def draw_markers(self: RendererPS,
                     gc: {get_linewidth, get_alpha, get_forced_alpha, get_rgb},
                     marker_path: Any,
                     marker_trans: Transform,
                     path: {iter_segments},
                     trans: Transform,
                     rgbFace: {__getitem__} = None) -> None: ...

    def draw_path_collection(self: RendererPS,
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

    @_api.delete_parameter("3.3", "ismath")
    def draw_tex(self: RendererPS,
                 gc: {get_rgb, set_linewidth},
                 x: Union[float, Any],
                 y: Any,
                 s: Any,
                 prop: {get_size_in_points},
                 angle: Any,
                 ismath: str = 'TeX!',
                 mtext: Any = None) -> Optional[Any]: ...

    def draw_text(self: RendererPS,
                  gc: Union[{get_rgb, set_linewidth}, Any],
                  x: float,
                  y: float,
                  s: str,
                  prop: FontProperties,
                  angle: float,
                  ismath: bool = False,
                  mtext: Text = None) -> Optional[Any]: ...

    def draw_mathtext(self: RendererPS,
                      gc: Union[{get_rgb, set_linewidth}, Any],
                      x: Any,
                      y: Any,
                      s: Any,
                      prop: Any,
                      angle: Any) -> None: ...

    def draw_gouraud_triangle(self: RendererPS,
                              gc: Any,
                              points: int,
                              colors: int,
                              trans: {transform}) -> None: ...

    def draw_gouraud_triangles(self: RendererPS,
                               gc: Any,
                               points: {__len__, ndim, shape, reshape},
                               colors: {__len__, ndim, shape, reshape},
                               trans: {transform}) -> None: ...

    def _draw_ps(self: RendererPS,
                 ps: Union[str, Any],
                 gc: Union[Union[{get_linewidth, get_alpha, get_forced_alpha, get_rgb}, GraphicsContextBase], Any],
                 rgbFace: Optional[Any],
                 fill: bool = True,
                 stroke: bool = True,
                 command: Any = None) -> None: ...


def _is_transparent(rgb_or_rgba: Union[Union[{__getitem__}, tuple[float, float, float, float]], Any]) -> bool: ...


@_api.deprecated("3.4", alternative="GraphicsContextBase")
class GraphicsContextPS(GraphicsContextBase):
    def get_capstyle(self: GraphicsContextPS) -> Any: ...

    def get_joinstyle(self: GraphicsContextPS) -> Any: ...


class _Orientation(Enum):
    portrait: ClassVar[_Orientation]
    landscape: ClassVar[_Orientation]

    def swap_if_landscape(self: _Orientation,
                          shape: Any) -> Any: ...


class FigureCanvasPS(FigureCanvasBase):
    fixed_dpi: ClassVar[int]
    filetypes: ClassVar[dict[str, str]]
    _pswriter: StringIO

    def get_default_filetype(self: FigureCanvasPS) -> str: ...

    def print_ps(self: FigureCanvasPS,
                 outfile: Any,
                 *args,
                 **kwargs) -> Optional[Any]: ...

    def print_eps(self: FigureCanvasPS,
                  outfile: Any,
                  *args,
                  **kwargs) -> Optional[Any]: ...

    @_api.delete_parameter("3.4", "dpi")
    def _print_ps(self: FigureCanvasPS,
                  outfile: Any,
                  format: Union[str, Any],
                  dpi: Any = None,
                  metadata: Any = None,
                  papertype: Any = None,
                  orientation: str = 'portrait',
                  *args,
                  **kwargs) -> Optional[Any]: ...

    def _print_figure(self: FigureCanvasPS,
                      outfile: Any,
                      format: {__eq__},
                      *,
                      dpi: Any,
                      dsc_comments: Any,
                      orientation: {swap_if_landscape},
                      papertype: {__eq__},
                      bbox_inches_restore: Any = None) -> Any: ...

    def _print_figure_tex(self: FigureCanvasPS,
                          outfile: Any,
                          format: {__eq__},
                          *,
                          dpi: Any,
                          dsc_comments: Any,
                          orientation: {name},
                          papertype: Any,
                          bbox_inches_restore: Any = None) -> Optional[Any]: ...

    def draw(self: FigureCanvasPS) -> None: ...


def convert_psfrags(tmpfile: Union[str, Any],
                    psfrags: Union[list[Any], Any],
                    font_preamble: Union[str, Any],
                    custom_preamble: Optional[Any],
                    paper_width: Any,
                    paper_height: Any,
                    orientation: {__eq__}) -> bool: ...


def _try_distill(*args,
                 func: Union[Union[Callable[[{__add__}, bool, str, Any, bool], None], Callable[
                     [{__add__}, bool, str, Any, bool], None]], Any],
                 **kwargs) -> None: ...


def gs_distill(tmpfile: {__add__},
               eps: bool = False,
               ptype: str = 'letter',
               bbox: Any = None,
               rotated: bool = False) -> None: ...


def xpdf_distill(tmpfile: {__add__},
                 eps: bool = False,
                 ptype: str = 'letter',
                 bbox: Any = None,
                 rotated: bool = False) -> None: ...


def get_bbox_header(lbrt: Union[Union[tuple[Union[float, Any], Union[float, Any], Union[float, Any], Union[float, Any]],
                                      tuple[int, int, Union[int, Any], Union[int, Any]]], Any],
                    rotated: bool = False) -> Tuple[str, str]: ...


FigureManagerPS: Type[FigureManagerBase]

psDefs: list[str]


def pstoeps(tmpfile: Union[Union[{__add__}, {__add__}], Any],
            bbox: Any = None,
            rotated: bool = False) -> None: ...


class _BackendPS(_Backend):
    FigureCanvas: ClassVar[Type[FigureCanvasPS]]
    pass