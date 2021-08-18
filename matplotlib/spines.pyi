from functools import partial
from typing import Any
from typing import Iterator
from typing import MutableMapping
from typing import Optional
from typing import Type
from typing import Union

from matplotlib import _api
from matplotlib.patches import Patch
from matplotlib.spines import Spine
from matplotlib.spines import Spines
from matplotlib.spines import SpinesProxy
from matplotlib.transforms import Bbox
from matplotlib.transforms import BlendedAffine2D
from matplotlib.transforms import BlendedGenericTransform
from matplotlib.transforms import CompositeAffine2D
from matplotlib.transforms import CompositeGenericTransform
from matplotlib.transforms import IdentityTransform
from object import object


class Spine(Patch):
    def __str__(self: Spine) -> str: ...

    def __init__(self: Spine,
                 axes: Any,
                 spine_type: str,
                 path: Any,
                 **kwargs) -> Optional[Any]: ...

    def set_patch_arc(self: Spine,
                      center: Any,
                      radius: {__mul__},
                      theta1: Any,
                      theta2: {__sub__, __ne__}) -> None: ...

    def set_patch_circle(self: Spine,
                         center: Any,
                         radius: {__mul__}) -> None: ...

    def set_patch_line(self: Spine) -> None: ...

    def _recompute_transform(self: Spine) -> None: ...

    def get_patch_transform(self: Spine) -> IdentityTransform: ...

    def get_window_extent(self: Spine,
                          renderer: Any = None) -> Union[Bbox, Any]: ...

    def get_path(self: Spine) -> Any: ...

    def _ensure_position_is_set(self: Spine) -> None: ...

    def register_axis(self: Spine,
                      axis: Any) -> None: ...

    def clear(self: Spine) -> None: ...

    @_api.deprecated("3.4", alternative="Spine.clear()")
    def cla(self: Spine) -> Optional[Any]: ...

    def _adjust_location(self: Spine) -> None: ...

    def draw(self: Spine,
             renderer: {open_group, new_gc, draw_path, close_group}) -> Any: ...

    def set_position(self: Spine,
                     position: Union[tuple[str, float], Any]) -> Any: ...

    def get_position(self: Spine) -> Any: ...

    def get_spine_transform(self: Spine) -> Union[Union[{input_dims, output_dims}, {output_dims,
                                                                                    input_dims}, CompositeAffine2D, CompositeGenericTransform, _NotImplementedType, BlendedAffine2D, BlendedGenericTransform], Any]: ...

    def set_bounds(self: Spine,
                   low: Optional[float] = None,
                   high: Optional[float] = None) -> Any: ...

    def get_bounds(self: Spine) -> Any: ...

    def linear_spine(cls: Type[Spine],
                     axes: Any,
                     spine_type: {__eq__},
                     **kwargs) -> Spine: ...

    def arc_spine(cls: Type[Spine],
                  axes: Any,
                  spine_type: Any,
                  center: Any,
                  radius: {__mul__},
                  theta1: Any,
                  theta2: {__sub__, __ne__},
                  **kwargs) -> Spine: ...

    def circular_spine(cls: Type[Spine],
                       axes: Any,
                       center: Any,
                       radius: {__mul__},
                       **kwargs) -> Spine: ...

    def set_color(self: Spine,
                  c: Any) -> None: ...


class SpinesProxy(object):
    def __init__(self: SpinesProxy,
                 spine_dict: Any) -> None: ...

    def __getattr__(self: SpinesProxy,
                    name: {startswith}) -> partial[None]: ...

    def __dir__(self: SpinesProxy) -> list[Union[Optional[str], Any]]: ...


class Spines(MutableMapping):
    def __init__(self: Spines,
                 **kwargs) -> None: ...

    def from_dict(cls: Type[Spines],
                  d: Any) -> Spines: ...

    def __getstate__(self: Spines) -> dict[str, Any]: ...

    def __setstate__(self: Spines,
                     state: Any) -> None: ...

    def __getattr__(self: Spines,
                    name: Any) -> Any: ...

    def __getitem__(self: Spines,
                    key: Any) -> _VT_co: ...

    def __setitem__(self: Spines,
                    key: Any,
                    value: Any) -> None: ...

    def __delitem__(self: Spines,
                    key: Any) -> None: ...

    def __iter__(self: Spines) -> Iterator[_T_co]: ...

    def __len__(self: Spines) -> int: ...
