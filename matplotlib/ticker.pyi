from builtins import str
from numbers import Integral
from typing import Any
from typing import Iterable
from typing import Optional
from typing import Tuple
from typing import Union

from matplotlib import _api
from matplotlib.ticker import AutoLocator
from matplotlib.ticker import AutoMinorLocator
from matplotlib.ticker import EngFormatter
from matplotlib.ticker import FixedFormatter
from matplotlib.ticker import FixedLocator
from matplotlib.ticker import FormatStrFormatter
from matplotlib.ticker import Formatter
from matplotlib.ticker import FuncFormatter
from matplotlib.ticker import IndexFormatter
from matplotlib.ticker import IndexLocator
from matplotlib.ticker import LinearLocator
from matplotlib.ticker import Locator
from matplotlib.ticker import LogFormatter
from matplotlib.ticker import LogFormatterExponent
from matplotlib.ticker import LogFormatterMathtext
from matplotlib.ticker import LogFormatterSciNotation
from matplotlib.ticker import LogLocator
from matplotlib.ticker import LogitFormatter
from matplotlib.ticker import LogitLocator
from matplotlib.ticker import MaxNLocator
from matplotlib.ticker import MultipleLocator
from matplotlib.ticker import NullFormatter
from matplotlib.ticker import NullLocator
from matplotlib.ticker import OldAutoLocator
from matplotlib.ticker import OldScalarFormatter
from matplotlib.ticker import PercentFormatter
from matplotlib.ticker import ScalarFormatter
from matplotlib.ticker import StrMethodFormatter
from matplotlib.ticker import SymmetricalLogLocator
from matplotlib.ticker import TickHelper
from matplotlib.ticker import _DummyAxis
from matplotlib.ticker import _Edge_integer
from numpy.core._multiarray_umath import ndarray
from object import object


class _DummyAxis(object):
    def __init__(self: _DummyAxis,
                 minpos: int = 0) -> None: ...

    def get_view_interval(self: _DummyAxis) -> Any: ...

    def set_view_interval(self: _DummyAxis,
                          vmin: Any,
                          vmax: Any) -> None: ...

    def get_minpos(self: _DummyAxis) -> int: ...

    def get_data_interval(self: _DummyAxis) -> Any: ...

    def set_data_interval(self: _DummyAxis,
                          vmin: Any,
                          vmax: Any) -> None: ...

    def get_tick_space(self: _DummyAxis) -> int: ...


class TickHelper(object):
    def set_axis(self: TickHelper,
                 axis: Any) -> None: ...

    def create_dummy_axis(self: TickHelper,
                          **kwargs) -> None: ...

    def set_view_interval(self: TickHelper,
                          vmin: Any,
                          vmax: Any) -> None: ...

    def set_data_interval(self: TickHelper,
                          vmin: Any,
                          vmax: Any) -> None: ...

    def set_bounds(self: TickHelper,
                   vmin: Any,
                   vmax: Any) -> None: ...


class Formatter(TickHelper):
    def __call__(self: Formatter,
                 x: Any,
                 pos: Any = None) -> Any: ...

    def format_ticks(self: Formatter,
                     values: Any) -> list[Any]: ...

    def format_data(self: Formatter,
                    value: Any) -> Any: ...

    def format_data_short(self: Formatter,
                          value: Any) -> Any: ...

    def get_offset(self: Formatter) -> str: ...

    def set_locs(self: Formatter,
                 locs: Any) -> None: ...

    def fix_minus(s: Union[Union[str, str, int], Any]) -> Union[Union[str, str, int], Any]: ...

    def _set_locator(self: Formatter,
                     locator: Any) -> None: ...


@_api.deprecated("3.3")
class IndexFormatter(Formatter):
    def __init__(self: IndexFormatter,
                 labels: Iterable) -> None: ...

    def __call__(self: IndexFormatter,
                 x: {__add__},
                 pos: Any = None) -> Union[str, Any]: ...


class NullFormatter(Formatter):
    def __call__(self: NullFormatter,
                 x: Any,
                 pos: Any = None) -> str: ...


class FixedFormatter(Formatter):
    def __init__(self: FixedFormatter,
                 seq: Any) -> None: ...

    def __call__(self: FixedFormatter,
                 x: Any,
                 pos: Optional[{__ge__}] = None) -> Union[str, Any]: ...

    def get_offset(self: FixedFormatter) -> str: ...

    def set_offset_string(self: FixedFormatter,
                          ofs: Any) -> None: ...


