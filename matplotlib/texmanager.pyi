from typing import Any
from typing import Optional
from typing import Union
from typing import tuple


class TexManager(object):
    @functools.lru_cache()
    def __new__(cls: Type[TexManager]) -> TexManager: ...

    def get_font_config(self: TexManager) -> str: ...

    def get_basefile(self: TexManager,
                     tex: {strip},
                     fontsize: {__mul__},
                     dpi: Optional[Any] = None) -> str: ...

    def get_font_preamble(self: TexManager) -> str: ...

    def get_custom_preamble(self: TexManager) -> Optional[Any]: ...

    def _get_preamble(self: TexManager) -> str: ...

    def make_tex(self: TexManager,
                 tex: {strip},
                 fontsize: {__mul__}) -> str: ...

    @_api.deprecated("3.3")
    def make_tex_preview(self: TexManager,
                         tex: {strip},
                         fontsize: {__mul__}) -> str: ...

    def _run_checked_subprocess(self: TexManager,
                                command: Union[list[str], list[str]],
                                tex: {strip},
                                cwd: Any = None) -> bytes: ...

    def make_dvi(self: TexManager,
                 tex: {strip},
                 fontsize: Any) -> str: ...

    @_api.deprecated("3.3")
    def make_dvi_preview(self: TexManager,
                         tex: {strip},
                         fontsize: Any) -> str: ...

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
                 rgb: tuple[int, int, int] = (0, 0, 0)) -> ndarray: ...

    def get_text_width_height_descent(self: TexManager,
                                      tex: {strip},
                                      fontsize: Any,
                                      renderer: {points_to_pixels} = None) -> Union[
        tuple[int, int, int], tuple[Any, Any, Any]]: ...
