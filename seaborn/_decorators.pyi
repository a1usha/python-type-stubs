from functools import wraps as wraps
from inspect import Parameter as Parameter
from inspect import signature as signature
from typing import Any
from typing import Callable


def _deprecate_positional_args(f: function) -> Callable[[Tuple[Any, ...], dict[str, Any]], Any]: ...


def share_init_params_with_map(cls: {map, __init__}) -> {map, __init__}: ...