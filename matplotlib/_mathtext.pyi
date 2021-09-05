from ft2font import KERNING_DEFAULT as KERNING_DEFAULT
from font_manager import get_font as get_font
from font_manager import findfont as findfont
from font_manager import FontProperties as FontProperties
from afm import AFM as AFM
from _mathtext_data import tex2uni as tex2uni
from _mathtext_data import stix_virtual_fonts as stix_virtual_fonts
from _mathtext_data import latex_to_standard as latex_to_standard
from _mathtext_data import latex_to_bakoma as latex_to_bakoma
from matplotlib import cbook as cbook
from matplotlib import _api as _api
from pyparsing import ZeroOrMore as ZeroOrMore
from pyparsing import Suppress as Suppress
from pyparsing import StringEnd as StringEnd
from pyparsing import Regex as Regex
from pyparsing import QuotedString as QuotedString
from pyparsing import ParseResults as ParseResults
from pyparsing import ParserElement as ParserElement
from pyparsing import ParseFatalException as ParseFatalException
from pyparsing import ParseBaseException as ParseBaseException
from pyparsing import Optional as Optional
from pyparsing import OneOrMore as OneOrMore
from pyparsing import oneOf as oneOf
from pyparsing import Literal as Literal
from pyparsing import Group as Group
from pyparsing import Forward as Forward
from pyparsing import FollowedBy as FollowedBy
from pyparsing import Empty as Empty
from pyparsing import Combine as Combine
from io import StringIO as StringIO
from collections import namedtuple as namedtuple
from types import SimpleNamespace
from typing import Any
from typing import ClassVar
from typing import List
from typing import Optional
from typing import Tuple
from typing import Type
from typing import Union

from matplotlib import _api
from matplotlib._mathtext import Accent
from matplotlib._mathtext import AutoHeightChar
from matplotlib._mathtext import AutoWidthChar
from matplotlib._mathtext import BakomaFonts
from matplotlib._mathtext import Box
from matplotlib._mathtext import Char
from matplotlib._mathtext import DejaVuFonts
from matplotlib._mathtext import DejaVuSansFontConstants
from matplotlib._mathtext import Fil
from matplotlib._mathtext import Fill
from matplotlib._mathtext import Filll
from matplotlib._mathtext import Fonts
from matplotlib._mathtext import Glue
from matplotlib._mathtext import HCentered
from matplotlib._mathtext import Hbox
from matplotlib._mathtext import Hlist
from matplotlib._mathtext import Hrule
from matplotlib._mathtext import Kern
from matplotlib._mathtext import List
from matplotlib._mathtext import NegFil
from matplotlib._mathtext import NegFill
from matplotlib._mathtext import NegFilll
from matplotlib._mathtext import Node
from matplotlib._mathtext import Parser
from matplotlib._mathtext import Rule
from matplotlib._mathtext import Ship
from matplotlib._mathtext import SsGlue
from matplotlib._mathtext import StandardPsFonts
from matplotlib._mathtext import StixFonts
from matplotlib._mathtext import SubSuperCluster
from matplotlib._mathtext import TruetypeFonts
from matplotlib._mathtext import UnicodeFonts
from matplotlib._mathtext import VCentered
from matplotlib._mathtext import Vbox
from matplotlib._mathtext import Vlist
from matplotlib._mathtext import Vrule
from matplotlib._mathtext.Parser import State
from matplotlib._mathtext.Parser import _MathStyle
from matplotlib.afm import AFM
from object import object
from pyparsing import Empty


def get_unicode_index(symbol: str,
                      math: bool = True) -> Union[int, Any]: ...


