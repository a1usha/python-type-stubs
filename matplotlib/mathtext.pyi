from matplotlib._mathtext_data import tex2uni as tex2uni
from matplotlib._mathtext_data import stix_virtual_fonts as stix_virtual_fonts
from matplotlib._mathtext_data import latex_to_standard as latex_to_standard
from matplotlib._mathtext_data import latex_to_cmex as latex_to_cmex
from matplotlib._mathtext_data import latex_to_bakoma as latex_to_bakoma
from matplotlib._mathtext import NUM_SIZE_LEVELS as NUM_SIZE_LEVELS
from matplotlib._mathtext import GROW_FACTOR as GROW_FACTOR
from matplotlib._mathtext import SHRINK_FACTOR as SHRINK_FACTOR
from matplotlib.font_manager import FontProperties as FontProperties
from matplotlib.ft2font import LOAD_NO_HINTING as LOAD_NO_HINTING
from matplotlib.ft2font import FT2Image as FT2Image
from matplotlib import _mathtext as _mathtext
from matplotlib import rcParams as rcParams
from matplotlib import colors as mcolors
from matplotlib import _api as _api
from PIL import Image as Image
from io import StringIO as StringIO
from collections import namedtuple as namedtuple
from typing import Any
from typing import ClassVar
from typing import Optional
from typing import Tuple
from typing import Type
from typing import Union
from typing import _PDFResult
from typing import _PSResult
from typing import _Result

from Warning import Warning
from matplotlib import _api
from matplotlib.font_manager import FontProperties
from matplotlib.mathtext import GlueSpec
from matplotlib.mathtext import MathTextParser
from matplotlib.mathtext import MathtextBackend
from matplotlib.mathtext import MathtextBackendAgg
from matplotlib.mathtext import MathtextBackendBitmap
from matplotlib.mathtext import MathtextBackendCairo
from matplotlib.mathtext import MathtextBackendPath
from matplotlib.mathtext import MathtextBackendPdf
from matplotlib.mathtext import MathtextBackendPs
from matplotlib.mathtext import MathtextBackendSvg
from object import object

_log: Logger
get_unicode_index: Callable[[str, bool], Union[int, Any]]
__module__: Any
from typing import Any


class MathtextBackend(object):
    depth: int
    width: int
    height: int

    def __init__(self: MathtextBackend) -> None: ...

    def set_canvas_size(self: MathtextBackend,
                        w: Union[int, Any],
                        h: Any,
                        d: Any) -> None: ...

    def render_glyph(self: MathtextBackend,
                     ox: Any,
                     oy: Any,
                     info: Any) -> Any: ...

    def render_rect_filled(self: MathtextBackend,
                           x1: Any,
                           y1: Any,
                           x2: Any,
                           y2: Any) -> Any: ...

    def get_results(self: MathtextBackend,
                    box: Any) -> Any: ...

    def get_hinting_type(self: MathtextBackend) -> int: ...


class MathtextBackendAgg(MathtextBackend):
    mode: str
    image: None
    bbox: list[int]
    ox: int
    oy: int

    def __init__(self: MathtextBackendAgg) -> None: ...

    def _update_bbox(self: MathtextBackendAgg,
                     x1: Any,
                     y1: Any,
                     x2: Any,
                     y2: Any) -> None: ...

    def set_canvas_size(self: MathtextBackendAgg,
                        w: Union[int, Any],
                        h: Any,
                        d: Any) -> None: ...

    def render_glyph(self: MathtextBackendAgg,
                     ox: Any,
                     oy: Any,
                     info: Any) -> None: ...

    def render_rect_filled(self: MathtextBackendAgg,
                           x1: Any,
                           y1: Any,
                           x2: Any,
                           y2: Any) -> None: ...

    def get_results(self: MathtextBackendAgg,
                    box: {height, depth, glue_order, glue_sign, children},
                    used_characters: Any) -> Tuple[int, int, int, int, int, Any, Any]: ...

    def get_hinting_type(self: MathtextBackendAgg) -> int: ...


@_api.deprecated("3.4", alternative="mathtext.math_to_image")
class MathtextBackendBitmap(MathtextBackendAgg):
    def get_results(self: MathtextBackendBitmap,
                    box: {height, depth, glue_order, glue_sign, children},
                    used_characters: Any) -> Tuple[Any, int]: ...


@_api.deprecated("3.4", alternative="MathtextBackendPath")
class MathtextBackendPs(MathtextBackend):
    _PSResult: ClassVar[Type[_PSResult]]
    pswriter: StringIO
    lastfont: None

    def __init__(self: MathtextBackendPs) -> None: ...

    def render_glyph(self: MathtextBackendPs,
                     ox: Any,
                     oy: Any,
                     info: {offset, postscript_name, fontsize, symbol_name}) -> None: ...

    def render_rect_filled(self: MathtextBackendPs,
                           x1: Any,
                           y1: Any,
                           x2: {__sub__},
                           y2: {__sub__}) -> None: ...

    def get_results(self: MathtextBackendPs,
                    box: {height, glue_order, glue_sign, children},
                    used_characters: Any) -> _PSResult: ...


@_api.deprecated("3.4", alternative="MathtextBackendPath")
class MathtextBackendPdf(MathtextBackend):
    _PDFResult: ClassVar[Type[_PDFResult]]
    glyphs: list[Any]
    rects: list[Any]

    def __init__(self: MathtextBackendPdf) -> None: ...

    def render_glyph(self: MathtextBackendPdf,
                     ox: Any,
                     oy: Any,
                     info: {font, offset, fontsize, num, symbol_name}) -> None: ...

    def render_rect_filled(self: MathtextBackendPdf,
                           x1: Any,
                           y1: Any,
                           x2: {__sub__},
                           y2: {__sub__}) -> None: ...

    def get_results(self: MathtextBackendPdf,
                    box: {height, glue_order, glue_sign, children},
                    used_characters: Any) -> _PDFResult: ...


