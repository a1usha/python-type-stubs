from matplotlib import units as units
from matplotlib import ticker as ticker
from matplotlib import _api as _api
from collections import OrderedDict as OrderedDict
from typing import Union

from matplotlib.category import StrCategoryFormatter
from matplotlib.category import StrCategoryLocator
from matplotlib.category import UnitData
from matplotlib.ticker import Formatter
from matplotlib.ticker import Locator
from matplotlib.units import ConversionInterface
from numpy.core._multiarray_umath import ndarray
from object import object

_log: Logger
from typing import Any


class StrCategoryConverter(ConversionInterface):
    def convert(value: Union[str, Any],
                unit: Any,
                axis: Any) -> Union[ndarray, Any]: ...

    def axisinfo(unit: Any,
                 axis: Any) -> Any: ...

    def default_units(data: Union[str, Any],
                      axis: Any) -> Any: ...

    def _validate_unit(unit: Any) -> Any: ...


class StrCategoryLocator(Locator):
    _units: dict

    def __init__(self: StrCategoryLocator,
                 units_mapping: dict) -> None: ...

    def __call__(self: StrCategoryLocator) -> list[Any]: ...

    def tick_values(self: StrCategoryLocator,
                    vmin: Any,
                    vmax: Any) -> list[Any]: ...


class StrCategoryFormatter(Formatter):
    _units: dict

    def __init__(self: StrCategoryFormatter,
                 units_mapping: dict) -> None: ...

    def __call__(self: StrCategoryFormatter,
                 x: Any,
                 pos: Any = None) -> Union[str, Any]: ...

    def format_ticks(self: StrCategoryFormatter,
                     values: Union[list[Any], Any]) -> list[Union[str, Any]]: ...

    def _text(value: Any) -> Union[str, Any]: ...


class UnitData(object):
    _mapping: OrderedDict[Any, Any]
    _counter: count[int]

    def __init__(self: UnitData,
                 data: Any = None) -> None: ...

    def _str_is_convertible(val: Any) -> bool: ...

    def update(self: UnitData,
               data: Union[bytes, Any]) -> None: ...
