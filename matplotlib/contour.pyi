from numbers import Integral
from typing import Any
from typing import Iterable
from typing import Optional
from typing import Tuple
from typing import Union

from matplotlib import _api
from matplotlib.cm import ScalarMappable
from matplotlib.contour import ClabelText
from matplotlib.contour import ContourLabeler
from matplotlib.contour import ContourSet
from matplotlib.contour import QuadContourSet
from matplotlib.text import Text
from matplotlib.ticker import ScalarFormatter
from numpy.core._multiarray_umath import ndarray
from numpy.ma.core import MaskedArray
from object import object


class ClabelText(Text):
    def get_rotation(self: ClabelText) -> Any: ...


class ContourLabeler(object):
    def clabel(self: ContourLabeler,
               levels: Union[ndarray, Iterable, int, float, None] = None,
               *,
               fontsize: Union[str, float] = None,
               inline: bool = True,
               inline_spacing: float = 5,
               fmt: Any = None,
               colors: Optional[Any] = None,
               use_clabeltext: bool = False,
               manual: Union[bool, Any] = False,
               rightside_up: bool = True,
               zorder: Optional[float] = None) -> Any: ...

    def print_label(self: ContourLabeler,
                    linecontour: {__len__},
                    labelwidth: Any) -> Union[bool, Any]: ...

    def too_close(self: ContourLabeler,
                  x: Optional[Any],
                  y: Optional[Any],
                  lw: Any) -> bool: ...

    @_api.deprecated("3.4")
    def get_label_coords(self: ContourLabeler,
                         distances: Any,
                         XX: {__getitem__},
                         YY: {__getitem__},
                         ysize: {__truediv__},
                         lw: Any) -> Union[Union[Tuple[Any, Any, Any], Tuple[Any, Any, None]], Any]: ...

    def get_label_width(self: ContourLabeler,
                        lev: Any,
                        fmt: Union[ScalarFormatter, Any],
                        fsize: Any) -> Any: ...

    def set_label_props(self: ContourLabeler,
                        label: Union[Union[Text, ClabelText], Any],
                        text: Any,
                        color: Any) -> None: ...

    def get_text(self: ContourLabeler,
                 lev: Any,
                 fmt: Union[ScalarFormatter, Any]) -> Union[str, Any]: ...

    def locate_label(self: ContourLabeler,
                     linecontour: {__len__},
                     labelwidth: {__gt__}) -> Tuple[None, None, Union[int, Any]]: ...

    def calc_label_rot_and_inline(self: ContourLabeler,
                                  slc: {__getitem__, shape, T},
                                  ind: Union[int, Any],
                                  lw: {__truediv__},
                                  lc: Optional[{__len__}] = None,
                                  spacing: int = 5) -> Tuple[Optional[int], list[ndarray]]: ...

    def _get_label_text(self: ContourLabeler,
                        x: Any,
                        y: Any,
                        rotation: Any) -> Text: ...

    def _get_label_clabeltext(self: ContourLabeler,
                              x: Any,
                              y: Any,
                              rotation: Any) -> ClabelText: ...

    def _add_label(self: ContourLabeler,
                   t: Union[Union[Text, ClabelText], Any],
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
               inline: Union[bool, Any],
               inline_spacing: Any) -> None: ...


def _is_closed_polygon(X: Union[{shape, T}, Any]) -> bool: ...


def _find_closest_point_on_path(xys: int,
                                p: tuple[float, float]) -> float: ...


class ContourSet(ScalarMappable, ContourLabeler):
    def __init__(self: ContourSet,
                 ax: Any,
                 levels: Any = None,
                 filled: bool = False,
                 linewidths: Any = None,
                 linestyles: Any = None,
                 hatches: Union[tuple[None], Any] = (None,),
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

    def _get_allsegs_and_allkinds(self: ContourSet) -> Tuple[Any, list[None]]: ...

    def _get_lowers_and_uppers(self: ContourSet) -> Tuple[list[Union[float, Any]], list[Union[float, Any]]]: ...

    def _make_paths(self: ContourSet,
                    segs: Any,
                    kinds: Any) -> list[Path]: ...

    def changed(self: ContourSet) -> None: ...

    def _autolev(self: ContourSet,
                 N: Union[Integral, Any]) -> Union[Union[None, ndarray, {__len__}], Any]: ...

    def _process_contour_level_args(self: ContourSet,
                                    args: Union[tuple[Any, ...], Any]) -> Any: ...

    def _process_levels(self: ContourSet) -> None: ...

    def _process_colors(self: ContourSet) -> None: ...

    def _process_linewidths(self: ContourSet) -> Union[list[Tuple[Optional[Any]]], list[Tuple[Any]]]: ...

    def _process_linestyles(self: ContourSet) -> Union[Union[list[str], list[Optional[Any]]], Any]: ...

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

    def _get_allsegs_and_allkinds(self: QuadContourSet) -> Tuple[list[Optional[Any]], Optional[list[Any]]]: ...

    def _contour_args(self: QuadContourSet,
                      args: Union[tuple[Any, ...], Any],
                      kwargs: Any) -> Tuple[Union[ndarray, Any], Union[ndarray, Any], Optional[MaskedArray]]: ...

    def _check_xyz(self: QuadContourSet,
                   args: Union[tuple[Any, ...], Any],
                   kwargs: Any) -> Tuple[Union[ndarray, Any], Union[ndarray, Any], MaskedArray]: ...

    def _initialize_x_y(self: QuadContourSet,
                        z: Union[MaskedArray, Any]) -> str: ...