class FuncFormatter(Formatter):
    def __init__(self: FuncFormatter,
                 func: Any) -> None: ...

    def __call__(self: FuncFormatter,
                 x: Any,
                 pos: Any = None) -> Any: ...

    def get_offset(self: FuncFormatter) -> str: ...

    def set_offset_string(self: FuncFormatter,
                          ofs: Any) -> None: ...


class FormatStrFormatter(Formatter):
    def __init__(self: FormatStrFormatter,
                 fmt: Any) -> None: ...

    def __call__(self: FormatStrFormatter,
                 x: Any,
                 pos: Any = None) -> Any: ...


class StrMethodFormatter(Formatter):
    def __init__(self: StrMethodFormatter,
                 fmt: Any) -> None: ...

    def __call__(self: StrMethodFormatter,
                 x: Any,
                 pos: Any = None) -> Any: ...


@_api.deprecated("3.3")
class OldScalarFormatter(Formatter):
    def __call__(self: OldScalarFormatter,
                 x: {__eq__},
                 pos: Any = None) -> Union[str, Any]: ...


class ScalarFormatter(Formatter):
    def __init__(self: ScalarFormatter,
                 useOffset: Union[bool, float] = None,
                 useMathText: bool = None,
                 useLocale: bool = None) -> None: ...

    def get_useOffset(self: ScalarFormatter) -> Union[bool, float]: ...

    def set_useOffset(self: ScalarFormatter,
                      val: Union[bool, float]) -> None: ...

    def get_useLocale(self: ScalarFormatter) -> Union[Optional[bool], Any]: ...

    def set_useLocale(self: ScalarFormatter,
                      val: Optional[bool]) -> None: ...

    def _format_maybe_minus_and_locale(self: ScalarFormatter,
                                       fmt: Union[str, Any],
                                       arg: Union[Union[Integral, {mask}, int], Any]) -> Any: ...

    def get_useMathText(self: ScalarFormatter) -> Optional[Any]: ...

    def set_useMathText(self: ScalarFormatter,
                        val: Optional[bool]) -> None: ...

    def __call__(self: ScalarFormatter,
                 x: Any,
                 pos: Any = None) -> Union[str, Any]: ...

    def set_scientific(self: ScalarFormatter,
                       b: Any) -> None: ...

    def set_powerlimits(self: ScalarFormatter,
                        lims: tuple[int, int]) -> Any: ...

    def format_data_short(self: ScalarFormatter,
                          value: {mask}) -> Union[str, Any]: ...

    def format_data(self: ScalarFormatter,
                    value: Union[int, Any]) -> Union[str, Any]: ...

    def get_offset(self: ScalarFormatter) -> Union[str, Any]: ...

    def set_locs(self: ScalarFormatter,
                 locs: Any) -> None: ...

    def _compute_offset(self: ScalarFormatter) -> None: ...

    def _set_order_of_magnitude(self: ScalarFormatter) -> None: ...

    def _set_format(self: ScalarFormatter) -> None: ...


class LogFormatter(Formatter):
    def __init__(self: LogFormatter,
                 base: float = 10.0,
                 labelOnlyBase: bool = False,
                 minor_thresholds: int = None,
                 linthresh: Optional[float] = None) -> None: ...

    def base(self: LogFormatter,
             base: Any) -> None: ...

    def label_minor(self: LogFormatter,
                    labelOnlyBase: bool) -> None: ...

    def set_locs(self: LogFormatter,
                 locs: Any = None) -> None: ...

    def _num_to_string(self: LogFormatter,
                       x: {__gt__, __lt__},
                       vmin: Any,
                       vmax: Any) -> Union[str, Any]: ...

    def __call__(self: LogFormatter,
                 x: {__eq__},
                 pos: Any = None) -> Union[str, Any]: ...

    def format_data(self: LogFormatter,
                    value: {__eq__}) -> Union[{__len__, __getitem__}, Any]: ...

    def format_data_short(self: LogFormatter,
                          value: Any) -> Union[str, Any]: ...

    def _pprint_val(self: LogFormatter,
                    x: Union[Union[{__gt__, __lt__}, float], Any],
                    d: Union[float, Any]) -> Union[str, Any]: ...


class LogFormatterExponent(LogFormatter):
    def _num_to_string(self: LogFormatterExponent,
                       x: {__gt__, __lt__},
                       vmin: Any,
                       vmax: Any) -> Union[str, Any]: ...


class LogFormatterMathtext(LogFormatter):
    def _non_decade_format(self: LogFormatterMathtext,
                           sign_string: Union[str, Any],
                           base: Any,
                           fx: Any,
                           usetex: Any) -> str: ...

    def __call__(self: LogFormatterMathtext,
                 x: {__eq__},
                 pos: Any = None) -> str: ...


