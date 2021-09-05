from utils import _check_argument as _check_argument
from scipy import stats as stats
from numbers import Number as Number
from distutils.version import LooseVersion as LooseVersion
from typing import Any
from typing import Tuple
from typing import Union

from object import object
from scipy.stats.kde import gaussian_kde
from seaborn._statistics import ECDF
from seaborn._statistics import Histogram
from seaborn._statistics import KDE


class KDE(object):
    cut: Any
    gridsize: Any
    cumulative: Any
    support: None
    bw_adjust: Any
    clip: Union[tuple[None, None], Any]
    bw_method: Any

    def __init__(self: KDE,
                 *,
                 bw_method: Any = None,
                 bw_adjust: Any = 1,
                 gridsize: Any = 200,
                 cut: Any = 3,
                 clip: Any = None,
                 cumulative: Any = False) -> None: ...

    def _define_support_grid(self: KDE,
                             x: {min, max},
                             bw: {__mul__},
                             cut: Any,
                             clip: {__getitem__},
                             gridsize: Any) -> Union[Tuple[Any, Optional[float]], Any]: ...

    def _define_support_univariate(self: KDE,
                                   x: Any,
                                   weights: Any) -> Union[Tuple[Any, Optional[float]], Any]: ...

    def _define_support_bivariate(self: KDE,
                                  x1: Any,
                                  x2: Any,
                                  weights: Any) -> Tuple[
        Union[Tuple[Any, Optional[float]], Any], Union[Tuple[Any, Optional[float]], Any]]: ...

    def define_support(self: KDE,
                       x1: Any,
                       x2: Any = None,
                       weights: Any = None,
                       cache: bool = True) -> Union[Union[Tuple[Any, Optional[float]], Tuple[
        Union[Tuple[Any, Optional[float]], Any], Union[Tuple[Any, Optional[float]], Any]]], Any]: ...

    def _fit(self: KDE,
             fit_data: Union[Union[list[Union[{min, max}, Any]], list[Any]], Any],
             weights: Any = None) -> gaussian_kde: ...

    def _eval_univariate(self: KDE,
                         x: Any,
                         weights: Any = None) -> Tuple[Any, Union[Tuple[Any, Optional[float]], Any]]: ...

    def _eval_bivariate(self: KDE,
                        x1: Any,
                        x2: Any,
                        weights: Any = None) -> Tuple[Any, Union[Tuple[Any, Optional[float]], Any]]: ...

    def __call__(self: KDE,
                 x1: Any,
                 x2: Any = None,
                 weights: Any = None) -> Tuple[Any, Union[Tuple[Any, Optional[float]], Any]]: ...


class Histogram(object):
    discrete: Union[bool, Any]
    stat: str
    bins: Any
    bin_kws: None
    binwidth: Any
    binrange: Any
    cumulative: bool

    def __init__(self: Histogram,
                 stat: str = "count",
                 bins: Any = "auto",
                 binwidth: Any = None,
                 binrange: Any = None,
                 discrete: Union[bool, Any] = False,
                 cumulative: bool = False) -> None: ...

    def _define_bin_edges(self: Histogram,
                          x: Any,
                          weights: Any,
                          bins: Any,
                          binwidth: Any,
                          binrange: Any,
                          discrete: Any) -> Any: ...

    def define_bin_params(self: Histogram,
                          x1: Any,
                          x2: Any = None,
                          weights: Any = None,
                          cache: bool = True) -> Union[
        dict[str, Union[int, Tuple[Any, Any]]], dict[Any, Any], dict[Any, Tuple[Any, ...]]]: ...

    def _eval_bivariate(self: Histogram,
                        x1: Any,
                        x2: Any,
                        weights: Any) -> Tuple[Union[int, Any], Any]: ...

    def _eval_univariate(self: Histogram,
                         x: Any,
                         weights: Any) -> Tuple[Union[Union[int, Iterable, float], Any], Any]: ...

    def __call__(self: Histogram,
                 x1: Any,
                 x2: Any = None,
                 weights: Any = None) -> Union[
        Tuple[Union[Union[int, Iterable, float], Any], Any], Tuple[Union[int, Any], Any]]: ...


class ECDF(object):
    stat: Any
    complementary: bool

    def __init__(self: ECDF,
                 stat: Any = "proportion",
                 complementary: bool = False) -> None: ...

    def _eval_bivariate(self: ECDF,
                        x1: Any,
                        x2: Any,
                        weights: Any) -> Any: ...

    def _eval_univariate(self: ECDF,
                         x: {argsort},
                         weights: Any) -> Tuple[Union[matrix, Any], Union[matrix, Any]]: ...

    def __call__(self: ECDF,
                 x1: Any,
                 x2: Any = None,
                 weights: Any = None) -> Union[Tuple[Union[matrix, Any], Union[matrix, Any]], Any]: ...
