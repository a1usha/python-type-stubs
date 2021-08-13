from typing import Any
from typing import Type

from matplotlib.axes._axes import Axes
from matplotlib.gridspec import SubplotSpec


class SubplotBase(object):
    def __init__(self: SubplotBase,
                 fig: Figure,
                 *args,
                 **kwargs) -> None: ...

    def __reduce__(self: SubplotBase) -> tuple[(axes_class: Any) ->

    @_api.deprecated(
        "3.4", alternative="get_subplotspec",
        addendum="(get_subplotspec returns a SubplotSpec instance.)")
    def get_geometry(self: SubplotBase) -> tuple[Any, Any, int]: ...

    @_api.deprecated("3.4", alternative="set_subplotspec")
    def change_geometry(self: SubplotBase,
                        numrows: Any,
                        numcols: Any,
                        num: {__sub__}) -> Optional[Any]: ...

    def get_subplotspec(self: SubplotBase) -> SubplotSpec: ...

    def set_subplotspec(self: SubplotBase,
                        subplotspec: SubplotSpec) -> None: ...

    def get_gridspec(self: SubplotBase) -> Any: ...

    @_api.deprecated(
        "3.4", alternative="get_subplotspec().get_position(self.figure)")
    @property
    def figbox(self: SubplotBase) -> Union[tuple[Bbox, Any, Any, Any, Any], Bbox]: ...

    @_api.deprecated("3.4", alternative="get_gridspec().nrows")
    @property
    def numRows(self: SubplotBase) -> Any: ...

    @_api.deprecated("3.4", alternative="get_gridspec().ncols")
    @property
    def numCols(self: SubplotBase) -> Any: ...

    @_api.deprecated("3.4")
    def update_params(self: SubplotBase) -> Optional[Any]: ...

    @_api.deprecated("3.4", alternative="ax.get_subplotspec().is_first_row()")
    def is_first_row(self: SubplotBase) -> bool: ...

    @_api.deprecated("3.4", alternative="ax.get_subplotspec().is_last_row()")
    def is_last_row(self: SubplotBase) -> bool: ...

    @_api.deprecated("3.4", alternative="ax.get_subplotspec().is_first_col()")
    def is_first_col(self: SubplotBase) -> bool: ...

    @_api.deprecated("3.4", alternative="ax.get_subplotspec().is_last_col()")
    def is_last_col(self: SubplotBase) -> bool: ...

    def label_outer(self: SubplotBase) -> None: ...

    def _make_twin_axes(self: SubplotBase,
                        *args,
                        **kwargs) -> Any: ...


@functools.lru_cache(None)
def subplot_class_factory(axes_class: Type[Axes] = None) -> Union[Type[SubplotBase], type]: ...


def _picklable_subplot_class_constructor(axes_class: Any) -> object: ...