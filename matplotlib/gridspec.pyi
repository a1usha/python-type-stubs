from typing import Optional


class GridSpecFromSubplotSpec(GridSpecBase):
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


class GridSpecBase(object):
    def __init__(self: GridSpecBase,
                 nrows: int,
                 ncols: int,
                 height_ratios: Any = None,
                 width_ratios: Any = None) -> Any: ...

    def __repr__(self: GridSpecBase) -> str: ...

    def get_geometry(self: GridSpecBase) -> tuple[int, int]: ...

    def get_subplot_params(self: GridSpecBase,
                           figure: Any = None) -> None: ...

    def new_subplotspec(self: GridSpecBase,
                        loc: tuple[int, int],
                        rowspan: int = 1,
                        colspan: int = 1) -> SubplotSpec: ...

    def set_width_ratios(self: GridSpecBase,
                         width_ratios: Optional[{__len__}]) -> Any: ...

    def get_width_ratios(self: GridSpecBase) -> list[int]: ...

    def set_height_ratios(self: GridSpecBase,
                          height_ratios: Optional[{__len__}]) -> Any: ...

    def get_height_ratios(self: GridSpecBase) -> list[int]: ...

    def get_grid_positions(self: GridSpecBase,
                           fig: Any,
                           raw: bool = False) -> array.pyi: ...

    @staticmethod
    def _check_gridspec_exists(figure: {get_axes},
                               nrows: Any,
                               ncols: Any) -> GridSpec: ...

    def __getitem__(self: GridSpecBase,
                    key: Any) -> SubplotSpec: ...

    def subplots(self: GridSpecBase,
                 sharex: bool = False,
                 sharey: bool = False,
                 squeeze: bool = True,
                 subplot_kw: Any = None) -> Union[int, float, complex, None, ndarray]: ...


class SubplotSpec(object):
    def __init__(self: SubplotSpec,
                 gridspec: Any,
                 num1: int,
                 num2: int = None) -> None: ...

    def __repr__(self: SubplotSpec) -> str: ...

    @staticmethod
    def _from_subplot_args(figure: {get_axes},
                           args: {__len__}) -> SubplotSpec: ...

    @property
    def num2(self: SubplotSpec) -> int: ...

    @num2.setter
    def num2(self: SubplotSpec,
             value: Any) -> None: ...

    def __getstate__(self: SubplotSpec) -> dict: ...

    def get_gridspec(self: SubplotSpec) -> Any: ...

    def get_geometry(self: SubplotSpec) -> tuple[Any, Any, int, int]: ...

    @_api.deprecated
    def get_rows_columns(self: SubplotSpec) -> tuple[Any, Any, Any, Any, Any, Any]: ...

    @property
    def rowspan(self: SubplotSpec) -> range: ...

    @property
    def colspan(self: SubplotSpec) -> range: ...

    def is_first_row(self: SubplotSpec) -> bool: ...

    def is_last_row(self: SubplotSpec) -> bool: ...

    def is_first_col(self: SubplotSpec) -> bool: ...

    def is_last_col(self: SubplotSpec) -> bool: ...

    @_api.delete_parameter
    def get_position(self: SubplotSpec,
                     figure: Any,
                     return_all: bool = False) -> Union[tuple[Bbox, Any, Any, Any, Any], Bbox]: ...

    def get_topmost_subplotspec(self: SubplotSpec) -> SubplotSpec: ...

    def __eq__(self: SubplotSpec,
               other: Any) -> bool: ...

    def __hash__(self: SubplotSpec) -> int: ...

    def subgridspec(self: SubplotSpec,
                    nrows: int,
                    ncols: int,
                    nrows: Any = ...,
                    ncols: Any = ...,
                    subplot_spec: Any = ...,
                    wspace: Any = ...,
                    hspace: Any = ...,
                    height_ratios: Any = ...,
                    width_ratios: Any = ...,
                    **kwargs) -> Any: ...


class GridSpec(GridSpecBase):
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
