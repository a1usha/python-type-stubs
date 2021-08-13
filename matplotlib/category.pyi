from typing import Any


class UnitData(object):
    def __init__(self: UnitData,
                 data: Any = None) -> None: ...

    @staticmethod
    def _str_is_convertible(val: Any) -> bool: ...

    def update(self: UnitData,
               data: bytes) -> None: ...


class StrCategoryConverter(ConversionInterface):
    @staticmethod
    def convert(value: str,
                unit: Any,
                axis: Any) -> ndarray: ...

    @staticmethod
    def axisinfo(unit: Any,
                 axis: Any) -> Any: ...

    @staticmethod
    def default_units(data: str,
                      axis: Any) -> Any: ...

    @staticmethod
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
                     values: Any) -> list[str]: ...

    @staticmethod
    def _text(value: Any) -> str: ...
