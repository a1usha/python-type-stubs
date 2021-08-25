from matplotlib.backends.qt_compat import QtCore as QtCore
from matplotlib.backends.qt_compat import QtWidgets as QtWidgets
from matplotlib.backends.qt_compat import QtGui as QtGui
from matplotlib import colors as mcolors
from matplotlib import _api as _api
from numbers import Real as Real
from numbers import Integral as Integral
from typing import Callable
from typing import ClassVar
from typing import Optional
from typing import Tuple
from typing import Union

from matplotlib.backends.qt_editor._formlayout import ColorButton
from matplotlib.backends.qt_editor._formlayout import ColorLayout
from matplotlib.backends.qt_editor._formlayout import FontLayout
from matplotlib.backends.qt_editor._formlayout import FormComboWidget
from matplotlib.backends.qt_editor._formlayout import FormDialog
from matplotlib.backends.qt_editor._formlayout import FormTabWidget
from matplotlib.backends.qt_editor._formlayout import FormWidget

__version__: str
__license__: Optional[str]
_log: Logger
BLACKLIST: set[str]
from typing import Any


class ColorButton():
    colorChanged: ClassVar[Any]
    color: ClassVar[Any]
    _color: Any

    def __init__(self: ColorButton,
                 parent: Any = None) -> None: ...

    def choose_color(self: ColorButton) -> None: ...

    def get_color(self: ColorButton) -> Any: ...

    def set_color(self: ColorButton,
                  color: {__ne__}) -> Optional[Any]: ...


def to_qcolor(color: Any) -> Any: ...


class ColorLayout():
    colorbtn: ColorButton
    lineedit: Any

    def __init__(self: ColorLayout,
                 color: {getRgbF},
                 parent: Any = None) -> None: ...

    def update_color(self: ColorLayout) -> None: ...

    def update_text(self: ColorLayout,
                    color: {getRgbF}) -> None: ...

    def text(self: ColorLayout) -> Any: ...


def font_is_installed(font: Any) -> list[Any]: ...


def tuple_to_qfont(tup: {__len__, __getitem__}) -> Optional[Any]: ...


def qfont_to_tuple(font: {family, pointSize, italic, bold}) -> Tuple[str, int, Any, Any]: ...


class FontLayout():
    size: Any
    bold: Any
    family: Any
    italic: Any

    def __init__(self: FontLayout,
                 value: {__len__, __getitem__},
                 parent: Any = None) -> None: ...

    def get_font(self: FontLayout) -> Tuple[str, int, Any, Any]: ...


def is_edit_valid(edit: {text, validator}) -> bool: ...


class FormWidget():
    update_buttons: ClassVar[Any]
    data: Any
    formlayout: Any
    widgets: list[Any]

    def __init__(self: FormWidget,
                 data: Any,
                 comment: Optional[str] = "",
                 with_margin: bool = False,
                 parent: Optional[Any] = None) -> None: ...

    def get_dialog(self: FormWidget) -> Any: ...

    def setup(self: FormWidget) -> None: ...

    def get(self: FormWidget) -> list[Union[Union[float, int, bool, str], Any]]: ...


class FormComboWidget():
    update_buttons: ClassVar[Any]
    stackwidget: Any
    widgetlist: list[FormWidget]
    combobox: Any

    def __init__(self: FormComboWidget,
                 datalist: {__iter__},
                 comment: str = "",
                 parent: Any = None) -> None: ...

    def setup(self: FormComboWidget) -> None: ...

    def get(self: FormComboWidget) -> list[list[Union[Union[float, int, bool, str], Any]]]: ...


class FormTabWidget():
    update_buttons: ClassVar[Any]
    tabwidget: Any
    widgetlist: list[Union[FormComboWidget, FormWidget]]

    def __init__(self: FormTabWidget,
                 datalist: {__iter__},
                 comment: str = "",
                 parent: Any = None) -> None: ...

    def setup(self: FormTabWidget) -> None: ...

    def get(self: FormTabWidget) -> list[Union[
        list[list[Union[Union[float, int, bool, str], Any]]], list[Union[Union[float, int, bool, str], Any]]]]: ...


class FormDialog():
    apply_callback: Any
    data: list[Union[Union[float, int, bool, str], Any]]
    bbox: Any
    formwidget: FormWidget
    float_fields: list[Any]

    def __init__(self: FormDialog,
                 data: {__getitem__},
                 title: str = "",
                 comment: str = "",
                 icon: Any = None,
                 parent: Any = None,
                 apply: Any = None) -> None: ...

    def register_float_field(self: FormDialog,
                             field: Any) -> None: ...

    def update_buttons(self: FormDialog) -> None: ...

    def accept(self: FormDialog) -> None: ...

    def reject(self: FormDialog) -> None: ...

    def apply(self: FormDialog) -> None: ...

    def get(self: FormDialog) -> list[Union[Union[float, int, bool, str], Any]]: ...


