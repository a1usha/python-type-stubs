from matplotlib import _backend_pdf_ps as _backend_pdf_ps
from matplotlib import _path as _path
from matplotlib.dates import UTC as UTC
from matplotlib.path import Path as Path
from matplotlib.transforms import BboxBase as BboxBase
from matplotlib.transforms import Affine2D as Affine2D
from matplotlib.mathtext import MathTextParser as MathTextParser
from matplotlib.ft2font import KERNING_UNFITTED as KERNING_UNFITTED
from matplotlib.ft2font import LOAD_NO_HINTING as LOAD_NO_HINTING
from matplotlib.ft2font import LOAD_NO_SCALE as LOAD_NO_SCALE
from matplotlib.ft2font import ITALIC as ITALIC
from matplotlib.ft2font import FIXED_WIDTH as FIXED_WIDTH
from matplotlib.afm import AFM as AFM
from matplotlib.font_manager import get_font as get_font
from matplotlib.font_manager import findfont as findfont
from matplotlib.figure import Figure as Figure
from matplotlib.backends.backend_mixed import MixedModeRenderer as MixedModeRenderer
from matplotlib.backend_bases import _no_output_draw as _no_output_draw
from matplotlib.backend_bases import RendererBase as RendererBase
from matplotlib.backend_bases import GraphicsContextBase as GraphicsContextBase
from matplotlib.backend_bases import FigureManagerBase as FigureManagerBase
from matplotlib.backend_bases import FigureCanvasBase as FigureCanvasBase
from matplotlib.backend_bases import _check_savefig_extra_args as _check_savefig_extra_args
from matplotlib.backend_bases import _Backend as _Backend
from matplotlib._pylab_helpers import Gcf as Gcf
from matplotlib import cbook as cbook
from matplotlib import _text_layout as _text_layout
from matplotlib import _api as _api
from PIL import Image as Image
from io import BytesIO as BytesIO
from functools import total_ordering as total_ordering
from enum import Enum as Enum
from datetime import datetime as datetime
from _typeshed import SupportsLessThan
from datetime import datetime
from enum import Enum
from typing import Any
from typing import ClassVar
from typing import Optional
from typing import Tuple
from typing import Type
from typing import Union

from PIL.Image import Image
from matplotlib import _api
from matplotlib.afm import AFM
from matplotlib.backend_bases import FigureCanvasBase
from matplotlib.backend_bases import GraphicsContextBase
from matplotlib.backend_bases import _Backend
from matplotlib.backends._backend_pdf_ps import RendererPDFPSBase
from matplotlib.backends.backend_pdf import FigureCanvasPdf
from matplotlib.backends.backend_pdf import GraphicsContextPdf
from matplotlib.backends.backend_pdf import Name
from matplotlib.backends.backend_pdf import Op
from matplotlib.backends.backend_pdf import Operator
from matplotlib.backends.backend_pdf import PdfFile
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.backends.backend_pdf import Reference
from matplotlib.backends.backend_pdf import RendererPdf
from matplotlib.backends.backend_pdf import Stream
from matplotlib.backends.backend_pdf import Verbatim
from matplotlib.font_manager import FontProperties
from matplotlib.mathtext import MathTextParser
from matplotlib.path import Path
from matplotlib.text import Text
from matplotlib.transforms import Affine2DBase
from matplotlib.transforms import Transform
from matplotlib.type1font import Type1Font
from object import object

_string_escape_regex: Pattern[bytes]


def fill(strings: Union[list[Union[bytes, Any]], Any],
         linelen: int = 75) -> bytes: ...


def _string_escape(match: {group}) -> Union[bytes, Any]: ...


def _create_pdf_info_dict(backend: str,
                          metadata: datetime) -> dict[str, Any]: ...


def _datetime_to_pdf(d: Union[datetime, Any]) -> str: ...


