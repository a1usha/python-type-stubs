from deprecation import MatplotlibDeprecationWarning as MatplotlibDeprecationWarning
from deprecation import suppress_matplotlib_deprecation_warning as suppress_matplotlib_deprecation_warning
from deprecation import deprecate_privatize_attribute as deprecate_privatize_attribute
from deprecation import deprecate_method_override as deprecate_method_override
from deprecation import make_keyword_only as make_keyword_only
from deprecation import delete_parameter as delete_parameter
from deprecation import rename_parameter as rename_parameter
from deprecation import warn_deprecated as warn_deprecated
from deprecation import deprecated as deprecated
from typing import Any

from matplotlib._api import classproperty
from object import object


class classproperty(object):
    _fget: Any
    _doc: Any
    fdel: None
    fset: None

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