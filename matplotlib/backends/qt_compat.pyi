from matplotlib import _api as _api
from distutils.version import LooseVersion as LooseVersion
from typing import Union

QT_API_PYQT5: str
QT_API_PYSIDE2: str
QT_API_PYQTv2: str
QT_API_PYSIDE: str
QT_API_PYQT: str
QT_API_ENV: Optional[str]
QT_API_ENV: str
_ETS: dict[Optional[str], Optional[str]]
from typing import Any


def _setup_pyqt5() -> Any: ...


ETS: dict[Any, tuple[str, int]]

QT_RC_MAJOR_VERSION: int


def _setup_pyqt4() -> Any: ...


def _devicePixelRatioF(obj: {devicePixelRatioF, devicePixelRatio}) -> Union[int, Any]: ...


def _setDevicePixelRatio(obj: Any,
                         val: Any) -> None: ...