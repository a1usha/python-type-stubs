from matplotlib.patches import CirclePolygon as CirclePolygon
from matplotlib import font_manager as font_manager
from matplotlib import docstring as docstring
from matplotlib import cbook as cbook
from matplotlib import _api as _api
from numpy import ma as ma
from typing import Any
from typing import ClassVar
from typing import Iterable
from typing import Optional
from typing import Tuple
from typing import Union

from matplotlib import _api
from matplotlib.artist import Artist
from matplotlib.backend_bases import MouseEvent
from matplotlib.collections import PolyCollection
from matplotlib.quiver import Barbs
from matplotlib.quiver import Quiver
from matplotlib.quiver import QuiverKey
from matplotlib.transforms import Affine2D
from matplotlib.transforms import Bbox
from numpy.ma.core import MaskedArray

_quiver_doc: str


class QuiverKey(Artist):
    halign: ClassVar[dict[str, str]]
    valign: ClassVar[dict[str, str]]
    pivot: ClassVar[dict[str, str]]
    color: Any
    label: str
    labelcolor: Any
    kw: dict[str, Any]
    verts: Union[MaskedArray, Any]
    _initialized: bool
    Q: Quiver
    coord: str
    labelsep: Union[float, Any]
    _cid: Any
    fontproperties: Union[dict, None, dict[Any, Any]]
    stale: bool
    zorder: float
    U: float
    X: float
    labelpos: str
    Y: float
    angle: float
    vector: PolyCollection
    text: Text
    _labelsep_inches: float

    def __init__(self: QuiverKey,
                 Q: Quiver,
                 X: float,
                 Y: float,
                 U: float,
                 label: str,
                 *,
                 angle: float = 0,
                 coordinates: str = 'axes',
                 color: Any = None,
                 labelsep: float = 0.1,
                 labelpos: str = 'N',
                 labelcolor: Any = None,
                 fontproperties: Optional[dict] = None,
                 **kwargs) -> None: ...

    def remove(self: QuiverKey) -> None: ...

    def _init(self: QuiverKey) -> None: ...

    def _text_x(self: QuiverKey,
                x: Any) -> Union[float, Any]: ...

    def _text_y(self: QuiverKey,
                y: Any) -> Union[float, Any]: ...

    def draw(self: QuiverKey,
             renderer: {get_rasterized, get_agg_filter, figure}) -> Optional[Any]: ...

    def _set_transform(self: QuiverKey) -> None: ...

    def set_figure(self: QuiverKey,
                   fig: Any) -> None: ...

    def contains(self: QuiverKey,
                 mouseevent: MouseEvent) -> Union[Tuple[Any, Any], Tuple[bool, dict[Any, Any]]]: ...


def _parse_args(*args,
                caller_name: str = 'function') -> Tuple[Any, Any, Any, Any, Optional[Any]]: ...


def _check_consistent_shapes(*args) -> Any: ...


class Quiver(PolyCollection):
    _PIVOT_VALS: ClassVar[tuple[str, str, str]]
    quiver_doc: ClassVar[str]
    XY: Any
    minlength: int
    angles: str
    headaxislength: float
    scale: Any
    _trans_scale: Union[float, Any]
    units: str
    N: int
    transform: Any
    _cid: Any
    stale: bool
    _new_UV: bool
    polykw: dict[str, Any]
    U: Any
    V: Any
    X: Any
    Y: Any
    pivot: str
    scale_units: Any
    minshaft: int
    Umask: Any
    headlength: float
    headwidth: int
    _axes: {transData, figure}
    _initialized: bool
    width: Any
    span: Any

    def __init__(self: Quiver,
                 ax: {transData, figure},
                 scale: Any = None,
                 headwidth: int = 3,
                 headlength: int = 5,
                 headaxislength: float = 4.5,
                 minshaft: int = 1,
                 minlength: int = 1,
                 units: str = 'width',
                 scale_units: Any = None,
                 angles: str = 'uv',
                 width: Any = None,
                 color: str = 'k',
                 pivot: str = 'tail',
                 *args,
                 **kwargs) -> Optional[Any]: ...

    @_api.deprecated("3.3", alternative="axes")
    def ax(self: Quiver) -> Any: ...

    def remove(self: Quiver) -> None: ...

    def _init(self: Quiver) -> None: ...

    def get_datalim(self: Quiver,
                    transData: {depth}) -> Bbox: ...

    def draw(self: Quiver,
             renderer: {open_group, new_gc, close_group}) -> Optional[Any]: ...

    def set_UVC(self: Quiver,
                U: Any,
                V: Any,
                C: Any = None) -> Any: ...

    def _dots_per_unit(self: Quiver,
                       units: Union[str, Any]) -> Union[float, Any]: ...

    def _set_transform(self: Quiver) -> Affine2D: ...

    def _angles_lengths(self: Quiver,
                        U: Union[{__add__}, Any],
                        V: Union[{__mul__}, Any],
                        eps: int = 1) -> Tuple[Any, Union[float, Any]]: ...

    def _make_verts(self: Quiver,
                    U: {__add__},
                    V: {__mul__},
                    angles: Union[str, Any]) -> Union[MaskedArray, Any]: ...

    def _h_arrows(self: Quiver,
                  length: Union[float, Any]) -> Tuple[Any, Any]: ...


_barbs_doc: str


class Barbs(PolyCollection):
    barbs_doc: ClassVar[str]
    fill_empty: bool
    _offsets: Any
    rounding: bool
    stale: bool
    sizes: Union[Union[Iterable, int, float, dict[Any, Any]], Any]
    u: Any
    v: Any
    x: Any
    y: Any
    _pivot: str
    _length: int
    flip: Any
    barb_increments: Union[dict[Any, Any], Any]

    def __init__(self: Barbs,
                 ax: {transData},
                 pivot: str = 'tip',
                 length: int = 7,
                 barbcolor: Any = None,
                 flagcolor: Any = None,
                 sizes: Union[Union[Iterable, int, float], Any] = None,
                 fill_empty: bool = False,
                 barb_increments: Any = None,
                 rounding: bool = True,
                 flip_barb: bool = False,
                 *args,
                 **kwargs) -> Optional[Any]: ...

    def _find_tails(self: Barbs,
                    mag: {__truediv__},
                    rounding: bool = True,
                    half: int = 5,
                    full: int = 10,
                    flag: int = 50) -> Tuple[Any, Any, Union[bool, Any], int]: ...

    def _make_barbs(self: Barbs,
                    u: Any,
                    v: Any,
                    nflags: {__getitem__},
                    nbarbs: {__getitem__},
                    half_barb: {__getitem__},
                    empty_flag: {__getitem__},
                    length: {__mul__, __neg__},
                    pivot: str,
                    sizes: dict,
                    fill_empty: bool,
                    flip: Iterable[bool]) -> list[Union[list[Any], Any]]: ...

    def set_UVC(self: Barbs,
                U: Any,
                V: Any,
                C: Any = None) -> None: ...

    def set_offsets(self: Barbs,
                    xy: Any) -> None: ...
