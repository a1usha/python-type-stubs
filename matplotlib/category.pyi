from typing import Any

from matplotlib.category import StrCategoryFormatter
from matplotlib.category import StrCategoryLocator
from matplotlib.category import UnitData
from matplotlib.ticker import Formatter
from matplotlib.ticker import Locator
from matplotlib.units import ConversionInterface
from numpy.core._multiarray_umath import ndarray
from object import object


class StrCategoryConverter(ConversionInterface):
    def convert(value: str,
                unit: Any,
                axis: Any) -> ndarray: ...

    def axisinfo(unit: Any,
                 axis: Any) -> Any: ...

    def default_units(data: str,
                      axis: Any) -> Any: ...

    def _validate_unit(unit: Any) -> Any: ...


class StrCategoryLocator(Locator):
    def __init__(self: StrCategoryLocator,
                 units_mapping: dict) -> None: ...

    def __call__(self: StrCategoryLocator) -> list: ...

    def tick_values(self: StrCategoryLocator,
                    vmin: Any,
                    vmax: Any) -> list: ...


class StrCategoryFormatter(Formatter):
    def __init__(self: StrCategoryFormatter,
                 units_mapping: dict) -> None: ...

    def __call__(self: StrCategoryFormatter,
                 x: Any,
                 pos: Any = None) -> str: ...

    def format_ticks(self: StrCategoryFormatter,
                     values: list) -> list[str]: ...

    def _text(value: Any) -> str: ...


class UnitData(object):
    def __init__(self: UnitData,
                 data: Any = None) -> None: ...

    def _str_is_convertible(val: Any) -> bool: ...

    def update(self: UnitData,
               data: bytes) -> None: ...
