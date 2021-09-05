from external.docscrape import NumpyDocString as NumpyDocString
from typing import Any
from typing import ClassVar
from typing import Type
from typing import Union

from object import object
from seaborn._docstrings import DocstringComponents


class DocstringComponents(object):
    regexp: ClassVar[Pattern[str]]
    entries: Union[dict[Any, Union[str, Any]], Any]

    def __init__(self: DocstringComponents,
                 comp_dict: Any,
                 strip_whitespace: bool = True) -> None: ...

    def __getattr__(self: DocstringComponents,
                    attr: Any) -> Union[str, Any]: ...

    def from_nested_components(cls: Type[DocstringComponents],
                               **kwargs) -> DocstringComponents: ...

    def from_function_params(cls: Type[DocstringComponents],
                             func: Any) -> DocstringComponents: ...


_core_params: dict[str, str]
_core_returns: dict[str, str]
_seealso_blurbs: dict[str, str]
_core_docs: dict[str, DocstringComponents]
