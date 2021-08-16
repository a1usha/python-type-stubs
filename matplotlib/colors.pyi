from functools import partial
from typing import Any
from typing import Iterable
from typing import Optional
from typing import Type
from typing import Union

from matplotlib.colors import Colormap
from matplotlib.scale import FuncScale
from matplotlib.scale import SymmetricalLogScale
from numpy.core._multiarray_umath import ndarray
from numpy.ma.core import MaskedArray


class _ColorMapping(dict):
    def __init__(self: _ColorMapping,
                 mapping: Any) -> None: ...

    def __setitem__(self: _ColorMapping,
                    key: Any,
                    value: Any) -> None: ...

    def __delitem__(self: _ColorMapping,
                    key: Any) -> None: ...


def get_named_colors_mapping() -> Union[dict, _ColorMapping]: ...


def _sanitize_extrema(ex: Optional[float]) -> Optional[float]: ...


def _is_nth_color(c: Any) -> Union[bool, Match[str], None]: ...


def is_color_like(c: Any) -> bool: ...


def _check_color_like(**kwargs) -> Any: ...


def same_color(c1: Any,
               c2: Any) -> bool: ...


def to_rgba(c: Any,
            alpha: Optional[float] = None) -> tuple: ...


def _to_rgba_no_colorcycle(c: {__len__},
                           alpha: Optional[float] = None) -> Union[
    tuple[float, float, float, float], tuple[float, ...], tuple[Any, ...]]: ...


def to_rgba_array(c: Any,
                  alpha: Union[float, Iterable, None] = None) -> array.pyi: ...


def to_rgb(c: Any) -> Union[_T_co, tuple[_T_co, ...]]: ...


def to_hex(c: ndarray,
           keep_alpha: bool = False) -> str: ...


class ColorConverter(object):
    pass


def _create_lookup_table(N: int,
                         data: int,
                         gamma: float = 1.0) -> array.pyi: ...


def _warn_if_global_cmap_modified(cmap: Colormap) -> None: ...


class Colormap(object):
    def __init__(self: Colormap,
                 name: str,
                 N: int = 256) -> None: ...

    def __call__(self: Colormap,
                 X: Union[float, int, ndarray, complex],
                 alpha: Union[float, ndarray, Iterable, int, None] = None,
                 bytes: bool = False) -> Union[tuple, ndarray]: ...

    def __copy__(self: Colormap) -> Colormap: ...

    def get_bad(self: Colormap) -> ndarray: ...

    def set_bad(self: Colormap,
                color: str = 'k',
                alpha: Any = None) -> None: ...

    def get_under(self: Colormap) -> ndarray: ...

    def set_under(self: Colormap,
                  color: str = 'k',
                  alpha: Any = None) -> None: ...

    def get_over(self: Colormap) -> ndarray: ...

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

    def is_gray(self: Colormap) -> Union[ndarray, bool]: ...

    def _resample(self: Colormap,
                  lutsize: Any) -> Any: ...

    def reversed(self: Colormap,
                 name: Optional[str] = None) -> Any: ...

    def _repr_png_(self: Colormap) -> bytes: ...

    def _repr_html_(self: Colormap) -> str: ...

    def copy(self: Colormap) -> Colormap: ...


class LinearSegmentedColormap(Colormap):
    def __init__(self: LinearSegmentedColormap,
                 name: str,
                 segmentdata: Any,
                 N: int = 256,
                 gamma: float = 1.0) -> None: ...

    def _init(self: LinearSegmentedColormap) -> None: ...

    def set_gamma(self: LinearSegmentedColormap,
                  gamma: Any) -> None: ...

    @staticmethod
    def from_list(name: str,
                  colors: Any,
                  N: int = 256,
                  gamma: float = 1.0) -> LinearSegmentedColormap: ...

    def _resample(self: LinearSegmentedColormap,
                  lutsize: Any) -> LinearSegmentedColormap: ...

    @staticmethod
    def _reverser(func: Any,
                  x: Any) -> Any: ...

    def reversed(self: LinearSegmentedColormap,
                 name: Optional[str] = None) -> LinearSegmentedColormap: ...


class ListedColormap(Colormap):
    def __init__(self: ListedColormap,
                 colors: Union[Iterable, ndarray, int, float],
                 name: Optional[str] = 'from_list',
                 N: Optional[int] = None) -> None: ...

    def _init(self: ListedColormap) -> None: ...

    def _resample(self: ListedColormap,
                  lutsize: Any) -> ListedColormap: ...

    def reversed(self: ListedColormap,
                 name: Optional[str] = None) -> ListedColormap: ...


class Normalize(object):
    def __init__(self: Normalize,
                 vmin: Optional[float] = None,
                 vmax: Optional[float] = None,
                 clip: bool = False) -> None: ...

    @staticmethod
    def process_value(value: Optional[float]) -> Any: ...

    def __call__(self: Normalize,
                 value: Any,
                 clip: bool = None) -> Optional[Any]: ...

    def inverse(self: Normalize,
                value: Any) -> MaskedConstant: ...

    def autoscale(self: Normalize,
                  A: MaskedArray) -> None: ...

    def autoscale_None(self: Normalize,
                       A: MaskedArray) -> None: ...

    def scaled(self: Normalize) -> Any: ...


class TwoSlopeNorm(Normalize):
    def __init__(self: TwoSlopeNorm,
                 vcenter: float,
                 vmin: Optional[float] = None,
                 vmax: Optional[float] = None) -> Any: ...

    def autoscale_None(self: TwoSlopeNorm,
                       A: MaskedArray) -> None: ...

    def __call__(self: TwoSlopeNorm,
                 value: Any,
                 clip: bool = None) -> None: ...


