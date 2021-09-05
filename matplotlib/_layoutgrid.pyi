from matplotlib.transforms import Bbox as Bbox
from typing import Any
from typing import Union

from matplotlib._layoutgrid import LayoutGrid
from matplotlib.transforms import Bbox
from object import object


class LayoutGrid(object):
    parent: Any
    parent_inner: bool
    margins: dict[str, Union[list[Any], Any]]
    nrows: int
    height_ratios: Any
    tops: list[Any]
    widths: list[Any]
    lefts: list[Any]
    bottoms: list[Any]
    parent_pos: Union[tuple[int, int], Any]
    inner_heights: list[Any]
    width_ratios: Any
    w_pad: Any
    artists: Any
    children: Any
    heights: list[Any]
    rights: list[Any]
    name: str
    margin_vals: dict[str, Any]
    h_pad: Any
    inner_widths: list[Any]
    ncols: int
    solver: Any

    def __init__(self: LayoutGrid,
                 parent: Any = None,
                 parent_pos: Union[tuple[int, int], Any] = (0, 0),
                 parent_inner: bool = False,
                 name: str = '',
                 ncols: int = 1,
                 nrows: int = 1,
                 h_pad: Any = None,
                 w_pad: Any = None,
                 width_ratios: Any = None,
                 height_ratios: Any = None) -> None: ...

    def __repr__(self: LayoutGrid) -> str: ...

    def reset_margins(self: LayoutGrid) -> None: ...

    def add_constraints(self: LayoutGrid) -> None: ...

    def hard_constraints(self: LayoutGrid) -> None: ...

    def add_child(self: LayoutGrid,
                  child: Any,
                  i: int = 0,
                  j: int = 0) -> None: ...

    def parent_constraints(self: LayoutGrid) -> None: ...

    def grid_constraints(self: LayoutGrid) -> None: ...

    def edit_margin(self: LayoutGrid,
                    todo: str,
                    size: Union[float, int],
                    cell: int) -> None: ...

    def edit_margin_min(self: LayoutGrid,
                        todo: str,
                        size: Union[float, int],
                        cell: int = 0) -> None: ...

    def edit_margins(self: LayoutGrid,
                     todo: str,
                     size: Union[float, int]) -> None: ...

    def edit_all_margins_min(self: LayoutGrid,
                             todo: str,
                             size: Union[float, int]) -> None: ...

    def edit_outer_margin_mins(self: LayoutGrid,
                               margin: dict,
                               ss: Any) -> None: ...

    def get_margins(self: LayoutGrid,
                    todo: Any,
                    col: Any) -> Any: ...

    def get_outer_bbox(self: LayoutGrid,
                       rows: int = 0,
                       cols: int = 0) -> Bbox: ...

    def get_inner_bbox(self: LayoutGrid,
                       rows: int = 0,
                       cols: int = 0) -> Bbox: ...

    def get_bbox_for_cb(self: LayoutGrid,
                        rows: int = 0,
                        cols: int = 0) -> Bbox: ...

    def get_left_margin_bbox(self: LayoutGrid,
                             rows: int = 0,
                             cols: int = 0) -> Bbox: ...

    def get_bottom_margin_bbox(self: LayoutGrid,
                               rows: int = 0,
                               cols: int = 0) -> Bbox: ...

    def get_right_margin_bbox(self: LayoutGrid,
                              rows: int = 0,
                              cols: int = 0) -> Bbox: ...

    def get_top_margin_bbox(self: LayoutGrid,
                            rows: int = 0,
                            cols: int = 0) -> Bbox: ...

    def update_variables(self: LayoutGrid) -> None: ...


_layoutboxobjnum: count[int]


def seq_id() -> str: ...


def print_children(lb: {children}) -> None: ...


def plot_children(fig: {canvas, add_artist, transFigure},
                  lg: {nrows, ncols, get_outer_bbox, get_inner_bbox, get_left_margin_bbox, get_right_margin_bbox,
                       get_bottom_margin_bbox, get_top_margin_bbox, children},
                  level: int = 0,
                  printit: bool = False) -> None: ...