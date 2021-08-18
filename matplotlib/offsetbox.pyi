from typing import Optional
from typing import Tuple
from typing import Union

from matplotlib import _api
from matplotlib.artist import Artist
from matplotlib.backend_bases import MouseEvent
from matplotlib.offsetbox import AnchoredOffsetbox
from matplotlib.offsetbox import AnchoredText
from matplotlib.offsetbox import AnnotationBbox
from matplotlib.offsetbox import AuxTransformBox
from matplotlib.offsetbox import DraggableAnnotation
from matplotlib.offsetbox import DraggableBase
from matplotlib.offsetbox import DraggableOffsetBox
from matplotlib.offsetbox import DrawingArea
from matplotlib.offsetbox import HPacker
from matplotlib.offsetbox import OffsetBox
from matplotlib.offsetbox import OffsetImage
from matplotlib.offsetbox import PackerBase
from matplotlib.offsetbox import PaddedBox
from matplotlib.offsetbox import TextArea
from matplotlib.offsetbox import VPacker
from matplotlib.text import _AnnotationBase
from matplotlib.transforms import Bbox
from matplotlib.transforms import BboxBase
from matplotlib.transforms import CompositeAffine2D
from matplotlib.transforms import CompositeGenericTransform
from matplotlib.transforms import Transform
from matplotlib.transforms import TransformedBbox
from numpy.core._multiarray_umath import ndarray
from object import object


def bbox_artist(*args,
                **kwargs) -> None: ...


def _get_packed_offsets(wd_list: list[tuple[float, float]],
                        total: Optional[float],
                        sep: float,
                        mode: str = "fixed") -> float: ...


def _get_aligned_offsets(hd_list: list[tuple[Any, Any]],
                         height: Optional[float],
                         align: str = "baseline") -> Any: ...


class OffsetBox(Artist):
    def __init__(self: OffsetBox,
                 *args,
                 **kwargs) -> None: ...

    def set_figure(self: OffsetBox,
                   fig: Any) -> None: ...

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
                   renderer: Any) -> Tuple[int, int]: ...

    def set_width(self: OffsetBox,
                  width: float) -> None: ...

    def set_height(self: OffsetBox,
                   height: float) -> None: ...

    def get_visible_children(self: OffsetBox) -> list: ...

    def get_children(self: OffsetBox) -> list: ...

    def get_extent_offsets(self: OffsetBox,
                           renderer: Any) -> Any: ...

    def get_extent(self: OffsetBox,
                   renderer: Optional[Any]) -> Tuple[Any, Any, Any, Any]: ...

    def get_window_extent(self: OffsetBox,
                          renderer: Optional[Any]) -> Bbox: ...

    def draw(self: OffsetBox,
             renderer: Optional[Any]) -> None: ...


class PackerBase(OffsetBox):
    def __init__(self: PackerBase,
                 pad: Optional[float] = None,
                 sep: Optional[float] = None,
                 width: Optional[float] = None,
                 height: Optional[float] = None,
                 align: str = "baseline",
                 mode: str = "fixed",
                 children: Any = None) -> None: ...


class VPacker(PackerBase):
    def get_extent_offsets(self: VPacker,
                           renderer: {points_to_pixels}) -> Tuple[
        Union[int, float], float, float, float, list[Tuple[Any, Any]]]: ...


class HPacker(PackerBase):
    def get_extent_offsets(self: HPacker,
                           renderer: {points_to_pixels}) -> Union[
        Tuple[Union[int, float], Union[int, float], float, float, list], Tuple[
            float, Union[int, float], float, float, list[Tuple[Any, Any]]]]: ...


class PaddedBox(OffsetBox):
    def __init__(self: PaddedBox,
                 child: Any,
                 pad: float = None,
                 draw_frame: bool = False,
                 patch_attrs: Optional[dict] = None) -> None: ...

    def get_extent_offsets(self: PaddedBox,
                           renderer: Optional[Any]) -> Tuple[
        Union[int, float], Union[int, float], float, float, list[Tuple[int, int]]]: ...

    def draw(self: PaddedBox,
             renderer: Optional[Any]) -> None: ...

    def update_frame(self: PaddedBox,
                     bbox: Bbox,
                     fontsize: Any = None) -> None: ...

    def draw_frame(self: PaddedBox,
                   renderer: Optional[Any]) -> None: ...


class DrawingArea(OffsetBox):
    def __init__(self: DrawingArea,
                 width: float,
                 height: float,
                 xdescent: float = 0.,
                 ydescent: float = 0.,
                 clip: bool = False) -> None: ...

    def clip_children(self: DrawingArea) -> bool: ...

    def clip_children(self: DrawingArea,
                      val: Any) -> None: ...

    def get_transform(self: DrawingArea) -> Union[{input_dims, output_dims}, {output_dims,
                                                                              input_dims}, CompositeAffine2D, CompositeGenericTransform, _NotImplementedType]: ...

    def set_transform(self: DrawingArea,
                      t: Any) -> None: ...

    def set_offset(self: DrawingArea,
                   xy: tuple[float, float]) -> None: ...

    def get_offset(self: DrawingArea) -> Tuple[float, float]: ...

    def get_window_extent(self: DrawingArea,
                          renderer: Optional[Any]) -> Bbox: ...

    def get_extent(self: DrawingArea,
                   renderer: Optional[Any]) -> Tuple[float, float, float, float]: ...

    def add_artist(self: DrawingArea,
                   a: {is_transform_set}) -> None: ...

    def draw(self: DrawingArea,
             renderer: Optional[Any]) -> None: ...


