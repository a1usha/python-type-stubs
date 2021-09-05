from _decorators import _deprecate_positional_args as _deprecate_positional_args
from axisgrid import _facet_docs as _facet_docs
from axisgrid import FacetGrid as FacetGrid
from palettes import dark_palette as dark_palette
from palettes import light_palette as light_palette
from palettes import husl_palette as husl_palette
from palettes import color_palette as color_palette
from algorithms import bootstrap as bootstrap
from utils import remove_na as remove_na
from seaborn import utils as utils
from _core import categorical_order as categorical_order
from _core import infer_orient as infer_orient
from _core import variable_type as variable_type
from distutils.version import LooseVersion as LooseVersion
from matplotlib.collections import PatchCollection as PatchCollection
from scipy import stats as stats
from numbers import Number as Number
from textwrap import dedent as dedent
from typing import Any
from typing import Callable
from typing import ClassVar
from typing import Optional
from typing import Tuple
from typing import Union

from object import object
from seaborn.axisgrid import FacetGrid
from seaborn.categorical import _BarPlotter
from seaborn.categorical import _BoxPlotter
from seaborn.categorical import _CategoricalPlotter
from seaborn.categorical import _CategoricalScatterPlotter
from seaborn.categorical import _CategoricalStatPlotter
from seaborn.categorical import _LVPlotter
from seaborn.categorical import _PointPlotter
from seaborn.categorical import _StripPlotter
from seaborn.categorical import _SwarmPlotter
from seaborn.categorical import _ViolinPlotter

__all__: Any


class _CategoricalPlotter(object):
    width: ClassVar[float]
    default_palette: ClassVar[str]
    require_numeric: ClassVar[bool]
    value_label: Union[Optional[Hashable], Any]
    gray: Any
    orient: Union[str, Any]
    hue_names: Optional[list]
    plot_data: Union[list[Any], list[Union[Union[DataFrame, Series], Any]]]
    group_label: Union[Optional[Hashable], Any]
    plot_units: Optional[list[Union[Union[DataFrame, Series], Any]]]
    group_names: Union[Union[list[Any], list], Any]
    plot_hues: Optional[list[Union[Union[DataFrame, Series], Any]]]
    hue_title: Optional[Hashable]
    colors: Union[Union[_ColorPalette[Any], list[Any], list, _ColorPalette[tuple[float, float, float]], _ColorPalette[
        tuple]], Any]

    def establish_variables(self: _CategoricalPlotter,
                            x: Any = None,
                            y: Any = None,
                            hue: Any = None,
                            data: Any = None,
                            orient: Union[str, Any] = None,
                            order: Any = None,
                            hue_order: Any = None,
                            units: Any = None) -> Any: ...

    def _group_longform(self: _CategoricalPlotter,
                        vals: {groupby, name},
                        grouper: Any,
                        order: Union[list, Any]) -> Tuple[list[Union[Union[DataFrame, Series], Any]], Hashable]: ...

    def establish_colors(self: _CategoricalPlotter,
                         color: Optional[Any],
                         palette: Any,
                         saturation: Union[int, Any]) -> Any: ...

    def hue_offsets(self: _CategoricalPlotter) -> Any: ...

    def nested_width(self: _CategoricalPlotter) -> float: ...

    def annotate_axes(self: _CategoricalPlotter,
                      ax: Union[{autoscale_view}, Any]) -> None: ...

    def add_legend_data(self: _CategoricalPlotter,
                        ax: Union[Union[{fill_betweenx, fill_between}, {autoscale_view}], Any],
                        color: Any,
                        label: Any) -> None: ...


class _BoxPlotter(_CategoricalPlotter):
    dodge: Any
    fliersize: Any
    width: Any
    linewidth: Optional[Any]

    def __init__(self: _BoxPlotter,
                 x: Any,
                 y: Any,
                 hue: Any,
                 data: Any,
                 order: Any,
                 hue_order: Any,
                 orient: Any,
                 color: Any,
                 palette: Any,
                 saturation: Any,
                 width: Any,
                 dodge: Any,
                 fliersize: Any,
                 linewidth: Any) -> None: ...

    def draw_boxplot(self: _BoxPlotter,
                     ax: Any,
                     kws: {pop}) -> None: ...

    def restyle_boxplot(self: _BoxPlotter,
                        artist_dict: {__getitem__},
                        color: Any,
                        props: {__getitem__}) -> None: ...

    def plot(self: _BoxPlotter,
             ax: Any,
             boxplot_kws: {pop}) -> None: ...


