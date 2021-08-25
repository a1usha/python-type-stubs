from matplotlib.transforms import TransformedBbox as TransformedBbox
from matplotlib.transforms import IdentityTransform as IdentityTransform
from matplotlib.transforms import BboxTransformTo as BboxTransformTo
from matplotlib.transforms import BboxTransform as BboxTransform
from matplotlib.transforms import Bbox as Bbox
from matplotlib.transforms import BboxBase as BboxBase
from matplotlib.transforms import Affine2D as Affine2D
from matplotlib.backend_bases import FigureCanvasBase as FigureCanvasBase
from matplotlib import _api as _api
from pathlib import Path as Path
from typing import Any
from typing import ClassVar
from typing import Iterable
from typing import Optional
from typing import Tuple
from typing import Union

from PIL.PngImagePlugin import PngImageFile
from matplotlib.artist import Artist
from matplotlib.backend_bases import MouseEvent
from matplotlib.cm import ScalarMappable
from matplotlib.image import AxesImage
from matplotlib.image import BboxImage
from matplotlib.image import FigureImage
from matplotlib.image import NonUniformImage
from matplotlib.image import PcolorImage
from matplotlib.image import _ImageBase
from matplotlib.transforms import Bbox
from matplotlib.transforms import BboxBase
from matplotlib.transforms import CompositeAffine2D
from matplotlib.transforms import CompositeGenericTransform
from numpy.core._multiarray_umath import ndarray

_log: Logger
_interpd_: dict[Union[str, Any], Union[int, Any]]
interpolations_names: set[Union[str, Any]]
from typing import Any


def composite_images(images: Iterable,
                     renderer: Any,
                     magnification: float = 1.0) -> Any: ...


def _draw_list_compositing_images(renderer: {option_image_nocomposite},
                                  parent: Any,
                                  artists: Any,
                                  suppress_composite: Any = None) -> None: ...


def _resample(image_obj: Union[_ImageBase, Any],
              data: Union[Union[ndarray, T, None], Any],
              out_shape: Union[tuple[int, int], Any],
              transform: Union[Union[{input_dims, output_dims}, {output_dims,
                                                                 input_dims}, CompositeAffine2D, CompositeGenericTransform, _NotImplementedType], Any],
              *,
              resample: Union[bool, Any] = None,
              alpha: int = 1) -> ndarray: ...


def _rgb_to_rgba(A: Union[Union[ndarray, Iterable, int, float, None], Any]) -> ndarray: ...


class _ImageBase(Artist, ScalarMappable):
    zorder: ClassVar[int]
    _imcache: None
    _interpolation: str
    _A: Union[ndarray, Iterable, int, float, None]
    _rgbacache: None
    stale: bool
    _resample: Union[Optional[bool], Any]
    _filterrad: float
    origin: Union[Optional[str], Any]
    axes: Optional[Any]
    _filternorm: bool

    def __init__(self: _ImageBase,
                 ax: Optional[Any],
                 cmap: Any = None,
                 norm: Any = None,
                 interpolation: Any = None,
                 origin: Any = None,
                 filternorm: bool = True,
                 filterrad: float = 4.0,
                 resample: bool = False,
                 **kwargs) -> None: ...

    def __getstate__(self: _ImageBase) -> dict[str, Any]: ...

    def get_size(self: _ImageBase) -> Union[_T_co, Tuple[_T_co, ...]]: ...

    def set_alpha(self: _ImageBase,
                  alpha: Any) -> Any: ...

    def _get_scalar_alpha(self: _ImageBase) -> Union[float, Any]: ...

    def changed(self: _ImageBase) -> None: ...

    def _make_image(self: _ImageBase,
                    A: Union[Union[ndarray, Iterable, int, float, None], Any],
                    in_bbox: Union[Bbox, Any],
                    out_bbox: Union[BboxBase, Any],
                    clip_bbox: {xmin, xmax, ymin, ymax},
                    magnification: float = 1.0,
                    unsampled: bool = False,
                    round_to_pixel_border: bool = True) -> Any: ...

    def make_image(self: _ImageBase,
                   renderer: Union[{new_gc, option_scale_image}, Any],
                   magnification: float = 1.0,
                   unsampled: bool = False) -> Any: ...

    def _check_unsampled_image(self: _ImageBase) -> bool: ...

    def draw(self: _ImageBase,
             renderer: {new_gc, option_scale_image},
             *args,
             **kwargs) -> Optional[Any]: ...

    def contains(self: _ImageBase,
                 mouseevent: MouseEvent) -> Union[Tuple[Any, Any], Tuple[bool, dict[Any, Any]]]: ...

    def write_png(self: _ImageBase,
                  fname: Any) -> None: ...

    def set_data(self: _ImageBase,
                 A: Union[Union[ndarray, Iterable, int, float], Any]) -> Any: ...

    def set_array(self: _ImageBase,
                  A: Union[ndarray, Iterable, int, float]) -> None: ...

    def get_interpolation(self: _ImageBase) -> str: ...

    def set_interpolation(self: _ImageBase,
                          s: str) -> None: ...

    def can_composite(self: _ImageBase) -> bool: ...

    def set_resample(self: _ImageBase,
                     v: Optional[bool]) -> None: ...

    def get_resample(self: _ImageBase) -> Union[Optional[bool], Any]: ...

    def set_filternorm(self: _ImageBase,
                       filternorm: bool) -> None: ...

    def get_filternorm(self: _ImageBase) -> bool: ...

    def set_filterrad(self: _ImageBase,
                      filterrad: Any) -> Any: ...

    def get_filterrad(self: _ImageBase) -> float: ...


