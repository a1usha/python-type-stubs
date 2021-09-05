from colors import crayons as crayons
from colors import xkcd_rgb as xkcd_rgb
from utils import get_color_cycle as get_color_cycle
from utils import desaturate as desaturate
from external import husl as husl
from itertools import cycle as cycle
from typing import Any
from typing import Tuple
from typing import Union

from list import list
from seaborn.palettes import _ColorPalette

SEABORN_PALETTES: dict[str, list[str]]
MPL_QUAL_PALS: dict[Union[str, Any], Union[int, Any]]
QUAL_PALETTE_SIZES: dict[Union[str, Any], Union[int, Any]]
QUAL_PALETTES: list[Union[str, Any]]
__all__: Any


class _ColorPalette(list):
    _orig_palette: Union[Union[_ColorPalette[Any], list[Any], list, _ColorPalette[tuple[float, float, float]],
                               _ColorPalette[tuple]], Any]

    def __enter__(self: _ColorPalette) -> _ColorPalette: ...

    def __exit__(self: _ColorPalette,
                 *args) -> None: ...

    def as_hex(self: _ColorPalette) -> _ColorPalette[Any]: ...

    def _repr_html_(self: _ColorPalette) -> str: ...


def color_palette(palette: Any = None,
                  n_colors: Any = None,
                  desat: Any = None,
                  as_cmap: bool = False) -> Union[Union[_ColorPalette[Any], list[Any], list, _ColorPalette[
    Tuple[float, float, float]], _ColorPalette[Tuple]], Any]: ...


def hls_palette(n_colors: int = 6,
                h: float = .01,
                l: float = .6,
                s: float = .65,
                as_cmap: bool = False) -> Union[_ColorPalette[Tuple[float, float, float]], Any]: ...


def husl_palette(n_colors: int = 6,
                 h: float = .01,
                 s: float = .9,
                 l: float = .65,
                 as_cmap: bool = False) -> Union[_ColorPalette[Any], Any]: ...


def mpl_palette(name: str,
                n_colors: int = 6,
                as_cmap: bool = False) -> Union[_ColorPalette[Tuple], Any]: ...


def _color_to_rgb(color: Union[Union[tuple[Any, float, float], tuple[Any, Union[float, Any], int]], Any],
                  input: Union[str, Any]) -> Any: ...


def dark_palette(color: Any,
                 n_colors: Any = 6,
                 reverse: Any = False,
                 as_cmap: Any = False,
                 input: Any = "rgb") -> Union[_ColorPalette[Tuple], Any]: ...


def light_palette(color: Any,
                  n_colors: Any = 6,
                  reverse: Any = False,
                  as_cmap: Any = False,
                  input: Any = "rgb") -> Union[_ColorPalette[Tuple], Any]: ...


def diverging_palette(h_neg: Any,
                      h_pos: Any,
                      s: Any = 75,
                      l: Any = 50,
                      sep: Any = 1,
                      n: Any = 6,
                      center: Any = "light",
                      as_cmap: Any = False) -> Union[_ColorPalette[Tuple], Any]: ...


def blend_palette(colors: Any,
                  n_colors: Any = 6,
                  as_cmap: Any = False,
                  input: str = "rgb") -> Union[_ColorPalette[Tuple], Any]: ...


def xkcd_palette(colors: list) -> Any: ...


def crayon_palette(colors: list) -> Any: ...


def cubehelix_palette(n_colors: int = 6,
                      start: Any = 0,
                      rot: float = .4,
                      gamma: Any = 1.0,
                      hue: Any = 0.8,
                      light: Any = .85,
                      dark: Any = .15,
                      reverse: bool = False,
                      as_cmap: bool = False) -> Union[_ColorPalette[Any], Any]: ...


def _parse_cubehelix_args(argstr: {startswith, endswith, split}) -> Union[
    Tuple[list[Any], dict[str, bool]], Tuple[list[float], dict]]: ...


def set_color_codes(palette: Any = "deep") -> Any: ...