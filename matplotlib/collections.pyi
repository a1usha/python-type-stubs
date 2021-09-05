from _enums import CapStyle as CapStyle
from _enums import JoinStyle as JoinStyle
from matplotlib import transforms as transforms
from matplotlib import path as mpath
from matplotlib import lines as mlines
from matplotlib import hatch as mhatch
from matplotlib import docstring as docstring
from matplotlib import colors as mcolors
from matplotlib import cm as cm
from matplotlib import cbook as cbook
from matplotlib import artist as artist
from matplotlib import _path as _path
from matplotlib import _api as _api
from numbers import Number as Number
from typing import Any
from typing import Callable
from typing import ClassVar
from typing import Collection
from typing import Iterable
from typing import Optional
from typing import Tuple
from typing import Type
from typing import Union

from matplotlib import _api
from matplotlib.artist import Artist
from matplotlib.backend_bases import MouseEvent
from matplotlib.cm import ScalarMappable
from matplotlib.collections import BrokenBarHCollection
from matplotlib.collections import CircleCollection
from matplotlib.collections import Collection
from matplotlib.collections import EllipseCollection
from matplotlib.collections import EventCollection
from matplotlib.collections import LineCollection
from matplotlib.collections import PatchCollection
from matplotlib.collections import PathCollection
from matplotlib.collections import PolyCollection
from matplotlib.collections import QuadMesh
from matplotlib.collections import RegularPolyCollection
from matplotlib.collections import TriMesh
from matplotlib.collections import _CollectionWithSizes
from matplotlib.transforms import Bbox
from matplotlib.transforms import IdentityTransform
from matplotlib.transforms import Transform