class Fonts(object):
    depth: Any
    mathtext_backend: Any
    used_characters: dict[Any, Any]
    width: Any
    default_font_prop: Any
    height: Any

    def __init__(self: Fonts,
                 default_font_prop: Any,
                 mathtext_backend: Any) -> None: ...

    @_api.deprecated("3.4")
    def destroy(self: Fonts) -> Optional[Any]: ...

    def get_kern(self: Fonts,
                 font1: Union[Union[{__eq__}, {__eq__}], Any],
                 fontclass1: Any,
                 sym1: Any,
                 fontsize1: Any,
                 font2: Any,
                 fontclass2: Any,
                 sym2: Any,
                 fontsize2: Any,
                 dpi: Any) -> float: ...

    def get_metrics(self: Fonts,
                    font: str,
                    font_class: str,
                    sym: str,
                    fontsize: float,
                    dpi: float,
                    math: bool = True) -> object: ...

    def set_canvas_size(self: Fonts,
                        w: Any,
                        h: Any,
                        d: Any) -> None: ...

    @_api.rename_parameter("3.4", "facename", "font")
    def render_glyph(self: Fonts,
                     ox: Any,
                     oy: Any,
                     font: Any,
                     font_class: Any,
                     sym: Any,
                     fontsize: Any,
                     dpi: Any) -> Optional[Any]: ...

    def render_rect_filled(self: Fonts,
                           x1: Any,
                           y1: Any,
                           x2: Any,
                           y2: Any) -> None: ...

    def get_xheight(self: Fonts,
                    font: Any,
                    fontsize: Any,
                    dpi: Any) -> Any: ...

    def get_underline_thickness(self: Fonts,
                                font: Any,
                                fontsize: Any,
                                dpi: Any) -> Any: ...

    def get_used_characters(self: Fonts) -> dict[Any, Any]: ...

    def get_results(self: Fonts,
                    box: Any) -> Any: ...

    def get_sized_alternatives_for_symbol(self: Fonts,
                                          fontname: Any,
                                          sym: Any) -> list[Tuple[Any, Any]]: ...


class TruetypeFonts(Fonts):
    glyphd: dict[str, Any]
    _fonts: dict[str, Any]

    def __init__(self: TruetypeFonts,
                 default_font_prop: Any,
                 mathtext_backend: Any) -> None: ...

    @_api.deprecated("3.4")
    def destroy(self: TruetypeFonts) -> Optional[Any]: ...

    def _get_font(self: TruetypeFonts,
                  font: Union[Union[str, int], Any]) -> Optional[Any]: ...

    def _get_offset(self: TruetypeFonts,
                    font: {postscript_name},
                    glyph: Any,
                    fontsize: Any,
                    dpi: Any) -> Union[float, Any]: ...

    def _get_info(self: TruetypeFonts,
                  fontname: Union[{__eq__}, Any],
                  font_class: Any,
                  sym: Any,
                  fontsize: Any,
                  dpi: Any,
                  math: bool = True) -> Union[SimpleNamespace, Any]: ...

    def get_xheight(self: TruetypeFonts,
                    fontname: Any,
                    fontsize: {__truediv__},
                    dpi: {__truediv__}) -> Union[float, Any]: ...

    def get_underline_thickness(self: TruetypeFonts,
                                font: Any,
                                fontsize: Any,
                                dpi: Any) -> Union[float, Any]: ...

    def get_kern(self: TruetypeFonts,
                 font1: Union[{__eq__}, Any],
                 fontclass1: Any,
                 sym1: Any,
                 fontsize1: {__eq__},
                 font2: Any,
                 fontclass2: Any,
                 sym2: Any,
                 fontsize2: Any,
                 dpi: Any) -> Union[float, Any]: ...


class BakomaFonts(TruetypeFonts):
    _fontmap: ClassVar[dict[str, str]]
    _slanted_symbols: ClassVar[set[str]]
    _size_alternatives: ClassVar[dict[Union[str, Any], Union[list[tuple[str, str]], Any]]]
    _stix_fallback: StixFonts
    fontmap: dict[str, str]

    def __init__(self: BakomaFonts,
                 *args,
                 **kwargs) -> None: ...

    def _get_glyph(self: BakomaFonts,
                   fontname: Any,
                   font_class: Any,
                   sym: Union[{__eq__}, Any],
                   fontsize: Any,
                   math: bool = True) -> Union[Union[Tuple[Optional[Any], Union[int, Any], Any, Any, Union[bool, Any]],
                                                     Tuple[Optional[Any], int, Optional[Any], Any, Union[
                                                         bool, Any]]], Any]: ...

    def get_sized_alternatives_for_symbol(self: BakomaFonts,
                                          fontname: Any,
                                          sym: Any) -> Union[list[Tuple[str, str]], Any]: ...


