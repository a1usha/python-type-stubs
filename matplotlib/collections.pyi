from typing import Any
from typing import Iterable
from typing import Optional
from typing import Union
from typing import tuple

from matplotlib.transforms import IdentityTransform
from numpy.core._multiarray_umath import ndarray


class Collection(Artist, ScalarMappable):
    @_api.delete_parameter("3.3", "offset_position")
    @docstring.interpd
    def __init__(self: Collection,
                 edgecolors: Iterable = None,
                 facecolors: Iterable = None,
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

    def get_transforms(self: Collection) -> ndarray: ...

    def get_offset_transform(self: Collection) -> Transform: ...

    def get_datalim(self: Collection,
                    transData: IdentityTransform) -> Bbox: ...

    def get_window_extent(self: Collection,
                          renderer: Any) -> Bbox: ...

    def _prepare_points(self: Collection) -> tuple[
        IdentityTransform, Union[IdentityTransform, Transform], Union[ndarray, Iterable, int, float], Union[
            list[{vertices, codes}], list[Path]]]: ...

    @artist.allow_rasterization
    def draw(self: Collection,
             renderer: {open_group, new_gc, close_group}) -> Optional[Any]: ...

    def set_pickradius(self: Collection,
                       pr: float) -> None: ...

    def get_pickradius(self: Collection) -> float: ...

    def contains(self: Collection,
                 mouseevent: MouseEvent) -> Union[tuple[Any, Any], tuple[bool, dict], tuple[bool, dict[Any, None]]]: ...

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
    def get_offset_position(self: Collection) -> str: ...

    def _get_default_linewidth(self: Collection) -> Optional[Any]: ...

    def set_linewidth(self: Collection,
                      lw: Union[float, Iterable]) -> None: ...

    def set_linestyle(self: Collection,
                      ls: Any) -> Any: ...

    @docstring.interpd
    def set_capstyle(self: Collection,
                     cs: Any) -> Optional[Any]: ...

    def get_capstyle(self: Collection) -> Any: ...

    @docstring.interpd
    def set_joinstyle(self: Collection,
                      js: Any) -> Optional[Any]: ...

    def get_joinstyle(self: Collection) -> Any: ...

    @staticmethod
    def _bcast_lwls(linewidths: Iterable,
                    dashes: Iterable) -> list: ...

    def set_antialiased(self: Collection,
                        aa: Union[bool, Iterable]) -> None: ...

    def _get_default_antialiased(self: Collection) -> Optional[Any]: ...

    def set_color(self: Collection,
                  c: Any) -> None: ...

    def _get_default_facecolor(self: Collection) -> Optional[Any]: ...

    def _set_facecolor(self: Collection,
                       c: Union[str, Iterable]) -> None: ...

    def set_facecolor(self: Collection,
                      c: Iterable) -> None: ...

    def get_facecolor(self: Collection) -> Union[ndarray, Iterable, int, float]: ...

    def get_edgecolor(self: Collection) -> Union[ndarray, Iterable, int, float, str]: ...

    def _get_default_edgecolor(self: Collection) -> Optional[Any]: ...

    def _set_edgecolor(self: Collection,
                       c: str) -> None: ...

    def set_edgecolor(self: Collection,
                      c: Any) -> None: ...

    def set_alpha(self: Collection,
                  alpha: Union[float, ndarray, Iterable, int, float[float], None]) -> None: ...

    def get_linewidth(self: Collection) -> list[int]: ...

    def get_linestyle(self: Collection) -> list[tuple[int, None]]: ...

    def _set_mappable_flags(self: Collection) -> bool: ...

    def update_scalarmappable(self: Collection) -> None: ...

    def get_fill(self: Collection) -> bool: ...

    def update_from(self: Collection,
                    other: {_transform, _transformSet, _visible, _alpha, clipbox, _clipon, _clippath, _label, _sketch,
                            _path_effects, sticky_edges}) -> None: ...


class AsteriskPolygonCollection(RegularPolyCollection):
    pass


class PolyCollection(_CollectionWithSizes):
    def __init__(self: PolyCollection,
                 verts: Union[Iterable[ndarray], Iterable, int, float],
                 sizes: Union[ndarray, Iterable, int, float] = None,
                 closed: bool = True,
                 **kwargs) -> None: ...

    def set_verts(self: PolyCollection,
                  verts: Union[Iterable[ndarray], Iterable, int, float],
                  closed: bool = True) -> None: ...

    def set_verts_and_codes(self: PolyCollection,
                            verts: {__len__},
                            codes: {__len__}) -> Any: ...


class QuadMesh(Collection):
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
                    transData: IdentityTransform) -> Bbox: ...

    @staticmethod
    def convert_mesh_to_paths(meshWidth: {__add__},
                              meshHeight: Any,
                              coordinates: Any) -> list[Path]: ...

    def convert_mesh_to_triangles(self: QuadMesh,
                                  meshWidth: {__add__},
                                  meshHeight: {__add__},
                                  coordinates: Any) -> tuple[None, None]: ...

    @artist.allow_rasterization
    def draw(self: QuadMesh,
             renderer: {open_group, new_gc, close_group}) -> Optional[Any]: ...