def pdfRepr(obj: Union[Union[
                           bytes, str, dict[str, Union[Reference, Name]], dict[str, Union[Reference, list[Name]]], dict[
                               str, Union[dict[str, Name], Reference, Name, list[Union[int, Any]]]], dict, dict[
                               str, Union[Name, list[Any], int]], dict[Any, Reference], dict[str, Name], dict[
                               str, Union[
                                   Union[Name, int, Reference, dict[str, Union[Name, list[Union[int, Any]]]]], Any]],
                           dict[Union[str, Any], Union[Union[Name, int, Reference], Any]], dict[Union[str, Any], Union[
                               Union[Name, int, Reference, list[int], list[Union[float, int]]], Any]], dict[
                               str, Union[Union[Name, int, list[int]], Any]], list[int], dict[
                               Union[SupportsLessThan, Any], Reference], int, dict[
                               str, Union[Union[Name, dict[str, Union[str, int]], Reference], Any]], dict[
                               str, Union[Union[Name, list[Reference], Reference], Any]], {__setitem__}, list[
                               Union[list[int], Any]], dict[Any, Any], datetime, dict[Name, Any], dict[
                               str, Union[Reference, int]]], Any]) -> Union[bytes, Any]: ...


class Reference(object):
    id: Any

    def __init__(self: Reference,
                 id: Any) -> None: ...

    def __repr__(self: Reference) -> Union[str, Any]: ...

    def pdfRepr(self: Reference) -> Union[bytes, Any]: ...

    def write(self: Reference,
              contents: Union[Union[dict[str, Union[Reference, Name]], dict[str, Union[Reference, list[Name]]], dict[
                  str, Union[dict[str, Name], Reference, Name, list[Union[int, Any]]]], dict, dict[
                                        str, Union[Name, list[Any], int]], dict[Any, Reference], dict[str, Name], dict[
                                        str, Union[Union[Name, int, Reference, dict[
                                            str, Union[Name, list[Union[int, Any]]]]], Any]], dict[
                                        Union[str, Any], Union[Union[Name, int, Reference], Any]], dict[
                                        Union[str, Any], Union[
                                            Union[Name, int, Reference, list[int], list[Union[float, int]]], Any]],
                                    dict[str, Union[Union[Name, int, list[int]], Any]], list[int], dict[
                                        Union[SupportsLessThan, Any], Reference], int, dict[
                                        str, Union[Union[Name, dict[str, Union[str, int]], Reference], Any]], dict[
                                        str, Union[Union[Name, list[Reference], Reference], Any]], {__setitem__}, list[
                                        Union[list[int], Any]], dict[Any, Any], datetime], Any],
              file: {write}) -> None: ...


class Name(object):
    __slots__: ClassVar[tuple[str]]
    _regex: ClassVar[Pattern[str]]
    name: bytes

    def __init__(self: Name,
                 name: Any) -> None: ...

    def __repr__(self: Name) -> str: ...

    def __str__(self: Name) -> str: ...

    def __eq__(self: Name,
               other: {name}) -> bool: ...

    def __lt__(self: Name,
               other: {name}) -> bool: ...

    def __hash__(self: Name) -> int: ...

    def hexify(match: {group}) -> str: ...

    def pdfRepr(self: Name) -> bytes: ...


class Operator(object):
    __slots__: ClassVar[tuple[str]]
    op: Any

    def __init__(self: Operator,
                 op: Any) -> None: ...

    def __repr__(self: Operator) -> Union[str, Any]: ...

    def pdfRepr(self: Operator) -> Any: ...


class Verbatim(object):
    _x: Any

    def __init__(self: Verbatim,
                 x: Any) -> None: ...

    def pdfRepr(self: Verbatim) -> Any: ...


