from typing import Any
from typing import Optional

from matplotlib.font_manager import FontProperties


class MathtextBackendPdf(MathtextBackend):
    def __init__(self: MathtextBackendPdf) -> None: ...

    def render_glyph(self: MathtextBackendPdf,
                     ox: Any,
                     oy: Any,
                     info: {font, offset, fontsize, num, symbol_name}) -> None: ...

    def render_rect_filled(self: MathtextBackendPdf,
                           x1: Any,
                           y1: Any,
                           x2: {__sub__},
                           y2: {__sub__}) -> None: ...

    def get_results(self: MathtextBackendPdf,
                    box: {height, glue_order, glue_sign, children},
                    used_characters: Any) -> _PDFResult: ...


class GlueSpec(object):
    def __init__(self: GlueSpec,
                 width: float = 0.,
                 stretch: float = 0.,
                 stretch_order: int = 0,
                 shrink: float = 0.,
                 shrink_order: int = 0) -> None: ...

    def copy(self: GlueSpec) -> GlueSpec: ...

    @classmethod
    def factory(cls: Type[GlueSpec],
                glue_type: Any) -> Any: ...


class MathtextBackendSvg(MathtextBackend):
    def __init__(self: MathtextBackendSvg) -> None: ...

    def render_glyph(self: MathtextBackendSvg,
                     ox: Any,
                     oy: Any,
                     info: {offset, font, fontsize, num, metrics}) -> None: ...

    def render_rect_filled(self: MathtextBackendSvg,
                           x1: Any,
                           y1: Any,
                           x2: {__sub__},
                           y2: {__sub__}) -> None: ...

    def get_results(self: MathtextBackendSvg,
                    box: {height, glue_order, glue_sign, children},
                    used_characters: Any) -> tuple[int, int, int, SimpleNamespace, Any]: ...


class MathtextBackend(object):
    def __init__(self: MathtextBackend) -> None: ...

    def set_canvas_size(self: MathtextBackend,
                        w: int,
                        h: Any,
                        d: Any) -> None: ...

    def render_glyph(self: MathtextBackend,
                     ox: Any,
                     oy: Any,
                     info: Any) -> Any: ...

    def render_rect_filled(self: MathtextBackend,
                           x1: Any,
                           y1: Any,
                           x2: Any,
                           y2: Any) -> Any: ...

    def get_results(self: MathtextBackend,
                    box: Any) -> Any: ...

    def get_hinting_type(self: MathtextBackend) -> int: ...


class MathtextBackendCairo(MathtextBackend):
    def __init__(self: MathtextBackendCairo) -> None: ...

    def render_glyph(self: MathtextBackendCairo,
                     ox: Any,
                     oy: Any,
                     info: {offset, num, font, fontsize}) -> None: ...

    def render_rect_filled(self: MathtextBackendCairo,
                           x1: Any,
                           y1: {__sub__},
                           x2: {__sub__},
                           y2: {__sub__}) -> None: ...

    def get_results(self: MathtextBackendCairo,
                    box: {height, glue_order, glue_sign, children},
                    used_characters: Any) -> tuple[int, int, int, list, list]: ...


class MathtextBackendAgg(MathtextBackend):
    def __init__(self: MathtextBackendAgg) -> None: ...

    def _update_bbox(self: MathtextBackendAgg,
                     x1: Any,
                     y1: Any,
                     x2: Any,
                     y2: Any) -> None: ...

    def set_canvas_size(self: MathtextBackendAgg,
                        w: int,
                        h: Any,
                        d: Any) -> None: ...

    def render_glyph(self: MathtextBackendAgg,
                     ox: Any,
                     oy: Any,
                     info: Any) -> None: ...

    def render_rect_filled(self: MathtextBackendAgg,
                           x1: Any,
                           y1: Any,
                           x2: Any,
                           y2: Any) -> None: ...

    def get_results(self: MathtextBackendAgg,
                    box: {height, depth, glue_order, glue_sign, children},
                    used_characters: Any) -> tuple[int, int, int, int, int, Any, Any]: ...

    def get_hinting_type(self: MathtextBackendAgg) -> int: ...


class MathtextBackendBitmap(MathtextBackendAgg):
    def get_results(self: MathtextBackendBitmap,
                    box: {height, depth, glue_order, glue_sign, children},
                    used_characters: Any) -> tuple[Any, int]: ...


class MathtextBackendPath(MathtextBackend):
    def __init__(self: MathtextBackendPath) -> None: ...

    def render_glyph(self: MathtextBackendPath,
                     ox: Any,
                     oy: Any,
                     info: {offset, font, fontsize, num}) -> None: ...

    def render_rect_filled(self: MathtextBackendPath,
                           x1: Any,
                           y1: Any,
                           x2: {__sub__},
                           y2: {__sub__}) -> None: ...

    def get_results(self: MathtextBackendPath,
                    box: {height, glue_order, glue_sign, children},
                    used_characters: Any) -> _Result: ...


class MathTextParser(object):
    def __init__(self: MathTextParser,
                 output: {lower}) -> None: ...

    def parse(self: MathTextParser,
              s: str,
              dpi: int = 72,
              prop: FontProperties = None,
              _force_standard_ps_fonts: bool = False) -> Any: ...

    @functools.lru_cache(50)
    def _parse_cached(self: MathTextParser,
                      s: str,
                      dpi: Any,
                      prop: Optional[{get_math_fontfamily, get_size_in_points}],
                      force_standard_ps_fonts: Any) -> Any: ...

    @_api.deprecated("3.4", alternative="mathtext.math_to_image")
    def to_mask(self: MathTextParser,
                texstr: str,
                dpi: float = 120,
                fontsize: int = 14) -> Any: ...

    @_api.deprecated("3.4", alternative="mathtext.math_to_image")
    def to_rgba(self: MathTextParser,
                texstr: str,
                color: Any = 'black',
                dpi: float = 120,
                fontsize: int = 14) -> Any: ...

    @_api.deprecated("3.4", alternative="mathtext.math_to_image")
    def to_png(self: MathTextParser,
               filename: {__eq__, name},
               texstr: str,
               color: Any = 'black',
               dpi: float = 120,
               fontsize: int = 14) -> int: ...

    @_api.deprecated("3.4", alternative="mathtext.math_to_image")
    def get_depth(self: MathTextParser,
                  texstr: str,
                  dpi: float = 120,
                  fontsize: int = 14) -> int: ...


class MathTextWarning(Warning):
    pass


class MathtextBackendPs(MathtextBackend):
    def __init__(self: MathtextBackendPs) -> None: ...

    def render_glyph(self: MathtextBackendPs,
                     ox: Any,
                     oy: Any,
                     info: {offset, postscript_name, fontsize, symbol_name}) -> None: ...

    def render_rect_filled(self: MathtextBackendPs,
                           x1: Any,
                           y1: Any,
                           x2: {__sub__},
                           y2: {__sub__}) -> None: ...

    def get_results(self: MathtextBackendPs,
                    box: {height, glue_order, glue_sign, children},
                    used_characters: Any) -> _PSResult: ...


def math_to_image(s: str,
                  filename_or_obj: Any,
                  prop: Any = None,
                  dpi: Optional[float] = None,
                  format: Optional[str] = None) -> Any: ...


@_api.deprecated("3.4")
def ship(ox: Any,
         oy: {__add__},
         box: {height, glue_order, glue_sign, children}) -> Optional[Any]: ...