class _ViolinPlotter(_CategoricalPlotter):
    dodge: Any
    split: Any
    gridsize: Any
    density: Union[list[Any], list[list[Any]]]
    width: Any
    inner: Optional[Any]
    linewidth: Optional[Any]
    support: Union[list[Union[Union[tuple[Any, Any, Any, Any], tuple[Any, Optional[float]]], Any]], list[list[Any]]]

    def __init__(self: _ViolinPlotter,
                 x: Any,
                 y: Any,
                 hue: Any,
                 data: Any,
                 order: Any,
                 hue_order: Any,
                 bw: Any,
                 cut: Any,
                 scale: {__eq__},
                 scale_hue: Any,
                 gridsize: Any,
                 width: Any,
                 inner: Any,
                 split: Any,
                 dodge: Any,
                 orient: Any,
                 linewidth: Any,
                 color: Any,
                 palette: Any,
                 saturation: Any) -> Any: ...

    def estimate_densities(self: _ViolinPlotter,
                           bw: Any,
                           cut: Any,
                           scale: {__eq__},
                           scale_hue: Any,
                           gridsize: Any) -> Any: ...

    def fit_kde(self: _ViolinPlotter,
                x: {std},
                bw: Any) -> Tuple[gaussian_kde, Union[float, Any]]: ...

    def kde_support(self: _ViolinPlotter,
                    x: {min, max},
                    bw: Union[float, Any],
                    cut: Any,
                    gridsize: Any) -> Union[Tuple[Any, Optional[float]], Any]: ...

    def scale_area(self: _ViolinPlotter,
                   density: Union[Union[list[Any], list[list[Any]]], Any],
                   max_density: Any,
                   scale_hue: Any) -> None: ...

    def scale_width(self: _ViolinPlotter,
                    density: Union[Union[list[Any], list[list[Any]]], Any]) -> None: ...

    def scale_count(self: _ViolinPlotter,
                    density: Union[Union[list[Any], list[list[Any]]], Any],
                    counts: Any,
                    scale_hue: Any) -> None: ...

    def dwidth(self: _ViolinPlotter) -> Union[float, Any]: ...

    def draw_violins(self: _ViolinPlotter,
                     ax: {fill_betweenx, fill_between}) -> None: ...

    def draw_single_observation(self: _ViolinPlotter,
                                ax: Union[{fill_betweenx, fill_between}, Any],
                                at_group: Union[int, Any],
                                at_quant: Any,
                                density: {__mul__}) -> None: ...

    def draw_box_lines(self: _ViolinPlotter,
                       ax: Union[{fill_betweenx, fill_between}, Any],
                       data: {__getitem__, __ge__, __le__},
                       support: Union[Optional[float], Any],
                       density: Any,
                       center: Any) -> None: ...

    def draw_quartiles(self: _ViolinPlotter,
                       ax: Union[{fill_betweenx, fill_between}, Any],
                       data: Any,
                       support: Union[Optional[float], Any],
                       density: {__getitem__},
                       center: Any,
                       split: bool = False) -> None: ...

    def draw_points(self: _ViolinPlotter,
                    ax: Union[{fill_betweenx, fill_between}, Any],
                    data: {__len__},
                    center: Union[int, Any]) -> None: ...

    def draw_stick_lines(self: _ViolinPlotter,
                         ax: Union[{fill_betweenx, fill_between}, Any],
                         data: {__iter__},
                         support: Union[Optional[float], Any],
                         density: {__getitem__},
                         center: Any,
                         split: bool = False) -> None: ...

    def draw_to_density(self: _ViolinPlotter,
                        ax: Union[{fill_betweenx, fill_between}, Any],
                        center: Union[int, Any],
                        val: Any,
                        support: Union[Union[tuple[Any, Any, Any, Any], tuple[Any, Optional[float]], float, None], Any],
                        density: {__getitem__},
                        split: Any,
                        **kwargs) -> None: ...

    def plot(self: _ViolinPlotter,
             ax: {fill_betweenx, fill_between}) -> None: ...


class _CategoricalScatterPlotter(_CategoricalPlotter):
    default_palette: ClassVar[str]
    require_numeric: ClassVar[bool]

    def point_colors(self: _CategoricalScatterPlotter) -> list[Union[Series, Any]]: ...

    def add_legend_data(self: _CategoricalScatterPlotter,
                        ax: Union[Union[{fill_betweenx, fill_between}, {autoscale_view}], Any]) -> None: ...


