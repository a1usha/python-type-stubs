from utils import remove_na as remove_na
from utils import get_color_cycle as get_color_cycle
from palettes import color_palette as color_palette
from palettes import QUAL_PALETTES as QUAL_PALETTES
from _decorators import share_init_params_with_map as share_init_params_with_map
from distutils.version import LooseVersion as LooseVersion
from datetime import datetime as datetime
from numbers import Number as Number
from collections.abc import Mapping as Mapping
from collections.abc import Sequence as Sequence
from collections.abc import Iterable as Iterable
from functools import partial as partial
from copy import copy as copy
from typing import Any
from typing import ClassVar
from typing import Generator
from typing import Optional
from typing import Tuple
from typing import Type
from typing import Union

from object import object
from pandas.core.frame import DataFrame
from seaborn._core import HueMapping
from seaborn._core import SemanticMapping
from seaborn._core import SizeMapping
from seaborn._core import StyleMapping
from seaborn._core import VectorPlotter


class SemanticMapping(object):
    map_type: ClassVar[None]
    levels: ClassVar[None]
    lookup_table: ClassVar[None]
    plotter: Union[Union[{plot_data}, {plot_data}, {plot_data}], Any]

    def __init__(self: SemanticMapping,
                 plotter: Union[Union[{plot_data}, {plot_data}, {plot_data}], Any]) -> None: ...

    def map(cls: SemanticMapping,
            plotter: Any,
            *args,
            **kwargs) -> Any: ...

    def _lookup_single(self: SemanticMapping,
                       key: Any) -> Any: ...

    def __call__(self: SemanticMapping,
                 key: Any,
                 *args,
                 **kwargs) -> Union[list[Any], Any]: ...


class HueMapping(SemanticMapping):
    palette: ClassVar[None]
    norm: ClassVar[None]
    cmap: ClassVar[None]
    map_type: Union[str, Any]
    lookup_table: Union[dict, dict[Any, Any]]
    cmap: Union[Union[None, str, _ColorPalette[Any], list[Any], list, _ColorPalette[tuple[float, float, float]],
                      _ColorPalette[tuple]], Any]
    palette: Any
    levels: Union[list, list[Union[SupportsLessThan, Any]], list[Any]]
    norm: Optional[Any]

    def __init__(self: HueMapping,
                 plotter: Union[Union[{plot_data}, {plot_data}], Any],
                 palette: Any = None,
                 order: Any = None,
                 norm: Any = None) -> None: ...

    def _lookup_single(self: HueMapping,
                       key: Any) -> Union[Tuple[int, int, int, int], Any]: ...

    def infer_map_type(self: HueMapping,
                       palette: Any,
                       norm: Any,
                       input_format: {__eq__},
                       var_type: Any) -> Union[str, Any]: ...

    def categorical_mapping(self: HueMapping,
                            data: Union[list[Any], Any],
                            palette: Any,
                            order: Any) -> Tuple[list, Union[dict, dict[Any, Any]]]: ...

    def numeric_mapping(self: HueMapping,
                        data: Any,
                        palette: Any,
                        norm: Any) -> Tuple[
        Union[list[Union[SupportsLessThan, Any]], list[Any]], dict[Any, Any], Any, Union[Union[str, _ColorPalette[Any],
                                                                                               list[Any], list,
                                                                                               _ColorPalette[Tuple[
                                                                                                   float, float, float]],
                                                                                               _ColorPalette[
                                                                                                   Tuple]], Any]]: ...


class SizeMapping(SemanticMapping):
    norm: ClassVar[None]
    map_type: Union[str, Any]
    sizes: Any
    lookup_table: Union[dict[Any, Any], dict]
    size_range: Union[Union[None, tuple[Union[SupportsLessThan, Any], Union[SupportsLessThan, Any]], tuple], Any]
    levels: Union[list, list[Any]]
    norm: Union[Optional[{clip, scaled}], Any]

    def __init__(self: SizeMapping,
                 plotter: Union[Union[{plot_data}, {plot_data}], Any],
                 sizes: Any = None,
                 order: Any = None,
                 norm: Any = None) -> None: ...

    def infer_map_type(self: SizeMapping,
                       norm: Any,
                       sizes: Any,
                       var_type: Any) -> Union[str, Any]: ...

    def _lookup_single(self: SizeMapping,
                       key: Any) -> Any: ...

    def categorical_mapping(self: SizeMapping,
                            data: Union[list[Any], Any],
                            sizes: Any,
                            order: Any) -> Tuple[list, dict[Any, Any]]: ...

    def numeric_mapping(self: SizeMapping,
                        data: Any,
                        sizes: Any,
                        norm: Optional[{clip, scaled}]) -> Tuple[
        list[Any], Union[dict, dict[Any, Any]], Union[Optional[{clip, scaled}], Any], Union[
            Union[Tuple[Union[SupportsLessThan, Any], Union[SupportsLessThan, Any]], Tuple], Any]]: ...


