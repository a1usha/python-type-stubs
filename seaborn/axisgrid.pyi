from _docstrings import _core_docs as _core_docs
from _docstrings import DocstringComponents as DocstringComponents
from _decorators import _deprecate_positional_args as _deprecate_positional_args
from palettes import blend_palette as blend_palette
from palettes import color_palette as color_palette
from utils import _draw_figure as _draw_figure
from utils import adjust_legend_subtitles as adjust_legend_subtitles
from utils import _check_argument as _check_argument
from seaborn import utils as utils
from _core import categorical_order as categorical_order
from _core import variable_type as variable_type
from _core import VectorPlotter as VectorPlotter
from distutils.version import LooseVersion as LooseVersion
from textwrap import dedent as dedent
from inspect import signature as signature
from itertools import product as product
from typing import Any
from typing import ClassVar
from typing import Generator
from typing import Optional
from typing import Tuple
from typing import Union

from object import object
from pandas.core.frame import DataFrame
from seaborn.axisgrid import FacetGrid
from seaborn.axisgrid import Grid
from seaborn.axisgrid import JointGrid
from seaborn.axisgrid import PairGrid
from seaborn.axisgrid import _BaseGrid
from seaborn.palettes import _ColorPalette

_param_docs: DocstringComponents
__all__: Any


class _BaseGrid(object):
    def set(self: _BaseGrid,
            **kwargs) -> _BaseGrid: ...

    def fig(self: _BaseGrid) -> Any: ...

    def figure(self: _BaseGrid) -> Any: ...

    def savefig(self: _BaseGrid,
                *args,
                **kwargs) -> None: ...


class Grid(_BaseGrid):
    _margin_titles: ClassVar[bool]
    _legend_out: ClassVar[bool]
    _legend: Any
    _tight_layout_rect: list[int]
    _tight_layout_pad: None
    _extract_legend_handles: bool
    _space_needed: Union[float, Any]

    def __init__(self: Grid) -> None: ...

    def tight_layout(self: Grid,
                     *args,
                     **kwargs) -> None: ...

    def add_legend(self: Grid,
                   legend_data: dict = None,
                   title: str = None,
                   label_order: list = None,
                   adjust_subtitles: bool = False,
                   **kwargs) -> Any: ...

    def _update_legend_data(self: Grid,
                            ax: {legend_, get_legend_handles_labels}) -> None: ...

    def _get_palette(self: Grid,
                     data: Union[{__len__}, Any],
                     hue: Optional[Any],
                     hue_order: Any,
                     palette: Any) -> Union[Union[_ColorPalette[Any], list[Any], list, _ColorPalette[
        Tuple[float, float, float]], _ColorPalette[Tuple]], Any]: ...

    def legend(self: Grid) -> Optional[Any]: ...


_facet_docs: dict[str, str]