@_api.deprecated("3.4", alternative="MathtextBackendPath")
class MathtextBackendSvg(MathtextBackend):
    svg_rects: list[Any]
    svg_glyphs: list[Any]

    def __init__(self: MathtextBackendSvg) -> None: ...

    def render_glyph(self: MathtextBackendSvg,
                     ox: Any,
                     oy: Any,
                     info: {offset, font, fontsize, num, metrics}) -> None: ...

    def render_rect_filled(self: MathtextBackendSvg,
                           x1: Any,
                           y1: Any,
                           x2: {__sub__},
                           y2: {__sub__}) -> None: ...

    def get_results(self: MathtextBackendSvg,
                    box: {height, glue_order, glue_sign, children},
                    used_characters: Any) -> Tuple[int, int, int, SimpleNamespace, Any]: ...


class MathtextBackendPath(MathtextBackend):
    _Result: ClassVar[Type[_Result]]
    glyphs: list[Any]
    rects: list[Any]

    def __init__(self: MathtextBackendPath) -> None: ...

    def render_glyph(self: MathtextBackendPath,
                     ox: Any,
                     oy: Any,
                     info: {offset, font, fontsize, num}) -> None: ...

    def render_rect_filled(self: MathtextBackendPath,
                           x1: Any,
                           y1: Any,
                           x2: {__sub__},
                           y2: {__sub__}) -> None: ...

    def get_results(self: MathtextBackendPath,
                    box: {height, glue_order, glue_sign, children},
                    used_characters: Any) -> _Result: ...


@_api.deprecated("3.4", alternative="MathtextBackendPath")
class MathtextBackendCairo(MathtextBackend):
    glyphs: list[Any]
    rects: list[Any]

    def __init__(self: MathtextBackendCairo) -> None: ...

    def render_glyph(self: MathtextBackendCairo,
                     ox: Any,
                     oy: Any,
                     info: {offset, num, font, fontsize}) -> None: ...

    def render_rect_filled(self: MathtextBackendCairo,
                           x1: Any,
                           y1: {__sub__},
                           x2: {__sub__},
                           y2: {__sub__}) -> None: ...

    def get_results(self: MathtextBackendCairo,
                    box: {height, glue_order, glue_sign, children},
                    used_characters: Any) -> Tuple[int, int, int, list[Any], list[Any]]: ...


class MathTextWarning(Warning):
    pass


@_api.deprecated("3.3")
class GlueSpec(object):
    stretch: float
    shrink: float
    width: float
    stretch_order: int
    shrink_order: int

    def __init__(self: GlueSpec,
                 width: float = 0.,
                 stretch: float = 0.,
                 stretch_order: int = 0,
                 shrink: float = 0.,
                 shrink_order: int = 0) -> None: ...

    def copy(self: GlueSpec) -> GlueSpec: ...

    def factory(cls: Type[GlueSpec],
                glue_type: Any) -> Any: ...


@_api.deprecated("3.4")
def ship(ox: Any,
         oy: {__add__},
         box: {height, glue_order, glue_sign, children}) -> Optional[Any]: ...


class MathTextParser(object):
    _parser: ClassVar[None]
    _backend_mapping: ClassVar[
        dict[str, Union[Union[_deprecated_property, Type[MathtextBackendAgg], Type[MathtextBackendPath]], Any]]]
    _font_type_mapping: ClassVar[
        dict[str, Type[Union[BakomaFonts, DejaVuSerifFonts, DejaVuSansFonts, StixFonts, StixSansFonts, UnicodeFonts]]]]
    _output: Any

    def __init__(self: MathTextParser,
                 output: {lower}) -> None: ...

    def parse(self: MathTextParser,
              s: Union[str, Any],
              dpi: int = 72,
              prop: Union[FontProperties, Any] = None,
              *,
              _force_standard_ps_fonts: bool = False) -> Any: ...

    def _parse_cached(self: MathTextParser,
                      s: Union[str, Any],
                      dpi: Any,
                      prop: Optional[{get_math_fontfamily, get_size_in_points}],
                      force_standard_ps_fonts: Any) -> Any: ...

    @_api.deprecated("3.4", alternative="mathtext.math_to_image")
    def to_mask(self: MathTextParser,
                texstr: str,
                dpi: float = 120,
                fontsize: int = 14) -> Any: ...

    @_api.deprecated("3.4", alternative="mathtext.math_to_image")
    def to_rgba(self: MathTextParser,
                texstr: str,
                color: Any = 'black',
                dpi: float = 120,
                fontsize: int = 14) -> Any: ...

    @_api.deprecated("3.4", alternative="mathtext.math_to_image")
    def to_png(self: MathTextParser,
               filename: {__eq__, name},
               texstr: str,
               color: Any = 'black',
               dpi: float = 120,
               fontsize: int = 14) -> int: ...

    @_api.deprecated("3.4", alternative="mathtext.math_to_image")
    def get_depth(self: MathTextParser,
                  texstr: str,
                  dpi: float = 120,
                  fontsize: int = 14) -> int: ...


def math_to_image(s: str,
                  filename_or_obj: Any,
                  prop: Any = None,
                  dpi: Optional[float] = None,
                  format: Optional[str] = None) -> Any: ...