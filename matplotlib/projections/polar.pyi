from typing import Any
from typing import Optional
from typing import Union


class RadialAxis(YAxis):
    def __init__(self: RadialAxis,
                 *args,
                 **kwargs) -> None: ...

    def _get_tick(self: RadialAxis,
                  major: Any) -> RadialTick: ...

    def _wrap_locator_formatter(self: RadialAxis) -> None: ...

    def clear(self: RadialAxis) -> None: ...

    @_api.deprecated
    def cla(self: RadialAxis) -> Optional[Any]: ...

    def _set_scale(self: RadialAxis,
                   value: Any,
                   **kwargs) -> None: ...


class _WedgeBbox(Bbox):
    def __init__(self: _WedgeBbox,
                 center: tuple[float, float],
                 viewLim: Any,
                 originLim: Any,
                 **kwargs) -> None: ...

    def get_points(self: _WedgeBbox) -> ndarray: ...


class PolarAxes(Axes):
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
                            which: str = 'grid') -> Union[{input_dims, output_dims}, {output_dims,
                                                                                      input_dims}, CompositeAffine2D, CompositeGenericTransform, _NotImplementedType]: ...

    def get_xaxis_text1_transform(self: PolarAxes,
                                  pad: Any) -> tuple[Union[{input_dims, output_dims}, {output_dims,
                                                                                       input_dims}, CompositeAffine2D, CompositeGenericTransform, _NotImplementedType], str, str]: ...

    def get_xaxis_text2_transform(self: PolarAxes,
                                  pad: Any) -> tuple[Union[{input_dims, output_dims}, {output_dims,
                                                                                       input_dims}, CompositeAffine2D, CompositeGenericTransform, _NotImplementedType], str, str]: ...

    def get_yaxis_transform(self: PolarAxes,
                            which: str = 'grid') -> Union[TransformWrapper, {input_dims, output_dims}, {output_dims,
                                                                                                        input_dims}, CompositeAffine2D, CompositeGenericTransform, _NotImplementedType]: ...

    def get_yaxis_text1_transform(self: PolarAxes,
                                  pad: float) -> Union[tuple[TransformWrapper, str, str], tuple[Union[{input_dims,
                                                                                                       output_dims}, {
                                                                                                          output_dims,
                                                                                                          input_dims}, CompositeAffine2D, CompositeGenericTransform, _NotImplementedType], str, str]]: ...

    def get_yaxis_text2_transform(self: PolarAxes,
                                  pad: float) -> tuple[Union[{input_dims, output_dims}, {output_dims,
                                                                                         input_dims}, CompositeAffine2D, CompositeGenericTransform, _NotImplementedType], str, str]: ...

    @_api.delete_parameter
    @_api.delete_parameter
    def draw(self: PolarAxes,
             renderer: Optional[{open_group, option_image_nocomposite, close_group}],
             *args,
             **kwargs) -> Optional[Any]: ...

    def _gen_axes_patch(self: PolarAxes) -> Wedge: ...

    def _gen_axes_spines(self: PolarAxes) -> OrderedDict[str, Spine]: ...

    def set_thetamax(self: PolarAxes,
                     thetamax: Any) -> None: ...

    def get_thetamax(self: PolarAxes) -> None: ...

    def set_thetamin(self: PolarAxes,
                     thetamin: Any) -> None: ...

    def get_thetamin(self: PolarAxes) -> None: ...

    def set_thetalim(self: PolarAxes,
                     *args,
                     **kwargs) -> tuple: ...

    def set_theta_offset(self: PolarAxes,
                         offset: Union[int, float]) -> None: ...

    def get_theta_offset(self: PolarAxes) -> Any: ...

    def set_theta_zero_location(self: PolarAxes,
                                loc: str,
                                offset: float = 0.0) -> None: ...

    def set_theta_direction(self: PolarAxes,
                            direction: int) -> None: ...

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

    def get_rsign(self: PolarAxes) -> None: ...

    def set_rlim(self: PolarAxes,
                 bottom: Any = None,
                 top: Any = None,
                 emit: bool = True,
                 auto: bool = False,
                 **kwargs) -> tuple[float, float]: ...

    def set_ylim(self: PolarAxes,
                 bottom: Optional[float] = None,
                 top: Optional[float] = None,
                 emit: bool = True,
                 auto: Optional[bool] = False,
                 ymin: Optional[float] = None,
                 ymax: Optional[float] = None) -> tuple[float, float]: ...

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
                       fmt: Optional[str] = None x: Any = ...,
                       y: Any = ...,
                       text: str = ...,
                       color: Any = ...,
                       verticalalignment: Any = ...,
                       horizontalalignment: Any = ...,
                       multialignment: Any = ...,
                       fontproperties: Any = ...,
                       rotation: float = ...,
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
                   fmt: Optional[str] = None x: Any = ...,
                   y: Any = ...,
                   text: str = ...,
                   color: Any = ...,
                   verticalalignment: Any = ...,
                   horizontalalignment: Any = ...,
                   multialignment: Any = ...,
                   fontproperties: Any = ...,
                   rotation: float = ...,
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