class AxesImage(_ImageBase):
    _extent: Union[Iterable, tuple, None]
    stale: bool

    def __str__(self: AxesImage) -> str: ...

    def __init__(self: AxesImage,
                 ax: Any,
                 cmap: Any = None,
                 norm: Any = None,
                 interpolation: str = None,
                 origin: str = None,
                 extent: Union[Iterable, tuple, None] = None,
                 filternorm: bool = True,
                 filterrad: Any = 4.0,
                 resample: bool = False,
                 **kwargs) -> None: ...

    def get_window_extent(self: AxesImage,
                          renderer: Any = None) -> Bbox: ...

    def make_image(self: AxesImage,
                   renderer: Union[{new_gc, option_scale_image}, Any],
                   magnification: float = 1.0,
                   unsampled: bool = False) -> Tuple[int, float, Affine2D]: ...

    def _check_unsampled_image(self: AxesImage) -> bool: ...

    def set_extent(self: AxesImage,
                   extent: Any) -> None: ...

    def get_extent(self: AxesImage) -> Union[
        Iterable, Tuple, Tuple[float, Union[float, Any], Union[float, Any], float], Tuple[
            float, Union[float, Any], float, Union[float, Any]]]: ...

    def get_cursor_data(self: AxesImage,
                        event: MouseEvent) -> Optional[Any]: ...

    def format_cursor_data(self: AxesImage,
                           data: {__getitem__}) -> Union[str, Any]: ...


class NonUniformImage(AxesImage):
    mouseover: ClassVar[bool]
    is_grayscale: ClassVar[deprecate_privatize_attribute]
    _imcache: None
    _A: Union[None, ndarray, Iterable, int, float]
    _is_grayscale: Any
    stale: bool
    _Ay: ndarray
    _Ax: ndarray

    def __init__(self: NonUniformImage,
                 ax: Any,
                 *,
                 interpolation: str = 'nearest',
                 **kwargs) -> None: ...

    def _check_unsampled_image(self: NonUniformImage) -> bool: ...

    def make_image(self: NonUniformImage,
                   renderer: Union[{new_gc, option_scale_image}, Any],
                   magnification: float = 1.0,
                   unsampled: bool = False) -> Tuple[None, Any, Any, IdentityTransform]: ...

    def set_data(self: NonUniformImage,
                 x: int,
                 y: int,
                 A: Union[ndarray, Iterable, int, float]) -> Any: ...

    def set_array(self: NonUniformImage,
                  *args) -> Any: ...

    def set_interpolation(self: NonUniformImage,
                          s: str) -> Any: ...

    def get_extent(self: NonUniformImage) -> Tuple[None, None, None, None]: ...

    def set_filternorm(self: NonUniformImage,
                       s: Any) -> None: ...

    def set_filterrad(self: NonUniformImage,
                      s: Any) -> None: ...

    def set_norm(self: NonUniformImage,
                 norm: Any) -> Any: ...

    def set_cmap(self: NonUniformImage,
                 cmap: Any) -> Any: ...


