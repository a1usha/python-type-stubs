from typing import Any
from typing import Generator
from typing import Iterable
from typing import Optional
from typing import Tuple
from typing import Type
from typing import Union

from matplotlib import _api
from matplotlib.path import Path
from matplotlib.transforms import Bbox
from matplotlib.transforms import Transform
from numpy.core._multiarray_umath import ndarray
from object import object


class Path(object):
    def __init__(self: Path,
                 vertices: int,
                 codes: Union[ndarray, Iterable, int, float, None] = None,
                 _interpolation_steps: Optional[int] = 1,
                 closed: Optional[bool] = False,
                 readonly: Optional[bool] = False) -> Any: ...

    def _fast_from_codes_and_verts(cls: Type[Path],
                                   verts: Any,
                                   codes: Any,
                                   internals_from: Optional[Path] = None) -> Path: ...

    def _update_values(self: Path) -> None: ...

    def vertices(self: Path) -> ndarray: ...

    def vertices(self: Path,
                 vertices: Any) -> Any: ...

    def codes(self: Path) -> Optional[ndarray]: ...

    def codes(self: Path,
              codes: Any) -> Any: ...

    def simplify_threshold(self: Path) -> Optional[Any]: ...

    def simplify_threshold(self: Path,
                           threshold: Any) -> None: ...

    def should_simplify(self: Path) -> Union[bool, None, ndarray]: ...

    def should_simplify(self: Path,
                        should_simplify: Any) -> None: ...

    def readonly(self: Path) -> bool: ...

    def __copy__(self: Path) -> Path: ...

    def __deepcopy__(self: Path,
                     memo: Any = None) -> Path: ...

    def make_compound_path_from_polys(cls: Type[Path],
                                      XY: {shape}) -> Path: ...

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
                      sketch: Optional[Iterable] = None) -> Generator[Tuple[ndarray, Any], Any, None]: ...

    def iter_bezier(self: Path,
                    **kwargs) -> Generator[Tuple[BezierSegment, Any], Any, None]: ...

    @_api.delete_parameter("3.3", "quantize")
    def cleaned(self: Path,
                transform: Optional[Transform] = None,
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

    def unit_rectangle(cls: Type[Path]) -> Path: ...

    def unit_regular_polygon(cls: Type[Path],
                             numVertices: {__le__}) -> Path: ...

    def unit_regular_star(cls: Type[Path],
                          numVertices: {__le__},
                          innerCircle: float = 0.5) -> Path: ...

    def unit_regular_asterisk(cls: Type[Path],
                              numVertices: Any) -> Path: ...

    def unit_circle(cls: Type[Path]) -> Path: ...

    def circle(cls: Type[Path],
               center: int = (0., 0.),
               radius: float = 1.,
               readonly: bool = False) -> Path: ...

    def unit_circle_righthalf(cls: Type[Path]) -> Path: ...

    def arc(cls: Type[Path],
            theta1: Any,
            theta2: {__sub__, __ne__},
            n: Optional[{__lt__, __add__}] = None,
            is_wedge: bool = False) -> Path: ...

    def wedge(cls: Type[Path],
              theta1: Any,
              theta2: {__sub__, __ne__},
              n: Any = None) -> Path: ...

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