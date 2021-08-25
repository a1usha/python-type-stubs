from matplotlib.transforms import Affine2D as Affine2D
from matplotlib.transforms import TransformedBbox as TransformedBbox
from matplotlib.transforms import Bbox as Bbox
from typing import Any
from typing import Callable
from typing import Optional
from typing import Tuple


def adjust_bbox(fig: {bbox, bbox_inches, get_tight_layout, transFigure, set_tight_layout, axes, dpi, patch},
                bbox_inches: {width, height},
                fixed_dpi: Optional[{__truediv__}] = None) -> Callable[[], None]: ...


def process_figure_for_rasterizing(fig: Any,
                                   bbox_inches_restore: Any,
                                   fixed_dpi: Any = None) -> Tuple[Any, Callable[[], None]]: ...