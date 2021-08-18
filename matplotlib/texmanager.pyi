from typing import Any
from typing import Optional
from typing import Tuple
from typing import Type
from typing import Union

from matplotlib import _api
from matplotlib.texmanager import TexManager
from numpy.core._multiarray_umath import ndarray
from object import object


class TexManager(object):
    def __new__(cls: Type[TexManager]) -> TexManager: ...

    def get_font_config(self: TexManager) -> str: ...

    def get_basefile(self: TexManager,
                     tex: Union[{strip}, Any],
                     fontsize: Union[{__mul__}, Any],
                     dpi: Optional[Any] = None) -> str: ...

    def get_font_preamble(self: TexManager) -> str: ...

    def get_custom_preamble(self: TexManager) -> Optional[Any]: ...

    def _get_preamble(self: TexManager) -> str: ...

    def make_tex(self: TexManager,
                 tex: Union[{strip}, Any],
                 fontsize: {__mul__}) -> str: ...

    @_api.deprecated("3.3")
    def make_tex_preview(self: TexManager,
                         tex: Union[{strip}, Any],
                         fontsize: {__mul__}) -> Union[str, Any]: ...

    def _run_checked_subprocess(self: TexManager,
                                command: Union[Union[list[str], list[Union[str, Any]]], Any],
                                tex: Union[{strip}, Any],
                                *,
                                cwd: Any = None) -> Union[bytes, Any]: ...

    def make_dvi(self: TexManager,
                 tex: Union[{strip}, Any],
                 fontsize: Any) -> Union[str, Any]: ...

    @_api.deprecated("3.3")
    def make_dvi_preview(self: TexManager,
                         tex: Union[{strip}, Any],
                         fontsize: Any) -> Union[str, Any]: ...

    def make_png(self: TexManager,
                 tex: Any,
                 fontsize: Optional[Any],
                 dpi: Any) -> str: ...

    def get_grey(self: TexManager,
                 tex: Any,
                 fontsize: Any = None,
                 dpi: Any = None) -> Optional[Any]: ...

    def get_rgba(self: TexManager,
                 tex: Any,
                 fontsize: Any = None,
                 dpi: Any = None,
                 rgb: Union[tuple[int, int, int], Any] = (0, 0, 0)) -> ndarray: ...

    def get_text_width_height_descent(self: TexManager,
                                      tex: {strip},
                                      fontsize: Any,
                                      renderer: {points_to_pixels} = None) -> Union[
        Tuple[int, int, int], Tuple[Any, Any, Any]]: ...