class RadialTick(YTick):
    def __init__(self: RadialTick,
                 *args,
                 **kwargs) -> None: ...

    def _determine_anchor(self: RadialTick,
                          mode: str,
                          angle: int,
                          start: Any) -> tuple[str, str]: ...

    def update_position(self: RadialTick,
                        loc: Any) -> None: ...


class RadialLocator(Locator):
    def __init__(self: RadialLocator,
                 base: Any,
                 axes: Any = None) -> None: ...

    def __call__(self: RadialLocator) -> list: ...

    @_api.deprecated
    def pan(self: RadialLocator,
            numsteps: Any) -> Any: ...

    @_api.deprecated
    def zoom(self: RadialLocator,
             direction: Any) -> Any: ...

    @_api.deprecated
    def refresh(self: RadialLocator) -> Any: ...

    def nonsingular(self: RadialLocator,
                    vmin: Any,
                    vmax: Any) -> tuple[int, int]: ...

    def view_limits(self: RadialLocator,
                    vmin: Any,
                    vmax: Any) -> float: ...


class PolarTransform(Transform):
    def __init__(self: PolarTransform,
                 axis: Any = None,
                 use_rmin: bool = True,
                 _apply_theta_transforms: bool = True) -> None: ...

    def transform_non_affine(self: PolarTransform,
                             tr: Optional[Any]) -> Any: ...

    def transform_path_non_affine(self: PolarTransform,
                                  path: {vertices, codes}) -> Path: ...

    def inverted(self: PolarTransform) -> InvertedPolarTransform: ...


class _ThetaShift(ScaledTranslation):
    def __init__(self: _ThetaShift,
                 axes: Any,
                 pad: float,
                 mode: str) -> None: ...

    def get_matrix(self: _ThetaShift) -> None: ...


class ThetaTick(XTick):
    def __init__(self: ThetaTick,
                 axes: {figure},
                 *args,
                 **kwargs) -> None: ...

    def _apply_params(self: ThetaTick,
                      **kwargs) -> None: ...

    def _update_padding(self: ThetaTick,
                        pad: Union[float, int],
                        angle: Any) -> None: ...

    def update_position(self: ThetaTick,
                        loc: {__mul__}) -> None: ...


class _AxisWrapper(object):
    def __init__(self: _AxisWrapper,
                 axis: Any) -> None: ...

    def get_view_interval(self: _AxisWrapper) -> None: ...

    def set_view_interval(self: _AxisWrapper,
                          vmin: Any,
                          vmax: Any) -> None: ...

    def get_minpos(self: _AxisWrapper) -> None: ...

    def get_data_interval(self: _AxisWrapper) -> None: ...

    def set_data_interval(self: _AxisWrapper,
                          vmin: Any,
                          vmax: Any) -> None: ...

    def get_tick_space(self: _AxisWrapper) -> Any: ...


class ThetaLocator(Locator):
    def __init__(self: ThetaLocator,
                 base: Any) -> None: ...

    def set_axis(self: ThetaLocator,
                 axis: Any) -> None: ...

    def __call__(self: ThetaLocator) -> Optional[float]: ...

    @_api.deprecated
    def pan(self: ThetaLocator,
            numsteps: Any) -> Any: ...

    def refresh(self: ThetaLocator) -> Any: ...

    def view_limits(self: ThetaLocator,
                    vmin: Any,
                    vmax: Any) -> None: ...

    @_api.deprecated
    def zoom(self: ThetaLocator,
             direction: Any) -> Any: ...


class ThetaAxis(XAxis):
    def _get_tick(self: ThetaAxis,
                  major: Any) -> ThetaTick: ...

    def _wrap_locator_formatter(self: ThetaAxis) -> None: ...

    def clear(self: ThetaAxis) -> None: ...

    @_api.deprecated
    def cla(self: ThetaAxis) -> Optional[Any]: ...

    def _set_scale(self: ThetaAxis,
                   value: Any,
                   **kwargs) -> None: ...

    def _copy_tick_props(self: ThetaAxis,
                         src: Optional[{label1, label2, tick1line, tick2line, gridline}],
                         dest: Optional[{label1, label2, tick1line, tick2line, gridline}]) -> None: ...


class InvertedPolarTransform(Transform):
    def __init__(self: InvertedPolarTransform,
                 axis: Any = None,
                 use_rmin: bool = True,
                 _apply_theta_transforms: bool = True) -> None: ...

    def transform_non_affine(self: InvertedPolarTransform,
                             xy: {T}) -> Any: ...

    def inverted(self: InvertedPolarTransform) -> PolarTransform: ...


class PolarAffine(Affine2DBase):
    def __init__(self: PolarAffine,
                 scale_transform: Any,
                 limits: Any) -> None: ...

    def get_matrix(self: PolarAffine) -> Any: ...


class ThetaFormatter(Formatter):
    def __call__(self: ThetaFormatter,
                 x: Any,
                 pos: Any = None) -> str: ...


def _is_full_circle_deg(thetamin: Any,
                        thetamax: {__sub__}) -> bool: ...


def _is_full_circle_rad(thetamin: Any,
                        thetamax: {__sub__}) -> bool: ...