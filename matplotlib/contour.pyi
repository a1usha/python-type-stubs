from numbers import Integral
from typing import Any
from typing import Iterable
from typing import Optional
from typing import Union
from typing import tuple

from matplotlib.contour import ClabelText
from matplotlib.text import Text
from matplotlib.ticker import ScalarFormatter
from numpy.core._multiarray_umath import ndarray
from numpy.ma.core import MaskedArray


class ContourLabeler(object):
    def clabel(self: ContourLabeler,
               levels: Union[ndarray, Iterable, int, float, None] = None,
               fontsize: Union[str, float] = None,
               inline: bool = True,
               inline_spacing: float = 5,
               fmt: Any = None,
               colors: Optional[Any] = None,
               use_clabeltext: bool = False,
               manual: bool = False,
               rightside_up: bool = True,
               zorder: Optional[float] = None) -> Any: ...

    def print_label(self: ContourLabeler,
                    linecontour: {__len__},
                    labelwidth: Any) -> bool: ...

    def too_close(self: ContourLabeler,
                  x: Optional[Any],
                  y: Optional[Any],
                  lw: Any) -> bool: ...

    @_api.deprecated
    def get_label_coords(self: ContourLabeler,
                         distances: Any,
                         XX: {__getitem__},
                         YY: {__getitem__},
                         ysize: {__truediv__},
                         lw: Any) -> Union[tuple[Any, Any, Any], tuple[Any, Any, None]]: ...

    def get_label_width(self: ContourLabeler,
                        lev: Any,
                        fmt: ScalarFormatter,
                        fsize: Any) -> Any: ...

    def set_label_props(self: ContourLabeler,
                        label: Union[Text, ClabelText],
                        text: Any,
                        color: Any) -> None: ...

    def get_text(self: ContourLabeler,
                 lev: Any,
                 fmt: ScalarFormatter) -> str: ...

    def locate_label(self: ContourLabeler,
                     linecontour: {__len__},
                     labelwidth: {__gt__}) -> tuple[None, None, int]: ...

    def calc_label_rot_and_inline(self: ContourLabeler,
                                  slc: {__getitem__, shape, T},
                                  ind: int,
                                  lw: {__truediv__},
                                  lc: Optional[{__len__}] = None,
                                  spacing: int = 5) -> tuple[Optional[int], list[ndarray]]: ...

    def _get_label_text(self: ContourLabeler,
                        x: Any,
                        y: Any,
                        rotation: Any) -> Text: ...

    def _get_label_clabeltext(self: ContourLabeler,
                              x: Any,
                              y: Any,
                              rotation: Any) -> ClabelText: ...

    def _add_label(self: ContourLabeler,
                   t: ClabelText,
                   x: Any,
                   y: Any,
                   lev: Any,
                   cvalue: Any) -> None: ...

    def add_label(self: ContourLabeler,
                  x: Any,
                  y: Any,
                  rotation: Any,
                  lev: Any,
                  cvalue: Any) -> None: ...

    def add_label_clabeltext(self: ContourLabeler,
                             x: Any,
                             y: Any,
                             rotation: Any,
                             lev: Any,
                             cvalue: Any) -> None: ...

    def add_label_near(self: ContourLabeler,
                       x: float,
                       y: float,
                       inline: bool = True,
                       inline_spacing: int = 5,
                       transform: Any = None) -> None: ...

    def pop_label(self: ContourLabeler,
                  index: int = -1) -> None: ...

    def labels(self: ContourLabeler,
               inline: bool,
               inline_spacing: Any) -> None: ...


class ContourSet(ScalarMappable, ContourLabeler):
    def __init__(self: ContourSet,
                 ax: Any,
                 levels: Any = None,
                 filled: bool = False,
                 linewidths: Any = None,
                 linestyles: Any = None,
                 hatches: tuple[None] = (None,),
                 alpha: Any = None,
                 origin: Any = None,
                 extent: Any = None,
                 cmap: Any = None,
                 colors: Any = None,
                 norm: Any = None,
                 vmin: Any = None,
                 vmax: Any = None,
                 extend: str = 'neither',
                 antialiased: Any = None,
                 nchunk: int = 0,
                 locator: Any = None,
                 transform: Any = None,
                 *args,
                 **kwargs) -> Any: ...

    def get_transform(self: ContourSet) -> Any: ...

    def __getstate__(self: ContourSet) -> dict[str, Any]: ...

    def legend_elements(self: ContourSet,
                        variable_name: str = 'x',
                        str_format: Any = str) -> Any: ...

    def _process_args(self: ContourSet,
                      *args,
                      **kwargs) -> dict[str, Any]: ...

    def _get_allsegs_and_allkinds(self: ContourSet) -> tuple[Any, list[None]]: ...

    def _get_lowers_and_uppers(self: ContourSet) -> tuple[list[float], list[float]]: ...

    def _make_paths(self: ContourSet,
                    segs: Any,
                    kinds: Any) -> list[Path]: ...

    def changed(self: ContourSet) -> None: ...

    def _autolev(self: ContourSet,
                 N: Integral) -> Union[None, ndarray, {__len__}]: ...

    def _process_contour_level_args(self: ContourSet,
                                    args: tuple[Any, ...]) -> Any: ...

    def _process_levels(self: ContourSet) -> None: ...

    def _process_colors(self: ContourSet) -> None: ...

    def _process_linewidths(self: ContourSet) -> Union[list[tuple[Optional[Any]]], list[tuple[Any]]]: ...

    def _process_linestyles(self: ContourSet) -> Union[list[str], list[Optional[Any]]]: ...

    def get_alpha(self: ContourSet) -> Any: ...

    def set_alpha(self: ContourSet,
                  alpha: Any) -> None: ...

    def find_nearest_contour(self: ContourSet,
                             x: float,
                             y: float,
                             indices: Optional[Iterable[int]] = None,
                             pixel: bool = True) -> Any: ...


class QuadContourSet(ContourSet):
    def _process_args(self: QuadContourSet,
                      corner_mask: Any = None,
                      *args,
                      **kwargs) -> dict[str, Any]: ...

    def _get_allsegs_and_allkinds(self: QuadContourSet) -> tuple[list[Optional[Any]], Optional[list]]: ...

    def _contour_args(self: QuadContourSet,
                      args: tuple[Any, ...],
                      kwargs: Any) -> tuple[ndarray, ndarray, Optional[MaskedArray]]: ...

    def _check_xyz(self: QuadContourSet,
                   args: tuple[Any, ...],
                   kwargs: Any) -> tuple[ndarray, ndarray, MaskedArray]: ...

    def _initialize_x_y(self: QuadContourSet,
                        z: MaskedArray) -> str: ...


class ClabelText(Text):
    def get_rotation(self: ClabelText) -> Any: ...


def _is_closed_polygon(X: {shape, T}) -> bool: ...


def _find_closest_point_on_path(xys: int,
                                p: tuple[float, float]) -> float: ...