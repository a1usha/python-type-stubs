from typing import Optional


class Triangulation(object):
    def __init__(self: Triangulation,
                 x: Any,
                 y: Any,
                 triangles: Optional[int] = None,
                 mask: Any = None) -> Any: ...

    def calculate_plane_coefficients(self: Triangulation,
                                     z: Any) -> None: ...

    @property
    def edges(self: Triangulation) -> Optional[Any]: ...

    def get_cpp_triangulation(self: Triangulation) -> Triangulation: ...

    def get_masked_triangles(self: Triangulation) -> Optional[ndarray]: ...

    @staticmethod
    def get_from_args_and_kwargs(*args,
                                 **kwargs) -> tuple[Triangulation, Any, dict[str, Any]]: ...

    def get_trifinder(self: Triangulation) -> TrapezoidMapTriFinder: ...

    @property
    def neighbors(self: Triangulation) -> Optional[Any]: ...

    def set_mask(self: Triangulation,
                 mask: Any) -> Any: ...