class TextArea(OffsetBox):
    @_api.delete_parameter("3.4", "minimumdescent")
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

    @_api.deprecated("3.4")
    def set_minimumdescent(self: TextArea,
                           t: Any) -> Optional[Any]: ...

    @_api.deprecated("3.4")
    def get_minimumdescent(self: TextArea) -> bool: ...

    def set_transform(self: TextArea,
                      t: Any) -> None: ...

    def set_offset(self: TextArea,
                   xy: tuple[float, float]) -> None: ...

    def get_offset(self: TextArea) -> Tuple[float, float]: ...

    def get_window_extent(self: TextArea,
                          renderer: Optional[Any]) -> Bbox: ...

    def get_extent(self: TextArea,
                   renderer: Optional[Any]) -> Tuple[Any, int, Union[float, int], Union[float, int]]: ...

    def draw(self: TextArea,
             renderer: Optional[Any]) -> None: ...


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

    def get_offset(self: AuxTransformBox) -> Tuple[float, float]: ...

    def get_window_extent(self: AuxTransformBox,
                          renderer: Optional[Any]) -> Bbox: ...

    def get_extent(self: AuxTransformBox,
                   renderer: Optional[Any]) -> Tuple[Any, Any, float, float]: ...

    def draw(self: AuxTransformBox,
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
                   renderer: Optional[Any]) -> Tuple[Union[int, float], Union[int, float], float, float]: ...

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
                           borderpad: {__neg__}) -> Tuple[Any, Any]: ...


class AnchoredText(AnchoredOffsetbox):
    def __init__(self: AnchoredText,
                 s: str,
                 loc: str,
                 pad: float = 0.4,
                 borderpad: float = 0.5,
                 prop: Optional[dict] = None,
                 **kwargs) -> Any: ...


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

    def get_offset(self: OffsetImage) -> Tuple[int, int]: ...

    def get_children(self: OffsetImage) -> list[BboxImage]: ...

    def get_window_extent(self: OffsetImage,
                          renderer: Optional[Any]) -> Bbox: ...

    def get_extent(self: OffsetImage,
                   renderer: Optional[Any]) -> Tuple[Union[float, int], Union[float, int], int, int]: ...

    def draw(self: OffsetImage,
             renderer: Optional[Any]) -> None: ...


class AnnotationBbox(Artist, _AnnotationBase):
    def __str__(self: AnnotationBbox) -> str: ...

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

    def xyann(self: AnnotationBbox) -> Any: ...

    def xyann(self: AnnotationBbox,
              xyann: Any) -> None: ...

    def anncoords(self: AnnotationBbox) -> Any: ...

    def anncoords(self: AnnotationBbox,
                  coords: Any) -> None: ...

    def contains(self: AnnotationBbox,
                 mouseevent: MouseEvent) -> Union[Tuple[Any, Any], Tuple[bool, dict], Tuple[bool, dict]]: ...

    def get_children(self: AnnotationBbox) -> list[Union[OffsetBox, FancyBboxPatch]]: ...

    def set_figure(self: AnnotationBbox,
                   fig: Any) -> None: ...

    def set_fontsize(self: AnnotationBbox,
                     s: Any = None) -> None: ...

    @_api.delete_parameter("3.3", "s")
    def get_fontsize(self: AnnotationBbox,
                     s: Any = None) -> Optional[Any]: ...

    def get_window_extent(self: AnnotationBbox,
                          renderer: Any) -> Bbox: ...

    def get_tightbbox(self: AnnotationBbox,
                      renderer: Any) -> Bbox: ...

    def update_positions(self: AnnotationBbox,
                         renderer: Optional[Any]) -> None: ...

    def _update_position_xybox(self: AnnotationBbox,
                               renderer: Optional[Any],
                               xy_pixel: Any) -> None: ...

    def draw(self: AnnotationBbox,
             renderer: Optional[{points_to_pixels, get_rasterized, get_agg_filter, figure}]) -> None: ...


class DraggableBase(object):
    def __init__(self: DraggableBase,
                 ref_artist: {pickable},
                 use_blit: bool = False) -> None: ...

    def on_motion(self: DraggableBase,
                  evt: Any) -> None: ...

    @_api.deprecated("3.3", alternative="self.on_motion")
    def on_motion_blit(self: DraggableBase,
                       evt: Any) -> Optional[Any]: ...

    def on_pick(self: DraggableBase,
                evt: {artist}) -> None: ...

    def on_release(self: DraggableBase,
                   event: Any) -> None: ...

    def _check_still_parented(self: DraggableBase) -> bool: ...

    def disconnect(self: DraggableBase) -> None: ...

    @_api.deprecated("3.3", alternative="self.ref_artist.contains")
    def artist_picker(self: DraggableBase,
                      artist: Any,
                      evt: Any) -> Any: ...

    def save_offset(self: DraggableBase) -> None: ...

    def update_offset(self: DraggableBase,
                      dx: Any,
                      dy: Any) -> None: ...

    def finalize_offset(self: DraggableBase) -> None: ...


class DraggableOffsetBox(DraggableBase):
    def __init__(self: DraggableOffsetBox,
                 ref_artist: {pickable},
                 offsetbox: Any,
                 use_blit: bool = False) -> None: ...

    def save_offset(self: DraggableOffsetBox) -> None: ...

    def update_offset(self: DraggableOffsetBox,
                      dx: Any,
                      dy: Any) -> None: ...

    def get_loc_in_canvas(self: DraggableOffsetBox) -> Tuple[Any, Any]: ...


class DraggableAnnotation(DraggableBase):
    def __init__(self: DraggableAnnotation,
                 annotation: {pickable},
                 use_blit: bool = False) -> None: ...

    def save_offset(self: DraggableAnnotation) -> None: ...

    def update_offset(self: DraggableAnnotation,
                      dx: Any,
                      dy: Any) -> None: ...
