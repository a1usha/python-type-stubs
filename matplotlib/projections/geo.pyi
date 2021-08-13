from typing import Any
from typing import Optional


class _GeoTransform(Transform):
    def __init__(self: _GeoTransform,
                 resolution: Any) -> None: ...

    def __str__(self: _GeoTransform) -> str: ...

    def transform_path_non_affine(self: _GeoTransform,
                                  path: {vertices, codes}) -> Path: ...


class MollweideTransform(_GeoTransform):
    def transform_non_affine(self: MollweideTransform,
                             ll: {T, shape}) -> ndarray: ...

    def inverted(self: MollweideTransform) -> InvertedMollweideTransform: ...


class InvertedMollweideTransform(_GeoTransform):
    def transform_non_affine(self: InvertedMollweideTransform,
                             xy: {T}) -> Any: ...

    def inverted(self: InvertedMollweideTransform) -> MollweideTransform: ...


class LambertAxes(GeoAxes):
    def __init__(self: LambertAxes,
                 center_longitude: int = 0,
                 center_latitude: int = 0,
                 *args,
                 **kwargs) -> None: ...

    def cla(self: LambertAxes) -> None: ...

    def _get_core_transform(self: LambertAxes,
                            resolution: Any) -> LambertTransform: ...

    def _get_affine_transform(self: LambertAxes) -> Affine2D: ...


class HammerTransform(_GeoTransform):
    def transform_non_affine(self: HammerTransform,
                             ll: {T}) -> Any: ...

    def inverted(self: HammerTransform) -> InvertedHammerTransform: ...


class AitoffAxes(GeoAxes):
    def __init__(self: AitoffAxes,
                 *args,
                 **kwargs) -> None: ...

    def _get_core_transform(self: AitoffAxes,
                            resolution: Any) -> AitoffTransform: ...


class AitoffTransform(_GeoTransform):
    def transform_non_affine(self: AitoffTransform,
                             ll: {T}) -> Any: ...

    def inverted(self: AitoffTransform) -> InvertedAitoffTransform: ...


class InvertedLambertTransform(_GeoTransform):
    def __init__(self: InvertedLambertTransform,
                 center_longitude: Any,
                 center_latitude: Any,
                 resolution: Any) -> None: ...

    def transform_non_affine(self: InvertedLambertTransform,
                             xy: {T}) -> Any: ...

    def inverted(self: InvertedLambertTransform) -> LambertTransform: ...


class LambertTransform(_GeoTransform):
    def __init__(self: LambertTransform,
                 center_longitude: Any,
                 center_latitude: Any,
                 resolution: Any) -> None: ...

    def transform_non_affine(self: LambertTransform,
                             ll: {T}) -> Any: ...

    def inverted(self: LambertTransform) -> InvertedLambertTransform: ...


class InvertedHammerTransform(_GeoTransform):
    def transform_non_affine(self: InvertedHammerTransform,
                             xy: {T}) -> Any: ...

    def inverted(self: InvertedHammerTransform) -> HammerTransform: ...


class InvertedAitoffTransform(_GeoTransform):
    def transform_non_affine(self: InvertedAitoffTransform,
                             xy: Any) -> ndarray: ...

    def inverted(self: InvertedAitoffTransform) -> AitoffTransform: ...


class GeoAxes(Axes):
    def _init_axis(self: GeoAxes) -> None: ...

    def cla(self: GeoAxes) -> None: ...

    def _set_lim_and_transforms(self: GeoAxes) -> None: ...

    def _get_affine_transform(self: GeoAxes) -> Affine2D: ...

    def get_xaxis_transform(self: GeoAxes,
                            which: str = 'grid') -> Union[{input_dims, output_dims}, {output_dims,
                                                                                      input_dims}, CompositeAffine2D, CompositeGenericTransform, _NotImplementedType]: ...

    def get_xaxis_text1_transform(self: GeoAxes,
                                  pad: Any) -> tuple[Union[{input_dims, output_dims}, {output_dims,
                                                                                       input_dims}, CompositeAffine2D, CompositeGenericTransform, _NotImplementedType], str, str]: ...

    def get_xaxis_text2_transform(self: GeoAxes,
                                  pad: Any) -> tuple[Union[{input_dims, output_dims}, {output_dims,
                                                                                       input_dims}, CompositeAffine2D, CompositeGenericTransform, _NotImplementedType], str, str]: ...

    def get_yaxis_transform(self: GeoAxes,
                            which: str = 'grid') -> Union[{input_dims, output_dims}, {output_dims,
                                                                                      input_dims}, CompositeAffine2D, CompositeGenericTransform, _NotImplementedType]: ...

    def get_yaxis_text1_transform(self: GeoAxes,
                                  pad: Any) -> tuple[Union[{input_dims, output_dims}, {output_dims,
                                                                                       input_dims}, CompositeAffine2D, CompositeGenericTransform, _NotImplementedType], str, str]: ...

    def get_yaxis_text2_transform(self: GeoAxes,
                                  pad: Any) -> tuple[Union[{input_dims, output_dims}, {output_dims,
                                                                                       input_dims}, CompositeAffine2D, CompositeGenericTransform, _NotImplementedType], str, str]: ...

    def _gen_axes_patch(self: GeoAxes) -> Circle: ...

    def _gen_axes_spines(self: GeoAxes) -> dict[str, Spine]: ...

    def set_yscale(self: GeoAxes,
                   *args,
                   **kwargs) -> Any: ...

    def set_xlim(self: GeoAxes,
                 *args,
                 **kwargs) -> Any: ...

    def format_coord(self: GeoAxes,
                     lon: Any,
                     lat: Any) -> str: ...

    def set_longitude_grid(self: GeoAxes,
                           degrees: int) -> None: ...

    def set_latitude_grid(self: GeoAxes,
                          degrees: int) -> None: ...

    def set_longitude_grid_ends(self: GeoAxes,
                                degrees: int) -> None: ...

    def get_data_ratio(self: GeoAxes) -> float: ...

    def can_zoom(self: GeoAxes) -> bool: ...

    def can_pan(self: GeoAxes) -> bool: ...

    def start_pan(self: GeoAxes,
                  x: float,
                  y: float,
                  button: Any) -> None: ...

    def end_pan(self: GeoAxes) -> None: ...

    def drag_pan(self: GeoAxes,
                 button: Any,
                 key: Optional[str],
                 x: float,
                 y: float) -> None: ...


class HammerAxes(GeoAxes):
    def __init__(self: HammerAxes,
                 *args,
                 **kwargs) -> None: ...

    def _get_core_transform(self: HammerAxes,
                            resolution: Any) -> HammerTransform: ...


class MollweideAxes(GeoAxes):
    def __init__(self: MollweideAxes,
                 *args,
                 **kwargs) -> None: ...

    def _get_core_transform(self: MollweideAxes,
                            resolution: Any) -> MollweideTransform: ...


class ThetaFormatter(Formatter):
    def __init__(self: ThetaFormatter,
                 round_to: float = 1.0) -> None: ...

    def __call__(self: ThetaFormatter,
                 x: Any,
                 pos: Any = None) -> str: ...
