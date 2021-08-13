from typing import Any
from typing import List
from typing import Optional
from typing import Union

from matplotlib._mathtext import Glue
from matplotlib._mathtext import Hbox
from matplotlib._mathtext import Hlist
from matplotlib._mathtext import Kern
from matplotlib._mathtext import List
from matplotlib._mathtext.Parser import State
from matplotlib._mathtext.Parser import _MathStyle


class Rule(Box):
    def __init__(self: Rule,
                 width: float,
                 height: Any,
                 depth: float,
                 state: {font_output}) -> None: ...

    def render(self: Rule,
               x: {__add__},
               y: {__add__},
               w: Any,
               h: Any) -> None: ...


class State(object):
    def __init__(self: State,
                 font_output: Any,
                 font: Any,
                 font_class: Any,
                 fontsize: Any,
                 dpi: Any) -> None: ...

    def copy(self: State) -> State: ...

    @property
    def font(self: State) -> Any: ...

    @font.setter
    def font(self: State,
             name: Any) -> None: ...


class Char(Node):
    def __init__(self: Char,
                 c: Any,
                 state: {font_output, font, font_class, fontsize, dpi},
                 math: bool = True) -> None: ...

    def __repr__(self: Char) -> str: ...

    def _update_metrics(self: Char) -> None: ...

    def is_slanted(self: Char) -> Any: ...

    def get_kerning(self: Char,
                    next: Optional[Glue]) -> float: ...

    def render(self: Char,
               x: float,
               y: Any) -> None: ...

    def shrink(self: Char) -> None: ...

    def grow(self: Char) -> None: ...


class Parser(object):
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
                    percentage: Union[float, int]) -> Kern: ...

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
                    toks: {__len__}) -> list: ...

    def group(self: Parser,
              s: Any,
              loc: Any,
              toks: {__getitem__}) -> list[Hlist]: ...

    def end_group(self: Parser,
                  s: Any,
                  loc: Any,
                  toks: Any) -> list: ...

    def font(self: Parser,
             s: Any,
             loc: Any,
             toks: Any) -> list: ...

    def is_overunder(self: Parser,
                     nucleus: Hbox) -> bool: ...

    def is_dropsub(self: Parser,
                   nucleus: Union[Glue, Kern, Hbox]) -> bool: ...

    def is_slanted(self: Parser,
                   nucleus: Union[Glue, Kern, Hbox]) -> bool: ...

    def is_between_brackets(self: Parser,
                            s: Any,
                            loc: Any) -> bool: ...

    def subsuper(self: Parser,
                 s: Any,
                 loc: Any,
                 toks: {__len__, __getitem__}) -> list[Hlist]: ...

    def _genfrac(self: Parser,
                 ldelim: str,
                 rdelim: str,
                 rule: float,
                 style: _MathStyle,
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
                state: State,
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
                              front: str,
                              middle: {__len__},
                              back: {__ne__}) -> Hlist: ...

    def auto_delim(self: Parser,
                   s: Any,
                   loc: Any,
                   toks: Any) -> Hlist: ...


class List(Box):
    def __init__(self: List,
                 elements: Union[list[Glue], list, list[Char]]) -> None: ...

    def __repr__(self: List) -> str: ...

    @staticmethod
    def _determine_order(totals: list[float]) -> int: ...

    def _set_glue(self: List,
                  x: float,
                  sign: int,
                  totals: list[float],
                  error_type: str) -> None: ...

    def shrink(self: List) -> None: ...

    def grow(self: List) -> None: ...


class Fill(Glue):
    def __init__(self: Fill) -> None: ...


class Box(Node):
    def __init__(self: Box,
                 width: float,
                 height: float,
                 depth: float) -> None: ...

    def shrink(self: Box) -> None: ...

    def grow(self: Box) -> None: ...

    def render(self: Box,
               x1: float,
               y1: float,
               x2: Any,
               y2: Any) -> None: ...


class Hbox(Box):
    def __init__(self: Hbox,
                 width: float) -> None: ...


class SsGlue(Glue):
    def __init__(self: SsGlue) -> None: ...


class Filll(Glue):
    def __init__(self: Filll) -> None: ...


class DejaVuSerifFonts(DejaVuFonts):
    pass


class AutoHeightChar(Hlist):
    def __init__(self: AutoHeightChar,
                 c: Any,
                 height: {__add__},
                 depth: Any,
                 state: {font_output, font, fontsize, dpi},
                 always: bool = False,
                 factor: Any = None) -> None: ...


class SubSuperCluster(Hlist):
    def __init__(self: SubSuperCluster) -> None: ...


class Vbox(Box):
    def __init__(self: Vbox,
                 height: float,
                 depth: float) -> None: ...


class NegFilll(Glue):
    def __init__(self: NegFilll) -> None: ...


class DejaVuSansFontConstants(FontConstantsBase):
    pass


