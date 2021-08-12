from typing import Union
from matplotlib import RcParams
from pathlib import Path
from typing import Any
from typing import Union
from matplotlib import RcParams
from pathlib import Path
from typing import Any
from typing import Any
from typing import Any
from typing import Any
from typing import Any
from typing import Union
from typing import Iterable
from pathlib import Path
from typing import Union
from typing import Iterable
from pathlib import Path


def context(style: Union[str, dict, Path, Iterable], after_reset: bool = False) -> Generator[Any, Any, None]: ...


def reload_library() -> None: ...


def use(style: Union[str, dict, Path, Iterable]) -> Any: ...


def update_user_library(library: dict[str, RcParams]) -> dict[str, RcParams]: ...


def read_style_directory(style_dir: str) -> dict[str, RcParams]: ...


def iter_user_libraries() -> Generator[str, Any, None]: ...


def update_nested_dict(main_dict: dict[str, RcParams], new_dict: dict[str, RcParams]) -> dict[str, RcParams]: ...


def load_base_library() -> dict[str, RcParams]: ...


def _remove_blacklisted_style_params(d: Union[str, Path, RcParams], warn: bool = True) -> dict[
    Union[str, SupportsLessThan], Optional[str]]: ...


def _apply_style(d: Union[str, Path, RcParams], warn: bool = True) -> None: ...