def fedit(data: Union[Union[list[Union[Union[tuple[str, str], tuple[str, list[Union[int, str]]], tuple[
    str, list[Union[str, tuple[str, str]]]], tuple[str, float], tuple[None, str], tuple[str, int], tuple[
                                                 str, tuple[str, int, bool, bool]], tuple[str, bool], tuple[
                                                 str, date]], Any]], tuple[tuple[list[Union[Union[
                                                                                                tuple[str, str], tuple[
                                                                                                    str, list[Union[
                                                                                                        int, str]]],
                                                                                                tuple[str, list[Union[
                                                                                                    str, tuple[
                                                                                                        str, str]]]],
                                                                                                tuple[str, float],
                                                                                                tuple[None, str], tuple[
                                                                                                    str, int], tuple[
                                                                                                    str, tuple[
                                                                                                        str, int, bool, bool]],
                                                                                                tuple[str, bool], tuple[
                                                                                                    str, date]], Any]], str, str],
                                                                           tuple[list[Union[Union[
                                                                                                tuple[str, str], tuple[
                                                                                                    str, list[Union[
                                                                                                        int, str]]],
                                                                                                tuple[str, list[Union[
                                                                                                    str, tuple[
                                                                                                        str, str]]]],
                                                                                                tuple[str, float],
                                                                                                tuple[None, str], tuple[
                                                                                                    str, int], tuple[
                                                                                                    str, tuple[
                                                                                                        str, int, bool, bool]],
                                                                                                tuple[str, bool], tuple[
                                                                                                    str, date]], Any]], str, str],
                                                                           tuple[list[Union[Union[
                                                                                                tuple[str, str], tuple[
                                                                                                    str, list[Union[
                                                                                                        int, str]]],
                                                                                                tuple[str, list[Union[
                                                                                                    str, tuple[
                                                                                                        str, str]]]],
                                                                                                tuple[str, float],
                                                                                                tuple[None, str], tuple[
                                                                                                    str, int], tuple[
                                                                                                    str, tuple[
                                                                                                        str, int, bool, bool]],
                                                                                                tuple[str, bool], tuple[
                                                                                                    str, date]], Any]], str, str]],
                            tuple[tuple[tuple[tuple[list[Union[Union[tuple[str, str], tuple[str, list[Union[int, str]]],
                                                                     tuple[str, list[Union[str, tuple[str, str]]]],
                                                                     tuple[str, float], tuple[None, str], tuple[
                                                                         str, int], tuple[
                                                                         str, tuple[str, int, bool, bool]], tuple[
                                                                         str, bool], tuple[
                                                                         str, date]], Any]], str, str], tuple[list[
                                                                                                                  Union[
                                                                                                                      Union[
                                                                                                                          tuple[
                                                                                                                              str, str],
                                                                                                                          tuple[
                                                                                                                              str,
                                                                                                                              list[
                                                                                                                                  Union[
                                                                                                                                      int, str]]],
                                                                                                                          tuple[
                                                                                                                              str,
                                                                                                                              list[
                                                                                                                                  Union[
                                                                                                                                      str,
                                                                                                                                      tuple[
                                                                                                                                          str, str]]]],
                                                                                                                          tuple[
                                                                                                                              str, float],
                                                                                                                          tuple[
                                                                                                                              None, str],
                                                                                                                          tuple[
                                                                                                                              str, int],
                                                                                                                          tuple[
                                                                                                                              str,
                                                                                                                              tuple[
                                                                                                                                  str, int, bool, bool]],
                                                                                                                          tuple[
                                                                                                                              str, bool],
                                                                                                                          tuple[
                                                                                                                              str, date]], Any]], str, str],
                                              tuple[list[Union[Union[tuple[str, str], tuple[str, list[Union[int, str]]],
                                                                     tuple[str, list[Union[str, tuple[str, str]]]],
                                                                     tuple[str, float], tuple[None, str], tuple[
                                                                         str, int], tuple[
                                                                         str, tuple[str, int, bool, bool]], tuple[
                                                                         str, bool], tuple[
                                                                         str, date]], Any]], str, str]], str, str],
                                  tuple[list[Union[Union[tuple[str, str], tuple[str, list[Union[int, str]]], tuple[
                                      str, list[Union[str, tuple[str, str]]]], tuple[str, float], tuple[None, str],
                                                         tuple[str, int], tuple[str, tuple[str, int, bool, bool]],
                                                         tuple[str, bool], tuple[str, date]], Any]], str, str], tuple[
                                      list[Union[Union[tuple[str, str], tuple[str, list[Union[int, str]]], tuple[
                                          str, list[Union[str, tuple[str, str]]]], tuple[str, float], tuple[None, str],
                                                       tuple[str, int], tuple[str, tuple[str, int, bool, bool]], tuple[
                                                           str, bool], tuple[str, date]], Any]], str, str]]], Any],
          title: str = "",
          comment: str = "",
          icon: Any = None,
          parent: Any = None,
          apply: Union[Callable[[Any], None], Any] = None) -> list[Union[Union[float, int, bool, str], Any]]: ...