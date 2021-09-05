from matplotlib.transforms import IdentityTransform as IdentityTransform
from matplotlib.transforms import Transform as Transform
from matplotlib.ticker import LogitLocator as LogitLocator
from matplotlib.ticker import SymmetricalLogLocator as SymmetricalLogLocator
from matplotlib.ticker import AutoMinorLocator as AutoMinorLocator
from matplotlib.ticker import AutoLocator as AutoLocator
from matplotlib.ticker import LogLocator as LogLocator
from matplotlib.ticker import NullLocator as NullLocator
from matplotlib.ticker import LogitFormatter as LogitFormatter
from matplotlib.ticker import LogFormatterSciNotation as LogFormatterSciNotation
from matplotlib.ticker import ScalarFormatter as ScalarFormatter
from matplotlib.ticker import NullFormatter as NullFormatter
from matplotlib import docstring as docstring
from matplotlib import _api as _api
from numpy import ma as ma
from typing import Any
from typing import Callable
from typing import ClassVar
from typing import Iterable
from typing import Optional
from typing import Tuple
from typing import Type
from typing import Union

from matplotlib import _api
from matplotlib.axis import Axis
from matplotlib.scale import FuncScale
from matplotlib.scale import FuncScaleLog
from matplotlib.scale import FuncTransform
from matplotlib.scale import InvertedLogTransform
from matplotlib.scale import InvertedSymmetricalLogTransform
from matplotlib.scale import LinearScale
from matplotlib.scale import LogScale
from matplotlib.scale import LogTransform
from matplotlib.scale import LogisticTransform
from matplotlib.scale import LogitScale
from matplotlib.scale import LogitTransform
from matplotlib.scale import ScaleBase
from matplotlib.scale import SymmetricalLogScale
from matplotlib.scale import SymmetricalLogTransform
from matplotlib.transforms import CompositeAffine2D
from matplotlib.transforms import CompositeGenericTransform
from matplotlib.transforms import IdentityTransform
from matplotlib.transforms import Transform
from object import object


class ScaleBase(object):
    def __init__(self: ScaleBase,
                 axis: Any) -> None: ...

    def get_transform(self: ScaleBase) -> Any: ...

    def set_default_locators_and_formatters(self: ScaleBase,
                                            axis: Any) -> Any: ...

    def limit_range_for_scale(self: ScaleBase,
                              vmin: Any,
                              vmax: Any,
                              minpos: Any) -> Tuple[Any, Any]: ...


class LinearScale(ScaleBase):
    name: ClassVar[str]

    def __init__(self: LinearScale,
                 axis: Any) -> None: ...

    def set_default_locators_and_formatters(self: LinearScale,
                                            axis: {set_major_locator, set_major_formatter, set_minor_formatter,
                                                   axis_name}) -> None: ...

    def get_transform(self: LinearScale) -> IdentityTransform: ...


class FuncTransform(Transform):
    input_dims: ClassVar[int]
    output_dims: ClassVar[int]
    _inverse: Callable
    _forward: Callable

    def __init__(self: FuncTransform,
                 forward: Callable,
                 inverse: Callable) -> Any: ...

    def transform_non_affine(self: FuncTransform,
                             values: Union[Union[Iterable, int, float], Any]) -> Any: ...

    def inverted(self: FuncTransform) -> FuncTransform: ...


class FuncScale(ScaleBase):
    name: ClassVar[str]
    _transform: FuncTransform

    def __init__(self: FuncScale,
                 axis: Any,
                 functions: tuple[Any, Any]) -> None: ...

    def get_transform(self: FuncScale) -> FuncTransform: ...

    def set_default_locators_and_formatters(self: FuncScale,
                                            axis: {set_major_locator, set_major_formatter, set_minor_formatter,
                                                   axis_name}) -> None: ...


