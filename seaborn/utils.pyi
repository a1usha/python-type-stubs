from matplotlib.cbook import normalize_kwargs as normalize_kwargs
from scipy import stats as stats
from urllib.request import urlretrieve as urlretrieve
from urllib.request import urlopen as urlopen
from typing import Any
from typing import Optional
from typing import Tuple
from typing import Union

from pandas.core.frame import DataFrame

__all__: Any


def sort_df(*args,
            df: {sort_values, sort},
            **kwargs) -> Any: ...


def ci_to_errsize(cis: Any,
                  heights: Any) -> Any: ...


def pmf_hist(a: Any,
             bins: int = 10) -> array.pyi: ...


def _draw_figure(fig: {canvas, stale}) -> None: ...


def desaturate(color: Any,
               prop: float) -> Any: ...


def saturate(color: Any) -> Any: ...


def set_hls_values(color: Any,
                   h: Any = None,
                   l: Any = None,
                   s: Any = None) -> Any: ...


def axlabel(xlabel: Any,
            ylabel: Any,
            **kwargs) -> None: ...


def remove_na(vector: Any) -> Any: ...


def get_color_cycle() -> list: ...


def despine(fig: Any = None,
            ax: Any = None,
            top: bool = True,
            right: bool = True,
            left: bool = False,
            bottom: bool = False,
            offset: Any = None,
            trim: bool = False) -> None: ...


def move_legend(obj: Any,
                loc: Union[str, int],
                **kwargs) -> Any: ...


def _kde_support(data: {min, max},
                 bw: {__mul__},
                 gridsize: Any,
                 cut: Any,
                 clip: {__getitem__}) -> Union[Tuple[Any, Optional[float]], Any]: ...


def percentiles(a: array.pyi,
                pcts: Any,
                axis: Optional[int] = None) -> array.pyi: ...


def ci(a: Any,
       which: int = 95,
       axis: Any = None) -> Union[Union[int, float, complex], Any]: ...


def sig_stars(p: {__lt__}) -> str: ...


def iqr(a: Any) -> Union[float, Any]: ...


def get_dataset_names() -> list[Any]: ...


def get_data_home(data_home: Any = None) -> Union[str, Any]: ...


def load_dataset(name: str,
                 cache: Any = True,
                 data_home: Any = None,
                 **kwargs) -> DataFrame: ...


def axis_ticklabels_overlap(labels: Any) -> bool: ...


def axes_ticklabels_overlap(ax: Any) -> Any: ...


def locator_to_legend_entries(locator: {tick_values},
                              limits: {__getitem__},
                              dtype: Any) -> Tuple[list[Any], list[Any]]: ...


def relative_luminance(color: Any) -> Any: ...


def to_utf8(obj: object) -> str: ...


def _normalize_kwargs(kws: Any,
                      artist: Any) -> Union[Union[dict[Any, Any], dict[Any, Any]], Any]: ...


def _check_argument(param: Any,
                    options: Any,
                    value: Any) -> Any: ...


def _assign_default_kwargs(kws: Any,
                           call_func: Any,
                           source_func: Any) -> Any: ...


def adjust_legend_subtitles(legend: {findobj}) -> None: ...