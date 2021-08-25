from matplotlib.backends.qt_compat import QtWidgets as QtWidgets
from typing import Any

from matplotlib.backends.qt_editor._formsubplottool import UiSubplotTool


class UiSubplotTool():
    _widgets: dict[str, Any]

    def __init__(self: UiSubplotTool,
                 *args,
                 **kwargs) -> None: ...
