from argparse import ArgumentParser as ArgumentParser
from matplotlib import rcParams as rcParams
from matplotlib import cbook as cbook
from matplotlib import _api as _api
from pathlib import Path as Path
from functools import wraps as wraps
from functools import partial as partial
from functools import lru_cache as lru_cache
from collections import namedtuple as namedtuple
from os import PathLike
from typing import Any
from typing import BinaryIO
from typing import Callable
from typing import ClassVar
from typing import Generator
from typing import Optional
from typing import Page
from typing import Type
from typing import Union

from matplotlib import _api
from matplotlib.dviread import Dvi
from matplotlib.dviread import DviFont
from matplotlib.dviread import Encoding
from matplotlib.dviread import PsfontsMap
from matplotlib.dviread import Tfm
from matplotlib.dviread import Vf
from object import object

_log: Logger
_dvistate: Any
Page: Type[Page]
Text: Type[Text]
Box: Type[Box]
from typing import Any


def _arg_raw(dvi: Any,
             delta: Any) -> Any: ...


def _arg(nbytes: Any,
         signed: Any,
         dvi: {_arg},
         _: Any) -> Any: ...


def _arg_slen(dvi: {_arg},
              delta: {__eq__}) -> Optional[Any]: ...


def _arg_slen1(dvi: {_arg},
               delta: {__add__}) -> Any: ...


def _arg_ulen1(dvi: {_arg},
               delta: {__add__}) -> Any: ...


_arg_mapping: dict[Any, Union[
    Callable[[Any, Any], Any], partial[Any], Callable[[{_arg}, {__eq__}], Optional[Any]], Callable[
        [{_arg}, {__add__, __eq__}], Any], Callable[[{_arg}, {__add__}], Any], Callable[[{_arg}, {__add__}], Any]]]


def _arg_olen1(dvi: {_arg},
               delta: {__add__, __eq__}) -> Any: ...


def _dispatch(table: Any,
              min: Any,
              max: Any = None,
              state: Any = None,
              args: Union[tuple[str], Any] = ('raw',)) -> Callable[
    [Any], Callable[[{state, _arg}, {__sub__}], Any]]: ...


class Dvi(object):
    _dtable: ClassVar[list[None]]
    _dispatch: ClassVar[partial[Callable[[Any], Callable[[{state, _arg}, {__sub__}], Any]]]]
    boxes: list[Any]
    stack: list[Any]
    f: Any
    h: int
    baseline: Optional[float]
    file: BinaryIO
    fonts: dict[Any, Any]
    v: int
    _baseline_v: None
    w: int
    x: int
    y: int
    z: int
    state: Any
    text: list[Any]
    dpi: Any

    def __init__(self: Dvi,
                 filename: Any,
                 dpi: Any) -> None: ...

    def _get_baseline(self: Dvi,
                      filename: Any) -> Optional[float]: ...

    def __enter__(self: Dvi) -> Dvi: ...

    def __exit__(self: Dvi,
                 etype: Any,
                 evalue: Any,
                 etrace: Any) -> None: ...

    def __iter__(self: Dvi) -> Generator[Union[Page, Page, Page], Any, None]: ...

    def close(self: Dvi) -> None: ...

    def _output(self: Dvi) -> Union[Page, Page, Page]: ...

    def _read(self: Dvi) -> bool: ...

    def _arg(self: Dvi,
             nbytes: Union[int, Any],
             signed: bool = False) -> Union[int, Any]: ...

    def _set_char_immediate(self: Dvi,
                            char: Any) -> Optional[Any]: ...

    def _set_char(self: Dvi,
                  char: Any) -> Optional[Any]: ...

    def _set_rule(self: Dvi,
                  a: {__gt__},
                  b: {__gt__}) -> Optional[Any]: ...

    def _put_char(self: Dvi,
                  char: Any) -> Optional[Any]: ...

    def _put_char_real(self: Dvi,
                       char: Any) -> None: ...

    def _put_rule(self: Dvi,
                  a: {__gt__},
                  b: {__gt__}) -> Optional[Any]: ...

    def _put_rule_real(self: Dvi,
                       a: {__gt__},
                       b: {__gt__}) -> None: ...

    def _nop(self: Dvi,
             _: Any) -> Optional[Any]: ...

    def _bop(self: Dvi,
             c0: Any,
             c1: Any,
             c2: Any,
             c3: Any,
             c4: Any,
             c5: Any,
             c6: Any,
             c7: Any,
             c8: Any,
             c9: Any,
             p: Any) -> Optional[Any]: ...

    def _eop(self: Dvi,
             _: Any) -> Optional[Any]: ...

    def _push(self: Dvi,
              _: Any) -> Optional[Any]: ...

    def _pop(self: Dvi,
             _: Any) -> Optional[Any]: ...

    def _right(self: Dvi,
               b: Any) -> Optional[Any]: ...

    def _right_w(self: Dvi,
                 new_w: Any) -> Optional[Any]: ...

    def _right_x(self: Dvi,
                 new_x: Any) -> Optional[Any]: ...

    def _down(self: Dvi,
              a: Any) -> Optional[Any]: ...

    def _down_y(self: Dvi,
                new_y: Any) -> Optional[Any]: ...

    def _down_z(self: Dvi,
                new_z: Any) -> Optional[Any]: ...

    def _fnt_num_immediate(self: Dvi,
                           k: Any) -> Optional[Any]: ...

    def _fnt_num(self: Dvi,
                 new_f: Any) -> Optional[Any]: ...

    def _xxx(self: Dvi,
             datalen: Any) -> Optional[Any]: ...

    def _fnt_def(self: Dvi,
                 k: Any,
                 c: {__ne__},
                 s: Any,
                 d: Any,
                 a: {__add__},
                 l: {__neg__}) -> Optional[Any]: ...

    def _fnt_def_real(self: Dvi,
                      k: Union[int, Any],
                      c: {__ne__},
                      s: Any,
                      d: Any,
                      a: {__add__},
                      l: {__neg__}) -> Any: ...

    def _pre(self: Dvi,
             i: {__ne__},
             num: {__ne__},
             den: {__ne__},
             mag: {__ne__},
             k: Any) -> Any: ...

    def _post(self: Dvi,
              _: Any) -> Optional[Any]: ...

    def _post_post(self: Dvi,
                   _: Any) -> Any: ...

    def _malformed(self: Dvi,
                   offset: Any) -> Any: ...


