from __future__ import absolute_import as absolute_import
from types import ModuleType
from typing import Any
from typing import Callable
from typing import ClassVar
from typing import Optional
from typing import Union

from object import object
from seaborn.external.six import Module_six_moves_urllib
from seaborn.external.six import Module_six_moves_urllib_error
from seaborn.external.six import Module_six_moves_urllib_parse
from seaborn.external.six import Module_six_moves_urllib_request
from seaborn.external.six import Module_six_moves_urllib_response
from seaborn.external.six import Module_six_moves_urllib_robotparser
from seaborn.external.six import MovedAttribute
from seaborn.external.six import MovedModule
from seaborn.external.six import _LazyDescr
from seaborn.external.six import _LazyModule
from seaborn.external.six import _MovedItems
from seaborn.external.six import _SixMetaPathImporter

PY2: bool
PY3: bool
PY34: Union[bool, Any]
__version__: str


def _add_doc(func: Union[Union[Callable[[Any], Any], Callable[[{im_func}], Any], Callable[
    [{keys}, dict[str, Any]], Iterator[Any]], Callable[[{iterkeys}, dict[str, Any]], Any], Callable[
                                   [{values}, dict[str, Any]], Iterator[Any]], Callable[
                                   [{itervalues}, dict[str, Any]], Any], Callable[
                                   [{items}, dict[str, Any]], Iterator[Any]], Callable[
                                   [{iteritems}, dict[str, Any]], Any], Callable[
                                   [{lists}, dict[str, Any]], Iterator[Any]], Callable[
                                   [{iterlists}, dict[str, Any]], Any], Callable[[{encode}], Any], Callable[[Any], Any],
                               Callable[[Any], Any], Callable[[{replace}], Any], Callable[
                                   [Any, Optional[{__traceback__}], Any], Any]], Any],
             doc: Union[str, Any]) -> None: ...


def _import_module(name: Any) -> ModuleType: ...


class _LazyDescr(object):
    name: Any

    def __init__(self: _LazyDescr,
                 name: Any) -> None: ...

    def __get__(self: _LazyDescr,
                obj: {__class__},
                tp: Any) -> Any: ...


class MovedModule(_LazyDescr):
    mod: Any

    def __init__(self: MovedModule,
                 name: Any,
                 old: Any,
                 new: Any = None) -> None: ...

    def _resolve(self: MovedModule) -> ModuleType: ...

    def __getattr__(self: MovedModule,
                    attr: Any) -> Any: ...


class _LazyModule(ModuleType):
    _moved_attributes: ClassVar[list[Any]]

    def __init__(self: _LazyModule,
                 name: str) -> None: ...

    def __dir__(self: _LazyModule) -> list[str]: ...


class MovedAttribute(_LazyDescr):
    mod: Any
    attr: Any

    def __init__(self: MovedAttribute,
                 name: Any,
                 old_mod: Any,
                 new_mod: Any,
                 old_attr: Any = None,
                 new_attr: Any = None) -> None: ...

    def _resolve(self: MovedAttribute) -> Any: ...


class _SixMetaPathImporter(object):
    get_source: ClassVar[Callable[[_SixMetaPathImporter, Any], None]]
    name: Any
    known_modules: dict[Any, Any]

    def __init__(self: _SixMetaPathImporter,
                 six_module_name: Any) -> None: ...

    def _add_module(self: _SixMetaPathImporter,
                    mod: Union[Union[
                                   MovedModule, _MovedItems, Module_six_moves_urllib_parse, Module_six_moves_urllib_error, Module_six_moves_urllib_request, Module_six_moves_urllib_response, Module_six_moves_urllib_robotparser, Module_six_moves_urllib], Any],
                    *args) -> None: ...

    def _get_module(self: _SixMetaPathImporter,
                    fullname: Union[str, Any]) -> Any: ...

    def find_module(self: _SixMetaPathImporter,
                    fullname: Any,
                    path: Any = None) -> Optional[_SixMetaPathImporter]: ...

    def __get_module(self: _SixMetaPathImporter,
                     fullname: Any) -> Any: ...

    def load_module(self: _SixMetaPathImporter,
                    fullname: Any) -> Union[ModuleType, Any]: ...

    def is_package(self: _SixMetaPathImporter,
                   fullname: Any) -> bool: ...

    def get_code(self: _SixMetaPathImporter,
                 fullname: Any) -> None: ...


_importer: _SixMetaPathImporter

_moved_attributes: list[Union[MovedAttribute, Any]]
_moved_attributes: list[Union[MovedAttribute, Any]]
_moved_attributes: list[Union[MovedAttribute, Any]]
_moved_attributes: list[MovedAttribute]
_moved_attributes: list[Union[MovedAttribute, Any]]
_moved_attributes: list[MovedAttribute]
_moved_attributes: list[MovedAttribute]

