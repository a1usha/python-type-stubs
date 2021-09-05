from matplotlib import docstring as docstring
from matplotlib import ticker as ticker
from matplotlib import contour as contour
from matplotlib import colors as colors
from matplotlib import cm as cm
from matplotlib import collections as collections
from matplotlib import _api as _api
from typing import Any
from typing import ClassVar
from typing import Optional
from typing import Tuple
from typing import Union

from matplotlib import _api
from matplotlib.colorbar import Colorbar
from matplotlib.colorbar import ColorbarBase
from matplotlib.colorbar import _ColorbarAutoLocator
from matplotlib.colorbar import _ColorbarAutoMinorLocator
from matplotlib.colorbar import _ColorbarLogLocator
from matplotlib.colorbar import _ColorbarSpine
from matplotlib.spines import Spine
from matplotlib.ticker import AutoMinorLocator
from matplotlib.ticker import LogFormatterSciNotation
from matplotlib.ticker import LogLocator
from matplotlib.ticker import MaxNLocator
from matplotlib.ticker import ScalarFormatter
from numpy.ma.core import MaskedConstant
from object import object

_make_axes_other_param_doc: str
_colormap_kw_doc: str
colorbar_doc: Any
colormap_kw_doc: str
make_axes_kw_doc: str
_make_axes_param_doc: str


def _set_ticks_on_axis_warn(*args,
                            **kwargs) -> None: ...


class _ColorbarAutoLocator(MaxNLocator):
    _colorbar: Any

    def __init__(self: _ColorbarAutoLocator,
                 colorbar: Any) -> None: ...

    def tick_values(self: _ColorbarAutoLocator,
                    vmin: {__gt__},
                    vmax: Any) -> Any: ...


class _ColorbarAutoMinorLocator(AutoMinorLocator):
    _colorbar: Any
    ndivs: Any

    def __init__(self: _ColorbarAutoMinorLocator,
                 colorbar: Any,
                 n: Any = None) -> None: ...

    def __call__(self: _ColorbarAutoMinorLocator) -> Union[list[Any], Any]: ...


class _ColorbarLogLocator(LogLocator):
    _colorbar: Any

    def __init__(self: _ColorbarLogLocator,
                 colorbar: Any,
                 *args,
                 **kwargs) -> None: ...

    def tick_values(self: _ColorbarLogLocator,
                    vmin: {__le__},
                    vmax: {__lt__}) -> Any: ...


class _ColorbarSpine(Spine):
    stale: bool
    _path: Path

    def __init__(self: _ColorbarSpine,
                 axes: Any) -> None: ...

    def get_window_extent(self: _ColorbarSpine,
                          renderer: Any = None) -> Any: ...

    def set_xy(self: _ColorbarSpine,
               xy: Any) -> None: ...

    def draw(self: _ColorbarSpine,
             renderer: {open_group, new_gc, draw_path, close_group}) -> Any: ...