class DviFont(object):
    __slots__: ClassVar[tuple[str, str, str, str, str, str]]
    _tfm: Tfm
    _scale: float
    size: Union[float, Any]
    texname: bytes
    widths: list[Union[int, Any]]
    _vf: Vf

    def __init__(self: DviFont,
                 scale: float,
                 tfm: Tfm,
                 texname: bytes,
                 vf: Vf) -> None: ...

    def __eq__(self: DviFont,
               other: {texname, size}) -> Union[bool, Any]: ...

    def __ne__(self: DviFont,
               other: {texname, size}) -> bool: ...

    def __repr__(self: DviFont) -> str: ...

    def _width_of(self: DviFont,
                  char: Any) -> Union[int, Any]: ...

    def _height_depth_of(self: DviFont,
                         char: {__eq__}) -> list[Union[int, Any]]: ...


class Vf(Dvi):
    boxes: list[Any]
    stack: list[Any]
    f: Any
    h: int
    v: int
    w: int
    x: int
    y: int
    z: int
    state: Any
    text: list[Any]
    _chars: dict[Any, Any]
    _first_font: None

    def __init__(self: Vf,
                 filename: Any) -> None: ...

    def __getitem__(self: Vf,
                    code: Any) -> Any: ...

    def _read(self: Vf) -> Any: ...

    def _init_packet(self: Vf,
                     pl: Union[int, Any]) -> Union[int, Any]: ...

    def _finalize_packet(self: Vf,
                         packet_char: Union[Optional[int], Any],
                         packet_width: Any) -> None: ...

    def _pre(self: Vf,
             i: {__ne__},
             x: Union[bytes, Any],
             cs: Any,
             ds: Any) -> Any: ...


def _fix2comp(num: {__and__}) -> Union[{__and__}, Any]: ...


def _mul2012(num1: Union[{__and__}, Any],
             num2: Union[float, Any]) -> Union[int, Any]: ...


class Tfm(object):
    __slots__: ClassVar[tuple[str, str, str, str, str]]
    design_size: Any
    depth: dict[Any, Union[{__and__}, Any]]
    checksum: Any
    width: dict[Any, Union[{__and__}, Any]]
    height: dict[Any, Union[{__and__}, Any]]

    def __init__(self: Tfm,
                 filename: Any) -> None: ...


PsFont: Type[PsFont]


class PsfontsMap(object):
    __slots__: ClassVar[tuple[str, str]]
    file: BinaryIO
    _font: dict[Any, Any]
    self: PsfontsMap
    _filename: str

    def __new__(cls: Type[PsfontsMap],
                filename: Any) -> PsfontsMap: ...

    def __getitem__(self: PsfontsMap,
                    texname: {decode}) -> Any: ...

    def _parse(self: PsfontsMap,
               file: Union[BinaryIO, Any]) -> None: ...


@_api.deprecated("3.3")
class Encoding(object):
    __slots__: ClassVar[tuple[str]]
    encoding: list[Any]

    def __init__(self: Encoding,
                 filename: Any) -> None: ...

    def __iter__(self: Encoding) -> Generator[Any, Any, None]: ...

    def _parse(file: Union[BinaryIO, Any]) -> list[Any]: ...


def _parse_enc(path: PathLike) -> list: ...


def find_tex_file(filename: Any,
                  format: Union[str, bytes] = None) -> Union[str, bytes]: ...


_tfmfile: partial[Optional[Any]]

_vffile: partial[Optional[Any]]


def _fontfile(cls: Any,
              suffix: Any,
              texname: {__add__}) -> Optional[Any]: ...