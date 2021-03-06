from path import Path as Path
from transforms import Bbox as Bbox
from text import Text as Text
from patches import Rectangle as Rectangle
from artist import allow_rasterization as allow_rasterization
from artist import Artist as Artist
from matplotlib import docstring as docstring
from matplotlib import artist as artist
from matplotlib import _api as _api
from typing import Any
from typing import ClassVar
from typing import Iterable
from typing import Optional
from typing import Tuple
from typing import Union

from matplotlib.artist import Artist
from matplotlib.axes._axes import Axes
from matplotlib.backend_bases import MouseEvent
from matplotlib.patches import Rectangle
from matplotlib.path import Path
from matplotlib.table import Cell
from matplotlib.table import Table
from matplotlib.text import Text
from matplotlib.transforms import Bbox


class Cell(Rectangle):
    PAD: ClassVar[float]
    _edges: ClassVar[str]
    _edge_aliases: ClassVar[dict[str, str]]
    stale: bool
    visible_edges: str
    _visible_edges: str
    _text: Text
    _loc: str

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

    def draw(self: Cell,
             renderer: {open_group, new_gc, draw_path, close_group}) -> Optional[Any]: ...

    def _set_text_position(self: Cell,
                           renderer: Union[{open_group, new_gc, draw_path, close_group}, Any]) -> None: ...

    def get_text_bounds(self: Cell,
                        renderer: Any) -> Any: ...

    def get_required_width(self: Cell,
                           renderer: Any) -> Union[float, Any]: ...

    def set_text_props(self: Cell,
                       **kwargs) -> Optional[Any]: ...

    def visible_edges(self: Cell) -> str: ...

    def visible_edges(self: Cell,
                      value: Any) -> Any: ...

    def get_path(self: Cell) -> Path: ...


CustomCell: Type[Cell]


class Table(Artist):
    codes: ClassVar[dict[Union[str, Any], Union[int, Any]]]
    FONTSIZE: ClassVar[int]
    AXESPAD: ClassVar[float]
    _bbox: Any
    _autoColumns: list[Any]
    stale: bool
    _autoFontsize: bool
    _axes: Axes
    _loc: Union[int, Any]
    _cells: dict[Any, Any]
    _edges: None

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

    def edges(self: Table) -> Any: ...

    def edges(self: Table,
              value: Any) -> None: ...

    def _approx_text_height(self: Table) -> Union[float, Any]: ...

    def draw(self: Table,
             renderer: Optional[{open_group, close_group}]) -> Optional[Any]: ...

    def _get_grid_bbox(self: Table,
                       renderer: Union[Optional[{open_group, close_group}], Any]) -> Bbox: ...

    def contains(self: Table,
                 mouseevent: MouseEvent) -> Union[Tuple[Any, Any], Tuple[bool, dict[Any, Any]]]: ...

    def get_children(self: Table) -> list[Any]: ...

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
                            renderer: Union[Optional[{open_group, close_group}], Any]) -> None: ...

    def scale(self: Table,
              xscale: Any,
              yscale: Any) -> None: ...

    def set_fontsize(self: Table,
                     size: Union[float, int]) -> None: ...

    def _offset(self: Table,
                ox: Union[Union[float, int], Any],
                oy: Any) -> None: ...

    def _update_positions(self: Table,
                          renderer: Union[Optional[{open_group, close_group}], Any]) -> None: ...

    def get_celld(self: Table) -> dict[Any, Any]: ...


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
          **kwargs) -> Any: ...