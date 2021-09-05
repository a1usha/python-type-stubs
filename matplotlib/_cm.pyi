from functools import partial as partial
from typing import Any
from typing import Union

_autumn_data: dict[str, tuple[tuple[float, float, float], tuple[float, float, float]]]
_bone_data: dict[str, Union[
    tuple[tuple[float, float, float], tuple[float, float, float], tuple[float, float, float]], tuple[
        tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[
            float, float, float]]]]
_cool_data: dict[str, tuple[tuple[float, float, float], tuple[float, float, float]]]
_copper_data: dict[str, Union[
    tuple[tuple[float, float, float], tuple[float, float, float], tuple[float, float, float]], tuple[
        tuple[float, float, float], tuple[float, float, float]]]]
_binary_data: dict[str, tuple[tuple[float, float, float], tuple[float, float, float]]]


def _flag_red(x: {__mul__}) -> Union[float, Any]: ...


def _flag_green(x: {__mul__}) -> Any: ...


_flag_data: dict[str, Union[
    Callable[[{__mul__}], Union[float, Any]], Callable[[{__mul__}], Union[float, Any]], Callable[[{__mul__}], Any]]]


def _flag_blue(x: {__mul__}) -> Union[float, Any]: ...


def _prism_red(x: {__mul__}) -> Union[float, Any]: ...


def _prism_green(x: {__mul__}) -> Union[float, Any]: ...


_prism_data: dict[str, Union[
    Callable[[{__mul__}], Union[float, Any]], Callable[[{__mul__}], Union[float, Any]], Callable[
        [{__mul__}], Union[float, Any]]]]


def _prism_blue(x: {__mul__}) -> Union[float, Any]: ...


def _ch_helper(gamma: Any,
               s: {__truediv__},
               r: {__mul__},
               h: {__mul__},
               p0: {__mul__},
               p1: {__mul__},
               x: {__pow__}) -> Union[float, Any]: ...


_cubehelix_data: dict[str, partial[Union[float, Any]]]

_bwr_data: tuple[tuple[float, float, float], tuple[float, float, float], tuple[float, float, float]]

_brg_data: tuple[tuple[float, float, float], tuple[float, float, float], tuple[float, float, float]]


def cubehelix(gamma: float = 1.0,
              s: float = 0.5,
              r: float = -1.5,
              h: float = 1.0) -> dict[str, partial[Union[float, Any]]]: ...


def _g0(x: Any) -> int: ...


def _g1(x: Any) -> float: ...


def _g2(x: Any) -> int: ...


def _g3(x: Any) -> Any: ...


def _g4(x: {__pow__}) -> Any: ...


def _g5(x: {__pow__}) -> Any: ...


def _g6(x: {__pow__}) -> Any: ...


def _g7(x: Any) -> Any: ...


def _g8(x: Any) -> Any: ...


def _g9(x: {__mul__}) -> Any: ...


def _g10(x: {__mul__}) -> Any: ...


def _g11(x: {__sub__}) -> Any: ...


def _g12(x: Any) -> Any: ...


def _g13(x: {__mul__}) -> Any: ...


def _g14(x: {__mul__}) -> Any: ...


def _g15(x: {__mul__}) -> Any: ...


def _g16(x: {__mul__}) -> Any: ...


def _g17(x: {__mul__}) -> Any: ...


def _g18(x: {__mul__}) -> Any: ...


def _g19(x: {__mul__}) -> Any: ...


def _g20(x: {__mul__}) -> Any: ...


def _g21(x: Any) -> Union[int, Any]: ...


def _g22(x: Any) -> Union[int, Any]: ...


def _g23(x: Any) -> Union[int, Any]: ...


def _g24(x: Any) -> Any: ...


def _g25(x: Any) -> Any: ...


def _g26(x: Any) -> Union[float, Any]: ...


def _g27(x: Any) -> Union[float, Any]: ...


def _g28(x: Any) -> Any: ...


def _g29(x: Any) -> Any: ...


def _g30(x: {__truediv__}) -> Union[float, Any]: ...


