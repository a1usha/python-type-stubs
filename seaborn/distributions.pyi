from _docstrings import _core_docs as _core_docs
from _docstrings import DocstringComponents as DocstringComponents
from _decorators import _deprecate_positional_args as _deprecate_positional_args
from external import husl as husl
from palettes import color_palette as color_palette
from utils import _assign_default_kwargs as _assign_default_kwargs
from utils import _check_argument as _check_argument
from utils import _normalize_kwargs as _normalize_kwargs
from utils import _kde_support as _kde_support
from utils import remove_na as remove_na
from axisgrid import _facet_docs as _facet_docs
from axisgrid import FacetGrid as FacetGrid
from _statistics import ECDF as ECDF
from _statistics import Histogram as Histogram
from _statistics import KDE as KDE
from _core import VectorPlotter as VectorPlotter
from scipy import stats as stats
from matplotlib.collections import LineCollection as LineCollection
from matplotlib.colors import to_rgba as to_rgba
from functools import partial as partial
from numbers import Number as Number
from functools import partial
from typing import Any
from typing import ClassVar
from typing import Optional
from typing import Tuple
from typing import Union

from matplotlib.colors import ListedColormap
from seaborn._core import VectorPlotter
from seaborn.axisgrid import FacetGrid
from seaborn.distributions import _DistributionPlotter

_dist_params: dict[str, str]
_param_docs: DocstringComponents
__all__: Any


class _DistributionPlotter(VectorPlotter):
    semantics: ClassVar[tuple[str, str, str, str]]
    wide_structure: ClassVar[dict[str, str]]
    flat_structure: ClassVar[dict[str, str]]

    def __init__(self: _DistributionPlotter,
                 data: Any = None,
                 variables: dict[Any, Any] = {}) -> None: ...

    def univariate(self: _DistributionPlotter) -> bool: ...

    def data_variable(self: _DistributionPlotter) -> str: ...

    def has_xy_data(self: _DistributionPlotter) -> bool: ...

    def _add_legend(self: _DistributionPlotter,
                    ax_obj: Union[FacetGrid, Any],
                    artist: Union[partial[Any], Any],
                    fill: Union[bool, Any],
                    element: Union[bool, Any],
                    multiple: Optional[Any],
                    alpha: Union[int, Any],
                    artist_kws: Any,
                    legend_kws: Any) -> None: ...

    def _artist_kws(self: _DistributionPlotter,
                    kws: Union[Union[dict[Any, Any], dict[Any, Any], dict[str, Any], dict[str, Union[Union[
                                                                                                         ListedColormap,
                                                                                                         _ColorPalette[
                                                                                                             Any], list[
                                                                                                             Any], list,
                                                                                                         _ColorPalette[
                                                                                                             tuple[
                                                                                                                 float, float, float]],
                                                                                                         _ColorPalette[
                                                                                                             tuple], None], Any]]], Any],
                    fill: Union[bool, Any],
                    element: Union[bool, Any],
                    multiple: Any,
                    color: Any,
                    alpha: Any) -> dict[str, Union[Union[ListedColormap, _ColorPalette[Any], list[Any], list,
                                                         _ColorPalette[Tuple[float, float, float]], _ColorPalette[
                                                             Tuple], None], Any]]: ...

    def _quantile_to_level(self: _DistributionPlotter,
                           data: Union[list[Any], Any],
                           quantile: Union[Optional[tuple[Any, Optional[float]]], Any]) -> Any: ...

    def _cmap_from_color(self: _DistributionPlotter,
                         color: Union[str, Any]) -> ListedColormap: ...

    def _default_discrete(self: _DistributionPlotter) -> Union[
        Union[bool, Tuple[Union[bool, Any], Union[bool, Any]]], Any]: ...

    def _resolve_multiple(self: _DistributionPlotter,
                          curves: Union[dict[tuple, Series], Any],
                          multiple: Union[Union[None, str, {__eq__}], Any]) -> Union[
        Tuple[Union[dict[Tuple, Series], Any], dict], Tuple[Union[dict[Tuple, Series], Any], Union[dict, Any]]]: ...

    def _compute_univariate_density(self: _DistributionPlotter,
                                    data_variable: Union[str, Any],
                                    common_norm: Union[bool, Any],
                                    common_grid: Any,
                                    estimate_kws: Any,
                                    log_scale: Any,
                                    warn_singular: bool = True) -> dict[Tuple, Series]: ...

    def plot_univariate_histogram(self: _DistributionPlotter,
                                  multiple: Union[str, Any],
                                  element: {__ne__, __eq__},
                                  fill: Any,
                                  common_norm: Any,
                                  common_bins: Any,
                                  shrink: {__mul__},
                                  kde: Any,
                                  kde_kws: Any,
                                  color: Any,
                                  legend: Any,
                                  line_kws: Any,
                                  estimate_kws: Any,
                                  **kwargs) -> Any: ...

    def plot_bivariate_histogram(self: _DistributionPlotter,
                                 common_bins: Union[bool, Any],
                                 common_norm: Any,
                                 thresh: Any,
                                 pthresh: Any,
                                 pmax: Any,
                                 color: Any,
                                 legend: Any,
                                 cbar: Any,
                                 cbar_ax: Any,
                                 cbar_kws: Any,
                                 estimate_kws: Any,
                                 **kwargs) -> None: ...

    def plot_univariate_density(self: _DistributionPlotter,
                                multiple: Union[str, Any],
                                common_norm: Any,
                                common_grid: Any,
                                warn_singular: Any,
                                fill: Any,
                                legend: Any,
                                estimate_kws: Any,
                                **kwargs) -> None: ...

    def plot_bivariate_density(self: _DistributionPlotter,
                               common_norm: Union[bool, Any],
                               fill: Any,
                               levels: Any,
                               thresh: Any,
                               color: Any,
                               legend: Any,
                               cbar: Any,
                               warn_singular: Any,
                               cbar_ax: Any,
                               cbar_kws: Any,
                               estimate_kws: Any,
                               **kwargs) -> Any: ...

    def plot_univariate_ecdf(self: _DistributionPlotter,
                             estimate_kws: Union[dict[str, Union[str, bool]], Any],
                             legend: Any,
                             **kwargs) -> None: ...

    def plot_rug(self: _DistributionPlotter,
                 height: Union[float, Any],
                 expand_margins: Any,
                 legend: Any,
                 **kwargs) -> None: ...

    def _plot_single_rug(self: _DistributionPlotter,
                         sub_data: {__getitem__},
                         var: Union[str, Any],
                         height: Any,
                         ax: {add_collection, autoscale_view},
                         kws: Any) -> None: ...


