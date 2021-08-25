from matplotlib import rcParamsDefault as rcParamsDefault
from matplotlib import rc_params_from_file as rc_params_from_file
from matplotlib import _api as _api
from pathlib import Path as Path
from pathlib import Path
from typing import Any
from typing import Generator
from typing import Iterable
from typing import Union

from matplotlib import RcParams

_log: Logger
__all__: Any
BASE_LIBRARY_PATH: str
USER_LIBRARY_PATHS: list[str]
STYLE_EXTENSION: str
STYLE_FILE_PATTERN: Pattern[str]
STYLE_BLACKLIST: set[Union[str, Any]]
from typing import Any


def _remove_blacklisted_style_params(d: Union[Union[str, Path, RcParams], Any],
                                     warn: bool = True) -> dict[
    Union[Union[str, SupportsLessThan], Any], Union[Optional[str], Any]]: ...


def _apply_style(d: Union[Union[str, Path, RcParams], Any],
                 warn: bool = True) -> None: ...


def use(style: Union[str, dict, Path, Iterable]) -> Any: ...


def context(style: Union[str, dict, Path, Iterable],
            after_reset: bool = False) -> Union[Generator[Any, Any, None], Any]: ...


def load_base_library() -> dict[str, RcParams]: ...


def iter_user_libraries() -> Generator[str, Any, None]: ...


def update_user_library(library: Union[dict[str, RcParams], Any]) -> Union[dict[str, RcParams], Any]: ...


def read_style_directory(style_dir: Union[str, Any]) -> dict[str, RcParams]: ...


_base_library: dict[str, RcParams]

library: None

available: list[Any]


def update_nested_dict(main_dict: Union[dict[str, RcParams], Any],
                       new_dict: Union[dict[str, RcParams], Any]) -> Union[dict[str, RcParams], Any]: ...


def reload_library() -> None: ...