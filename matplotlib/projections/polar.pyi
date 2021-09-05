from matplotlib.path import Path as Path
from matplotlib.axes import Axes as Axes
from matplotlib import rcParams as rcParams
from matplotlib import cbook as cbook
from matplotlib import _api as _api
from collections import OrderedDict as OrderedDict
from collections import OrderedDict
from typing import Any
from typing import ClassVar
from typing import Optional
from typing import OrderedDict
from typing import Tuple
from typing import Union

from matplotlib import _api
from matplotlib.axes._axes import Axes
from matplotlib.axis import XAxis
from matplotlib.axis import XTick
from matplotlib.axis import YAxis
from matplotlib.axis import YTick
from matplotlib.patches import Wedge
from matplotlib.path import Path
from matplotlib.projections.polar import InvertedPolarTransform
from matplotlib.projections.polar import PolarAffine
from matplotlib.projections.polar import PolarAxes
from matplotlib.projections.polar import PolarTransform
from matplotlib.projections.polar import RadialAxis
from matplotlib.projections.polar import RadialLocator
from matplotlib.projections.polar import RadialTick
from matplotlib.projections.polar import ThetaAxis
from matplotlib.projections.polar import ThetaFormatter
from matplotlib.projections.polar import ThetaLocator
from matplotlib.projections.polar import ThetaTick
from matplotlib.projections.polar import _AxisWrapper
from matplotlib.projections.polar import _ThetaShift
from matplotlib.projections.polar import _WedgeBbox
from matplotlib.ticker import Formatter
from matplotlib.ticker import Locator
from matplotlib.transforms import Affine2DBase
from matplotlib.transforms import Bbox
from matplotlib.transforms import CompositeAffine2D
from matplotlib.transforms import CompositeGenericTransform
from matplotlib.transforms import ScaledTranslation
from matplotlib.transforms import Transform
from matplotlib.transforms import TransformWrapper
from object import object


class PolarTransform(Transform):
    input_dims: ClassVar[int]
    output_dims: ClassVar[int]
    __str__: ClassVar[Callable[[Any], Any]]
    _use_rmin: bool
    _axis: Any
    _apply_theta_transforms: bool

    def __init__(self: PolarTransform,
                 axis: Any = None,
                 use_rmin: bool = True,
                 _apply_theta_transforms: bool = True) -> None: ...

    def transform_non_affine(self: PolarTransform,
                             tr: Any) -> Any: ...

    def transform_path_non_affine(self: PolarTransform,
                                  path: {vertices, codes}) -> Path: ...

    def inverted(self: PolarTransform) -> InvertedPolarTransform: ...


class PolarAffine(Affine2DBase):
    __str__: ClassVar[Callable[[Any], Any]]
    _scale_transform: Any
    _limits: Any
    _invalid: int
    _inverted: None
    _mtx: None

    def __init__(self: PolarAffine,
                 scale_transform: Any,
                 limits: Any) -> None: ...

    def get_matrix(self: PolarAffine) -> Any: ...


class InvertedPolarTransform(Transform):
    input_dims: ClassVar[int]
    output_dims: ClassVar[int]
    __str__: ClassVar[Callable[[Any], Any]]
    _use_rmin: bool
    _axis: Any
    _apply_theta_transforms: bool

    def __init__(self: InvertedPolarTransform,
                 axis: Any = None,
                 use_rmin: bool = True,
                 _apply_theta_transforms: bool = True) -> None: ...

    def transform_non_affine(self: InvertedPolarTransform,
                             xy: {T}) -> Any: ...

    def inverted(self: InvertedPolarTransform) -> PolarTransform: ...


class ThetaFormatter(Formatter):
    def __call__(self: ThetaFormatter,
                 x: Any,
                 pos: Any = None) -> str: ...


class _AxisWrapper(object):
    _axis: Any

    def __init__(self: _AxisWrapper,
                 axis: Any) -> None: ...

    def get_view_interval(self: _AxisWrapper) -> Any: ...

    def set_view_interval(self: _AxisWrapper,
                          vmin: Any,
                          vmax: Any) -> None: ...

    def get_minpos(self: _AxisWrapper) -> Any: ...

    def get_data_interval(self: _AxisWrapper) -> Any: ...

    def set_data_interval(self: _AxisWrapper,
                          vmin: Any,
                          vmax: Any) -> None: ...

    def get_tick_space(self: _AxisWrapper) -> Any: ...


