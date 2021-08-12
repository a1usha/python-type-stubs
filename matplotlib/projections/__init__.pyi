from typing import Any
from typing import Union
from typing import Any
from typing import Iterable
from numpy.core._multiarray_umath import ndarray
from typing import Any
from typing import Union
from typing import Any
from typing import Iterable
from numpy.core._multiarray_umath import ndarray
from typing import Union
from typing import Any
from typing import Optional
from typing import Optional
from typing import Any
from typing import Optional
from typing import Any
from typing import Union
from typing import Any
from typing import Any
from typing import Optional
from typing import Optional
from typing import Any


class ExecutableNotFoundError(FileNotFoundError):
    pass


class _StrongRef(object):
    def __init__(self: _StrongRef, obj: Any) -> None: ...

    def __call__(self: _StrongRef) -> Any: ...

    def __eq__(self: _StrongRef, other: {_obj}) -> bool: ...

    def __hash__(self: _StrongRef) -> int: ...


class _OrderedSet(MutableSet):
    def __init__(self: _OrderedSet) -> None: ...

    def __contains__(self: _OrderedSet, key: Any) -> bool: ...

    def __iter__(self: _OrderedSet) -> Iterator[_T_co]: ...

    def __len__(self: _OrderedSet) -> int: ...

    def add(self: _OrderedSet, key: Any) -> None: ...

    def discard(self: _OrderedSet, key: Any) -> None: ...


class IgnoredKeywordWarning(UserWarning):
    pass


class ProjectionRegistry(object):
    def __init__(self: ProjectionRegistry) -> None: ...

    def register(self: ProjectionRegistry, , *args) -> None: ...

    def get_projection_class(self: ProjectionRegistry, name: str) -> Any: ...

    def get_projection_names(self: ProjectionRegistry) -> list[SupportsLessThan]: ...


def deprecated(*args, , **kwargs) -> (obj
: Any, message: Optional[str], name: Optional[str], alternative: Optional[str], pending: Optional[bool], obj_type: Optional[str], addendum: Optional[str]) ->


def get_data_path() -> str: ...


def _preprocess_data(func: Optional[{__name__}] = None, replace_names: Any = None, label_namer: Any = None) -> Union[
    partial, (ax: Any, args: tuple[Any, ...], data: Any, kwargs: dict[str, Any]) ->


def _add_data_doc(docstring: str, replace_names: Optional[list[str]]) -> str: ...


def _get_executable_info(name: str) -> tuple: ...


def _check_versions() -> Any: ...


def _rc_params_in_file(fname: Any, transform: Any = lambda x: x, fail_on_error: Any = False) -> RcParams: ...


def _logged_cached(fmt: str, func: Any = None) -> Union[partial, (kwargs: dict[str, Any]) ->


def _ensure_handler() -> StreamHandler: ...


def _get_ssl_context() -> Optional[SSLContext]: ...


def _get_config_or_cache_dir(xdg_base_getter: Union[()) -> str: ...


def _get_xdg_config_dir() -> Optional[str]: ...


def _open_file_or_url(fname: Any) -> Generator[Union[Generator[Any, Any, None], TextIO], Any, None]: ...


def checkdep_usetex(s: Any) -> bool: ...


def _label_from_arg(y: Optional[Any], default_name: Optional[Any]) -> Optional[str]: ...


def _get_xdg_cache_dir() -> Optional[str]: ...


def check_in_list(_values: Any, _print_supported_values: bool = True, , **kwargs) -> Any: ...


def check_isinstance(_types: Any, , **kwargs) -> Any: ...


def check_getitem(_mapping: Any, , **kwargs) -> Any: ...


def warn_external(message: Any, category: Any = None) -> None: ...


def check_shape(_shape: Any, , **kwargs) -> Any: ...


def _get_nonzero_slices(buf: {any}) -> tuple[slice, slice]: ...


def _format_approx(number: Any, precision: Any) -> str: ...


def _str_lower_equal(obj: {lower}, s: Any) -> bool: ...


def _get_data_path(*args, ) -> Path: ...


def _unikey_or_keysym_to_mplkey(unikey: {isprintable}, keysym: {lower}) -> Union[{isprintable}, str]: ...


def _backend_module_name(name: {startswith, lower}) -> str: ...


def _pformat_subprocess(command: Any) -> str: ...


def local_over_kwdict(*args, local_var: Any, kwargs: dict, ) -> Any: ...


def _define_aliases(alias_d: {items}, cls: Optional[{_alias_map}] = None) -> Union[partial, {_alias_map}, None]: ...


def _premultiplied_argb32_to_unmultiplied_rgba8888(buf: Any) -> Any: ...


def _unfold(arr: ndarray, axis: int, size: int, step: int) -> Any: ...


def _weak_or_strong_ref(func: {__self__, __func__}, callback: Union[(proxy: Any, Any, _is_finalizing: ()) -> Union[
    ReferenceType, _StrongRef]: ...


def _to_unmasked_float_array(x: Any) -> ndarray: ...


def _combine_masks(*args, ) -> Union[tuple, list[Union[ndarray, Iterable, int, float, None]]]: ...


def _array_perimeter(arr: ndarray) -> Any: ...


def _lock_path(path: Any) -> Generator: ...


def _setattr_cm(obj: {__dict__}, , **kwargs) -> Generator[Any, Any, None]: ...


def _reshape_2D(X: Union[ndarray, Iterable, int, float], name: str) -> Union[
    list[list], list[object], list[ndarray], list]: ...


def _setup_new_guiapp() -> None: ...


def _topmost_artist(artists: Any, _cached_max: partial[Union[_T1, _T2]] = functools.partial(max,
                                                                                            key=operator.attrgetter(
                                                                                                "zorder"))) -> Union[
    _T1, _T2]: ...


def _get_running_interactive_framework() -> Any: ...


def _check_1d(x: Union[float, ndarray, Iterable, int]) -> Union[ndarray, float, Iterable, int]: ...


def _unmultiplied_rgba8888_to_premultiplied_argb32(rgba8888: Any) -> Any: ...


def _str_equal(obj: {__eq__}, s: Any) -> bool: ...


def get_realpath_and_stat(path: Any) -> tuple[Union[str, bytes], tuple[int, int]]: ...


def _local_over_kwdict(*args, local_var: Any, kwargs: dict,
                       warning_cls: Type[MatplotlibDeprecationWarning] = MatplotlibDeprecationWarning) -> Optional[
    Any]: ...


def _array_patch_perimeters(x: ndarray, rstride: int, cstride: int) -> Any: ...


def _exception_printer(exc: Any) -> Any: ...


def _check_and_log_subprocess(command: Any, logger: {debug}, , **kwargs) -> bytes: ...


def get_projection_class(projection: Any = None) -> Any: ...


def register_projection(cls: Any) -> None: ...


def _replacer(data: Any, value: Any) -> Union[list, list]: ...


def rcdefaults() -> None: ...


def is_url(filename: Any) -> Any: ...


def rc(group: {__iter__}, , **kwargs) -> Any: ...


def rc_context(rc: dict = None, fname: Any = None) -> Generator[Any, Any, None]: ...


def set_loglevel(level: Any) -> None: ...


def warn_deprecated(*args, , **kwargs) -> Optional[Any]: ...


def test(verbosity: Any = None, coverage: bool = False, recursionlimit: int = 0, , **kwargs) -> int: ...