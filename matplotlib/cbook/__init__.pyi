from _weakref import ReferenceType
from functools import partial
from gzip import GzipFile
from io import TextIOWrapper
from pathlib import Path
from typing import Any
from typing import BinaryIO
from typing import Callable
from typing import Generator
from typing import Iterable
from typing import Iterator
from typing import MutableSet
from typing import Optional
from typing import TextIO
from typing import Tuple
from typing import Type
from typing import Union

from UserWarning import UserWarning
from dict import dict
from list import list
from matplotlib import _api
from matplotlib._api.deprecation import MatplotlibDeprecationWarning
from matplotlib.cbook import CallbackRegistry
from matplotlib.cbook import Grouper
from matplotlib.cbook import Stack
from matplotlib.cbook import _OrderedSet
from matplotlib.cbook import _StrongRef
from matplotlib.cbook import maxdict
from matplotlib.cbook import silent_list
from numpy.core._multiarray_umath import ndarray
from object import object


@_api.deprecated("3.4")
def deprecated(*args,
               **kwargs) -> Union[Callable[
                                      [Any, Optional[str], Optional[str], Optional[str], Optional[bool], Optional[str],
                                       Optional[str]], Union[_deprecated_property, Any]], Any]: ...


@_api.deprecated("3.4")
def warn_deprecated(*args,
                    **kwargs) -> Optional[Any]: ...


def _get_running_interactive_framework() -> Any: ...


def _exception_printer(exc: Any) -> Any: ...


class _StrongRef(object):
    def __init__(self: _StrongRef,
                 obj: Any) -> None: ...

    def __call__(self: _StrongRef) -> Any: ...

    def __eq__(self: _StrongRef,
               other: {_obj}) -> bool: ...

    def __hash__(self: _StrongRef) -> int: ...


def _weak_or_strong_ref(func: {__self__, __func__},
                        callback: Union[Union[Callable[[Any, Any, Callable[[], bool]], None], Callable[
                            [Any, Any, Callable[[], bool]], None]], Any]) -> Union[
    Union[ReferenceType, _StrongRef], Any]: ...


class CallbackRegistry(object):
    def __init__(self: CallbackRegistry,
                 exception_handler: Optional[Callable] = _exception_printer) -> None: ...

    def __getstate__(self: CallbackRegistry) -> dict[str, Optional[dict]]: ...

    def __setstate__(self: CallbackRegistry,
                     state: Any) -> None: ...

    @_api.rename_parameter("3.4", "s", "signal")
    def connect(self: CallbackRegistry,
                signal: Any,
                func: {__self__, __func__}) -> Union[int, Any]: ...

    def _remove_proxy(self: CallbackRegistry,
                      proxy: Any,
                      *,
                      _is_finalizing: Callable[[], bool] = sys.is_finalizing) -> None: ...

    def disconnect(self: CallbackRegistry,
                   cid: Any) -> None: ...

    def process(self: CallbackRegistry,
                s: Any,
                *args,
                **kwargs) -> Any: ...


class silent_list(list):
    def __init__(self: silent_list,
                 type: Any,
                 seq: Any = None) -> None: ...

    def __repr__(self: silent_list) -> str: ...


@_api.deprecated("3.3")
class IgnoredKeywordWarning(UserWarning):
    pass


@_api.deprecated("3.3", alternative="normalize_kwargs")
def local_over_kwdict(*args,
                      local_var: Any,
                      kwargs: dict) -> Any: ...


def _local_over_kwdict(*args,
                       local_var: Any,
                       kwargs: Union[dict, Any],
                       warning_cls: Type[MatplotlibDeprecationWarning] = MatplotlibDeprecationWarning) -> Optional[
    Any]: ...


def strip_math(s: {__len__, __getitem__}) -> Union[{__len__, __getitem__}, Any]: ...


def is_writable_file_like(obj: Any) -> bool: ...


def file_requires_unicode(x: {write}) -> bool: ...


