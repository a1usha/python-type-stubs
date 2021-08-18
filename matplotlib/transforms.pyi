from _typeshed import SupportsLessThan
from typing import Generator
from typing import Iterable
from typing import Optional
from typing import Tuple
from typing import Type
from typing import Union

from matplotlib import _api
from matplotlib.path import Path
from matplotlib.transforms import Affine2D
from matplotlib.transforms import Affine2DBase
from matplotlib.transforms import AffineBase
from matplotlib.transforms import AffineDeltaTransform
from matplotlib.transforms import Bbox
from matplotlib.transforms import BboxBase
from matplotlib.transforms import BboxTransform
from matplotlib.transforms import BboxTransformFrom
from matplotlib.transforms import BboxTransformTo
from matplotlib.transforms import BboxTransformToMaxOnly
from matplotlib.transforms import BlendedAffine2D
from matplotlib.transforms import BlendedGenericTransform
from matplotlib.transforms import CompositeAffine2D
from matplotlib.transforms import CompositeGenericTransform
from matplotlib.transforms import IdentityTransform
from matplotlib.transforms import LockableBbox
from matplotlib.transforms import ScaledTranslation
from matplotlib.transforms import Transform
from matplotlib.transforms import TransformNode
from matplotlib.transforms import TransformWrapper
from matplotlib.transforms import TransformedBbox
from matplotlib.transforms import TransformedPatchPath
from matplotlib.transforms import TransformedPath
from matplotlib.transforms import _BlendedMixin
from numpy.core._multiarray_umath import ndarray
from numpy.ma.core import MaskedArray
from object import object


def _make_str_method(*args,
                     **kwargs) -> (self: Any) ->


class TransformNode(object):
    def __init__(self: TransformNode,
                 shorthand_name: str = None) -> None: ...

    def __str__(self: TransformNode) -> str: ...

    def __getstate__(self: TransformNode) -> dict[str, dict]: ...

    def __setstate__(self: TransformNode,
                     data_dict: Any) -> None: ...

    def __copy__(self: TransformNode) -> object: ...

    def __deepcopy__(self: TransformNode,
                     memo: Any) -> Union[TransformNode, object]: ...

    def invalidate(self: TransformNode) -> None: ...

    def _invalidate_internal(self: TransformNode,
                             value: Union[int, {__eq__}],
                             invalidating_node: Any) -> None: ...

    def set_children(self: TransformNode,
                     *args) -> None: ...

    def frozen(self: TransformNode) -> TransformNode: ...


