from matplotlib.path import Path as Path
from matplotlib import transforms as mtransforms
from matplotlib import patches as mpatches
from matplotlib import colors as mcolors
from matplotlib.backend_bases import RendererBase as RendererBase
from typing import Any
from typing import Type
from typing import Union

from matplotlib.backend_bases import RendererBase
from matplotlib.font_manager import FontProperties
from matplotlib.patheffects import AbstractPathEffect
from matplotlib.patheffects import PathEffectRenderer
from matplotlib.patheffects import PathPatchEffect
from matplotlib.patheffects import SimpleLineShadow
from matplotlib.patheffects import SimplePatchShadow
from matplotlib.patheffects import Stroke
from matplotlib.patheffects import TickedStroke
from matplotlib.transforms import Affine2D
from matplotlib.transforms import Transform
from object import object


class AbstractPathEffect(object):
    _offset: int

    def __init__(self: AbstractPathEffect,
                 offset: int = (0., 0.)) -> None: ...

    def _offset_transform(self: AbstractPathEffect,
                          renderer: Union[Union[{draw_path}, {new_gc, draw_path}, {new_gc, draw_path}, {new_gc,
                                                                                                        points_to_pixels,
                                                                                                        draw_path}], Any]) -> Affine2D: ...

    def _update_gc(self: AbstractPathEffect,
                   gc: Any,
                   new_gc_dict: Union[dict[str, Any], Any]) -> Any: ...

    def draw_path(self: AbstractPathEffect,
                  renderer: {draw_path},
                  gc: Any,
                  tpath: Any,
                  affine: Any,
                  rgbFace: Any = None) -> Any: ...


class PathEffectRenderer(RendererBase):
    _path_effects: Any
    _renderer: Any

    def __init__(self: PathEffectRenderer,
                 path_effects: Any,
                 renderer: Any) -> None: ...

    def copy_with_path_effect(self: PathEffectRenderer,
                              path_effects: Union[list[Any], Any]) -> PathEffectRenderer: ...

    def draw_path(self: PathEffectRenderer,
                  gc: Union[{get_rgb, set_linewidth}, Any],
                  tpath: Any,
                  affine: Any,
                  rgbFace: Any = None) -> None: ...

    def draw_markers(self: PathEffectRenderer,
                     gc: Any,
                     marker_path: Any,
                     marker_trans: Transform,
                     path: {iter_segments},
                     *args,
                     **kwargs) -> None: ...

    def draw_path_collection(self: PathEffectRenderer,
                             gc: {_alpha, _forced_alpha, _antialiased, _capstyle, _cliprect, _clippath, _dashes,
                                  _joinstyle, _linestyle, _linewidth, _rgb, _hatch, _hatch_color, _hatch_linewidth,
                                  _url, _gid, _snap, _sketch},
                             master_transform: Any,
                             paths: {__len__, __getitem__},
                             *args,
                             **kwargs) -> None: ...

    def _draw_text_as_path(self: PathEffectRenderer,
                           gc: {get_rgb, set_linewidth},
                           x: Any,
                           y: Any,
                           s: str,
                           prop: FontProperties,
                           angle: Any,
                           ismath: Any) -> None: ...

    def __getattribute__(self: PathEffectRenderer,
                         name: Any) -> Any: ...


class Normal(AbstractPathEffect):
    pass


def _subclass_with_normal(effect_class: Union[Type[Union[Stroke, SimplePatchShadow, TickedStroke]], Any]) -> Type[
    withEffect]: ...


class Stroke(AbstractPathEffect):
    _gc: dict[str, Any]

    def __init__(self: Stroke,
                 offset: int = (0, 0),
                 **kwargs) -> None: ...

    def draw_path(self: Stroke,
                  renderer: {draw_path},
                  gc: Any,
                  tpath: Any,
                  affine: {__add__},
                  rgbFace: Any) -> None: ...


withStroke: Type[withEffect]


class SimplePatchShadow(AbstractPathEffect):
    _rho: float
    _alpha: float
    _gc: dict[str, Any]
    _shadow_rgbFace: Union[Iterable, tuple]

    def __init__(self: SimplePatchShadow,
                 offset: Any = (2, -2),
                 shadow_rgbFace: Any = None,
                 alpha: float = None,
                 rho: float = 0.3,
                 **kwargs) -> None: ...

    def draw_path(self: SimplePatchShadow,
                  renderer: {draw_path},
                  gc: Any,
                  tpath: Any,
                  affine: {__add__},
                  rgbFace: Any) -> None: ...


withSimplePatchShadow: Type[withEffect]


class SimpleLineShadow(AbstractPathEffect):
    _shadow_color: Union[Iterable, tuple]
    _rho: float
    _alpha: float
    _gc: dict[str, Any]

    def __init__(self: SimpleLineShadow,
                 offset: Any = (2, -2),
                 shadow_color: Any = 'k',
                 alpha: float = 0.3,
                 rho: float = 0.3,
                 **kwargs) -> None: ...

    def draw_path(self: SimpleLineShadow,
                  renderer: {draw_path},
                  gc: Any,
                  tpath: Any,
                  affine: {__add__},
                  rgbFace: Any) -> None: ...


class PathPatchEffect(AbstractPathEffect):
    patch: PathPatch

    def __init__(self: PathPatchEffect,
                 offset: int = (0, 0),
                 **kwargs) -> None: ...

    def draw_path(self: PathPatchEffect,
                  renderer: {draw_path},
                  gc: {get_clip_rectangle, get_clip_path},
                  tpath: Any,
                  affine: {__add__},
                  rgbFace: Any) -> None: ...


class TickedStroke(AbstractPathEffect):
    _angle: float
    _spacing: float
    _gc: dict[str, Any]
    _length: float

    def __init__(self: TickedStroke,
                 offset: int = (0, 0),
                 spacing: float = 10.0,
                 angle: float = 45.0,
                 length: float = np.sqrt(2),
                 **kwargs) -> None: ...

    def draw_path(self: TickedStroke,
                  renderer: {draw_path},
                  gc: Any,
                  tpath: Any,
                  affine: {__add__, transform_path, inverted},
                  rgbFace: Any) -> None: ...


withTickedStroke: Type[withEffect]
