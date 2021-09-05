from matplotlib import units as units
from matplotlib import ticker as ticker
from matplotlib import cbook as cbook
from matplotlib import _api as _api
from dateutil.relativedelta import relativedelta as relativedelta
from dateutil.rrule import SECONDLY as SECONDLY
from dateutil.rrule import MINUTELY as MINUTELY
from dateutil.rrule import HOURLY as HOURLY
from dateutil.rrule import DAILY as DAILY
from dateutil.rrule import WEEKLY as WEEKLY
from dateutil.rrule import MONTHLY as MONTHLY
from dateutil.rrule import YEARLY as YEARLY
from dateutil.rrule import SU as SU
from dateutil.rrule import SA as SA
from dateutil.rrule import FR as FR
from dateutil.rrule import TH as TH
from dateutil.rrule import WE as WE
from dateutil.rrule import TU as TU
from dateutil.rrule import MO as MO
from dateutil.rrule import rrule as rrule
from datetime import datetime
from datetime import timedelta
from datetime import tzinfo
from typing import Any
from typing import Callable
from typing import ClassVar
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
from object import object

UTC: Any
__all__: Any

EPOCH_OFFSET: float

JULIAN_OFFSET: float

MICROSECONDLY: int

HOURS_PER_DAY: float

MIN_PER_HOUR: float

SEC_PER_MIN: float

MONTHS_PER_YEAR: float

DAYS_PER_WEEK: float

DAYS_PER_MONTH: float

DAYS_PER_YEAR: float

MINUTES_PER_DAY: float

SEC_PER_HOUR: float

SEC_PER_DAY: float

SEC_PER_WEEK: float

MUSECONDS_PER_DAY: float

WEEKDAYS: tuple[weekday, weekday, weekday, weekday, weekday, weekday, weekday]

_epoch: None


def _get_rc_timezone() -> Union[Optional[tzinfo], Any]: ...


def _reset_epoch_test_example() -> None: ...


def set_epoch(epoch: str) -> Any: ...


def get_epoch() -> str: ...


def _dt64_to_ordinalf(d: {astype, __sub__}) -> Union[float, Any]: ...


_from_ordinalf_np_vectorized: Callable

_dateutil_parser_parse_np_vectorized: Callable


def _from_ordinalf(x: {__mul__},
                   tz: Any = None) -> Union[timedelta, Any]: ...


def datestr2num(d: Union[str, Iterable[str]],
                default: Optional[datetime] = None) -> Union[float, Any]: ...


def date2num(d: Union[Union[datetime, datetime64], Any]) -> Union[float, Any]: ...


def julian2num(j: Union[float, Iterable]) -> Any: ...


def num2julian(n: Union[float, Iterable]) -> Any: ...


_ordinalf_to_timedelta_np_vectorized: Callable


def num2date(x: Union[float, Iterable],
             tz: str = None) -> Any: ...


def num2timedelta(x: Union[float, Iterable]) -> Union[timedelta, list[timedelta]]: ...


def drange(dstart: Any,
           dend: Any,
           delta: timedelta) -> Any: ...


def _wrap_in_tex(text: Union[str, Any]) -> str: ...


class DateFormatter(Formatter):
    _usetex: Union[Optional[bool], Any]
    tz: Union[Optional[tzinfo], Any]
    fmt: str

    @_api.deprecated("3.3")
    def illegal_s(self: DateFormatter) -> Pattern[str]: ...

    def __init__(self: DateFormatter,
                 fmt: str,
                 tz: tzinfo = None,
                 *,
                 usetex: bool = None) -> None: ...

    def __call__(self: DateFormatter,
                 x: Any,
                 pos: int = 0) -> Union[str, Any]: ...

    def set_tzinfo(self: DateFormatter,
                   tz: Any) -> None: ...


@_api.deprecated("3.3")
class IndexDateFormatter(Formatter):
    t: Iterable[float]
    tz: Union[Optional[tzinfo], Any]
    fmt: str

    def __init__(self: IndexDateFormatter,
                 t: Iterable[float],
                 fmt: str,
                 tz: Any = None) -> None: ...

    def __call__(self: IndexDateFormatter,
                 x: Any,
                 pos: int = 0) -> Union[str, Any]: ...


class ConciseDateFormatter(Formatter):
    formats: list[str]
    _tz: Any
    show_offset: bool
    _usetex: Optional[Any]
    zero_formats: Union[list[str], Any]
    _locator: Any
    offset_formats: list[str]
    defaultfmt: str
    offset_string: str

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
                 pos: Any = None) -> Union[str, Any]: ...

    def format_ticks(self: ConciseDateFormatter,
                     values: Any) -> list[str]: ...

    def get_offset(self: ConciseDateFormatter) -> str: ...

    def format_data_short(self: ConciseDateFormatter,
                          value: Any) -> Any: ...


class AutoDateFormatter(Formatter):
    _formatter: DateFormatter
    _tz: Optional[str]
    _usetex: Union[Optional[bool], Any]
    scaled: dict[Union[float, int], Optional[Any]]
    _locator: Any
    defaultfmt: str

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
                 pos: Any = None) -> Union[str, Any]: ...