class Hrule(Rule):
    def __init__(self: Hrule,
                 state: {font_output, font, fontsize, dpi},
                 thickness: Optional[{__mul__}] = None) -> None: ...


class StixSansFonts(StixFonts):
    pass


class STIXSansFontConstants(FontConstantsBase):
    pass


class Accent(Char):
    def _update_metrics(self: Accent) -> None: ...

    def shrink(self: Accent) -> None: ...

    def grow(self: Accent) -> None: ...

    def render(self: Accent,
               x: float,
               y: {__add__}) -> None: ...


class Hlist(List):
    def __init__(self: Hlist,
                 elements: list[Glue],
                 w: float = 0.,
                 m: str = 'additional',
                 do_kern: bool = True) -> None: ...

    def kern(self: Hlist) -> None: ...

    def hpack(self: Hlist,
              w: float = 0.,
              m: str = 'additional') -> None: ...


class STIXFontConstants(FontConstantsBase):
    pass


class DejaVuFonts(UnicodeFonts):
    def __init__(self: DejaVuFonts,
                 *args,
                 **kwargs) -> None: ...

    def _get_glyph(self: DejaVuFonts,
                   fontname: Any,
                   font_class: Any,
                   sym: {__eq__},
                   fontsize: Any,
                   math: bool = True) -> Union[
        tuple[Optional[FT2Font], int, None, Any, bool], tuple[Optional[FT2Font], int, None, Any, bool]]: ...


class Glue(Node):
    @_api.delete_parameter
    def __init__(self: Glue,
                 glue_type: str,
                 copy: bool = False) -> Any: ...

    def shrink(self: Glue) -> None: ...

    def grow(self: Glue) -> None: ...


class NegFill(Glue):
    def __init__(self: NegFill) -> None: ...


class TruetypeFonts(Fonts):
    def __init__(self: TruetypeFonts,
                 default_font_prop: Any,
                 mathtext_backend: Any) -> None: ...

    @_api.deprecated
    def destroy(self: TruetypeFonts) -> Optional[Any]: ...

    def _get_font(self: TruetypeFonts,
                  font: Union[str, int]) -> FT2Font: ...

    def _get_offset(self: TruetypeFonts,
                    font: {postscript_name},
                    glyph: Any,
                    fontsize: Any,
                    dpi: Any) -> float: ...

    def _get_info(self: TruetypeFonts,
                  fontname: {__eq__},
                  font_class: Any,
                  sym: Any,
                  fontsize: Any,
                  dpi: Any,
                  math: bool = True) -> Optional[SimpleNamespace]: ...

    def get_xheight(self: TruetypeFonts,
                    fontname: Any,
                    fontsize: {__truediv__},
                    dpi: {__truediv__}) -> float: ...

    def get_underline_thickness(self: TruetypeFonts,
                                font: Any,
                                fontsize: Any,
                                dpi: Any) -> float: ...

    def get_kern(self: TruetypeFonts,
                 font1: {__eq__},
                 fontclass1: Any,
                 sym1: Any,
                 fontsize1: {__eq__},
                 font2: Any,
                 fontclass2: Any,
                 sym2: Any,
                 fontsize2: Any,
                 dpi: Any) -> float: ...


class Vlist(List):
    def __init__(self: Vlist,
                 elements: Union[list[Glue], list, list[Char]],
                 h: float = 0.,
                 m: str = 'additional') -> None: ...

    def vpack(self: Vlist,
              h: float = 0.,
              m: str = 'additional',
              l: float = np.inf) -> None: ...


class Vrule(Rule):
    def __init__(self: Vrule,
                 state: {font_output}) -> None: ...


class VCentered(Vlist):
    def __init__(self: VCentered,
                 elements: Union[list[Glue], list, list[Char]]) -> None: ...


class Fil(Glue):
    def __init__(self: Fil) -> None: ...


class StixFonts(UnicodeFonts):
    def __init__(self: StixFonts,
                 *args,
                 **kwargs) -> None: ...

    def _map_virtual_font(self: StixFonts,
                          fontname: str,
                          font_class: Any,
                          uniindex: Any) -> tuple[Union[str, int, tuple[int, int, str, int], None], int]: ...

    @functools.lru_cache
    def get_sized_alternatives_for_symbol(self: StixFonts,
                                          fontname: Any,
                                          sym: Any) -> Union[list[tuple[Any, str]], list[tuple[int, str]]]: ...


class HCentered(Hlist):
    def __init__(self: HCentered,
                 elements: list[Glue]) -> None: ...


