from builtins import str
from numbers import Integral
from typing import Any
from typing import Iterable
from typing import Optional
from typing import Union
from typing import tuple

from numpy.core._multiarray_umath import ndarray


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
                     values: Any) -> list: ...

    def format_data(self: Formatter,
                    value: Any) -> Any: ...

    def format_data_short(self: Formatter,
                          value: Any) -> Any: ...

    def get_offset(self: Formatter) -> str: ...

    def set_locs(self: Formatter,
                 locs: Any) -> None: ...

    @staticmethod
    def fix_minus(s: Union[str, str, int]) -> Union[str, str, int]: ...

    def _set_locator(self: Formatter,
                     locator: Any) -> None: ...


class Locator(TickHelper):
    def tick_values(self: Locator,
                    vmin: Any,
                    vmax: Any) -> Any: ...

    def set_params(self: Locator,
                   **kwargs) -> None: ...

    def __call__(self: Locator) -> Any: ...

    def raise_if_exceeds(self: Locator,
                         locs: Union[ndarray, None, tuple[ndarray, Optional[float]], int, float, Iterable]) -> Union[
        ndarray, None, tuple[ndarray, Optional[float]], int, float, Iterable]: ...

    def nonsingular(self: Locator,
                    v0: Any,
                    v1: Any) -> float: ...

    def view_limits(self: Locator,
                    vmin: Any,
                    vmax: Any) -> float: ...

    @_api.deprecated
    def pan(self: Locator,
            numsteps: Any) -> Optional[Any]: ...

    @_api.deprecated
    def zoom(self: Locator,
             direction: Any) -> Optional[Any]: ...

    @_api.deprecated
    def refresh(self: Locator) -> Optional[Any]: ...


class NullFormatter(Formatter):
    def __call__(self: NullFormatter,
                 x: Any,
                 pos: Any = None) -> str: ...


class FixedLocator(Locator):
    def __init__(self: FixedLocator,
                 locs: Any,
                 nbins: Any = None) -> None: ...

    def set_params(self: FixedLocator,
                   nbins: Any = None) -> None: ...

    def __call__(self: FixedLocator) -> ndarray: ...

    def tick_values(self: FixedLocator,
                    vmin: Any,
                    vmax: Any) -> ndarray: ...


class MaxNLocator(Locator):
    def __init__(self: MaxNLocator,
                 *args,
                 **kwargs) -> Any: ...

    @staticmethod
    def _validate_steps(steps: Any) -> ndarray: ...

    @staticmethod
    def _staircase(steps: ndarray) -> ndarray: ...

    def set_params(self: MaxNLocator,
                   **kwargs) -> Any: ...

    def _raw_ticks(self: MaxNLocator,
                   vmin: {__sub__},
                   vmax: {__sub__, __add__}) -> Union[int, float]: ...

    def __call__(self: MaxNLocator) -> Any: ...

    def tick_values(self: MaxNLocator,
                    vmin: Union[{__lt__}, {__le__}, float, {__le__}, {__gt__, __ge__}],
                    vmax: Union[float, int, {__gt__, __ge__}, {__le__}]) -> Any: ...

    def view_limits(self: MaxNLocator,
                    dmin: Any,
                    dmax: Any) -> tuple[Any, Any]: ...


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
                       vmax: Any) -> str: ...

    def __call__(self: LogFormatter,
                 x: {__eq__},
                 pos: Any = None) -> str: ...

    def format_data(self: LogFormatter,
                    value: Any) -> {__len__, __getitem__}: ...

    def format_data_short(self: LogFormatter,
                          value: Any) -> str: ...

    def _pprint_val(self: LogFormatter,
                    x: float,
                    d: {__lt__, __le__}) -> str: ...


class LogFormatterMathtext(LogFormatter):
    def _non_decade_format(self: LogFormatterMathtext,
                           sign_string: str,
                           base: Any,
                           fx: Any,
                           usetex: Any) -> str: ...

    def __call__(self: LogFormatterMathtext,
                 x: {__eq__},
                 pos: Any = None) -> str: ...


class LogFormatterSciNotation(LogFormatterMathtext):
    def _non_decade_format(self: LogFormatterSciNotation,
                           sign_string: str,
                           base: Any,
                           fx: {__sub__},
                           usetex: Any) -> str: ...


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
                       x: {__truediv__}) -> float: ...

    @property
    def symbol(self: PercentFormatter) -> str: ...

    @symbol.setter
    def symbol(self: PercentFormatter,
               symbol: Any) -> None: ...