class BboxBase(TransformNode):
    def _check(points: ndarray) -> None: ...

    def frozen(self: BboxBase) -> Bbox: ...

    def __array__(self: BboxBase,
                  *args,
                  **kwargs) -> Any: ...

    def x0(self: BboxBase) -> Any: ...

    def y0(self: BboxBase) -> Any: ...

    def x1(self: BboxBase) -> Any: ...

    def y1(self: BboxBase) -> Any: ...

    def p0(self: BboxBase) -> Any: ...

    def p1(self: BboxBase) -> Any: ...

    def xmin(self: BboxBase) -> Union[ndarray, int, float, complex]: ...

    def ymin(self: BboxBase) -> Union[ndarray, int, float, complex]: ...

    def xmax(self: BboxBase) -> Union[ndarray, int, float, complex]: ...

    def ymax(self: BboxBase) -> Union[ndarray, int, float, complex]: ...

    def min(self: BboxBase) -> Union[ndarray, int, float, complex]: ...

    def max(self: BboxBase) -> Union[ndarray, int, float, complex]: ...

    def intervalx(self: BboxBase) -> Any: ...

    def intervaly(self: BboxBase) -> Any: ...

    def width(self: BboxBase) -> Any: ...

    def height(self: BboxBase) -> Any: ...

    def size(self: BboxBase) -> Any: ...

    def bounds(self: BboxBase) -> Tuple[Any, Any, Any, Any]: ...

    def extents(self: BboxBase) -> Any: ...

    def get_points(self: BboxBase) -> Any: ...

    def containsx(self: BboxBase,
                  x: Any) -> bool: ...

    def containsy(self: BboxBase,
                  y: Any) -> bool: ...

    def contains(self: BboxBase,
                 x: Any,
                 y: Any) -> bool: ...

    def overlaps(self: BboxBase,
                 other: Any) -> bool: ...

    def fully_containsx(self: BboxBase,
                        x: Any) -> bool: ...

    def fully_containsy(self: BboxBase,
                        y: Any) -> bool: ...

    def fully_contains(self: BboxBase,
                       x: Any,
                       y: Any) -> bool: ...

    def fully_overlaps(self: BboxBase,
                       other: Any) -> bool: ...

    def transformed(self: BboxBase,
                    transform: {transform}) -> Bbox: ...

    @_api.deprecated("3.3", alternative="transformed(transform.inverted())")
    def inverse_transformed(self: BboxBase,
                            transform: {inverted}) -> Bbox: ...

    def anchored(self: BboxBase,
                 c: Union[tuple[float, float], str],
                 container: Optional[Bbox] = None) -> Bbox: ...

    def shrunk(self: BboxBase,
               mx: {__mul__},
               my: {__mul__}) -> Bbox: ...

    def shrunk_to_aspect(self: BboxBase,
                         box_aspect: {__le__},
                         container: Optional[{size}] = None,
                         fig_aspect: float = 1.0) -> Bbox: ...

    def splitx(self: BboxBase,
               *args) -> list[Bbox]: ...

    def splity(self: BboxBase,
               *args) -> list[Bbox]: ...

    def count_contains(self: BboxBase,
                       vertices: Any) -> int: ...

    def count_overlaps(self: BboxBase,
                       bboxes: Any) -> None: ...

    def expanded(self: BboxBase,
                 sw: {__mul__},
                 sh: {__mul__}) -> Bbox: ...

    def padded(self: BboxBase,
               p: {__neg__}) -> Bbox: ...

    def translated(self: BboxBase,
                   tx: Any,
                   ty: Any) -> Bbox: ...

    def corners(self: BboxBase) -> ndarray: ...

    def rotated(self: BboxBase,
                radians: Any) -> Bbox: ...

    def union(bboxes: {__len__}) -> Bbox: ...

    def intersection(bbox1: {xmin, xmax, ymin, ymax},
                     bbox2: {xmin, xmax, ymin, ymax}) -> Optional[Bbox]: ...


class Bbox(BboxBase):
    def __init__(self: Bbox,
                 points: ndarray,
                 **kwargs) -> Any: ...

    def __init__(self: Bbox,
                 points: Any,
                 **kwargs) -> None: ...

    def invalidate(self: Bbox) -> None: ...

    def unit() -> Bbox: ...

    def null() -> Bbox: ...

    def from_bounds(x0: {__add__},
                    y0: {__add__},
                    width: Any,
                    height: Any) -> Bbox: ...

    def from_extents(*args,
                     minpos: Optional[float] = None) -> Bbox: ...

    def __format__(self: Bbox,
                   fmt: Any) -> str: ...

    def __str__(self: Bbox) -> str: ...

    def __repr__(self: Bbox) -> str: ...

    def ignore(self: Bbox,
               value: Any) -> None: ...

    def update_from_path(self: Bbox,
                         path: Any,
                         ignore: Optional[bool] = None,
                         updatex: bool = True,
                         updatey: bool = True) -> None: ...

    def update_from_data_xy(self: Bbox,
                            xy: ndarray,
                            ignore: Optional[bool] = None,
                            updatex: bool = True,
                            updatey: bool = True) -> None: ...

    def x0(self: Bbox,
           val: Any) -> Optional[Any]: ...

    def y0(self: Bbox,
           val: Any) -> Optional[Any]: ...

    def x1(self: Bbox,
           val: Any) -> Optional[Any]: ...

    def y1(self: Bbox,
           val: Any) -> Optional[Any]: ...

    def p0(self: Bbox,
           val: Any) -> Optional[Any]: ...

    def p1(self: Bbox,
           val: Any) -> Optional[Any]: ...

    def intervalx(self: Bbox,
                  interval: Any) -> Optional[Any]: ...

    def intervaly(self: Bbox,
                  interval: Any) -> Optional[Any]: ...

    def bounds(self: Bbox,
               bounds: Any) -> Optional[Any]: ...

    def minpos(self: Bbox) -> ndarray: ...

    def minposx(self: Bbox) -> None: ...

    def minposy(self: Bbox) -> None: ...

    def get_points(self: Bbox) -> ndarray: ...

    def set_points(self: Bbox,
                   points: Any) -> None: ...

    def set(self: Bbox,
            other: {get_points}) -> None: ...

    def mutated(self: Bbox) -> bool: ...

    def mutatedx(self: Bbox) -> bool: ...

    def mutatedy(self: Bbox) -> bool: ...


