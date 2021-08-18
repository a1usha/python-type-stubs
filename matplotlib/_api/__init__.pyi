from functools import partial
from logging import StreamHandler
from ssl import SSLContext
from typing import Generator
from typing import MutableMapping
from typing import Optional
from typing import Tuple
from typing import Union

from FileNotFoundError import FileNotFoundError
from dict import dict
from matplotlib import RcParams
from matplotlib import _api
from matplotlib._api import classproperty
from object import object


class classproperty(object):
    def __init__(self: classproperty,
                 fget: Any,
                 fset: Any = None,
                 fdel: Any = None,
                 doc: Any = None) -> Any: ...

    def __get__(self: classproperty,
                instance: Any,
                owner: Any) -> Any: ...

    def fget(self: classproperty) -> Any: ...


def check_isinstance(_types: Any,
                     **kwargs) -> Any: ...


def check_in_list(_values: Any,
                  *,
                  _print_supported_values: bool = True,
                  **kwargs) -> Any: ...


def check_shape(_shape: Any,
                **kwargs) -> Any: ...


def check_getitem(_mapping: Any,
                  **kwargs) -> Any: ...


def warn_external(message: Any,
                  category: Any = None) -> None: ...


def _check_versions() -> Any: ...


def _ensure_handler() -> StreamHandler: ...


def set_loglevel(level: Any) -> None: ...


def _logged_cached(fmt: str,
                   func: Any = None) -> Union[partial, (kwargs: dict[str, Any]) ->


class ExecutableNotFoundError(FileNotFoundError):
    pass


def _get_executable_info(name: str) -> Tuple: ...


def checkdep_usetex(s: Any) -> bool: ...


def _get_xdg_config_dir() -> Optional[str]: ...


def _get_xdg_cache_dir() -> Optional[str]: ...


def _get_config_or_cache_dir(xdg_base_getter: Union[()) -> str: ...


def get_configdir() -> str: ...


def get_cachedir() -> str: ...


def get_data_path() -> str: ...


def matplotlib_fname() -> str: ...


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


def is_url(filename: Any) -> Any: ...


def _get_ssl_context() -> Optional[SSLContext]: ...


def _open_file_or_url(fname: Any) -> Generator[Union[Generator[Any, Any, None], TextIO], Any, None]: ...


def _rc_params_in_file(fname: Any,
                       transform: Any = lambda x: x,
                       fail_on_error: Any = False) -> RcParams: ...


def rc_params_from_file(fname: Any,
                        fail_on_error: bool = False,
                        use_default_template: bool = True) -> RcParams: ...


def rc(group: {__iter__},
       **kwargs) -> Any: ...


def rcdefaults() -> None: ...


def rc_file_defaults() -> None: ...


def rc_file(fname: Any,
            *,
            use_default_template: bool = True) -> None: ...


def rc_context(rc: dict = None,
               fname: Any = None) -> Generator[Any, Any, None]: ...


def use(backend: str,
        *,
        force: Any = True) -> Any: ...


def get_backend() -> Optional[Any]: ...


def interactive(b: Any) -> None: ...


def is_interactive() -> Optional[Any]: ...


@_api.delete_parameter("3.3", "recursionlimit")
def test(verbosity: Any = None,
         coverage: bool = False,
         *,
         recursionlimit: int = 0,
         **kwargs) -> int: ...


def _replacer(data: Any,
              value: Any) -> Union[list, list]: ...


def _label_from_arg(y: Optional[Any],
                    default_name: Optional[Any]) -> Optional[str]: ...


def _add_data_doc(docstring: str,
                  replace_names: Optional[list[str]]) -> str: ...


def _preprocess_data(func: Optional[{__name__}] = None,
                     *,
                     replace_names: Any = None,
                     label_namer: Any = None) -> Union[
    partial, (ax: Any, args: Tuple[Any, ...], data: Any, kwargs: dict[str, Any]) ->