class UnicodeFonts(TruetypeFonts):
    use_cmex: ClassVar[bool]
    _slanted_symbols: ClassVar[set[str]]
    fontmap: dict[Union[str, int], str]
    cm_fallback: Union[StixSansFonts, StixFonts, BakomaFonts, None]

    def __init__(self: UnicodeFonts,
                 *args,
                 **kwargs) -> None: ...

    def _map_virtual_font(self: UnicodeFonts,
                          fontname: Union[str, Any],
                          font_class: Any,
                          uniindex: Any) -> Tuple[Union[str, Any], Any]: ...

    def _get_glyph(self: UnicodeFonts,
                   fontname: Union[str, Any],
                   font_class: Any,
                   sym: Union[{__eq__}, Any],
                   fontsize: Any,
                   math: bool = True) -> Union[Union[Tuple[Optional[Any], int, Optional[Any], Any, Union[bool, Any]],
                                                     Tuple[Optional[Any], Union[int, Any], Any, Any, Union[
                                                         bool, Any]]], Any]: ...

    def get_sized_alternatives_for_symbol(self: UnicodeFonts,
                                          fontname: Any,
                                          sym: Any) -> Union[Union[list[Tuple[Any, Union[str, Any]]], list[
        Tuple[int, str]], list[Tuple[str, str]], list[Tuple[Any, Any]]], Any]: ...


class DejaVuFonts(UnicodeFonts):
    use_cmex: ClassVar[bool]
    bakoma: BakomaFonts
    fontmap: dict[Union[str, int], str]
    cm_fallback: StixSansFonts

    def __init__(self: DejaVuFonts,
                 *args,
                 **kwargs) -> None: ...

    def _get_glyph(self: DejaVuFonts,
                   fontname: Any,
                   font_class: Any,
                   sym: {__eq__},
                   fontsize: Any,
                   math: bool = True) -> Union[Union[Tuple[Optional[Any], Union[int, Any], Any, Any, Union[bool, Any]],
                                                     Tuple[Optional[Any], int, Optional[Any], Any, Union[
                                                         bool, Any]]], Any]: ...


class DejaVuSerifFonts(DejaVuFonts):
    _fontmap: ClassVar[dict[Union[str, int], str]]
    pass


class DejaVuSansFonts(DejaVuFonts):
    _fontmap: ClassVar[dict[Union[str, int], str]]
    pass


class StixFonts(UnicodeFonts):
    _fontmap: ClassVar[dict[Union[Union[str, int], Any], Union[str, Any]]]
    use_cmex: ClassVar[bool]
    cm_fallback: ClassVar[bool]
    _sans: ClassVar[bool]
    fontmap: dict[Union[Union[str, int], Any], str]

    def __init__(self: StixFonts,
                 *args,
                 **kwargs) -> None: ...

    def _map_virtual_font(self: StixFonts,
                          fontname: Union[str, Any],
                          font_class: Any,
                          uniindex: Any) -> Tuple[
        Union[Union[str, int, Tuple[int, int, str, int], None], Any], Union[int, Any]]: ...

    def get_sized_alternatives_for_symbol(self: StixFonts,
                                          fontname: Any,
                                          sym: Any) -> Union[
        list[Tuple[Any, Union[str, Any]]], list[Tuple[int, str]]]: ...


class StixSansFonts(StixFonts):
    _sans: ClassVar[bool]
    pass


class StandardPsFonts(Fonts):
    basepath: ClassVar[str]
    fontmap: ClassVar[dict[Optional[str], str]]
    pswriter: ClassVar[Union[_deprecated_property, Any]]
    glyphd: dict[str, AFM]
    fonts: dict[str, AFM]

    def __init__(self: StandardPsFonts,
                 default_font_prop: Any,
                 mathtext_backend: Any = None) -> None: ...

    def _get_font(self: StandardPsFonts,
                  font: Union[Union[str, {__eq__}], Any]) -> AFM: ...

    def _get_info(self: StandardPsFonts,
                  fontname: Union[{__eq__}, Any],
                  font_class: Any,
                  sym: {__len__},
                  fontsize: Any,
                  dpi: Any,
                  math: bool = True) -> Any: ...

    def get_kern(self: StandardPsFonts,
                 font1: {__eq__},
                 fontclass1: Any,
                 sym1: Any,
                 fontsize1: {__eq__},
                 font2: Any,
                 fontclass2: Any,
                 sym2: Any,
                 fontsize2: Any,
                 dpi: Any) -> Union[float, Any]: ...

    def get_xheight(self: StandardPsFonts,
                    font: Any,
                    fontsize: Any,
                    dpi: Any) -> Union[float, Any]: ...

    def get_underline_thickness(self: StandardPsFonts,
                                font: Any,
                                fontsize: Any,
                                dpi: Any) -> Union[float, Any]: ...


