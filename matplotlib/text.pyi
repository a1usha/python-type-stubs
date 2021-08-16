from typing import Any
from typing import Optional
from typing import Union
from typing import tuple

from matplotlib.text import Text


@contextlib.contextmanager
def _wrap_text(textobj: Text) -> Generator[Text, Any, None]: ...


def get_rotation(rotation: str) -> float: ...


def _get_textbox(text: Text,
                 renderer: Optional[Any]) -> tuple[Any, Any, Any, Any]: ...


@cbook._define_aliases({
    "color": ["c"],
    "fontfamily": ["family"],
    "fontproperties": ["font", "font_properties"],
    "horizontalalignment": ["ha"],
    "multialignment": ["ma"],
    "fontname": ["name"],
    "fontsize": ["size"],
    "fontstretch": ["stretch"],
    "fontstyle": ["style"],
    "fontvariant": ["variant"],
    "verticalalignment": ["va"],
    "fontweight": ["weight"],
})
class Text(Artist):
    def __repr__(self: Text) -> str: ...

    def __init__(self: Text,
                 x: int = 0,
                 y: int = 0,
                 text: str = '',
                 color: Any = None,
                 verticalalignment: str = 'baseline',
                 horizontalalignment: str = 'left',
                 multialignment: Any = None,
                 fontproperties: Any = None,
                 rotation: Any = None,
                 linespacing: Any = None,
                 rotation_mode: Any = None,
                 usetex: Any = None,
                 wrap: bool = False,
                 transform_rotates_text: bool = False,
                 **kwargs) -> None: ...

    def update(self: Text,
               kwargs: dict[str, Any]) -> None: ...

    def __getstate__(self: Text) -> dict[str, Any]: ...

    def contains(self: Text,
                 mouseevent: MouseEvent) -> Union[tuple[Any, Any], tuple[bool, dict], tuple[bool, dict[str, Any]]]: ...

    def _get_xy_display(self: Text) -> Any: ...

    def _get_multialignment(self: Text) -> Any: ...

    def get_rotation(self: Text) -> float: ...

    def get_transform_rotates_text(self: Text) -> bool: ...

    def set_rotation_mode(self: Text,
                          m: Optional[str]) -> None: ...

    def get_rotation_mode(self: Text) -> Optional[str]: ...

    def update_from(self: Text,
                    other: {_transform, _transformSet, _visible, _alpha, clipbox, _clipon, _clippath, _label, _sketch,
                            _path_effects, sticky_edges}) -> None: ...

    def _get_layout(self: Text,
                    renderer: Optional[Any]) -> tuple[Bbox, list[tuple[str, tuple[int, int], Any]], int]: ...

    def set_bbox(self: Text,
                 rectprops: Any) -> None: ...

    def get_bbox_patch(self: Text) -> Any: ...

    def update_bbox_position_size(self: Text,
                                  renderer: Optional[Any]) -> None: ...

    def _update_clip_properties(self: Text) -> None: ...

    def set_clip_box(self: Text,
                     clipbox: Any) -> None: ...

    def set_clip_path(self: Text,
                      path: Any,
                      transform: Any = None) -> None: ...

    def set_clip_on(self: Text,
                    b: bool) -> None: ...

    def get_wrap(self: Text) -> bool: ...

    def set_wrap(self: Text,
                 wrap: bool) -> None: ...

    def _get_wrap_line_width(self: Text) -> Union[float, int]: ...

    def _get_dist_to_box(self: Text,
                         rotation: float,
                         x0: Any,
                         y0: Any,
                         figure_box: Any) -> float: ...

    def _get_rendered_text_width(self: Text,
                                 text: str) -> int: ...

    def _get_wrapped_text(self: Text) -> str: ...

    @artist.allow_rasterization
    def draw(self: Text,
             renderer: Optional[{open_group, get_canvas_width_height, new_gc, flipy, close_group}]) -> Optional[
        Any]: ...

    def get_color(self: Text) -> Any: ...

    def get_fontproperties(self: Text) -> Any: ...

    def get_fontfamily(self: Text) -> Any: ...

    def get_fontname(self: Text) -> Any: ...

    def get_fontstyle(self: Text) -> Any: ...

    def get_fontsize(self: Text) -> Any: ...

    def get_fontvariant(self: Text) -> Any: ...

    def get_fontweight(self: Text) -> Any: ...

    def get_stretch(self: Text) -> Any: ...

    def get_horizontalalignment(self: Text) -> Any: ...

    def get_unitless_position(self: Text) -> tuple[float, float]: ...

    def get_position(self: Text) -> tuple[int, int]: ...

    def get_prop_tup(self: Text,
                     renderer: Optional[Any] = None) -> tuple[
        float, float, str, Any, Any, Any, int, Any, Optional[str], bool, Any, ReferenceType, float]: ...

    def get_text(self: Text) -> str: ...

    def get_verticalalignment(self: Text) -> Any: ...

    def get_window_extent(self: Text,
                          renderer: Any = None,
                          dpi: Optional[float] = None) -> Bbox: ...

    def set_backgroundcolor(self: Text,
                            color: Any) -> None: ...

    def set_color(self: Text,
                  color: Any) -> None: ...

    def set_horizontalalignment(self: Text,
                                align: str) -> None: ...

    def set_multialignment(self: Text,
                           align: str) -> None: ...

    def set_linespacing(self: Text,
                        spacing: Any) -> None: ...

    def set_fontfamily(self: Text,
                       fontname: str) -> None: ...

    def set_fontvariant(self: Text,
                        variant: str) -> None: ...

    def set_fontstyle(self: Text,
                      fontstyle: str) -> None: ...

    def set_fontsize(self: Text,
                     fontsize: str) -> None: ...

    def get_math_fontfamily(self: Text) -> Any: ...

    def set_math_fontfamily(self: Text,
                            fontfamily: str) -> None: ...

    def set_fontweight(self: Text,
                       weight: str) -> None: ...

    def set_fontstretch(self: Text,
                        stretch: str) -> None: ...

    def set_position(self: Text,
                     xy: tuple[float, float]) -> None: ...

    def set_x(self: Text,
              x: float) -> None: ...

    def set_y(self: Text,
              y: float) -> None: ...

    def set_rotation(self: Text,
                     s: str) -> None: ...

    def set_transform_rotates_text(self: Text,
                                   t: bool) -> None: ...

    def set_verticalalignment(self: Text,
                              align: str) -> None: ...

    def set_text(self: Text,
                 s: object) -> None: ...

    def _preprocess_math(self: Text,
                         s: str) -> Union[tuple[str, str], tuple[str, bool], tuple[str, bool]]: ...

    def set_fontproperties(self: Text,
                           fp: Any) -> None: ...

    def set_usetex(self: Text,
                   usetex: Optional[bool]) -> None: ...

    def get_usetex(self: Text) -> Any: ...

    def set_fontname(self: Text,
                     fontname: str) -> Any: ...


