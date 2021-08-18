from pathlib import Path
from typing import Any
from typing import Generator
from typing import Iterable
from typing import Union

from matplotlib import RcParams


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


def update_nested_dict(main_dict: Union[dict[str, RcParams], Any],
                       new_dict: Union[dict[str, RcParams], Any]) -> Union[dict[str, RcParams], Any]: ...


def reload_library() -> None: ...