class StandardPsFonts(Fonts):
    def __init__(self: StandardPsFonts,
                 default_font_prop: Any,
                 mathtext_backend: Any = None) -> None: ...

    def _get_font(self: StandardPsFonts,
                  font: Union[str, {__eq__}]) -> AFM: ...

    def _get_info(self: StandardPsFonts,
                  fontname: {__eq__},
                  font_class: Any,
                  sym: {__len__},
                  fontsize: Any,
                  dpi: Any,
                  math: bool = True) -> Optional[Any]: ...

    def get_kern(self: StandardPsFonts,
                 font1: {__eq__},
                 fontclass1: Any,
                 sym1: Any,
                 fontsize1: {__eq__},
                 font2: Any,
                 fontclass2: Any,
                 sym2: Any,
                 fontsize2: Any,
                 dpi: Any) -> float: ...

    def get_xheight(self: StandardPsFonts,
                    font: Any,
                    fontsize: Any,
                    dpi: Any) -> float: ...

    def get_underline_thickness(self: StandardPsFonts,
                                font: Any,
                                fontsize: Any,
                                dpi: Any) -> float: ...


class DejaVuSansFonts(DejaVuFonts):
    pass


class Fonts(object):
    def __init__(self: Fonts,
                 default_font_prop: Any,
                 mathtext_backend: Any) -> None: ...

    @_api.deprecated
    def destroy(self: Fonts) -> Optional[Any]: ...

    def get_kern(self: Fonts,
                 font1: Union[{__eq__}, {__eq__}],
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

    @_api.rename_parameter
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

    def get_used_characters(self: Fonts) -> dict: ...

    def get_results(self: Fonts,
                    box: Any) -> Any: ...

    def get_sized_alternatives_for_symbol(self: Fonts,
                                          fontname: Any,
                                          sym: Any) -> list[tuple[Any, Any]]: ...


class ComputerModernFontConstants(FontConstantsBase):
    pass


class BakomaFonts(TruetypeFonts):
    def __init__(self: BakomaFonts,
                 *args,
                 **kwargs) -> None: ...

    def _get_glyph(self: BakomaFonts,
                   fontname: Any,
                   font_class: Any,
                   sym: {__eq__},
                   fontsize: Any,
                   math: bool = True) -> Union[
        tuple[Optional[FT2Font], int, None, Any, bool], tuple[Optional[FT2Font], int, None, Any, bool]]: ...

    def get_sized_alternatives_for_symbol(self: BakomaFonts,
                                          fontname: Any,
                                          sym: Any) -> list[tuple[str, str]]: ...


class Ship(object):
    def __call__(self: Ship,
                 ox: Any,
                 oy: {__add__},
                 box: {height}) -> None: ...

    @staticmethod
    def clamp(value: {__lt__, __gt__}) -> Union[float, {__lt__, __gt__}]: ...

    def hlist_out(self: Ship,
                  box: Hlist) -> None: ...

    def vlist_out(self: Ship,
                  box: List) -> Any: ...


class Kern(Node):
    def __init__(self: Kern,
                 width: Any) -> None: ...

    def __repr__(self: Kern) -> str: ...

    def shrink(self: Kern) -> None: ...

    def grow(self: Kern) -> None: ...


class DejaVuSerifFontConstants(FontConstantsBase):
    pass


class AutoWidthChar(Hlist):
    def __init__(self: AutoWidthChar,
                 c: Any,
                 width: {__truediv__},
                 state: {font_output, font},
                 always: bool = False,
                 char_class: Type[Char] = Char) -> None: ...


class FontConstantsBase(object):
    pass


class _MathStyle(Enum):
    pass


class NegFil(Glue):
    def __init__(self: NegFil) -> None: ...


class UnicodeFonts(TruetypeFonts):
    def __init__(self: UnicodeFonts,
                 *args,
                 **kwargs) -> None: ...

    def _map_virtual_font(self: UnicodeFonts,
                          fontname: str,
                          font_class: Any,
                          uniindex: Any) -> tuple[str, Any]: ...

    def _get_glyph(self: UnicodeFonts,
                   fontname: str,
                   font_class: Any,
                   sym: {__eq__},
                   fontsize: Any,
                   math: bool = True) -> Union[
        tuple[Optional[FT2Font], int, None, Any, bool], tuple[Optional[FT2Font], int, None, Any, bool]]: ...

    def get_sized_alternatives_for_symbol(self: UnicodeFonts,
                                          fontname: Any,
                                          sym: Any) -> Union[
        list[tuple[Any, str]], list[tuple[int, str]], list[tuple[str, str]], list[tuple[Any, Any]]]: ...


class Node(object):
    def __init__(self: Node) -> None: ...

    def __repr__(self: Node) -> str: ...

    def get_kerning(self: Node,
                    next: Optional[Glue]) -> float: ...

    def shrink(self: Node) -> None: ...

    def grow(self: Node) -> None: ...

    def render(self: Node,
               x: Any,
               y: Any) -> None: ...


def _get_font_constant_set(state: State) -> Type[
    Union[STIXSansFontConstants, DejaVuSansFontConstants, DejaVuSerifFontConstants, ComputerModernFontConstants]]: ...


def Error(msg: str) -> Empty: ...


def get_unicode_index(symbol: str,
                      math: bool = True) -> int: ...