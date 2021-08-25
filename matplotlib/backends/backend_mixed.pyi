from matplotlib.tight_bbox import process_figure_for_rasterizing as process_figure_for_rasterizing
from matplotlib.backends.backend_agg import RendererAgg as RendererAgg
from matplotlib import cbook as cbook
from typing import Any
from typing import Union

from matplotlib.backend_bases import RendererBase
from matplotlib.backends.backend_mixed import MixedModeRenderer
from matplotlib.figure import Figure
from object import object


class MixedModeRenderer(object):
    figure: Figure
    _raster_renderer_class: Union[Type[RendererAgg], RendererBase]
    _vector_renderer: RendererBase
    _renderer: RendererBase
    _raster_renderer: None
    _bbox_inches_restore: Any
    dpi: float
    _width: Union[int, float, complex]
    _height: Union[int, float, complex]
    _figdpi: Union[Optional[float], Any]

    def __init__(self: MixedModeRenderer,
                 figure: Figure,
                 width: Union[int, float, complex],
                 height: Union[int, float, complex],
                 dpi: float,
                 vector_renderer: RendererBase,
                 raster_renderer_class: RendererBase = None,
                 bbox_inches_restore: Any = None) -> None: ...

    def __getattr__(self: MixedModeRenderer,
                    attr: Any) -> Any: ...

    def start_rasterizing(self: MixedModeRenderer) -> None: ...

    def stop_rasterizing(self: MixedModeRenderer) -> None: ...