class Collection(Artist, ScalarMappable):
    _offsets: ClassVar[Any]
    _transOffset: ClassVar[IdentityTransform]
    _transforms: ClassVar[Any]
    _edge_default: ClassVar[bool]
    _edge_is_mapped: None
    _hatch: str
    _A: Any
    _offsets: Any
    _mapped_colors: None
    _offset_position: str
    _linewidths: list[int]
    _edgecolors: str
    _us_linestyles: list[tuple[int, None]]
    _us_lw: list[int]
    norm: Any
    stale: bool
    _original_edgecolor: Union[str, Any]
    _path_effects: None
    _paths: None
    _facecolors: Union[Union[Iterable, int, float], Any]
    _update_dict: Any
    _offsetsNone: Any
    _antialiaseds: Any
    _capstyle: None
    _transOffset: Any
    _hatch_color: Union[Iterable, tuple]
    _linestyles: list[tuple[int, None]]
    _joinstyle: None
    _urls: Union[Iterable[str], list[None]]
    _face_is_mapped: None
    _uniform_offsets: Any
    cmap: Any
    _alpha: Any
    _original_facecolor: Union[str, Iterable]
    _pickradius: float

    @_api.delete_parameter("3.3", "offset_position")
    def __init__(self: Collection,
                 edgecolors: Union[Iterable, Any] = None,
                 facecolors: Union[Iterable, Any] = None,
                 linewidths: Union[float, Iterable] = None,
                 linestyles: Any = 'solid',
                 capstyle: Any = None,
                 joinstyle: Any = None,
                 antialiaseds: Union[bool, Iterable[bool]] = None,
                 offsets: int = None,
                 transOffset: Any = None,
                 norm: Any = None,
                 cmap: Any = None,
                 pickradius: float = 5.0,
                 hatch: Optional[str] = None,
                 urls: Iterable[str] = None,
                 offset_position: Any = 'screen',
                 zorder: float = 1,
                 **kwargs) -> Optional[Any]: ...

    def get_paths(self: Collection) -> Any: ...

    def set_paths(self: Collection) -> Any: ...

    def get_transforms(self: Collection) -> Any: ...

    def get_offset_transform(self: Collection) -> Union[Transform, Any]: ...

    def get_datalim(self: Collection,
                    transData: Union[IdentityTransform, Any]) -> Bbox: ...

    def get_window_extent(self: Collection,
                          renderer: Any) -> Bbox: ...

    def _prepare_points(self: Collection) -> Tuple[
        Union[IdentityTransform, Any], Union[Union[IdentityTransform, Transform], Any], Union[
            Union[Iterable, int, float], Any], Union[Union[list[{vertices, codes}], list[Path]], Any]]: ...

    def draw(self: Collection,
             renderer: {open_group, new_gc, close_group}) -> Optional[Any]: ...

    def set_pickradius(self: Collection,
                       pr: float) -> None: ...

    def get_pickradius(self: Collection) -> float: ...

    def contains(self: Collection,
                 mouseevent: MouseEvent) -> Union[
        Tuple[Any, Any], Tuple[bool, dict[Any, Any]], Tuple[bool, dict[Any, Any]]]: ...

    def set_urls(self: Collection,
                 urls: Optional[Iterable[str]]) -> None: ...

    def get_urls(self: Collection) -> Union[Iterable[str], list[None]]: ...

    def set_hatch(self: Collection,
                  hatch: str) -> None: ...

    def get_hatch(self: Collection) -> str: ...

    def set_offsets(self: Collection,
                    offsets: int) -> None: ...

    def get_offsets(self: Collection) -> Any: ...

    @_api.deprecated("3.3")
    def set_offset_position(self: Collection,
                            offset_position: str) -> Optional[Any]: ...

    @_api.deprecated("3.3")
    def get_offset_position(self: Collection) -> Union[str, Any]: ...

    def _get_default_linewidth(self: Collection) -> Optional[Any]: ...

    def set_linewidth(self: Collection,
                      lw: Union[float, Iterable]) -> None: ...

    def set_linestyle(self: Collection,
                      ls: Any) -> Any: ...

    def set_capstyle(self: Collection,
                     cs: Any) -> Optional[Any]: ...

    def get_capstyle(self: Collection) -> Any: ...

    def set_joinstyle(self: Collection,
                      js: Any) -> Optional[Any]: ...

    def get_joinstyle(self: Collection) -> Any: ...

    def _bcast_lwls(linewidths: Iterable,
                    dashes: Iterable) -> list: ...

    def set_antialiased(self: Collection,
                        aa: Union[bool, Iterable]) -> None: ...

    def _get_default_antialiased(self: Collection) -> Optional[Any]: ...

    def set_color(self: Collection,
                  c: Any) -> None: ...

    def _get_default_facecolor(self: Collection) -> Optional[Any]: ...

    def _set_facecolor(self: Collection,
                       c: Union[Union[str, Iterable], Any]) -> None: ...

    def set_facecolor(self: Collection,
                      c: Union[Iterable, Any]) -> None: ...

    def get_facecolor(self: Collection) -> Union[Union[Iterable, int, float], Any]: ...

    def get_edgecolor(self: Collection) -> Union[Union[Iterable, int, float, str], Any]: ...

    def _get_default_edgecolor(self: Collection) -> Optional[Any]: ...

    def _set_edgecolor(self: Collection,
                       c: Union[str, Any]) -> None: ...

    def set_edgecolor(self: Collection,
                      c: Any) -> None: ...

    def set_alpha(self: Collection,
                  alpha: Union[Union[float, Iterable, int, float[float], None], Any]) -> None: ...

    def get_linewidth(self: Collection) -> list[int]: ...

    def get_linestyle(self: Collection) -> list[Tuple[int, None]]: ...

    def _set_mappable_flags(self: Collection) -> bool: ...

    def update_scalarmappable(self: Collection) -> None: ...

    def get_fill(self: Collection) -> bool: ...

    def update_from(self: Collection,
                    other: {_transform, _transformSet, _visible, _alpha, clipbox, _clipon, _clippath, _label, _sketch,
                            _path_effects, sticky_edges}) -> None: ...


class _CollectionWithSizes(Collection):
    _factor: ClassVar[float]
    _sizes: Any
    stale: bool
    _transforms: Any

    def get_sizes(self: _CollectionWithSizes) -> array.pyi: ...

    def set_sizes(self: _CollectionWithSizes,
                  sizes: Optional[Any],
                  dpi: float = 72.0) -> None: ...

    def draw(self: _CollectionWithSizes,
             renderer: {open_group, new_gc, close_group}) -> Optional[Any]: ...


class PathCollection(_CollectionWithSizes):
    stale: bool
    _paths: Any

    def __init__(self: PathCollection,
                 paths: Any,
                 sizes: Union[Union[Iterable, int, float], Any] = None,
                 **kwargs) -> None: ...

    def set_paths(self: PathCollection,
                  paths: Any) -> None: ...

    def get_paths(self: PathCollection) -> Any: ...

    def legend_elements(self: PathCollection,
                        prop: str = "colors",
                        num: Union[Union[int, None, Iterable, float], Any] = "auto",
                        fmt: str = None,
                        func: function = lambda x: x,
                        **kwargs) -> Any: ...


