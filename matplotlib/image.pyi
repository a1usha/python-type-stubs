from typing import Any
from typing import Iterable
from typing import Optional
from typing import Union
from typing import tuple

from PIL.PngImagePlugin import PngImageFile
from matplotlib.image import _ImageBase
from matplotlib.transforms import Bbox
from matplotlib.transforms import BboxBase
from matplotlib.transforms import CompositeAffine2D
from matplotlib.transforms import CompositeGenericTransform
from numpy.core._multiarray_umath import ndarray


class _ImageBase(Artist, ScalarMappable):
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

    def get_size(self: _ImageBase) -> Union[_T_co, tuple[_T_co, ...]]: ...

    def set_alpha(self: _ImageBase,
                  alpha: Any) -> Any: ...

    def _get_scalar_alpha(self: _ImageBase) -> float: ...

    def changed(self: _ImageBase) -> None: ...

    def _make_image(self: _ImageBase,
                    A: Union[ndarray, Iterable, int, float, None],
                    in_bbox: Bbox,
                    out_bbox: BboxBase,
                    clip_bbox: {xmin, xmax, ymin, ymax},
                    magnification: float = 1.0,
                    unsampled: bool = False,
                    round_to_pixel_border: bool = True) -> Any: ...

    def make_image(self: _ImageBase,
                   renderer: {new_gc, option_scale_image},
                   magnification: float = 1.0,
                   unsampled: bool = False) -> Any: ...

    def _check_unsampled_image(self: _ImageBase) -> bool: ...

    @martist.allow_rasterization
    def draw(self: _ImageBase,
             renderer: {new_gc, option_scale_image},
             *args,
             **kwargs) -> Optional[Any]: ...

    def contains(self: _ImageBase,
                 mouseevent: MouseEvent) -> Union[tuple[Any, Any], tuple[bool, dict]]: ...

    def write_png(self: _ImageBase,
                  fname: Any) -> None: ...

    def set_data(self: _ImageBase,
                 A: Union[ndarray, Iterable, int, float]) -> Any: ...

    def set_array(self: _ImageBase,
                  A: Union[ndarray, Iterable, int, float]) -> None: ...

    def get_interpolation(self: _ImageBase) -> str: ...

    def set_interpolation(self: _ImageBase,
                          s: str) -> None: ...

    def can_composite(self: _ImageBase) -> bool: ...

    def set_resample(self: _ImageBase,
                     v: Optional[bool]) -> None: ...

    def get_resample(self: _ImageBase) -> Optional[bool]: ...

    def set_filternorm(self: _ImageBase,
                       filternorm: bool) -> None: ...

    def get_filternorm(self: _ImageBase) -> bool: ...

    def set_filterrad(self: _ImageBase,
                      filterrad: Any) -> Any: ...

    def get_filterrad(self: _ImageBase) -> float: ...


class AxesImage(_ImageBase):
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
                   renderer: {new_gc, option_scale_image},
                   magnification: float = 1.0,
                   unsampled: bool = False) -> tuple[int, float, Affine2D]: ...

    def _check_unsampled_image(self: AxesImage) -> bool: ...

    def set_extent(self: AxesImage,
                   extent: Any) -> None: ...

    def get_extent(self: AxesImage) -> Union[
        Iterable, tuple, tuple[float, float, float, float], tuple[float, float, float, float]]: ...

    def get_cursor_data(self: AxesImage,
                        event: MouseEvent) -> Optional[Any]: ...

    def format_cursor_data(self: AxesImage,
                           data: {__getitem__}) -> str: ...


class NonUniformImage(AxesImage):
    def __init__(self: NonUniformImage,
                 ax: Any,
                 interpolation: str = 'nearest',
                 **kwargs) -> None: ...

    def _check_unsampled_image(self: NonUniformImage) -> bool: ...

    def make_image(self: NonUniformImage,
                   renderer: {new_gc, option_scale_image},
                   magnification: float = 1.0,
                   unsampled: bool = False) -> tuple[None, Any, Any, IdentityTransform]: ...

    def set_data(self: NonUniformImage,
                 x: int,
                 y: int,
                 A: Union[ndarray, Iterable, int, float]) -> Any: ...

    def set_array(self: NonUniformImage,
                  *args) -> Any: ...

    def set_interpolation(self: NonUniformImage,
                          s: str) -> Any: ...

    def get_extent(self: NonUniformImage) -> tuple[None, None, None, None]: ...

    def set_filternorm(self: NonUniformImage,
                       s: Any) -> None: ...

    def set_filterrad(self: NonUniformImage,
                      s: Any) -> None: ...

    def set_norm(self: NonUniformImage,
                 norm: Any) -> Any: ...

    def set_cmap(self: NonUniformImage,
                 cmap: Any) -> Any: ...


