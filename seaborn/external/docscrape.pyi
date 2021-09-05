from collections.abc import Mapping as Mapping
from collections.abc import Callable as Callable
from collections import namedtuple as namedtuple
from warnings import warn as warn
from typing import Any
from typing import Callable
from typing import ClassVar
from typing import Generator
from typing import Iterator
from typing import Mapping
from typing import Optional
from typing import Tuple
from typing import Type
from typing import Union

from Exception import Exception
from object import object
from seaborn.external.docscrape import ClassDoc
from seaborn.external.docscrape import FunctionDoc
from seaborn.external.docscrape import NumpyDocString
from seaborn.external.docscrape import ParseError
from seaborn.external.docscrape import Reader


def strip_blank_lines(l: Union[list[str], Any]) -> Union[list[str], Any]: ...


class Reader(object):
    _l: int
    _str: list[str]

    def __init__(self: Reader,
                 data: str) -> None: ...

    def __getitem__(self: Reader,
                    n: Any) -> Union[str, list[str]]: ...

    def reset(self: Reader) -> None: ...

    def read(self: Reader) -> Union[str, list[str]]: ...

    def seek_next_non_empty_line(self: Reader) -> None: ...

    def eof(self: Reader) -> bool: ...

    def read_to_condition(self: Reader,
                          condition_func: Union[Union[Callable[[{strip}], bool], Callable[
                              [{strip, lstrip, __len__}], Union[bool, Any]]], Any]) -> Union[
        str, list[str], list[Any]]: ...

    def read_to_next_empty_line(self: Reader) -> Union[str, list[str], list[Any]]: ...

    def read_to_next_unindented_line(self: Reader) -> Union[str, list[str], list[Any]]: ...

    def peek(self: Reader,
             n: int = 0) -> Union[str, list[str]]: ...

    def is_empty(self: Reader) -> bool: ...


class ParseError(Exception):
    def __str__(self: ParseError) -> str: ...


Parameter: Type[Parameter]


class NumpyDocString(Mapping):
    sections: ClassVar[dict[Union[str, Any], Union[Union[str, list[str], list[Any]], Any]]]
    _role: ClassVar[str]
    _funcbacktick: ClassVar[str]
    _funcplain: ClassVar[str]
    _funcname: ClassVar[str]
    _funcnamenext: ClassVar[str]
    _funcnamenext: ClassVar[str]
    _description: ClassVar[str]
    _func_rgx: ClassVar[Pattern[str]]
    _line_rgx: ClassVar[Pattern[str]]
    empty_description: ClassVar[str]
    _doc: Reader
    _parsed_data: dict[Union[str, Any], Union[Union[str, list[str], list[Any]], Any]]

    def __init__(self: NumpyDocString,
                 docstring: Union[Optional[str], Any],
                 config: dict[Any, Any] = {}) -> Any: ...

    def __getitem__(self: NumpyDocString,
                    key: Any) -> _VT_co: ...

    def __setitem__(self: NumpyDocString,
                    key: Any,
                    val: Any) -> None: ...

    def __iter__(self: NumpyDocString) -> Iterator[_T_co]: ...

    def __len__(self: NumpyDocString) -> int: ...

    def _is_at_section(self: NumpyDocString) -> bool: ...

    def _strip(self: NumpyDocString,
               doc: Union[Union[str, list[str], list[Any]], Any]) -> Union[Union[str, list[str], list[Any]], Any]: ...

    def _read_to_next_section(self: NumpyDocString) -> Union[str, list[str], list[Any]]: ...

    def _read_sections(self: NumpyDocString) -> Generator[
        Union[Tuple[str, Union[str, list[str], list[Any]]], Type[StopIteration], Tuple[str, Any]], Any, None]: ...

    def _parse_param_list(self: NumpyDocString,
                          content: Any,
                          single_element_is_type: bool = False) -> list[Parameter]: ...

    def _parse_see_also(self: NumpyDocString,
                        content: {__iter__}) -> list[
        Tuple[list[Tuple[Union[str, Any], Union[str, Any]]], list[Any]]]: ...

    def _parse_index(self: NumpyDocString,
                     section: Union[str, Any],
                     content: {__iter__}) -> dict[Union[str, Any], Union[str, list[str]]]: ...

    def _parse_summary(self: NumpyDocString) -> None: ...

    def _parse(self: NumpyDocString) -> Any: ...

    def _error_location(self: NumpyDocString,
                        msg: Union[str, Any],
                        error: bool = True) -> Any: ...

    def _str_header(self: NumpyDocString,
                    name: Union[str, Any],
                    symbol: str = '-') -> list[Union[str, Any]]: ...

    def _str_indent(self: NumpyDocString,
                    doc: Union[list[str], Any],
                    indent: int = 4) -> list[Any]: ...

    def _str_signature(self: NumpyDocString) -> list[str]: ...

    def _str_summary(self: NumpyDocString) -> Union[list[Any], Any]: ...

    def _str_extended_summary(self: NumpyDocString) -> Union[list[Any], Any]: ...

    def _str_param_list(self: NumpyDocString,
                        name: Union[str, Any]) -> list[Any]: ...

    def _str_section(self: NumpyDocString,
                     name: Union[str, Any]) -> list[Any]: ...

    def _str_see_also(self: NumpyDocString,
                      func_role: Union[str, Any]) -> Union[list[Any], Any]: ...

    def _str_index(self: NumpyDocString) -> Union[list[Any], str]: ...

    def __str__(self: NumpyDocString,
                func_role: str = '') -> str: ...


def indent(str: Optional[{split}],
           indent: int = 4) -> str: ...


def dedent_lines(lines: Union[Union[str, list[str], list[Any]], Any]) -> list[str]: ...


def header(text: {__add__, __len__},
           style: str = '-') -> Any: ...


class FunctionDoc(NumpyDocString):
    _role: str
    _f: Any

    def __init__(self: FunctionDoc,
                 func: Any,
                 role: str = 'func',
                 doc: Any = None,
                 config: dict[Any, Any] = {}) -> Any: ...

    def get_func(self: FunctionDoc) -> Tuple[Union[Optional[bool], Any], Union[str, Any]]: ...

    def __str__(self: FunctionDoc) -> str: ...


class ClassDoc(NumpyDocString):
    extra_public_methods: ClassVar[list[str]]
    show_inherited_members: Union[bool, Any]
    _cls: None
    _mod: str

    def __init__(self: ClassDoc,
                 cls: Any,
                 doc: Any = None,
                 modulename: str = '',
                 func_doc: Type[FunctionDoc] = FunctionDoc,
                 config: dict[Any, Any] = {}) -> Any: ...

    def methods(self: ClassDoc) -> Union[list[Any], list[str]]: ...

    def properties(self: ClassDoc) -> Union[list[Any], list[str]]: ...

    def _is_show_member(self: ClassDoc,
                        name: Union[str, Any]) -> bool: ...