class BrokenBarHCollection(PolyCollection):
    def __init__(self: BrokenBarHCollection,
                 xranges: list[tuple[float, float]],
                 yrange: tuple[float, float],
                 **kwargs) -> None: ...

    @classmethod
    def span_where(cls: Type[BrokenBarHCollection],
                   x: Any,
                   ymin: Any,
                   ymax: {__sub__},
                   where: Any,
                   **kwargs) -> BrokenBarHCollection: ...


class TriMesh(Collection):
    def __init__(self: TriMesh,
                 triangulation: {x, y},
                 **kwargs) -> None: ...

    def get_paths(self: TriMesh) -> Optional[list[Path]]: ...

    def set_paths(self: TriMesh) -> None: ...

    @staticmethod
    def convert_mesh_to_paths(tri: {get_masked_triangles, x, y}) -> list[Path]: ...

    @artist.allow_rasterization
    def draw(self: TriMesh,
             renderer: {open_group, new_gc, close_group}) -> Optional[Any]: ...


class CircleCollection(_CollectionWithSizes):
    def __init__(self: CircleCollection,
                 sizes: Union[float, ndarray, Iterable, int],
                 **kwargs) -> None: ...


class _CollectionWithSizes(Collection):
    def get_sizes(self: _CollectionWithSizes) -> array.pyi: ...

    def set_sizes(self: _CollectionWithSizes,
                  sizes: Optional[ndarray],
                  dpi: float = 72.0) -> None: ...

    @artist.allow_rasterization
    def draw(self: _CollectionWithSizes,
             renderer: {open_group, new_gc, close_group}) -> Optional[Any]: ...


class EventCollection(LineCollection):
    def __init__(self: EventCollection,
                 positions: int,
                 orientation: str = 'horizontal',
                 lineoffset: float = 0,
                 linelength: float = 1,
                 linewidth: Any = None,
                 color: Iterable = None,
                 linestyle: Any = 'solid',
                 antialiased: Any = None,
                 **kwargs) -> None: ...

    def get_positions(self: EventCollection) -> list: ...

    def set_positions(self: EventCollection,
                      positions: Union[int, ndarray]) -> Any: ...

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


class PathCollection(_CollectionWithSizes):
    def __init__(self: PathCollection,
                 paths: Any,
                 sizes: Union[ndarray, Iterable, int, float] = None,
                 **kwargs) -> None: ...

    def set_paths(self: PathCollection,
                  paths: Any) -> None: ...

    def get_paths(self: PathCollection) -> Any: ...

    def legend_elements(self: PathCollection,
                        prop: str = "colors",
                        num: Union[int, None, ndarray, Iterable, float] = "auto",
                        fmt: str = None,
                        func: function = lambda x: x,
                        **kwargs) -> Any: ...


class StarPolygonCollection(RegularPolyCollection):
    pass


class EllipseCollection(Collection):
    def __init__(self: EllipseCollection,
                 widths: Union[ndarray, Iterable, int, float],
                 heights: Union[ndarray, Iterable, int, float],
                 angles: Union[ndarray, Iterable, int, float],
                 units: str = 'points',
                 **kwargs) -> None: ...

    def _set_transforms(self: EllipseCollection) -> Any: ...

    @artist.allow_rasterization
    def draw(self: EllipseCollection,
             renderer: {open_group, new_gc, close_group}) -> Optional[Any]: ...


class PatchCollection(Collection):
    def __init__(self: PatchCollection,
                 patches: Any,
                 match_original: bool = False,
                 **kwargs) -> None: ...

    def set_paths(self: PatchCollection,
                  patches: Any) -> None: ...


class LineCollection(Collection):
    def __init__(self: LineCollection,
                 segments: Union[Iterable[ndarray], Iterable, int, float],
                 zorder: int = 2,
                 *args,
                 **kwargs) -> None: ...

    def set_segments(self: LineCollection,
                     segments: Union[Iterable[ndarray], Iterable, int, float, ndarray]) -> None: ...

    def get_segments(self: LineCollection) -> list: ...

    def _add_offsets(self: LineCollection,
                     segs: list[Union[ndarray, MaskedArray]]) -> list[Union[ndarray, MaskedArray]]: ...

    def _get_default_linewidth(self: LineCollection) -> Optional[Any]: ...

    def _get_default_antialiased(self: LineCollection) -> Optional[Any]: ...

    def _get_default_edgecolor(self: LineCollection) -> Optional[Any]: ...

    def _get_default_facecolor(self: LineCollection) -> str: ...

    def set_color(self: LineCollection,
                  c: Iterable) -> None: ...

    def get_color(self: LineCollection) -> str: ...


class RegularPolyCollection(_CollectionWithSizes):
    def __init__(self: RegularPolyCollection,
                 numsides: int,
                 rotation: float = 0,
                 sizes: Union[Iterable, tuple[float]] = (1,),
                 **kwargs) -> None: ...

    def get_numsides(self: RegularPolyCollection) -> int: ...

    def get_rotation(self: RegularPolyCollection) -> float: ...

    @artist.allow_rasterization
    def draw(self: RegularPolyCollection,
             renderer: {open_group, new_gc, close_group}) -> Optional[Any]: ...
