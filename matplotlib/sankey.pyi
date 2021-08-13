from typing import Any
from typing import Union
from typing import tuple


class Sankey(object):
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
             center: tuple[int, int] = (0, 0)) -> list[tuple[uint8, Any]]: ...

    def _add_input(self: Sankey,
                   path: Union[list[tuple[uint8, list[float]]], list[
                       Union[tuple[uint8, list[float]], tuple[uint8, list[float]]]]],
                   angle: Any,
                   flow: Any,
                   length: Any) -> Union[tuple[list[int], list[int]], tuple[
        Union[list[float], list[Union[float, int]]], Union[list[float], list[Union[float, int]]]]]: ...

    def _add_output(self: Sankey,
                    path: Union[list[Union[tuple[uint8, list[float]], tuple[uint8, list[float]]]], list[
                        tuple[uint8, list[float]]]],
                    angle: Any,
                    flow: Any,
                    length: Any) -> Union[tuple[list[int], list[int]], tuple[
        Union[list[float], list[Union[float, int]]], Union[list[float], list[Union[float, int]]]]]: ...

    def _revert(self: Sankey,
                path: list[tuple[uint8, list[float]]],
                first_action: uint8 = Path.LINETO) -> list[tuple[uint8, Any]]: ...

    @docstring.dedent_interpd
    def add(self: Sankey,
            patchlabel: str = '',
            flows: Iterable[float] = None,
            orientations: int = None,
            labels: Iterable[Optional[str]] = '',
            trunklength: float = 1.0,
            pathlengths: Iterable[float] = 0.25,
            prior: int = None,
            connect: tuple[int, int] = (0, 0),
            rotation: float = 0path: Any = ...,
            **kwargs) -> Sankey: ...

    def finish(self: Sankey) -> list: ...