class rrulewrapper(object):
    _construct: dict[str, Any]
    _rrule: rrule
    _base_tzinfo: Any
    _tzinfo: Any

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
                              returns_list: bool = False) -> Union[Union[
                                                                       Callable[[Tuple[Any, ...], dict[str, Any]], Any],
                                                                       Callable[[Tuple[Any, ...], dict[str, Any]], list[
                                                                           Any]]], Any]: ...

    def __getattr__(self: rrulewrapper,
                    name: Any) -> Union[Union[Callable[[Tuple[Any, ...], dict[str, Any]], Any], Callable[
        [Tuple[Any, ...], dict[str, Any]], list[Any]]], Any]: ...

    def __setstate__(self: rrulewrapper,
                     state: Any) -> None: ...


class DateLocator(Locator):
    hms0d: ClassVar[dict[str, int]]
    tz: Union[Optional[tzinfo], Any]

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
                    vmax: {__lt__, __sub__}) -> Union[Tuple[Union[float, Any], Union[float, Any]], Tuple[
        Union[{__lt__, __sub__}, Any], Union[{__lt__, __sub__}, Any]]]: ...


class RRuleLocator(DateLocator):
    rule: Union[rrulewrapper, Any]

    def __init__(self: RRuleLocator,
                 o: Union[rrulewrapper, Any],
                 tz: tzinfo = None) -> None: ...

    def __call__(self: RRuleLocator) -> Union[Union[list[Any], float, {__len__}], Any]: ...

    def tick_values(self: RRuleLocator,
                    vmin: Union[{__gt__, year}, Any],
                    vmax: Union[{__sub__, year}, Any]) -> Union[Union[float, {__len__}], Any]: ...

    def _get_unit(self: RRuleLocator) -> Union[float, int]: ...

    def get_unit_generic(freq: Union[int, Any]) -> Union[float, int]: ...

    def _get_interval(self: RRuleLocator) -> Any: ...


class AutoDateLocator(DateLocator):
    _byranges: list[Optional[range]]
    _freqs: list[int]
    minticks: int
    intervald: dict[int, Union[list[Union[int, Any]], list[int]]]
    interval_multiples: bool
    maxticks: dict[int, int]
    _freq: int

    def __init__(self: AutoDateLocator,
                 tz: tzinfo = None,
                 minticks: int = 5,
                 maxticks: int = None,
                 interval_multiples: bool = True) -> None: ...

    def __call__(self: AutoDateLocator) -> Union[Union[list[Any], float, {__len__}], Any]: ...

    def tick_values(self: AutoDateLocator,
                    vmin: {__gt__, __sub__, year},
                    vmax: {__sub__, __add__, year}) -> Union[Union[float, {__len__}], Any]: ...

    def nonsingular(self: AutoDateLocator,
                    vmin: {__eq__},
                    vmax: {__lt__, __sub__}) -> Union[Tuple[Union[float, Any], Union[float, Any]], Tuple[
        Union[float, {__lt__, __sub__}, {__eq__}], Union[float, {__lt__, __sub__}, {__eq__}]]]: ...

    def _get_unit(self: AutoDateLocator) -> Union[float, int]: ...

    def get_locator(self: AutoDateLocator,
                    dmin: Union[{__sub__, year}, Any],
                    dmax: Union[{__add__, year}, Any]) -> Union[RRuleLocator, YearLocator, MicrosecondLocator]: ...


class YearLocator(DateLocator):
    replaced: dict[str, Union[int, tzinfo]]
    base: _Edge_integer

    def __init__(self: YearLocator,
                 base: int = 1,
                 month: int = 1,
                 day: int = 1,
                 tz: tzinfo = None) -> None: ...

    def __call__(self: YearLocator) -> Union[Union[list[Any], float], Any]: ...

    def tick_values(self: YearLocator,
                    vmin: Union[{__gt__, __sub__}, Any],
                    vmax: {year}) -> Union[float, Any]: ...


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
    _interval: int
    tz: tzinfo
    _wrapped_locator: MultipleLocator

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

    def __call__(self: MicrosecondLocator) -> Union[Union[list[Any], float], Any]: ...

    def tick_values(self: MicrosecondLocator,
                    vmin: Union[{__gt__, __sub__, year}, Any],
                    vmax: Any) -> Union[float, Any]: ...

    def _get_unit(self: MicrosecondLocator) -> float: ...

    def _get_interval(self: MicrosecondLocator) -> int: ...


def epoch2num(e: Iterable) -> Any: ...


def num2epoch(d: Iterable) -> Any: ...


def date_ticker_factory(span: {__eq__, __mul__, __truediv__},
                        tz: Any = None,
                        numticks: int = 5) -> Tuple[
    Union[MinuteLocator, HourLocator, DayLocator, WeekdayLocator, MonthLocator, YearLocator], DateFormatter]: ...


class DateConverter(ConversionInterface):
    _interval_multiples: bool

    def __init__(self: DateConverter,
                 *,
                 interval_multiples: bool = True) -> None: ...

    def axisinfo(self: DateConverter,
                 unit: Any,
                 axis: Any) -> AxisInfo: ...

    def convert(value: Any,
                unit: Any,
                axis: Any) -> Union[float, Any]: ...

    def default_units(x: Any,
                      axis: Any) -> Optional[Any]: ...


class ConciseDateConverter(DateConverter):
    _formats: Any
    _zero_formats: Any
    _offset_formats: Any
    _show_offset: bool
    _interval_multiples: bool

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
    conv_st: ClassVar[str]
    int_mult: ClassVar[bool]
    conv_st: Any
    int_mult: Any

    def set_converter(cls: Type[_rcParam_helper],
                      s: Any) -> Any: ...

    def set_int_mult(cls: Type[_rcParam_helper],
                     b: Any) -> None: ...

    def register_converters(cls: Type[_rcParam_helper]) -> None: ...
