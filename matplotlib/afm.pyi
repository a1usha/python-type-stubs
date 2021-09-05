from _mathtext_data import uni2type1 as uni2type1
from collections import namedtuple as namedtuple
from typing import Any
from typing import Tuple
from typing import Union

from matplotlib.afm import AFM
from object import object


def _to_int(x: Any) -> int: ...


def _to_float(x: {replace}) -> float: ...


def _to_str(x: Union[{__len__, __iter__}, Any]) -> Any: ...


def _to_list_of_ints(s: Any) -> list[int]: ...


def _to_list_of_floats(s: {split}) -> list[float]: ...


def _to_bool(s: {lower}) -> bool: ...


CharMetrics: Type[CharMetrics]


def _parse_header(fh: {__iter__}) -> dict[Any, Union[Union[float, bool, list[int]], Any]]: ...


def _parse_char_metrics(fh: Union[{__iter__}, Any]) -> dict: ...


CompositePart: Type[CompositePart]


def _parse_kern_pairs(fh: {__iter__}) -> dict[Tuple[Any, Any], float]: ...


def _parse_composites(fh: {__iter__}) -> dict: ...


def _parse_optional(fh: Union[{__iter__}, Any]) -> dict: ...


class AFM(object):
    _header: dict[Any, Union[Union[float, bool, list[int]], Any]]
    _kern: dict
    _composite: dict
    _metrics: dict
    _metrics_by_name: dict

    def __init__(self: AFM,
                 fh: {__iter__}) -> None: ...

    def get_bbox_char(self: AFM,
                      c: Any,
                      isord: bool = False) -> Any: ...

    def string_width_height(self: AFM,
                            s: {__len__, __iter__}) -> Union[
        Tuple[int, int], Tuple[int, Union[Union[int, float], Any]]]: ...

    def get_str_bbox_and_descent(self: AFM,
                                 s: {__len__, __iter__}) -> Union[Tuple[int, int, int, int, int], Tuple[
        Union[int, Any], Union[float, Any], int, Union[Union[int, float], Any], float]]: ...

    def get_str_bbox(self: AFM,
                     s: Any) -> Tuple: ...

    def get_name_char(self: AFM,
                      c: Any,
                      isord: bool = False) -> Any: ...

    def get_width_char(self: AFM,
                       c: Any,
                       isord: bool = False) -> Any: ...

    def get_width_from_char_name(self: AFM,
                                 name: Any) -> Any: ...

    def get_height_char(self: AFM,
                        c: Any,
                        isord: bool = False) -> Any: ...

    def get_kern_dist(self: AFM,
                      c1: Any,
                      c2: Any) -> Union[int, Any]: ...

    def get_kern_dist_from_name(self: AFM,
                                name1: Any,
                                name2: Any) -> Union[int, Any]: ...

    def get_fontname(self: AFM) -> Union[Union[float, bool, list[int]], Any]: ...

    def postscript_name(self: AFM) -> Union[Union[float, bool, list[int]], Any]: ...

    def get_fullname(self: AFM) -> Union[Union[float, bool, list[int]], Any]: ...

    def get_familyname(self: AFM) -> Union[float, bool, list[int], str]: ...

    def family_name(self: AFM) -> Union[float, bool, list[int], str]: ...

    def get_weight(self: AFM) -> Union[Union[float, bool, list[int]], Any]: ...

    def get_angle(self: AFM) -> Union[Union[float, bool, list[int]], Any]: ...

    def get_capheight(self: AFM) -> Union[Union[float, bool, list[int]], Any]: ...

    def get_xheight(self: AFM) -> Union[Union[float, bool, list[int]], Any]: ...

    def get_underline_thickness(self: AFM) -> Union[Union[float, bool, list[int]], Any]: ...

    def get_horizontal_stem_width(self: AFM) -> Union[Union[float, bool, list[int]], Any]: ...

    def get_vertical_stem_width(self: AFM) -> Union[Union[float, bool, list[int]], Any]: ...
