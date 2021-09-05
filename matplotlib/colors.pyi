from _color_data import XKCD_COLORS as XKCD_COLORS
from _color_data import CSS4_COLORS as CSS4_COLORS
from _color_data import TABLEAU_COLORS as TABLEAU_COLORS
from _color_data import BASE_COLORS as BASE_COLORS
from matplotlib import scale as scale
from matplotlib import cbook as cbook
from matplotlib import _api as _api
from PIL.PngImagePlugin import PngInfo as PngInfo
from PIL import Image as Image
from numbers import Number as Number
from collections.abc import Sequence as Sequence
from collections.abc import Sized as Sized
from functools import partial
from typing import Any
from typing import Callable
from typing import ClassVar
from typing import Iterable
from typing import Match
from typing import Optional
from typing import Tuple
from typing import Type
from typing import Union

from dict import dict
from matplotlib.colors import BoundaryNorm
from matplotlib.colors import CenteredNorm
from matplotlib.colors import Colormap
from matplotlib.colors import LightSource
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.colors import ListedColormap
from matplotlib.colors import LogNorm
from matplotlib.colors import NoNorm
from matplotlib.colors import Normalize
from matplotlib.colors import PowerNorm
from matplotlib.colors import SymLogNorm
from matplotlib.colors import TwoSlopeNorm
from matplotlib.colors import _ColorMapping
from matplotlib.scale import FuncScale
from matplotlib.scale import SymmetricalLogScale
from numpy.ma.core import MaskedArray
from numpy.ma.core import MaskedConstant
from numpy.ma.core import mvoid
from object import object


class _ColorMapping(dict):
    cache: dict[Any, Any]

    def __init__(self: _ColorMapping,
                 mapping: Any) -> None: ...

    def __setitem__(self: _ColorMapping,
                    key: Any,
                    value: Any) -> None: ...

    def __delitem__(self: _ColorMapping,
                    key: Any) -> None: ...


_colors_full_map: dict[Any, Any]
_colors_full_map: _ColorMapping
_colors_full_map: dict[Any, Any]
_colors_full_map: _ColorMapping
_REPR_PNG_SIZE: tuple[int, int]


def get_named_colors_mapping() -> Union[dict[Any, Any], _ColorMapping]: ...


def _sanitize_extrema(ex: Union[Optional[float], Any]) -> Union[Optional[float], Any]: ...


def _is_nth_color(c: Any) -> Union[bool, Match[str], None]: ...


def is_color_like(c: Any) -> bool: ...


def _check_color_like(**kwargs) -> Any: ...


def same_color(c1: Any,
               c2: Any) -> Union[bool, Any]: ...


def to_rgba(c: Any,
            alpha: Optional[float] = None) -> Tuple: ...


def _to_rgba_no_colorcycle(c: {__len__},
                           alpha: Union[Optional[float], Any] = None) -> Union[
    Tuple[float, float, float, float], Tuple[float, ...], Tuple[Union[float, int], ...]]: ...


def to_rgba_array(c: Any,
                  alpha: Union[float, Iterable, None] = None) -> array.pyi: ...


def to_rgb(c: Any) -> Union[Union[_T_co, Tuple[_T_co, ...]], Any]: ...


cnames: dict[Union[str, Any], Union[str, Any]]

hexColorPattern: Pattern[str]

rgb2hex: Callable[[Any, bool], str]

hex2color: Callable[[Any], Union[Union[_T_co, tuple[_T_co, ...]], Any]]


def to_hex(c: Any,
           keep_alpha: bool = False) -> str: ...


colorConverter: ColorConverter


class ColorConverter(object):
    colors: ClassVar[_ColorMapping]
    cache: ClassVar[dict[Any, Any]]
    to_rgb: ClassVar[staticmethod]
    to_rgba: ClassVar[staticmethod]
    to_rgba_array: ClassVar[staticmethod]
    pass