class Op(Operator, Enum):
    close_fill_stroke: ClassVar[Op]
    fill_stroke: ClassVar[Op]
    fill: ClassVar[Op]
    closepath: ClassVar[Op]
    close_stroke: ClassVar[Op]
    stroke: ClassVar[Op]
    endpath: ClassVar[Op]
    begin_text: ClassVar[Op]
    end_text: ClassVar[Op]
    curveto: ClassVar[Op]
    rectangle: ClassVar[Op]
    lineto: ClassVar[Op]
    moveto: ClassVar[Op]
    concat_matrix: ClassVar[Op]
    use_xobject: ClassVar[Op]
    setgray_stroke: ClassVar[Op]
    setgray_nonstroke: ClassVar[Op]
    setrgb_stroke: ClassVar[Op]
    setrgb_nonstroke: ClassVar[Op]
    setcolorspace_stroke: ClassVar[Op]
    setcolorspace_nonstroke: ClassVar[Op]
    setcolor_stroke: ClassVar[Op]
    setcolor_nonstroke: ClassVar[Op]
    setdash: ClassVar[Op]
    setlinejoin: ClassVar[Op]
    setlinecap: ClassVar[Op]
    setgstate: ClassVar[Op]
    gsave: ClassVar[Op]
    grestore: ClassVar[Op]
    textpos: ClassVar[Op]
    selectfont: ClassVar[Op]
    textmatrix: ClassVar[Op]
    show: ClassVar[Op]
    showkern: ClassVar[Op]
    setlinewidth: ClassVar[Op]
    clip: ClassVar[Op]
    shading: ClassVar[Op]

    def paint_path(cls: Type[Op],
                   fill: bool,
                   stroke: bool) -> Op: ...


class Stream(object):
    __slots__: ClassVar[tuple[str, str, str, str, str, str, str]]
    pdfFile: PdfFile
    file: BytesIO
    len: Optional[Reference]
    pos: int
    extra: dict[Name, Any]
    id: int
    compressobj: _Compress

    def __init__(self: Stream,
                 id: int,
                 len: Optional[Reference],
                 file: PdfFile,
                 extra: dict[Name, Any] = None,
                 png: Optional[dict] = None) -> None: ...

    def _writeHeader(self: Stream) -> None: ...

    def end(self: Stream) -> None: ...

    def write(self: Stream,
              data: Any) -> None: ...

    def _flush(self: Stream) -> None: ...


def _get_pdf_charprocs(font_path: Any,
                       glyph_ids: Union[list[Any], Any]) -> dict[Any, Union[bytes, Any]]: ...


