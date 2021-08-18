from datetime import datetime
from datetime import timedelta
from datetime import tzinfo
from typing import Iterable
from typing import Optional
from typing import Pattern
from typing import Tuple
from typing import Type
from typing import Union

from matplotlib import _api
from matplotlib.dates import AutoDateFormatter
from matplotlib.dates import AutoDateLocator
from matplotlib.dates import ConciseDateConverter
from matplotlib.dates import ConciseDateFormatter
from matplotlib.dates import DateConverter
from matplotlib.dates import DateFormatter
from matplotlib.dates import DateLocator
from matplotlib.dates import DayLocator
from matplotlib.dates import HourLocator
from matplotlib.dates import IndexDateFormatter
from matplotlib.dates import MicrosecondLocator
from matplotlib.dates import MinuteLocator
from matplotlib.dates import MonthLocator
from matplotlib.dates import RRuleLocator
from matplotlib.dates import SecondLocator
from matplotlib.dates import WeekdayLocator
from matplotlib.dates import YearLocator
from matplotlib.dates import _rcParam_helper
from matplotlib.dates import rrulewrapper
from matplotlib.ticker import Formatter
from matplotlib.ticker import Locator
from matplotlib.units import AxisInfo
from matplotlib.units import ConversionInterface
from numpy.core import datetime64
from numpy.core._multiarray_umath import ndarray
from object import object


def _get_rc_timezone() -> Optional[tzinfo]: ...


def _reset_epoch_test_example() -> None: ...


def set_epoch(epoch: str) -> Any: ...


def get_epoch() -> str: ...


def _dt64_to_ordinalf(d: ndarray) -> float: ...


def _from_ordinalf(x: {__mul__},
                   tz: Any = None) -> timedelta: ...


def datestr2num(d: Union[str, Iterable[str]],
                default: Optional[datetime] = None) -> Union[ndarray, float]: ...


def date2num(d: Union[datetime, datetime64]) -> Union[ndarray, float]: ...


def julian2num(j: Union[float, Iterable]) -> None: ...


def num2julian(n: Union[float, Iterable]) -> None: ...


def num2date(x: Union[float, Iterable],
             tz: str = None) -> Any: ...


def num2timedelta(x: Union[float, Iterable]) -> Union[timedelta, list[timedelta]]: ...


def drange(dstart: Any,
           dend: Any,
           delta: timedelta) -> Any: ...


def _wrap_in_tex(text: str) -> str: ...


class DateFormatter(Formatter):
    @_api.deprecated("3.3")
    def illegal_s(self: DateFormatter) -> Pattern[str]: ...

    def __init__(self: DateFormatter,
                 fmt: str,
                 tz: tzinfo = None,
                 *,
                 usetex: bool = None) -> None: ...

    def __call__(self: DateFormatter,
                 x: Any,
                 pos: int = 0) -> str: ...

    def set_tzinfo(self: DateFormatter,
                   tz: Any) -> None: ...


@_api.deprecated("3.3")
class IndexDateFormatter(Formatter):
    def __init__(self: IndexDateFormatter,
                 t: Iterable[float],
                 fmt: str,
                 tz: Any = None) -> None: ...

    def __call__(self: IndexDateFormatter,
                 x: Any,
                 pos: int = 0) -> str: ...


class ConciseDateFormatter(Formatter):
    def __init__(self: ConciseDateFormatter,
                 locator: Any,
                 tz: Any = None,
                 formats: Any = None,
                 offset_formats: Any = None,
                 zero_formats: Any = None,
                 show_offset: bool = True,
                 *,
                 usetex: Any = None) -> Any: ...

    def __call__(self: ConciseDateFormatter,
                 x: Any,
                 pos: Any = None) -> str: ...

    def format_ticks(self: ConciseDateFormatter,
                     values: Any) -> list[str]: ...

    def get_offset(self: ConciseDateFormatter) -> str: ...

    def format_data_short(self: ConciseDateFormatter,
                          value: Any) -> Any: ...


