from typing import Iterable
from typing import Optional
from typing import Tuple
from typing import Union

from matplotlib.font_manager import FontProperties
from matplotlib.ft2font import FT2Font
from matplotlib.path import Path
from matplotlib.texmanager import TexManager
from matplotlib.textpath import TextPath
from matplotlib.textpath import TextToPath
from object import object


class TextToPath(object):
    def __init__(self: TextToPath) -> None: ...

    def _get_font(self: TextToPath,
                  prop: {get_size_in_points}) -> FT2Font: ...

    def _get_hinting_flag(self: TextToPath) -> int: ...

    def _get_char_id(self: TextToPath,
                     font: FT2Font,
                     ccode: Any) -> str: ...

    def get_text_width_height_descent(self: TextToPath,
                                      s: Any,
                                      prop: {get_size_in_points},
                                      ismath: {__eq__}) -> Union[Tuple[Any, Any, Any], Tuple[float, float, float]]: ...

    def get_text_path(self: TextToPath,
                      prop: Any,
                      s: str,
                      ismath: str = False) -> list: ...

    def get_glyphs_with_font(self: TextToPath,
                             font: FT2Font,
                             s: Any,
                             glyph_map: Any = None,
                             return_new_glyphs_only: bool = False) -> Tuple[
        list[Tuple[str, Any, int, float]], Union[OrderedDict[str, None], OrderedDict], list]: ...

    def get_glyphs_mathtext(self: TextToPath,
                            prop: Any,
                            s: Any,
                            glyph_map: Any = None,
                            return_new_glyphs_only: bool = False) -> Tuple[
        list[Tuple[str, Any, Any, float]], Union[OrderedDict[str, Any], OrderedDict], list[
            Tuple[list[Union[Tuple[Any, Any], Tuple[int, int]]], list[uint8]]]]: ...

    def get_texmanager(self: TextToPath) -> TexManager: ...

    def get_glyphs_tex(self: TextToPath,
                       prop: Any,
                       s: Any,
                       glyph_map: Any = None,
                       return_new_glyphs_only: bool = False) -> Tuple[
        list[Tuple[str, Any, Any, float]], Union[OrderedDict[str, None], OrderedDict], list[
            Tuple[list[Union[Tuple[Any, Any], Tuple[int, int]]], list[uint8]]]]: ...

    def _get_ps_font_and_encoding(texname: Any) -> Tuple[FT2Font, Optional[Iterable]]: ...


class TextPath(Path):
    def __init__(self: TextPath,
                 xy: Any,
                 s: str,
                 size: Union[float, None, int] = None,
                 prop: Optional[FontProperties] = None,
                 _interpolation_steps: Optional[int] = 1,
                 usetex: bool = False) -> None: ...

    def set_size(self: TextPath,
                 size: Union[None, float, int]) -> None: ...

    def get_size(self: TextPath) -> Union[None, float, int]: ...

    def vertices(self: TextPath) -> Any: ...

    def codes(self: TextPath) -> Iterable: ...

    def _revalidate_path(self: TextPath) -> None: ...
