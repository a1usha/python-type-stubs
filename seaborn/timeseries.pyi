from palettes import color_palette as color_palette
from seaborn import algorithms as algo
from seaborn import utils as utils
from external.six import string_types as string_types
from scipy import interpolate as interpolate
from scipy import stats as stats
from __future__ import division as division
from typing import Any
from typing import Union

__all__: Any


def tsplot(data: Any,
           time: Any = None,
           unit: str = None,
           condition: Any = None,
           value: str = None,
           err_style: Union[str, list, None] = "ci_band",
           ci: Any = 68,
           interpolate: bool = True,
           color: Any = None,
           estimator: Any = np.mean,
           n_boot: int = 5000,
           err_palette: Any = None,
           err_kws: Any = None,
           legend: Any = True,
           ax: Any = None,
           **kwargs) -> Any: ...


def _plot_ci_band(ax: {fill_between},
                  x: Any,
                  ci: Any,
                  color: Any,
                  err_kws: Any,
                  **kwargs) -> None: ...


def _plot_ci_bars(ax: {plot},
                  x: Any,
                  central_data: Any,
                  ci: {T},
                  color: Any,
                  err_kws: Any,
                  **kwargs) -> None: ...


def _plot_boot_traces(ax: {plot},
                      x: Any,
                      boot_data: {T},
                      color: Any,
                      err_kws: {setdefault, __contains__},
                      **kwargs) -> None: ...


def _plot_unit_traces(ax: Any,
                      x: Any,
                      data: Any,
                      ci: Any,
                      color: Any,
                      err_kws: Any,
                      **kwargs) -> None: ...


def _plot_unit_points(ax: Any,
                      x: Any,
                      data: Any,
                      color: Any,
                      err_kws: Any,
                      **kwargs) -> None: ...


def _plot_boot_kde(ax: {imshow},
                   x: Any,
                   boot_data: Any,
                   color: Any,
                   **kwargs) -> None: ...


def _plot_unit_kde(ax: {imshow},
                   x: Any,
                   data: Any,
                   color: Any,
                   **kwargs) -> None: ...


def _ts_kde(ax: {imshow},
            x: {min, max},
            data: {min, max},
            color: Any,
            **kwargs) -> None: ...