class LogFormatterSciNotation(LogFormatterMathtext):
    def _non_decade_format(self: LogFormatterSciNotation,
                           sign_string: Union[str, Any],
                           base: Any,
                           fx: {__sub__},
                           usetex: Any) -> str: ...


class LogitFormatter(Formatter):
    def __init__(self: LogitFormatter,
                 *,
                 use_overline: bool = False,
                 one_half: str = r"\frac{1}{2}",
                 minor: bool = False,
                 minor_threshold: int = 25,
                 minor_number: int = 6) -> None: ...

    def use_overline(self: LogitFormatter,
                     use_overline: bool) -> None: ...

    def set_one_half(self: LogitFormatter,
                     one_half: Any) -> None: ...

    def set_minor_threshold(self: LogitFormatter,
                            minor_threshold: int) -> None: ...

    def set_minor_number(self: LogitFormatter,
                         minor_number: int) -> None: ...

    def set_locs(self: LogitFormatter,
                 locs: {__len__}) -> None: ...

    def _format_value(self: LogitFormatter,
                      x: Union[Union[{__le__, __ge__, __lt__, __gt__}, int], Any],
                      locs: Union[Optional[ndarray], Any],
                      sci_notation: bool = True) -> str: ...

    def _one_minus(self: LogitFormatter,
                   s: Union[str, Any]) -> Union[str, Any]: ...

    def __call__(self: LogitFormatter,
                 x: {__le__, __ge__, __lt__, __gt__},
                 pos: Any = None) -> Union[str, Any]: ...

    def format_data_short(self: LogitFormatter,
                          value: {__lt__}) -> str: ...


class EngFormatter(Formatter):
    def __init__(self: EngFormatter,
                 unit: str = "",
                 places: int = None,
                 sep: str = " ",
                 *,
                 usetex: bool = None,
                 useMathText: bool = None) -> None: ...

    def get_usetex(self: EngFormatter) -> Optional[Any]: ...

    def set_usetex(self: EngFormatter,
                   val: Any) -> None: ...

    def get_useMathText(self: EngFormatter) -> Optional[Any]: ...

    def set_useMathText(self: EngFormatter,
                        val: Any) -> None: ...

    def __call__(self: EngFormatter,
                 x: {__lt__, __ne__},
                 pos: Any = None) -> Any: ...

    def format_eng(self: EngFormatter,
                   num: {__lt__, __ne__}) -> str: ...


class PercentFormatter(Formatter):
    def __init__(self: PercentFormatter,
                 xmax: float = 100,
                 decimals: Optional[int] = None,
                 symbol: Optional[str] = '%',
                 is_latex: bool = False) -> None: ...

    def __call__(self: PercentFormatter,
                 x: Any,
                 pos: Any = None) -> Any: ...

    def format_pct(self: PercentFormatter,
                   x: Any,
                   display_range: Any) -> str: ...

    def convert_to_pct(self: PercentFormatter,
                       x: {__truediv__}) -> Union[float, Any]: ...

    def symbol(self: PercentFormatter) -> str: ...

    def symbol(self: PercentFormatter,
               symbol: Any) -> None: ...


def _if_refresh_overridden_call_and_emit_deprec(locator: {refresh}) -> None: ...


class Locator(TickHelper):
    def tick_values(self: Locator,
                    vmin: Any,
                    vmax: Any) -> Any: ...

    def set_params(self: Locator,
                   **kwargs) -> None: ...

    def __call__(self: Locator) -> Any: ...

    def raise_if_exceeds(self: Locator,
                         locs: Union[
                             Union[ndarray, None, tuple[ndarray, Optional[float]], int, float, Iterable], Any]) -> \
    Union[Union[ndarray, None, Tuple[ndarray, Optional[float]], int, float, Iterable], Any]: ...

    def nonsingular(self: Locator,
                    v0: Any,
                    v1: Any) -> float: ...

    def view_limits(self: Locator,
                    vmin: Any,
                    vmax: Any) -> float: ...

    @_api.deprecated("3.3")
    def pan(self: Locator,
            numsteps: Any) -> Optional[Any]: ...

    @_api.deprecated("3.3")
    def zoom(self: Locator,
             direction: Any) -> Optional[Any]: ...

    @_api.deprecated("3.3")
    def refresh(self: Locator) -> Optional[Any]: ...


class IndexLocator(Locator):
    def __init__(self: IndexLocator,
                 base: Any,
                 offset: Any) -> None: ...

    def set_params(self: IndexLocator,
                   base: Any = None,
                   offset: Any = None) -> None: ...

    def __call__(self: IndexLocator) -> Any: ...

    def tick_values(self: IndexLocator,
                    vmin: {__add__},
                    vmax: {__add__}) -> Any: ...