class CenteredNorm(Normalize):
    def __init__(self: CenteredNorm,
                 vcenter: float = 0,
                 halfrange: Optional[float] = None,
                 clip: bool = False) -> None: ...

    def _set_vmin_vmax(self: CenteredNorm) -> None: ...

    def autoscale(self: CenteredNorm,
                  A: MaskedArray) -> None: ...

    def autoscale_None(self: CenteredNorm,
                       A: MaskedArray) -> None: ...

    @property
    def vcenter(self: CenteredNorm) -> float: ...

    @vcenter.setter
    def vcenter(self: CenteredNorm,
                vcenter: Any) -> None: ...

    @property
    def halfrange(self: CenteredNorm) -> float: ...

    @halfrange.setter
    def halfrange(self: CenteredNorm,
                  halfrange: Any) -> None: ...

    def __call__(self: CenteredNorm,
                 value: Any,
                 clip: bool = None) -> Optional[Any]: ...


def _make_norm_from_scale(scale_cls: Union[Type[FuncScale], partial[LogScale], Type[SymmetricalLogScale]],
                          base_norm_cls: Optional[{__name__, __qualname__, __module__}] = None,
                          *,
                          init: Union[(functions: Any, vmin: Any, vmax: Any, clip: Any)) -> Union[
    partial, Type[Norm]]: ...


@_make_norm_from_scale(
    scale.FuncScale,
    init=lambda functions, vmin=None, vmax=None, clip=False: None)
class FuncNorm(Normalize):
    pass


@_make_norm_from_scale(functools.partial(scale.LogScale, nonpositive="mask"))
class LogNorm(Normalize):
    def autoscale(self: LogNorm,
                  A: MaskedArray) -> None: ...

    def autoscale_None(self: LogNorm,
                       A: MaskedArray) -> None: ...


@_make_norm_from_scale(
    scale.SymmetricalLogScale,
    init=lambda linthresh, linscale=1., vmin=None, vmax=None, clip=False, *,
                base=10: None)
class SymLogNorm(Normalize):
    @property
    def linthresh(self: SymLogNorm) -> Any: ...

    @linthresh.setter
    def linthresh(self: SymLogNorm,
                  value: Any) -> None: ...


class PowerNorm(Normalize):
    def __init__(self: PowerNorm,
                 gamma: Any,
                 vmin: Optional[float] = None,
                 vmax: Optional[float] = None,
                 clip: bool = False) -> None: ...

    def __call__(self: PowerNorm,
                 value: Any,
                 clip: bool = None) -> Optional[Any]: ...

    def inverse(self: PowerNorm,
                value: Any) -> float: ...


class BoundaryNorm(Normalize):
    def __init__(self: BoundaryNorm,
                 boundaries: Union[ndarray, Iterable, int, float],
                 ncolors: int,
                 clip: Optional[bool] = False,
                 *,
                 extend: str = 'neither') -> Any: ...

    def __call__(self: BoundaryNorm,
                 value: Any,
                 clip: bool = None) -> Optional[int]: ...

    def inverse(self: BoundaryNorm,
                value: Any) -> Any: ...


class NoNorm(Normalize):
    def __call__(self: NoNorm,
                 value: Any,
                 clip: bool = None) -> Any: ...

    def inverse(self: NoNorm,
                value: Any) -> Any: ...


def rgb_to_hsv(arr: Union[ndarray, Iterable, int, float]) -> Any: ...


def hsv_to_rgb(hsv: Union[ndarray, Iterable, int, float]) -> Any: ...


def _vector_magnitude(arr: Optional[Any]) -> None: ...


class LightSource(object):
    def __init__(self: LightSource,
                 azdeg: float = 315,
                 altdeg: float = 45,
                 hsv_min_val: int = 0,
                 hsv_max_val: int = 1,
                 hsv_min_sat: int = 1,
                 hsv_max_sat: int = 0) -> None: ...

    @property
    def direction(self: LightSource) -> ndarray: ...

    def hillshade(self: LightSource,
                  elevation: int,
                  vert_exag: Union[int, float, complex, None] = 1,
                  dx: Union[int, float, complex, None] = 1,
                  dy: Union[int, float, complex, None] = 1,
                  fraction: Union[int, float, complex, None] = 1.) -> Any: ...

    def shade_normals(self: LightSource,
                      normals: Optional[Any],
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
                  rgb: Union[ndarray, Iterable, int, float],
                  elevation: Union[ndarray, Iterable, int, float],
                  fraction: Union[int, float, complex] = 1.,
                  blend_mode: Optional[str] = 'hsv',
                  vert_exag: Union[int, float, complex, None] = 1,
                  dx: Union[int, float, complex, None] = 1,
                  dy: Union[int, float, complex, None] = 1,
                  **kwargs) -> Any: ...

    def blend_hsv(self: LightSource,
                  rgb: ndarray,
                  intensity: ndarray,
                  hsv_max_sat: Union[int, float, complex] = None,
                  hsv_max_val: Union[int, float, complex, None] = None,
                  hsv_min_val: Union[int, float, complex, None] = None,
                  hsv_min_sat: Union[int, float, complex, None] = None) -> Any: ...

    def blend_soft_light(self: LightSource,
                         rgb: ndarray,
                         intensity: ndarray) -> Any: ...

    def blend_overlay(self: LightSource,
                      rgb: ndarray,
                      intensity: ndarray) -> Any: ...


def from_levels_and_colors(levels: Iterable[numbers.pyi],
                           colors: Iterable,
                           extend: Optional[str] = 'neither') -> Any: ...