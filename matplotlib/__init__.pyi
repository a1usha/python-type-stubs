from typing import Any
from typing import Callable
from typing import Iterable
from typing import Optional
from typing import Union
from typing import tuple

from numpy.core._multiarray_umath import ndarray


def use(backend: str,
        force: Any = True) -> Any: ...


def get_backend() -> Optional[Any]: ...


def rc_file(fname: Any,
            use_default_template: bool = True) -> None: ...


def rc_file_defaults() -> None: ...


class RcParams(MutableMapping, dict):
    def __init__(self: RcParams,
                 *args,
                 **kwargs) -> None: ...

    def __setitem__(self: RcParams,
                    key: {__eq__},
                    val: Optional[{startswith, endswith}]) -> None: ...

    def __getitem__(self: RcParams,
                    key: {__eq__}) -> Optional[Any]: ...

    def __repr__(self: RcParams) -> str: ...

    def __str__(self: RcParams) -> str: ...

    def __iter__(self: RcParams) -> Generator[SupportsLessThan, Any, None]: ...

    def __len__(self: RcParams) -> int: ...

    def find_all(self: RcParams,
                 pattern: Any) -> RcParams: ...

    def copy(self: RcParams) -> dict: ...


def rc_params(fail_on_error: bool = False) -> RcParams: ...


def rc_params_from_file(fname: Any,
                        fail_on_error: bool = False,
                        use_default_template: bool = True) -> RcParams: ...


def matplotlib_fname() -> str: ...


def interactive(b: Any) -> None: ...


def is_interactive() -> Optional[Any]: ...


@_logged_cached
def get_configdir() -> str: ...


@_logged_cached
def get_cachedir() -> str: ...


class CallbackRegistry(object):
    def __init__(self: CallbackRegistry,
                 exception_handler: Optional[Callable] = _exception_printer) -> None: ...

    def __getstate__(self: CallbackRegistry) -> dict[str, Optional[dict]]: ...

    def __setstate__(self: CallbackRegistry,
                     state: Any) -> None: ...

    @_api.rename_parameter
    def connect(self: CallbackRegistry,
                signal: Any,
                func: {__self__, __func__}) -> int: ...

    def _remove_proxy(self: CallbackRegistry,
                      proxy: Any,
                      _is_finalizing: ()) -> None: ...

    def disconnect(self: CallbackRegistry,
                   cid: Any) -> None: ...

    def process(self: CallbackRegistry,
                s: Any,
                *args,
                **kwargs) -> Any: ...


class Grouper(object):
    def __init__(self: Grouper,
                 init: tuple = ()) -> None: ...

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

    def __iter__(self: Grouper) -> Generator[list, Any, None]: ...

    def get_siblings(self: Grouper,
                     a: Any) -> list: ...


class Stack(object):
    def __init__(self: Stack,
                 default: Any = None) -> None: ...

    def __call__(self: Stack) -> Any: ...

    def __len__(self: Stack) -> int: ...

    def __getitem__(self: Stack,
                    ind: Any) -> list: ...

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


def boxplot_stats(X: Union[ndarray, Iterable, int, float],
                  whis: Any = 1.5,
                  bootstrap: Optional[int] = None,
                  labels: Union[ndarray, Iterable, int, float, None] = None,
                  autorange: Optional[bool] = False) -> Any: ...


def contiguous_regions(mask: Any) -> Union[list, list[tuple[Any, Any]]]: ...


def delete_masked_points(*args,
                         ) -> Union[tuple, list[Union[MaskedArray, ndarray, str]]]: ...


def file_requires_unicode(x: {write}) -> bool: ...


def flatten(seq: {__iter__},
            scalarp: (val: Any)) -> Generator[Optional[Any], Any, None]: ...


def get_sample_data(fname: Any,
                    asfileobj: bool = True,
                    np_load: bool = False) -> Union[
    TextIOWrapper, GzipFile, ndarray, Iterable, int, float, tuple, dict, BinaryIO, TextIO, str]: ...


def index_of(y: Union[float, ndarray, Iterable, int]) -> Any: ...


def is_math_text(s: Any) -> bool: ...


def is_scalar_or_string(val: Any) -> bool: ...


def is_writable_file_like(obj: Any) -> bool: ...


class maxdict(dict):
    def __init__(self: maxdict,
                 maxsize: Any) -> None: ...

    def __setitem__(self: maxdict,
                    k: _KT,
                    v: _VT) -> None: ...


@_api.delete_parameter
@_api.delete_parameter
@_api.delete_parameter
def normalize_kwargs(kw: Optional[dict],
                     alias_mapping: Any = None,
                     required: Optional[Iterable[str]] = (),
                     forbidden: Optional[Iterable[str]] = (),
                     allowed: Optional[Iterable[str]] = None) -> dict: ...


@contextlib.contextmanager
def open_file_cm(path_or_file: Any,
                 mode: str = "r",
                 encoding: Any = None) -> Generator[Any, Any, None]: ...


def print_cycles(objects: {__iter__},
                 outstream: TextIO = sys.stdout,
                 show_progress: bool = False) -> None: ...


def pts_to_midstep(*args,
                   x: Union[ndarray, Iterable, int, float]) -> array.pyi: ...


def pts_to_poststep(*args,
                    x: Union[ndarray, Iterable, int, float]) -> array.pyi: ...


def pts_to_prestep(*args,
                   x: Union[ndarray, Iterable, int, float]) -> array.pyi: ...


def report_memory(i: int = 0) -> int: ...


def safe_first_element(obj: Any) -> Any: ...


def safe_masked_invalid(x: Any,
                        copy: bool = False) -> Union[ndarray, Iterable, int, float, None]: ...


def sanitize_sequence(data: Any) -> Union[list, list]: ...


def sanitize_sequence(data: Any) -> Union[list, list]: ...


def sanitize_sequence(data: Any) -> Union[list, list]: ...


def sanitize_sequence(data: Any) -> Union[list, list]: ...


class silent_list(list):
    def __init__(self: silent_list,
                 type: Any,
                 seq: Any = None) -> None: ...

    def __repr__(self: silent_list) -> str: ...


def simple_linear_interpolation(a: Union[ndarray, Iterable, int, float],
                                steps: int) -> array.pyi: ...


def strip_math(s: {__len__, __getitem__}) -> {__len__, __getitem__}: ...


def to_filehandle(fname: Any,
                  flag: str = 'r',
                  return_opened: bool = False,
                  encoding: Optional[str] = None) -> Any: ...


def to_filehandle(fname: Any,
                  flag: str = 'r',
                  return_opened: bool = False,
                  encoding: Optional[str] = None) -> Any: ...


def violin_stats(X: Union[ndarray, Iterable, int, float],
                 method: Callable,
                 points: int = 100,
                 quantiles: Union[ndarray, Iterable, int, float] = None) -> list[
    dict[str, Union[ndarray, tuple[ndarray, Optional[float]], int, float, complex]]]: ...