SHRINK_FACTOR: float
GROW_FACTOR: float
NUM_SIZE_LEVELS: int


class FontConstantsBase(object):
    script_space: ClassVar[float]
    subdrop: ClassVar[float]
    sup1: ClassVar[float]
    sub1: ClassVar[float]
    sub2: ClassVar[float]
    delta: ClassVar[float]
    delta_slanted: ClassVar[float]
    delta_integral: ClassVar[float]
    pass


class ComputerModernFontConstants(FontConstantsBase):
    script_space: ClassVar[float]
    subdrop: ClassVar[float]
    sup1: ClassVar[float]
    sub1: ClassVar[float]
    sub2: ClassVar[float]
    delta: ClassVar[float]
    delta_slanted: ClassVar[float]
    delta_integral: ClassVar[float]
    pass


class STIXFontConstants(FontConstantsBase):
    script_space: ClassVar[float]
    sup1: ClassVar[float]
    sub2: ClassVar[float]
    delta: ClassVar[float]
    delta_slanted: ClassVar[float]
    delta_integral: ClassVar[float]
    pass


class STIXSansFontConstants(FontConstantsBase):
    script_space: ClassVar[float]
    sup1: ClassVar[float]
    delta_slanted: ClassVar[float]
    delta_integral: ClassVar[float]
    pass


class DejaVuSerifFontConstants(FontConstantsBase):
    pass


_font_constant_mapping: dict[Union[str, Any], Union[
    Type[Union[DejaVuSansFontConstants, DejaVuSerifFontConstants, ComputerModernFontConstants]], Any]]


class DejaVuSansFontConstants(FontConstantsBase):
    pass


def _get_font_constant_set(state: Union[State, Any]) -> Union[Type[Union[
    STIXSansFontConstants, DejaVuSansFontConstants, DejaVuSerifFontConstants, ComputerModernFontConstants]], Any]: ...


class Node(object):
    size: int

    def __init__(self: Node) -> None: ...

    def __repr__(self: Node) -> str: ...

    def get_kerning(self: Node,
                    next: Union[Optional[Glue], Any]) -> float: ...

    def shrink(self: Node) -> None: ...

    def grow(self: Node) -> None: ...

    def render(self: Node,
               x: Any,
               y: Any) -> None: ...


class Box(Node):
    depth: Union[float, Any]
    width: Union[float, Any]
    height: Union[float, Any]

    def __init__(self: Box,
                 width: Union[float, Any],
                 height: Union[float, Any],
                 depth: Union[float, Any]) -> None: ...

    def shrink(self: Box) -> None: ...

    def grow(self: Box) -> None: ...

    def render(self: Box,
               x1: Union[float, Any],
               y1: Union[float, Any],
               x2: Any,
               y2: Any) -> None: ...


class Vbox(Box):
    def __init__(self: Vbox,
                 height: Union[float, Any],
                 depth: Union[float, Any]) -> None: ...


class Hbox(Box):
    def __init__(self: Hbox,
                 width: Union[float, Any]) -> None: ...


class Char(Node):
    c: Any
    depth: Any
    width: Any
    font_output: Any
    fontsize: Any
    math: bool
    dpi: Any
    _metrics: Any
    font_class: Any
    font: Any
    height: Any

    def __init__(self: Char,
                 c: Any,
                 state: {font_output, font, font_class, fontsize, dpi},
                 math: bool = True) -> None: ...

    def __repr__(self: Char) -> Union[str, Any]: ...

    def _update_metrics(self: Char) -> None: ...

    def is_slanted(self: Char) -> Any: ...

    def get_kerning(self: Char,
                    next: Union[Optional[Glue], Any]) -> Union[float, Any]: ...

    def render(self: Char,
               x: Union[float, Any],
               y: Any) -> None: ...

    def shrink(self: Char) -> None: ...

    def grow(self: Char) -> None: ...


