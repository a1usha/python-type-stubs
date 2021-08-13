from typing import Any
from typing import Optional
from typing import Union
from typing import tuple

from matplotlib.transforms import Bbox
from matplotlib.transforms import Transform


class DrawingArea(OffsetBox):
    def __init__(self: DrawingArea,
                 width: float,
                 height: float,
                 xdescent: float = 0.,
                 ydescent: float = 0.,
                 clip: bool = False) -> None: ...

    @property
    def clip_children(self: DrawingArea) -> bool: ...

    @clip_children.setter
    def clip_children(self: DrawingArea,
                      val: Any) -> None: ...

    def get_transform(self: DrawingArea) -> Union[{input_dims, output_dims}, {output_dims,
                                                                              input_dims}, CompositeAffine2D, CompositeGenericTransform, _NotImplementedType]: ...

    def set_transform(self: DrawingArea,
                      t: Any) -> None: ...

    def set_offset(self: DrawingArea,
                   xy: tuple[float, float]) -> None: ...

    def get_offset(self: DrawingArea) -> tuple[float, float]: ...

    def get_window_extent(self: DrawingArea,
                          renderer: Optional[Any]) -> Bbox: ...

    def get_extent(self: DrawingArea,
                   renderer: Optional[Any]) -> tuple[float, float, float, float]: ...

    def add_artist(self: DrawingArea,
                   a: {is_transform_set}) -> None: ...

    def draw(self: DrawingArea,
             renderer: Optional[Any]) -> None: ...


class AnchoredOffsetbox(OffsetBox):
    def __init__(self: AnchoredOffsetbox,
                 loc: str,
                 pad: float = 0.4,
                 borderpad: float = 0.5,
                 child: Any = None,
                 prop: Any = None,
                 frameon: bool = True,
                 bbox_to_anchor: Any = None,
                 bbox_transform: Optional[Transform] = None,
                 **kwargs) -> None: ...

    def set_child(self: AnchoredOffsetbox,
                  child: Any) -> None: ...

    def get_child(self: AnchoredOffsetbox) -> Any: ...

    def get_children(self: AnchoredOffsetbox) -> list: ...

    def get_extent(self: AnchoredOffsetbox,
                   renderer: Optional[Any]) -> tuple[Union[int, float], Union[int, float], float, float]: ...

    def get_bbox_to_anchor(self: AnchoredOffsetbox) -> Union[BboxBase, TransformedBbox]: ...

    def set_bbox_to_anchor(self: AnchoredOffsetbox,
                           bbox: Any,
                           transform: Any = None) -> Any: ...

    def get_window_extent(self: AnchoredOffsetbox,
                          renderer: Optional[Any]) -> Bbox: ...

    def _update_offset_func(self: AnchoredOffsetbox,
                            renderer: Optional[Any],
                            fontsize: Any = None) -> None: ...

    def update_frame(self: AnchoredOffsetbox,
                     bbox: Bbox,
                     fontsize: Any = None) -> None: ...

    def draw(self: AnchoredOffsetbox,
             renderer: Optional[Any]) -> None: ...

    def _get_anchored_bbox(self: AnchoredOffsetbox,
                           loc: Any,
                           bbox: Bbox,
                           parentbbox: {padded},
                           borderpad: {__neg__}) -> tuple[Any, Any]: ...


class AuxTransformBox(OffsetBox):
    def __init__(self: AuxTransformBox,
                 aux_transform: Any) -> None: ...

    def add_artist(self: AuxTransformBox,
                   a: {set_transform}) -> None: ...

    def get_transform(self: AuxTransformBox) -> Any: ...

    def set_transform(self: AuxTransformBox,
                      t: Any) -> None: ...

    def set_offset(self: AuxTransformBox,
                   xy: tuple[float, float]) -> None: ...

    def get_offset(self: AuxTransformBox) -> tuple[float, float]: ...

    def get_window_extent(self: AuxTransformBox,
                          renderer: Optional[Any]) -> Bbox: ...

    def get_extent(self: AuxTransformBox,
                   renderer: Optional[Any]) -> tuple[Any, Any, float, float]: ...

    def draw(self: AuxTransformBox,
             renderer: Optional[Any]) -> None: ...


class HPacker(PackerBase):
    def get_extent_offsets(self: HPacker,
                           renderer: {points_to_pixels}) -> Union[
        tuple[Union[int, float], Union[int, float], float, float, list], tuple[
            float, Union[int, float], float, float, list[tuple[Any, Any]]]]: ...


class DraggableAnnotation(DraggableBase):
    def __init__(self: DraggableAnnotation,
                 annotation: {pickable},
                 use_blit: bool = False) -> None: ...

    def save_offset(self: DraggableAnnotation) -> None: ...

    def update_offset(self: DraggableAnnotation,
                      dx: Any,
                      dy: Any) -> None: ...


