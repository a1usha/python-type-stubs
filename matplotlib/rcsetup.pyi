from typing import Any
from typing import Optional
from typing import Tuple
from typing import Type
from typing import Union

from cycler import Cycler
from list import list
from matplotlib import _api
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


def _listify_validator(scalar_validator: Union[(s: Any),
                       allow_stringlist: bool = False,
                       *,
                       n: int = None,
                       doc: str = None) -> (s: Any) ->


def validate_any(s: Any) -> Any: ...


def _validate_date(s: Any) -> Any: ...


def validate_bool(b: Any) -> bool: ...


@_api.deprecated("3.3")
def validate_bool_maybe_none(b: str) -> Optional[bool]: ...


def _validate_date_converter(s: Any) -> None: ...


def _validate_date_int_mult(s: Any) -> None: ...


def _validate_tex_preamble(s: Optional[{__eq__}]) -> str: ...


def validate_axisbelow(s: Any) -> Union[bool, str]: ...


def validate_dpi(s: {__eq__}) -> Union[{__eq__}, float]: ...


def _make_type_validator(cls: Type[Union[str, int, float]],
                         *,
                         allow_none: bool = False) -> (s: Optional[{lower}]) ->


def validate_fonttype(s: {lower}) -> Union[int, None, str, float]: ...


def validate_backend(s: {startswith, endswith}) -> {startswith, endswith}: ...


def _validate_toolbar(s: Any) -> Any: ...


@_api.deprecated("3.3")
def _make_nseq_validator(cls: Type[Union[float, int]],
                         n: Any = None,
                         allow_none: bool = False) -> (s: Any) ->


@_api.deprecated("3.3")
def validate_nseq_float(n: Any) -> (s: Any) ->


@_api.deprecated("3.3")
def validate_nseq_int(n: Any) -> (s: Any) ->


def validate_color_or_inherit(s: {__eq__}) -> Union[{__eq__}, str]: ...


def validate_color_or_auto(s: {__eq__}) -> Union[{__eq__}, str]: ...


def validate_color_for_prop_cycle(s: Any) -> str: ...


def validate_color(s: Union[{__eq__}, {__eq__}]) -> str: ...


def _validate_cmap(s: Any) -> Any: ...


def validate_aspect(s: Any) -> float: ...


def validate_fontsize_None(s: Optional[{__eq__}]) -> Union[None, str, float]: ...


def validate_fontsize(s: Optional[{__eq__}]) -> Union[str, None, float]: ...


def validate_fontweight(s: Any) -> int: ...


def validate_font_properties(s: Any) -> Any: ...


def _validate_mathtext_fallback_to_cm(b: Optional[{__eq__}]) -> Optional[bool]: ...


def _validate_mathtext_fallback(s: Optional[{__eq__, lower}]) -> Optional[str]: ...


def validate_whiskers(s: Any) -> Union[list[Union[
    None, str, int, float, slice, Tuple, list, Tuple[int, str], {__len__, __getitem__}, Tuple[
        int, Union[str, {__len__, __getitem__}]]]], float]: ...


def validate_ps_distiller(s: Any) -> Optional[Any]: ...


def _validate_linestyle(ls: {__len__, __getitem__}) -> Union[
    Tuple[int, str], str, {__len__, __getitem__}, Tuple[int, Union[str, {__len__, __getitem__}]]]: ...


def validate_markevery(s: Union[None, int, float, slice]) -> Union[slice, float, int, Tuple, list]: ...


@_api.deprecated("3.3")
def validate_hinting(s: {startswith, endswith}) -> Any: ...


@_api.deprecated("3.3")
def validate_movie_writer(s: Any) -> Any: ...


def validate_bbox(s: Any) -> Optional[str]: ...


def validate_sketch(s: Optional[{__eq__}]) -> Optional[Tuple[Union[None, str, int, float, slice, Tuple, list, Tuple[
    int, str], {__len__, __getitem__}, Tuple[int, Union[str, {__len__, __getitem__}]]], ...]]: ...


def _validate_greaterequal0_lessthan1(s: Any) -> Union[None, str, int, float]: ...


def _validate_greaterequal0_lessequal1(s: Any) -> Union[None, str, int, float]: ...


def validate_hatch(s: Any) -> str: ...


def cycler(*args,
           **kwargs) -> Cycler: ...


def validate_cycler(s: Any) -> Cycler: ...


def validate_hist_bins(s: Any) -> Union[str, int, list[Union[
    None, str, int, float, slice, Tuple, list, Tuple[int, str], {__len__, __getitem__}, Tuple[
        int, Union[str, {__len__, __getitem__}]]]]]: ...


@_api.deprecated("3.3")
def validate_webagg_address(s: Any) -> Any: ...


class _ignorecase(list):
    pass


def _convert_validator_spec(key: str,
                            conv: Union[(s: {startswith, endswith})) -> Union[
    ValidateInStrings, (s: {startswith, endswith}) ->