from json.encoder import JSONEncoder
from pathlib import Path
from typing import Any
from typing import Optional
from typing import Type
from typing import Union

from matplotlib.font_manager import FontEntry
from matplotlib.font_manager import FontManager
from matplotlib.font_manager import FontProperties
from matplotlib.font_manager import _JSONEncoder
from matplotlib.ft2font import FT2Font
from object import object


def _cached_realpath(path: Union[str, Any]) -> Union[str, Any]: ...


def get_fontext_synonyms(fontext: Union[str, Any]) -> list[str]: ...


def list_fonts(directory: Union[str, Any],
               extensions: Union[list[str], Any]) -> list[Union[bytes, str]]: ...


def win32FontDirectory() -> Union[str, Any]: ...


def _win32RegistryFonts(reg_domain: int,
                        base_dir: str) -> set: ...


def win32InstalledFonts(directory: Any = None,
                        fontext: str = 'ttf') -> list[str]: ...


def _call_fc_list() -> Union[list[Any], list[str]]: ...


def get_fontconfig_fonts(fontext: str = 'ttf') -> list[str]: ...


def findSystemFonts(fontpaths: Union[list[Path], Any] = None,
                    fontext: str = 'ttf') -> list[Union[Union[str, bytes], Any]]: ...


class FontEntry(object):
    def __init__(self: FontEntry,
                 fname: str = '',
                 name: str = '',
                 style: str = 'normal',
                 variant: str = 'normal',
                 weight: str = 'normal',
                 stretch: str = 'normal',
                 size: str = 'medium') -> None: ...

    def __repr__(self: FontEntry) -> str: ...


def ttfFontProperty(font: Any) -> FontEntry: ...


def afmFontProperty(fontpath: Any,
                    font: Any) -> FontEntry: ...


class FontProperties(object):
    def __init__(self: FontProperties,
                 family: Any = None,
                 style: Any = None,
                 variant: Any = None,
                 weight: Any = None,
                 stretch: Any = None,
                 size: Any = None,
                 fname: Any = None,
                 math_fontfamily: Any = None) -> None: ...

    def _from_any(cls: Type[FontProperties],
                  arg: Any) -> FontProperties: ...

    def __hash__(self: FontProperties) -> int: ...

    def __eq__(self: FontProperties,
               other: Any) -> bool: ...

    def __str__(self: FontProperties) -> str: ...

    def get_family(self: FontProperties) -> Optional[list[str]]: ...

    def get_name(self: FontProperties) -> object: ...

    def get_style(self: FontProperties) -> Optional[Any]: ...

    def get_variant(self: FontProperties) -> Optional[Any]: ...

    def get_weight(self: FontProperties) -> Optional[Any]: ...

    def get_stretch(self: FontProperties) -> Optional[Any]: ...

    def get_size(self: FontProperties) -> Optional[Any]: ...

    def get_size_in_points(self: FontProperties) -> Optional[Any]: ...

    def get_file(self: FontProperties) -> Any: ...

    def get_fontconfig_pattern(self: FontProperties) -> str: ...

    def set_family(self: FontProperties,
                   family: Union[str, Any]) -> None: ...

    def set_style(self: FontProperties,
                  style: Any) -> None: ...

    def set_variant(self: FontProperties,
                    variant: Any) -> None: ...

    def set_weight(self: FontProperties,
                   weight: Any) -> Any: ...

    def set_stretch(self: FontProperties,
                    stretch: Any) -> Any: ...

    def set_size(self: FontProperties,
                 size: Any) -> Any: ...

    def set_file(self: FontProperties,
                 file: Any) -> None: ...

    def set_fontconfig_pattern(self: FontProperties,
                               pattern: Union[str, Any]) -> None: ...

    def get_math_fontfamily(self: FontProperties) -> Any: ...

    def set_math_fontfamily(self: FontProperties,
                            fontfamily: str) -> None: ...

    def copy(self: FontProperties) -> FontProperties: ...


class _JSONEncoder(JSONEncoder):
    def default(self: _JSONEncoder,
                o: Any) -> Any: ...


def _json_decode(o: {pop}) -> Union[{pop}, FontManager, FontEntry]: ...


def json_dump(data: Union[FontManager, Any],
              filename: Union[Path, Any]) -> None: ...


def json_load(filename: Union[Path, Any]) -> Any: ...


def _normalize_font_family(family: Union[Optional[str], Any]) -> Optional[list[str]]: ...


class FontManager(object):
    def __init__(self: FontManager,
                 size: Any = None,
                 weight: str = 'normal') -> None: ...

    def addfont(self: FontManager,
                path: Any) -> None: ...

    def defaultFont(self: FontManager) -> dict: ...

    def get_default_weight(self: FontManager) -> str: ...

    def get_default_size() -> Optional[Any]: ...

    def set_default_weight(self: FontManager,
                           weight: Any) -> None: ...

    def _expand_aliases(family: Union[str, Any]) -> Optional[Any]: ...

    def score_family(self: FontManager,
                     families: Union[Optional[list[str]], Any],
                     family2: Any) -> float: ...

    def score_style(self: FontManager,
                    style1: Optional[Any],
                    style2: Any) -> float: ...

    def score_variant(self: FontManager,
                      variant1: Optional[Any],
                      variant2: Any) -> float: ...

    def score_stretch(self: FontManager,
                      stretch1: Optional[Any],
                      stretch2: Any) -> Union[float, Any]: ...

    def score_weight(self: FontManager,
                     weight1: Optional[Any],
                     weight2: Any) -> Union[float, Any]: ...

    def score_size(self: FontManager,
                   size1: Optional[Any],
                   size2: {__eq__}) -> Union[float, Any]: ...

    def findfont(self: FontManager,
                 prop: Any,
                 fontext: str = 'ttf',
                 directory: Optional[str] = None,
                 fallback_to_default: bool = True,
                 rebuild_if_missing: bool = True) -> str: ...

    def _findfont_cached(self: FontManager,
                         prop: Any,
                         fontext: {__eq__},
                         directory: Any,
                         fallback_to_default: Any,
                         rebuild_if_missing: Any,
                         rc_params: Any) -> Union[str, Any]: ...


def is_opentype_cff_font(filename: Any) -> bool: ...


def _get_font(filename: Union[str, Any],
              hinting_factor: Optional[Any],
              *,
              _kerning_factor: Optional[Any],
              thread_id: Union[int, Any]) -> FT2Font: ...


def get_font(filename: Union[str, Any],
             hinting_factor: Any = None) -> FT2Font: ...


def _load_fontmanager(*,
                      try_read_cache: bool = True) -> Union[FontManager, Any]: ...