class VPacker(PackerBase):
    def get_extent_offsets(self: VPacker,
                           renderer: {points_to_pixels}) -> tuple[
        Union[int, float], float, float, float, list[tuple[Any, Any]]]: ...


class PackerBase(OffsetBox):
    def __init__(self: PackerBase,
                 pad: Optional[float] = None,
                 sep: Optional[float] = None,
                 width: Optional[float] = None,
                 height: Optional[float] = None,
                 align: str = "baseline",
                 mode: str = "fixed",
                 children: Any = None) -> None: ...


class OffsetBox(Artist):
    def __init__(self: OffsetBox,
                 *args,
                 **kwargs) -> None: ...

    def set_figure(self: OffsetBox,
                   fig: Any) -> None: ...

    @martist.Artist.axes.setter
    def axes(self: OffsetBox,
             ax: Any) -> Optional[Any]: ...

    def contains(self: OffsetBox,
                 mouseevent: MouseEvent) -> bool: ...

    def set_offset(self: OffsetBox,
                   xy: tuple[float, float]) -> None: ...

    def get_offset(self: OffsetBox,
                   width: Union[int, float],
                   height: Union[int, float],
                   xdescent: float,
                   ydescent: float,
                   renderer: Any) -> tuple[int, int]: ...

    def set_width(self: OffsetBox,
                  width: float) -> None: ...

    def set_height(self: OffsetBox,
                   height: float) -> None: ...

    def get_visible_children(self: OffsetBox) -> list: ...

    def get_children(self: OffsetBox) -> list: ...

    def get_extent_offsets(self: OffsetBox,
                           renderer: Any) -> Any: ...

    def get_extent(self: OffsetBox,
                   renderer: Optional[Any]) -> tuple[Any, Any, Any, Any]: ...

    def get_window_extent(self: OffsetBox,
                          renderer: Optional[Any]) -> Bbox: ...

    def draw(self: OffsetBox,
             renderer: Optional[Any]) -> None: ...


class PaddedBox(OffsetBox):
    def __init__(self: PaddedBox,
                 child: Any,
                 pad: float = None,
                 draw_frame: bool = False,
                 patch_attrs: Optional[dict] = None) -> None: ...

    def get_extent_offsets(self: PaddedBox,
                           renderer: Optional[Any]) -> tuple[
        Union[int, float], Union[int, float], float, float, list[tuple[int, int]]]: ...

    def draw(self: PaddedBox,
             renderer: Optional[Any]) -> None: ...

    def update_frame(self: PaddedBox,
                     bbox: Bbox,
                     fontsize: Any = None) -> None: ...

    def draw_frame(self: PaddedBox,
                   renderer: Optional[Any]) -> None: ...


class AnnotationBbox(Artist, _AnnotationBase):
    def __str__(self: AnnotationBbox) -> str: ...

    @docstring.dedent_interpd
    def __init__(self: AnnotationBbox,
                 offsetbox: OffsetBox,
                 xy: tuple[float, float],
                 xybox: Any = None,
                 xycoords: Any = 'data',
                 boxcoords: Any = None,
                 frameon: bool = True,
                 pad: float = 0.4,
                 annotation_clip: Any = None,
                 box_alignment: tuple[float, float] = (0.5, 0.5),
                 bboxprops: Any = None,
                 arrowprops: Any = None,
                 fontsize: Any = None,
                 **kwargs) -> Optional[Any]: ...

    @property
    def xyann(self: AnnotationBbox) -> Any: ...

    @xyann.setter
    def xyann(self: AnnotationBbox,
              xyann: Any) -> None: ...

    @property
    def anncoords(self: AnnotationBbox) -> Any: ...

    @anncoords.setter
    def anncoords(self: AnnotationBbox,
                  coords: Any) -> None: ...

    def contains(self: AnnotationBbox,
                 mouseevent: MouseEvent) -> Union[tuple[Any, Any], tuple[bool, dict], tuple[bool, dict]]: ...

    def get_children(self: AnnotationBbox) -> list[Union[OffsetBox, FancyBboxPatch]]: ...

    def set_figure(self: AnnotationBbox,
                   fig: Any) -> None: ...

    def set_fontsize(self: AnnotationBbox,
                     s: Any = None) -> None: ...

    @_api.delete_parameter
    def get_fontsize(self: AnnotationBbox,
                     s: Any = None) -> Optional[Any]: ...

    def get_window_extent(self: AnnotationBbox,
                          renderer: Any) -> Bbox: ...

    def get_tightbbox(self: AnnotationBbox,
                      renderer: Any) -> Bbox: ...

    def update_positions(self: AnnotationBbox,
                         renderer: {points_to_pixels}) -> None: ...

    def _update_position_xybox(self: AnnotationBbox,
                               renderer: Any,
                               xy_pixel: Any) -> None: ...

    def draw(self: AnnotationBbox,
             renderer: Optional[{points_to_pixels, get_rasterized, get_agg_filter, figure}]) -> None: ...


