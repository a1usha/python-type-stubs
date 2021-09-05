from _version import get_versions as get_versions
from matplotlib.rcsetup import cycler as cycler
from matplotlib.rcsetup import validate_backend as validate_backend
from matplotlib.cbook import mplDeprecation as mplDeprecation
from matplotlib.cbook import sanitize_sequence as sanitize_sequence
from matplotlib.cbook import MatplotlibDeprecationWarning as MatplotlibDeprecationWarning
from matplotlib import rcsetup as rcsetup
from matplotlib import docstring as docstring
from matplotlib import cbook as cbook
from matplotlib import _api as _api
from pathlib import Path as Path
from inspect import Parameter as Parameter
from distutils.version import LooseVersion as LooseVersion
from collections.abc import MutableMapping as MutableMapping
from collections import namedtuple as namedtuple
from functools import partial
from logging import StreamHandler
from ssl import SSLContext
from typing import Any
from typing import Callable
from typing import ClassVar
from typing import Generator
from typing import MutableMapping
from typing import Optional
from typing import Tuple
from typing import Union

from FileNotFoundError import FileNotFoundError
from dict import dict
from matplotlib import RcParams
from matplotlib import _api

__bibtex__: str
__version__: str


def _check_versions() -> Any: ...


def _ensure_handler() -> StreamHandler[_StreamT]: ...


def set_loglevel(level: Any) -> None: ...


_ExecInfo: Type[_ExecInfo]


def _logged_cached(fmt: Union[str, Any],
                   func: Any = None) -> Union[partial[Any], Callable[[dict[str, Any]], Any]]: ...


class ExecutableNotFoundError(FileNotFoundError):
    pass


def _get_executable_info(name: str) -> Tuple: ...


def checkdep_usetex(s: Any) -> bool: ...


def _get_xdg_config_dir() -> Optional[str]: ...


def _get_xdg_cache_dir() -> Optional[str]: ...


def _get_config_or_cache_dir(
        xdg_base_getter: Union[Union[Callable[[], Optional[str]], Callable[[], Optional[str]]], Any]) -> str: ...


def get_configdir() -> Union[str, Any]: ...


def get_cachedir() -> Union[str, Any]: ...


def get_data_path() -> Union[str, Any]: ...


_deprecated_map: dict[str, Optional[str]]

_deprecated_ignore_map: dict[str, Union[tuple[str, None], str, None]]

_deprecated_remain_as_none: dict[str, Union[tuple[str], str, None]]

_all_deprecated: set[Any]


def matplotlib_fname() -> str: ...


class RcParams(MutableMapping, dict):
    validate: ClassVar[Union[dict, dict[Union[str, Any], Union[Union[Callable[[{startswith, endswith}], Union[
        {startswith, endswith}, Any]], Callable[[Any], bool], Callable[[Any], Any], Callable[
                                                                         [Optional[{lower}]], Optional[Any]]], Any]]]]

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

    def __iter__(self: RcParams) -> Generator[Union[SupportsLessThan, Any], Any, None]: ...

    def __len__(self: RcParams) -> int: ...

    def find_all(self: RcParams,
                 pattern: Any) -> RcParams: ...

    def copy(self: RcParams) -> dict: ...


URL_REGEX: Pattern[str]


def rc_params(fail_on_error: bool = False) -> RcParams: ...


def is_url(filename: Any) -> Any: ...


def _get_ssl_context() -> Optional[SSLContext]: ...


def _open_file_or_url(fname: Any) -> Union[Generator[Union[Generator[Any, Any, None], TextIO], Any, None], Any]: ...


def _rc_params_in_file(fname: Any,
                       transform: Any = lambda x: x,
                       fail_on_error: Any = False) -> RcParams: ...


rcParamsDefault: RcParams

rcParams: RcParams


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
               fname: Any = None) -> Union[Generator[Any, Any, None], Any]: ...


def use(backend: str,
        *,
        force: Any = True) -> Any: ...


def get_backend() -> Optional[Any]: ...


def interactive(b: Any) -> None: ...


default_test_modules: list[str]


def is_interactive() -> Optional[Any]: ...


__test__: bool


@_api.delete_parameter("3.3", "recursionlimit")
def test(verbosity: Any = None,
         coverage: bool = False,
         *,
         recursionlimit: int = 0,
         **kwargs) -> Union[int, Any]: ...


def _replacer(data: Any,
              value: Any) -> Union[Union[list[Any], list], Any]: ...


_DATA_DOC_TITLE: str

_DATA_DOC_APPENDIX: str


def _label_from_arg(y: Optional[Any],
                    default_name: Optional[Any]) -> Union[Optional[str], Any]: ...


def _add_data_doc(docstring: str,
                  replace_names: Optional[list[str]]) -> str: ...


def _preprocess_data(func: Optional[{__name__}] = None,
                     *,
                     replace_names: Any = None,
                     label_namer: Any = None) -> Union[
    partial[Any], Callable[[Any, Tuple[Any, ...], Any, dict[str, Any]], Any]]: ...