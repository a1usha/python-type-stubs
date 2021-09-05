from _docstrings import _core_docs as _core_docs
from _docstrings import DocstringComponents as DocstringComponents
from _decorators import _deprecate_positional_args as _deprecate_positional_args
from axisgrid import _facet_docs as _facet_docs
from axisgrid import FacetGrid as FacetGrid
from algorithms import bootstrap as bootstrap
from utils import ci as ci_func
from utils import adjust_legend_subtitles as adjust_legend_subtitles
from utils import locator_to_legend_entries as locator_to_legend_entries
from utils import ci_to_errsize as ci_to_errsize
from _core import VectorPlotter as VectorPlotter
from typing import Any
from typing import ClassVar
from typing import Optional
from typing import Tuple
from typing import Union

from seaborn._core import VectorPlotter
from seaborn.axisgrid import FacetGrid
from seaborn.relational import _LinePlotter
from seaborn.relational import _RelationalPlotter
from seaborn.relational import _ScatterPlotter

_relational_narrative: DocstringComponents
_relational_docs: dict[str, str]
_param_docs: DocstringComponents
__all__: Any


class _RelationalPlotter(VectorPlotter):
    wide_structure: ClassVar[dict[str, str]]
    sort: ClassVar[bool]
    legend_order: list[Any]
    legend_data: dict[Any, Any]
    legend_title: Union[str, Any]

    def add_legend_data(self: _RelationalPlotter,
                        ax: Union[
                            Union[{plot, get_xlabel, get_ylabel}, {scatter, get_xlabel, get_ylabel}], Any]) -> Any: ...


class _LinePlotter(_RelationalPlotter):
    _legend_attributes: ClassVar[list[str]]
    _legend_func: ClassVar[str]
    estimator: Any
    seed: Any
    err_style: Any
    ci: Any
    legend: Any
    sort: bool
    err_kws: Union[dict[Any, Any], Any]
    n_boot: Any
    _default_size_range: Union[_NotImplementedType, Any]

    def __init__(self: _LinePlotter,
                 *,
                 data: Any = None,
                 variables: dict[Any, Any] = {},
                 estimator: Any = None,
                 ci: Any = None,
                 n_boot: Any = None,
                 seed: Any = None,
                 sort: bool = True,
                 err_style: Any = None,
                 err_kws: Any = None,
                 legend: Any = None) -> None: ...

    def aggregate(self: _LinePlotter,
                  vals: {groupby},
                  grouper: Any,
                  units: Any = None) -> Union[Tuple[Any, Any, None], Tuple[Any, Any, Optional[DataFrame]]]: ...

    def plot(self: _LinePlotter,
             ax: {plot, get_xlabel, get_ylabel},
             kws: {pop, setdefault, update}) -> Any: ...


class _ScatterPlotter(_RelationalPlotter):
    _legend_attributes: ClassVar[list[str]]
    _legend_func: ClassVar[str]
    legend: Any
    alpha: Any
    _default_size_range: Union[_NotImplementedType, Any]

    def __init__(self: _ScatterPlotter,
                 *,
                 data: Any = None,
                 variables: dict[Any, Any] = {},
                 x_bins: Any = None,
                 y_bins: Any = None,
                 estimator: Any = None,
                 ci: Any = None,
                 n_boot: Any = None,
                 alpha: Any = None,
                 x_jitter: Any = None,
                 y_jitter: Any = None,
                 legend: Any = None) -> None: ...

    def plot(self: _ScatterPlotter,
             ax: {scatter, get_xlabel, get_ylabel},
             kws: {get, pop, setdefault, __setitem__}) -> None: ...


def lineplot(*,
             x: Any = None,
             y: Any = None,
             hue: Any = None,
             size: Any = None,
             style: Any = None,
             data: Any = None,
             palette: Any = None,
             hue_order: Any = None,
             hue_norm: Any = None,
             sizes: Any = None,
             size_order: Any = None,
             size_norm: Any = None,
             dashes: bool = True,
             markers: Any = None,
             style_order: Any = None,
             units: Any = None,
             estimator: str = "mean",
             ci: int = 95,
             n_boot: int = 1000,
             seed: Any = None,
             sort: bool = True,
             err_style: str = "band",
             err_kws: Any = None,
             legend: str = "auto",
             ax: Optional[{plot, get_xlabel, get_ylabel}] = None,
             **kwargs) -> Union[Optional[{plot, get_xlabel, get_ylabel}], Any]: ...


def scatterplot(*,
                x: Any = None,
                y: Any = None,
                hue: Any = None,
                style: Any = None,
                size: Any = None,
                data: Any = None,
                palette: Any = None,
                hue_order: Any = None,
                hue_norm: Any = None,
                sizes: Any = None,
                size_order: Any = None,
                size_norm: Any = None,
                markers: bool = True,
                style_order: Any = None,
                x_bins: Any = None,
                y_bins: Any = None,
                units: Any = None,
                estimator: Any = None,
                ci: int = 95,
                n_boot: int = 1000,
                alpha: Any = None,
                x_jitter: Any = None,
                y_jitter: Any = None,
                legend: str = "auto",
                ax: Optional[{scatter, get_xlabel, get_ylabel}] = None,
                **kwargs) -> Union[Optional[{scatter, get_xlabel, get_ylabel}], Any]: ...


def relplot(*,
            x: Any = None,
            y: Any = None,
            hue: Any = None,
            size: Any = None,
            style: Any = None,
            data: Any = None,
            row: Any = None,
            col: Any = None,
            col_wrap: Any = None,
            row_order: Any = None,
            col_order: Any = None,
            palette: Any = None,
            hue_order: Any = None,
            hue_norm: Any = None,
            sizes: Any = None,
            size_order: Any = None,
            size_norm: Any = None,
            markers: Any = None,
            dashes: Any = None,
            style_order: Any = None,
            legend: str = "auto",
            kind: str = "scatter",
            height: int = 5,
            aspect: int = 1,
            facet_kws: Any = None,
            units: Any = None,
            **kwargs) -> Union[FacetGrid, Any]: ...