_moved_attributes: list[Union[MovedAttribute, Any]]
_moved_attributes: list[Union[MovedAttribute, Any]]
_moved_attributes: list[Union[MovedAttribute, Any]]
_moved_attributes: list[MovedAttribute]
_moved_attributes: list[Union[MovedAttribute, Any]]
_moved_attributes: list[MovedAttribute]
_moved_attributes: list[MovedAttribute]

moves: _MovedItems


class _MovedItems(_LazyModule):
    __path__: ClassVar[list[Any]]
    pass


_urllib_parse_moved_attributes: list[Union[MovedAttribute, Any]]

_moved_attributes: list[Union[MovedAttribute, Any]]
_moved_attributes: list[Union[MovedAttribute, Any]]
_moved_attributes: list[Union[MovedAttribute, Any]]
_moved_attributes: list[MovedAttribute]
_moved_attributes: list[Union[MovedAttribute, Any]]
_moved_attributes: list[MovedAttribute]
_moved_attributes: list[MovedAttribute]


class Module_six_moves_urllib_parse(_LazyModule):
    pass


_urllib_error_moved_attributes: list[MovedAttribute]

_moved_attributes: list[Union[MovedAttribute, Any]]
_moved_attributes: list[Union[MovedAttribute, Any]]
_moved_attributes: list[Union[MovedAttribute, Any]]
_moved_attributes: list[MovedAttribute]
_moved_attributes: list[Union[MovedAttribute, Any]]
_moved_attributes: list[MovedAttribute]
_moved_attributes: list[MovedAttribute]


class Module_six_moves_urllib_error(_LazyModule):
    pass


_urllib_request_moved_attributes: list[Union[MovedAttribute, Any]]

_moved_attributes: list[Union[MovedAttribute, Any]]
_moved_attributes: list[Union[MovedAttribute, Any]]
_moved_attributes: list[Union[MovedAttribute, Any]]
_moved_attributes: list[MovedAttribute]
_moved_attributes: list[Union[MovedAttribute, Any]]
_moved_attributes: list[MovedAttribute]
_moved_attributes: list[MovedAttribute]


class Module_six_moves_urllib_request(_LazyModule):
    pass


_urllib_response_moved_attributes: list[MovedAttribute]

_moved_attributes: list[Union[MovedAttribute, Any]]
_moved_attributes: list[Union[MovedAttribute, Any]]
_moved_attributes: list[Union[MovedAttribute, Any]]
_moved_attributes: list[MovedAttribute]
_moved_attributes: list[Union[MovedAttribute, Any]]
_moved_attributes: list[MovedAttribute]
_moved_attributes: list[MovedAttribute]


class Module_six_moves_urllib_response(_LazyModule):
    pass


_urllib_robotparser_moved_attributes: list[MovedAttribute]

_moved_attributes: list[Union[MovedAttribute, Any]]
_moved_attributes: list[Union[MovedAttribute, Any]]
_moved_attributes: list[Union[MovedAttribute, Any]]
_moved_attributes: list[MovedAttribute]
_moved_attributes: list[Union[MovedAttribute, Any]]
_moved_attributes: list[MovedAttribute]
_moved_attributes: list[MovedAttribute]


class Module_six_moves_urllib_robotparser(_LazyModule):
    pass


class Module_six_moves_urllib(ModuleType):
    __path__: ClassVar[list[Any]]
    parse: ClassVar[Any]
    error: ClassVar[Any]
    request: ClassVar[Any]
    response: ClassVar[Any]
    robotparser: ClassVar[Any]

    def __dir__(self: Module_six_moves_urllib) -> list[str]: ...


def add_move(move: {name}) -> None: ...


next: Union[Callable[[Iterator[_T], _VT], Union[_T, _VT]], Callable[[Iterator[_T]], _T], Callable[[{next}], Any]]

get_method_function: Union[attrgetter[Any], attrgetter[tuple[Any, ...]]]

get_method_self: Union[attrgetter[Any], attrgetter[tuple[Any, ...]]]

get_function_closure: Union[attrgetter[Any], attrgetter[tuple[Any, ...]]]

get_function_code: Union[attrgetter[Any], attrgetter[tuple[Any, ...]]]

get_function_defaults: Union[attrgetter[Any], attrgetter[tuple[Any, ...]]]

get_function_globals: Union[attrgetter[Any], attrgetter[tuple[Any, ...]]]


def remove_move(name: Any) -> Any: ...


def assertCountEqual(*args,
                     self: Any,
                     **kwargs) -> Any: ...


def assertRaisesRegex(*args,
                      self: Any,
                      **kwargs) -> Any: ...


print_: Optional[Any]


def assertRegex(*args,
                self: Any,
                **kwargs) -> Any: ...


def with_metaclass(*args,
                   meta: Any) -> metaclass: ...


def add_metaclass(metaclass: Any) -> Callable[[{__dict__, __name__, __bases__}], Any]: ...


__path__: list[Any]

__package__: Any


def python_2_unicode_compatible(klass: Any) -> Any: ...