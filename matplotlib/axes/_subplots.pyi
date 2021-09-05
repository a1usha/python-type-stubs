from matplotlib.gridspec import SubplotSpec as SubplotSpec
from matplotlib.gridspec import GridSpec as GridSpec
from matplotlib.axes._axes import Axes as Axes
from matplotlib import docstring as docstring
from matplotlib import _api as _api
from typing import Any
from typing import Optional
from typing import Tuple
from typing import Type
from typing import Union

from matplotlib import _api
from matplotlib.axes._axes import Axes
from matplotlib.axes._subplots import SubplotBase
from matplotlib.figure import Figure
from matplotlib.gridspec import SubplotSpec
from object import object


class SubplotBase(object):
    _subplotspec: SubplotSpec

    def __init__(self: SubplotBase,
                 fig: Figure,
                 *args,
                 **kwargs) -> None: ...

    def __reduce__(self: SubplotBase) -> Tuple[
        Callable[[Any], Union[object, Any]], Tuple[Union[Type[Axes], type]], Any]: ...

    @_api.deprecated(
        "3.4", alternative="get_subplotspec",
        addendum="(get_subplotspec returns a SubplotSpec instance.)")
    def get_geometry(self: SubplotBase) -> Union[Tuple[Any, Any, int], Any]: ...

    @_api.deprecated("3.4", alternative="set_subplotspec")
    def change_geometry(self: SubplotBase,
                        numrows: Any,
                        numcols: Any,
                        num: {__sub__}) -> Optional[Any]: ...

    def get_subplotspec(self: SubplotBase) -> SubplotSpec: ...

    def set_subplotspec(self: SubplotBase,
                        subplotspec: Union[SubplotSpec, Any]) -> None: ...

    def get_gridspec(self: SubplotBase) -> Any: ...

    @_api.deprecated(
        "3.4", alternative="get_position()")
    def figbox(self: SubplotBase) -> Any: ...

    @_api.deprecated("3.4", alternative="get_gridspec().nrows")
    def numRows(self: SubplotBase) -> Any: ...

    @_api.deprecated("3.4", alternative="get_gridspec().ncols")
    def numCols(self: SubplotBase) -> Any: ...

    @_api.deprecated("3.4")
    def update_params(self: SubplotBase) -> Optional[Any]: ...

    @_api.deprecated("3.4", alternative="ax.get_subplotspec().is_first_row()")
    def is_first_row(self: SubplotBase) -> Union[bool, Any]: ...

    @_api.deprecated("3.4", alternative="ax.get_subplotspec().is_last_row()")
    def is_last_row(self: SubplotBase) -> Union[bool, Any]: ...

    @_api.deprecated("3.4", alternative="ax.get_subplotspec().is_first_col()")
    def is_first_col(self: SubplotBase) -> Union[bool, Any]: ...

    @_api.deprecated("3.4", alternative="ax.get_subplotspec().is_last_col()")
    def is_last_col(self: SubplotBase) -> Union[bool, Any]: ...

    def label_outer(self: SubplotBase) -> None: ...

    def _make_twin_axes(self: SubplotBase,
                        *args,
                        **kwargs) -> Any: ...


_subplot_classes: dict[Any, Any]

Subplot: Union[Type[SubplotBase], type]


def subplot_class_factory(axes_class: Union[Type[Axes], Any] = None) -> Union[Type[SubplotBase], type]: ...


def _picklable_subplot_class_constructor(axes_class: Any) -> Union[object, Any]: ...