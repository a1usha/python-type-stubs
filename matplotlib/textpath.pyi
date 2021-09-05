from matplotlib.transforms import Affine2D as Affine2D
from matplotlib.path import Path as Path
from matplotlib.mathtext import MathTextParser as MathTextParser
from matplotlib.ft2font import LOAD_TARGET_LIGHT as LOAD_TARGET_LIGHT
from matplotlib.ft2font import LOAD_NO_HINTING as LOAD_NO_HINTING
from matplotlib.font_manager import get_font as get_font
from matplotlib.font_manager import FontProperties as FontProperties
from matplotlib import rcParams as rcParams
from matplotlib import font_manager as font_manager
from matplotlib import dviread as dviread
from matplotlib import _text_layout as _text_layout
from collections import OrderedDict as OrderedDict
from typing import Any
from typing import ClassVar
from typing import Iterable
from typing import Optional
from typing import Tuple
from typing import Union

from matplotlib.font_manager import FontProperties
from matplotlib.path import Path
from matplotlib.texmanager import TexManager
from matplotlib.textpath import TextPath
from matplotlib.textpath import TextToPath
from object import object


class TextToPath(object):
    FONT_SCALE: ClassVar[float]
    DPI: ClassVar[int]
    mathtext_parser: MathTextParser
    _texmanager: None

    def __init__(self: TextToPath) -> None: ...

    def _get_font(self: TextToPath,
                  prop: Union[{get_size_in_points}, Any]) -> Any: ...

    def _get_hinting_flag(self: TextToPath) -> Any: ...

    def _get_char_id(self: TextToPath,
                     font: {postscript_name},
                     ccode: Any) -> str: ...

    def get_text_width_height_descent(self: TextToPath,
                                      s: Any,
                                      prop: {get_size_in_points},
                                      ismath: {__eq__}) -> Union[
        Tuple[Any, Any, Any], Tuple[Union[float, Any], Union[float, Any], Union[float, Any]]]: ...

    def get_text_path(self: TextToPath,
                      prop: Any,
                      s: str,
                      ismath: str = False) -> list: ...

    def get_glyphs_with_font(self: TextToPath,
                             font: {postscript_name},
                             s: Any,
                             glyph_map: Any = None,
                             return_new_glyphs_only: bool = False) -> Tuple[
        list[Tuple[str, Any, int, float]], Union[Union[OrderedDict[str, Any], OrderedDict[Any, Any]], Any], list[
            Any]]: ...

    def get_glyphs_mathtext(self: TextToPath,
                            prop: Any,
                            s: Any,
                            glyph_map: Any = None,
                            return_new_glyphs_only: bool = False) -> Tuple[
        list[Tuple[str, Any, Any, Union[float, Any]]], Union[Union[OrderedDict[str, Any], OrderedDict[Any, Any]], Any],
        list[Tuple[list[Union[Tuple[Any, Any], Tuple[int, int]]], list[uint8]]]]: ...

    def get_texmanager(self: TextToPath) -> Union[TexManager, Any]: ...

    def get_glyphs_tex(self: TextToPath,
                       prop: Any,
                       s: Any,
                       glyph_map: Any = None,
                       return_new_glyphs_only: bool = False) -> Tuple[
        list[Tuple[str, Any, Any, Union[float, Any]]], Union[Union[OrderedDict[str, Any], OrderedDict[Any, Any]], Any],
        list[Tuple[list[Union[Tuple[Any, Any], Tuple[int, int]]], list[uint8]]]]: ...

    def _get_ps_font_and_encoding(texname: Any) -> Tuple[Any, Optional[Iterable]]: ...


text_to_path: TextToPath


class TextPath(Path):
    _cached_vertices: None
    _size: Union[Union[None, float, int], Any]
    _xy: Any
    _codes: Iterable
    _interpolation_steps: Optional[int]
    _invalid: bool
    _vertices: Iterable
    _should_simplify: bool
    _simplify_threshold: Optional[Any]

    def __init__(self: TextPath,
                 xy: Any,
                 s: str,
                 size: Union[float, None, int] = None,
                 prop: Optional[FontProperties] = None,
                 _interpolation_steps: Optional[int] = 1,
                 usetex: bool = False) -> None: ...

    def set_size(self: TextPath,
                 size: Union[Union[None, float, int], Any]) -> None: ...

    def get_size(self: TextPath) -> Union[Union[None, float, int], Any]: ...

    def vertices(self: TextPath) -> Any: ...

    def codes(self: TextPath) -> Iterable: ...

    def _revalidate_path(self: TextPath) -> None: ...
