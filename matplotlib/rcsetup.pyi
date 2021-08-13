from typing import Any
from typing import Optional
from typing import Type
from typing import Union

from matplotlib.rcsetup import ValidateInStrings


class ValidateInStrings(object):
    def __init__(self: ValidateInStrings,
                 key: Any,
                 valid: Any,
                 ignorecase: bool = False,
                 _deprecated_since: Any = None) -> None: ...

    def __call__(self: ValidateInStrings,
                 s: {startswith, endswith}) -> Any: ...


class _ignorecase(list):
    pass


def cycler(*args,
           **kwargs) -> Cycler: ...


def _make_type_validator(cls: Type[Union[str, int, float]],
                         allow_none: bool = False) -> (s: Optional[{lower}]) ->


def validate_hatch(s: Any) -> str: ...


def validate_markevery(s: Union[None, int, float, slice]) -> Union[slice, float, int, tuple, list]: ...


def validate_color(s: Union[{__eq__}, {__eq__}]) -> str: ...


def validate_color_for_prop_cycle(s: Any) -> str: ...


def validate_dpi(s: {__eq__}) -> Union[{__eq__}, float]: ...


def _validate_tex_preamble(s: Optional[{__eq__}]) -> str: ...


@_api.deprecated("3.3")
def validate_bool_maybe_none(b: str) -> Optional[bool]: ...


@_api.deprecated("3.3")
def validate_movie_writer(s: Any) -> Any: ...


@_api.deprecated("3.3")
def validate_nseq_int(n: Any) -> (s: Any) ->


def _validate_date_int_mult(s: Any) -> None: ...


def _validate_date_converter(s: Any) -> None: ...


def validate_aspect(s: Any) -> float: ...


def _convert_validator_spec(key: str,
                            conv: Union[(s: {startswith, endswith})) -> Union[
    ValidateInStrings, (s: {startswith, endswith}) ->


@_api.deprecated("3.3")
def validate_nseq_float(n: Any) -> (s: Any) ->


def _validate_greaterequal0_lessequal1(s: Any) -> Union[None, str, int, float]: ...


def validate_color_or_inherit(s: {__eq__}) -> Union[{__eq__}, str]: ...


def _validate_linestyle(ls: {__len__, __getitem__}) -> Union[
    tuple[int, str], str, {__len__, __getitem__}, tuple[int, Union[str, {__len__, __getitem__}]]]: ...


def _validate_mathtext_fallback(s: Optional[{__eq__, lower}]) -> Optional[str]: ...


def validate_axisbelow(s: Any) -> Union[bool, str]: ...


def validate_backend(s: {startswith, endswith}) -> {startswith, endswith}: ...


def _validate_cmap(s: Any) -> Any: ...


@_api.deprecated("3.3")
def _make_nseq_validator(cls: Type[Union[float, int]],
                         n: Any = None,
                         allow_none: bool = False) -> (s: Any) ->


def validate_sketch(s: Optional[{__eq__}]) -> Optional[tuple[Union[None, str, int, float, slice, tuple, list, tuple[
    int, str], {__len__, __getitem__}, tuple[int, Union[str, {__len__, __getitem__}]]], ...]]: ...


def validate_bbox(s: Any) -> Optional[str]: ...


def validate_fontsize_None(s: Optional[{__eq__}]) -> Union[None, str, float]: ...


def validate_bool(b: Any) -> bool: ...


def validate_any(s: Any) -> Any: ...


def validate_fontsize(s: Optional[{__eq__}]) -> Union[str, None, float]: ...


def validate_whiskers(s: Any) -> Union[list[Union[
    None, str, int, float, slice, tuple, list, tuple[int, str], {__len__, __getitem__}, tuple[
        int, Union[str, {__len__, __getitem__}]]]], float]: ...


def _validate_toolbar(s: Any) -> Any: ...


def _validate_greaterequal0_lessthan1(s: Any) -> Union[None, str, int, float]: ...


@lru_cache()
def _listify_validator(scalar_validator: Union[(s: Any),
                       allow_stringlist: bool = False,
                       n: int = None,
                       doc: str = None) -> (s: Any) ->


@_api.deprecated("3.3")
def validate_webagg_address(s: Any) -> Any: ...


def validate_color_or_auto(s: {__eq__}) -> Union[{__eq__}, str]: ...


def validate_fonttype(s: {lower}) -> Union[int, None, str, float]: ...


@_api.deprecated("3.3")
def validate_hinting(s: {startswith, endswith}) -> Any: ...


def validate_hist_bins(s: Any) -> Union[str, int, list[Union[
    None, str, int, float, slice, tuple, list, tuple[int, str], {__len__, __getitem__}, tuple[
        int, Union[str, {__len__, __getitem__}]]]]]: ...


def validate_ps_distiller(s: Any) -> Optional[Any]: ...


def validate_font_properties(s: Any) -> Any: ...


def validate_cycler(s: Any) -> Cycler: ...


def _validate_date(s: Any) -> Any: ...


def validate_fontweight(s: Any) -> int: ...


def _validate_mathtext_fallback_to_cm(b: Optional[{__eq__}]) -> Optional[bool]: ...