class PolyCollection(_CollectionWithSizes):
    set_paths: ClassVar[Callable[[PolyCollection, Union[Iterable, int, float], bool], None]]
    stale: bool
    _paths: list[Path]

    def __init__(self: PolyCollection,
                 verts: Union[Iterable, int, float],
                 sizes: Union[Union[Iterable, int, float], Any] = None,
                 closed: bool = True,
                 **kwargs) -> None: ...

    def set_verts(self: PolyCollection,
                  verts: Union[Iterable, int, float],
                  closed: bool = True) -> None: ...

    def set_verts_and_codes(self: PolyCollection,
                            verts: {__len__},
                            codes: {__len__}) -> Any: ...


class BrokenBarHCollection(PolyCollection):
    def __init__(self: BrokenBarHCollection,
                 xranges: list[tuple[float, float]],
                 yrange: tuple[float, float],
                 **kwargs) -> None: ...

    def span_where(cls: Type[BrokenBarHCollection],
                   x: Any,
                   ymin: Any,
                   ymax: {__sub__},
                   where: Any,
                   **kwargs) -> BrokenBarHCollection: ...


class RegularPolyCollection(_CollectionWithSizes):
    _path_generator: ClassVar[Callable[[{__le__}], Union[Path, Any]]]
    _factor: ClassVar[Union[float, Any]]
    _numsides: int
    _rotation: float
    _paths: list[Union[Path, Any]]
    _transforms: list[Any]

    def __init__(self: RegularPolyCollection,
                 numsides: int,
                 rotation: float = 0,
                 sizes: Union[Iterable, tuple[float]] = (1,),
                 **kwargs) -> None: ...

    def get_numsides(self: RegularPolyCollection) -> int: ...

    def get_rotation(self: RegularPolyCollection) -> float: ...

    def draw(self: RegularPolyCollection,
             renderer: {open_group, new_gc, close_group}) -> Optional[Any]: ...


class StarPolygonCollection(RegularPolyCollection):
    _path_generator: ClassVar[Callable[[{__le__}, float], Union[Path, Any]]]
    pass


class AsteriskPolygonCollection(RegularPolyCollection):
    _path_generator: ClassVar[Callable[[{__le__}], Union[Path, Any]]]
    pass


class LineCollection(Collection):
    _edge_default: ClassVar[bool]
    set_verts: ClassVar[Callable[[LineCollection, Union[Union[Iterable, int, float], Any]], None]]
    set_paths: ClassVar[Callable[[LineCollection, Union[Union[Iterable, int, float], Any]], None]]
    set_colors: ClassVar[Callable[[LineCollection, Union[Iterable, Any]], None]]
    get_colors: ClassVar[Callable[[LineCollection], str]]
    stale: bool
    _paths: list[Path]

    def __init__(self: LineCollection,
                 segments: Union[Iterable, int, float],
                 zorder: int = 2,
                 *args,
                 **kwargs) -> None: ...

    def set_segments(self: LineCollection,
                     segments: Union[Union[Iterable, int, float], Any]) -> None: ...

    def get_segments(self: LineCollection) -> list: ...

    def _add_offsets(self: LineCollection,
                     segs: Union[list[Union[MaskedArray, Any]], Any]) -> Union[list[Union[MaskedArray, Any]], Any]: ...

    def _get_default_linewidth(self: LineCollection) -> Optional[Any]: ...

    def _get_default_antialiased(self: LineCollection) -> Optional[Any]: ...

    def _get_default_edgecolor(self: LineCollection) -> Optional[Any]: ...

    def _get_default_facecolor(self: LineCollection) -> str: ...

    def set_color(self: LineCollection,
                  c: Union[Iterable, Any]) -> None: ...

    def get_color(self: LineCollection) -> str: ...


