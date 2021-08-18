from matplotlib.projections import ProjectionRegistry
from object import object


class ProjectionRegistry(object):
    def __init__(self: ProjectionRegistry) -> None: ...

    def register(self: ProjectionRegistry,
                 *args) -> None: ...

    def get_projection_class(self: ProjectionRegistry,
                             name: str) -> Any: ...

    def get_projection_names(self: ProjectionRegistry) -> list[SupportsLessThan]: ...


def register_projection(cls: Any) -> None: ...


def get_projection_class(projection: Any = None) -> Any: ...