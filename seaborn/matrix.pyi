from _decorators import _deprecate_positional_args as _deprecate_positional_args
from utils import _draw_figure as _draw_figure
from utils import to_utf8 as to_utf8
from utils import relative_luminance as relative_luminance
from utils import axis_ticklabels_overlap as axis_ticklabels_overlap
from utils import despine as despine
from axisgrid import Grid as Grid
from seaborn import cm as cm
from scipy.cluster import hierarchy as hierarchy
from matplotlib import gridspec as gridspec
from matplotlib.collections import LineCollection as LineCollection
from typing import Any
from typing import Hashable
from typing import Optional
from typing import Tuple
from typing import Union

from matplotlib.axes._axes import Axes
from numpy.ma.core import MaskedArray
from object import object
from pandas.core.arrays.base import ExtensionArray
from pandas.core.frame import DataFrame
from pandas.core.indexes.base import Index
from seaborn.axisgrid import Grid
from seaborn.matrix import ClusterGrid
from seaborn.matrix import _DendrogramPlotter
from seaborn.matrix import _HeatMapper

__all__: Any


def _index_to_label(index: Union[Index, Any]) -> Union[str, Hashable]: ...


def _index_to_ticklabels(index: Union[Index, Any]) -> Union[Union[list[str], ExtensionArray], Any]: ...


def _convert_colors(colors: {__getitem__}) -> Union[list[Any], list[list[Any]]]: ...


def _matrix_mask(data: Union[DataFrame, Any],
                 mask: Any) -> Union[Union[_NotImplementedType, bool, int], Any]: ...


class _HeatMapper(object):
    ylabel: Union[str, Hashable]
    data: DataFrame
    yticklabels: Union[list[Any], Any]
    xticks: Union[Union[float, list[Any]], Any]
    cbar_kws: Union[dict[Any, Any], Any]
    vmin: Union[Union[int, float, complex], Any]
    annot: bool
    fmt: Any
    annot_data: Union[Optional[MaskedArray], Any]
    yticks: Union[Union[float, list[Any]], Any]
    plot_data: MaskedArray
    cmap: Any
    xticklabels: Union[list[Any], Any]
    annot_kws: Union[dict[Any, Any], Any]
    xlabel: Union[str, Hashable]
    vmax: Union[Union[int, float, complex], Any]
    cbar: Any

    def __init__(self: _HeatMapper,
                 data: {columns, index},
                 vmin: Any,
                 vmax: Any,
                 cmap: Any,
                 center: Any,
                 robust: Any,
                 annot: Any,
                 fmt: Any,
                 annot_kws: Optional[{copy}],
                 cbar: Any,
                 cbar_kws: Optional[{copy}],
                 xticklabels: bool = True,
                 yticklabels: bool = True,
                 mask: Any = None) -> Any: ...

    def _determine_cmap_params(self: _HeatMapper,
                               plot_data: Union[MaskedArray, Any],
                               vmin: Any,
                               vmax: Any,
                               cmap: Any,
                               center: Any,
                               robust: Any) -> None: ...

    def _annotate_heatmap(self: _HeatMapper,
                          ax: Union[{pcolormesh, set, invert_yaxis, set_xticklabels, set_yticklabels, figure}, Any],
                          mesh: {update_scalarmappable, get_array, get_facecolors}) -> None: ...

    def _skip_ticks(self: _HeatMapper,
                    labels: Union[Union[list[Any], list[str], ExtensionArray, str, {__len__}], Any],
                    tickevery: Union[Union[int, bool], Any]) -> Tuple[Union[Union[float, list[Any]], Any], Union[
        Union[list[Any], list[str], ExtensionArray, str, {__len__}], Any]]: ...

    def _auto_ticks(self: _HeatMapper,
                    ax: Union[{pcolormesh, set, invert_yaxis, set_xticklabels, set_yticklabels, figure}, Any],
                    labels: Union[list[Any], Any],
                    axis: Any) -> Union[
        Tuple[list[Any], list[Any]], Tuple[Union[Union[float, list[Any]], Any], Union[list[Any], Any]]]: ...

    def plot(self: _HeatMapper,
             ax: {pcolormesh, set, invert_yaxis, set_xticklabels, set_yticklabels, figure},
             cax: Any,
             kws: Any) -> None: ...


def heatmap(data: Any,
            *,
            vmin: Any = None,
            vmax: Any = None,
            cmap: Any = None,
            center: Any = None,
            robust: Any = False,
            annot: Any = None,
            fmt: Any = ".2g",
            annot_kws: Any = None,
            linewidths: Any = 0,
            linecolor: Any = "white",
            cbar: Any = True,
            cbar_kws: Any = None,
            cbar_ax: Any = None,
            square: Any = False,
            xticklabels: Any = "auto",
            yticklabels: Any = "auto",
            mask: Any = None,
            ax: Any = None,
            **kwargs) -> Any: ...