class TransformedBbox(BboxBase):
    def __init__(self: TransformedBbox,
                 bbox: Bbox,
                 transform: Transform,
                 **kwargs) -> Any: ...

    def get_points(self: TransformedBbox) -> ndarray: ...

    def get_points(self: TransformedBbox) -> ndarray: ...


class LockableBbox(BboxBase):
    def __init__(self: LockableBbox,
                 bbox: Bbox,
                 x0: Optional[float] = None,
                 y0: Optional[float] = None,
                 x1: Optional[float] = None,
                 y1: Optional[float] = None,
                 **kwargs) -> Any: ...

    def get_points(self: LockableBbox) -> ndarray: ...

    def get_points(self: LockableBbox) -> ndarray: ...

    def locked_x0(self: LockableBbox) -> Optional[Any]: ...

    def locked_x0(self: LockableBbox,
                  x0: Any) -> None: ...

    def locked_y0(self: LockableBbox) -> Optional[Any]: ...

    def locked_y0(self: LockableBbox,
                  y0: Any) -> None: ...

    def locked_x1(self: LockableBbox) -> Optional[Any]: ...

    def locked_x1(self: LockableBbox,
                  x1: Any) -> None: ...

    def locked_y1(self: LockableBbox) -> Optional[Any]: ...

    def locked_y1(self: LockableBbox,
                  y1: Any) -> None: ...


class Transform(TransformNode):
    def __init_subclass__(cls: Type[Transform]) -> None: ...

    def __add__(self: Transform,
                other: Any) -> Union[Transform, CompositeAffine2D, CompositeGenericTransform, _NotImplementedType]: ...

    def _iter_break_from_left_to_right(self: Transform) -> Generator[
        Tuple[IdentityTransform, Transform], Any, None]: ...

    def depth(self: Transform) -> int: ...

    def contains_branch(self: Transform,
                        other: {depth}) -> bool: ...

    def contains_branch_seperately(self: Transform,
                                   other_transform: Any) -> list[bool]: ...

    def __sub__(self: Transform,
                other: {_iter_break_from_left_to_right, has_inverse}) -> Union[
        _NotImplementedType, IdentityTransform, Transform, CompositeAffine2D, CompositeGenericTransform]: ...

    def __array__(self: Transform,
                  *args,
                  **kwargs) -> ndarray: ...

    def transform(self: Transform,
                  values: Union[ndarray, Iterable, int, float]) -> array.pyi: ...

    def transform_affine(self: Transform,
                         values: Union[ndarray, Iterable, int, float]) -> array.pyi: ...

    def transform_non_affine(self: Transform,
                             values: Union[ndarray, Iterable, int, float]) -> array.pyi: ...

    def transform_bbox(self: Transform,
                       bbox: {get_points}) -> Bbox: ...

    def get_affine(self: Transform) -> IdentityTransform: ...

    def get_matrix(self: Transform) -> ndarray: ...

    def transform_point(self: Transform,
                        point: {__len__}) -> Union[ndarray, Iterable, int, float]: ...

    def transform_path(self: Transform,
                       path: {vertices, codes}) -> {vertices, codes}: ...

    def transform_path_affine(self: Transform,
                              path: Path) -> Path: ...

    def transform_path_non_affine(self: Transform,
                                  path: {vertices, codes}) -> Path: ...

    def transform_angles(self: Transform,
                         angles: Any,
                         pts: int,
                         radians: bool = False,
                         pushoff: float = 1e-5) -> Any: ...

    def inverted(self: Transform) -> Any: ...


