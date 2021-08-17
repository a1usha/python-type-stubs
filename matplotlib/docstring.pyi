from typing import Any
from typing import Type

from matplotlib import _api
from matplotlib.docstring import Substitution
from object import object


class Substitution(object):
    def __init__(self: Substitution,
                 *args,
                 **kwargs) -> Any: ...

    def __call__(self: Substitution,
                 func: {__doc__}) -> {__doc__}: ...

    def update(self: Substitution,
               *args,
               **kwargs) -> None: ...

    @_api.deprecated("3.3", alternative="assign to the params attribute")
    def from_params(cls: Type[Substitution],
                    params: Any) -> Substitution: ...


def copy(source: Any) -> (target: Any) ->