class PcolorImage(AxesImage):
    def __init__(self: PcolorImage,
                 ax: Any,
                 x: Optional[int] = None,
                 y: Optional[int] = None,
                 A: Union[ndarray, Iterable, int, float] = None,
                 cmap: Any = None,
                 norm: Any = None,
                 **kwargs) -> None: ...

    def make_image(self: PcolorImage,
                   renderer: {new_gc, option_scale_image},
                   magnification: float = 1.0,
                   unsampled: bool = False) -> tuple[None, Any, Any, IdentityTransform]: ...

    def _check_unsampled_image(self: PcolorImage) -> bool: ...

    def set_data(self: PcolorImage,
                 x: Optional[int],
                 y: Optional[int],
                 A: Union[ndarray, Iterable, int, float]) -> Any: ...

    def set_array(self: PcolorImage,
                  *args) -> Any: ...

    def get_cursor_data(self: PcolorImage,
                        event: MouseEvent) -> None: ...


class BboxImage(_ImageBase):
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
                          renderer: {new_gc, option_scale_image} = None) -> BboxBase: ...

    def contains(self: BboxImage,
                 mouseevent: MouseEvent) -> Union[tuple[Any, Any], tuple[bool, dict]]: ...

    def make_image(self: BboxImage,
                   renderer: {new_gc, option_scale_image},
                   magnification: float = 1.0,
                   unsampled: bool = False) -> tuple[int, float, Affine2D]: ...


class FigureImage(_ImageBase):
    def __init__(self: FigureImage,
                 fig: Any,
                 cmap: Any = None,
                 norm: Any = None,
                 offsetx: int = 0,
                 offsety: int = 0,
                 origin: Any = None,
                 **kwargs) -> None: ...

    def get_extent(self: FigureImage) -> tuple[float, Union[float, int], float, Union[float, int]]: ...

    def make_image(self: FigureImage,
                   renderer: {new_gc, option_scale_image},
                   magnification: float = 1.0,
                   unsampled: bool = False) -> tuple[int, float, Affine2D]: ...

    def set_data(self: FigureImage,
                 A: Union[ndarray, Iterable, int, float]) -> None: ...


def composite_images(images: Iterable,
                     renderer: Any,
                     magnification: float = 1.0) -> Any: ...


def pil_to_array(pilImage: Union[ndarray, Iterable, int, float, PngImageFile]) -> Any: ...


def thumbnail(infile: Any,
              thumbfile: Any,
              scale: float = 0.1,
              interpolation: str = 'bilinear',
              preview: bool = False) -> Any: ...


def _pil_png_to_float_array(pil_png: PngImageFile) -> Optional[ndarray]: ...


def _rgb_to_rgba(A: Union[ndarray, Iterable, int, float, None]) -> ndarray: ...


def _draw_list_compositing_images(renderer: {option_image_nocomposite},
                                  parent: Any,
                                  artists: Any,
                                  suppress_composite: Any = None) -> None: ...


def imsave(fname: Any,
           arr: Union[ndarray, Iterable, int, float],
           vmin: Optional[float] = None,
           vmax: Optional[float] = None,
           cmap: Any = None,
           format: Optional[str] = None,
           origin: str = None,
           dpi: float = 100,
           metadata: Optional[dict] = None,
           pil_kwargs: Optional[dict] = None) -> Any: ...


def imread(fname: Any,
           format: Optional[str] = None) -> Any: ...


def _resample(image_obj: _ImageBase,
              data: Union[ndarray, T, None],
              out_shape: tuple[int, int],
              transform: Union[{input_dims, output_dims}, {output_dims,
                                                           input_dims}, CompositeAffine2D, CompositeGenericTransform, _NotImplementedType],
              resample: bool = None,
              alpha: int = 1) -> ndarray: ...