from seaborn import palettes as palettes
from cycler import cycler as cycler
from distutils.version import LooseVersion as LooseVersion
from typing import Any
from typing import Callable
from typing import ClassVar
from typing import Optional
from typing import Union

from dict import dict
from seaborn.rcmod import _AxesStyle
from seaborn.rcmod import _PlottingContext
from seaborn.rcmod import _RCAesthetics

_style_keys: list[Union[str, Any]]
_context_keys: list[Union[str, Any]]
__all__: Any


def set_theme(context: Union[str, dict] = "notebook",
              style: Union[str, dict] = "darkgrid",
              palette: Union[str, Any] = "deep",
              font: str = "sans-serif",
              font_scale: Any = 1,
              color_codes: bool = True,
              rc: Optional[dict] = None) -> None: ...


def set(*args,
        **kwargs) -> None: ...


def reset_defaults() -> None: ...


def reset_orig() -> None: ...


def axes_style(style: Any = None,
               rc: Any = None) -> Union[_AxesStyle[_KT, _VT], _AxesStyle[Any, Any]]: ...


def set_style(style: Any = None,
              rc: Any = None) -> None: ...


def plotting_context(context: Any = None,
                     font_scale: Any = 1,
                     rc: Any = None) -> Union[_PlottingContext[_KT, _VT], _PlottingContext[Any, Any]]: ...


def set_context(context: Any = None,
                font_scale: Any = 1,
                rc: Any = None) -> None: ...


class _RCAesthetics(dict):
    _orig: dict

    def __enter__(self: _RCAesthetics) -> None: ...

    def __exit__(self: _RCAesthetics,
                 exc_type: Any,
                 exc_value: Any,
                 exc_tb: Any) -> None: ...

    def __call__(self: _RCAesthetics,
                 func: Any) -> Callable[[Tuple[Any, ...], dict[str, Any]], Any]: ...


class _AxesStyle(_RCAesthetics):
    _keys: ClassVar[list[Union[str, Any]]]
    _set: ClassVar[staticmethod]
    pass


class _PlottingContext(_RCAesthetics):
    _keys: ClassVar[list[Union[str, Any]]]
    _set: ClassVar[staticmethod]
    pass


def set_palette(palette: Any,
                n_colors: int = None,
                desat: float = None,
                color_codes: bool = False) -> None: ...