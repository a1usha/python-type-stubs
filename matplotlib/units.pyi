from decimal import Decimal
from typing import Any
from typing import Optional


class Registry(dict):
    def get_converter(self: Registry,
                      x: Any) -> Optional[Any]: ...


class ConversionError(TypeError):
    pass


class DecimalConverter(ConversionInterface):
    @staticmethod
    def convert(value: Decimal,
                unit: Any,
                axis: Any) -> Union[float, MaskedArray, ndarray]: ...

    @staticmethod
    def axisinfo(unit: Any,
                 axis: Any) -> AxisInfo: ...

    @staticmethod
    def default_units(x: Any,
                      axis: Any) -> None: ...


class ConversionInterface(object):
    @staticmethod
    def axisinfo(unit: Any,
                 axis: Any) -> None: ...

    @staticmethod
    def default_units(x: Any,
                      axis: Any) -> None: ...

    @staticmethod
    def convert(obj: Any,
                unit: Any,
                axis: Any) -> Any: ...

    @staticmethod
    def is_numlike(x: Any) -> bool: ...


class AxisInfo(object):
    def __init__(self: AxisInfo,
                 majloc: Any = None,
                 minloc: Any = None,
                 majfmt: Any = None,
                 minfmt: Any = None,
                 label: Optional[str] = None,
                 default_limits: Any = None) -> None: ...


def _is_natively_supported(x: Any) -> bool: ...