class PdfFile(object):
    _identityToUnicodeCMap: ClassVar[bytes]
    fh: Union[BytesIO, Any]
    _object_seq: count[Union[Union[int, float, SupportsFloat, SupportsInt, SupportsIndex, SupportsComplex], Any]]
    fontObject: Reference
    fontNames: dict[Any, Any]
    XObjectObject: Reference
    type1Descriptors: dict[Any, Any]
    _soft_mask_groups: list[Any]
    gouraudObject: Reference
    _image_seq: Generator[Name, Any, None]
    original_file_like: Any
    _soft_mask_states: dict[Any, Any]
    infoDict: datetime
    startxref: Union[int, Any]
    gouraudTriangles: list[Any]
    _internal_font_seq: Generator[Name, Any, None]
    _images: OrderedDict[Any, Any]
    hatchObject: Reference
    height: Any
    _extGStateObject: Reference
    _soft_mask_seq: Generator[Name, Any, None]
    passed_in_file_object: bool
    multi_byte_charprocs: dict[Any, Any]
    currentstream: None
    resourceObject: Reference
    pagesObject: Reference
    tell_base: Any
    _hatch_pattern_seq: Generator[Name, Any, None]
    infoObject: Reference
    dviFontInfo: dict[Any, Any]
    paths: list[Any]
    width: Any
    xrefTable: list[list[Union[int, str]]]
    pageAnnotations: list[Any]
    rootObject: Reference
    _character_tracker: CharacterTracker
    pageList: list[Any]
    _alpha_state_seq: Generator[Name, Any, None]
    markers: OrderedDict[Any, Any]
    _annotations: list[Any]
    alphaStates: dict[Any, Any]
    hatchPatterns: OrderedDict[Any, Any]

    def __init__(self: PdfFile,
                 filename: Any,
                 metadata: Any = None) -> None: ...

    @_api.deprecated("3.3")
    def used_characters(self: PdfFile) -> Any: ...

    def newPage(self: PdfFile,
                width: Any,
                height: Any) -> None: ...

    def newTextnote(self: PdfFile,
                    text: Any,
                    positionRect: list[int] = [-100, -100, 0, 0]) -> None: ...

    def finalize(self: PdfFile) -> None: ...

    def close(self: PdfFile) -> None: ...

    def write(self: PdfFile,
              data: Union[bytes, Any]) -> None: ...

    def output(self: PdfFile,
               *args) -> None: ...

    def beginStream(self: PdfFile,
                    id: Any,
                    len: Union[Optional[Reference], Any],
                    extra: Union[Union[
                                     dict[str, Union[int, Name, list[int]]], dict[str, Reference], dict[str, int], dict[
                                         str, bytes], dict[str, Union[
                                         int, Name, list[Union[int, Any]], list[Union[int, float]], float, dict[
                                             str, list[Name]]]], dict[
                                         str, Union[Union[int, Name, bool, list[Any]], Any]], dict[
                                         str, Union[Union[Name, Verbatim, int], Any]], dict[
                                         str, Union[Name, list[Any]]], dict[
                                         str, Union[Name, list[int], list[Any]]]], Any] = None,
                    png: Union[Optional[dict[str, Union[Union[int, Verbatim], Any]]], Any] = None) -> None: ...

    def endStream(self: PdfFile) -> None: ...

    def _write_annotations(self: PdfFile) -> None: ...

    def fontName(self: PdfFile,
                 fontprop: Union[SupportsLessThan, Any]) -> Union[Name, Any]: ...

    def dviFontName(self: PdfFile,
                    dvifont: {texname}) -> Union[Name, Any]: ...

    def writeFonts(self: PdfFile) -> None: ...

    def _write_afm_font(self: PdfFile,
                        filename: Union[SupportsLessThan, Any]) -> Reference: ...

    def _embedTeXFont(self: PdfFile,
                      fontinfo: {dvifont, __dict__, encodingfile, fontfile, effects}) -> Reference: ...

    def createType1Descriptor(self: PdfFile,
                              t1font: Union[Type1Font, Any],
                              fontfile: Any) -> Reference: ...

    def _get_xobject_symbol_name(self: PdfFile,
                                 filename: Union[SupportsLessThan, Any],
                                 symbol_name: Any) -> str: ...

    def embedTTF(self: PdfFile,
                 filename: Any,
                 characters: Any) -> Reference: ...

    def alphaState(self: PdfFile,
                   alpha: {__getitem__}) -> Union[Name, Any]: ...

    def _soft_mask_state(self: PdfFile,
                         smask: Reference) -> Name: ...

    def writeExtGSTates(self: PdfFile) -> None: ...

    def _write_soft_mask_groups(self: PdfFile) -> None: ...

    def hatchPattern(self: PdfFile,
                     hatch_style: Any) -> Union[Optional[Name], Any]: ...

    def writeHatches(self: PdfFile) -> None: ...

    def addGouraudTriangles(self: PdfFile,
                            points: Any,
                            colors: Any) -> Any: ...

    def writeGouraudTriangles(self: PdfFile) -> None: ...

    def imageObject(self: PdfFile,
                    image: Any) -> Union[Name, Any]: ...

    def _unpack(self: PdfFile,
                im: Any) -> Union[Tuple[Any, None], Tuple[Any, Optional[Any]]]: ...

    def _writePng(self: PdfFile,
                  img: Union[Image, Any]) -> Tuple[bytes, Optional[int], Optional[bytes]]: ...

    def _writeImg(self: PdfFile,
                  data: {shape},
                  id: Any,
                  smask: Any = None) -> Any: ...

    def writeImages(self: PdfFile) -> None: ...

    def markerObject(self: PdfFile,
                     path: Any,
                     trans: Any,
                     fill: Any,
                     stroke: Any,
                     lw: Any,
                     joinstyle: Any,
                     capstyle: Any) -> Union[Name, Any]: ...

    def writeMarkers(self: PdfFile) -> None: ...

    def pathCollectionObject(self: PdfFile,
                             gc: {get_joinstyle, get_capstyle},
                             path: Any,
                             trans: Any,
                             padding: Any,
                             filled: Any,
                             stroked: Any) -> Name: ...

    def writePathCollectionTemplates(self: PdfFile) -> None: ...

    def pathOperations(path: Union[Optional[Path], Any],
                       transform: Any,
                       clip: Union[Optional[tuple[float, float, Union[int, Any], Union[int, Any]]], Any] = None,
                       simplify: Union[bool, Any] = None,
                       sketch: Any = None) -> list[Verbatim]: ...

    def writePath(self: PdfFile,
                  path: Any,
                  transform: Any,
                  clip: bool = False,
                  sketch: Any = None) -> None: ...

    def reserveObject(self: PdfFile,
                      name: str = '') -> Reference: ...

    def recordXref(self: PdfFile,
                   id: Union[int, Any]) -> None: ...

    def writeObject(self: PdfFile,
                    object: Union[Reference, Any],
                    contents: Union[Union[dict[str, Union[Reference, Name]], dict[str, Union[Reference, list[Name]]],
                                          dict[str, Union[
                                              dict[str, Name], Reference, Name, list[Union[int, Any]]]], dict, dict[
                                              str, Union[Name, list[Any], int]], dict[Any, Reference], dict[str, Name],
                                          dict[str, Union[Union[Name, int, Reference, dict[
                                              str, Union[Name, list[Union[int, Any]]]]], Any]], dict[
                                              Union[str, Any], Union[Union[Name, int, Reference], Any]], dict[
                                              Union[str, Any], Union[Union[Name, int, Reference, list[int], list[
                                                  Union[float, int]]], Any]], dict[
                                              str, Union[Union[Name, int, list[int]], Any]], list[int], dict[
                                              Union[SupportsLessThan, Any], Reference], int, dict[
                                              str, Union[Union[Name, dict[str, Union[str, int]], Reference], Any]],
                                          dict[str, Union[Union[Name, list[Reference], Reference], Any]], {__setitem__},
                                          list[Union[list[int], Any]], dict[Any, Any], datetime], Any]) -> None: ...

    def writeXref(self: PdfFile) -> Any: ...

    def writeInfoDict(self: PdfFile) -> None: ...

    def writeTrailer(self: PdfFile) -> None: ...