class _StripPlotter(_CategoricalScatterPlotter):
    dodge: Any
    jitterer: Any
    width: float

    def __init__(self: _StripPlotter,
                 x: Any,
                 y: Any,
                 hue: Any,
                 data: Any,
                 order: Any,
                 hue_order: Any,
                 jitter: {__eq__},
                 dodge: Any,
                 orient: Any,
                 color: Any,
                 palette: Any) -> None: ...

    def draw_stripplot(self: _StripPlotter,
                       ax: Union[{add_patch}, Any],
                       kws: Any) -> None: ...

    def plot(self: _StripPlotter,
             ax: {add_patch},
             kws: Any) -> None: ...


class _SwarmPlotter(_CategoricalScatterPlotter):
    dodge: Any
    width: float

    def __init__(self: _SwarmPlotter,
                 x: Any,
                 y: Any,
                 hue: Any,
                 data: Any,
                 order: Any,
                 hue_order: Any,
                 dodge: Any,
                 orient: Any,
                 color: Any,
                 palette: Any) -> None: ...

    def could_overlap(self: _SwarmPlotter,
                      xy_i: Any,
                      swarm: Any,
                      d: Any) -> Any: ...

    def position_candidates(self: _SwarmPlotter,
                            xy_i: Any,
                            neighbors: {__iter__},
                            d: {__pow__}) -> Any: ...

    def first_non_overlapping_candidate(self: _SwarmPlotter,
                                        candidates: {__iter__},
                                        neighbors: {__len__},
                                        d: Union[float, Any]) -> Any: ...

    def beeswarm(self: _SwarmPlotter,
                 orig_xy: {__getitem__},
                 d: {__pow__}) -> Any: ...

    def add_gutters(self: _SwarmPlotter,
                    points: {__lt__, __gt__, __len__},
                    center: Union[int, Any],
                    width: {__truediv__}) -> {__lt__, __gt__, __len__}: ...

    def swarm_points(self: _SwarmPlotter,
                     ax: Union[{add_patch}, Any],
                     points: {get_offsets, set_offsets},
                     center: Any,
                     width: Any,
                     s: Any,
                     **kwargs) -> None: ...

    def draw_swarmplot(self: _SwarmPlotter,
                       ax: Union[{add_patch}, Any],
                       kws: {pop}) -> None: ...

    def plot(self: _SwarmPlotter,
             ax: {autoscale_view, add_patch},
             kws: {pop}) -> None: ...


class _CategoricalStatPlotter(_CategoricalPlotter):
    require_numeric: ClassVar[bool]
    statistic: Any
    confint: Any

    def nested_width(self: _CategoricalStatPlotter) -> float: ...

    def estimate_statistic(self: _CategoricalStatPlotter,
                           estimator: Any,
                           ci: Any,
                           n_boot: Any,
                           seed: Any) -> None: ...

    def draw_confints(self: _CategoricalStatPlotter,
                      ax: Union[{bar, barh}, Any],
                      at_group: Any,
                      confint: Any,
                      colors: Union[list[Any], Any],
                      errwidth: Any = None,
                      capsize: Any = None,
                      **kwargs) -> None: ...


class _BarPlotter(_CategoricalStatPlotter):
    dodge: Any
    errcolor: Any
    errwidth: Any
    capsize: Any

    def __init__(self: _BarPlotter,
                 x: Any,
                 y: Any,
                 hue: Any,
                 data: Any,
                 order: Any,
                 hue_order: Any,
                 estimator: Any,
                 ci: Any,
                 n_boot: Any,
                 units: Any,
                 seed: Any,
                 orient: Any,
                 color: Any,
                 palette: Any,
                 saturation: Any,
                 errcolor: Any,
                 errwidth: Any,
                 capsize: Any,
                 dodge: Any) -> None: ...

    def draw_bars(self: _BarPlotter,
                  ax: {bar, barh},
                  kws: Any) -> None: ...

    def plot(self: _BarPlotter,
             ax: {bar, barh},
             bar_kws: Union[dict[str, Any], Any]) -> None: ...