class Accent(Char):
    depth: int
    width: Any
    _metrics: Any
    height: Any

    def _update_metrics(self: Accent) -> None: ...

    def shrink(self: Accent) -> None: ...

    def grow(self: Accent) -> None: ...

    def render(self: Accent,
               x: Union[float, Any],
               y: {__add__}) -> None: ...


class List(Box):
    children: Union[Union[list[Union[Glue, Any]], list[Any], list[Char]], Any]
    glue_set: float
    shift_amount: float
    glue_ratio: float
    glue_order: int
    glue_sign: int

    def __init__(self: List,
                 elements: Union[Union[list[Union[Glue, Any]], list[Any], list[Char]], Any]) -> None: ...

    def __repr__(self: List) -> str: ...

    def _determine_order(totals: Union[list[float], Any]) -> Union[int, Any]: ...

    def _set_glue(self: List,
                  x: Union[float, Any],
                  sign: Union[int, Any],
                  totals: Union[list[float], Any],
                  error_type: Union[str, Any]) -> None: ...

    def shrink(self: List) -> None: ...

    def grow(self: List) -> None: ...


class Hlist(List):
    depth: Union[float, Any]
    children: list[Union[Union[Glue, Kern], Any]]
    width: float
    glue_ratio: float
    glue_order: int
    glue_sign: int
    height: Union[float, Any]

    def __init__(self: Hlist,
                 elements: Union[list[Union[Glue, Any]], Any],
                 w: float = 0.,
                 m: str = 'additional',
                 do_kern: bool = True) -> None: ...

    def kern(self: Hlist) -> None: ...

    def hpack(self: Hlist,
              w: float = 0.,
              m: str = 'additional') -> None: ...


class Vlist(List):
    depth: float
    width: Union[float, Any]
    glue_ratio: float
    glue_order: int
    glue_sign: int
    height: float

    def __init__(self: Vlist,
                 elements: Union[Union[list[Union[Glue, Any]], list[Any], list[Char]], Any],
                 h: float = 0.,
                 m: str = 'additional') -> None: ...

    def vpack(self: Vlist,
              h: float = 0.,
              m: str = 'additional',
              l: float = np.inf) -> None: ...


class Rule(Box):
    font_output: Any

    def __init__(self: Rule,
                 width: Union[float, Any],
                 height: Any,
                 depth: Union[float, Any],
                 state: {font_output}) -> None: ...

    def render(self: Rule,
               x: {__add__},
               y: {__add__},
               w: Any,
               h: Any) -> None: ...


class Hrule(Rule):
    def __init__(self: Hrule,
                 state: Union[{font_output, font, fontsize, dpi}, Any],
                 thickness: Optional[{__mul__}] = None) -> None: ...


class Vrule(Rule):
    def __init__(self: Vrule,
                 state: {font_output}) -> None: ...


_GlueSpec: Type[_GlueSpec]
_named: dict[str, _GlueSpec]


class Glue(Node):
    glue_subtype: ClassVar[Union[_deprecated_property, Any]]
    glue_spec: Union[str, Any]

    @_api.delete_parameter("3.3", "copy")
    def __init__(self: Glue,
                 glue_type: Union[str, Any],
                 copy: bool = False) -> Any: ...

    def shrink(self: Glue) -> None: ...

    def grow(self: Glue) -> None: ...


@_api.deprecated("3.3", alternative="Glue('fil')")
class Fil(Glue):
    def __init__(self: Fil) -> None: ...


@_api.deprecated("3.3", alternative="Glue('fill')")
class Fill(Glue):
    def __init__(self: Fill) -> None: ...


@_api.deprecated("3.3", alternative="Glue('filll')")
class Filll(Glue):
    def __init__(self: Filll) -> None: ...


@_api.deprecated("3.3", alternative="Glue('neg_fil')")
class NegFil(Glue):
    def __init__(self: NegFil) -> None: ...


@_api.deprecated("3.3", alternative="Glue('neg_fill')")
class NegFill(Glue):
    def __init__(self: NegFill) -> None: ...


@_api.deprecated("3.3", alternative="Glue('neg_filll')")
class NegFilll(Glue):
    def __init__(self: NegFilll) -> None: ...


@_api.deprecated("3.3", alternative="Glue('ss')")
class SsGlue(Glue):
    def __init__(self: SsGlue) -> None: ...


