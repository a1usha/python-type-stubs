from typing import Iterable
from typing import Optional
from typing import Union

from matplotlib.path import Path
from matplotlib.transforms import Transform
from numpy.core._multiarray_umath import ndarray


class Path(object):
    def __init__(self: Path,
                 vertices: int,
                 codes: Union[ndarray, Iterable, int, float, None] = None,
                 _interpolation_steps: Optional[int] = 1,
                 closed: Optional[bool] = False,
                 readonly: Optional[bool] = False) -> Any: ...

    @classmethod
    def _fast_from_codes_and_verts(cls: Type[Path],
                                   verts: Any,
                                   codes: Any,
                                   internals_from: Optional[Path] = None) -> Path: ...

    def _update_values(self: Path) -> None: ...

    @property
    def vertices(self: Path) -> ndarray: ...

    @vertices.setter
    def vertices(self: Path,
                 vertices: Any) -> Any: ...

    @property
    def codes(self: Path) -> Optional[ndarray]: ...

    @codes.setter
    def codes(self: Path,
              codes: Any) -> Any: ...

    @property
    def simplify_threshold(self: Path) -> Optional[Any]: ...

    @simplify_threshold.setter
    def simplify_threshold(self: Path,
                           threshold: Any) -> None: ...

    @property
    def should_simplify(self: Path) -> Union[bool, None, ndarray]: ...

    @should_simplify.setter
    def should_simplify(self: Path,
                        should_simplify: Any) -> None: ...

    @property
    def readonly(self: Path) -> bool: ...

    def __copy__(self: Path) -> Path: ...

    def __deepcopy__(self: Path,
                     memo: Any = None) -> Path: ...

    @classmethod
    def make_compound_path_from_polys(cls: Type[Path],
                                      XY: {shape}) -> Path: ...

    @classmethod
    def make_compound_path(cls: Type[Path],
                           *args) -> Path: ...

    def __repr__(self: Path) -> str: ...

    def __len__(self: Path) -> int: ...

    def iter_segments(self: Path,
                      transform: Optional[Transform] = None,
                      remove_nans: Optional[bool] = True,
                      clip: Optional[float] = None,
                      snap: Optional[bool] = False,
                      stroke_width: Optional[float] = 1.0,
                      simplify: Optional[bool] = None,
                      curves: Optional[bool] = True,
                      sketch: Optional[Iterable] = None) -> Generator[tuple[ndarray, Any], Any, None]: ...

    def iter_bezier(self: Path,
                    **kwargs) -> Generator[tuple[BezierSegment, Any], Any, None]: ...

    @_api.delete_parameter
    def cleaned(self: Path,
                transform: Any = None,
                remove_nans: bool = False,
                clip: Any = None,
                quantize: bool = False,
                simplify: bool = False,
                curves: bool = False,
                stroke_width: float = 1.0,
                snap: bool = False,
                sketch: Any = None) -> Path: ...

    def transformed(self: Path,
                    transform: {transform}) -> Path: ...

    def contains_point(self: Path,
                       point: tuple[float, float],
                       transform: Optional[Transform] = None,
                       radius: float = 0.0) -> bool: ...

    def contains_points(self: Path,
                        points: int,
                        transform: Optional[Transform] = None,
                        radius: float = 0.0) -> Any: ...

    def contains_path(self: Path,
                      path: Any,
                      transform: Any = None) -> None: ...

    def get_extents(self: Path,
                    transform: Optional[Transform] = None,
                    **kwargs) -> Bbox: ...

    def intersects_path(self: Path,
                        other: Any,
                        filled: bool = True) -> None: ...

    def intersects_bbox(self: Path,
                        bbox: {x0, y0, x1, y1},
                        filled: bool = True) -> None: ...

    def interpolated(self: Path,
                     steps: {__eq__}) -> Path: ...

    def to_polygons(self: Path,
                    transform: Any = None,
                    width: int = 0,
                    height: int = 0,
                    closed_only: bool = True) -> Union[list, list[Union[list[Optional[Any]], ndarray]], None]: ...

    @classmethod
    def unit_rectangle(cls: Type[Path]) -> Path: ...

    @classmethod
    def unit_regular_polygon(cls: Type[Path],
                             numVertices: {__le__}) -> Path: ...

    @classmethod
    def unit_regular_star(cls: Type[Path],
                          numVertices: {__le__},
                          innerCircle: float = 0.5) -> Path: ...

    @classmethod
    def unit_regular_asterisk(cls: Type[Path],
                              numVertices: Any) -> Path: ...

    @classmethod
    def unit_circle(cls: Type[Path]) -> Path: ...

    @classmethod
    def circle(cls: Type[Path],
               center: int = (0., 0.),
               radius: float = 1.,
               readonly: bool = False) -> Path: ...

    @classmethod
    def unit_circle_righthalf(cls: Type[Path]) -> Path: ...

    @classmethod
    def arc(cls: Type[Path],
            theta1: Any,
            theta2: {__sub__, __ne__},
            n: Optional[{__lt__, __add__}] = None,
            is_wedge: bool = False) -> Path: ...

    @classmethod
    def wedge(cls: Type[Path],
              theta1: Any,
              theta2: {__sub__, __ne__},
              n: Any = None) -> Path: ...

    @staticmethod
    @lru_cache
    def hatch(hatchpattern: Optional[{count}],
              density: int = 6) -> Optional[Path]: ...

    def clip_to_bbox(self: Path,
                     bbox: Any,
                     inside: bool = True) -> Path: ...


def get_path_collection_extents(master_transform: Any,
                                paths: Iterable[Path],
                                transforms: Any,
                                offsets: int,
                                offset_transform: Any) -> Bbox: ...