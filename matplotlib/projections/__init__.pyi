from typing import Any
from typing import Optional
from typing import Union


class ExecutableNotFoundError(FileNotFoundError):
    pass


class ProjectionRegistry(object):
    def __init__(self: ProjectionRegistry) -> None: ...

    def register(self: ProjectionRegistry,
                 *args) -> None: ...

    def get_projection_class(self: ProjectionRegistry,
                             name: str) -> Any: ...

    def get_projection_names(self: ProjectionRegistry) -> list[SupportsLessThan]: ...


@_logged_cached
def get_data_path() -> str: ...


def _preprocess_data(func: Optional[{__name__}] = None,
                     replace_names: Any = None,
                     label_namer: Any = None) -> Union[
    partial, (ax: Any, args: tuple[Any, ...], data: Any, kwargs: dict[str, Any]) ->


def _add_data_doc(docstring: str,
                  replace_names: Optional[list[str]]) -> str: ...


@functools.lru_cache
def _get_executable_info(name: str) -> tuple: ...


def _check_versions() -> Any: ...


def _rc_params_in_file(fname: Any,
                       transform: Any = lambda x: x,
                       fail_on_error: Any = False) -> RcParams: ...


def _logged_cached(fmt: str,
                   func: Any = None) -> Union[partial, (kwargs: dict[str, Any]) ->


@functools.lru_cache
def _ensure_handler() -> StreamHandler: ...


@functools.lru_cache
def _get_ssl_context() -> Optional[SSLContext]: ...


def _get_config_or_cache_dir(xdg_base_getter: Union[()) -> str: ...


def _get_xdg_config_dir() -> Optional[str]: ...


@contextlib.contextmanager
def _open_file_or_url(fname: Any) -> Generator[Union[Generator[Any, Any, None], TextIO], Any, None]: ...


def checkdep_usetex(s: Any) -> bool: ...


def _label_from_arg(y: Optional[Any],
                    default_name: Optional[Any]) -> Optional[str]: ...


def _get_xdg_cache_dir() -> Optional[str]: ...


def check_in_list(_values: Any,
                  _print_supported_values: bool = True,
                  **kwargs) -> Any: ...


def check_isinstance(_types: Any,
                     **kwargs) -> Any: ...


def check_getitem(_mapping: Any,
                  **kwargs) -> Any: ...


def warn_external(message: Any,
                  category: Any = None) -> None: ...


def check_shape(_shape: Any,
                **kwargs) -> Any: ...


def get_projection_class(projection: Any = None) -> Any: ...


def register_projection(cls: Any) -> None: ...


def _replacer(data: Any,
              value: Any) -> Union[list, list]: ...


def rcdefaults() -> None: ...


def is_url(filename: Any) -> Any: ...


def rc(group: {__iter__},
       **kwargs) -> Any: ...


@contextlib.contextmanager
def rc_context(rc: dict = None,
               fname: Any = None) -> Generator[Any, Any, None]: ...


def set_loglevel(level: Any) -> None: ...


@_api.delete_parameter
def test(verbosity: Any = None,
         coverage: bool = False,
         recursionlimit: int = 0,
         **kwargs) -> int: ...