class HCentered(Hlist):
    def __init__(self: HCentered,
                 elements: Union[list[Union[Glue, Any]], Any]) -> None: ...


class VCentered(Vlist):
    def __init__(self: VCentered,
                 elements: Union[Union[list[Union[Glue, Any]], list[Any], list[Char]], Any]) -> None: ...


class Kern(Node):
    height: ClassVar[int]
    depth: ClassVar[int]
    width: Any

    def __init__(self: Kern,
                 width: Any) -> None: ...

    def __repr__(self: Kern) -> Union[str, Any]: ...

    def shrink(self: Kern) -> None: ...

    def grow(self: Kern) -> None: ...


class SubSuperCluster(Hlist):
    super: None
    sub: None
    nucleus: None

    def __init__(self: SubSuperCluster) -> None: ...


class AutoHeightChar(Hlist):
    shift_amount: Union[int, Any]

    def __init__(self: AutoHeightChar,
                 c: Any,
                 height: {__add__},
                 depth: Any,
                 state: {font_output, font, fontsize, dpi},
                 always: bool = False,
                 factor: Any = None) -> None: ...


class AutoWidthChar(Hlist):
    width: Any

    def __init__(self: AutoWidthChar,
                 c: Any,
                 width: {__truediv__},
                 state: {font_output, font},
                 always: bool = False,
                 char_class: Type[Char] = Char) -> None: ...


class Ship(object):
    cur_h: float
    max_push: int
    off_h: Any
    off_v: Any
    cur_s: int
    cur_v: float

    def __call__(self: Ship,
                 ox: Any,
                 oy: {__add__},
                 box: {height}) -> None: ...

    def clamp(value: {__lt__, __gt__}) -> Union[float, {__lt__, __gt__}]: ...

    def hlist_out(self: Ship,
                  box: Union[Union[{height}, Hlist], Any]) -> None: ...

    def vlist_out(self: Ship,
                  box: Union[List, Any]) -> Any: ...


ship: Ship


def Error(msg: Union[str, Any]) -> Empty: ...


