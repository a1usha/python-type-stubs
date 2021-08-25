from transforms import Transform as Transform
from transforms import IdentityTransform as IdentityTransform
from transforms import BboxTransformTo as BboxTransformTo
from transforms import BboxBase as BboxBase
from transforms import Bbox as Bbox
from transforms import Affine2D as Affine2D
from textpath import TextPath as TextPath
from patches import Rectangle as Rectangle
from patches import FancyBboxPatch as FancyBboxPatch
from patches import FancyArrowPatch as FancyArrowPatch
from font_manager import FontProperties as FontProperties
from artist import Artist as Artist
from matplotlib import docstring as docstring
from matplotlib import cbook as cbook
from matplotlib import artist as artist
from matplotlib import _api as _api
from typing import ClassVar
from typing import Generator
from typing import Iterable
from typing import Optional
from typing import Tuple
from typing import Union

from matplotlib.artist import Artist
from matplotlib.backend_bases import MouseEvent
from matplotlib.offsetbox import DraggableAnnotation
from matplotlib.text import Annotation
from matplotlib.text import OffsetFrom
from matplotlib.text import Text
from matplotlib.text import _AnnotationBase
from matplotlib.transforms import Affine2D
from matplotlib.transforms import Bbox
from matplotlib.transforms import BboxTransformTo
from matplotlib.transforms import BlendedAffine2D
from matplotlib.transforms import BlendedGenericTransform
from matplotlib.transforms import Transform
from numpy.core._multiarray_umath import ndarray
from object import object

_log: Logger
from typing import Any


def _wrap_text(textobj: Union[Text, Any]) -> Union[Generator[Union[Text, Any], Any, None], Any]: ...


def get_rotation(rotation: str) -> float: ...


def _get_textbox(text: Union[Text, Any],
                 renderer: Optional[Any]) -> Tuple[Any, Any, Any, Any]: ...


class Text(Artist):
    zorder: ClassVar[int]
    _cached: ClassVar[maxdict]
    _transform_rotates_text: bool
    _bbox_patch: None
    _rotation: Any
    _renderer: None
    _usetex: Any
    _multialignment: Any
    _linespacing: Union[float, Any]
    _color: Any
    _picker: Any
    _verticalalignment: Any
    _horizontalalignment: Any
    _rotation_mode: Optional[str]
    stale: bool
    _x: int
    _y: int
    _wrap: bool
    _text: str
    _fontproperties: Any

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
               kwargs: Union[dict[str, Any], Any]) -> None: ...

    def __getstate__(self: Text) -> dict[str, Any]: ...

    def contains(self: Text,
                 mouseevent: MouseEvent) -> Union[
        Tuple[Any, Any], Tuple[bool, dict[Any, Any]], Tuple[Union[bool, Any], dict[str, Any]]]: ...

    def _get_xy_display(self: Text) -> Any: ...

    def _get_multialignment(self: Text) -> Any: ...

    def get_rotation(self: Text) -> Union[float, Any]: ...

    def get_transform_rotates_text(self: Text) -> bool: ...

    def set_rotation_mode(self: Text,
                          m: Optional[str]) -> None: ...

    def get_rotation_mode(self: Text) -> Optional[str]: ...

    def update_from(self: Text,
                    other: {_transform, _transformSet, _visible, _alpha, clipbox, _clipon, _clippath, _label, _sketch,
                            _path_effects, sticky_edges}) -> None: ...

    def _get_layout(self: Text,
                    renderer: Optional[Any]) -> Union[
        Tuple[Bbox, list[Tuple[str, Tuple[Union[int, Any], Union[int, Any]], Any]], Union[int, Any]], Any]: ...

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

    def _get_wrap_line_width(self: Text) -> Union[Union[float, int], Any]: ...

    def _get_dist_to_box(self: Text,
                         rotation: Union[Union[int, float], Any],
                         x0: Any,
                         y0: Any,
                         figure_box: Any) -> Union[float, Any]: ...

    def _get_rendered_text_width(self: Text,
                                 text: Union[str, Any]) -> int: ...

    def _get_wrapped_text(self: Text) -> str: ...

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

    def get_unitless_position(self: Text) -> Tuple[float, float]: ...

    def get_position(self: Text) -> Tuple[int, int]: ...

    def get_prop_tup(self: Text,
                     renderer: Optional[Any] = None) -> Tuple[
        float, float, str, Any, Any, Any, int, Any, Optional[str], bool, Any, ReferenceType, Union[float, Any]]: ...

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
                         s: Union[str, Any]) -> Union[
        Tuple[Union[str, Any], str], Tuple[Union[str, Any], bool], Tuple[str, bool]]: ...

    def set_fontproperties(self: Text,
                           fp: Any) -> None: ...

    def set_usetex(self: Text,
                   usetex: Optional[bool]) -> None: ...

    def get_usetex(self: Text) -> Any: ...

    def set_fontname(self: Text,
                     fontname: str) -> Any: ...