class LogitFormatter(Formatter):
    def __init__(self: LogitFormatter,
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
                      x: Union[{__le__, __ge__, __lt__, __gt__}, int],
                      locs: Optional[ndarray],
                      sci_notation: bool = True) -> str: ...

    def _one_minus(self: LogitFormatter,
                   s: str) -> str: ...

    def __call__(self: LogitFormatter,
                 x: {__le__, __ge__, __lt__, __gt__},
                 pos: Any = None) -> str: ...

    def format_data_short(self: LogitFormatter,
                          value: {__lt__}) -> str: ...


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


class EngFormatter(Formatter):
    def __init__(self: EngFormatter,
                 unit: str = "",
                 places: int = None,
                 sep: str = " ",
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


class LogFormatterExponent(LogFormatter):
    def _num_to_string(self: LogFormatterExponent,
                       x: {__gt__, __lt__},
                       vmin: Any,
                       vmax: Any) -> str: ...


class LinearLocator(Locator):
    def __init__(self: LinearLocator,
                 numticks: Any = None,
                 presets: Any = None) -> None: ...

    @property
    def numticks(self: LinearLocator) -> int: ...

    @numticks.setter
    def numticks(self: LinearLocator,
                 numticks: Any) -> None: ...

    def set_params(self: LinearLocator,
                   numticks: Any = None,
                   presets: Any = None) -> None: ...

    def __call__(self: LinearLocator) -> list: ...

    def tick_values(self: LinearLocator,
                    vmin: Any,
                    vmax: Any) -> list: ...

    def view_limits(self: LinearLocator,
                    vmin: {__eq__},
                    vmax: {__lt__}) -> float: ...


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


class OldScalarFormatter(Formatter):
    def __call__(self: OldScalarFormatter,
                 x: {__eq__},
                 pos: Any = None) -> str: ...


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
             base: float) -> None: ...

    def subs(self: LogLocator,
             subs: Union[None, str, Iterable[float]]) -> Any: ...

    def __call__(self: LogLocator) -> Optional[ndarray]: ...

    def tick_values(self: LogLocator,
                    vmin: {__le__},
                    vmax: {__lt__}) -> Optional[ndarray]: ...

    def view_limits(self: LogLocator,
                    vmin: Any,
                    vmax: Any) -> tuple[Union[float, int, {__le__}, {__gt__}, {__lt__}], Union[float, int]]: ...

    def nonsingular(self: LogLocator,
                    vmin: {__gt__},
                    vmax: {__le__}) -> tuple[Union[int, float, {__gt__}], Union[int, float]]: ...


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


class FormatStrFormatter(Formatter):
    def __init__(self: FormatStrFormatter,
                 fmt: Any) -> None: ...

    def __call__(self: FormatStrFormatter,
                 x: Any,
                 pos: Any = None) -> Any: ...


class NullLocator(Locator):
    def __call__(self: NullLocator) -> list: ...

    def tick_values(self: NullLocator,
                    vmin: Any,
                    vmax: Any) -> list: ...


class ScalarFormatter(Formatter):
    def __init__(self: ScalarFormatter,
                 useOffset: Union[bool, float] = None,
                 useMathText: bool = None,
                 useLocale: bool = None) -> None: ...

    def get_useOffset(self: ScalarFormatter) -> Union[bool, float]: ...

    def set_useOffset(self: ScalarFormatter,
                      val: Union[bool, float]) -> None: ...

    def get_useLocale(self: ScalarFormatter) -> Optional[bool]: ...

    def set_useLocale(self: ScalarFormatter,
                      val: Optional[bool]) -> None: ...

    def _format_maybe_minus_and_locale(self: ScalarFormatter,
                                       fmt: str,
                                       arg: Union[Integral, {mask}, int]) -> Any: ...

    def get_useMathText(self: ScalarFormatter) -> Optional[Any]: ...

    def set_useMathText(self: ScalarFormatter,
                        val: Optional[bool]) -> None: ...

    def __call__(self: ScalarFormatter,
                 x: Any,
                 pos: Any = None) -> str: ...

    def set_scientific(self: ScalarFormatter,
                       b: Any) -> None: ...

    def set_powerlimits(self: ScalarFormatter,
                        lims: tuple[int, int]) -> Any: ...

    def format_data_short(self: ScalarFormatter,
                          value: {mask}) -> str: ...

    def format_data(self: ScalarFormatter,
                    value: int) -> str: ...

    def get_offset(self: ScalarFormatter) -> str: ...

    def set_locs(self: ScalarFormatter,
                 locs: Any) -> None: ...

    def _compute_offset(self: ScalarFormatter) -> None: ...

    def _set_order_of_magnitude(self: ScalarFormatter) -> None: ...

    def _set_format(self: ScalarFormatter) -> None: ...


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


