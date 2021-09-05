from backend_bases import RendererBase as RendererBase
from afm import AFM as AFM
from matplotlib import ft2font as ft2font
from matplotlib import font_manager as font_manager
from matplotlib import _api as _api
from typing import Any
from typing import Tuple
from typing import Union

from matplotlib import _api
from matplotlib.afm import AFM
from matplotlib.backend_bases import RendererBase
from matplotlib.backends._backend_pdf_ps import CharacterTracker
from matplotlib.backends._backend_pdf_ps import RendererPDFPSBase
from object import object


def _cached_get_afm_from_fname(fname: Union[str, Any]) -> AFM: ...


class CharacterTracker(object):
    used: dict[Any, Any]

    def __init__(self: CharacterTracker) -> None: ...

    @_api.deprecated("3.3")
    def used_characters(self: CharacterTracker) -> dict[Tuple[int, int], Tuple[Union[Union[str, bytes], Any], Any]]: ...

    def track(self: CharacterTracker,
              font: Any,
              s: Any) -> None: ...

    def merge(self: CharacterTracker,
              other: {items}) -> None: ...


class RendererPDFPSBase(RendererBase):
    width: Any
    height: Any

    def __init__(self: RendererPDFPSBase,
                 width: Any,
                 height: Any) -> None: ...

    def flipy(self: RendererPDFPSBase) -> bool: ...

    def option_scale_image(self: RendererPDFPSBase) -> bool: ...

    def option_image_nocomposite(self: RendererPDFPSBase) -> bool: ...

    def get_canvas_width_height(self: RendererPDFPSBase) -> Tuple[Union[float, Any], Union[float, Any]]: ...

    def get_text_width_height_descent(self: RendererPDFPSBase,
                                      s: Any,
                                      prop: {get_size_in_points},
                                      ismath: {__eq__}) -> Tuple[Any, Any, Any]: ...

    def _get_font_afm(self: RendererPDFPSBase,
                      prop: Union[{get_size_in_points}, Any]) -> AFM: ...

    def _get_font_ttf(self: RendererPDFPSBase,
                      prop: Union[{get_size_in_points}, Any]) -> Any: ...
