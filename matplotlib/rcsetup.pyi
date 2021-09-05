from cycler import cycler as ccycler
from cycler import Cycler as Cycler
from matplotlib._enums import CapStyle as CapStyle
from matplotlib._enums import JoinStyle as JoinStyle
from matplotlib.fontconfig_pattern import parse_fontconfig_pattern as parse_fontconfig_pattern
from matplotlib.colors import is_color_like as is_color_like
from matplotlib.colors import Colormap as Colormap
from matplotlib.cbook import ls_mapper as ls_mapper
from matplotlib import cbook as cbook
from matplotlib import animation as animation
from matplotlib import _api as _api
from numbers import Number as Number
from functools import reduce as reduce
from functools import lru_cache as lru_cache
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

non_interactive_bk: list[str]
all_backends: list[Union[str, Any]]
interactive_bk: list[Union[str, Any]]


class ValidateInStrings(object):
    valid: dict
    ignorecase: bool
    _deprecated_since: Any
    key: Any

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
                                                         [Any], str], Callable[[Any], list[
    Union[Union[None, str, int, float, slice, tuple, list, tuple[int, str], tuple[int, Union[str, Any]]], Any]]],
                                                     Callable[[Any], Union[str, Any]], Callable[
                                                         [{__len__, __getitem__}], Union[Union[tuple[int, str], str,
                                                                                               tuple[int, Union[
                                                                                                   str, Any]]], Any]],
                                                     Type[JoinStyle], Type[CapStyle]], Any],
                       allow_stringlist: bool = False,
                       *,
                       n: Union[int, Any] = None,
                       doc: Union[str, Any] = None) -> Callable[[Any], list[
    Union[Union[None, str, int, float, slice, Tuple, list, Tuple[int, str], Tuple[int, Union[str, Any]]], Any]]]: ...


validate_anylist: Callable[[Any], list[Any]]


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


validate_string: Callable[[Optional[{lower}]], Union[Union[None, str, int, float], Any]]

validate_string_or_None: Callable[[Optional[{lower}]], Union[Union[None, str, int, float], Any]]

validate_stringlist: Callable[[Any], list[Any]]

validate_int: Callable[[Optional[{lower}]], Union[Union[None, str, int, float], Any]]

validate_int_or_None: Callable[[Optional[{lower}]], Union[Union[None, str, int, float], Any]]

validate_float: Callable[[Optional[{lower}]], Union[Union[None, str, int, float], Any]]

validate_float_or_None: Callable[[Optional[{lower}]], Union[Union[None, str, int, float], Any]]

validate_floatlist: Callable[[Any], list[
    Union[Union[None, str, int, float, slice, tuple, list, tuple[int, str], tuple[int, Union[str, Any]]], Any]]]


def _make_type_validator(cls: Union[Type[Union[str, int, float]], Any],
                         *,
                         allow_none: bool = False) -> Callable[
    [Optional[{lower}]], Union[Union[None, str, int, float], Any]]: ...


_validate_standard_backends: ValidateInStrings

_auto_backend_sentinel: object


def validate_fonttype(s: {lower}) -> Union[Union[None, str, int, float], Any]: ...


validate_toolbar: ValidateInStrings


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


validate_colorlist: Callable[[Any], list[Any]]


def validate_color(s: Union[Union[{__eq__}, {__eq__}], Any]) -> Union[str, Any]: ...


validate_orientation: ValidateInStrings


def _validate_cmap(s: Any) -> Any: ...


def validate_aspect(s: Any) -> Union[float, Any]: ...


def validate_fontsize_None(s: Optional[{__eq__}]) -> Union[None, str, float]: ...


validate_fontsizelist: Callable[[Any], list[Any]]


def validate_fontsize(s: Union[Optional[{__eq__}], Any]) -> Union[str, None, float]: ...


def validate_fontweight(s: Any) -> Union[int, Any]: ...


def validate_font_properties(s: Any) -> Any: ...


def _validate_mathtext_fallback_to_cm(b: Optional[{__eq__}]) -> Union[Optional[bool], Any]: ...


validate_fontset: ValidateInStrings

validate_mathtext_default: ValidateInStrings

_validate_alignment: ValidateInStrings


def _validate_mathtext_fallback(s: Optional[{__eq__, lower}]) -> Optional[str]: ...