def _g31(x: Any) -> Union[float, Any]: ...


def _g32(x: {__len__, __lt__, __getitem__, __ge__}) -> Any: ...


def _g33(x: Any) -> Any: ...


def _g34(x: Any) -> Union[int, Any]: ...


def _g35(x: Any) -> Union[float, Any]: ...


gfunc: dict

_gnuplot_data: dict[str, Any]

_gnuplot2_data: dict[str, Any]

_ocean_data: dict[str, Any]

_afmhot_data: dict[str, Any]

_rainbow_data: dict[str, Any]

_seismic_data: tuple[
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float]]

_terrain_data: tuple[tuple[float, tuple[float, float, float]], tuple[float, tuple[float, float, float]], tuple[
    float, tuple[float, float, float]], tuple[float, tuple[float, float, float]], tuple[
                         float, tuple[float, float, float]], tuple[float, tuple[float, float, float]]]

_gray_data: dict[str, tuple[tuple[float, int, int], tuple[float, int, int]]]

_hot_data: dict[str, Union[
    tuple[tuple[float, float, float], tuple[float, float, float], tuple[float, float, float]], tuple[
        tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[
            float, float, float]]]]

_hsv_data: dict[str, Union[tuple[tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
                                 tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
                                 tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
                                 tuple[float, float, float]], tuple[
                               tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
                               tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
                               tuple[float, float, float]]]]

_jet_data: dict[str, Union[tuple[tuple[float, int, int], tuple[float, int, int], tuple[float, int, int], tuple[
    float, int, int], tuple[float, float, float]], tuple[
                               tuple[float, float, float], tuple[float, int, int], tuple[float, int, int], tuple[
                                   float, int, int], tuple[float, int, int]], tuple[
                               tuple[float, int, int], tuple[float, int, int], tuple[float, int, int], tuple[
                                   float, int, int], tuple[float, int, int], tuple[float, int, int]]]]

_pink_data: dict[str, tuple[
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float]]]

_spring_data: dict[str, tuple[tuple[float, float, float], tuple[float, float, float]]]

_summer_data: dict[str, tuple[tuple[float, float, float], tuple[float, float, float]]]

_winter_data: dict[str, tuple[tuple[float, float, float], tuple[float, float, float]]]

_nipy_spectral_data: dict[str, list[Union[tuple[float, float, float], Any]]]

_Blues_data: tuple[
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float]]

_BrBG_data: tuple[
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float]]

_BuGn_data: tuple[
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float]]

_BuPu_data: tuple[
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float]]

_GnBu_data: tuple[
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float]]

_Greens_data: tuple[
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float]]

_Greys_data: tuple[
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float]]

_Oranges_data: tuple[
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float]]

_OrRd_data: tuple[
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float]]

_PiYG_data: tuple[
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float]]

_PRGn_data: tuple[
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float]]

_PuBu_data: tuple[
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float]]

_PuBuGn_data: tuple[
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float]]

_PuOr_data: tuple[
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float]]

_PuRd_data: tuple[
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float]]

_Purples_data: tuple[
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float]]

_RdBu_data: tuple[
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float]]

_RdGy_data: tuple[
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float]]

_RdPu_data: tuple[
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float]]

_RdYlBu_data: tuple[
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float]]

_RdYlGn_data: tuple[
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float]]

_Reds_data: tuple[
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float]]

_Spectral_data: tuple[
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float]]

_YlGn_data: tuple[
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float]]

_YlGnBu_data: tuple[
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float]]

_YlOrBr_data: tuple[
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float]]

_YlOrRd_data: tuple[
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float]]

_Accent_data: tuple[
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float]]

_Dark2_data: tuple[
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float]]

_Paired_data: tuple[
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float]]

_Pastel1_data: tuple[
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float]]

_Pastel2_data: tuple[
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float]]

_Set1_data: tuple[
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float]]

_Set2_data: tuple[
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float]]

_Set3_data: tuple[
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float]]