class RendererPdf(RendererPDFPSBase):
    _afm_font_dir: ClassVar[Path]
    _use_afm_rc_name: ClassVar[str]
    file: Any
    image_dpi: Any
    gc: GraphicsContextPdf

    def __init__(self: RendererPdf,
                 file: Any,
                 image_dpi: Any,
                 height: Any,
                 width: Any) -> None: ...

    @_api.deprecated("3.4")
    def mathtext_parser(self: RendererPdf) -> MathTextParser: ...

    def finalize(self: RendererPdf) -> None: ...

    def check_gc(self: RendererPdf,
                 gc: Union[Union[{get_hatch_path, get_sketch_params}, GraphicsContextBase, {fill, stroke, get_joinstyle,
                                                                                            get_capstyle}, {_rgb,
                                                                                                            get_url}, {
                                     get_rgb, set_linewidth}], Any],
                 fillcolor: Optional[Any] = None) -> None: ...

    @_api.deprecated("3.3")
    def track_characters(self: RendererPdf,
                         *args,
                         **kwargs) -> Optional[Any]: ...

    @_api.deprecated("3.3")
    def merge_used_characters(self: RendererPdf,
                              *args,
                              **kwargs) -> Optional[Any]: ...

    def get_image_magnification(self: RendererPdf) -> Union[float, Any]: ...

    def draw_image(self: RendererPdf,
                   gc: Any,
                   x: Union[int, float, complex],
                   y: Union[int, float, complex],
                   im: int,
                   transform: Affine2DBase = None) -> None: ...

    def draw_path(self: RendererPdf,
                  gc: Union[GraphicsContextPdf, Any],
                  path: Any,
                  transform: Any,
                  rgbFace: Any = None) -> None: ...

    def draw_path_collection(self: RendererPdf,
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

    def draw_markers(self: RendererPdf,
                     gc: {fill, stroke, get_joinstyle, get_capstyle},
                     marker_path: {__len__},
                     marker_trans: Transform,
                     path: {iter_segments},
                     trans: Transform,
                     rgbFace: Any = None) -> None: ...

    def draw_gouraud_triangle(self: RendererPdf,
                              gc: Any,
                              points: int,
                              colors: int,
                              trans: {transform}) -> None: ...

    def draw_gouraud_triangles(self: RendererPdf,
                               gc: Any,
                               points: {__len__, ndim, shape},
                               colors: {__len__, ndim, shape, __getitem__},
                               trans: {transform}) -> None: ...

    def _setup_textpos(self: RendererPdf,
                       x: Union[float, Any],
                       y: Union[Union[float, int], Any],
                       angle: Union[Union[float, int], Any],
                       oldx: int = 0,
                       oldy: int = 0,
                       oldangle: int = 0) -> None: ...

    def draw_mathtext(self: RendererPdf,
                      gc: Union[{_rgb, get_url}, Any],
                      x: Any,
                      y: Any,
                      s: Any,
                      prop: Any,
                      angle: Any) -> None: ...

    @_api.delete_parameter("3.3", "ismath")
    def draw_tex(self: RendererPdf,
                 gc: {get_rgb, set_linewidth},
                 x: Any,
                 y: Any,
                 s: Any,
                 prop: {get_size_in_points},
                 angle: Any,
                 ismath: str = 'TeX!',
                 mtext: Any = None) -> Optional[Any]: ...

    def encode_string(self: RendererPdf,
                      s: Union[str, Any],
                      fonttype: Union[Optional[int], Any]) -> bytes: ...

    def draw_text(self: RendererPdf,
                  gc: {_rgb, get_url},
                  x: float,
                  y: float,
                  s: str,
                  prop: FontProperties,
                  angle: float,
                  ismath: bool = False,
                  mtext: Text = None) -> None: ...

    def _draw_xobject_glyph(self: RendererPdf,
                            font: Union[AFM, Any],
                            fontsize: Optional[Any],
                            glyph_idx: Any,
                            x: Any,
                            y: Any) -> None: ...

    def new_gc(self: RendererPdf) -> GraphicsContextPdf: ...


class GraphicsContextPdf(GraphicsContextBase):
    capstyles: ClassVar[dict[str, int]]
    joinstyles: ClassVar[dict[str, int]]
    commands: ClassVar[tuple[
        tuple[tuple[str, str], Callable[[GraphicsContextPdf, Any, Any], list[Union[Op, Any]]]], tuple[
            tuple[str, str, str], Callable[[GraphicsContextPdf, Any, Any, Any], list[Union[Op, Any]]]], tuple[
            tuple[str], Callable[[GraphicsContextPdf, Any], list[Union[Op, Any]]]], tuple[tuple[str], Callable[
            [GraphicsContextPdf, Union[tuple[float, float, float], Any]], Union[list[Any], list[Union[Op, Any]]]]],
        tuple[tuple[str], Callable[[GraphicsContextPdf, Any], list[Union[Op, Any]]]], tuple[
            tuple[str], Callable[[GraphicsContextPdf, Any], list[Union[Op, Any]]]], tuple[
            tuple[str], Callable[[GraphicsContextPdf, Any], list[Union[Union[list[Any], int, Op], Any]]]], tuple[
            tuple[str], Callable[[GraphicsContextPdf, {__getitem__}], Union[list[Any], list[Union[Op, Any]]]]], tuple[
            tuple[str, str], Callable[[GraphicsContextPdf, Any, Any], Union[
                list[Any], list[Union[Op, Any]], list[Union[Name, Op]], list[Union[Union[Name, Op], Any]]]]]]]
    parent: None
    file: Any
    _fillcolor: tuple[float, float, float]
    _effective_alphas: tuple[float, float]

    def __init__(self: GraphicsContextPdf,
                 file: Any) -> None: ...

    def __repr__(self: GraphicsContextPdf) -> str: ...

    def stroke(self: GraphicsContextPdf) -> bool: ...

    def fill(self: GraphicsContextPdf,
             *args) -> Union[bool, Any]: ...

    def paint(self: GraphicsContextPdf) -> Op: ...

    def capstyle_cmd(self: GraphicsContextPdf,
                     style: Any) -> list[Union[Op, Any]]: ...

    def joinstyle_cmd(self: GraphicsContextPdf,
                      style: Any) -> list[Union[Op, Any]]: ...

    def linewidth_cmd(self: GraphicsContextPdf,
                      width: Any) -> list[Union[Op, Any]]: ...

    def dash_cmd(self: GraphicsContextPdf,
                 dashes: Any) -> list[Union[Union[list[Any], int, Op], Any]]: ...

    def alpha_cmd(self: GraphicsContextPdf,
                  alpha: Any,
                  forced: Any,
                  effective_alphas: Any) -> list[Union[Op, Any]]: ...

    def hatch_cmd(self: GraphicsContextPdf,
                  hatch: Any,
                  hatch_color: Any) -> Union[
        list[Any], list[Union[Op, Any]], list[Union[Name, Op]], list[Union[Union[Name, Op], Any]]]: ...

    def rgb_cmd(self: GraphicsContextPdf,
                rgb: {__getitem__}) -> Union[list[Any], list[Union[Op, Any]]]: ...

    def fillcolor_cmd(self: GraphicsContextPdf,
                      rgb: Union[tuple[float, float, float], Any]) -> Union[
        list[Any], list[Union[float, Op]], list[Union[Op, Any]]]: ...

    def push(self: GraphicsContextPdf) -> list[Op]: ...

    def pop(self: GraphicsContextPdf) -> list[Op]: ...

    def clip_cmd(self: GraphicsContextPdf,
                 cliprect: Any,
                 clippath: Any) -> list[Union[Op, Any]]: ...

    def delta(self: GraphicsContextPdf,
              other: Union[Union[{get_hatch_path, get_sketch_params}, GraphicsContextBase, {fill, stroke, get_joinstyle,
                                                                                            get_capstyle}, {_rgb,
                                                                                                            get_url}, {
                                     get_rgb, set_linewidth}], Any]) -> list[Any]: ...

    def copy_properties(self: GraphicsContextPdf,
                        other: Union[Union[{get_rgb, set_linewidth}, GraphicsContextPdf], Any]) -> None: ...

    def finalize(self: GraphicsContextPdf) -> list[Op]: ...


class PdfPages(object):
    __slots__: ClassVar[tuple[str, str]]
    _file: PdfFile
    keep_empty: Optional[bool]

    def __init__(self: PdfPages,
                 filename: Any,
                 keep_empty: Optional[bool] = True,
                 metadata: Optional[dict] = None) -> None: ...

    def __enter__(self: PdfPages) -> PdfPages: ...

    def __exit__(self: PdfPages,
                 exc_type: Any,
                 exc_val: Any,
                 exc_tb: Any) -> None: ...

    def close(self: PdfPages) -> None: ...

    def infodict(self: PdfPages) -> datetime: ...

    def savefig(self: PdfPages,
                figure: Any = None,
                **kwargs) -> Any: ...

    def get_pagecount(self: PdfPages) -> int: ...

    def attach_note(self: PdfPages,
                    text: Any,
                    positionRect: list[int] = [-100, -100, 0, 0]) -> None: ...


class FigureCanvasPdf(FigureCanvasBase):
    fixed_dpi: ClassVar[int]
    filetypes: ClassVar[dict[str, str]]

    def get_default_filetype(self: FigureCanvasPdf) -> str: ...

    @_api.delete_parameter("3.4", "dpi")
    def print_pdf(self: FigureCanvasPdf,
                  filename: Any,
                  *,
                  dpi: Any = None,
                  bbox_inches_restore: Any = None,
                  metadata: Any = None) -> Optional[Any]: ...

    def draw(self: FigureCanvasPdf) -> None: ...


FigureManagerPdf: Type[FigureManagerBase]


class _BackendPdf(_Backend):
    FigureCanvas: ClassVar[Type[FigureCanvasPdf]]
    pass