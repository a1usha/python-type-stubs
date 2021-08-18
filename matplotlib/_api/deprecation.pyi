from functools import partial
from typing import Any
from typing import Callable
from typing import Generator
from typing import Optional
from typing import Union

from UserWarning import UserWarning
from matplotlib._api.deprecation import _deprecated_parameter_class
from matplotlib._api.deprecation import deprecate_privatize_attribute
from object import object


class MatplotlibDeprecationWarning(UserWarning):
    pass


def _generate_deprecation_warning(since: Union[str, Any],
                                  message: str = '',
                                  name: str = '',
                                  alternative: str = '',
                                  pending: bool = False,
                                  obj_type: str = '',
                                  addendum: str = '',
                                  *,
                                  removal: str = '') -> Union[
    PendingDeprecationWarning, MatplotlibDeprecationWarning]: ...


def warn_deprecated(since: str,
                    *,
                    message: Optional[str] = '',
                    name: Optional[str] = '',
                    alternative: Optional[str] = '',
                    pending: Optional[bool] = False,
                    obj_type: Optional[str] = '',
                    addendum: Optional[str] = '',
                    removal: Optional[str] = '') -> None: ...


def deprecated(since: str,
               *,
               message: Optional[str] = '',
               name: Optional[str] = '',
               alternative: Optional[str] = '',
               pending: Optional[bool] = False,
               obj_type: Optional[str] = None,
               addendum: Optional[str] = '',
               removal: Optional[str] = '') -> Callable[
    [Any, Optional[str], Optional[str], Optional[str], Optional[bool], Optional[str], Optional[str]], Union[
        Union[_deprecated_property, Callable[[Tuple[Any, ...], dict[str, Any]], type]], Any]]: ...


class deprecate_privatize_attribute(object):
    def __init__(self: deprecate_privatize_attribute,
                 *args,
                 **kwargs) -> None: ...

    def __set_name__(self: deprecate_privatize_attribute,
                     owner: Any,
                     name: Any) -> None: ...


def rename_parameter(since: Any,
                     old: Any,
                     new: Any,
                     func: Optional[{__name__}] = None) -> Union[
    partial[Any], Callable[[Tuple[Any, ...], dict[str, Any]], Any]]: ...


class _deprecated_parameter_class(object):
    def __repr__(self: _deprecated_parameter_class) -> str: ...


def delete_parameter(since: Any,
                     name: Any,
                     func: Any = None,
                     **kwargs) -> Union[partial[Any], Callable[[Tuple[Any, ...], dict[str, Any]], Any]]: ...


def make_keyword_only(since: Any,
                      name: Any,
                      func: Optional[{__name__, __signature__}] = None) -> Union[
    partial[Any], Callable[[Tuple[Any, ...], dict[str, Any]], Any]]: ...


def deprecate_method_override(method: {__name__, __get__},
                              obj: Any,
                              *,
                              allow_empty: bool = False,
                              **kwargs) -> Optional[Any]: ...


def suppress_matplotlib_deprecation_warning() -> Union[Generator[Any, Any, None], Any]: ...