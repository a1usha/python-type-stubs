from path import Path as Path
from matplotlib._path import update_path_extents as update_path_extents
from matplotlib._path import count_bboxes_overlapping_bbox as count_bboxes_overlapping_bbox
from matplotlib._path import affine_transform as affine_transform
from matplotlib import _api as _api
from numpy.linalg import inv as inv
from _typeshed import SupportsLessThan
from typing import Any
from typing import Callable
from typing import ClassVar
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
from numpy.ma.core import MaskedArray
from object import object

DEBUG: bool


def _make_str_method(*args,
                     **kwargs) -> Callable[[Any], Any]: ...


class TransformNode(object):
    INVALID_NON_AFFINE: ClassVar[int]
    INVALID_AFFINE: ClassVar[int]
    INVALID: ClassVar[int]
    is_affine: ClassVar[bool]
    is_bbox: ClassVar[bool]
    pass_through: ClassVar[bool]
    _shorthand_name: str
    _invalid: int
    __dict__: dict[str, Any]
    _parents: dict[Any, Any]

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
                             value: Union[Union[int, {__eq__}], Any],
                             invalidating_node: Any) -> None: ...

    def set_children(self: TransformNode,
                     *args) -> None: ...

    def frozen(self: TransformNode) -> TransformNode: ...


class BboxBase(TransformNode):
    is_bbox: ClassVar[bool]
    is_affine: ClassVar[bool]
    coefs: ClassVar[dict[str, Union[tuple[float, int], tuple[float, float], tuple[int, int], tuple[int, float]]]]

    def _check(points: Any) -> None: ...

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

    def xmin(self: BboxBase) -> Union[Union[int, float, complex], Any]: ...

    def ymin(self: BboxBase) -> Union[Union[int, float, complex], Any]: ...

    def xmax(self: BboxBase) -> Union[Union[int, float, complex], Any]: ...

    def ymax(self: BboxBase) -> Union[Union[int, float, complex], Any]: ...

    def min(self: BboxBase) -> Union[Union[int, float, complex], Any]: ...

    def max(self: BboxBase) -> Union[Union[int, float, complex], Any]: ...

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
                            transform: {inverted}) -> Union[Bbox, Any]: ...

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
                       vertices: Any) -> Union[int, Any]: ...

    def count_overlaps(self: BboxBase,
                       bboxes: Any) -> Any: ...

    def expanded(self: BboxBase,
                 sw: {__mul__},
                 sh: {__mul__}) -> Bbox: ...

    def padded(self: BboxBase,
               p: {__neg__}) -> Bbox: ...

    def translated(self: BboxBase,
                   tx: Any,
                   ty: Any) -> Bbox: ...

    def corners(self: BboxBase) -> Any: ...

    def rotated(self: BboxBase,
                radians: Any) -> Bbox: ...

    def union(bboxes: {__len__}) -> Bbox: ...

    def intersection(bbox1: {xmin, xmax, ymin, ymax},
                     bbox2: {xmin, xmax, ymin, ymax}) -> Optional[Bbox]: ...


