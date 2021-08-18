from typing import Any
from typing import Callable
from typing import Optional
from typing import Tuple
from typing import Type
from typing import Union

from cycler import Cycler
from list import list
from matplotlib import _api
from matplotlib._enums import CapStyle
from matplotlib._enums import JoinStyle
from matplotlib.rcsetup import ValidateInStrings
from object import object


class ValidateInStrings(object):
    def __init__(self: ValidateInStrings,
                 key: Any,
                 valid: Any,
                 ignorecase: bool = False,
                 *,
                 _deprecated_since: Any = None) -> None: ...

    def __call__(self: ValidateInStrings,
                 s: {startswith, endswith}) -> Any: ...


def _listify_validator(scalar_validator: Union[Union[Callable[[Any], Any], Callable[
    [Optional[{lower}]], Union[Union[None, str, int, float], Any]], Callable[
                                                         [Union[Union[{__eq__}, {__eq__}], Any]], Union[str, Any]],
                                                     Callable[[Union[Optional[{__eq__}], Any]], Union[
                                                         str, None, float]], ValidateInStrings, Callable[
                                                         [Union[None, int, float, slice]], Union[
                                                             Union[slice, float, int, tuple, list], Any]], Callable[
                                                         [Any], str], Callable[[Any], list[Union[Union[
                                                                                                     None, str, int, float, slice, tuple, list,
                                                                                                     tuple[int, str], {
                                                                                                         __len__,
                                                                                                         __getitem__},
                                                                                                     tuple[int, Union[
                                                                                                         Union[str, {
                                                                                                             __len__,
                                                                                                             __getitem__}], Any]]], Any]]],
                                                     Callable[[Any], Union[str, Any]], Callable[
                                                         [{__len__, __getitem__}], Union[Union[tuple[int, str], str, {
                                                             __len__, __getitem__}, tuple[int, Union[
                                                             Union[str, {__len__, __getitem__}], Any]]], Any]], Type[
                                                         JoinStyle], Type[CapStyle]], Any],
                       allow_stringlist: bool = False,
                       *,
                       n: Union[int, Any] = None,
                       doc: Union[str, Any] = None) -> Callable[[Any], list[Union[Union[
                                                                                      None, str, int, float, slice, Tuple, list,
                                                                                      Tuple[int, str], {__len__,
                                                                                                        __getitem__},
                                                                                      Tuple[int, Union[Union[str, {
                                                                                          __len__,
                                                                                          __getitem__}], Any]]], Any]]]: ...


def validate_any(s: Any) -> Any: ...


def _validate_date(s: Any) -> Any: ...


def validate_bool(b: Any) -> bool: ...


@_api.deprecated("3.3")
def validate_bool_maybe_none(b: Union[str, Any]) -> Union[Optional[bool], Any]: ...


def _validate_date_converter(s: Any) -> None: ...


def _validate_date_int_mult(s: Any) -> None: ...


def _validate_tex_preamble(s: Optional[{__eq__}]) -> str: ...


def validate_axisbelow(s: Any) -> Union[bool, str]: ...


def validate_dpi(s: {__eq__}) -> Union[{__eq__}, float]: ...


def _make_type_validator(cls: Union[Type[Union[str, int, float]], Any],
                         *,
                         allow_none: bool = False) -> Callable[
    [Optional[{lower}]], Union[Union[None, str, int, float], Any]]: ...


def validate_fonttype(s: {lower}) -> Union[Union[int, None, str, float], Any]: ...


def validate_backend(s: {startswith, endswith}) -> Union[{startswith, endswith}, Any]: ...


def _validate_toolbar(s: Any) -> Any: ...


@_api.deprecated("3.3")
def _make_nseq_validator(cls: Union[Type[Union[float, int]], Any],
                         n: Any = None,
                         allow_none: bool = False) -> Union[
    Callable[[Any], list[Union[Union[float, int, str], Any]]], Any]: ...


@_api.deprecated("3.3")
def validate_nseq_float(n: Any) -> Union[Callable[[Any], list[Union[Union[float, int, str], Any]]], Any]: ...