class OffsetFrom(object):
    _unit: str
    _artist: Any
    _ref_coord: tuple[float, float]

    def __init__(self: OffsetFrom,
                 artist: Any,
                 ref_coord: tuple[float, float],
                 unit: str = "points") -> None: ...

    def set_unit(self: OffsetFrom,
                 unit: str) -> None: ...

    def get_unit(self: OffsetFrom) -> str: ...

    def _get_scale(self: OffsetFrom,
                   renderer: Any) -> Union[float, Any]: ...

    def __call__(self: OffsetFrom,
                 renderer: Any) -> Transform: ...


class _AnnotationBase(object):
    xycoords: str
    xy: Union[tuple[float, float], Any]
    _draggable: None
    _annotation_clip: Optional[bool]

    def __init__(self: _AnnotationBase,
                 xy: Union[tuple[float, float], Any],
                 xycoords: str = 'data',
                 annotation_clip: Any = None) -> None: ...

    def _get_xy(self: _AnnotationBase,
                renderer: Optional[Any],
                x: Union[float, Any],
                y: Any,
                s: Any) -> Union[Union[ndarray, Iterable, int, float], Any]: ...

    def _get_xy_transform(self: _AnnotationBase,
                          renderer: Optional[Any],
                          s: Union[Union[tuple, str, {__ne__}, None], Any]) -> Union[
        Union[BlendedAffine2D, BlendedGenericTransform, BboxTransformTo, Transform, Affine2D], Any]: ...

    def _get_ref_xy(self: _AnnotationBase,
                    renderer: Optional[Any]) -> Union[Union[ndarray, Iterable, int, float], Any]: ...

    def set_annotation_clip(self: _AnnotationBase,
                            b: Optional[bool]) -> None: ...

    def get_annotation_clip(self: _AnnotationBase) -> Optional[bool]: ...

    def _get_position_xy(self: _AnnotationBase,
                         renderer: Optional[Any]) -> Union[Union[ndarray, Iterable, int, float], Any]: ...

    def _check_xy(self: _AnnotationBase,
                  renderer: Optional[Any]) -> Union[bool, Any]: ...

    def draggable(self: _AnnotationBase,
                  state: Optional[bool] = None,
                  use_blit: bool = False) -> Union[Optional[DraggableAnnotation], Any]: ...


class Annotation(Text, _AnnotationBase):
    anncoords: ClassVar[property]
    arrowprops: Any
    arrow_patch: None
    _renderer: Optional[{open_group, get_canvas_width_height, new_gc, flipy, close_group}]
    _xycoords: Any
    _arrow_relpos: Any
    _textcoords: Union[Optional[{__ne__}], Any]

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
                 event: {canvas}) -> Tuple[Any, Any]: ...

    def xycoords(self: Annotation) -> Any: ...

    def xycoords(self: Annotation,
                 xycoords: Any) -> Any: ...

    def xyann(self: Annotation) -> Tuple[int, int]: ...

    def xyann(self: Annotation,
              xytext: Any) -> None: ...

    def get_anncoords(self: Annotation) -> Union[Optional[{__ne__}], Any]: ...

    def set_anncoords(self: Annotation,
                      coords: Any) -> None: ...

    def set_figure(self: Annotation,
                   fig: Any) -> None: ...

    def update_positions(self: Annotation,
                         renderer: Optional[Any]) -> None: ...

    def draw(self: Annotation,
             renderer: Optional[{open_group, get_canvas_width_height, new_gc, flipy, close_group}]) -> Optional[
        Any]: ...

    def get_window_extent(self: Annotation,
                          renderer: Any = None) -> Bbox: ...

    def get_tightbbox(self: Annotation,
                      renderer: Any) -> Union[Bbox, Any]: ...