class Bbox(BboxBase):
    _invalid: int
    _minpos: Any
    _ignore: bool
    _points_orig: Any
    _points: Any

    def __init__(self: Bbox,
                 points: Any,
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
                            xy: Any,
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

    def minpos(self: Bbox) -> Any: ...

    def minposx(self: Bbox) -> Any: ...

    def minposy(self: Bbox) -> Any: ...

    def get_points(self: Bbox) -> Any: ...

    def set_points(self: Bbox,
                   points: Any) -> None: ...

    def set(self: Bbox,
            other: {get_points}) -> None: ...

    def mutated(self: Bbox) -> bool: ...

    def mutatedx(self: Bbox) -> bool: ...

    def mutatedy(self: Bbox) -> bool: ...


class TransformedBbox(BboxBase):
    __str__: ClassVar[Callable[[Any], Any]]
    _bbox: Bbox
    _transform: Transform
    _invalid: int
    _points: None

    def __init__(self: TransformedBbox,
                 bbox: Bbox,
                 transform: Transform,
                 **kwargs) -> Any: ...

    def get_points(self: TransformedBbox) -> Any: ...

    def get_points(self: TransformedBbox) -> Any: ...


class LockableBbox(BboxBase):
    __str__: ClassVar[Callable[[Any], Any]]
    _bbox: Bbox
    _invalid: int
    _locked_points: Union[Union[Iterable, int, float], Any]
    _points: None

    def __init__(self: LockableBbox,
                 bbox: Bbox,
                 x0: Optional[float] = None,
                 y0: Optional[float] = None,
                 x1: Optional[float] = None,
                 y1: Optional[float] = None,
                 **kwargs) -> Any: ...

    def get_points(self: LockableBbox) -> Any: ...

    def get_points(self: LockableBbox) -> Any: ...

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
    input_dims: ClassVar[None]
    output_dims: ClassVar[None]
    is_separable: ClassVar[bool]
    has_inverse: ClassVar[bool]
    has_inverse: bool
    is_separable: bool

    def __init_subclass__(cls: Type[Transform]) -> None: ...

    def __add__(self: Transform,
                other: Any) -> Union[
        Union[Transform, CompositeAffine2D, CompositeGenericTransform, _NotImplementedType], Any]: ...

    def _iter_break_from_left_to_right(self: Transform) -> Generator[
        Tuple[IdentityTransform, Transform], Any, None]: ...

    def depth(self: Transform) -> int: ...

    def contains_branch(self: Transform,
                        other: {depth}) -> bool: ...

    def contains_branch_seperately(self: Transform,
                                   other_transform: Any) -> list[bool]: ...

    def __sub__(self: Transform,
                other: {_iter_break_from_left_to_right, has_inverse}) -> Union[Union[
                                                                                   _NotImplementedType, IdentityTransform, Transform, CompositeAffine2D, CompositeGenericTransform], Any]: ...

    def __array__(self: Transform,
                  *args,
                  **kwargs) -> Any: ...

    def transform(self: Transform,
                  values: Union[Union[Iterable, int, float], Any]) -> array.pyi: ...

    def transform_affine(self: Transform,
                         values: Union[Union[Iterable, int, float], Any]) -> array.pyi: ...

    def transform_non_affine(self: Transform,
                             values: Union[Union[Iterable, int, float], Any]) -> array.pyi: ...

    def transform_bbox(self: Transform,
                       bbox: {get_points}) -> Bbox: ...

    def get_affine(self: Transform) -> IdentityTransform: ...

    def get_matrix(self: Transform) -> Any: ...

    def transform_point(self: Transform,
                        point: {__len__}) -> Union[Union[Iterable, int, float], Any]: ...

    def transform_path(self: Transform,
                       path: {vertices, codes}) -> Union[{vertices, codes}, Any]: ...

    def transform_path_affine(self: Transform,
                              path: Union[Path, Any]) -> Union[Path, Any]: ...

    def transform_path_non_affine(self: Transform,
                                  path: {vertices, codes}) -> Path: ...

    def transform_angles(self: Transform,
                         angles: Any,
                         pts: int,
                         radians: bool = False,
                         pushoff: float = 1e-5) -> Any: ...

    def inverted(self: Transform) -> Any: ...


class TransformWrapper(Transform):
    pass_through: ClassVar[bool]
    __str__: ClassVar[Callable[[Any], Any]]
    is_affine: ClassVar[property]
    is_separable: ClassVar[property]
    has_inverse: ClassVar[property]
    _invalid: int
    transform_path_affine: Any
    get_affine: Any
    transform: Any
    transform_non_affine: Any
    transform_affine: Any
    get_matrix: Any
    transform_path_non_affine: Any
    output_dims: Any
    inverted: Any
    _child: Union[Union[{input_dims, output_dims}, {input_dims, output_dims}], Any]
    transform_path: Any
    input_dims: Any

    def __init__(self: TransformWrapper,
                 child: {input_dims, output_dims}) -> None: ...

    def _init(self: TransformWrapper,
              child: {input_dims, output_dims}) -> None: ...

    def __eq__(self: TransformWrapper,
               other: Any) -> Any: ...

    def frozen(self: TransformWrapper) -> Any: ...

    def _set(self: TransformWrapper,
             child: Union[Union[{input_dims, output_dims}, {input_dims, output_dims}], Any]) -> None: ...

    def set(self: TransformWrapper,
            child: {input_dims, output_dims}) -> Any: ...


class AffineBase(Transform):
    is_affine: ClassVar[bool]
    _inverted: None

    def __init__(self: AffineBase,
                 *args,
                 **kwargs) -> None: ...

    def __array__(self: AffineBase,
                  *args,
                  **kwargs) -> Any: ...

    def __eq__(self: AffineBase,
               other: Any) -> Union[bool, _NotImplementedType]: ...

    def transform(self: AffineBase,
                  values: Union[Union[Iterable, int, float], Any]) -> Any: ...

    def transform_affine(self: AffineBase,
                         values: Union[Union[Iterable, int, float], Any]) -> Any: ...

    def transform_non_affine(self: AffineBase,
                             points: Any) -> Any: ...

    def transform_path(self: AffineBase,
                       path: {vertices, codes}) -> Path: ...

    def transform_path_affine(self: AffineBase,
                              path: Union[Path, Any]) -> Path: ...

    def transform_path_non_affine(self: AffineBase,
                                  path: {vertices, codes}) -> {vertices, codes}: ...

    def get_affine(self: AffineBase) -> AffineBase: ...


class Affine2DBase(AffineBase):
    input_dims: ClassVar[int]
    output_dims: ClassVar[int]
    _invalid: int
    _inverted: Affine2D

    def frozen(self: Affine2DBase) -> Affine2D: ...

    def is_separable(self: Affine2DBase) -> bool: ...

    def to_values(self: Affine2DBase) -> Tuple: ...

    def transform_affine(self: Affine2DBase,
                         points: Any) -> Union[MaskedArray, Any]: ...

    def transform_affine(self: Affine2DBase,
                         points: Any) -> Union[MaskedArray, Any]: ...

    def inverted(self: Affine2DBase) -> Union[Affine2D, Any]: ...


class Affine2D(Affine2DBase):
    __str__: ClassVar[Callable[[Any], Any]]
    _invalid: int
    _inverted: None
    _mtx: Any

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
               theta: Union[float, Any]) -> Affine2D: ...

    def rotate_deg(self: Affine2D,
                   degrees: Any) -> Affine2D: ...

    def rotate_around(self: Affine2D,
                      x: {__neg__},
                      y: {__neg__},
                      theta: Any) -> Affine2D: ...

    def rotate_deg_around(self: Affine2D,
                          x: Any,
                          y: Any,
                          degrees: Any) -> Affine2D: ...

    def translate(self: Affine2D,
                  tx: Union[float, Any],
                  ty: Union[float, Any]) -> Affine2D: ...

    def scale(self: Affine2D,
              sx: Any,
              sy: Any = None) -> Affine2D: ...

    def skew(self: Affine2D,
             xShear: Union[float, Any],
             yShear: Any) -> Affine2D: ...

    def skew_deg(self: Affine2D,
                 xShear: Any,
                 yShear: Any) -> Affine2D: ...