class FacetGrid(Grid):
    _col_wrap: Optional[Any]
    data: {__len__}
    _x_var: None
    _n_facets: int
    _col_var: Optional[Any]
    _not_na: Any
    _dropna: bool
    _legend_out: bool
    _y_var: None
    _legend: None
    row_names: Union[list[Any], list]
    col_names: Union[list[Any], list]
    _hue_var: Any
    _ncol: Union[int, Any]
    _colors: Union[Union[_ColorPalette[Any], list[Any], list, _ColorPalette[tuple[float, float, float]], _ColorPalette[
        tuple]], Any]
    _legend_data: dict[Any, Any]
    _nrow: int
    hue_names: Optional[list]
    _axes_dict: Union[dict[Any, Any], dict[tuple[Any, Any], Any]]
    hue_kws: Union[dict[Any, Any], Any]
    _axes: Any
    _margin_titles_texts: list[Any]
    _margin_titles: bool
    _figure: Any
    _row_var: Optional[Any]

    def __init__(self: FacetGrid,
                 data: {__len__},
                 *,
                 row: Any = None,
                 col: Any = None,
                 hue: Any = None,
                 col_wrap: Any = None,
                 sharex: bool = True,
                 sharey: bool = True,
                 height: int = 3,
                 aspect: int = 1,
                 palette: Any = None,
                 row_order: Any = None,
                 col_order: Any = None,
                 hue_order: Any = None,
                 hue_kws: Any = None,
                 dropna: bool = False,
                 legend_out: bool = True,
                 despine: bool = True,
                 margin_titles: bool = False,
                 xlim: Any = None,
                 ylim: Any = None,
                 subplot_kws: Any = None,
                 gridspec_kws: Any = None,
                 size: Any = None) -> Any: ...

    def facet_data(self: FacetGrid) -> Generator[Tuple[Tuple[Any, Any, Any], Any], Any, None]: ...

    def map(self: FacetGrid,
            func: Any,
            *args,
            **kwargs) -> object: ...

    def map_dataframe(self: FacetGrid,
                      func: Any,
                      *args,
                      **kwargs) -> object: ...

    def _facet_color(self: FacetGrid,
                     hue_index: Any,
                     kw_color: Optional[Any]) -> Union[Optional[list[Any]], Any]: ...

    def _facet_plot(self: FacetGrid,
                    func: {__module__},
                    ax: {legend_, get_legend_handles_labels},
                    plot_args: Any,
                    plot_kwargs: Any) -> None: ...

    def _finalize_grid(self: FacetGrid,
                       axlabels: Union[Union[tuple[Any, ...], list[Optional[Any]]], Any]) -> None: ...

    def facet_axis(self: FacetGrid,
                   row_i: Any,
                   col_j: Any,
                   modify_state: bool = True) -> Any: ...

    def despine(self: FacetGrid,
                **kwargs) -> FacetGrid: ...

    def set_axis_labels(self: FacetGrid,
                        x_var: Any = None,
                        y_var: Any = None,
                        clear_inner: bool = True,
                        **kwargs) -> FacetGrid: ...

    def set_xlabels(self: FacetGrid,
                    label: Any = None,
                    clear_inner: bool = True,
                    **kwargs) -> FacetGrid: ...

    def set_ylabels(self: FacetGrid,
                    label: Any = None,
                    clear_inner: bool = True,
                    **kwargs) -> FacetGrid: ...

    def set_xticklabels(self: FacetGrid,
                        labels: Any = None,
                        step: Any = None,
                        **kwargs) -> FacetGrid: ...

    def set_yticklabels(self: FacetGrid,
                        labels: Any = None,
                        **kwargs) -> FacetGrid: ...

    def set_titles(self: FacetGrid,
                   template: str = None,
                   row_template: Any = None,
                   col_template: Any = None,
                   **kwargs) -> object: ...

    def refline(self: FacetGrid,
                *,
                x: Any = None,
                y: Any = None,
                color: Any = '.5',
                linestyle: str = '--',
                **kwargs) -> Any: ...

    def axes(self: FacetGrid) -> Any: ...

    def ax(self: FacetGrid) -> Any: ...

    def axes_dict(self: FacetGrid) -> Union[dict[Any, Any], dict[Tuple[Any, Any], Any]]: ...

    def _inner_axes(self: FacetGrid) -> Any: ...

    def _left_axes(self: FacetGrid) -> Any: ...

    def _not_left_axes(self: FacetGrid) -> Any: ...

    def _bottom_axes(self: FacetGrid) -> Any: ...

    def _not_bottom_axes(self: FacetGrid) -> Any: ...


