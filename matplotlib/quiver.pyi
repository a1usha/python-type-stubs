from typing import Any
from typing import Iterable
from typing import Optional
from typing import Union

from numpy.core._multiarray_umath import ndarray


class Quiver(PolyCollection):
    @docstring.Substitution(_quiver_doc)
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

    @martist.allow_rasterization
    def draw(self: Quiver,
             renderer: {open_group, new_gc, close_group}) -> Optional[Any]: ...

    def set_UVC(self: Quiver,
                U: Any,
                V: Any,
                C: Any = None) -> Any: ...

    def _dots_per_unit(self: Quiver,
                       units: str) -> float: ...

    def _set_transform(self: Quiver) -> Affine2D: ...

    def _angles_lengths(self: Quiver,
                        U: {__add__},
                        V: ndarray,
                        eps: int = 1) -> tuple[None, float]: ...

    def _make_verts(self: Quiver,
                    U: ndarray,
                    V: {__mul__},
                    angles: str) -> Optional[ndarray]: ...

    def _h_arrows(self: Quiver,
                  length: float) -> tuple[Any, None]: ...


class Barbs(PolyCollection):
    @docstring.interpd
    def __init__(self: Barbs,
                 ax: {transData},
                 pivot: str = 'tip',
                 length: int = 7,
                 barbcolor: Any = None,
                 flagcolor: Any = None,
                 sizes: Union[ndarray, Iterable, int, float] = None,
                 fill_empty: bool = False,
                 barb_increments: Any = None,
                 rounding: bool = True,
                 flip_barb: bool = False,
                 *args,
                 **kwargs) -> Optional[Any]: ...

    def _find_tails(self: Barbs,
                    mag: Optional[Any],
                    rounding: bool = True,
                    half: int = 5,
                    full: int = 10,
                    flag: int = 50) -> tuple[Any, Any, bool, int]: ...

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
                    flip: Iterable[bool]) -> list[Union[list, ndarray]]: ...

    def set_UVC(self: Barbs,
                U: Any,
                V: Any,
                C: Any = None) -> None: ...

    def set_offsets(self: Barbs,
                    xy: Any) -> None: ...


class QuiverKey(Artist):
    def __init__(self: QuiverKey,
                 Q: Quiver,
                 X: float,
                 Y: float,
                 U: float,
                 label: str,
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
                x: Any) -> float: ...

    def _text_y(self: QuiverKey,
                y: Any) -> float: ...

    @martist.allow_rasterization
    def draw(self: QuiverKey,
             renderer: {get_rasterized, get_agg_filter, figure}) -> Optional[Any]: ...

    def _set_transform(self: QuiverKey) -> None: ...

    def set_figure(self: QuiverKey,
                   fig: Any) -> None: ...

    def contains(self: QuiverKey,
                 mouseevent: MouseEvent) -> Union[tuple[Any, Any], tuple[bool, dict]]: ...


def _parse_args(*args,
                caller_name: str = 'function') -> tuple[Any, Any, Any, Any, Optional[Any]]: ...


def _check_consistent_shapes(*args) -> Any: ...