def _create_lookup_table(N: int,
                         data: int,
                         gamma: float = 1.0) -> array.pyi: ...


def _warn_if_global_cmap_modified(cmap: Union[Colormap, Any]) -> None: ...


class Colormap(object):
    _i_bad: int
    _rgba_bad: tuple[float, float, float, float]
    _i_over: int
    _rgba_under: None
    name: str
    _rgba_over: None
    _isinit: bool
    colorbar_extend: bool
    _i_under: int
    N: int

    def __init__(self: Colormap,
                 name: str,
                 N: int = 256) -> None: ...

    def __call__(self: Colormap,
                 X: Union[Union[float, int, complex], Any],
                 alpha: Union[Union[float, Iterable, int, None], Any] = None,
                 bytes: bool = False) -> Union[Tuple, Any]: ...

    def __copy__(self: Colormap) -> Colormap: ...

    def get_bad(self: Colormap) -> Any: ...

    def set_bad(self: Colormap,
                color: str = 'k',
                alpha: Any = None) -> None: ...

    def get_under(self: Colormap) -> Any: ...

    def set_under(self: Colormap,
                  color: str = 'k',
                  alpha: Any = None) -> None: ...

    def get_over(self: Colormap) -> Any: ...

    def set_over(self: Colormap,
                 color: str = 'k',
                 alpha: Any = None) -> None: ...

    def set_extremes(self: Colormap,
                     *,
                     bad: Any = None,
                     under: Any = None,
                     over: Any = None) -> None: ...

    def with_extremes(self: Colormap,
                      *,
                      bad: Any = None,
                      under: Any = None,
                      over: Any = None) -> Colormap: ...

    def _set_extremes(self: Colormap) -> None: ...

    def _init(self: Colormap) -> Any: ...

    def is_gray(self: Colormap) -> bool: ...

    def _resample(self: Colormap,
                  lutsize: Any) -> Any: ...

    def reversed(self: Colormap,
                 name: Optional[str] = None) -> Any: ...

    def _repr_png_(self: Colormap) -> bytes: ...

    def _repr_html_(self: Colormap) -> str: ...

    def copy(self: Colormap) -> Colormap: ...


class LinearSegmentedColormap(Colormap):
    _lut: Any
    monochrome: bool
    _segmentdata: Any
    _isinit: bool
    _gamma: float

    def __init__(self: LinearSegmentedColormap,
                 name: str,
                 segmentdata: Any,
                 N: int = 256,
                 gamma: float = 1.0) -> None: ...

    def _init(self: LinearSegmentedColormap) -> None: ...

    def set_gamma(self: LinearSegmentedColormap,
                  gamma: Any) -> None: ...

    def from_list(name: str,
                  colors: Any,
                  N: int = 256,
                  gamma: float = 1.0) -> LinearSegmentedColormap: ...

    def _resample(self: LinearSegmentedColormap,
                  lutsize: Any) -> LinearSegmentedColormap: ...

    def _reverser(func: Any,
                  x: Any) -> Any: ...

    def reversed(self: LinearSegmentedColormap,
                 name: Optional[str] = None) -> LinearSegmentedColormap: ...


class ListedColormap(Colormap):
    _lut: Any
    monochrome: bool
    _isinit: bool
    colors: list[float]

    def __init__(self: ListedColormap,
                 colors: Union[Union[Iterable, int, float], Any],
                 name: Optional[str] = 'from_list',
                 N: Optional[int] = None) -> None: ...

    def _init(self: ListedColormap) -> None: ...

    def _resample(self: ListedColormap,
                  lutsize: Any) -> ListedColormap: ...

    def reversed(self: ListedColormap,
                 name: Optional[str] = None) -> ListedColormap: ...