class LogTransform(Transform):
    input_dims: ClassVar[int]
    output_dims: ClassVar[int]
    _clip: Any
    base: {__le__, __eq__}

    @_api.rename_parameter("3.3", "nonpos", "nonpositive")
    def __init__(self: LogTransform,
                 base: {__le__, __eq__},
                 nonpositive: str = 'clip') -> Any: ...

    def __str__(self: LogTransform) -> str: ...

    def transform_non_affine(self: LogTransform,
                             a: Any) -> Any: ...

    def inverted(self: LogTransform) -> InvertedLogTransform: ...


class InvertedLogTransform(Transform):
    input_dims: ClassVar[int]
    output_dims: ClassVar[int]
    base: Any

    def __init__(self: InvertedLogTransform,
                 base: Any) -> None: ...

    def __str__(self: InvertedLogTransform) -> str: ...

    def transform_non_affine(self: InvertedLogTransform,
                             a: Any) -> None: ...

    def inverted(self: InvertedLogTransform) -> LogTransform: ...


class LogScale(ScaleBase):
    name: ClassVar[str]
    base: ClassVar[property]
    _transform: LogTransform
    subs: Any

    @_api.deprecated("3.3", alternative="scale.LogTransform")
    def LogTransform(self: LogScale) -> Type[LogTransform]: ...

    @_api.deprecated("3.3", alternative="scale.InvertedLogTransform")
    def InvertedLogTransform(self: LogScale) -> Type[InvertedLogTransform]: ...

    def __init__(self: LogScale,
                 axis: Any,
                 **kwargs) -> None: ...

    def set_default_locators_and_formatters(self: LogScale,
                                            axis: {set_major_locator, set_major_formatter, set_minor_locator,
                                                   set_minor_formatter}) -> None: ...

    def get_transform(self: LogScale) -> LogTransform: ...

    def limit_range_for_scale(self: LogScale,
                              vmin: {__le__},
                              vmax: {__le__},
                              minpos: Any) -> Tuple[
        Union[Union[float, {__le__}], Any], Union[Union[float, {__le__}], Any]]: ...


class FuncScaleLog(LogScale):
    name: ClassVar[str]
    _transform: Union[{input_dims, output_dims}, {output_dims,
                                                  input_dims}, CompositeAffine2D, CompositeGenericTransform, _NotImplementedType]
    subs: None

    def __init__(self: FuncScaleLog,
                 axis: Axis,
                 functions: tuple[Any, Any],
                 base: float = 10) -> None: ...

    def base(self: FuncScaleLog) -> Any: ...

    def get_transform(self: FuncScaleLog) -> Union[{input_dims, output_dims}, {output_dims,
                                                                               input_dims}, CompositeAffine2D, CompositeGenericTransform, _NotImplementedType]: ...


class SymmetricalLogTransform(Transform):
    input_dims: ClassVar[int]
    output_dims: ClassVar[int]
    _linscale_adj: Union[float, Any]
    linthresh: {__le__}
    _log_base: Any
    linscale: {__le__, __truediv__}
    base: {__le__}

    def __init__(self: SymmetricalLogTransform,
                 base: {__le__},
                 linthresh: {__le__},
                 linscale: {__le__, __truediv__}) -> Any: ...

    def transform_non_affine(self: SymmetricalLogTransform,
                             a: {__getitem__}) -> Union[float, Any]: ...

    def inverted(self: SymmetricalLogTransform) -> InvertedSymmetricalLogTransform: ...


class InvertedSymmetricalLogTransform(Transform):
    input_dims: ClassVar[int]
    output_dims: ClassVar[int]
    _linscale_adj: Union[float, Any]
    linthresh: {__le__}
    invlinthresh: Union[Union[Iterable, int, float], Any]
    linscale: {__le__, __truediv__}
    base: {__le__}

    def __init__(self: InvertedSymmetricalLogTransform,
                 base: {__le__},
                 linthresh: {__le__},
                 linscale: {__le__, __truediv__}) -> None: ...

    def transform_non_affine(self: InvertedSymmetricalLogTransform,
                             a: {__getitem__}) -> Any: ...

    def inverted(self: InvertedSymmetricalLogTransform) -> SymmetricalLogTransform: ...