class IdentityTransform(Affine2DBase):
    _mtx: ClassVar[Any]
    __str__: ClassVar[Callable[[Any], Any]]

    def frozen(self: IdentityTransform) -> IdentityTransform: ...

    def get_matrix(self: IdentityTransform) -> Any: ...

    def transform(self: IdentityTransform,
                  points: Union[Union[Iterable, int, float], Any]) -> Any: ...

    def transform_affine(self: IdentityTransform,
                         points: Any) -> Any: ...

    def transform_non_affine(self: IdentityTransform,
                             points: Any) -> Any: ...

    def transform_path(self: IdentityTransform,
                       path: {vertices, codes}) -> {vertices, codes}: ...

    def transform_path_affine(self: IdentityTransform,
                              path: Union[Path, Any]) -> Union[Path, Any]: ...

    def transform_path_non_affine(self: IdentityTransform,
                                  path: {vertices, codes}) -> {vertices, codes}: ...

    def get_affine(self: IdentityTransform) -> IdentityTransform: ...

    def inverted(self: IdentityTransform) -> IdentityTransform: ...


class _BlendedMixin(object):
    __str__: ClassVar[Callable[[Any], Any]]

    def __eq__(self: _BlendedMixin,
               other: Any) -> Union[bool, _NotImplementedType]: ...

    def contains_branch_seperately(self: _BlendedMixin,
                                   transform: Any) -> Tuple[Any, Any]: ...