class TransformWrapper(Transform):
    def __init__(self: TransformWrapper,
                 child: {input_dims, output_dims}) -> None: ...

    def _init(self: TransformWrapper,
              child: {input_dims, output_dims}) -> None: ...

    def __eq__(self: TransformWrapper,
               other: Any) -> Any: ...

    def frozen(self: TransformWrapper) -> Any: ...

    def _set(self: TransformWrapper,
             child: Union[{input_dims, output_dims}, {input_dims, output_dims}]) -> None: ...

    def set(self: TransformWrapper,
            child: {input_dims, output_dims}) -> Any: ...


class AffineBase(Transform):
    def __init__(self: AffineBase,
                 *args,
                 **kwargs) -> None: ...

    def __array__(self: AffineBase,
                  *args,
                  **kwargs) -> ndarray: ...

    def __eq__(self: AffineBase,
               other: Any) -> Union[ndarray, bool, _NotImplementedType]: ...

    def transform(self: AffineBase,
                  values: Union[ndarray, Iterable, int, float]) -> Any: ...

    def transform_affine(self: AffineBase,
                         values: Union[ndarray, Iterable, int, float]) -> Any: ...

    def transform_non_affine(self: AffineBase,
                             points: Any) -> Any: ...

    def transform_path(self: AffineBase,
                       path: {vertices, codes}) -> Path: ...

    def transform_path_affine(self: AffineBase,
                              path: Path) -> Path: ...

    def transform_path_non_affine(self: AffineBase,
                                  path: {vertices, codes}) -> {vertices, codes}: ...

    def get_affine(self: AffineBase) -> AffineBase: ...


class Affine2DBase(AffineBase):
    def frozen(self: Affine2DBase) -> Affine2D: ...

    def is_separable(self: Affine2DBase) -> bool: ...

    def to_values(self: Affine2DBase) -> Tuple: ...

    def transform_affine(self: Affine2DBase,
                         points: Any) -> None: ...

    def transform_affine(self: Affine2DBase,
                         points: Any) -> None: ...

    def inverted(self: Affine2DBase) -> Affine2D: ...


class Affine2D(Affine2DBase):
    def __init__(self: Affine2D,
                 matrix: Optional[{copy}] = None,
                 **kwargs) -> None: ...

    def from_values(a: Any,
                    b: Any,
                    c: Any,
                    d: Any,
                    e: Any,
                    f: Any) -> Affine2D: ...

    def get_matrix(self: Affine2D) -> Any: ...

    def set_matrix(self: Affine2D,
                   mtx: Any) -> None: ...

    def set(self: Affine2D,
            other: {get_matrix}) -> None: ...

    def identity() -> Affine2D: ...

    def clear(self: Affine2D) -> Affine2D: ...

    def rotate(self: Affine2D,
               theta: float) -> Affine2D: ...

    def rotate_deg(self: Affine2D,
                   degrees: Any) -> Affine2D: ...

    def rotate_around(self: Affine2D,
                      x: {__neg__},
                      y: {__neg__},
                      theta: Any) -> Any: ...

    def rotate_deg_around(self: Affine2D,
                          x: Any,
                          y: Any,
                          degrees: Any) -> Any: ...

    def translate(self: Affine2D,
                  tx: float,
                  ty: float) -> Affine2D: ...

    def scale(self: Affine2D,
              sx: Any,
              sy: Any = None) -> Affine2D: ...

    def skew(self: Affine2D,
             xShear: float,
             yShear: Any) -> Affine2D: ...

    def skew_deg(self: Affine2D,
                 xShear: Any,
                 yShear: Any) -> Affine2D: ...


