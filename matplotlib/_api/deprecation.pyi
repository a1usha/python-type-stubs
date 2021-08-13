from typing import Any
from typing import Optional


class deprecate_privatize_attribute(object):
    def __init__(self: deprecate_privatize_attribute,
                 *args,
                 **kwargs) -> None: ...

    def __set_name__(self: deprecate_privatize_attribute,
                     owner: Any,
                     name: Any) -> None: ...


class MatplotlibDeprecationWarning(UserWarning):
    pass


class _deprecated_parameter_class(object):
    def __repr__(self: _deprecated_parameter_class) -> str: ...


def deprecated(since: str,
               message: Optional[str] = '',
               name: Optional[str] = '',
               alternative: Optional[str] = '',
               pending: Optional[bool] = False,
               obj_type: Optional[str] = None,
               addendum: Optional[str] = '',
               removal: Optional[str] = '') -> (obj
: Any, message: Optional[str], name: Optional[str], alternative: Optional[str], pending: Optional[bool], obj_type: Optional[str], addendum: Optional[str]) ->


@contextlib.contextmanager
def suppress_matplotlib_deprecation_warning() -> Generator[Any, Any, None]: ...


def make_keyword_only(since: Any,
                      name: Any,
                      func: Optional[{__name__, __signature__}] = None) -> Union[
    partial, (args: tuple[Any, ...], kwargs: dict[str, Any]) ->


def rename_parameter(since: Any,
                     old: Any,
                     new: Any,
                     func: Optional[{__name__}] = None) -> Union[
    partial, (args: tuple[Any, ...], kwargs: dict[str, Any]) ->


def delete_parameter(since: Any,
                     name: Any,
                     func: Any = None,
                     **kwargs) -> Union[partial, (inner_args: tuple[Any, ...], inner_kwargs: dict[str, Any]) ->


def deprecate_method_override(method: {__name__, __get__},
                              obj: Any,
                              allow_empty: bool = False,
                              **kwargs) -> Optional[Any]: ...


def _generate_deprecation_warning(since: str,
                                  message: str = '',
                                  name: str = '',
                                  alternative: str = '',
                                  pending: bool = False,
                                  obj_type: str = '',
                                  addendum: str = '',
                                  removal: str = '') -> Union[
    PendingDeprecationWarning, MatplotlibDeprecationWarning]: ...


def warn_deprecated(since: str,
                    message: Optional[str] = '',
                    name: Optional[str] = '',
                    alternative: Optional[str] = '',
                    pending: Optional[bool] = False,
                    obj_type: Optional[str] = '',
                    addendum: Optional[str] = '',
                    removal: Optional[str] = '') -> None: ...