class SymmetricalLogScale(ScaleBase):
    name: ClassVar[str]
    base: ClassVar[property]
    linthresh: ClassVar[property]
    linscale: ClassVar[property]
    _transform: SymmetricalLogTransform
    subs: Any

    @_api.deprecated("3.3", alternative="scale.SymmetricalLogTransform")
    def SymmetricalLogTransform(self: SymmetricalLogScale) -> Type[SymmetricalLogTransform]: ...

    @_api.deprecated(
        "3.3", alternative="scale.InvertedSymmetricalLogTransform")
    def InvertedSymmetricalLogTransform(self: SymmetricalLogScale) -> Type[InvertedSymmetricalLogTransform]: ...

    def __init__(self: SymmetricalLogScale,
                 axis: Any,
                 **kwargs) -> None: ...

    def set_default_locators_and_formatters(self: SymmetricalLogScale,
                                            axis: {set_major_locator, set_major_formatter, set_minor_locator,
                                                   set_minor_formatter}) -> None: ...

    def get_transform(self: SymmetricalLogScale) -> SymmetricalLogTransform: ...


class LogitTransform(Transform):
    input_dims: ClassVar[int]
    output_dims: ClassVar[int]
    _nonpositive: str
    _clip: Any

    @_api.rename_parameter("3.3", "nonpos", "nonpositive")
    def __init__(self: LogitTransform,
                 nonpositive: str = 'mask') -> Optional[Any]: ...

    def transform_non_affine(self: LogitTransform,
                             a: {__truediv__}) -> Any: ...

    def inverted(self: LogitTransform) -> LogisticTransform: ...

    def __str__(self: LogitTransform) -> str: ...


class LogisticTransform(Transform):
    input_dims: ClassVar[int]
    output_dims: ClassVar[int]
    _nonpositive: str

    @_api.rename_parameter("3.3", "nonpos", "nonpositive")
    def __init__(self: LogisticTransform,
                 nonpositive: str = 'mask') -> Optional[Any]: ...

    def transform_non_affine(self: LogisticTransform,
                             a: {__neg__}) -> Union[float, Any]: ...

    def inverted(self: LogisticTransform) -> LogitTransform: ...

    def __str__(self: LogisticTransform) -> str: ...


class LogitScale(ScaleBase):
    name: ClassVar[str]
    _use_overline: bool
    _one_half: str
    _transform: LogitTransform

    @_api.rename_parameter("3.3", "nonpos", "nonpositive")
    def __init__(self: LogitScale,
                 axis: Axis,
                 nonpositive: str = 'mask',
                 *,
                 one_half: str = r"\frac{1}{2}",
                 use_overline: bool = False) -> Optional[Any]: ...

    def get_transform(self: LogitScale) -> LogitTransform: ...

    def set_default_locators_and_formatters(self: LogitScale,
                                            axis: {set_major_locator, set_major_formatter, set_minor_locator,
                                                   set_minor_formatter}) -> None: ...

    def limit_range_for_scale(self: LogitScale,
                              vmin: {__le__},
                              vmax: {__ge__},
                              minpos: Any) -> Tuple[
        Union[Union[float, {__le__}], Any], Union[Union[int, float, {__ge__}], Any]]: ...


_scale_mapping: dict[str, Type[Union[LogitScale, LinearScale, SymmetricalLogScale, LogScale, FuncScale, FuncScaleLog]]]


def get_scale_names() -> list[str]: ...


def scale_factory(scale: Any,
                  axis: Axis,
                  **kwargs) -> Any: ...


def register_scale(scale_class: Any) -> None: ...


def _get_scale_docs() -> str: ...