class _PointPlotter(_CategoricalStatPlotter):
    default_palette: ClassVar[str]
    dodge: Union[float, Any]
    errwidth: Any
    scale: Any
    linestyles: Union[list[str], Any]
    join: Union[bool, Any]
    markers: Union[list[str], Any]
    capsize: Any
    colors: list[Any]

    def __init__(self: _PointPlotter,
                 x: Any,
                 y: Any,
                 hue: Any,
                 data: Any,
                 order: Any,
                 hue_order: Any,
                 estimator: Any,
                 ci: Any,
                 n_boot: Any,
                 units: Any,
                 seed: Any,
                 markers: Any,
                 linestyles: Any,
                 dodge: Any,
                 join: Any,
                 scale: Any,
                 orient: Any,
                 color: Any,
                 palette: Any,
                 errwidth: Any = None,
                 capsize: Any = None) -> None: ...

    def hue_offsets(self: _PointPlotter) -> Any: ...

    def draw_points(self: _PointPlotter,
                    ax: Any) -> None: ...

    def plot(self: _PointPlotter,
             ax: Any) -> None: ...


class _CountPlotter(_BarPlotter):
    require_numeric: ClassVar[bool]
    pass


class _LVPlotter(_CategoricalPlotter):
    saturation: Any
    outlier_prop: {__gt__, __le__}
    dodge: Any
    showfliers: bool
    width: Any
    k_depth: Number
    scale: Any
    trust_alpha: Any
    linewidth: Optional[Any]

    def __init__(self: _LVPlotter,
                 x: Any,
                 y: Any,
                 hue: Any,
                 data: Any,
                 order: Any,
                 hue_order: Any,
                 orient: Any,
                 color: Any,
                 palette: Any,
                 saturation: Any,
                 width: Any,
                 dodge: Any,
                 k_depth: Any,
                 linewidth: Any,
                 scale: Any,
                 outlier_prop: {__gt__, __le__},
                 trust_alpha: Any,
                 showfliers: bool = True) -> Any: ...

    def _lv_box_ends(self: _LVPlotter,
                     vals: Any) -> Tuple[list[Union[Union[int, float, complex], Any]], Union[int, Any]]: ...

    def _lv_outliers(self: _LVPlotter,
                     vals: {__getitem__, __lt__, __gt__},
                     k: {__add__}) -> Any: ...

    def _width_functions(self: _LVPlotter,
                         width_func: Any) -> Any: ...

    def _lvplot(self: _LVPlotter,
                box_data: Any,
                positions: Union[list[Union[int, Any]], Any],
                color: list[float] = [255. / 256., 185. / 256., 0.],
                widths: int = 1,
                ax: Any = None,
                **kwargs) -> None: ...

    def draw_letter_value_plot(self: _LVPlotter,
                               ax: {autoscale_view},
                               kws: Any) -> None: ...

    def plot(self: _LVPlotter,
             ax: {autoscale_view},
             boxplot_kws: Any) -> None: ...


_categorical_docs: dict[str, str]


def boxplot(*,
            x: Any = None,
            y: Any = None,
            hue: Any = None,
            data: Any = None,
            order: Any = None,
            hue_order: Any = None,
            orient: Any = None,
            color: Any = None,
            palette: Any = None,
            saturation: float = .75,
            width: float = .8,
            dodge: bool = True,
            fliersize: int = 5,
            linewidth: Any = None,
            whis: float = 1.5,
            ax: Any = None,
            **kwargs) -> Any: ...


def violinplot(*,
               x: Any = None,
               y: Any = None,
               hue: Any = None,
               data: Any = None,
               order: Any = None,
               hue_order: Any = None,
               bw: str = "scott",
               cut: int = 2,
               scale: str = "area",
               scale_hue: bool = True,
               gridsize: int = 100,
               width: float = .8,
               inner: str = "box",
               split: bool = False,
               dodge: bool = True,
               orient: Any = None,
               linewidth: Any = None,
               color: Any = None,
               palette: Any = None,
               saturation: float = .75,
               ax: Optional[{fill_betweenx, fill_between}] = None,
               **kwargs) -> Union[Optional[{fill_betweenx, fill_between}], Any]: ...


def boxenplot(*,
              x: Any = None,
              y: Any = None,
              hue: Any = None,
              data: Any = None,
              order: Any = None,
              hue_order: Any = None,
              orient: Any = None,
              color: Any = None,
              palette: Any = None,
              saturation: float = .75,
              width: float = .8,
              dodge: bool = True,
              k_depth: str = 'tukey',
              linewidth: Any = None,
              scale: str = 'exponential',
              outlier_prop: float = 0.007,
              trust_alpha: float = 0.05,
              showfliers: bool = True,
              ax: Optional[{autoscale_view}] = None,
              **kwargs) -> Union[Optional[{autoscale_view}], Any]: ...