class StyleMapping(SemanticMapping):
    map_type: ClassVar[str]
    lookup_table: dict[Any, dict[Any, Any]]
    levels: list

    def __init__(self: StyleMapping,
                 plotter: Union[Union[{plot_data}, {plot_data}], Any],
                 markers: Any = None,
                 dashes: Any = None,
                 order: Any = None) -> Any: ...

    def _lookup_single(self: StyleMapping,
                       key: Any,
                       attr: Any = None) -> Union[dict[Any, Any], Any]: ...

    def _map_attributes(self: StyleMapping,
                        arg: Any,
                        levels: Union[list, Any],
                        defaults: Any,
                        attr: Any) -> Union[dict, dict[Any, Any], dict[Any, Any]]: ...


class VectorPlotter(object):
    _semantic_mappings: ClassVar[dict[str, {map, __init__}]]
    semantics: ClassVar[tuple[str, str, str, str, str, str]]
    wide_structure: ClassVar[dict[str, str]]
    flat_structure: ClassVar[dict[str, str]]
    _default_size_range: ClassVar[tuple[int, int]]
    _comp_data: Any
    variables: Any
    plot_data: Any
    ax: None
    _var_levels: dict[Any, Any]
    var_types: dict
    input_format: str
    facets: FacetGrid

    def __init__(self: VectorPlotter,
                 data: Any = None,
                 variables: dict[Any, Any] = {}) -> None: ...

    def get_semantics(cls: Type[VectorPlotter],
                      kwargs: {items},
                      semantics: Optional[{__contains__}] = None) -> dict[Any, Any]: ...

    def has_xy_data(self: VectorPlotter) -> bool: ...

    def var_levels(self: VectorPlotter) -> dict[Any, Any]: ...

    def assign_variables(self: VectorPlotter,
                         data: Any = None,
                         variables: dict[Any, Any] = {}) -> VectorPlotter: ...

    def _assign_variables_wideform(self: VectorPlotter,
                                   data: Any = None,
                                   **kwargs) -> DataFrame: ...

    def _assign_variables_longform(self: VectorPlotter,
                                   data: Any = None,
                                   **kwargs) -> DataFrame: ...

    def iter_data(self: VectorPlotter,
                  grouping_vars: Union[str, list] = None,
                  reverse: Any = False,
                  from_comp_data: Any = False) -> Generator[
        Union[Tuple[dict[Union[Tuple, str], Any], Any], Tuple[dict[Any, Any], Any]], Any, None]: ...

    def comp_data(self: VectorPlotter) -> Any: ...

    def _get_axes(self: VectorPlotter,
                  sub_vars: {get}) -> Any: ...

    def _attach(self: VectorPlotter,
                obj: Any,
                allowed_types: Union[str, list[str]] = None,
                log_scale: Any = None) -> Any: ...

    def _log_scaled(self: VectorPlotter,
                    axis: Any) -> bool: ...

    def _add_axis_labels(self: VectorPlotter,
                         ax: {get_xlabel, get_ylabel},
                         default_x: str = "",
                         default_y: str = "") -> None: ...


def variable_type(vector: Any,
                  boolean_type: Any = "numeric") -> Any: ...


def infer_orient(x: Any = None,
                 y: Any = None,
                 orient: Optional[str] = None,
                 require_numeric: bool = True) -> Any: ...


def unique_dashes(n: int) -> Union[list, Any]: ...


def unique_markers(n: int) -> Union[list[str], Any]: ...


def categorical_order(vector: Any,
                      order: Any = None) -> list: ...