def to_filehandle(fname: Any,
                  flag: str = 'r',
                  return_opened: bool = False,
                  encoding: Optional[str] = None) -> Any: ...


def open_file_cm(path_or_file: Any,
                 mode: str = "r",
                 encoding: Any = None) -> Union[Generator[Any, Any, None], Any]: ...


def is_scalar_or_string(val: Any) -> bool: ...


def get_sample_data(fname: Any,
                    asfileobj: bool = True,
                    *,
                    np_load: bool = False) -> Union[
    TextIOWrapper, GzipFile, ndarray, Iterable, int, float, Tuple, dict, BinaryIO, TextIO, str]: ...


def _get_data_path(*args) -> Path: ...


def flatten(seq: {__iter__},
            scalarp: Callable[[Any], bool] = is_scalar_or_string) -> Generator[Optional[Any], Any, None]: ...


@_api.deprecated("3.3", alternative="os.path.realpath and os.stat")
def get_realpath_and_stat(path: Any) -> Union[Tuple[Union[Union[str, bytes], Any], Tuple[int, int]], Any]: ...


class maxdict(dict):
    def __init__(self: maxdict,
                 maxsize: Any) -> None: ...

    def __setitem__(self: maxdict,
                    k: _KT,
                    v: _VT) -> None: ...


class Stack(object):
    def __init__(self: Stack,
                 default: Any = None) -> None: ...

    def __call__(self: Stack) -> Any: ...

    def __len__(self: Stack) -> int: ...

    def __getitem__(self: Stack,
                    ind: Any) -> Union[list[Any], Any]: ...

    def forward(self: Stack) -> Any: ...

    def back(self: Stack) -> Any: ...

    def push(self: Stack,
             o: Any) -> Any: ...

    def home(self: Stack) -> Optional[Any]: ...

    def empty(self: Stack) -> bool: ...

    def clear(self: Stack) -> None: ...

    def bubble(self: Stack,
               o: Any) -> Any: ...

    def remove(self: Stack,
               o: Any) -> Any: ...


def report_memory(i: int = 0) -> int: ...


def safe_masked_invalid(x: Any,
                        copy: bool = False) -> Union[ndarray, Iterable, int, float, None]: ...


def print_cycles(objects: {__iter__},
                 outstream: TextIO = sys.stdout,
                 show_progress: bool = False) -> None: ...


class Grouper(object):
    def __init__(self: Grouper,
                 init: Union[tuple, Any] = ()) -> None: ...

    def __contains__(self: Grouper,
                     item: Any) -> bool: ...

    def clean(self: Grouper) -> None: ...

    def join(self: Grouper,
             a: Any,
             *args) -> None: ...

    def joined(self: Grouper,
               a: Any,
               b: Any) -> Any: ...

    def remove(self: Grouper,
               a: Any) -> None: ...

    def __iter__(self: Grouper) -> Generator[list[Any], Any, None]: ...

    def get_siblings(self: Grouper,
                     a: Any) -> list[Any]: ...


def simple_linear_interpolation(a: Union[ndarray, Iterable, int, float],
                                steps: int) -> array.pyi: ...


def delete_masked_points(*args) -> Union[Tuple, list[Union[Union[MaskedArray, ndarray, str], Any]]]: ...


def _combine_masks(*args) -> Union[Tuple, list[Union[Union[ndarray, Iterable, int, float, None], Any]]]: ...


def boxplot_stats(X: Union[ndarray, Iterable, int, float],
                  whis: Any = 1.5,
                  bootstrap: Optional[int] = None,
                  labels: Union[ndarray, Iterable, int, float, None] = None,
                  autorange: Optional[bool] = False) -> Any: ...


def contiguous_regions(mask: Any) -> Union[list[Any], list[Tuple[Any, Any]]]: ...


def is_math_text(s: Any) -> bool: ...


def _to_unmasked_float_array(x: Any) -> ndarray: ...


def _check_1d(x: Union[Union[float, ndarray, Iterable, int], Any]) -> Union[
    Union[ndarray, float, Iterable, int], Any]: ...


