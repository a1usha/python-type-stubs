from typing import Any
from typing import Optional
from typing import Union

m: list[list[float]]
m_inv: list[list[float]]
refX: float
refY: float
refZ: float
refU: float
refV: float
lab_e: float
lab_k: float
__version__: str


def husl_to_rgb(h: Any,
                s: Any,
                l: Any) -> list[Union[float, Any]]: ...


def husl_to_hex(h: Any,
                s: Any,
                l: Any) -> str: ...


def rgb_to_husl(r: Any,
                g: Any,
                b: Any) -> list[Union[float, Any]]: ...


def hex_to_husl(hex: {startswith}) -> list[Union[float, Any]]: ...


def huslp_to_rgb(h: Any,
                 s: Any,
                 l: Any) -> list[Union[float, Any]]: ...


def huslp_to_hex(h: Any,
                 s: Any,
                 l: Any) -> str: ...


def rgb_to_huslp(r: Any,
                 g: Any,
                 b: Any) -> list[Union[float, Any]]: ...


def hex_to_huslp(hex: {startswith}) -> list[Union[float, Any]]: ...


def lch_to_rgb(l: Any,
               c: Any,
               h: Any) -> list[Union[float, Any]]: ...


def rgb_to_lch(r: Any,
               g: Any,
               b: Any) -> list[Union[float, Any]]: ...


def max_chroma(L: {__add__, __truediv__, __mul__},
               H: Union[float, Any]) -> Union[float, Any]: ...


def _hrad_extremum(L: Union[{__add__, __truediv__, __mul__}, Any]) -> Optional[float]: ...


def max_chroma_pastel(L: Any) -> Union[float, Any]: ...


def dot_product(a: Any,
                b: Union[Union[list[float], list[Union[float, Any]]], Any]) -> Union[int, Any]: ...


def f(t: Union[float, Any]) -> Union[float, Any]: ...


def f_inv(t: Union[float, Any]) -> Union[float, Any]: ...


def from_linear(c: {__le__}) -> Union[float, Any]: ...


def to_linear(c: {__gt__}) -> Union[float, Any]: ...


def rgb_prepare(triple: Union[list[Any], Any]) -> list[int]: ...


def hex_to_rgb(hex: {startswith}) -> list[float]: ...


def rgb_to_hex(triple: Union[list[Union[float, Any]], Any]) -> str: ...


def xyz_to_rgb(triple: Union[Union[list[float], list[Union[float, Any]]], Any]) -> list[Union[float, Any]]: ...


def rgb_to_xyz(triple: Union[list[Any], Any]) -> list[Union[int, Any]]: ...


def xyz_to_luv(triple: Union[list[Union[int, Any]], Any]) -> Union[list[float], list[Union[float, Any]]]: ...


def luv_to_xyz(triple: Union[list[Union[float, Any]], Any]) -> Union[list[float], list[Union[float, Any]]]: ...


def luv_to_lch(triple: Union[Union[list[float], list[Union[float, Any]]], Any]) -> list[Union[float, Any]]: ...


def lch_to_luv(triple: Union[list[Any], Any]) -> list[Union[float, Any]]: ...


def husl_to_lch(triple: Union[list[Any], Any]) -> Union[
    list[Union[Union[int, float], Any]], list[Union[float, Any]]]: ...


def lch_to_husl(triple: Union[list[Union[float, Any]], Any]) -> list[Union[float, Any]]: ...


def huslp_to_lch(triple: Union[list[Any], Any]) -> Union[
    list[Union[Union[int, float], Any]], list[Union[float, Any]]]: ...


def lch_to_huslp(triple: Union[list[Union[float, Any]], Any]) -> list[Union[float, Any]]: ...