class Parser(object):
    _binary_operators: ClassVar[set[str]]
    _relation_symbols: ClassVar[set[str]]
    _arrow_symbols: ClassVar[set[str]]
    _spaced_symbols: ClassVar[set[str]]
    _punctuation_symbols: ClassVar[set[str]]
    _overunder_symbols: ClassVar[set[str]]
    _overunder_functions: ClassVar[set[str]]
    _dropsub_symbols: ClassVar[set[str]]
    _fontnames: ClassVar[set[str]]
    _function_names: ClassVar[set[str]]
    _ambi_delim: ClassVar[set[str]]
    _left_delim: ClassVar[set[str]]
    _right_delim: ClassVar[set[str]]
    _space_widths: ClassVar[dict[Union[str, Any], Union[Union[float, int], Any]]]
    accentprefixed: ClassVar[Callable[[Parser, Any, Any, Any], Union[list[Char], list[Hlist]]]]
    _char_over_chars: ClassVar[dict[str, tuple[tuple[str, str, float], tuple[None, str, float], float]]]
    _accent_map: ClassVar[dict[Union[str, Any], Union[str, Any]]]
    _wide_accents: ClassVar[set[str]]
    _accentprefixed: ClassVar[list[Union[str, Any]]]
    required_group: ClassVar[Callable[[Parser, Any, Any, {__getitem__}], list[Hlist]]]
    simple_group: ClassVar[Callable[[Parser, Any, Any, {__getitem__}], list[Hlist]]]
    _state_stack: list[State]
    _math_expression: Forward
    _em_width_cache: dict[Any, Any]
    _expression: Forward

    def __init__(self: Parser) -> None: ...

    def parse(self: Parser,
              s: Any,
              fonts_object: Any,
              fontsize: Any,
              dpi: Any) -> Any: ...

    def get_state(self: Parser) -> State: ...

    def pop_state(self: Parser) -> None: ...

    def push_state(self: Parser) -> None: ...

    def main(self: Parser,
             s: Any,
             loc: Any,
             toks: Any) -> list[Hlist]: ...

    def math_string(self: Parser,
                    s: Any,
                    loc: Any,
                    toks: {__getitem__}) -> Any: ...

    def math(self: Parser,
             s: Any,
             loc: Any,
             toks: Any) -> list[Hlist]: ...

    def non_math(self: Parser,
                 s: Any,
                 loc: Any,
                 toks: {__getitem__}) -> list[Hlist]: ...

    def _make_space(self: Parser,
                    percentage: Union[Union[float, int], Any]) -> Kern: ...

    def space(self: Parser,
              s: Any,
              loc: Any,
              toks: Any) -> list[Kern]: ...

    def customspace(self: Parser,
                    s: Any,
                    loc: Any,
                    toks: {__getitem__}) -> list[Kern]: ...

    def symbol(self: Parser,
               s: Any,
               loc: Any,
               toks: Any) -> Union[list[Char], list[Hlist]]: ...

    def unknown_symbol(self: Parser,
                       s: Any,
                       loc: Any,
                       toks: Any) -> Any: ...

    def c_over_c(self: Parser,
                 s: Any,
                 loc: Any,
                 toks: Any) -> Vlist: ...

    def accent(self: Parser,
               s: Any,
               loc: Any,
               toks: Any) -> Vlist: ...

    def function(self: Parser,
                 s: Any,
                 loc: {__add__},
                 toks: {__getitem__}) -> Hlist: ...

    def operatorname(self: Parser,
                     s: Any,
                     loc: {__add__},
                     toks: {__getitem__}) -> Hlist: ...

    def start_group(self: Parser,
                    s: Any,
                    loc: Any,
                    toks: {__len__}) -> list[Any]: ...

    def group(self: Parser,
              s: Any,
              loc: Any,
              toks: {__getitem__}) -> list[Hlist]: ...

    def end_group(self: Parser,
                  s: Any,
                  loc: Any,
                  toks: Any) -> list[Any]: ...

    def font(self: Parser,
             s: Any,
             loc: Any,
             toks: Any) -> list[Any]: ...

    def is_overunder(self: Parser,
                     nucleus: Union[Hbox, Any]) -> bool: ...

    def is_dropsub(self: Parser,
                   nucleus: Union[Union[Glue, Kern, Hbox], Any]) -> bool: ...

    def is_slanted(self: Parser,
                   nucleus: Union[Union[Glue, Kern, Hbox], Any]) -> Union[bool, Any]: ...

    def is_between_brackets(self: Parser,
                            s: Any,
                            loc: Any) -> bool: ...

    def subsuper(self: Parser,
                 s: Any,
                 loc: Any,
                 toks: {__len__, __getitem__}) -> Union[list[Hlist], Any]: ...

    def _genfrac(self: Parser,
                 ldelim: Union[str, Any],
                 rdelim: Union[str, Any],
                 rule: Union[float, Any],
                 style: Union[_MathStyle, Any],
                 num: {width},
                 den: {width}) -> Union[Hlist, list[Hlist]]: ...

    def genfrac(self: Parser,
                s: Any,
                loc: Any,
                toks: Any) -> Union[Hlist, list[Hlist]]: ...

    def frac(self: Parser,
             s: Any,
             loc: Any,
             toks: Any) -> Union[Hlist, list[Hlist]]: ...

    def dfrac(self: Parser,
              s: Any,
              loc: Any,
              toks: Any) -> Union[Hlist, list[Hlist]]: ...

    def binom(self: Parser,
              s: Any,
              loc: Any,
              toks: Any) -> Union[Hlist, list[Hlist]]: ...

    def _genset(self: Parser,
                state: Union[State, Any],
                annotation: {shrink},
                body: Any,
                overunder: {__eq__}) -> Vlist: ...

    def sqrt(self: Parser,
             s: Any,
             loc: Any,
             toks: Any) -> list[Hlist]: ...

    def overline(self: Parser,
                 s: Any,
                 loc: Any,
                 toks: Any) -> list[Hlist]: ...

    def overset(self: Parser,
                s: Any,
                loc: Any,
                toks: {__len__, __getitem__}) -> Vlist: ...

    def underset(self: Parser,
                 s: Any,
                 loc: Any,
                 toks: {__len__, __getitem__}) -> Vlist: ...

    def _auto_sized_delimiter(self: Parser,
                              front: Union[str, Any],
                              middle: {__len__},
                              back: {__ne__}) -> Hlist: ...

    def auto_delim(self: Parser,
                   s: Any,
                   loc: Any,
                   toks: Any) -> Hlist: ...