@_api.deprecated("3.3")
def validate_nseq_int(n: Any) -> Union[Callable[[Any], list[Union[Union[float, int, str], Any]]], Any]: ...


def validate_color_or_inherit(s: {__eq__}) -> Union[Union[{__eq__}, str], Any]: ...


def validate_color_or_auto(s: {__eq__}) -> Union[Union[{__eq__}, str], Any]: ...


def validate_color_for_prop_cycle(s: Any) -> Union[str, Any]: ...


def validate_color(s: Union[Union[{__eq__}, {__eq__}], Any]) -> Union[str, Any]: ...


def _validate_cmap(s: Any) -> Any: ...


def validate_aspect(s: Any) -> Union[float, Any]: ...


def validate_fontsize_None(s: Optional[{__eq__}]) -> Union[None, str, float]: ...


def validate_fontsize(s: Union[Optional[{__eq__}], Any]) -> Union[str, None, float]: ...


def validate_fontweight(s: Any) -> Union[int, Any]: ...


def validate_font_properties(s: Any) -> Any: ...


def _validate_mathtext_fallback_to_cm(b: Optional[{__eq__}]) -> Union[Optional[bool], Any]: ...


def _validate_mathtext_fallback(s: Optional[{__eq__, lower}]) -> Optional[str]: ...


def validate_whiskers(s: Any) -> Union[list[Union[Union[None, str, int, float, slice, Tuple, list, Tuple[int, str], {
    __len__, __getitem__}, Tuple[int, Union[Union[str, {__len__, __getitem__}], Any]]], Any]], float]: ...


def validate_ps_distiller(s: Any) -> Optional[Any]: ...


def _validate_linestyle(ls: {__len__, __getitem__}) -> Union[Union[Tuple[int, str], str, {__len__, __getitem__}, Tuple[
    int, Union[Union[str, {__len__, __getitem__}], Any]]], Any]: ...


def validate_markevery(s: Union[None, int, float, slice]) -> Union[Union[slice, float, int, Tuple, list], Any]: ...


@_api.deprecated("3.3")
def validate_hinting(s: {startswith, endswith}) -> Any: ...


@_api.deprecated("3.3")
def validate_movie_writer(s: Any) -> Any: ...


def validate_bbox(s: Any) -> Union[Optional[str], Any]: ...


def validate_sketch(s: Optional[{__eq__}]) -> Optional[Tuple[Union[Union[
                                                                       None, str, int, float, slice, Tuple, list, Tuple[
                                                                           int, str], {__len__, __getitem__}, Tuple[
                                                                           int, Union[Union[str, {__len__,
                                                                                                  __getitem__}], Any]]], Any], ...]]: ...


def _validate_greaterequal0_lessthan1(s: Any) -> Union[Union[None, str, int, float], Any]: ...


def _validate_greaterequal0_lessequal1(s: Any) -> Union[Union[None, str, int, float], Any]: ...


def validate_hatch(s: Any) -> str: ...


def cycler(*args,
           **kwargs) -> Cycler: ...


def validate_cycler(s: Any) -> Cycler: ...


def validate_hist_bins(s: Any) -> Union[str, int, list[Union[Union[None, str, int, float, slice, Tuple, list, Tuple[
    int, str], {__len__, __getitem__}, Tuple[int, Union[Union[str, {__len__, __getitem__}], Any]]], Any]]]: ...


@_api.deprecated("3.3")
def validate_webagg_address(s: Any) -> Any: ...


class _ignorecase(list):
    pass


def _convert_validator_spec(key: Union[str, Any],
                            conv: Union[Union[Callable[[{startswith, endswith}], Union[{startswith, endswith}, Any]],
                                              Callable[[Any], bool], Callable[[Any], Any], Callable[
                                                  [Optional[{lower}]], Union[
                                                      Union[None, str, int, float], Any]]], Any]) -> Union[
    ValidateInStrings, Callable[[{startswith, endswith}], Union[{startswith, endswith}, Any]], Callable[[Any], bool],
    Callable[[Any], Any], Callable[[Optional[{lower}]], Union[Union[None, str, int, float], Any]]]: ...