class Normalize(object):
    _scale: LinearScale
    vmax: Union[Optional[float], Any]
    vmin: Union[Optional[float], Any]
    clip: bool

    def __init__(self: Normalize,
                 vmin: Optional[float] = None,
                 vmax: Optional[float] = None,
                 clip: bool = False) -> None: ...

    def process_value(value: Union[Optional[float], Any]) -> Any: ...

    def __call__(self: Normalize,
                 value: Any,
                 clip: bool = None) -> Union[Union[mvoid, MaskedArray, MaskedConstant], Any]: ...

    def inverse(self: Normalize,
                value: Any) -> Union[MaskedConstant, Any]: ...

    def autoscale(self: Normalize,
                  A: Union[MaskedArray, Any]) -> None: ...

    def autoscale_None(self: Normalize,
                       A: Union[MaskedArray, Any]) -> None: ...

    def scaled(self: Normalize) -> Any: ...


class TwoSlopeNorm(Normalize):
    vcenter: float
    vmax: Optional[float]
    vmin: Optional[float]

    def __init__(self: TwoSlopeNorm,
                 vcenter: float,
                 vmin: Optional[float] = None,
                 vmax: Optional[float] = None) -> Any: ...

    def autoscale_None(self: TwoSlopeNorm,
                       A: Union[MaskedArray, Any]) -> None: ...

    def __call__(self: TwoSlopeNorm,
                 value: Any,
                 clip: bool = None) -> Union[MaskedArray, Any]: ...


class CenteredNorm(Normalize):
    halfrange: Optional[float]
    _halfrange: Union[float, Any]
    vmax: None
    vmin: None
    _vcenter: float
    clip: bool

    def __init__(self: CenteredNorm,
                 vcenter: float = 0,
                 halfrange: Optional[float] = None,
                 clip: bool = False) -> None: ...

    def _set_vmin_vmax(self: CenteredNorm) -> None: ...

    def autoscale(self: CenteredNorm,
                  A: Union[MaskedArray, Any]) -> None: ...

    def autoscale_None(self: CenteredNorm,
                       A: Union[MaskedArray, Any]) -> None: ...

    def vcenter(self: CenteredNorm) -> float: ...

    def vcenter(self: CenteredNorm,
                vcenter: Any) -> None: ...

    def halfrange(self: CenteredNorm) -> Union[float, Any]: ...

    def halfrange(self: CenteredNorm,
                  halfrange: Any) -> None: ...

    def __call__(self: CenteredNorm,
                 value: Any,
                 clip: bool = None) -> Union[Union[mvoid, MaskedArray, MaskedConstant], Any]: ...


def _make_norm_from_scale(scale_cls: Union[Union[Type[FuncScale], partial[LogScale], Type[SymmetricalLogScale]], Any],
                          base_norm_cls: Optional[{__name__, __qualname__, __module__, __doc__}] = None,
                          *,
                          init: Union[Union[Callable[[Any, Any, Any, Any], None], Callable[
                              [Any, Any, Any, Any, Any, Any, Any], None]], Any] = None) -> Union[
    partial[Any], Type[Norm]]: ...


class FuncNorm(Normalize):
    pass


class LogNorm(Normalize):
    def autoscale(self: LogNorm,
                  A: Union[MaskedArray, Any]) -> None: ...

    def autoscale_None(self: LogNorm,
                       A: Union[MaskedArray, Any]) -> None: ...


class SymLogNorm(Normalize):
    def linthresh(self: SymLogNorm) -> Any: ...

    def linthresh(self: SymLogNorm,
                  value: Any) -> None: ...


class PowerNorm(Normalize):
    gamma: Any

    def __init__(self: PowerNorm,
                 gamma: Any,
                 vmin: Optional[float] = None,
                 vmax: Optional[float] = None,
                 clip: bool = False) -> None: ...

    def __call__(self: PowerNorm,
                 value: Any,
                 clip: bool = None) -> Union[Union[mvoid, MaskedArray, MaskedConstant], Any]: ...

    def inverse(self: PowerNorm,
                value: Any) -> Union[float, Any]: ...