class DraggableOffsetBox(DraggableBase):
    def __init__(self: DraggableOffsetBox,
                 ref_artist: {pickable},
                 offsetbox: Any,
                 use_blit: bool = False) -> None: ...

    def save_offset(self: DraggableOffsetBox) -> None: ...

    def update_offset(self: DraggableOffsetBox,
                      dx: Any,
                      dy: Any) -> None: ...

    def get_loc_in_canvas(self: DraggableOffsetBox) -> tuple[Any, Any]: ...


class AnchoredText(AnchoredOffsetbox):
    def __init__(self: AnchoredText,
                 s: str,
                 loc: str,
                 pad: float = 0.4,
                 borderpad: float = 0.5,
                 prop: Optional[dict] = None,
                 **kwargs) -> Any: ...


class DraggableBase(object):
    def __init__(self: DraggableBase,
                 ref_artist: {pickable},
                 use_blit: bool = False) -> None: ...

    def on_motion(self: DraggableBase,
                  evt: Any) -> None: ...

    @_api.deprecated
    def on_motion_blit(self: DraggableBase,
                       evt: Any) -> Optional[Any]: ...

    def on_pick(self: DraggableBase,
                evt: {artist}) -> None: ...

    def on_release(self: DraggableBase,
                   event: Any) -> None: ...

    def _check_still_parented(self: DraggableBase) -> bool: ...

    def disconnect(self: DraggableBase) -> None: ...

    @_api.deprecated
    def artist_picker(self: DraggableBase,
                      artist: Any,
                      evt: Any) -> Any: ...

    def save_offset(self: DraggableBase) -> None: ...

    def update_offset(self: DraggableBase,
                      dx: Any,
                      dy: Any) -> None: ...

    def finalize_offset(self: DraggableBase) -> None: ...


class OffsetImage(OffsetBox):
    def __init__(self: OffsetImage,
                 arr: Any,
                 zoom: int = 1,
                 cmap: Any = None,
                 norm: Any = None,
                 interpolation: Any = None,
                 origin: Any = None,
                 filternorm: bool = True,
                 filterrad: float = 4.0,
                 resample: bool = False,
                 dpi_cor: bool = True,
                 **kwargs) -> None: ...

    def set_data(self: OffsetImage,
                 arr: Any) -> None: ...

    def get_data(self: OffsetImage) -> ndarray: ...

    def set_zoom(self: OffsetImage,
                 zoom: int) -> None: ...

    def get_zoom(self: OffsetImage) -> int: ...

    def get_offset(self: OffsetImage) -> tuple[int, int]: ...

    def get_children(self: OffsetImage) -> list[BboxImage]: ...

    def get_window_extent(self: OffsetImage,
                          renderer: Optional[Any]) -> Bbox: ...

    def get_extent(self: OffsetImage,
                   renderer: Optional[Any]) -> tuple[Union[float, int], Union[float, int], int, int]: ...

    def draw(self: OffsetImage,
             renderer: Optional[Any]) -> None: ...


class TextArea(OffsetBox):
    @_api.delete_parameter
    def __init__(self: TextArea,
                 s: str,
                 textprops: dict = None,
                 multilinebaseline: bool = False,
                 minimumdescent: bool = True) -> Optional[Any]: ...

    def set_text(self: TextArea,
                 s: Any) -> None: ...

    def get_text(self: TextArea) -> str: ...

    def set_multilinebaseline(self: TextArea,
                              t: Any) -> None: ...

    def get_multilinebaseline(self: TextArea) -> bool: ...

    @_api.deprecated
    def set_minimumdescent(self: TextArea,
                           t: Any) -> Optional[Any]: ...

    @_api.deprecated
    def get_minimumdescent(self: TextArea) -> bool: ...

    def set_transform(self: TextArea,
                      t: Any) -> None: ...

    def set_offset(self: TextArea,
                   xy: tuple[float, float]) -> None: ...

    def get_offset(self: TextArea) -> tuple[float, float]: ...

    def get_window_extent(self: TextArea,
                          renderer: Optional[Any]) -> Bbox: ...

    def get_extent(self: TextArea,
                   renderer: Optional[Any]) -> tuple[Any, int, Union[float, int], Union[float, int]]: ...

    def draw(self: TextArea,
             renderer: Optional[Any]) -> None: ...


def _get_aligned_offsets(hd_list: list[tuple[Any, Any]],
                         height: Optional[float],
                         align: str = "baseline") -> Any: ...


def _get_packed_offsets(wd_list: list[tuple[float, float]],
                        total: Optional[float],
                        sep: float,
                        mode: str = "fixed") -> float: ...


def bbox_artist(*args,
                ,
                **kwargs) -> None: ...