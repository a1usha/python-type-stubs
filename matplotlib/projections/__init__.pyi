from mpl_toolkits.mplot3d import Axes3D as Axes3D
from polar import PolarAxes as PolarAxes
from geo import MollweideAxes as MollweideAxes
from geo import LambertAxes as LambertAxes
from geo import HammerAxes as HammerAxes
from geo import AitoffAxes as AitoffAxes
from matplotlib import docstring as docstring
from matplotlib import axes as axes
from typing import Any
from typing import Union

from matplotlib.projections import ProjectionRegistry
from object import object


class ProjectionRegistry(object):
    _all_projection_types: dict[Any, Any]

    def __init__(self: ProjectionRegistry) -> None: ...

    def register(self: ProjectionRegistry,
                 *args) -> None: ...

    def get_projection_class(self: ProjectionRegistry,
                             name: Union[str, Any]) -> Any: ...

    def get_projection_names(self: ProjectionRegistry) -> list[Union[SupportsLessThan, Any]]: ...


projection_registry: ProjectionRegistry


def register_projection(cls: Any) -> None: ...


get_projection_names: Callable[[], list[Union[SupportsLessThan, Any]]]


def get_projection_class(projection: Any = None) -> Any: ...