class FixedLocator(Locator):
    def __init__(self: FixedLocator,
                 locs: Any,
                 nbins: Any = None) -> None: ...

    def set_params(self: FixedLocator,
                   nbins: Any = None) -> None: ...

    def __call__(self: FixedLocator) -> Union[ndarray, Any]: ...

    def tick_values(self: FixedLocator,
                    vmin: Optional[Any],
                    vmax: Any) -> Union[ndarray, Any]: ...


class NullLocator(Locator):
    def __call__(self: NullLocator) -> list[Any]: ...

    def tick_values(self: NullLocator,
                    vmin: Optional[Any],
                    vmax: Any) -> list[Any]: ...


class LinearLocator(Locator):
    def __init__(self: LinearLocator,
                 numticks: Any = None,
                 presets: Any = None) -> None: ...

    def numticks(self: LinearLocator) -> Union[int, Any]: ...

    def numticks(self: LinearLocator,
                 numticks: Any) -> None: ...

    def set_params(self: LinearLocator,
                   numticks: Any = None,
                   presets: Any = None) -> None: ...

    def __call__(self: LinearLocator) -> Union[list[Any], Any]: ...

    def tick_values(self: LinearLocator,
                    vmin: Any,
                    vmax: Any) -> Union[list[Any], Any]: ...

    def view_limits(self: LinearLocator,
                    vmin: {__eq__},
                    vmax: {__lt__}) -> float: ...


class MultipleLocator(Locator):
    def __init__(self: MultipleLocator,
                 base: float = 1.0) -> None: ...

    def set_params(self: MultipleLocator,
                   base: Any) -> None: ...

    def __call__(self: MultipleLocator) -> Any: ...

    def tick_values(self: MultipleLocator,
                    vmin: Any,
                    vmax: {__lt__, __sub__}) -> Any: ...

    def view_limits(self: MultipleLocator,
                    dmin: Any,
                    dmax: Any) -> float: ...


def scale_range(vmin: Union[{__sub__}, Any],
                vmax: {__sub__, __add__},
                n: int = 1,
                threshold: int = 100) -> Tuple[float, Union[int, float]]: ...


class _Edge_integer(object):
    def __init__(self: _Edge_integer,
                 step: {__le__},
                 offset: Any) -> Any: ...

    def closeto(self: _Edge_integer,
                ms: {__sub__},
                edge: Union[int, Any]) -> Union[bool, Any]: ...

    def le(self: _Edge_integer,
           x: Union[Union[int, float], Any]) -> Union[int, Any]: ...

    def ge(self: _Edge_integer,
           x: Union[Union[{__lt__, __sub__}, int, float], Any]) -> Union[int, Any]: ...


class MaxNLocator(Locator):
    def __init__(self: MaxNLocator,
                 *args,
                 **kwargs) -> Any: ...

    def _validate_steps(steps: Any) -> ndarray: ...

    def _staircase(steps: Union[ndarray, Any]) -> ndarray: ...

    def set_params(self: MaxNLocator,
                   **kwargs) -> Any: ...

    def _raw_ticks(self: MaxNLocator,
                   vmin: {__sub__},
                   vmax: {__sub__, __add__}) -> Union[Union[int, float], Any]: ...

    def __call__(self: MaxNLocator) -> Any: ...

    def tick_values(self: MaxNLocator,
                    vmin: Union[Union[{__lt__}, {__le__}, float, {__le__}, {__gt__, __ge__}], Any],
                    vmax: Union[Union[{__le__}, {__lt__}, float, int, {__gt__, __ge__}, {__le__}], Any]) -> Any: ...

    def view_limits(self: MaxNLocator,
                    dmin: Any,
                    dmax: Any) -> Union[Tuple[Any, Any], Any]: ...


def is_decade(x: Union[int, Any],
              base: int = 10,
              *,
              rtol: float = 1e-10) -> Union[bool, Any]: ...


def _decade_less_equal(x: Union[Union[float, int, {__le__}, {__gt__}, {__lt__}], Any],
                       base: Union[float, Any]) -> Union[Union[float, int, {__le__}, {__gt__}, {__lt__}], Any]: ...


def _decade_greater_equal(x: Union[Union[float, int, {__gt__}, {__le__}, {__lt__}], Any],
                          base: Union[float, Any]) -> Union[Union[float, int, {__gt__}, {__le__}, {__lt__}], Any]: ...