class BoundaryNorm(Normalize):
    extend: str
    _scale: None
    _offset: int
    vmax: Any
    boundaries: Any
    _n_regions: int
    vmin: Any
    clip: Optional[bool]
    N: int
    Ncmap: int

    def __init__(self: BoundaryNorm,
                 boundaries: Union[Union[Iterable, int, float], Any],
                 ncolors: int,
                 clip: Optional[bool] = False,
                 *,
                 extend: str = 'neither') -> Any: ...

    def __call__(self: BoundaryNorm,
                 value: Any,
                 clip: bool = None) -> Union[Union[int, MaskedArray], Any]: ...

    def inverse(self: BoundaryNorm,
                value: Any) -> Any: ...


class NoNorm(Normalize):
    def __call__(self: NoNorm,
                 value: Any,
                 clip: bool = None) -> Any: ...

    def inverse(self: NoNorm,
                value: Any) -> Any: ...


def rgb_to_hsv(arr: Union[Union[Iterable, int, float], Any]) -> Any: ...


def hsv_to_rgb(hsv: Union[Union[Iterable, int, float], Any]) -> Any: ...


def _vector_magnitude(arr: {shape, __getitem__}) -> Any: ...


class LightSource(object):
    hsv_min_val: int
    hsv_max_sat: int
    azdeg: float
    altdeg: float
    hsv_max_val: int
    hsv_min_sat: int

    def __init__(self: LightSource,
                 azdeg: float = 315,
                 altdeg: float = 45,
                 hsv_min_val: int = 0,
                 hsv_max_val: int = 1,
                 hsv_min_sat: int = 1,
                 hsv_max_sat: int = 0) -> None: ...

    def direction(self: LightSource) -> Any: ...

    def hillshade(self: LightSource,
                  elevation: int,
                  vert_exag: Union[int, float, complex, None] = 1,
                  dx: Union[int, float, complex, None] = 1,
                  dy: Union[int, float, complex, None] = 1,
                  fraction: Union[int, float, complex, None] = 1.) -> Any: ...

    def shade_normals(self: LightSource,
                      normals: {dot},
                      fraction: Union[int, float, complex, None] = 1.) -> Any: ...

    def shade(self: LightSource,
              data: int,
              cmap: Any,
              norm: Any = None,
              blend_mode: Optional[str] = 'overlay',
              vmin: Optional[float] = None,
              vmax: Optional[float] = None,
              vert_exag: Union[int, float, complex, None] = 1,
              dx: Union[int, float, complex, None] = 1,
              dy: Union[int, float, complex, None] = 1,
              fraction: Union[int, float, complex, None] = 1,
              **kwargs) -> Any: ...

    def shade_rgb(self: LightSource,
                  rgb: Union[Union[Iterable, int, float], Any],
                  elevation: Union[Union[Iterable, int, float], Any],
                  fraction: Union[int, float, complex] = 1.,
                  blend_mode: Optional[str] = 'hsv',
                  vert_exag: Union[int, float, complex, None] = 1,
                  dx: Union[int, float, complex, None] = 1,
                  dy: Union[int, float, complex, None] = 1,
                  **kwargs) -> Any: ...

    def blend_hsv(self: LightSource,
                  rgb: Any,
                  intensity: Any,
                  hsv_max_sat: Union[int, float, complex] = None,
                  hsv_max_val: Union[int, float, complex, None] = None,
                  hsv_min_val: Union[int, float, complex, None] = None,
                  hsv_min_sat: Union[int, float, complex, None] = None) -> Any: ...

    def blend_soft_light(self: LightSource,
                         rgb: Any,
                         intensity: Any) -> Any: ...

    def blend_overlay(self: LightSource,
                      rgb: Any,
                      intensity: Any) -> Any: ...


def from_levels_and_colors(levels: Iterable[numbers.pyi],
                           colors: Iterable,
                           extend: Optional[str] = 'neither') -> Any: ...