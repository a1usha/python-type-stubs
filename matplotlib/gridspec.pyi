from matplotlib.transforms import Bbox as Bbox
from matplotlib import rcParams as rcParams
from matplotlib import tight_layout as tight_layout
from matplotlib import _pylab_helpers as _pylab_helpers
from matplotlib import _api as _api
from numbers import Integral as Integral
from typing import ClassVar
from typing import Optional
from typing import Tuple
from typing import Union

from matplotlib import _api
from matplotlib.gridspec import GridSpec
from matplotlib.gridspec import GridSpecBase
from matplotlib.gridspec import GridSpecFromSubplotSpec
from matplotlib.gridspec import SubplotSpec
from matplotlib.transforms import Bbox
from numpy.core._multiarray_umath import ndarray
from object import object

_log: Logger
from typing import Any


class GridSpecBase(object):
    nrows: ClassVar[property]
    ncols: ClassVar[property]
    _row_height_ratios: Union[list[int], Any]
    _col_width_ratios: Union[list[int], Any]
    _nrows: int
    _ncols: int

    def __init__(self: GridSpecBase,
                 nrows: int,
                 ncols: int,
                 height_ratios: Any = None,
                 width_ratios: Any = None) -> Any: ...

    def __repr__(self: GridSpecBase) -> str: ...

    def get_geometry(self: GridSpecBase) -> Tuple[int, int]: ...

    def get_subplot_params(self: GridSpecBase,
                           figure: Any = None) -> None: ...

    def new_subplotspec(self: GridSpecBase,
                        loc: tuple[int, int],
                        rowspan: int = 1,
                        colspan: int = 1) -> SubplotSpec: ...

    def set_width_ratios(self: GridSpecBase,
                         width_ratios: Optional[{__len__}]) -> Any: ...

    def get_width_ratios(self: GridSpecBase) -> Union[list[int], Any]: ...

    def set_height_ratios(self: GridSpecBase,
                          height_ratios: Optional[{__len__}]) -> Any: ...

    def get_height_ratios(self: GridSpecBase) -> Union[list[int], Any]: ...

    def get_grid_positions(self: GridSpecBase,
                           fig: Any,
                           raw: bool = False) -> array.pyi: ...

    def _check_gridspec_exists(figure: {get_axes},
                               nrows: Any,
                               ncols: Any) -> Union[GridSpec, Any]: ...

    def __getitem__(self: GridSpecBase,
                    key: Any) -> SubplotSpec: ...

    def subplots(self: GridSpecBase,
                 *,
                 sharex: bool = False,
                 sharey: bool = False,
                 squeeze: bool = True,
                 subplot_kw: Any = None) -> Union[int, float, complex, None, ndarray]: ...


class GridSpec(GridSpecBase):
    _AllowedKeys: ClassVar[list[str]]
    figure: Any
    top: Optional[float]
    left: Optional[float]
    bottom: Optional[float]
    wspace: Optional[float]
    _toplayoutbox: Any
    right: Optional[float]
    _layoutgrid: LayoutGrid
    hspace: Optional[float]

    def __init__(self: GridSpec,
                 nrows: int,
                 ncols: int,
                 figure: Any = None,
                 left: Optional[float] = None,
                 bottom: Optional[float] = None,
                 right: Optional[float] = None,
                 top: Optional[float] = None,
                 wspace: Optional[float] = None,
                 hspace: Optional[float] = None,
                 width_ratios: Any = None,
                 height_ratios: Any = None) -> None: ...

    def __getstate__(self: GridSpec) -> dict[str, None]: ...

    def update(self: GridSpec,
               **kwargs) -> Any: ...

    def get_subplot_params(self: GridSpec,
                           figure: Any = None) -> Any: ...

    def locally_modified_subplot_params(self: GridSpec) -> list[str]: ...

    def tight_layout(self: GridSpec,
                     figure: {axes},
                     renderer: Any = None,
                     pad: float = 1.08,
                     h_pad: Optional[float] = None,
                     w_pad: Optional[float] = None,
                     rect: int = None) -> None: ...


class GridSpecFromSubplotSpec(GridSpecBase):
    _toplayoutgrid: LayoutGrid
    figure: Any
    _wspace: Any
    _layoutgrid: LayoutGrid
    _hspace: Any
    _subplot_spec: {get_gridspec}

    def __init__(self: GridSpecFromSubplotSpec,
                 nrows: int,
                 ncols: int,
                 subplot_spec: {get_gridspec},
                 wspace: Any = None,
                 hspace: Any = None,
                 height_ratios: Any = None,
                 width_ratios: Any = None) -> None: ...

    def get_subplot_params(self: GridSpecFromSubplotSpec,
                           figure: Optional[{subplotpars}] = None) -> Any: ...

    def get_topmost_subplotspec(self: GridSpecFromSubplotSpec) -> Any: ...


class SubplotSpec(object):
    _num2: Any
    _gridspec: Any
    num1: int
    num2: int

    def __init__(self: SubplotSpec,
                 gridspec: Any,
                 num1: int,
                 num2: int = None) -> None: ...

    def __repr__(self: SubplotSpec) -> str: ...

    def _from_subplot_args(figure: {get_axes},
                           args: {__len__}) -> SubplotSpec: ...

    def num2(self: SubplotSpec) -> Union[int, Any]: ...

    def num2(self: SubplotSpec,
             value: Any) -> None: ...

    def __getstate__(self: SubplotSpec) -> dict[Any, Any]: ...

    def get_gridspec(self: SubplotSpec) -> Any: ...

    def get_geometry(self: SubplotSpec) -> Tuple[Any, Any, int, Union[int, Any]]: ...

    @_api.deprecated("3.3", alternative="rowspan, colspan")
    def get_rows_columns(self: SubplotSpec) -> Union[Tuple[Any, Any, Any, Any, Any, Any], Any]: ...

    def rowspan(self: SubplotSpec) -> range: ...

    def colspan(self: SubplotSpec) -> range: ...

    def is_first_row(self: SubplotSpec) -> bool: ...

    def is_last_row(self: SubplotSpec) -> Union[bool, Any]: ...

    def is_first_col(self: SubplotSpec) -> bool: ...

    def is_last_col(self: SubplotSpec) -> Union[bool, Any]: ...

    @_api.delete_parameter("3.4", "return_all")
    def get_position(self: SubplotSpec,
                     figure: Any,
                     return_all: bool = False) -> Union[Union[Tuple[Bbox, Any, Any, Any, Any], Bbox], Any]: ...

    def get_topmost_subplotspec(self: SubplotSpec) -> Union[SubplotSpec, Any]: ...

    def __eq__(self: SubplotSpec,
               other: Any) -> bool: ...

    def __hash__(self: SubplotSpec) -> int: ...

    def subgridspec(self: SubplotSpec,
                    nrows: int,
                    ncols: int,
                    subplot_spec: Any = ...,
                    wspace: Any = ...,
                    hspace: Any = ...,
                    height_ratios: Any = ...,
                    width_ratios: Any = ...,
                    **kwargs) -> Any: ...
