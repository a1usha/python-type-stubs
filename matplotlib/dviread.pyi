from typing import Any
from typing import BinaryIO
from typing import Optional
from typing import Union
from typing import tuple


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


def _arg_olen1(dvi: {_arg},
               delta: {__add__, __eq__}) -> Any: ...


def _dispatch(table: Any,
              min: Any,
              max: Any = None,
              state: Any = None,
              args: tuple[str] = ('raw',)) -> (method: Any) ->


class Dvi(object):
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
             nbytes: int,
             signed: bool = False) -> int: ...

    @_dispatch(min=0, max=127, state=_dvistate.inpage)
    def _set_char_immediate(self: Dvi,
                            char: Any) -> Optional[Any]: ...

    @_dispatch(min=128, max=131, state=_dvistate.inpage, args=('olen1',))
    def _set_char(self: Dvi,
                  char: Any) -> Optional[Any]: ...

    @_dispatch(132, state=_dvistate.inpage, args=('s4', 's4'))
    def _set_rule(self: Dvi,
                  a: {__gt__},
                  b: {__gt__}) -> Optional[Any]: ...

    @_dispatch(min=133, max=136, state=_dvistate.inpage, args=('olen1',))
    def _put_char(self: Dvi,
                  char: Any) -> Optional[Any]: ...

    def _put_char_real(self: Dvi,
                       char: Any) -> None: ...

    @_dispatch(137, state=_dvistate.inpage, args=('s4', 's4'))
    def _put_rule(self: Dvi,
                  a: Any,
                  b: {__gt__}) -> Optional[Any]: ...

    def _put_rule_real(self: Dvi,
                       a: {__gt__},
                       b: {__gt__}) -> None: ...

    @_dispatch(138)
    def _nop(self: Dvi,
             _: Any) -> Optional[Any]: ...

    @_dispatch(139, state=_dvistate.outer, args=('s4',) * 11)
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

    @_dispatch(140, state=_dvistate.inpage)
    def _eop(self: Dvi,
             _: Any) -> Optional[Any]: ...

    @_dispatch(141, state=_dvistate.inpage)
    def _push(self: Dvi,
              _: Any) -> Optional[Any]: ...

    @_dispatch(142, state=_dvistate.inpage)
    def _pop(self: Dvi,
             _: Any) -> Optional[Any]: ...

    @_dispatch(min=143, max=146, state=_dvistate.inpage, args=('slen1',))
    def _right(self: Dvi,
               b: Any) -> Optional[Any]: ...

    @_dispatch(min=147, max=151, state=_dvistate.inpage, args=('slen',))
    def _right_w(self: Dvi,
                 new_w: Any) -> Optional[Any]: ...

    @_dispatch(min=152, max=156, state=_dvistate.inpage, args=('slen',))
    def _right_x(self: Dvi,
                 new_x: Any) -> Optional[Any]: ...

    @_dispatch(min=157, max=160, state=_dvistate.inpage, args=('slen1',))
    def _down(self: Dvi,
              a: Any) -> Optional[Any]: ...

    @_dispatch(min=161, max=165, state=_dvistate.inpage, args=('slen',))
    def _down_y(self: Dvi,
                new_y: Any) -> Optional[Any]: ...

    @_dispatch(min=166, max=170, state=_dvistate.inpage, args=('slen',))
    def _down_z(self: Dvi,
                new_z: Any) -> Optional[Any]: ...

    @_dispatch(min=171, max=234, state=_dvistate.inpage)
    def _fnt_num_immediate(self: Dvi,
                           k: Any) -> Optional[Any]: ...

    @_dispatch(min=235, max=238, state=_dvistate.inpage, args=('olen1',))
    def _fnt_num(self: Dvi,
                 new_f: Any) -> Optional[Any]: ...

    @_dispatch(min=239, max=242, args=('ulen1',))
    def _xxx(self: Dvi,
             datalen: Any) -> Optional[Any]: ...

    @_dispatch(min=243, max=246, args=('olen1', 'u4', 'u4', 'u4', 'u1', 'u1'))
    def _fnt_def(self: Dvi,
                 k: Any,
                 c: {__ne__},
                 s: Any,
                 d: Any,
                 a: {__add__},
                 l: {__neg__}) -> Optional[Any]: ...

    def _fnt_def_real(self: Dvi,
                      k: int,
                      c: {__ne__},
                      s: Any,
                      d: Any,
                      a: {__add__},
                      l: {__neg__}) -> Any: ...

    @_dispatch(247, state=_dvistate.pre, args=('u1', 'u4', 'u4', 'u4', 'u1'))
    def _pre(self: Dvi,
             i: {__ne__},
             num: {__ne__},
             den: {__ne__},
             mag: {__ne__},
             k: Any) -> Any: ...

    @_dispatch(248, state=_dvistate.outer)
    def _post(self: Dvi,
              _: Any) -> Optional[Any]: ...

    @_dispatch(249)
    def _post_post(self: Dvi,
                   _: Any) -> Any: ...

    @_dispatch(min=250, max=255)
    def _malformed(self: Dvi,
                   offset: Any) -> Any: ...


class DviFont(object):
    def __init__(self: DviFont,
                 scale: float,
                 tfm: Tfm,
                 texname: bytes,
                 vf: Vf) -> None: ...

    def __eq__(self: DviFont,
               other: {texname, size}) -> bool: ...

    def __ne__(self: DviFont,
               other: Any) -> bool: ...

    def __repr__(self: DviFont) -> str: ...

    def _width_of(self: DviFont,
                  char: Any) -> int: ...

    def _height_depth_of(self: DviFont,
                         char: {__eq__}) -> list[int]: ...


class Vf(Dvi):
    def __init__(self: Vf,
                 filename: Any) -> None: ...

    def __getitem__(self: Vf,
                    code: Any) -> Any: ...

    def _read(self: Vf) -> Any: ...

    def _init_packet(self: Vf,
                     pl: int) -> int: ...

    def _finalize_packet(self: Vf,
                         packet_char: Optional[int],
                         packet_width: Any) -> None: ...

    def _pre(self: Vf,
             i: {__ne__},
             x: bytes,
             cs: Any,
             ds: Any) -> Any: ...


def _fix2comp(num: {__and__}) -> {__and__}: ...


def _mul2012(num1: {__and__},
             num2: float) -> int: ...


class Tfm(object):
    def __init__(self: Tfm,
                 filename: Any) -> None: ...


class PsfontsMap(object):
    @lru_cache()
    def __new__(cls: Type[PsfontsMap],
                filename: Any) -> PsfontsMap: ...

    def __getitem__(self: PsfontsMap,
                    texname: {decode}) -> Any: ...

    def _parse(self: PsfontsMap,
               file: BinaryIO) -> None: ...


@_api.deprecated("3.3")
class Encoding(object):
    def __init__(self: Encoding,
                 filename: Any) -> None: ...

    def __iter__(self: Encoding) -> Generator[Any, Any, None]: ...

    @staticmethod
    def _parse(file: Any) -> list: ...


def _parse_enc(path: PathLike) -> list: ...


@lru_cache()
def find_tex_file(filename: Any,
                  format: Union[str, bytes] = None) -> Union[str, bytes]: ...


@lru_cache()
def _fontfile(cls: Any,
              suffix: Any,
              texname: {__add__}) -> Optional[Any]: ...