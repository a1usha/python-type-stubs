from _decorators import _deprecate_positional_args as _deprecate_positional_args
from axisgrid import _facet_docs as _facet_docs
from axisgrid import FacetGrid as FacetGrid
from seaborn import algorithms as algo
from seaborn import utils as utils
from scipy.spatial import distance as distance
from textwrap import dedent as dedent
from typing import Any
from typing import Tuple
from typing import Union

from object import object
from seaborn.axisgrid import FacetGrid
from seaborn.regression import _LinearPlotter
from seaborn.regression import _RegressionPlotter

__all__: Any


class _LinearPlotter(object):
    data: Any

    def establish_variables(self: _LinearPlotter,
                            data: Any,
                            **kwargs) -> Any: ...

    def dropna(self: _LinearPlotter,
               *args) -> None: ...

    def plot(self: _LinearPlotter,
             ax: Any) -> Any: ...


class _RegressionPlotter(_LinearPlotter):
    robust: bool
    seed: Any
    color: Any
    ci: int
    logx: bool
    x_range: tuple[Any, Any]
    label: Any
    y_jitter: Any
    lowess: bool
    x_jitter: Any
    x_estimator: Union[Callable[[Union[Union[Iterable, int, float], Any], Union[None, int, Iterable, tuple[int]],
                                 Optional[object], Any, Optional[bool], Any,
                                 Union[Union[Iterable, int, float[bool], None], Any]], Any], Any]
    logistic: bool
    truncate: bool
    scatter: bool
    x: Any
    y: Any
    x_ci: Union[int, str]
    x_discrete: Any
    n_boot: int
    fit_reg: bool
    order: int

    def __init__(self: _RegressionPlotter,
                 x: Any,
                 y: Any,
                 data: Any = None,
                 x_estimator: Any = None,
                 x_bins: Any = None,
                 x_ci: str = "ci",
                 scatter: bool = True,
                 fit_reg: bool = True,
                 ci: int = 95,
                 n_boot: int = 1000,
                 units: Any = None,
                 seed: Any = None,
                 order: int = 1,
                 logistic: bool = False,
                 lowess: bool = False,
                 robust: bool = False,
                 logx: bool = False,
                 x_partial: Any = None,
                 y_partial: Any = None,
                 truncate: bool = False,
                 dropna: bool = True,
                 x_jitter: Any = None,
                 y_jitter: Any = None,
                 color: Any = None,
                 label: Any = None) -> Any: ...

    def scatter_data(self: _RegressionPlotter) -> Tuple[Any, Any]: ...

    def estimate_data(self: _RegressionPlotter) -> Tuple[
        list[Any], list[Any], list[Union[Union[None, Tuple[Any, Any], int, float, complex], Any]]]: ...

    def fit_regression(self: _RegressionPlotter,
                       ax: Any = None,
                       x_range: Any = None,
                       grid: Any = None) -> Tuple[
        Union[Tuple[Any, Optional[float]], Any], Any, Union[Union[None, int, float, complex], Any]]: ...

    def fit_fast(self: _RegressionPlotter,
                 grid: Union[tuple[Any, Optional[float]], Any]) -> Union[Tuple[Any, None], Tuple[Any, Any]]: ...

    def fit_poly(self: _RegressionPlotter,
                 grid: Union[tuple[Any, Optional[float]], Any],
                 order: Any) -> Union[Tuple[Union[poly1d, Any], None], Tuple[Union[poly1d, Any], array.pyi]]: ...

    def fit_statsmodels(self: _RegressionPlotter,
                        grid: Union[tuple[Any, Optional[float]], Any],
                        model: Any,
                        **kwargs) -> Union[Tuple[Any, None], Tuple[Any, array.pyi]]: ...

    def fit_lowess(self: _RegressionPlotter) -> Tuple[Any, Any]: ...

    def fit_logx(self: _RegressionPlotter,
                 grid: Union[tuple[Any, Optional[float]], Any]) -> Union[Tuple[Any, None], Tuple[Any, Any]]: ...

    def bin_predictor(self: _RegressionPlotter,
                      bins: {__getitem__, ravel}) -> Tuple[Any, matrix]: ...

    def regress_out(self: _RegressionPlotter,
                    a: {mean},
                    b: Any) -> Any: ...

    def plot(self: _RegressionPlotter,
             ax: Any,
             scatter_kws: Union[dict[Any, Any], Any],
             line_kws: {setdefault}) -> None: ...

    def scatterplot(self: _RegressionPlotter,
                    ax: Any,
                    kws: Any) -> None: ...

    def lineplot(self: _RegressionPlotter,
                 ax: {plot},
                 kws: {__getitem__, pop, setdefault}) -> None: ...


_regression_docs: dict[str, str]


def lmplot(*,
           x: Any = None,
           y: Any = None,
           data: Any = None,
           hue: Any = None,
           col: Any = None,
           row: Any = None,
           palette: Any = None,
           col_wrap: Any = None,
           height: int = 5,
           aspect: int = 1,
           markers: str = "o",
           sharex: Any = None,
           sharey: Any = None,
           hue_order: Any = None,
           col_order: Any = None,
           row_order: Any = None,
           legend: bool = True,
           legend_out: Any = None,
           x_estimator: Any = None,
           x_bins: Any = None,
           x_ci: str = "ci",
           scatter: bool = True,
           fit_reg: bool = True,
           ci: int = 95,
           n_boot: int = 1000,
           units: Any = None,
           seed: Any = None,
           order: int = 1,
           logistic: bool = False,
           lowess: bool = False,
           robust: bool = False,
           logx: bool = False,
           x_partial: Any = None,
           y_partial: Any = None,
           truncate: bool = True,
           x_jitter: Any = None,
           y_jitter: Any = None,
           scatter_kws: Any = None,
           line_kws: Any = None,
           facet_kws: Any = None,
           size: Any = None) -> Union[FacetGrid, Any]: ...


def regplot(*,
            x: Any = None,
            y: Any = None,
            data: Any = None,
            x_estimator: Any = None,
            x_bins: Any = None,
            x_ci: str = "ci",
            scatter: bool = True,
            fit_reg: bool = True,
            ci: int = 95,
            n_boot: int = 1000,
            units: Any = None,
            seed: Any = None,
            order: int = 1,
            logistic: bool = False,
            lowess: bool = False,
            robust: bool = False,
            logx: bool = False,
            x_partial: Any = None,
            y_partial: Any = None,
            truncate: bool = True,
            dropna: bool = True,
            x_jitter: Any = None,
            y_jitter: Any = None,
            label: Any = None,
            color: Any = None,
            marker: str = "o",
            scatter_kws: Any = None,
            line_kws: Any = None,
            ax: Any = None) -> Any: ...


def residplot(*,
              x: Union[str, Any] = None,
              y: Union[str, Any] = None,
              data: Any = None,
              lowess: Any = False,
              x_partial: Any = None,
              y_partial: Any = None,
              order: Any = 1,
              robust: Any = False,
              dropna: Any = True,
              label: Any = None,
              color: Any = None,
              scatter_kws: Any = None,
              line_kws: Any = None,
              ax: Any = None) -> Any: ...