class AutoDateFormatter(Formatter):
    def __init__(self: AutoDateFormatter,
                 locator: Any,
                 tz: Optional[str] = None,
                 defaultfmt: str = '%Y-%m-%d',
                 *,
                 usetex: bool = None) -> None: ...

    def _set_locator(self: AutoDateFormatter,
                     locator: Any) -> None: ...

    def __call__(self: AutoDateFormatter,
                 x: Any,
                 pos: Any = None) -> str: ...


class rrulewrapper(object):
    def __init__(self: rrulewrapper,
                 freq: Any,
                 tzinfo: Any = None,
                 **kwargs) -> None: ...

    def set(self: rrulewrapper,
            **kwargs) -> None: ...

    def _update_rrule(self: rrulewrapper,
                      **kwargs) -> Any: ...

    def _attach_tzinfo(self: rrulewrapper,
                       dt: {replace},
                       tzinfo: Any) -> Any: ...

    def _aware_return_wrapper(self: rrulewrapper,
                              f: Any,
                              returns_list: bool = False) -> Union[(args: Tuple[Any, ...], kwargs: dict[str, Any]) ->

    def __getattr__(self: rrulewrapper,
                    name: Any) -> Union[(args: Tuple[Any, ...], kwargs: dict[str, Any]) ->

    def __setstate__(self: rrulewrapper,
                     state: Any) -> None: ...


class DateLocator(Locator):
    def __init__(self: DateLocator,
                 tz: tzinfo = None) -> None: ...

    def set_tzinfo(self: DateLocator,
                   tz: Any) -> None: ...

    def datalim_to_dt(self: DateLocator) -> Tuple[Any, Any]: ...

    def viewlim_to_dt(self: DateLocator) -> Tuple[Any, Any]: ...

    def _get_unit(self: DateLocator) -> int: ...

    def _get_interval(self: DateLocator) -> int: ...

    def nonsingular(self: DateLocator,
                    vmin: Any,
                    vmax: {__lt__, __sub__}) -> Union[
        Tuple[Union[ndarray, float], Union[ndarray, float]], Tuple[{__lt__, __sub__}, {__lt__, __sub__}]]: ...


class RRuleLocator(DateLocator):
    def __init__(self: RRuleLocator,
                 o: rrulewrapper,
                 tz: tzinfo = None) -> None: ...

    def __call__(self: RRuleLocator) -> Union[list, ndarray, float, {__len__}]: ...

    def tick_values(self: RRuleLocator,
                    vmin: {__gt__, year},
                    vmax: {__sub__, year}) -> Union[ndarray, float, {__len__}]: ...

    def _get_unit(self: RRuleLocator) -> Union[float, int]: ...

    def get_unit_generic(freq: int) -> Union[float, int]: ...

    def _get_interval(self: RRuleLocator) -> Any: ...


class AutoDateLocator(DateLocator):
    def __init__(self: AutoDateLocator,
                 tz: tzinfo = None,
                 minticks: int = 5,
                 maxticks: int = None,
                 interval_multiples: bool = True) -> None: ...

    def __call__(self: AutoDateLocator) -> Union[list, ndarray, float, {__len__}]: ...

    def tick_values(self: AutoDateLocator,
                    vmin: {__gt__, __sub__, year},
                    vmax: {__sub__, __add__, year}) -> Union[ndarray, float, {__len__}]: ...

    def nonsingular(self: AutoDateLocator,
                    vmin: {__eq__},
                    vmax: {__lt__, __sub__}) -> Union[Tuple[Union[ndarray, float], Union[ndarray, float]], Tuple[
        Union[float, {__lt__, __sub__}, {__eq__}], Union[float, {__lt__, __sub__}, {__eq__}]]]: ...

    def _get_unit(self: AutoDateLocator) -> Union[float, int]: ...

    def get_locator(self: AutoDateLocator,
                    dmin: {__sub__, year},
                    dmax: {__add__, year}) -> Union[RRuleLocator, YearLocator, MicrosecondLocator]: ...


class YearLocator(DateLocator):
    def __init__(self: YearLocator,
                 base: int = 1,
                 month: int = 1,
                 day: int = 1,
                 tz: tzinfo = None) -> None: ...

    def __call__(self: YearLocator) -> Union[list, ndarray, float]: ...

    def tick_values(self: YearLocator,
                    vmin: {__gt__, __sub__},
                    vmax: {year}) -> Union[ndarray, float]: ...


class MonthLocator(RRuleLocator):
    def __init__(self: MonthLocator,
                 bymonth: Any = None,
                 bymonthday: int = 1,
                 interval: int = 1,
                 tz: tzinfo = None) -> None: ...


class WeekdayLocator(RRuleLocator):
    def __init__(self: WeekdayLocator,
                 byweekday: int = 1,
                 interval: int = 1,
                 tz: tzinfo = None) -> None: ...


class DayLocator(RRuleLocator):
    def __init__(self: DayLocator,
                 bymonthday: Any = None,
                 interval: int = 1,
                 tz: tzinfo = None) -> Any: ...


class HourLocator(RRuleLocator):
    def __init__(self: HourLocator,
                 byhour: Any = None,
                 interval: int = 1,
                 tz: tzinfo = None) -> None: ...


class MinuteLocator(RRuleLocator):
    def __init__(self: MinuteLocator,
                 byminute: Any = None,
                 interval: int = 1,
                 tz: tzinfo = None) -> None: ...


class SecondLocator(RRuleLocator):
    def __init__(self: SecondLocator,
                 bysecond: Any = None,
                 interval: int = 1,
                 tz: tzinfo = None) -> None: ...


class MicrosecondLocator(DateLocator):
    def __init__(self: MicrosecondLocator,
                 interval: int = 1,
                 tz: tzinfo = None) -> None: ...

    def set_axis(self: MicrosecondLocator,
                 axis: Any) -> None: ...

    def set_view_interval(self: MicrosecondLocator,
                          vmin: Any,
                          vmax: Any) -> None: ...

    def set_data_interval(self: MicrosecondLocator,
                          vmin: Any,
                          vmax: Any) -> None: ...

    def __call__(self: MicrosecondLocator) -> Union[list, float]: ...

    def tick_values(self: MicrosecondLocator,
                    vmin: {__gt__, __sub__, year},
                    vmax: Any) -> float: ...

    def _get_unit(self: MicrosecondLocator) -> float: ...

    def _get_interval(self: MicrosecondLocator) -> int: ...


def epoch2num(e: Iterable) -> Any: ...


def num2epoch(d: Iterable) -> Any: ...


def date_ticker_factory(span: {__eq__, __mul__, __truediv__},
                        tz: Any = None,
                        numticks: int = 5) -> Tuple[
    Union[MinuteLocator, HourLocator, DayLocator, WeekdayLocator, MonthLocator, YearLocator], DateFormatter]: ...


class DateConverter(ConversionInterface):
    def __init__(self: DateConverter,
                 *,
                 interval_multiples: bool = True) -> None: ...

    def axisinfo(self: DateConverter,
                 unit: Any,
                 axis: Any) -> AxisInfo: ...

    def convert(value: Any,
                unit: Any,
                axis: Any) -> Union[ndarray, float]: ...

    def default_units(x: Any,
                      axis: Any) -> Optional[Any]: ...


class ConciseDateConverter(DateConverter):
    def __init__(self: ConciseDateConverter,
                 formats: Any = None,
                 zero_formats: Any = None,
                 offset_formats: Any = None,
                 show_offset: bool = True,
                 *,
                 interval_multiples: bool = True) -> None: ...

    def axisinfo(self: ConciseDateConverter,
                 unit: Any,
                 axis: Any) -> AxisInfo: ...


class _rcParam_helper(object):
    def set_converter(cls: Type[_rcParam_helper],
                      s: Any) -> Any: ...

    def set_int_mult(cls: Type[_rcParam_helper],
                     b: Any) -> None: ...

    def register_converters(cls: Type[_rcParam_helper]) -> None: ...