validate_ps_papersize: ValidateInStrings


def validate_whiskers(s: Any) -> Union[list[Any], float]: ...


_validate_named_linestyle: ValidateInStrings


def validate_ps_distiller(s: Any) -> Optional[Any]: ...


validate_fillstyle: ValidateInStrings

validate_fillstylelist: Callable[[Any], list[Any]]


def _validate_linestyle(ls: {__len__, __getitem__}) -> Union[Union[Tuple[int, str], str, {__len__, __getitem__}, Tuple[
    int, Union[Union[str, {__len__, __getitem__}], Any]]], Any]: ...


validate_markeverylist: Callable[[Any], list[Any]]

validate_legend_loc: ValidateInStrings

validate_svg_fonttype: ValidateInStrings


def validate_markevery(s: Union[None, int, float, slice]) -> Union[Union[slice, float, int, Tuple, list], Any]: ...


_validate_hinting: ValidateInStrings

validate_pgf_texsystem: ValidateInStrings


@_api.deprecated("3.3")
def validate_hinting(s: {startswith, endswith}) -> Any: ...


validate_movie_frame_fmt: ValidateInStrings

validate_axis_locator: ValidateInStrings

validate_movie_html_fmt: ValidateInStrings


@_api.deprecated("3.3")
def validate_movie_writer(s: Any) -> Any: ...


def validate_bbox(s: Any) -> Union[Optional[str], Any]: ...


def validate_sketch(s: Optional[{__eq__}]) -> Optional[Tuple[Any, ...]]: ...


def _validate_greaterequal0_lessthan1(s: Any) -> Union[Union[None, str, int, float], Any]: ...


_range_validators: dict[str, Union[Callable[[Any], Union[Union[None, str, int, float], Any]], Callable[
    [Any], Union[Union[None, str, int, float], Any]]]]

validate_grid_axis: ValidateInStrings


def _validate_greaterequal0_lessequal1(s: Any) -> Union[Union[None, str, int, float], Any]: ...


validate_hatchlist: Callable[[Any], list[Any]]

validate_dashlist: Callable[[Any], list[Any]]

_prop_validators: dict[Union[str, Any], Union[Callable[[Any], list[Any]], Any]]

_prop_aliases: dict[str, str]


def validate_hatch(s: Any) -> str: ...


def cycler(*args,
           **kwargs) -> Cycler: ...


def validate_cycler(s: Any) -> Cycler: ...


def validate_hist_bins(s: Any) -> Union[str, int, list[
    Union[Union[None, str, int, float, slice, Tuple, list, Tuple[int, str], Tuple[int, Union[str, Any]]], Any]]]: ...


validate_axes_titlelocation: ValidateInStrings


@_api.deprecated("3.3")
def validate_webagg_address(s: Any) -> Any: ...


class _ignorecase(list):
    pass


_validators: dict[Union[str, Any], Union[Union[Callable[[{startswith, endswith}], Union[{startswith, endswith}, Any]],
                                               Callable[[Any], bool], Callable[[Any], Any], Callable[
                                                   [Optional[{lower}]], Union[
                                                       Union[None, str, int, float], Any]]], Any]]
_validators: dict

_hardcoded_defaults: dict[str, Union[bool, list[Any], None, list[str], int, str, object]]

_validators: dict[Union[str, Any], Union[Union[Callable[[{startswith, endswith}], Union[{startswith, endswith}, Any]],
                                               Callable[[Any], bool], Callable[[Any], Any], Callable[
                                                   [Optional[{lower}]], Union[
                                                       Union[None, str, int, float], Any]]], Any]]
_validators: dict


def _convert_validator_spec(key: Union[str, Any],
                            conv: Union[Union[Callable[[{startswith, endswith}], Union[{startswith, endswith}, Any]],
                                              Callable[[Any], bool], Callable[[Any], Any], Callable[
                                                  [Optional[{lower}]], Union[
                                                      Union[None, str, int, float], Any]]], Any]) -> Union[
    ValidateInStrings, Callable[[{startswith, endswith}], Union[{startswith, endswith}, Any]], Callable[[Any], bool],
    Callable[[Any], Any], Callable[[Optional[{lower}]], Union[Union[None, str, int, float], Any]]]: ...