from matplotlib._pylab_helpers import Gcf as Gcf
from matplotlib.figure import Figure as Figure
from matplotlib.path import Path as Path
from matplotlib.backends.backend_pdf import _datetime_to_pdf as _datetime_to_pdf
from matplotlib.backends.backend_pdf import _create_pdf_info_dict as _create_pdf_info_dict
from matplotlib.backends.backend_mixed import MixedModeRenderer as MixedModeRenderer
from matplotlib.backend_bases import _no_output_draw as _no_output_draw
from matplotlib.backend_bases import RendererBase as RendererBase
from matplotlib.backend_bases import GraphicsContextBase as GraphicsContextBase
from matplotlib.backend_bases import FigureManagerBase as FigureManagerBase
from matplotlib.backend_bases import FigureCanvasBase as FigureCanvasBase
from matplotlib.backend_bases import _check_savefig_extra_args as _check_savefig_extra_args
from matplotlib.backend_bases import _Backend as _Backend
from matplotlib import font_manager as fm
from matplotlib import cbook as cbook
from matplotlib import _api as _api
from PIL import Image as Image
from tempfile import TemporaryDirectory as TemporaryDirectory
from io import BytesIO as BytesIO
from codecs import StreamWriter
from pathlib import Path
from typing import Any
from typing import Callable
from typing import ClassVar
from typing import Iterable
from typing import Optional
from typing import Tuple
from typing import Type
from typing import Union

from Exception import Exception
from matplotlib import _api
from matplotlib.backend_bases import FigureCanvasBase
from matplotlib.backend_bases import GraphicsContextBase
from matplotlib.backend_bases import RendererBase
from matplotlib.backend_bases import _Backend
from matplotlib.backends.backend_pgf import FigureCanvasPgf
from matplotlib.backends.backend_pgf import LatexError
from matplotlib.backends.backend_pgf import LatexManager
from matplotlib.backends.backend_pgf import PdfPages
from matplotlib.backends.backend_pgf import RendererPgf
from matplotlib.backends.backend_pgf import TmpDirCleaner
from matplotlib.font_manager import FontProperties
from matplotlib.text import Text
from matplotlib.transforms import Affine2DBase
from matplotlib.transforms import Transform
from object import object


def get_fontspec() -> str: ...


latex_pt_to_in: float

latex_in_to_pt: float

mpl_pt_to_in: float

mpl_in_to_pt: float

NO_ESCAPE: str

re_mathsep: Pattern[str]

_replace_escapetext: partial[str]

_replace_mathdefault: partial[str]


def get_preamble() -> Optional[Any]: ...


def common_texification(text: Union[str, Any]) -> str: ...


def writeln(fh: Union[StreamWriter, Any],
            line: Union[str, Any]) -> None: ...


def _font_properties_str(prop: Union[Union[{get_size_in_points}, FontProperties], Any]) -> str: ...


def _metadata_to_str(key: {__eq__},
                     value: Any) -> str: ...


def make_pdf_to_png_converter() -> Union[Callable[[Any, Any, Any], None], Callable[[Any, Any, Any], None]]: ...


class LatexError(Exception):
    latex_output: str

    def __init__(self: LatexError,
                 message: Any,
                 latex_output: str = "") -> None: ...

    def __str__(self: LatexError) -> str: ...


class LatexManager(object):
    tmpdir: AnyStr
    _tmpdir: Union[TemporaryDirectory[AnyStr], TemporaryDirectory[Union[Union[str, bytes], Any]]]
    _finalize_latex: finalize
    latex_header: str
    texcommand: Optional[Any]
    latex: None
    str_cache: dict[Any, Any]
    _finalize_tmpdir: finalize

    def _build_latex_header() -> str: ...

    def _get_cached_or_new(cls: Type[LatexManager]) -> LatexManager: ...

    def _get_cached_or_new_impl(cls: Type[LatexManager],
                                header: Union[str, Any]) -> LatexManager: ...

    def _stdin_writeln(self: LatexManager,
                       s: Union[str, Any]) -> None: ...

    def _expect(self: LatexManager,
                s: Union[str, Any]) -> str: ...

    def _expect_prompt(self: LatexManager) -> str: ...

    def __init__(self: LatexManager) -> Any: ...

    def _setup_latex_process(self: LatexManager) -> None: ...

    @_api.deprecated("3.3")
    def latex_stdin_utf8(self: LatexManager) -> Any: ...

    def get_width_height_descent(self: LatexManager,
                                 text: Union[str, Any],
                                 prop: Any) -> Union[Tuple[float, float, float], Any]: ...


def _get_image_inclusion_command() -> str: ...


