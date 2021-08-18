from typing import Any
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
from numpy.core._multiarray_umath import ndarray
from numpy.ma.core import MaskedConstant
from object import object


def _set_ticks_on_axis_warn(*args,
                            **kwargs) -> None: ...


class _ColorbarAutoLocator(MaxNLocator):
    def __init__(self: _ColorbarAutoLocator,
                 colorbar: Any) -> None: ...

    def tick_values(self: _ColorbarAutoLocator,
                    vmin: {__gt__},
                    vmax: Any) -> Any: ...


class _ColorbarAutoMinorLocator(AutoMinorLocator):
    def __init__(self: _ColorbarAutoMinorLocator,
                 colorbar: Any,
                 n: Any = None) -> None: ...

    def __call__(self: _ColorbarAutoMinorLocator) -> Union[list[Any], Any]: ...


class _ColorbarLogLocator(LogLocator):
    def __init__(self: _ColorbarLogLocator,
                 colorbar: Any,
                 *args,
                 **kwargs) -> None: ...

    def tick_values(self: _ColorbarLogLocator,
                    vmin: {__le__},
                    vmax: {__lt__}) -> None: ...


class _ColorbarSpine(Spine):
    def __init__(self: _ColorbarSpine,
                 axes: Any) -> None: ...

    def get_window_extent(self: _ColorbarSpine,
                          renderer: Any = None) -> Any: ...

    def set_xy(self: _ColorbarSpine,
               xy: Any) -> None: ...

    def draw(self: _ColorbarSpine,
             renderer: {open_group, new_gc, draw_path, close_group}) -> Any: ...


class ColorbarBase(object):
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
                  levels: Union[Union[ndarray, int, float], Any],
                  colors: Union[list[colors.py], Any],
                  linewidths: Union[Union[float, ndarray, int], Any],
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
                               default: float = 0.05) -> ndarray: ...

    def _uniform_y(self: ColorbarBase,
                   N: Union[int, Any]) -> Union[ndarray, Tuple[ndarray, Optional[float]]]: ...

    def _proportional_y(self: ColorbarBase) -> Union[ndarray, Any]: ...

    def _mesh(self: ColorbarBase) -> Tuple[Any, Any]: ...

    def _locate(self: ColorbarBase,
                x: Union[Union[ndarray, int, float, None], Any]) -> Any: ...

    def set_alpha(self: ColorbarBase,
                  alpha: Any) -> None: ...

    def remove(self: ColorbarBase) -> None: ...


def _add_disjoint_kwargs(d: Union[dict[str, Any], Any],
                         **kwargs) -> None: ...


class Colorbar(ColorbarBase):
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