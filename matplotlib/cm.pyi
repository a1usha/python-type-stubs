from typing import Any
from typing import Iterator
from typing import MutableMapping
from typing import Optional
from typing import Tuple
from typing import Union

from matplotlib import _api
from matplotlib.cm import ScalarMappable
from matplotlib.cm import _DeprecatedCmapDictWrapper
from matplotlib.colors import Colormap
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.colors import ListedColormap
from numpy.core._multiarray_umath import ndarray
from object import object


def _gen_cmap_registry() -> dict[Union[str, Any], Union[Union[LinearSegmentedColormap, ListedColormap], Any]]: ...


class _DeprecatedCmapDictWrapper(MutableMapping):
    def __init__(self: _DeprecatedCmapDictWrapper,
                 cmap_registry: Any) -> None: ...

    def __delitem__(self: _DeprecatedCmapDictWrapper,
                    key: Any) -> None: ...

    def __getitem__(self: _DeprecatedCmapDictWrapper,
                    key: Any) -> _VT_co: ...

    def __iter__(self: _DeprecatedCmapDictWrapper) -> Iterator[_T_co]: ...

    def __len__(self: _DeprecatedCmapDictWrapper) -> int: ...

    def __setitem__(self: _DeprecatedCmapDictWrapper,
                    key: Any,
                    val: Any) -> None: ...

    def get(self: _DeprecatedCmapDictWrapper,
            key: Any,
            default: Any = None) -> Any: ...

    def _warn_deprecated(self: _DeprecatedCmapDictWrapper) -> None: ...


def register_cmap(name: Optional[str] = None,
                  cmap: Colormap = None,
                  *,
                  override_builtin: bool = False) -> None: ...


def get_cmap(name: Union[Colormap, str, None] = None,
             lut: Optional[int] = None) -> Union[Union[Colormap, LinearSegmentedColormap, ListedColormap], Any]: ...


def unregister_cmap(name: str) -> Union[Union[None, LinearSegmentedColormap, ListedColormap], Any]: ...


class ScalarMappable(object):
    def __init__(self: ScalarMappable,
                 norm: Any = None,
                 cmap: Any = None) -> None: ...

    def _scale_norm(self: ScalarMappable,
                    norm: Any,
                    vmin: Any,
                    vmax: Any) -> None: ...

    def to_rgba(self: ScalarMappable,
                x: {ndim},
                alpha: Any = None,
                bytes: bool = False,
                norm: bool = True) -> Union[Union[ndarray, {ndim}, None], Any]: ...

    def set_array(self: ScalarMappable,
                  A: Optional[ndarray]) -> None: ...

    def get_array(self: ScalarMappable) -> Any: ...

    def get_cmap(self: ScalarMappable) -> Any: ...

    def get_clim(self: ScalarMappable) -> Tuple[Any, Any]: ...

    def set_clim(self: ScalarMappable,
                 vmin: float = None,
                 vmax: float = None) -> None: ...

    def get_alpha(self: ScalarMappable) -> float: ...

    def set_cmap(self: ScalarMappable,
                 cmap: Any) -> None: ...

    def set_norm(self: ScalarMappable,
                 norm: Any) -> None: ...

    def autoscale(self: ScalarMappable) -> Any: ...

    def autoscale_None(self: ScalarMappable) -> Any: ...

    def _add_checker(self: ScalarMappable,
                     checker: Any) -> None: ...

    def _check_update(self: ScalarMappable,
                      checker: Any) -> bool: ...

    def changed(self: ScalarMappable) -> None: ...

    @_api.deprecated("3.3")
    def add_checker(self: ScalarMappable,
                    checker: Any) -> Optional[Any]: ...

    @_api.deprecated("3.3")
    def check_update(self: ScalarMappable,
                     checker: Any) -> Union[bool, Any]: ...