_gist_earth_data: dict[str, Union[tuple[tuple[float, float, float], tuple[float, float, float], tuple[
    float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[
                                            float, float, float]], tuple[
                                      tuple[float, float, float], tuple[float, float, float], tuple[
                                          float, float, float], tuple[float, float, float], tuple[float, float, float],
                                      tuple[float, float, float], tuple[float, float, float], tuple[
                                          float, float, float], tuple[float, float, float], tuple[float, float, float],
                                      tuple[float, float, float]], tuple[
                                      tuple[float, float, float], tuple[float, float, float], tuple[
                                          float, float, float], tuple[float, float, float], tuple[float, float, float],
                                      tuple[float, float, float], tuple[float, float, float], tuple[
                                          float, float, float], tuple[float, float, float], tuple[float, float, float],
                                      tuple[float, float, float], tuple[float, float, float], tuple[
                                          float, float, float], tuple[float, float, float], tuple[float, float, float],
                                      tuple[float, float, float], tuple[float, float, float], tuple[
                                          float, float, float], tuple[float, float, float], tuple[float, float, float],
                                      tuple[float, float, float], tuple[float, float, float], tuple[
                                          float, float, float]]]]

_gist_gray_data: dict[str, Any]


def _g36(x: Any) -> Union[int, Any]: ...


def _gist_heat_red(x: Any) -> Union[float, Any]: ...


def _gist_heat_green(x: Any) -> Union[int, Any]: ...


_gist_heat_data: dict[
    str, Union[Callable[[Any], Union[float, Any]], Callable[[Any], Union[int, Any]], Callable[[Any], Union[int, Any]]]]

_gist_ncar_data: dict[str, Union[tuple[
                                     tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
                                     tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
                                     tuple[float, float, float], tuple[float, float, float], tuple[
                                         float, float, float]], tuple[
                                     tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
                                     tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
                                     tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
                                     tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
                                     tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
                                     tuple[float, float, float], tuple[float, float, float], tuple[
                                         float, float, float]], tuple[
                                     tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
                                     tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
                                     tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
                                     tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
                                     tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
                                     tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
                                     tuple[float, float, float], tuple[float, float, float]]]]

_gist_rainbow_data: tuple[tuple[float, tuple[float, float, float]], tuple[float, tuple[float, float, float]], tuple[
    float, tuple[float, float, float]], tuple[float, tuple[float, float, float]], tuple[
                              float, tuple[float, float, float]], tuple[float, tuple[float, float, float]], tuple[
                              float, tuple[float, float, float]], tuple[float, tuple[float, float, float]]]

_gist_stern_data: dict[str, Union[tuple[tuple[float, float, float], tuple[float, float, float], tuple[
    float, float, float], tuple[float, float, float]], tuple[tuple[int, int, int], tuple[int, int, int]]]]


def _gist_heat_blue(x: Any) -> Union[int, Any]: ...


_gist_yarg_data: dict[str, Callable[[Any], Union[int, Any]]]

_coolwarm_data: dict[str, list[Union[tuple[float, float, float], Any]]]

_CMRmap_data: dict[str, tuple[
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float]]]

_wistia_data: dict[str, list[tuple[float, float, float]]]

_tab10_data: tuple[
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float], tuple[float, float, float]]

_tab20_data: tuple[
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float]]

_tab20b_data: tuple[
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float]]

_tab20c_data: tuple[
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float]]

datad: dict[Union[str, Any], Union[Union[tuple[tuple[float, float, float], tuple[float, float, float], tuple[
    float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[
                                                   float, float, float], tuple[float, float, float], tuple[
                                                   float, float, float]], tuple[
                                             tuple[float, float, float], tuple[float, float, float], tuple[
                                                 float, float, float], tuple[float, float, float], tuple[
                                                 float, float, float], tuple[float, float, float], tuple[
                                                 float, float, float], tuple[float, float, float], tuple[
                                                 float, float, float], tuple[float, float, float], tuple[
                                                 float, float, float]], dict[str, tuple[
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float], tuple[float, float, float], tuple[float, float, float], tuple[float, float, float],
    tuple[float, float, float]]]], Any]]


def _gist_yarg(x: Any) -> Union[int, Any]: ...