class PcolorImage(AxesImage):
    is_grayscale: ClassVar[deprecate_privatize_attribute]
    _A: Union[Union[None, ndarray, Iterable, int, float], Any]
    _rgbacache: Union[Union[ndarray, {ndim}, None], Any]
    _is_grayscale: Any
    stale: bool
    _Ay: Union[Optional[ndarray], Any]
    _Ax: Union[Optional[ndarray], Any]

    def __init__(self: PcolorImage,
                 ax: Any,
                 x: Optional[int] = None,
                 y: Optional[int] = None,
                 A: Union[ndarray, Iterable, int, float] = None,
                 cmap: Any = None,
                 norm: Any = None,
                 **kwargs) -> None: ...

    def make_image(self: PcolorImage,
                   renderer: Union[{new_gc, option_scale_image}, Any],
                   magnification: float = 1.0,
                   unsampled: bool = False) -> Tuple[None, Any, Any, IdentityTransform]: ...

    def _check_unsampled_image(self: PcolorImage) -> bool: ...

    def set_data(self: PcolorImage,
                 x: Optional[int],
                 y: Optional[int],
                 A: Union[ndarray, Iterable, int, float]) -> Any: ...

    def set_array(self: PcolorImage,
                  *args) -> Any: ...

    def get_cursor_data(self: PcolorImage,
                        event: MouseEvent) -> None: ...


class FigureImage(_ImageBase):
    zorder: ClassVar[int]
    _interpolation: ClassVar[str]
    figure: Any
    magnification: float
    stale: bool
    ox: int
    oy: int

    def __init__(self: FigureImage,
                 fig: Any,
                 cmap: Any = None,
                 norm: Any = None,
                 offsetx: int = 0,
                 offsety: int = 0,
                 origin: Any = None,
                 **kwargs) -> None: ...

    def get_extent(self: FigureImage) -> Tuple[
        float, Union[Union[float, int], Any], float, Union[Union[float, int], Any]]: ...

    def make_image(self: FigureImage,
                   renderer: Union[{new_gc, option_scale_image}, Any],
                   magnification: float = 1.0,
                   unsampled: bool = False) -> Tuple[int, float, Affine2D]: ...

    def set_data(self: FigureImage,
                 A: Union[Union[ndarray, Iterable, int, float], Any]) -> None: ...


class BboxImage(_ImageBase):
    _transform: BboxTransformTo
    bbox: Any

    def __init__(self: BboxImage,
                 bbox: Any,
                 cmap: Any = None,
                 norm: Any = None,
                 interpolation: Any = None,
                 origin: Any = None,
                 filternorm: bool = True,
                 filterrad: float = 4.0,
                 resample: bool = False,
                 **kwargs) -> None: ...

    def get_window_extent(self: BboxImage,
                          renderer: Union[{new_gc, option_scale_image}, Any] = None) -> Union[BboxBase, Any]: ...

    def contains(self: BboxImage,
                 mouseevent: MouseEvent) -> Union[Tuple[Any, Any], Tuple[bool, dict[Any, Any]]]: ...

    def make_image(self: BboxImage,
                   renderer: Union[{new_gc, option_scale_image}, Any],
                   magnification: float = 1.0,
                   unsampled: bool = False) -> Tuple[int, float, Affine2D]: ...


def imread(fname: Any,
           format: Optional[str] = None) -> Any: ...


def imsave(fname: Any,
           arr: Union[ndarray, Iterable, int, float],
           vmin: Optional[float] = None,
           vmax: Optional[float] = None,
           cmap: Any = None,
           format: Optional[str] = None,
           origin: str = None,
           dpi: float = 100,
           *,
           metadata: Optional[dict] = None,
           pil_kwargs: Optional[dict] = None) -> Any: ...


def pil_to_array(pilImage: Union[Union[ndarray, Iterable, int, float, PngImageFile], Any]) -> Any: ...


def _pil_png_to_float_array(pil_png: Union[PngImageFile, Any]) -> Optional[ndarray]: ...


def thumbnail(infile: Any,
              thumbfile: Any,
              scale: float = 0.1,
              interpolation: str = 'bilinear',
              preview: bool = False) -> Any: ...