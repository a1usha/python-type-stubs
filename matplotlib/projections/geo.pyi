from matplotlib.transforms import Transform as Transform
from matplotlib.transforms import BboxTransformTo as BboxTransformTo
from matplotlib.transforms import Affine2D as Affine2D
from matplotlib.ticker import NullFormatter as NullFormatter
from matplotlib.ticker import FixedLocator as FixedLocator
from matplotlib.ticker import NullLocator as NullLocator
from matplotlib.ticker import Formatter as Formatter
from matplotlib.path import Path as Path
from matplotlib.patches import Circle as Circle
from matplotlib.axes import Axes as Axes
from matplotlib import rcParams as rcParams
from matplotlib import _api as _api
from typing import Any
from typing import ClassVar
from typing import Optional
from typing import Tuple
from typing import Union

from matplotlib.axes._axes import Axes
from matplotlib.patches import Circle
from matplotlib.path import Path
from matplotlib.projections.geo import AitoffAxes
from matplotlib.projections.geo import GeoAxes
from matplotlib.projections.geo import HammerAxes
from matplotlib.projections.geo import LambertAxes
from matplotlib.projections.geo import MollweideAxes
from matplotlib.projections.geo import _GeoTransform
from matplotlib.projections.geo.AitoffAxes import AitoffTransform
from matplotlib.projections.geo.HammerAxes import HammerTransform
from matplotlib.projections.geo.LambertAxes import LambertTransform
from matplotlib.projections.geo.MollweideAxes import MollweideTransform
from matplotlib.transforms import Affine2D
from matplotlib.transforms import CompositeAffine2D
from matplotlib.transforms import CompositeGenericTransform
from matplotlib.transforms import Transform


class GeoAxes(Axes):
    RESOLUTION: ClassVar[int]
    set_xscale: ClassVar[Callable[[GeoAxes, tuple[Any, ...], dict[str, Any]], Any]]
    set_ylim: ClassVar[Callable[[GeoAxes, tuple[Any, ...], dict[str, Any]], Any]]
    transAxes: BboxTransformTo
    _longitude_cap: Any
    _xaxis_text2_transform: Union[Union[{input_dims, output_dims}, {output_dims,
                                                                    input_dims}, CompositeAffine2D, CompositeGenericTransform, _NotImplementedType], Any]
    _xaxis_text1_transform: Union[Union[{input_dims, output_dims}, {output_dims,
                                                                    input_dims}, CompositeAffine2D, CompositeGenericTransform, _NotImplementedType], Any]
    _yaxis_transform: Union[Union[{input_dims, output_dims}, {output_dims,
                                                              input_dims}, CompositeAffine2D, CompositeGenericTransform, _NotImplementedType], Any]
    yaxis: YAxis
    _yaxis_text2_transform: Union[Union[{input_dims, output_dims}, {output_dims,
                                                                    input_dims}, CompositeAffine2D, CompositeGenericTransform, _NotImplementedType], Any]
    transAffine: Affine2D
    _xaxis_pretransform: Affine2D
    _xaxis_transform: Union[Union[{input_dims, output_dims}, {output_dims,
                                                              input_dims}, CompositeAffine2D, CompositeGenericTransform, _NotImplementedType], Any]
    xaxis: XAxis
    _yaxis_text1_transform: Union[Union[{input_dims, output_dims}, {output_dims,
                                                                    input_dims}, CompositeAffine2D, CompositeGenericTransform, _NotImplementedType], Any]
    transProjection: Any
    transData: Any

    def _init_axis(self: GeoAxes) -> None: ...

    def cla(self: GeoAxes) -> None: ...

    def _set_lim_and_transforms(self: GeoAxes) -> None: ...

    def _get_affine_transform(self: GeoAxes) -> Affine2D: ...

    def get_xaxis_transform(self: GeoAxes,
                            which: str = 'grid') -> Union[Union[{input_dims, output_dims}, {output_dims,
                                                                                            input_dims}, CompositeAffine2D, CompositeGenericTransform, _NotImplementedType], Any]: ...

    def get_xaxis_text1_transform(self: GeoAxes,
                                  pad: Any) -> Tuple[Union[Union[{input_dims, output_dims}, {output_dims,
                                                                                             input_dims}, CompositeAffine2D, CompositeGenericTransform, _NotImplementedType], Any], str, str]: ...

    def get_xaxis_text2_transform(self: GeoAxes,
                                  pad: Any) -> Tuple[Union[Union[{input_dims, output_dims}, {output_dims,
                                                                                             input_dims}, CompositeAffine2D, CompositeGenericTransform, _NotImplementedType], Any], str, str]: ...

    def get_yaxis_transform(self: GeoAxes,
                            which: str = 'grid') -> Union[Union[{input_dims, output_dims}, {output_dims,
                                                                                            input_dims}, CompositeAffine2D, CompositeGenericTransform, _NotImplementedType], Any]: ...

    def get_yaxis_text1_transform(self: GeoAxes,
                                  pad: Any) -> Tuple[Union[Union[{input_dims, output_dims}, {output_dims,
                                                                                             input_dims}, CompositeAffine2D, CompositeGenericTransform, _NotImplementedType], Any], str, str]: ...

    def get_yaxis_text2_transform(self: GeoAxes,
                                  pad: Any) -> Tuple[Union[Union[{input_dims, output_dims}, {output_dims,
                                                                                             input_dims}, CompositeAffine2D, CompositeGenericTransform, _NotImplementedType], Any], str, str]: ...

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
                           degrees: Union[int, Any]) -> None: ...

    def set_latitude_grid(self: GeoAxes,
                          degrees: Union[int, Any]) -> None: ...

    def set_longitude_grid_ends(self: GeoAxes,
                                degrees: Union[int, Any]) -> None: ...

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


class _GeoTransform(Transform):
    input_dims: ClassVar[int]
    output_dims: ClassVar[int]
    _resolution: Any

    def __init__(self: _GeoTransform,
                 resolution: Any) -> None: ...

    def __str__(self: _GeoTransform) -> str: ...

    def transform_path_non_affine(self: _GeoTransform,
                                  path: {vertices, codes}) -> Path: ...


class AitoffAxes(GeoAxes):
    name: ClassVar[str]
    _longitude_cap: Union[float, Any]

    def __init__(self: AitoffAxes,
                 *args,
                 **kwargs) -> None: ...

    def _get_core_transform(self: AitoffAxes,
                            resolution: Any) -> AitoffTransform: ...


class HammerAxes(GeoAxes):
    name: ClassVar[str]
    _longitude_cap: Union[float, Any]

    def __init__(self: HammerAxes,
                 *args,
                 **kwargs) -> None: ...

    def _get_core_transform(self: HammerAxes,
                            resolution: Any) -> HammerTransform: ...


class MollweideAxes(GeoAxes):
    name: ClassVar[str]
    _longitude_cap: Union[float, Any]

    def __init__(self: MollweideAxes,
                 *args,
                 **kwargs) -> None: ...

    def _get_core_transform(self: MollweideAxes,
                            resolution: Any) -> MollweideTransform: ...


class LambertAxes(GeoAxes):
    name: ClassVar[str]
    _center_latitude: int
    _longitude_cap: Union[float, Any]
    _center_longitude: int

    def __init__(self: LambertAxes,
                 center_longitude: int = 0,
                 center_latitude: int = 0,
                 *args,
                 **kwargs) -> None: ...

    def cla(self: LambertAxes) -> None: ...

    def _get_core_transform(self: LambertAxes,
                            resolution: Any) -> LambertTransform: ...

    def _get_affine_transform(self: LambertAxes) -> Affine2D: ...
