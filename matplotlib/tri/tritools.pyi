from matplotlib.tri import Triangulation as Triangulation
from matplotlib import _api as _api
from typing import Any
from typing import Tuple

from matplotlib.tri.tritools import TriAnalyzer
from object import object


class TriAnalyzer(object):
    _triangulation: Any

    def __init__(self: TriAnalyzer,
                 triangulation: Any) -> None: ...

    def scale_factors(self: TriAnalyzer) -> Tuple[float, float]: ...

    def circle_ratios(self: TriAnalyzer,
                      rescale: bool = True) -> Any: ...

    def get_flat_tri_mask(self: TriAnalyzer,
                          min_circle_ratio: float = 0.01,
                          rescale: bool = True) -> Any: ...

    def _get_compressed_triangulation(self: TriAnalyzer) -> Any: ...

    def _total_to_compress_renum(valid: int) -> Any: ...