class IdentityTransform(Affine2DBase):
    def frozen(self: IdentityTransform) -> IdentityTransform: ...

    def get_matrix(self: IdentityTransform) -> ndarray: ...

    def transform(self: IdentityTransform,
                  points: Union[ndarray, Iterable, int, float]) -> Any: ...

    def transform_affine(self: IdentityTransform,
                         points: Any) -> Any: ...

    def transform_non_affine(self: IdentityTransform,
                             points: Any) -> Any: ...

    def transform_path(self: IdentityTransform,
                       path: {vertices, codes}) -> {vertices, codes}: ...

    def transform_path_affine(self: IdentityTransform,
                              path: Path) -> Path: ...

    def transform_path_non_affine(self: IdentityTransform,
                                  path: {vertices, codes}) -> {vertices, codes}: ...

    def get_affine(self: IdentityTransform) -> IdentityTransform: ...

    def inverted(self: IdentityTransform) -> IdentityTransform: ...


class _BlendedMixin(object):
    def __eq__(self: _BlendedMixin,
               other: Any) -> Union[bool, _NotImplementedType]: ...

    def contains_branch_seperately(self: _BlendedMixin,
                                   transform: Any) -> Tuple[Any, Any]: ...


class BlendedGenericTransform(_BlendedMixin, Transform):
    def __init__(self: BlendedGenericTransform,
                 x_transform: Any,
                 y_transform: Any,
                 **kwargs) -> None: ...

    def depth(self: BlendedGenericTransform) -> SupportsLessThan: ...

    def contains_branch(self: BlendedGenericTransform,
                        other: {depth}) -> bool: ...

    def frozen(self: BlendedGenericTransform) -> Union[BlendedAffine2D, BlendedGenericTransform]: ...

    def transform_non_affine(self: BlendedGenericTransform,
                             points: Any) -> Union[MaskedArray, ndarray]: ...

    def inverted(self: BlendedGenericTransform) -> BlendedGenericTransform: ...

    def get_affine(self: BlendedGenericTransform) -> Affine2D: ...


class BlendedAffine2D(_BlendedMixin, Affine2DBase):
    def __init__(self: BlendedAffine2D,
                 x_transform: {is_affine, is_separable},
                 y_transform: {is_affine, is_separable},
                 **kwargs) -> Any: ...

    def get_matrix(self: BlendedAffine2D) -> ndarray: ...


def blended_transform_factory(x_transform: Any,
                              y_transform: Any) -> Union[BlendedAffine2D, BlendedGenericTransform]: ...


class CompositeGenericTransform(Transform):
    def __init__(self: CompositeGenericTransform,
                 a: {output_dims, input_dims},
                 b: {input_dims, output_dims},
                 **kwargs) -> Any: ...

    def frozen(self: CompositeGenericTransform) -> Union[TransformNode, Affine2D, CompositeGenericTransform]: ...

    def _invalidate_internal(self: CompositeGenericTransform,
                             value: int,
                             invalidating_node: Any) -> None: ...

    def __eq__(self: CompositeGenericTransform,
               other: Any) -> bool: ...

    def _iter_break_from_left_to_right(self: CompositeGenericTransform) -> Generator[Tuple[Any, Any], Any, None]: ...

    def transform_affine(self: CompositeGenericTransform,
                         points: Any) -> Any: ...

    def transform_non_affine(self: CompositeGenericTransform,
                             points: Any) -> Any: ...

    def transform_path_non_affine(self: CompositeGenericTransform,
                                  path: {vertices, codes}) -> {vertices, codes}: ...

    def get_affine(self: CompositeGenericTransform) -> Affine2D: ...

    def inverted(self: CompositeGenericTransform) -> CompositeGenericTransform: ...


