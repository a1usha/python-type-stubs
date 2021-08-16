from typing import Any
from typing import Iterable
from typing import Optional
from typing import Union


class Cell(Rectangle):
    def __init__(self: Cell,
                 xy: Any,
                 width: float,
                 height: float,
                 edgecolor: Any = 'k',
                 facecolor: Any = 'w',
                 fill: bool = True,
                 text: str = '',
                 loc: str = None,
                 fontproperties: dict = None,
                 *,
                 visible_edges: str = 'closed') -> None: ...

    def set_transform(self: Cell,
                      trans: Any) -> None: ...

    def set_figure(self: Cell,
                   fig: Any) -> None: ...

    def get_text(self: Cell) -> Text: ...

    def set_fontsize(self: Cell,
                     size: Any) -> None: ...

    def get_fontsize(self: Cell) -> Any: ...

    def auto_set_font_size(self: Cell,
                           renderer: Any) -> Any: ...

    @allow_rasterization
    def draw(self: Cell,
             renderer: {open_group, new_gc, draw_path, close_group}) -> Optional[Any]: ...

    def _set_text_position(self: Cell,
                           renderer: {open_group, new_gc, draw_path, close_group}) -> None: ...

    def get_text_bounds(self: Cell,
                        renderer: Any) -> Any: ...

    def get_required_width(self: Cell,
                           renderer: Any) -> float: ...

    @docstring.dedent_interpd
    def set_text_props(self: Cell,
                       **kwargs) -> Optional[Any]: ...

    @property
    def visible_edges(self: Cell) -> str: ...

    @visible_edges.setter
    def visible_edges(self: Cell,
                      value: Any) -> Any: ...

    def get_path(self: Cell) -> Path: ...


class Table(Artist):
    def __init__(self: Table,
                 ax: Axes,
                 loc: str = None,
                 bbox: Any = None,
                 **kwargs) -> Any: ...

    def add_cell(self: Table,
                 row: int,
                 col: int,
                 *args,
                 **kwargs) -> Any: ...

    def __setitem__(self: Table,
                    position: {__getitem__},
                    cell: {set_figure, set_transform, set_clip_on}) -> Any: ...

    def __getitem__(self: Table,
                    position: Any) -> Any: ...

    @property
    def edges(self: Table) -> Any: ...

    @edges.setter
    def edges(self: Table,
              value: Any) -> None: ...

    def _approx_text_height(self: Table) -> float: ...

    @allow_rasterization
    def draw(self: Table,
             renderer: Optional[{open_group, close_group}]) -> Optional[Any]: ...

    def _get_grid_bbox(self: Table,
                       renderer: Optional[{open_group, close_group}]) -> Bbox: ...

    def contains(self: Table,
                 mouseevent: MouseEvent) -> Union[tuple[Any, Any], tuple[bool, dict]]: ...

    def get_children(self: Table) -> list: ...

    def get_window_extent(self: Table,
                          renderer: Any) -> Bbox: ...

    def _do_cell_alignment(self: Table) -> None: ...

    def auto_set_column_width(self: Table,
                              col: Union[int, Iterable[int]]) -> None: ...

    def _auto_set_column_width(self: Table,
                               col: Any,
                               renderer: Any) -> None: ...

    def auto_set_font_size(self: Table,
                           value: bool = True) -> None: ...

    def _auto_set_font_size(self: Table,
                            renderer: Optional[{open_group, close_group}]) -> None: ...

    def scale(self: Table,
              xscale: Any,
              yscale: Any) -> None: ...

    def set_fontsize(self: Table,
                     size: Union[float, int]) -> None: ...

    def _offset(self: Table,
                ox: Union[float, int],
                oy: Any) -> None: ...

    def _update_positions(self: Table,
                          renderer: Optional[{open_group, close_group}]) -> None: ...

    def get_celld(self: Table) -> dict: ...


@docstring.dedent_interpd
def table(ax: {add_table},
          cellText: Optional[int] = None,
          cellColours: Optional[int] = None,
          cellLoc: str = 'right',
          colWidths: Optional[Iterable[float]] = None,
          rowLabels: Optional[Iterable[str]] = None,
          rowColours: Optional[Iterable] = None,
          rowLoc: str = 'left',
          colLabels: Optional[Iterable[str]] = None,
          colColours: Optional[Iterable] = None,
          colLoc: str = 'center',
          loc: Optional[str] = 'bottom',
          bbox: Any = None,
          edges: str = 'closed',
          ax: Any = ...,
          loc: Any = ...,
          bbox: Any = ...,
          **kwargs) -> Any: ...