class PairGrid(Grid):
    _legend_data: dict[Any, Any]
    _despine: bool
    square_grid: bool
    x_vars: list[list[Any]]
    data: Any
    _corner: bool
    hue_names: Union[list[Any], list]
    diag_axes: None
    hue_vals: Any
    axes: Any
    diag_vars: None
    _tight_layout_pad: Any
    hue_kws: Union[dict[Any, Any], Any]
    _orig_palette: Any
    _dropna: bool
    _hue_order: Union[list[str], list]
    _figure: Any
    _tight_layout_rect: list[float]
    palette: Union[Union[_ColorPalette[Any], list[Any], list, _ColorPalette[tuple[float, float, float]], _ColorPalette[
        tuple]], Any]
    _hue_var: Any
    _extract_legend_handles: bool
    y_vars: list[list[Any]]
    diag_sharey: bool

    def __init__(self: PairGrid,
                 data: Any,
                 *,
                 hue: Any = None,
                 hue_order: list = None,
                 palette: Any = None,
                 hue_kws: Any = None,
                 vars: Any = None,
                 x_vars: Any = None,
                 y_vars: Any = None,
                 corner: bool = False,
                 diag_sharey: bool = True,
                 height: Any = 2.5,
                 aspect: Any = 1,
                 layout_pad: Any = .5,
                 despine: bool = True,
                 dropna: bool = False,
                 size: Any = None) -> Any: ...

    def map(self: PairGrid,
            func: Any,
            **kwargs) -> PairGrid: ...

    def map_lower(self: PairGrid,
                  func: Any,
                  **kwargs) -> PairGrid: ...

    def map_upper(self: PairGrid,
                  func: Any,
                  **kwargs) -> PairGrid: ...

    def map_offdiag(self: PairGrid,
                    func: Any,
                    **kwargs) -> PairGrid: ...

    def map_diag(self: PairGrid,
                 func: Any,
                 **kwargs) -> PairGrid: ...

    def _map_diag_iter_hue(self: PairGrid,
                           func: {__module__},
                           **kwargs) -> PairGrid: ...

    def _map_bivariate(self: PairGrid,
                       func: {__module__},
                       indices: Union[Union[zip[tuple[Any]], zip[tuple[Any, Any]], zip[tuple[Any, Any, Any]], zip[
                           tuple[Any, Any, Any, Any]], zip[tuple[Any, Any, Any, Any, Any]], list[
                                                tuple[int, int]]], Any],
                       **kwargs) -> None: ...

    def _plot_bivariate(self: PairGrid,
                        x_var: Union[Union[list[Any], list[list[Any]]], Any],
                        y_var: Any,
                        ax: {legend_, get_legend_handles_labels},
                        func: {__module__},
                        **kwargs) -> None: ...

    def _plot_bivariate_iter_hue(self: PairGrid,
                                 x_var: Union[{__eq__}, Any],
                                 y_var: Any,
                                 ax: {legend_, get_legend_handles_labels},
                                 func: {__module__},
                                 **kwargs) -> None: ...

    def _add_axis_labels(self: PairGrid) -> None: ...

    def _find_numeric_cols(self: PairGrid,
                           data: {__iter__, __getitem__}) -> list[Any]: ...


class JointGrid(_BaseGrid):
    _hue_params: dict[str, Any]
    ax_joint: Any
    _figure: Any
    x: Optional[Any]
    y: Optional[Any]
    hue: Optional[Any]
    ax_marg_y: Any
    ax_marg_x: Any

    def __init__(self: JointGrid,
                 *,
                 x: Any = None,
                 y: Any = None,
                 data: Any = None,
                 height: int = 6,
                 ratio: int = 5,
                 space: float = .2,
                 dropna: bool = False,
                 xlim: Any = None,
                 ylim: Any = None,
                 size: Any = None,
                 marginal_ticks: bool = False,
                 hue: Any = None,
                 palette: Any = None,
                 hue_order: Any = None,
                 hue_norm: Any = None) -> Optional[Any]: ...

    def _inject_kwargs(self: JointGrid,
                       func: Any,
                       kws: Union[dict[str, Any], Any],
                       params: {items}) -> None: ...

    def plot(self: JointGrid,
             joint_func: Any,
             marginal_func: Any,
             **kwargs) -> Any: ...

    def plot_joint(self: JointGrid,
                   func: Any,
                   **kwargs) -> Any: ...

    def plot_marginals(self: JointGrid,
                       func: Any,
                       **kwargs) -> Any: ...

    def refline(self: JointGrid,
                *,
                x: Any = None,
                y: Any = None,
                joint: Any = True,
                marginal: Any = True,
                color: Any = '.5',
                linestyle: str = '--',
                **kwargs) -> Any: ...

    def set_axis_labels(self: JointGrid,
                        xlabel: Any = "",
                        ylabel: Any = "",
                        **kwargs) -> Any: ...


def pairplot(data: DataFrame,
             *,
             hue: Any = None,
             hue_order: list = None,
             palette: Any = None,
             vars: Any = None,
             x_vars: Any = None,
             y_vars: Any = None,
             kind: Any = "scatter",
             diag_kind: Any = "auto",
             markers: Any = None,
             height: Any = 2.5,
             aspect: Any = 1,
             corner: bool = False,
             dropna: bool = False,
             plot_kws: Any = None,
             diag_kws: Any = None,
             grid_kws: Any = None,
             size: Any = None) -> PairGrid: ...


def jointplot(*,
              x: Any = None,
              y: Any = None,
              data: Any = None,
              kind: str = "scatter",
              color: Any = None,
              height: int = 6,
              ratio: int = 5,
              space: float = .2,
              dropna: bool = False,
              xlim: Any = None,
              ylim: Any = None,
              marginal_ticks: bool = False,
              joint_kws: Any = None,
              marginal_kws: Any = None,
              hue: Any = None,
              palette: Any = None,
              hue_order: Any = None,
              hue_norm: Any = None,
              **kwargs) -> Union[JointGrid, Any]: ...