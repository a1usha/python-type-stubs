from matplotlib import docstring as docstring
from matplotlib.transforms import Affine2D as Affine2D
from matplotlib.patches import PathPatch as PathPatch
from matplotlib.path import Path as Path
from types import SimpleNamespace as SimpleNamespace
from typing import Any
from typing import Iterable
from typing import Tuple
from typing import Union

from matplotlib.sankey import Sankey
from numpy.core import uint8
from object import object

RIGHT: int
UP: int
DOWN: int
__version__: str


class Sankey(object):
    extent: Any
    margin: float
    offset: float
    format: str
    scale: float
    diagrams: list[Any]
    unit: str
    ax: Any
    gap: float
    pitch: Any
    radius: float
    shoulder: float
    tolerance: float

    def __init__(self: Sankey,
                 ax: Any = None,
                 scale: float = 1.0,
                 unit: str = '',
                 format: str = '%G',
                 gap: float = 0.25,
                 radius: float = 0.1,
                 shoulder: float = 0.03,
                 offset: float = 0.15,
                 head_angle: int = 100,
                 margin: float = 0.4,
                 tolerance: float = 1e-6,
                 **kwargs) -> Any: ...

    def _arc(self: Sankey,
             quadrant: int = 0,
             cw: bool = True,
             radius: int = 1,
             center: Union[tuple[int, int], Any] = (0, 0)) -> list[Tuple[uint8, Any]]: ...

    def _add_input(self: Sankey,
                   path: Union[Union[list[tuple[uint8, list[Union[float, Any]]]], list[
                       Union[tuple[uint8, list[Union[float, Any]]], tuple[uint8, list[float]]]]], Any],
                   angle: Any,
                   flow: Any,
                   length: Any) -> Union[Tuple[list[int], list[int]], Tuple[
        Union[list[Union[float, Any]], list[Union[Union[float, int], Any]]], Union[
            list[Union[float, Any]], list[Union[Union[float, int], Any]]]]]: ...

    def _add_output(self: Sankey,
                    path: Union[Union[
                                    list[Union[tuple[uint8, list[Union[float, Any]]], tuple[uint8, list[float]]]], list[
                                        tuple[uint8, list[Union[float, Any]]]]], Any],
                    angle: Any,
                    flow: Any,
                    length: Any) -> Union[Tuple[list[int], list[int]], Tuple[
        Union[list[Union[float, Any]], list[Union[Union[float, int], Any]]], Union[
            list[Union[float, Any]], list[Union[Union[float, int], Any]]]]]: ...

    def _revert(self: Sankey,
                path: Union[list[tuple[uint8, list[Union[float, Any]]]], Any],
                first_action: uint8 = Path.LINETO) -> list[Tuple[Union[uint8, Any], Any]]: ...

    def add(self: Sankey,
            patchlabel: str = '',
            flows: Iterable[float] = None,
            orientations: int = None,
            labels: Iterable[Optional[str]] = '',
            trunklength: float = 1.0,
            pathlengths: Iterable[float] = 0.25,
            prior: int = None,
            connect: tuple[int, int] = (0, 0),
            rotation: float = 0,
            path: Any = ...,
            **kwargs) -> Sankey: ...

    def finish(self: Sankey) -> list[Any]: ...
