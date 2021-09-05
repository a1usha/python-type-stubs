from matplotlib import cbook as cbook
from numpy import ma as ma
from numbers import Number as Number
from decimal import Decimal as Decimal
from decimal import Decimal
from typing import Any
from typing import Optional
from typing import Union

from TypeError import TypeError
from dict import dict
from matplotlib.units import AxisInfo
from matplotlib.units import Registry
from numpy.ma.core import MaskedArray
from object import object


class ConversionError(TypeError):
    pass


def _is_natively_supported(x: Any) -> bool: ...


class AxisInfo(object):
    minfmt: Any
    majloc: Any
    minloc: Any
    default_limits: Any
    label: Optional[str]
    majfmt: Any

    def __init__(self: AxisInfo,
                 majloc: Any = None,
                 minloc: Any = None,
                 majfmt: Any = None,
                 minfmt: Any = None,
                 label: Optional[str] = None,
                 default_limits: Any = None) -> None: ...


class ConversionInterface(object):
    def axisinfo(unit: Any,
                 axis: Any) -> None: ...

    def default_units(x: Any,
                      axis: Any) -> None: ...

    def convert(obj: Any,
                unit: Any,
                axis: Any) -> Any: ...

    def is_numlike(x: Any) -> bool: ...


class DecimalConverter(ConversionInterface):
    def convert(value: Union[Decimal, Any],
                unit: Any,
                axis: Any) -> Union[float, MaskedArray]: ...

    def axisinfo(unit: Any,
                 axis: Any) -> AxisInfo: ...

    def default_units(x: Any,
                      axis: Any) -> None: ...


class Registry(dict):
    def get_converter(self: Registry,
                      x: Any) -> Optional[Any]: ...


registry: Registry[Type[Decimal], DecimalConverter]