def stripplot(*,
              x: Any = None,
              y: Any = None,
              hue: Any = None,
              data: Any = None,
              order: Any = None,
              hue_order: Any = None,
              jitter: bool = True,
              dodge: bool = False,
              orient: Any = None,
              color: Any = None,
              palette: Any = None,
              size: int = 5,
              edgecolor: str = "gray",
              linewidth: int = 0,
              ax: Optional[{add_patch}] = None,
              **kwargs) -> Union[Optional[{add_patch}], Any]: ...


def swarmplot(*,
              x: Any = None,
              y: Any = None,
              hue: Any = None,
              data: Any = None,
              order: Any = None,
              hue_order: Any = None,
              dodge: bool = False,
              orient: Any = None,
              color: Any = None,
              palette: Any = None,
              size: int = 5,
              edgecolor: str = "gray",
              linewidth: int = 0,
              ax: Optional[{autoscale_view, add_patch}] = None,
              **kwargs) -> Union[Optional[{autoscale_view, add_patch}], Any]: ...


def barplot(*,
            x: Any = None,
            y: Any = None,
            hue: Any = None,
            data: Any = None,
            order: Any = None,
            hue_order: Any = None,
            estimator: Callable[
                [Union[Union[Iterable, int, float], Any], Union[None, int, Iterable, tuple[int]], Optional[object], Any,
                 Optional[bool], Any, Union[Union[Iterable, int, float[bool], None], Any]], Any] = np.mean,
            ci: int = 95,
            n_boot: int = 1000,
            units: Any = None,
            seed: Any = None,
            orient: Any = None,
            color: Any = None,
            palette: Any = None,
            saturation: float = .75,
            errcolor: str = ".26",
            errwidth: Any = None,
            capsize: Any = None,
            dodge: bool = True,
            ax: Optional[{bar, barh}] = None,
            **kwargs) -> Union[Optional[{bar, barh}], Any]: ...


def pointplot(*,
              x: Any = None,
              y: Any = None,
              hue: Any = None,
              data: Any = None,
              order: Any = None,
              hue_order: Any = None,
              estimator: Callable[
                  [Union[Union[Iterable, int, float], Any], Union[None, int, Iterable, tuple[int]], Optional[object],
                   Any, Optional[bool], Any, Union[Union[Iterable, int, float[bool], None], Any]], Any] = np.mean,
              ci: int = 95,
              n_boot: int = 1000,
              units: Any = None,
              seed: Any = None,
              markers: str = "o",
              linestyles: str = "-",
              dodge: bool = False,
              join: bool = True,
              scale: int = 1,
              orient: Any = None,
              color: Any = None,
              palette: Any = None,
              errwidth: Any = None,
              capsize: Any = None,
              ax: Any = None,
              **kwargs) -> Any: ...


def countplot(*,
              x: Any = None,
              y: Any = None,
              hue: Any = None,
              data: Any = None,
              order: Any = None,
              hue_order: Any = None,
              orient: Any = None,
              color: Any = None,
              palette: Any = None,
              saturation: float = .75,
              dodge: bool = True,
              ax: Optional[{bar, barh}] = None,
              **kwargs) -> Union[Optional[{bar, barh}], Any]: ...


def factorplot(*args,
               **kwargs) -> Any: ...


def catplot(*,
            x: Any = None,
            y: Any = None,
            hue: Any = None,
            data: Any = None,
            row: Any = None,
            col: Any = None,
            col_wrap: Any = None,
            estimator: Callable[
                [Union[Union[Iterable, int, float], Any], Union[None, int, Iterable, tuple[int]], Optional[object], Any,
                 Optional[bool], Any, Union[Union[Iterable, int, float[bool], None], Any]], Any] = np.mean,
            ci: int = 95,
            n_boot: int = 1000,
            units: Any = None,
            seed: Any = None,
            order: Any = None,
            hue_order: Any = None,
            row_order: Any = None,
            col_order: Any = None,
            kind: str = "strip",
            height: int = 5,
            aspect: int = 1,
            orient: Any = None,
            color: Any = None,
            palette: Any = None,
            legend: bool = True,
            legend_out: bool = True,
            sharex: bool = True,
            sharey: bool = True,
            margin_titles: bool = False,
            facet_kws: Any = None,
            **kwargs) -> Union[FacetGrid, Any]: ...