class EventCollection(LineCollection):
    _edge_default: ClassVar[bool]
    extend_positions: ClassVar[Callable[[EventCollection, Optional[{__len__}]], None]]
    append_positions: ClassVar[Callable[[EventCollection, Optional[{__len__}]], None]]
    stale: bool
    _is_horizontal: bool
    _linelength: float
    _lineoffset: float

    def __init__(self: EventCollection,
                 positions: int,
                 orientation: str = 'horizontal',
                 lineoffset: float = 0,
                 linelength: float = 1,
                 linewidth: Any = None,
                 color: Union[Iterable, Any] = None,
                 linestyle: Any = 'solid',
                 antialiased: Any = None,
                 **kwargs) -> None: ...

    def get_positions(self: EventCollection) -> list[Any]: ...

    def set_positions(self: EventCollection,
                      positions: Union[int, Any]) -> Any: ...

    def add_positions(self: EventCollection,
                      position: Optional[{__len__}]) -> None: ...

    def is_horizontal(self: EventCollection) -> bool: ...

    def get_orientation(self: EventCollection) -> str: ...

    def switch_orientation(self: EventCollection) -> None: ...

    def set_orientation(self: EventCollection,
                        orientation: str = None) -> None: ...

    def get_linelength(self: EventCollection) -> float: ...

    def set_linelength(self: EventCollection,
                       linelength: {__eq__, __truediv__}) -> None: ...

    def get_lineoffset(self: EventCollection) -> float: ...

    def set_lineoffset(self: EventCollection,
                       lineoffset: {__eq__, __add__, __sub__}) -> None: ...

    def get_linewidth(self: EventCollection) -> int: ...

    def get_linewidths(self: EventCollection) -> list[int]: ...

    def get_color(self: EventCollection) -> str: ...


class CircleCollection(_CollectionWithSizes):
    _factor: ClassVar[Union[float, Any]]
    _paths: list[Union[Path, Any]]

    def __init__(self: CircleCollection,
                 sizes: Union[Union[float, Iterable, int], Any],
                 **kwargs) -> None: ...


class EllipseCollection(Collection):
    _units: str
    _heights: Union[float, Any]
    _widths: Union[float, Any]
    _angles: Any
    _transforms: Any
    _paths: list[Union[Path, Any]]

    def __init__(self: EllipseCollection,
                 widths: Union[Union[Iterable, int, float], Any],
                 heights: Union[Union[Iterable, int, float], Any],
                 angles: Union[Union[Iterable, int, float], Any],
                 units: str = 'points',
                 **kwargs) -> None: ...

    def _set_transforms(self: EllipseCollection) -> Any: ...

    def draw(self: EllipseCollection,
             renderer: {open_group, new_gc, close_group}) -> Optional[Any]: ...


class PatchCollection(Collection):
    _paths: list[Any]

    def __init__(self: PatchCollection,
                 patches: Any,
                 match_original: bool = False,
                 **kwargs) -> None: ...

    def set_paths(self: PatchCollection,
                  patches: Any) -> None: ...


class TriMesh(Collection):
    _bbox: Bbox
    _shading: str
    _paths: list[Path]
    _triangulation: {x, y}

    def __init__(self: TriMesh,
                 triangulation: {x, y},
                 **kwargs) -> None: ...

    def get_paths(self: TriMesh) -> Optional[list[Path]]: ...

    def set_paths(self: TriMesh) -> None: ...

    def convert_mesh_to_paths(tri: Union[{x, y}, Any]) -> list[Path]: ...

    def draw(self: TriMesh,
             renderer: {open_group, new_gc, close_group}) -> Optional[Any]: ...


class QuadMesh(Collection):
    _meshWidth: {__add__}
    _bbox: Bbox
    _shading: str
    _meshHeight: {__add__}
    _coordinates: Any
    _antialiased: bool
    stale: bool
    _paths: list[Path]

    def __init__(self: QuadMesh,
                 meshWidth: {__add__},
                 meshHeight: {__add__},
                 coordinates: {reshape},
                 antialiased: bool = True,
                 shading: str = 'flat',
                 **kwargs) -> None: ...

    def get_paths(self: QuadMesh) -> Optional[list[Path]]: ...

    def set_paths(self: QuadMesh) -> None: ...

    def get_datalim(self: QuadMesh,
                    transData: Union[IdentityTransform, Any]) -> Bbox: ...

    def convert_mesh_to_paths(meshWidth: Union[{__add__}, Any],
                              meshHeight: Any,
                              coordinates: Any) -> list[Path]: ...

    def convert_mesh_to_triangles(self: QuadMesh,
                                  meshWidth: Union[{__add__}, Any],
                                  meshHeight: {__add__},
                                  coordinates: Any) -> Tuple[Any, Any]: ...

    def draw(self: QuadMesh,
             renderer: {open_group, new_gc, close_group}) -> Optional[Any]: ...


_artist_kwdoc: str