class _DendrogramPlotter(object):
    rotate: Any
    ylabel: str
    data: DataFrame
    shape: tuple[int, int]
    method: Any
    yticklabels: list[Any]
    xticks: list[Any]
    label: Any
    linkage: Any
    axis: Any
    yticks: list[Any]
    array: Any
    metric: Any
    independent_coord: Any
    xticklabels: list[Any]
    xlabel: str
    dendrogram: dict
    dependent_coord: Any

    def __init__(self: _DendrogramPlotter,
                 data: DataFrame,
                 linkage: Any,
                 metric: Any,
                 method: Any,
                 axis: Any,
                 label: Any,
                 rotate: Any) -> None: ...

    def _calculate_linkage_scipy(self: _DendrogramPlotter) -> Any: ...

    def _calculate_linkage_fastcluster(self: _DendrogramPlotter) -> Any: ...

    def calculated_linkage(self: _DendrogramPlotter) -> Any: ...

    def calculate_dendrogram(self: _DendrogramPlotter) -> dict: ...

    def reordered_ind(self: _DendrogramPlotter) -> Any: ...

    def plot(self: _DendrogramPlotter,
             ax: Axes,
             tree_kws: Any) -> _DendrogramPlotter: ...


def dendrogram(data: DataFrame,
               *,
               linkage: Any = None,
               axis: Any = 1,
               label: Any = True,
               metric: Any = 'euclidean',
               method: Any = 'average',
               rotate: Any = False,
               tree_kws: Any = None,
               ax: Any = None) -> _DendrogramPlotter: ...


class ClusterGrid(Grid):
    ax_heatmap: Any
    data: DataFrame
    gs: GridSpec
    data2d: Union[DataFrame, Any]
    row_colors: Union[list[Any], list[list[Any]], None]
    col_colors: Union[list[Any], list[list[Any]], None]
    ax_cbar: Any
    dendrogram_row: None
    _figure: Any
    cbar_pos: Optional[Any]
    ax_col_dendrogram: Any
    ax_row_colors: Any
    row_color_labels: Union[list[Any], list[str], None]
    cax: Optional[Any]
    ax_row_dendrogram: Any
    col_color_labels: Union[list[Any], list[str], None]
    dendrogram_col: None
    ax_col_colors: Any
    mask: Union[Union[_NotImplementedType, bool, int], Any]

    def __init__(self: ClusterGrid,
                 data: Any,
                 pivot_kws: Any = None,
                 z_score: Any = None,
                 standard_scale: Any = None,
                 figsize: Any = None,
                 row_colors: Any = None,
                 col_colors: Any = None,
                 mask: Any = None,
                 dendrogram_ratio: Any = None,
                 colors_ratio: Any = None,
                 cbar_pos: Any = None) -> None: ...

    def _preprocess_colors(self: ClusterGrid,
                           data: Union[DataFrame, Any],
                           colors: Any,
                           axis: Union[int, Any]) -> Tuple[
        Union[list[Any], list[list[Any]], None], Union[list[Any], list[str], None]]: ...

    def format_data(self: ClusterGrid,
                    data: Union[DataFrame, Any],
                    pivot_kws: Any,
                    z_score: Any = None,
                    standard_scale: Any = None) -> Union[DataFrame, Any]: ...

    def z_score(data2d: DataFrame,
                axis: int = 1) -> DataFrame: ...

    def standard_scale(data2d: DataFrame,
                       axis: int = 1) -> DataFrame: ...

    def dim_ratios(self: ClusterGrid,
                   colors: Union[Union[list[Any], list[list[Any]], None], Any],
                   dendrogram_ratio: Any,
                   colors_ratio: Any) -> list[Union[int, Any]]: ...

    def color_list_to_matrix_and_cmap(colors: Any,
                                      ind: list,
                                      axis: int = 0) -> Any: ...

    def plot_dendrograms(self: ClusterGrid,
                         row_cluster: Union[bool, Any],
                         col_cluster: Any,
                         metric: Any,
                         method: Any,
                         row_linkage: Any,
                         col_linkage: Any,
                         tree_kws: Any) -> None: ...

    def plot_colors(self: ClusterGrid,
                    xind: Any,
                    yind: Any,
                    **kwargs) -> None: ...

    def plot_matrix(self: ClusterGrid,
                    colorbar_kws: Union[dict[Any, Any], Any],
                    xind: Any,
                    yind: Any,
                    **kwargs) -> Any: ...

    def plot(self: ClusterGrid,
             metric: Any,
             method: Any,
             colorbar_kws: Any,
             row_cluster: Any,
             col_cluster: Any,
             row_linkage: Any,
             col_linkage: Any,
             tree_kws: Any,
             **kwargs) -> ClusterGrid: ...


def clustermap(data: Any,
               *,
               pivot_kws: Any = None,
               method: Any = 'average',
               metric: Any = 'euclidean',
               z_score: Any = None,
               standard_scale: Any = None,
               figsize: Any = (10, 10),
               cbar_kws: Any = None,
               row_cluster: bool = True,
               col_cluster: bool = True,
               row_linkage: Any = None,
               col_linkage: Any = None,
               row_colors: Any = None,
               col_colors: Any = None,
               mask: Any = None,
               dendrogram_ratio: float = .2,
               colors_ratio: float = 0.03,
               cbar_pos: Any = (.02, .8, .05, .18),
               tree_kws: Any = None,
               **kwargs) -> ClusterGrid: ...