class CompositeAffine2D(Affine2DBase):
    def __init__(self: CompositeAffine2D,
                 a: {is_affine, output_dims, input_dims},
                 b: {is_affine, input_dims, output_dims},
                 **kwargs) -> Any: ...

    def depth(self: CompositeAffine2D) -> Any: ...

    def _iter_break_from_left_to_right(self: CompositeAffine2D) -> Generator[Tuple[Any, Any], Any, None]: ...

    def get_matrix(self: CompositeAffine2D) -> ndarray: ...


def composite_transform_factory(a: Transform,
                                b: Transform) -> Union[Transform, CompositeAffine2D, CompositeGenericTransform]: ...


class BboxTransform(Affine2DBase):
    def __init__(self: BboxTransform,
                 boxin: {is_bbox},
                 boxout: {is_bbox},
                 **kwargs) -> Any: ...

    def get_matrix(self: BboxTransform) -> ndarray: ...


class BboxTransformTo(Affine2DBase):
    def __init__(self: BboxTransformTo,
                 boxout: {is_bbox},
                 **kwargs) -> Any: ...

    def get_matrix(self: BboxTransformTo) -> ndarray: ...


class BboxTransformToMaxOnly(BboxTransformTo):
    def get_matrix(self: BboxTransformToMaxOnly) -> ndarray: ...


class BboxTransformFrom(Affine2DBase):
    def __init__(self: BboxTransformFrom,
                 boxin: {is_bbox},
                 **kwargs) -> Any: ...

    def get_matrix(self: BboxTransformFrom) -> ndarray: ...


class ScaledTranslation(Affine2DBase):
    def __init__(self: ScaledTranslation,
                 xt: Any,
                 yt: Any,
                 scale_trans: Any,
                 **kwargs) -> None: ...

    def get_matrix(self: ScaledTranslation) -> None: ...


class AffineDeltaTransform(Affine2DBase):
    def __init__(self: AffineDeltaTransform,
                 transform: Any,
                 **kwargs) -> None: ...

    def get_matrix(self: AffineDeltaTransform) -> Any: ...


class TransformedPath(TransformNode):
    def __init__(self: TransformedPath,
                 path: Any,
                 transform: Transform) -> None: ...

    def _revalidate(self: TransformedPath) -> None: ...

    def get_transformed_points_and_affine(self: TransformedPath) -> Tuple[Any, IdentityTransform]: ...

    def get_transformed_path_and_affine(self: TransformedPath) -> Tuple[Any, IdentityTransform]: ...

    def get_fully_transformed_path(self: TransformedPath) -> {vertices, codes}: ...

    def get_affine(self: TransformedPath) -> IdentityTransform: ...


class TransformedPatchPath(TransformedPath):
    def __init__(self: TransformedPatchPath,
                 patch: Any) -> None: ...

    def _revalidate(self: TransformedPatchPath) -> None: ...


def nonsingular(vmin: float,
                vmax: float,
                expander: float = 0.001,
                tiny: float = 1e-15,
                increasing: bool = True) -> float: ...


def interval_contains(interval: tuple[float, float],
                      val: float) -> bool: ...


def _interval_contains_close(interval: tuple[float, float],
                             val: float,
                             rtol: float = 1e-10) -> bool: ...


def interval_contains_open(interval: tuple[float, float],
                           val: float) -> bool: ...


def offset_copy(trans: Any,
                fig: Any = None,
                x: float = 0.0,
                y: float = 0.0,
                units: str = 'inches') -> Any: ...