class BlendedGenericTransform(_BlendedMixin, Transform):
    input_dims: ClassVar[int]
    output_dims: ClassVar[int]
    is_separable: ClassVar[bool]
    pass_through: ClassVar[bool]
    is_affine: ClassVar[property]
    has_inverse: ClassVar[property]
    _invalid: int
    _x: Any
    _y: Any
    _affine: None

    def __init__(self: BlendedGenericTransform,
                 x_transform: Any,
                 y_transform: Any,
                 **kwargs) -> None: ...

    def depth(self: BlendedGenericTransform) -> Union[SupportsLessThan, Any]: ...

    def contains_branch(self: BlendedGenericTransform,
                        other: {depth}) -> bool: ...

    def frozen(self: BlendedGenericTransform) -> Union[BlendedAffine2D, BlendedGenericTransform]: ...

    def transform_non_affine(self: BlendedGenericTransform,
                             points: Any) -> Union[MaskedArray, Any]: ...

    def inverted(self: BlendedGenericTransform) -> BlendedGenericTransform: ...

    def get_affine(self: BlendedGenericTransform) -> Union[Affine2D, Any]: ...


class BlendedAffine2D(_BlendedMixin, Affine2DBase):
    is_separable: ClassVar[bool]
    _invalid: int
    _x: {is_affine, is_separable}
    _y: {is_affine, is_separable}
    _inverted: None
    _mtx: None

    def __init__(self: BlendedAffine2D,
                 x_transform: {is_affine, is_separable},
                 y_transform: {is_affine, is_separable},
                 **kwargs) -> Any: ...

    def get_matrix(self: BlendedAffine2D) -> Any: ...


def blended_transform_factory(x_transform: Any,
                              y_transform: Any) -> Union[BlendedAffine2D, BlendedGenericTransform]: ...


class CompositeGenericTransform(Transform):
    pass_through: ClassVar[bool]
    depth: ClassVar[property]
    is_affine: ClassVar[property]
    is_separable: ClassVar[property]
    has_inverse: ClassVar[property]
    __str__: ClassVar[Callable[[Any], Any]]
    _a: {output_dims, input_dims}
    _b: {input_dims, output_dims}
    _invalid: int
    output_dims: Any
    input_dims: Any

    def __init__(self: CompositeGenericTransform,
                 a: {output_dims, input_dims},
                 b: {input_dims, output_dims},
                 **kwargs) -> Any: ...

    def frozen(self: CompositeGenericTransform) -> Union[TransformNode, Affine2D, CompositeGenericTransform]: ...

    def _invalidate_internal(self: CompositeGenericTransform,
                             value: Union[int, Any],
                             invalidating_node: Any) -> None: ...

    def __eq__(self: CompositeGenericTransform,
               other: Any) -> Union[bool, Any]: ...

    def _iter_break_from_left_to_right(self: CompositeGenericTransform) -> Generator[Tuple[Any, Any], Any, None]: ...

    def transform_affine(self: CompositeGenericTransform,
                         points: Any) -> Any: ...

    def transform_non_affine(self: CompositeGenericTransform,
                             points: Any) -> Any: ...

    def transform_path_non_affine(self: CompositeGenericTransform,
                                  path: {vertices, codes}) -> Union[{vertices, codes}, Any]: ...

    def get_affine(self: CompositeGenericTransform) -> Union[Affine2D, Any]: ...

    def inverted(self: CompositeGenericTransform) -> CompositeGenericTransform: ...