class OffsetFrom(object):
    def __init__(self: OffsetFrom,
                 artist: Any,
                 ref_coord: tuple[float, float],
                 unit: str = "points") -> None: ...

    def set_unit(self: OffsetFrom,
                 unit: str) -> None: ...

    def get_unit(self: OffsetFrom) -> str: ...

    def _get_scale(self: OffsetFrom,
                   renderer: Any) -> float: ...

    def __call__(self: OffsetFrom,
                 renderer: Any) -> Transform: ...


class _AnnotationBase(object):
    def __init__(self: _AnnotationBase,
                 xy: tuple[float, float],
                 xycoords: str = 'data',
                 annotation_clip: Any = None) -> None: ...

    def _get_xy(self: _AnnotationBase,
                renderer: Optional[Any],
                x: float,
                y: Any,
                s: Any) -> Union[ndarray, Iterable, int, float]: ...

    def _get_xy_transform(self: _AnnotationBase,
                          renderer: Optional[Any],
                          s: Union[tuple, str, {__ne__}, None]) -> Union[
        BlendedAffine2D, BlendedGenericTransform, BboxTransformTo, Transform, Affine2D]: ...

    def _get_ref_xy(self: _AnnotationBase,
                    renderer: Optional[Any]) -> Union[ndarray, Iterable, int, float]: ...

    def set_annotation_clip(self: _AnnotationBase,
                            b: Optional[bool]) -> None: ...

    def get_annotation_clip(self: _AnnotationBase) -> Optional[bool]: ...

    def _get_position_xy(self: _AnnotationBase,
                         renderer: Optional[Any]) -> Union[ndarray, Iterable, int, float]: ...

    def _check_xy(self: _AnnotationBase,
                  renderer: Optional[Any]) -> bool: ...

    def draggable(self: _AnnotationBase,
                  state: Optional[bool] = None,
                  use_blit: bool = False) -> Optional[DraggableAnnotation]: ...


class Annotation(Text, _AnnotationBase):
    def __str__(self: Annotation) -> str: ...

    def __init__(self: Annotation,
                 text: str,
                 xy: tuple[float, float],
                 xytext: Any = None,
                 xycoords: Any = 'data',
                 textcoords: Optional[{__ne__}] = None,
                 arrowprops: Any = None,
                 annotation_clip: Any = None,
                 **kwargs) -> Any: ...

    def contains(self: Annotation,
                 event: {canvas}) -> tuple[Any, Any]: ...

    @property
    def xycoords(self: Annotation) -> Any: ...

    @xycoords.setter
    def xycoords(self: Annotation,
                 xycoords: Any) -> Any: ...

    @property
    def xyann(self: Annotation) -> tuple[int, int]: ...

    @xyann.setter
    def xyann(self: Annotation,
              xytext: Any) -> None: ...

    def get_anncoords(self: Annotation) -> Optional[{__ne__}]: ...

    def set_anncoords(self: Annotation,
                      coords: Any) -> None: ...

    def set_figure(self: Annotation,
                   fig: Any) -> None: ...

    def update_positions(self: Annotation,
                         renderer: Optional[Any]) -> None: ...

    @artist.allow_rasterization
    def draw(self: Annotation,
             renderer: Optional[{open_group, get_canvas_width_height, new_gc, flipy, close_group}]) -> Optional[
        Any]: ...

    def get_window_extent(self: Annotation,
                          renderer: Any = None) -> Bbox: ...

    def get_tightbbox(self: Annotation,
                      renderer: Any) -> Bbox: ...