class RendererPgf(RendererBase):
    fh: Any
    figure: {dpi}
    image_counter: int
    dpi: Any

    @_api.delete_parameter("3.3", "dummy")
    def __init__(self: RendererPgf,
                 figure: {dpi},
                 fh: Any,
                 dummy: bool = False) -> Optional[Any]: ...

    def draw_markers(self: RendererPgf,
                     gc: {get_capstyle, get_joinstyle, get_forced_alpha, get_linewidth, get_rgb, get_dashes},
                     marker_path: {get_extents, iter_segments},
                     marker_trans: Transform,
                     path: {iter_segments},
                     trans: Transform,
                     rgbFace: Any = None) -> None: ...

    def draw_path(self: RendererPgf,
                  gc: {get_capstyle, get_joinstyle, get_forced_alpha, get_linewidth, get_rgb, get_dashes, get_hatch},
                  path: Any,
                  transform: Any,
                  rgbFace: Any = None) -> None: ...

    def _print_pgf_clip(self: RendererPgf,
                        gc: Union[Union[{get_linewidth}, {get_linewidth, get_hatch}], Any]) -> None: ...

    def _print_pgf_path_styles(self: RendererPgf,
                               gc: Union[Union[{get_linewidth}, {get_linewidth, get_hatch}], Any],
                               rgbFace: Any) -> None: ...

    def _print_pgf_path(self: RendererPgf,
                        gc: Union[Union[None, {get_linewidth, get_hatch}, {get_linewidth}], Any],
                        path: {iter_segments},
                        transform: Any,
                        rgbFace: Any = None) -> None: ...

    def _pgf_path_draw(self: RendererPgf,
                       stroke: bool = True,
                       fill: bool = False) -> None: ...

    def option_scale_image(self: RendererPgf) -> bool: ...

    def option_image_nocomposite(self: RendererPgf) -> bool: ...

    def draw_image(self: RendererPgf,
                   gc: Any,
                   x: Union[int, float, complex],
                   y: Union[int, float, complex],
                   im: int,
                   transform: Affine2DBase = None) -> None: ...

    def draw_tex(self: RendererPgf,
                 gc: {get_rgb, set_linewidth},
                 x: Any,
                 y: Any,
                 s: Any,
                 prop: Any,
                 angle: Any,
                 ismath: str = "TeX!",
                 mtext: Any = None) -> None: ...

    def draw_text(self: RendererPgf,
                  gc: Union[{get_rgb, set_linewidth}, Any],
                  x: float,
                  y: float,
                  s: str,
                  prop: FontProperties,
                  angle: float,
                  ismath: bool = False,
                  mtext: Text = None) -> None: ...

    def get_text_width_height_descent(self: RendererPgf,
                                      s: Any,
                                      prop: {get_size_in_points},
                                      ismath: {__eq__}) -> Tuple[
        Union[float, Any], Union[float, Any], Union[float, Any]]: ...

    def flipy(self: RendererPgf) -> bool: ...

    def get_canvas_width_height(self: RendererPgf) -> Tuple[Any, Any]: ...

    def points_to_pixels(self: RendererPgf,
                         points: Union[Union[float, Iterable, int], Any]) -> Union[float, Any]: ...


@_api.deprecated("3.3", alternative="GraphicsContextBase")
class GraphicsContextPgf(GraphicsContextBase):
    pass


@_api.deprecated("3.4")
class TmpDirCleaner(object):
    _remaining_tmpdirs: ClassVar[set[Any]]

    @_api.classproperty
    @_api.deprecated("3.4")
    def remaining_tmpdirs(cls: TmpDirCleaner) -> Union[set[Any], Any]: ...

    @_api.deprecated("3.4")
    def add(tmpdir: Any) -> Optional[Any]: ...

    @_api.deprecated("3.4")
    def cleanup_remaining_tmpdirs() -> Optional[Any]: ...


class FigureCanvasPgf(FigureCanvasBase):
    filetypes: ClassVar[dict[str, str]]

    def get_default_filetype(self: FigureCanvasPgf) -> str: ...

    def _print_pgf_to_fh(self: FigureCanvasPgf,
                         fh: Union[StreamWriter, Any],
                         *,
                         bbox_inches_restore: Any = None) -> Optional[Any]: ...

    def print_pgf(self: FigureCanvasPgf,
                  fname_or_fh: Union[Path, Any],
                  *args,
                  **kwargs) -> None: ...

    def print_pdf(self: FigureCanvasPgf,
                  fname_or_fh: Union[Path, Any],
                  metadata: Any = None,
                  *args,
                  **kwargs) -> None: ...

    def print_png(self: FigureCanvasPgf,
                  fname_or_fh: Any,
                  *args,
                  **kwargs) -> None: ...

    def get_renderer(self: FigureCanvasPgf) -> RendererPgf: ...

    def draw(self: FigureCanvasPgf) -> None: ...


FigureManagerPgf: Type[FigureManagerBase]


class _BackendPgf(_Backend):
    FigureCanvas: ClassVar[Type[FigureCanvasPgf]]
    pass


class PdfPages(object):
    __slots__: ClassVar[tuple[str, str, str, str, str, str]]
    metadata: ClassVar[Union[_deprecated_property, Any]]
    _file: BytesIO
    keep_empty: bool
    _info_dict: datetime
    _n_figures: int
    _metadata: dict[Any, Any]
    _output_name: Any

    def __init__(self: PdfPages,
                 filename: Any,
                 *,
                 keep_empty: bool = True,
                 metadata: Optional[dict] = None) -> None: ...

    def _write_header(self: PdfPages,
                      width_inches: Any,
                      height_inches: Any) -> None: ...

    def __enter__(self: PdfPages) -> PdfPages: ...

    def __exit__(self: PdfPages,
                 exc_type: Any,
                 exc_val: Any,
                 exc_tb: Any) -> None: ...

    def close(self: PdfPages) -> None: ...

    def _run_latex(self: PdfPages) -> None: ...

    def savefig(self: PdfPages,
                figure: Any = None,
                **kwargs) -> Any: ...

    def get_pagecount(self: PdfPages) -> int: ...