class CompositeAffine2D(Affine2DBase):
    __str__: ClassVar[Callable[[Any], Any]]
    _a: {is_affine, output_dims, input_dims}
    _b: {is_affine, input_dims, output_dims}
    _invalid: int
    _inverted: None
    output_dims: Any
    _mtx: None
    input_dims: Any

    def __init__(self: CompositeAffine2D,
                 a: {is_affine, output_dims, input_dims},
                 b: {is_affine, input_dims, output_dims},
                 **kwargs) -> Any: ...

    def depth(self: CompositeAffine2D) -> Any: ...

    def _iter_break_from_left_to_right(self: CompositeAffine2D) -> Generator[Tuple[Any, Any], Any, None]: ...

    def get_matrix(self: CompositeAffine2D) -> Any: ...


def composite_transform_factory(a: Union[Transform, Any],
                                b: Union[Transform, Any]) -> Union[
    Union[Transform, CompositeAffine2D, CompositeGenericTransform], Any]: ...


class BboxTransform(Affine2DBase):
    is_separable: ClassVar[bool]
    __str__: ClassVar[Callable[[Any], Any]]
    _boxin: {is_bbox}
    _invalid: int
    _inverted: None
    _boxout: {is_bbox}
    _mtx: None

    def __init__(self: BboxTransform,
                 boxin: {is_bbox},
                 boxout: {is_bbox},
                 **kwargs) -> Any: ...

    def get_matrix(self: BboxTransform) -> Any: ...


class BboxTransformTo(Affine2DBase):
    is_separable: ClassVar[bool]
    __str__: ClassVar[Callable[[Any], Any]]
    _invalid: int
    _inverted: None
    _boxout: {is_bbox}
    _mtx: None

    def __init__(self: BboxTransformTo,
                 boxout: {is_bbox},
                 **kwargs) -> Any: ...

    def get_matrix(self: BboxTransformTo) -> Any: ...


class BboxTransformToMaxOnly(BboxTransformTo):
    _invalid: int
    _inverted: None
    _mtx: Any

    def get_matrix(self: BboxTransformToMaxOnly) -> Any: ...


class BboxTransformFrom(Affine2DBase):
    is_separable: ClassVar[bool]
    __str__: ClassVar[Callable[[Any], Any]]
    _boxin: {is_bbox}
    _invalid: int
    _inverted: None
    _mtx: None

    def __init__(self: BboxTransformFrom,
                 boxin: {is_bbox},
                 **kwargs) -> Any: ...

    def get_matrix(self: BboxTransformFrom) -> Any: ...


class ScaledTranslation(Affine2DBase):
    __str__: ClassVar[Callable[[Any], Any]]
    _scale_trans: Any
    _t: tuple[Any, Any]
    _invalid: int
    _inverted: None
    _mtx: None

    def __init__(self: ScaledTranslation,
                 xt: Any,
                 yt: Any,
                 scale_trans: Any,
                 **kwargs) -> None: ...

    def get_matrix(self: ScaledTranslation) -> Any: ...


class AffineDeltaTransform(Affine2DBase):
    __str__: ClassVar[Callable[[Any], Any]]
    _base_transform: Any
    _mtx: Any

    def __init__(self: AffineDeltaTransform,
                 transform: Any,
                 **kwargs) -> None: ...

    def get_matrix(self: AffineDeltaTransform) -> Any: ...


class TransformedPath(TransformNode):
    _transform: Transform
    _transformed_points: None
    _invalid: int
    _path: Any
    _transformed_path: None

    def __init__(self: TransformedPath,
                 path: Any,
                 transform: Transform) -> None: ...

    def _revalidate(self: TransformedPath) -> None: ...

    def get_transformed_points_and_affine(self: TransformedPath) -> Tuple[Any, IdentityTransform]: ...

    def get_transformed_path_and_affine(self: TransformedPath) -> Tuple[Any, IdentityTransform]: ...

    def get_fully_transformed_path(self: TransformedPath) -> Union[{vertices, codes}, Any]: ...

    def get_affine(self: TransformedPath) -> IdentityTransform: ...


class TransformedPatchPath(TransformedPath):
    _transform: Any
    _transformed_points: None
    _invalid: int
    _path: Any
    _transformed_path: None
    _patch: Any

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