class SymmetricalLogLocator(Locator):
    def __init__(self: SymmetricalLogLocator,
                 transform: Any = None,
                 subs: Iterable[float] = None,
                 linthresh: Optional[float] = None,
                 base: Optional[float] = None) -> Any: ...

    def set_params(self: SymmetricalLogLocator,
                   subs: Any = None,
                   numticks: Any = None) -> None: ...

    def __call__(self: SymmetricalLogLocator) -> list[Union[{__lt__, __gt__}, {__lt__}]]: ...

    def tick_values(self: SymmetricalLogLocator,
                    vmin: {__lt__},
                    vmax: {__lt__, __gt__}) -> list[Union[{__lt__, __gt__}, {__lt__}]]: ...

    def view_limits(self: SymmetricalLogLocator,
                    vmin: Any,
                    vmax: {__lt__}) -> float: ...


class AutoMinorLocator(Locator):
    def __init__(self: AutoMinorLocator,
                 n: Any = None) -> None: ...

    def __call__(self: AutoMinorLocator) -> list: ...

    def tick_values(self: AutoMinorLocator,
                    vmin: Any,
                    vmax: Any) -> Any: ...


class LogitLocator(MaxNLocator):
    def __init__(self: LogitLocator,
                 minor: bool = False,
                 nbins: Any = "auto") -> None: ...

    def set_params(self: LogitLocator,
                   minor: Any = None,
                   **kwargs) -> None: ...

    @property
    def minor(self: LogitLocator) -> bool: ...

    @minor.setter
    def minor(self: LogitLocator,
              value: Any) -> None: ...

    def tick_values(self: LogitLocator,
                    vmin: Union[{__lt__}, {__le__}],
                    vmax: Union[{__le__}, {__lt__}]) -> list: ...

    def nonsingular(self: LogitLocator,
                    vmin: {__gt__, __ge__},
                    vmax: Union[{__le__}, {__lt__}]) -> tuple[Union[float, {__le__}, {__lt__}, {__gt__, __ge__}], Union[
        float, int, {__gt__, __ge__}, {__le__}, {__lt__}]]: ...


class _Edge_integer(object):
    def __init__(self: _Edge_integer,
                 step: {__le__},
                 offset: Any) -> Any: ...

    def closeto(self: _Edge_integer,
                ms: {__sub__},
                edge: int) -> bool: ...

    def le(self: _Edge_integer,
           x: Union[int, float]) -> int: ...

    def ge(self: _Edge_integer,
           x: Union[{__lt__, __sub__}, int, float]) -> int: ...


class AutoLocator(MaxNLocator):
    def __init__(self: AutoLocator) -> None: ...


class IndexFormatter(Formatter):
    def __init__(self: IndexFormatter,
                 labels: Iterable) -> None: ...

    def __call__(self: IndexFormatter,
                 x: {__add__},
                 pos: Any = None) -> str: ...


class FixedFormatter(Formatter):
    def __init__(self: FixedFormatter,
                 seq: Any) -> None: ...

    def __call__(self: FixedFormatter,
                 x: Any,
                 pos: Optional[{__ge__}] = None) -> str: ...

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


class StrMethodFormatter(Formatter):
    def __init__(self: StrMethodFormatter,
                 fmt: Any) -> None: ...

    def __call__(self: StrMethodFormatter,
                 x: Any,
                 pos: Any = None) -> Any: ...


def _decade_greater_equal(x: Union[float, int, {__gt__}, {__le__}, {__lt__}],
                          base: float) -> Union[float, int, {__gt__}, {__le__}, {__lt__}]: ...


def is_decade(x: int,
              base: int = 10,
              rtol: float = 1e-10) -> bool: ...


def _decade_less(x: Union[float, {__gt__}],
                 base: float) -> Union[float, int]: ...


def _decade_greater(x: Union[float, {__le__}],
                    base: float) -> Union[float, int]: ...


def _if_refresh_overridden_call_and_emit_deprec(locator: {refresh}) -> None: ...


def is_close_to_int(x: Union[float, int],
                    atol: float = 1e-10) -> bool: ...


def _decade_less_equal(x: Union[float, int, {__le__}, {__gt__}, {__lt__}],
                       base: float) -> Union[float, int, {__le__}, {__gt__}, {__lt__}]: ...


def scale_range(vmin: {__sub__},
                vmax: {__sub__, __add__},
                n: int = 1,
                threshold: int = 100) -> tuple[float, Union[int, float]]: ...