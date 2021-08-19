from typing import Any

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