class ColorbarBase(object):
    n_rasterize: ClassVar[int]
    values: Any
    _boundaries: Any
    dividers: LineCollection
    norm: Union[Normalize, Any]
    ticklocation: str
    patch: Polygon
    outline: _ColorbarSpine
    spacing: str
    stale: bool
    _values: Union[float, Any]
    alpha: float
    boundaries: Any
    extendfrac: Any
    vmax: Any
    lines: list[Any]
    _manual_tick_data_values: None
    drawedges: bool
    solids_patches: list[Any]
    orientation: str
    solids: None
    __scale: None
    extendrect: bool
    filled: bool
    vmin: Any
    extend: Union[str, Any]
    formatter: Any
    ax: Any
    cmap: Union[Union[Colormap, LinearSegmentedColormap, ListedColormap], Any]
    _y: Union[Union[MaskedConstant, tuple[Union[Optional[float], Any], ...]], Any]
    _inside: Any
    locator: Any

    @_api.make_keyword_only("3.3", "cmap")
    def __init__(self: ColorbarBase,
                 ax: Any,
                 cmap: Any = None,
                 norm: Any = None,
                 alpha: float = None,
                 values: Any = None,
                 boundaries: Any = None,
                 orientation: str = 'vertical',
                 ticklocation: str = 'auto',
                 extend: str = None,
                 spacing: str = 'uniform',
                 ticks: Any = None,
                 format: Any = None,
                 drawedges: bool = False,
                 filled: bool = True,
                 extendfrac: Any = None,
                 extendrect: bool = False,
                 label: str = '') -> Optional[Any]: ...

    def _extend_lower(self: ColorbarBase) -> bool: ...

    def _extend_upper(self: ColorbarBase) -> bool: ...

    def draw_all(self: ColorbarBase) -> None: ...

    @_api.deprecated("3.3")
    def config_axis(self: ColorbarBase) -> Optional[Any]: ...

    def _config_axis(self: ColorbarBase) -> None: ...

    def _get_ticker_locator_formatter(self: ColorbarBase) -> Tuple[Union[Union[
                                                                             SymmetricalLogLocator, _ColorbarLogLocator, FixedLocator, IndexLocator, MaxNLocator, _ColorbarAutoLocator], Any],
                                                                   Union[Union[
                                                                             LogFormatterSciNotation, ScalarFormatter], Any]]: ...

    def _use_auto_colorbar_locator(self: ColorbarBase) -> bool: ...

    def _reset_locator_formatter_scale(self: ColorbarBase) -> None: ...

    def update_ticks(self: ColorbarBase) -> None: ...

    def set_ticks(self: ColorbarBase,
                  ticks: Any,
                  update_ticks: bool = True) -> None: ...

    def get_ticks(self: ColorbarBase,
                  minor: bool = False) -> Any: ...

    def set_ticklabels(self: ColorbarBase,
                       ticklabels: Any,
                       update_ticks: bool = True) -> None: ...

    def minorticks_on(self: ColorbarBase) -> None: ...

    def minorticks_off(self: ColorbarBase) -> None: ...

    def set_label(self: ColorbarBase,
                  label: str,
                  *,
                  loc: Optional[str] = None,
                  **kwargs) -> None: ...

    def _add_solids(self: ColorbarBase,
                    X: Any,
                    Y: Any,
                    C: Any) -> None: ...

    def _add_solids_pcolormesh(self: ColorbarBase,
                               X: Any,
                               Y: {shape},
                               C: {shape}) -> None: ...

    def _add_solids_patches(self: ColorbarBase,
                            X: {__len__, __getitem__},
                            Y: {__getitem__},
                            C: {__len__, __getitem__},
                            mappable: {hatches}) -> None: ...

    def add_lines(self: ColorbarBase,
                  levels: Union[Union[int, float], Any],
                  colors: Union[list[colors.py], Any],
                  linewidths: Union[Union[float, int], Any],
                  erase: bool = True) -> None: ...

    def _ticker(self: ColorbarBase,
                locator: {create_dummy_axis, set_view_interval, set_data_interval},
                formatter: Union[Union[LogFormatterSciNotation, ScalarFormatter], Any]) -> Tuple[
        Any, list[Any], Union[Union[str, {replace}], Any]]: ...

    def _process_values(self: ColorbarBase,
                        b: Union[MaskedConstant, Any] = None) -> None: ...

    def _get_extension_lengths(self: ColorbarBase,
                               frac: Any,
                               automin: Any,
                               automax: Any,
                               default: float = 0.05) -> Any: ...

    def _uniform_y(self: ColorbarBase,
                   N: Union[int, Any]) -> Union[Tuple[Any, Optional[float]], Any]: ...

    def _proportional_y(self: ColorbarBase) -> Any: ...

    def _mesh(self: ColorbarBase) -> Tuple[Any, Any]: ...

    def _locate(self: ColorbarBase,
                x: Union[Union[int, float], Any]) -> Any: ...

    def set_alpha(self: ColorbarBase,
                  alpha: Any) -> None: ...

    def remove(self: ColorbarBase) -> None: ...


def _add_disjoint_kwargs(d: Union[dict[str, Any], Any],
                         **kwargs) -> None: ...


class Colorbar(ColorbarBase):
    formatter: None
    patch: Polygon
    outline: _ColorbarSpine
    stale: bool
    solids: None
    cmap: Any
    lines: list[Any]
    mappable: {get_array, cmap, norm, colorbar, colorbar_cid, callbacksSM}
    locator: None
    norm: Any

    def __init__(self: Colorbar,
                 ax: Any,
                 mappable: {get_array, cmap, norm, colorbar, colorbar_cid, callbacksSM},
                 **kwargs) -> None: ...

    @_api.deprecated("3.3", alternative="update_normal")
    def on_mappable_changed(self: Colorbar,
                            mappable: {norm, get_alpha, cmap}) -> Optional[Any]: ...

    def add_lines(self: Colorbar,
                  CS: Any,
                  erase: bool = True) -> Any: ...

    def update_normal(self: Colorbar,
                      mappable: {norm, get_alpha, cmap}) -> None: ...

    @_api.deprecated("3.3", alternative="update_normal")
    def update_bruteforce(self: Colorbar,
                          mappable: {norm, get_alpha, cmap}) -> Optional[Any]: ...

    def remove(self: Colorbar) -> None: ...


def _normalize_location_orientation(location: Any,
                                    orientation: Optional[{__ne__}]) -> Any: ...


def make_axes(parents: Any,
              location: Any = None,
              orientation: Any = None,
              fraction: float = 0.15,
              shrink: float = 1.0,
              aspect: int = 20,
              **kwargs) -> Any: ...


def make_axes_gridspec(parent: Any,
                       *,
                       location: Any = None,
                       orientation: Any = None,
                       fraction: float = 0.15,
                       shrink: float = 1.0,
                       aspect: int = 20,
                       **kwargs) -> Any: ...


@_api.deprecated("3.4", alternative="Colorbar")
class ColorbarPatch(Colorbar):
    pass


@_api.deprecated("3.4", alternative="Colorbar")
def colorbar_factory(cax: Any,
                     mappable: Any,
                     **kwargs) -> Any: ...