def _decade_less(x: Union[Union[float, {__gt__}], Any],
                 base: Union[float, Any]) -> Union[Union[float, int], Any]: ...


def _decade_greater(x: Union[Union[float, {__le__}], Any],
                    base: Union[float, Any]) -> Union[Union[float, int], Any]: ...


def is_close_to_int(x: Union[Union[float, int], Any],
                    *,
                    atol: float = 1e-10) -> Union[bool, Any]: ...


class LogLocator(Locator):
    def __init__(self: LogLocator,
                 base: float = 10.0,
                 subs: Union[None, str, Iterable[float]] = (1.0,),
                 numdecs: int = 4,
                 numticks: Optional[int] = None) -> None: ...

    def set_params(self: LogLocator,
                   base: Any = None,
                   subs: Any = None,
                   numdecs: Any = None,
                   numticks: Any = None) -> None: ...

    def base(self: LogLocator,
             base: Union[float, Any]) -> None: ...

    def subs(self: LogLocator,
             subs: Union[Union[None, str, Iterable[float]], Any]) -> Any: ...

    def __call__(self: LogLocator) -> Union[Optional[ndarray], Any]: ...

    def tick_values(self: LogLocator,
                    vmin: {__le__},
                    vmax: {__lt__}) -> Union[Optional[ndarray], Any]: ...

    def view_limits(self: LogLocator,
                    vmin: Any,
                    vmax: Any) -> Tuple[
        Union[Union[float, int, {__le__}, {__gt__}, {__lt__}], Any], Union[Union[float, int], Any]]: ...

    def nonsingular(self: LogLocator,
                    vmin: {__gt__},
                    vmax: {__le__}) -> Tuple[Union[Union[int, float, {__le__}, {__gt__}], Any], Union[
        Union[int, float, {__gt__}, {__le__}, {__lt__}], Any]]: ...


class SymmetricalLogLocator(Locator):
    def __init__(self: SymmetricalLogLocator,
                 transform: Any = None,
                 subs: Iterable[float] = None,
                 linthresh: Optional[float] = None,
                 base: Optional[float] = None) -> Any: ...

    def set_params(self: SymmetricalLogLocator,
                   subs: Any = None,
                   numticks: Any = None) -> None: ...

    def __call__(self: SymmetricalLogLocator) -> Union[list[Union[{__lt__, __gt__}, {__lt__}]], Any]: ...

    def tick_values(self: SymmetricalLogLocator,
                    vmin: {__lt__},
                    vmax: {__lt__, __gt__}) -> Union[list[Union[{__lt__, __gt__}, {__lt__}]], Any]: ...

    def view_limits(self: SymmetricalLogLocator,
                    vmin: Any,
                    vmax: {__lt__}) -> float: ...


class LogitLocator(MaxNLocator):
    def __init__(self: LogitLocator,
                 minor: bool = False,
                 *,
                 nbins: Any = "auto") -> None: ...

    def set_params(self: LogitLocator,
                   minor: Any = None,
                   **kwargs) -> None: ...

    def minor(self: LogitLocator) -> bool: ...

    def minor(self: LogitLocator,
              value: Any) -> None: ...

    def tick_values(self: LogitLocator,
                    vmin: Union[Union[{__lt__}, {__le__}], Any],
                    vmax: Union[Union[{__le__}, {__lt__}], Any]) -> Union[list[Any], Any]: ...

    def nonsingular(self: LogitLocator,
                    vmin: {__gt__, __ge__},
                    vmax: Union[Union[{__le__}, {__lt__}], Any]) -> Tuple[
        Union[Union[float, {__le__}, {__lt__}, {__gt__, __ge__}], Any], Union[
            Union[float, int, {__gt__, __ge__}, {__le__}, {__lt__}], Any]]: ...


class AutoLocator(MaxNLocator):
    def __init__(self: AutoLocator) -> None: ...


class AutoMinorLocator(Locator):
    def __init__(self: AutoMinorLocator,
                 n: Any = None) -> None: ...

    def __call__(self: AutoMinorLocator) -> Union[list[Any], Any]: ...

    def tick_values(self: AutoMinorLocator,
                    vmin: Any,
                    vmax: Any) -> Any: ...


@_api.deprecated("3.3")
class OldAutoLocator(Locator):
    def __call__(self: OldAutoLocator) -> Any: ...

    def tick_values(self: OldAutoLocator,
                    vmin: Any,
                    vmax: Any) -> Any: ...

    def view_limits(self: OldAutoLocator,
                    vmin: Any,
                    vmax: {__sub__}) -> float: ...

    def get_locator(self: OldAutoLocator,
                    d: Any) -> MultipleLocator: ...