class _DistributionFacetPlotter(_DistributionPlotter):
    semantics: ClassVar[tuple[str, str, str, str, str, str]]
    pass


def histplot(data: Any = None,
             *,
             x: Any = None,
             y: Any = None,
             hue: Any = None,
             weights: Any = None,
             stat: str = "count",
             bins: str = "auto",
             binwidth: Any = None,
             binrange: Any = None,
             discrete: Any = None,
             cumulative: bool = False,
             common_bins: bool = True,
             common_norm: bool = True,
             multiple: str = "layer",
             element: str = "bars",
             fill: bool = True,
             shrink: int = 1,
             kde: bool = False,
             kde_kws: Any = None,
             line_kws: Any = None,
             thresh: int = 0,
             pthresh: Any = None,
             pmax: Any = None,
             cbar: bool = False,
             cbar_ax: Any = None,
             cbar_kws: Any = None,
             palette: Any = None,
             hue_order: Any = None,
             hue_norm: Any = None,
             color: Any = None,
             log_scale: Any = None,
             legend: bool = True,
             ax: Any = None,
             **kwargs) -> Any: ...


def kdeplot(x: Any = None,
            *,
            y: Any = None,
            shade: Any = None,
            vertical: bool = False,
            kernel: Any = None,
            bw: Any = None,
            gridsize: int = 200,
            cut: int = 3,
            clip: Any = None,
            legend: bool = True,
            cumulative: bool = False,
            shade_lowest: Any = None,
            cbar: bool = False,
            cbar_ax: Any = None,
            cbar_kws: Any = None,
            ax: Any = None,
            weights: Any = None,
            hue: Any = None,
            palette: Any = None,
            hue_order: Any = None,
            hue_norm: Any = None,
            multiple: str = "layer",
            common_norm: bool = True,
            common_grid: bool = False,
            levels: int = 10,
            thresh: float = .05,
            bw_method: str = "scott",
            bw_adjust: int = 1,
            log_scale: Any = None,
            color: Any = None,
            fill: Any = None,
            data: Any = None,
            data2: Any = None,
            warn_singular: bool = True,
            **kwargs) -> Any: ...


def ecdfplot(data: Any = None,
             *,
             x: Any = None,
             y: Any = None,
             hue: Any = None,
             weights: Any = None,
             stat: str = "proportion",
             complementary: bool = False,
             palette: Any = None,
             hue_order: Any = None,
             hue_norm: Any = None,
             log_scale: Any = None,
             legend: bool = True,
             ax: Any = None,
             **kwargs) -> Any: ...


def rugplot(x: Any = None,
            *,
            height: float = .025,
            axis: Optional[{__eq__}] = None,
            ax: Any = None,
            data: Any = None,
            y: Any = None,
            hue: Any = None,
            palette: Any = None,
            hue_order: Any = None,
            hue_norm: Any = None,
            expand_margins: bool = True,
            legend: bool = True,
            a: Any = None,
            **kwargs) -> Any: ...


def displot(data: Any = None,
            *,
            x: Any = None,
            y: Any = None,
            hue: Any = None,
            row: Any = None,
            col: Any = None,
            weights: Any = None,
            kind: str = "hist",
            rug: bool = False,
            rug_kws: Any = None,
            log_scale: Any = None,
            legend: bool = True,
            palette: Any = None,
            hue_order: Any = None,
            hue_norm: Any = None,
            color: Any = None,
            col_wrap: Any = None,
            row_order: Any = None,
            col_order: Any = None,
            height: int = 5,
            aspect: int = 1,
            facet_kws: Any = None,
            **kwargs) -> FacetGrid: ...


def _freedman_diaconis_bins(a: Any) -> int: ...


def distplot(a: Any = None,
             bins: Any = None,
             hist: Any = True,
             kde: Any = True,
             rug: Any = False,
             fit: Any = None,
             hist_kws: Any = None,
             kde_kws: Any = None,
             rug_kws: Any = None,
             fit_kws: Any = None,
             color: Any = None,
             vertical: Any = False,
             norm_hist: Any = False,
             axlabel: Any = None,
             label: Any = None,
             ax: Any = None,
             x: Any = None) -> Any: ...