def _reshape_2D(X: Union[Union[ndarray, Iterable, int, float], Any],
                name: Union[str, Any]) -> Union[list[list[Any]], list[Any], list[ndarray]]: ...


def violin_stats(X: Union[ndarray, Iterable, int, float],
                 method: Callable,
                 points: int = 100,
                 quantiles: Union[ndarray, Iterable, int, float] = None) -> list[
    dict[str, Union[Union[ndarray, Tuple[ndarray, Optional[float]], int, float, complex], Any]]]: ...


def pts_to_prestep(*args,
                   x: Union[ndarray, Iterable, int, float]) -> array.pyi: ...


def pts_to_poststep(*args,
                    x: Union[ndarray, Iterable, int, float]) -> array.pyi: ...


def pts_to_midstep(*args,
                   x: Union[ndarray, Iterable, int, float]) -> array.pyi: ...


def index_of(y: Union[float, ndarray, Iterable, int]) -> Any: ...


def safe_first_element(obj: Any) -> Any: ...


def sanitize_sequence(data: Any) -> Union[Union[list[Any], list], Any]: ...


@_api.delete_parameter("3.3", "required")
@_api.delete_parameter("3.3", "forbidden")
@_api.delete_parameter("3.3", "allowed")
def normalize_kwargs(kw: Optional[dict],
                     alias_mapping: Any = None,
                     required: Optional[Iterable[str]] = (),
                     forbidden: Optional[Iterable[str]] = (),
                     allowed: Optional[Iterable[str]] = None) -> Union[dict[Any, Any], Any]: ...


def _lock_path(path: Any) -> Union[Generator[Any, Any, Any], Any]: ...


def _topmost_artist(artists: Any,
                    _cached_max: partial[Union[_T1, _T2]] = functools.partial(max,
                                                                              key=operator.attrgetter("zorder"))) -> \
Union[_T1, _T2]: ...


def _str_equal(obj: {__eq__},
               s: Any) -> Union[bool, Any]: ...


def _str_lower_equal(obj: {lower},
                     s: Any) -> Union[bool, Any]: ...


def _define_aliases(alias_d: {items},
                    cls: Optional[{_alias_map}] = None) -> Union[partial[Any], {_alias_map}, None]: ...


def _array_perimeter(arr: ndarray) -> Any: ...


def _unfold(arr: ndarray,
            axis: int,
            size: int,
            step: int) -> Any: ...


def _array_patch_perimeters(x: ndarray,
                            rstride: int,
                            cstride: int) -> Any: ...


def _setattr_cm(obj: {__dict__},
                **kwargs) -> Union[Generator[Any, Any, None], Any]: ...


class _OrderedSet(MutableSet):
    def __init__(self: _OrderedSet) -> None: ...

    def __contains__(self: _OrderedSet,
                     key: Any) -> bool: ...

    def __iter__(self: _OrderedSet) -> Iterator[_T_co]: ...

    def __len__(self: _OrderedSet) -> int: ...

    def add(self: _OrderedSet,
            key: Any) -> None: ...

    def discard(self: _OrderedSet,
                key: Any) -> None: ...


def _premultiplied_argb32_to_unmultiplied_rgba8888(buf: Any) -> Any: ...


def _unmultiplied_rgba8888_to_premultiplied_argb32(rgba8888: Any) -> Any: ...


def _get_nonzero_slices(buf: {any}) -> Tuple[slice, slice]: ...


def _pformat_subprocess(command: Any) -> str: ...


def _check_and_log_subprocess(command: Any,
                              logger: {debug},
                              **kwargs) -> bytes: ...


def _backend_module_name(name: {startswith, lower}) -> Union[str, Any]: ...


def _setup_new_guiapp() -> None: ...


def _format_approx(number: Any,
                   precision: Any) -> str: ...


def _unikey_or_keysym_to_mplkey(unikey: {isprintable},
                                keysym: {lower}) -> Union[Union[{isprintable}, str], Any]: ...