class ThetaLocator(Locator):
    axis: _AxisWrapper
    base: Any

    def __init__(self: ThetaLocator,
                 base: Any) -> None: ...

    def set_axis(self: ThetaLocator,
                 axis: Any) -> None: ...

    def __call__(self: ThetaLocator) -> Union[float, Any]: ...

    @_api.deprecated("3.3")
    def pan(self: ThetaLocator,
            numsteps: Any) -> Any: ...

    def refresh(self: ThetaLocator) -> Any: ...

    def view_limits(self: ThetaLocator,
                    vmin: Any,
                    vmax: Any) -> Any: ...

    @_api.deprecated("3.3")
    def zoom(self: ThetaLocator,
             direction: Any) -> Any: ...


class ThetaTick(XTick):
    _text2_translate: ScaledTranslation
    _text1_translate: ScaledTranslation

    def __init__(self: ThetaTick,
                 axes: {figure},
                 *args,
                 **kwargs) -> None: ...

    def _apply_params(self: ThetaTick,
                      **kwargs) -> None: ...

    def _update_padding(self: ThetaTick,
                        pad: Union[int, Any],
                        angle: Any) -> None: ...

    def update_position(self: ThetaTick,
                        loc: {__mul__}) -> None: ...


class ThetaAxis(XAxis):
    __name__: ClassVar[str]
    axis_name: ClassVar[str]
    isDefault_majloc: bool
    isDefault_majfmt: bool

    def _get_tick(self: ThetaAxis,
                  major: Any) -> ThetaTick: ...

    def _wrap_locator_formatter(self: ThetaAxis) -> None: ...

    def clear(self: ThetaAxis) -> None: ...

    @_api.deprecated("3.4", alternative="ThetaAxis.clear()")
    def cla(self: ThetaAxis) -> Optional[Any]: ...

    def _set_scale(self: ThetaAxis,
                   value: Any,
                   **kwargs) -> None: ...

    def _copy_tick_props(self: ThetaAxis,
                         src: Optional[{label1, label2, tick1line, tick2line, gridline}],
                         dest: Optional[{label1, label2, tick1line, tick2line, gridline}]) -> None: ...


class RadialLocator(Locator):
    _axes: Any
    base: Any

    def __init__(self: RadialLocator,
                 base: Any,
                 axes: Any = None) -> None: ...

    def __call__(self: RadialLocator) -> Union[list[Any], Any]: ...

    @_api.deprecated("3.3")
    def pan(self: RadialLocator,
            numsteps: Any) -> Any: ...

    @_api.deprecated("3.3")
    def zoom(self: RadialLocator,
             direction: Any) -> Any: ...

    @_api.deprecated("3.3")
    def refresh(self: RadialLocator) -> Any: ...

    def nonsingular(self: RadialLocator,
                    vmin: Any,
                    vmax: Any) -> Union[Tuple[int, int], Any]: ...

    def view_limits(self: RadialLocator,
                    vmin: Any,
                    vmax: Any) -> float: ...


class _ThetaShift(ScaledTranslation):
    __str__: ClassVar[Callable[[Any], Any]]
    mode: str
    pad: float
    _t: tuple[Union[float, Any], Union[float, Any]]
    axes: Any

    def __init__(self: _ThetaShift,
                 axes: Any,
                 pad: float,
                 mode: str) -> None: ...

    def get_matrix(self: _ThetaShift) -> Any: ...


class RadialTick(YTick):
    def __init__(self: RadialTick,
                 *args,
                 **kwargs) -> None: ...

    def _determine_anchor(self: RadialTick,
                          mode: Union[str, Any],
                          angle: Union[int, Any],
                          start: Any) -> Tuple[str, str]: ...

    def update_position(self: RadialTick,
                        loc: Any) -> None: ...


class RadialAxis(YAxis):
    __name__: ClassVar[str]
    axis_name: ClassVar[str]
    isDefault_majloc: bool

    def __init__(self: RadialAxis,
                 *args,
                 **kwargs) -> None: ...

    def _get_tick(self: RadialAxis,
                  major: Any) -> RadialTick: ...

    def _wrap_locator_formatter(self: RadialAxis) -> None: ...

    def clear(self: RadialAxis) -> None: ...

    @_api.deprecated("3.4", alternative="RadialAxis.clear()")
    def cla(self: RadialAxis) -> Optional[Any]: ...

    def _set_scale(self: RadialAxis,
                   value: Any,
                   **kwargs) -> None: ...


def _is_full_circle_deg(thetamin: Any,
                        thetamax: {__sub__}) -> Union[bool, Any]: ...


def _is_full_circle_rad(thetamin: Any,
                        thetamax: {__sub__}) -> Union[bool, Any]: ...


class _WedgeBbox(Bbox):
    __str__: ClassVar[Callable[[Any], Any]]
    _originLim: Any
    _center: tuple[float, float]
    _invalid: int
    _viewLim: Any

    def __init__(self: _WedgeBbox,
                 center: tuple[float, float],
                 viewLim: Any,
                 originLim: Any,
                 **kwargs) -> None: ...

    def get_points(self: _WedgeBbox) -> Any: ...


