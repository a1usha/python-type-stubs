from typing import Any
from typing import Callable
from typing import Optional
from typing import Union


def bootstrap(*args,
              **kwargs) -> array.pyi: ...


def _structured_bootstrap(args: Union[list[Any], Any],
                          n_boot: Union[int, Any],
                          units: Optional[Any],
                          func: Union[Union[Callable[[Any], Any], Callable[
                              [Union[Union[Iterable, int, float], Any], Union[None, int, Iterable, tuple[int]],
                               Optional[object], Any, Optional[bool], Any,
                               Union[Union[Iterable, int, float[bool], None], Any]], Any]], Any],
                          func_kwargs: Union[Union[dict[Any, Any], dict[Any, Optional[Any]]], Any],
                          integers: Any) -> Any: ...


def _handle_random_seed(seed: Any = None) -> Any: ...