class PolarAxes(Axes):
    name: ClassVar[str]
    transAxes: BboxTransformTo
    _direction: Affine2D
    transShift: Union[{input_dims, output_dims}, {output_dims,
                                                  input_dims}, CompositeAffine2D, CompositeGenericTransform, _NotImplementedType]
    _yaxis_transform: Union[Union[{input_dims, output_dims}, {output_dims,
                                                              input_dims}, CompositeAffine2D, CompositeGenericTransform, _NotImplementedType], Any]
    yaxis: RadialAxis
    axesLim: _WedgeBbox
    _theta_offset: Affine2D
    _xaxis_transform: Union[Union[{input_dims, output_dims}, {output_dims,
                                                              input_dims}, CompositeAffine2D, CompositeGenericTransform, _NotImplementedType], Any]
    _default_rlabel_position: Any
    _r_label_position: Affine2D
    xaxis: ThetaAxis
    use_sticky_edges: bool
    _default_theta_offset: int
    _yaxis_text_transform: TransformWrapper
    _originViewLim: LockableBbox
    _xaxis_text_transform: Union[Union[{input_dims, output_dims}, {output_dims,
                                                                   input_dims}, CompositeAffine2D, CompositeGenericTransform, _NotImplementedType], Any]
    _pan_start: SimpleNamespace
    transWedge: BboxTransformFrom
    transProjection: Any
    _realViewLim: TransformedBbox
    _default_theta_direction: int
    transData: Union[Union[{input_dims, output_dims}, {output_dims,
                                                       input_dims}, CompositeAffine2D, CompositeGenericTransform, _NotImplementedType], Any]
    transProjectionAffine: Any
    transScale: TransformWrapper

    def __init__(self: PolarAxes,
                 theta_offset: int = 0,
                 theta_direction: int = 1,
                 rlabel_position: float = 22.5,
                 *args,
                 **kwargs) -> None: ...

    def cla(self: PolarAxes) -> None: ...

    def _init_axis(self: PolarAxes) -> None: ...

    def _set_lim_and_transforms(self: PolarAxes) -> None: ...

    def get_xaxis_transform(self: PolarAxes,
                            which: str = 'grid') -> Union[Union[{input_dims, output_dims}, {output_dims,
                                                                                            input_dims}, CompositeAffine2D, CompositeGenericTransform, _NotImplementedType], Any]: ...

    def get_xaxis_text1_transform(self: PolarAxes,
                                  pad: Any) -> Tuple[Union[Union[{input_dims, output_dims}, {output_dims,
                                                                                             input_dims}, CompositeAffine2D, CompositeGenericTransform, _NotImplementedType], Any], str, str]: ...

    def get_xaxis_text2_transform(self: PolarAxes,
                                  pad: Any) -> Tuple[Union[Union[{input_dims, output_dims}, {output_dims,
                                                                                             input_dims}, CompositeAffine2D, CompositeGenericTransform, _NotImplementedType], Any], str, str]: ...

    def get_yaxis_transform(self: PolarAxes,
                            which: str = 'grid') -> Union[Union[
                                                              TransformWrapper, {input_dims, output_dims}, {output_dims,
                                                                                                            input_dims}, CompositeAffine2D, CompositeGenericTransform, _NotImplementedType], Any]: ...

    def get_yaxis_text1_transform(self: PolarAxes,
                                  pad: Union[float, Any]) -> Union[Tuple[TransformWrapper, str, str], Tuple[Union[{
                                                                                                                      input_dims,
                                                                                                                      output_dims}, {
                                                                                                                      output_dims,
                                                                                                                      input_dims}, CompositeAffine2D, CompositeGenericTransform, _NotImplementedType], str, str]]: ...

    def get_yaxis_text2_transform(self: PolarAxes,
                                  pad: Union[float, Any]) -> Tuple[Union[{input_dims, output_dims}, {output_dims,
                                                                                                     input_dims}, CompositeAffine2D, CompositeGenericTransform, _NotImplementedType], str, str]: ...

    @_api.delete_parameter("3.3", "args")
    @_api.delete_parameter("3.3", "kwargs")
    def draw(self: PolarAxes,
             renderer: Optional[{open_group, option_image_nocomposite, close_group}],
             *args,
             **kwargs) -> Optional[Any]: ...

    def _gen_axes_patch(self: PolarAxes) -> Wedge: ...

    def _gen_axes_spines(self: PolarAxes) -> OrderedDict[str, Spine]: ...

    def set_thetamax(self: PolarAxes,
                     thetamax: Any) -> None: ...

    def get_thetamax(self: PolarAxes) -> Any: ...

    def set_thetamin(self: PolarAxes,
                     thetamin: Any) -> None: ...

    def get_thetamin(self: PolarAxes) -> Any: ...

    def set_thetalim(self: PolarAxes,
                     *args,
                     **kwargs) -> Tuple: ...

    def set_theta_offset(self: PolarAxes,
                         offset: Union[int, Any]) -> None: ...

    def get_theta_offset(self: PolarAxes) -> Any: ...

    def set_theta_zero_location(self: PolarAxes,
                                loc: str,
                                offset: float = 0.0) -> None: ...

    def set_theta_direction(self: PolarAxes,
                            direction: Union[int, Any]) -> None: ...

    def get_theta_direction(self: PolarAxes) -> Any: ...

    def set_rmax(self: PolarAxes,
                 rmax: float) -> None: ...

    def get_rmax(self: PolarAxes) -> float: ...

    def set_rmin(self: PolarAxes,
                 rmin: float) -> None: ...

    def get_rmin(self: PolarAxes) -> float: ...

    def set_rorigin(self: PolarAxes,
                    rorigin: float) -> None: ...

    def get_rorigin(self: PolarAxes) -> float: ...

    def get_rsign(self: PolarAxes) -> Any: ...

    def set_rlim(self: PolarAxes,
                 bottom: Any = None,
                 top: Any = None,
                 emit: bool = True,
                 auto: bool = False,
                 **kwargs) -> Tuple[float, float]: ...

    def set_ylim(self: PolarAxes,
                 bottom: Optional[float] = None,
                 top: Optional[float] = None,
                 emit: bool = True,
                 auto: Optional[bool] = False,
                 *,
                 ymin: Optional[float] = None,
                 ymax: Optional[float] = None) -> Tuple[float, float]: ...

    def get_rlabel_position(self: PolarAxes) -> float: ...

    def set_rlabel_position(self: PolarAxes,
                            value: Union[int, float, complex]) -> None: ...

    def set_yscale(self: PolarAxes,
                   *args,
                   **kwargs) -> None: ...

    def set_rscale(self: PolarAxes,
                   *args,
                   **kwargs) -> None: ...

    def set_rticks(self: PolarAxes,
                   *args,
                   **kwargs) -> Any: ...

    def set_thetagrids(self: PolarAxes,
                       angles: Any,
                       labels: Any = None,
                       fmt: Optional[str] = None,
                       x: Any = ...,
                       y: Any = ...,
                       text: str = ...,
                       color: Any = ...,
                       verticalalignment: Any = ...,
                       horizontalalignment: Any = ...,
                       multialignment: Any = ...,
                       fontproperties: Any = ...,
                       rotation: Union[float, Any] = ...,
                       linespacing: Any = ...,
                       rotation_mode: Optional[str] = ...,
                       usetex: Any = ...,
                       wrap: bool = ...,
                       transform_rotates_text: bool = ...,
                       **kwargs) -> Any: ...

    def set_rgrids(self: PolarAxes,
                   radii: Any,
                   labels: Any = None,
                   angle: float = None,
                   fmt: Optional[str] = None,
                   x: Any = ...,
                   y: Any = ...,
                   text: str = ...,
                   color: Any = ...,
                   verticalalignment: Any = ...,
                   horizontalalignment: Any = ...,
                   multialignment: Any = ...,
                   fontproperties: Any = ...,
                   rotation: Union[float, Any] = ...,
                   linespacing: Any = ...,
                   rotation_mode: Optional[str] = ...,
                   usetex: Any = ...,
                   wrap: bool = ...,
                   transform_rotates_text: bool = ...,
                   **kwargs) -> Any: ...

    def set_xscale(self: PolarAxes,
                   scale: {__ne__},
                   *args,
                   **kwargs) -> Any: ...

    def format_coord(self: PolarAxes,
                     theta: {__lt__, __mul__},
                     r: Any) -> str: ...

    def get_data_ratio(self: PolarAxes) -> float: ...

    def can_zoom(self: PolarAxes) -> bool: ...

    def can_pan(self: PolarAxes) -> bool: ...

    def start_pan(self: PolarAxes,
                  x: float,
                  y: float,
                  button: {__eq__}) -> None: ...

    def end_pan(self: PolarAxes) -> None: ...

    def drag_pan(self: PolarAxes,
                 button: Any,
                 key: Optional[str],
                 x: float,
                 y: float) -> None: ...


PolarTransform: Type[PolarTransform]
PolarAffine: Type[PolarAffine]
InvertedPolarTransform: Type[InvertedPolarTransform]
ThetaFormatter: Type[ThetaFormatter]
RadialLocator: Type[RadialLocator]
ThetaLocator: Type[ThetaLocator]
