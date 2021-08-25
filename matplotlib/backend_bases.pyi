from matplotlib._enums import CapStyle as CapStyle
from matplotlib._enums import JoinStyle as JoinStyle
from matplotlib.transforms import Affine2D as Affine2D
from matplotlib.path import Path as Path
from matplotlib.cbook import _setattr_cm as _setattr_cm
from matplotlib.backend_managers import ToolManager as ToolManager
from matplotlib._pylab_helpers import Gcf as Gcf
from matplotlib import rcParams as rcParams
from matplotlib import is_interactive as is_interactive
from matplotlib import get_backend as get_backend
from matplotlib import widgets as widgets
from matplotlib import transforms as transforms
from matplotlib import tight_bbox as tight_bbox
from matplotlib import textpath as textpath
from matplotlib import docstring as docstring
from matplotlib import colors as colors
from matplotlib import cbook as cbook
from matplotlib import backend_tools as tools
from matplotlib import _api as _api
from weakref import WeakKeyDictionary as WeakKeyDictionary
from enum import IntEnum as IntEnum
from enum import Enum as Enum
from contextlib import suppress as suppress
from contextlib import contextmanager as contextmanager
from collections import namedtuple as namedtuple
from enum import Enum
from enum import IntEnum
from functools import partial
from typing import Any
from typing import Callable
from typing import ClassVar
from typing import Generator
from typing import Iterable
from typing import Optional
from typing import Tuple
from typing import Type
from typing import Union

from Exception import Exception
from matplotlib import _api
from matplotlib.backend_bases import DrawEvent
from matplotlib.backend_bases import Event
from matplotlib.backend_bases import FigureCanvasBase
from matplotlib.backend_bases import FigureManagerBase
from matplotlib.backend_bases import GraphicsContextBase
from matplotlib.backend_bases import KeyEvent
from matplotlib.backend_bases import LocationEvent
from matplotlib.backend_bases import MouseEvent
from matplotlib.backend_bases import NavigationToolbar2
from matplotlib.backend_bases import PickEvent
from matplotlib.backend_bases import RendererBase
from matplotlib.backend_bases import ResizeEvent
from matplotlib.backend_bases import ShowBase
from matplotlib.backend_bases import StatusbarBase
from matplotlib.backend_bases import TimerBase
from matplotlib.backend_bases import ToolContainerBase
from matplotlib.backend_bases import _Backend
from matplotlib.backend_bases import _Mode
from matplotlib.backend_tools import Cursors
from matplotlib.figure import Figure
from matplotlib.font_manager import FontProperties
from matplotlib.path import Path
from matplotlib.texmanager import TexManager
from matplotlib.text import Text
from matplotlib.transforms import Affine2D
from matplotlib.transforms import Affine2DBase
from matplotlib.transforms import Transform
from numpy.core._multiarray_umath import ndarray
from object import object
from str import str

_log: Logger
_default_filetypes: dict[Union[str, Any], Union[str, Any]]
_default_backends: dict[Union[str, Any], Union[str, Any]]
from typing import Any


def _safe_pyplot_import() -> pyplot.py: ...


def register_backend(format: str,
                     backend: Any,
                     description: str = None) -> None: ...


def get_registered_canvas_class(format: Union[str, Any]) -> Union[Optional[str], Any]: ...


class RendererBase(object):
    _text2path: TextToPath
    _rasterizing: bool
    _raster_depth: int
    _texmanager: None

    def __init__(self: RendererBase) -> None: ...

    def open_group(self: RendererBase,
                   s: Any,
                   gid: Any = None) -> None: ...

    def close_group(self: RendererBase,
                    s: Any) -> None: ...

    def draw_path(self: RendererBase,
                  gc: Union[Union[GraphicsContextBase, {get_rgb, set_linewidth}], Any],
                  path: Union[Path, Any],
                  transform: Union[Affine2D, Any],
                  rgbFace: Any = None) -> Any: ...

    def draw_markers(self: RendererBase,
                     gc: Any,
                     marker_path: Any,
                     marker_trans: Transform,
                     path: {iter_segments},
                     trans: Transform,
                     rgbFace: Any = None) -> None: ...

    def draw_path_collection(self: RendererBase,
                             gc: Union[{get_linewidth}, Any],
                             master_transform: Any,
                             paths: {__len__, __getitem__},
                             all_transforms: {__len__},
                             offsets: {__len__},
                             offsetTrans: Any,
                             facecolors: {__len__},
                             edgecolors: {__len__},
                             linewidths: {__len__},
                             linestyles: {__len__},
                             antialiaseds: {__len__, __getitem__},
                             urls: {__len__},
                             offset_position: {__eq__}) -> None: ...

    def draw_quad_mesh(self: RendererBase,
                       gc: {get_linewidth, _alpha, _forced_alpha, _antialiased, _capstyle, _cliprect, _clippath,
                            _dashes, _joinstyle, _linestyle, _linewidth, _rgb, _hatch, _hatch_color, _hatch_linewidth,
                            _url, _gid, _snap, _sketch},
                       master_transform: Any,
                       meshWidth: {__mul__},
                       meshHeight: Any,
                       coordinates: Any,
                       offsets: {__len__},
                       offsetTrans: Any,
                       facecolors: {__len__},
                       antialiased: Any,
                       edgecolors: Optional[{__len__}]) -> None: ...

    def draw_gouraud_triangle(self: RendererBase,
                              gc: Any,
                              points: int,
                              colors: int,
                              transform: Transform) -> Any: ...

    def draw_gouraud_triangles(self: RendererBase,
                               gc: Any,
                               triangles_array: Any,
                               colors_array: Any,
                               transform: Transform) -> None: ...

    def _iter_collection_raw_paths(self: RendererBase,
                                   master_transform: Any,
                                   paths: Union[list[Path], Any],
                                   all_transforms: {__len__}) -> Generator[Tuple[Path, Union[Union[{input_dims,
                                                                                                    output_dims}, {
                                                                                                       output_dims,
                                                                                                       input_dims}, CompositeAffine2D, CompositeGenericTransform, _NotImplementedType], Any]], Any, None]: ...

    def _iter_collection_uses_per_path(self: RendererBase,
                                       paths: {__len__},
                                       all_transforms: {__len__},
                                       offsets: {__len__},
                                       facecolors: {__len__},
                                       edgecolors: {__len__}) -> int: ...

    def _iter_collection(self: RendererBase,
                         gc: {_alpha, _forced_alpha, _antialiased, _capstyle, _cliprect, _clippath, _dashes, _joinstyle,
                              _linestyle, _linewidth, _rgb, _hatch, _hatch_color, _hatch_linewidth, _url, _gid, _snap,
                              _sketch},
                         master_transform: Any,
                         all_transforms: {__len__},
                         path_ids: {__len__, __getitem__},
                         offsets: {__len__},
                         offsetTrans: Any,
                         facecolors: {__len__},
                         edgecolors: {__len__},
                         linewidths: {__len__},
                         linestyles: {__len__},
                         antialiaseds: {__len__, __getitem__},
                         urls: {__len__},
                         offset_position: {__eq__}) -> Generator[
        Tuple[Union[int, Any], Union[int, Any], Any, GraphicsContextBase, Optional[Any]], Any, None]: ...

    def get_image_magnification(self: RendererBase) -> float: ...

    def draw_image(self: RendererBase,
                   gc: Any,
                   x: Union[int, float, complex],
                   y: Union[int, float, complex],
                   im: int,
                   transform: Affine2DBase = None) -> Any: ...

    def option_image_nocomposite(self: RendererBase) -> bool: ...

    def option_scale_image(self: RendererBase) -> bool: ...

    @_api.delete_parameter("3.3", "ismath")
    def draw_tex(self: RendererBase,
                 gc: {get_rgb, set_linewidth},
                 x: Any,
                 y: Any,
                 s: Any,
                 prop: Any,
                 angle: Any,
                 ismath: str = 'TeX!',
                 mtext: Any = None) -> Optional[Any]: ...

    def draw_text(self: RendererBase,
                  gc: Any,
                  x: float,
                  y: float,
                  s: str,
                  prop: FontProperties,
                  angle: float,
                  ismath: bool = False,
                  mtext: Text = None) -> None: ...

    def _get_text_path_transform(self: RendererBase,
                                 x: Union[float, Any],
                                 y: Any,
                                 s: str,
                                 prop: FontProperties,
                                 angle: Any,
                                 ismath: Any) -> Tuple[Path, Affine2D]: ...

    def _draw_text_as_path(self: RendererBase,
                           gc: {get_rgb, set_linewidth},
                           x: Union[float, Any],
                           y: Any,
                           s: str,
                           prop: FontProperties,
                           angle: Any,
                           ismath: Any) -> None: ...

    def get_text_width_height_descent(self: RendererBase,
                                      s: Any,
                                      prop: {get_size_in_points},
                                      ismath: {__eq__}) -> Union[
        Union[Tuple[Any, Any, Any], Tuple[Any, Any, None]], Any]: ...

    def flipy(self: RendererBase) -> bool: ...

    def get_canvas_width_height(self: RendererBase) -> Tuple[int, int]: ...

    def get_texmanager(self: RendererBase) -> Union[TexManager, Any]: ...

    def new_gc(self: RendererBase) -> GraphicsContextBase: ...

    def points_to_pixels(self: RendererBase,
                         points: Union[float, ndarray, Iterable, int]) -> Union[float, ndarray, Iterable, int]: ...

    def start_rasterizing(self: RendererBase) -> None: ...

    def stop_rasterizing(self: RendererBase) -> None: ...

    def start_filter(self: RendererBase) -> None: ...

    def stop_filter(self: RendererBase,
                    filter_func: Any) -> None: ...

    def _draw_disabled(self: RendererBase) -> Union[Generator[Any, Any, None], Any]: ...


class GraphicsContextBase(object):
    _capstyle: Any
    _rgb: tuple[float, float, float, float]
    _hatch: None
    _sketch: None
    _hatch_color: Union[Iterable, tuple]
    _joinstyle: Any
    _gid: None
    _clippath: None
    _antialiased: int
    _linestyle: str
    _linewidth: int
    _cliprect: None
    _alpha: float
    _snap: None
    _hatch_linewidth: Optional[Any]
    _url: None
    _dashes: tuple[int, None]
    _forced_alpha: bool

    def __init__(self: GraphicsContextBase) -> None: ...

    def copy_properties(self: GraphicsContextBase,
                        gc: Union[{get_linewidth}, Any]) -> None: ...

    def restore(self: GraphicsContextBase) -> None: ...

    def get_alpha(self: GraphicsContextBase) -> float: ...

    def get_antialiased(self: GraphicsContextBase) -> int: ...

    def get_capstyle(self: GraphicsContextBase) -> Any: ...

    def get_clip_rectangle(self: GraphicsContextBase) -> Any: ...

    def get_clip_path(self: GraphicsContextBase) -> Union[Tuple[Any, Any], Tuple[None, None]]: ...

    def get_dashes(self: GraphicsContextBase) -> Tuple[int, None]: ...

    def get_forced_alpha(self: GraphicsContextBase) -> bool: ...

    def get_joinstyle(self: GraphicsContextBase) -> Any: ...

    def get_linewidth(self: GraphicsContextBase) -> int: ...

    def get_rgb(self: GraphicsContextBase) -> Tuple[float, float, float, float]: ...

    def get_url(self: GraphicsContextBase) -> Any: ...

    def get_gid(self: GraphicsContextBase) -> Any: ...

    def get_snap(self: GraphicsContextBase) -> Any: ...

    def set_alpha(self: GraphicsContextBase,
                  alpha: Any) -> None: ...

    def set_antialiased(self: GraphicsContextBase,
                        b: Any) -> None: ...

    def set_capstyle(self: GraphicsContextBase,
                     cs: Any) -> Optional[Any]: ...

    def set_clip_rectangle(self: GraphicsContextBase,
                           rectangle: Any) -> None: ...

    def set_clip_path(self: GraphicsContextBase,
                      path: Any) -> None: ...

    def set_dashes(self: GraphicsContextBase,
                   dash_offset: Optional[float],
                   dash_list: Union[ndarray, Iterable, int, float, None]) -> Any: ...

    def set_foreground(self: GraphicsContextBase,
                       fg: Any,
                       isRGBA: bool = False) -> None: ...

    def set_joinstyle(self: GraphicsContextBase,
                      js: Any) -> Optional[Any]: ...

    def set_linewidth(self: GraphicsContextBase,
                      w: Union[Union[float, None, int], Any]) -> None: ...

    def set_url(self: GraphicsContextBase,
                url: Optional[Any]) -> None: ...

    def set_gid(self: GraphicsContextBase,
                id: Any) -> None: ...

    def set_snap(self: GraphicsContextBase,
                 snap: Any) -> None: ...

    def set_hatch(self: GraphicsContextBase,
                  hatch: Any) -> None: ...

    def get_hatch(self: GraphicsContextBase) -> Any: ...

    def get_hatch_path(self: GraphicsContextBase,
                       density: float = 6.0) -> Optional[Path]: ...

    def get_hatch_color(self: GraphicsContextBase) -> Union[Iterable, Tuple]: ...

    def set_hatch_color(self: GraphicsContextBase,
                        hatch_color: Any) -> None: ...

    def get_hatch_linewidth(self: GraphicsContextBase) -> Optional[Any]: ...

    def get_sketch_params(self: GraphicsContextBase) -> Optional[Tuple]: ...

    def set_sketch_params(self: GraphicsContextBase,
                          scale: Optional[float] = None,
                          length: float = None,
                          randomness: float = None) -> None: ...


class TimerBase(object):
    _interval: int
    single_shot: bool
    callbacks: Union[list[Any], Any]
    interval: int
    _single: Any

    def __init__(self: TimerBase,
                 interval: int = None,
                 callbacks: Union[Iterable, tuple] = None) -> None: ...

    def __del__(self: TimerBase) -> None: ...

    def start(self: TimerBase,
              interval: Optional[int] = None) -> None: ...

    def stop(self: TimerBase) -> None: ...

    def _timer_start(self: TimerBase) -> None: ...

    def _timer_stop(self: TimerBase) -> None: ...

    def interval(self: TimerBase) -> int: ...

    def interval(self: TimerBase,
                 interval: Any) -> None: ...

    def single_shot(self: TimerBase) -> Any: ...

    def single_shot(self: TimerBase,
                    ss: Any) -> None: ...

    def add_callback(self: TimerBase,
                     func: Any,
                     *args,
                     **kwargs) -> Any: ...

    def remove_callback(self: TimerBase,
                        func: Any,
                        *args,
                        **kwargs) -> None: ...

    def _timer_set_interval(self: TimerBase) -> None: ...

    def _timer_set_single_shot(self: TimerBase) -> None: ...

    def _on_timer(self: TimerBase) -> None: ...


class Event(object):
    canvas: Union[{get_width_height}, Any]
    name: Any
    guiEvent: Any

    def __init__(self: Event,
                 name: Any,
                 canvas: Union[{get_width_height}, Any],
                 guiEvent: Any = None) -> None: ...


class DrawEvent(Event):
    renderer: Any

    def __init__(self: DrawEvent,
                 name: Any,
                 canvas: Union[{get_width_height}, Any],
                 renderer: Any) -> None: ...


class ResizeEvent(Event):
    width: Any
    height: Any

    def __init__(self: ResizeEvent,
                 name: Any,
                 canvas: {get_width_height}) -> None: ...


class CloseEvent(Event):
    pass


class LocationEvent(Event):
    lastevent: ClassVar[None]
    inaxes: Any
    x: Union[int, Any]
    y: Union[int, Any]
    xdata: Any
    ydata: Any

    def __init__(self: LocationEvent,
                 name: Any,
                 canvas: Any,
                 x: Any,
                 y: Any,
                 guiEvent: Any = None) -> None: ...

    def _update_enter_leave(self: LocationEvent) -> None: ...


class MouseButton(IntEnum):
    LEFT: ClassVar[MouseButton]
    MIDDLE: ClassVar[MouseButton]
    RIGHT: ClassVar[MouseButton]
    BACK: ClassVar[MouseButton]
    FORWARD: ClassVar[MouseButton]
    pass


class MouseEvent(LocationEvent):
    button: Any
    dblclick: bool
    step: int
    key: Any

    def __init__(self: MouseEvent,
                 name: Any,
                 canvas: Any,
                 x: Any,
                 y: Any,
                 button: Any = None,
                 key: Any = None,
                 step: int = 0,
                 dblclick: bool = False,
                 guiEvent: Any = None) -> None: ...

    def __str__(self: MouseEvent) -> str: ...


class PickEvent(Event):
    mouseevent: Any
    artist: Any

    def __init__(self: PickEvent,
                 name: Any,
                 canvas: Any,
                 mouseevent: Any,
                 artist: Any,
                 guiEvent: Any = None,
                 **kwargs) -> None: ...


class KeyEvent(LocationEvent):
    key: Any

    def __init__(self: KeyEvent,
                 name: Any,
                 canvas: Any,
                 key: Any,
                 x: int = 0,
                 y: int = 0,
                 guiEvent: Any = None) -> None: ...


def _get_renderer(figure: Union[Union[{draw}, Figure], Any],
                  print_method: Union[partial[Any], Any] = None) -> Any: ...


def _no_output_draw(figure: {draw}) -> None: ...


def _is_non_interactive_terminal_ipython(ip: {parent}) -> Union[bool, Any]: ...


def _check_savefig_extra_args(func: Any = None,
                              extra_kwargs: Union[tuple, Any] = ()) -> Union[
    partial[Any], Callable[[Tuple[Any, ...], dict[str, Any]], Any]]: ...


class FigureCanvasBase(object):
    required_interactive_framework: ClassVar[None]
    events: ClassVar[list[Union[str, Any]]]
    fixed_dpi: ClassVar[None]
    filetypes: ClassVar[dict[Union[str, Any], Union[str, Any]]]
    callbacks: ClassVar[property]
    button_pick_id: ClassVar[property]
    scroll_pick_id: ClassVar[property]
    _timer_cls: ClassVar[Type[TimerBase]]
    toolbar: None
    figure: Union[Figure, Any]
    _button: None
    manager: None
    widgetlock: LockDraw
    _looping: bool
    _is_saving: bool
    _lasty: None
    mouse_grabber: None
    _key: None
    _is_idle_drawing: bool
    _lastx: None

    @_api.classproperty
    def supports_blit(cls: FigureCanvasBase) -> Union[bool, Any]: ...

    def __init__(self: FigureCanvasBase,
                 figure: Optional[{set_canvas}] = None) -> None: ...

    def _fix_ipython_backend2gui(cls: Type[FigureCanvasBase]) -> None: ...

    def _idle_draw_cntx(self: FigureCanvasBase) -> Union[Generator[Any, Any, None], Any]: ...

    def is_saving(self: FigureCanvasBase) -> bool: ...

    def pick(self: FigureCanvasBase,
             mouseevent: Any) -> None: ...

    def blit(self: FigureCanvasBase,
             bbox: Any = None) -> None: ...

    def resize(self: FigureCanvasBase,
               w: Any,
               h: Any) -> None: ...

    def draw_event(self: FigureCanvasBase,
                   renderer: Any) -> None: ...

    def resize_event(self: FigureCanvasBase) -> None: ...

    def close_event(self: FigureCanvasBase,
                    guiEvent: Any = None) -> None: ...

    def key_press_event(self: FigureCanvasBase,
                        key: Any,
                        guiEvent: Any = None) -> None: ...

    def key_release_event(self: FigureCanvasBase,
                          key: Any,
                          guiEvent: Any = None) -> None: ...

    def pick_event(self: FigureCanvasBase,
                   mouseevent: {guiEvent},
                   artist: Any,
                   **kwargs) -> None: ...

    def scroll_event(self: FigureCanvasBase,
                     x: Any,
                     y: Any,
                     step: {__ge__},
                     guiEvent: Any = None) -> None: ...

    def button_press_event(self: FigureCanvasBase,
                           x: Any,
                           y: Any,
                           button: Any,
                           dblclick: bool = False,
                           guiEvent: Any = None) -> None: ...

    def button_release_event(self: FigureCanvasBase,
                             x: float,
                             y: float,
                             button: Any,
                             guiEvent: Any = None) -> None: ...

    def motion_notify_event(self: FigureCanvasBase,
                            x: float,
                            y: float,
                            guiEvent: Any = None) -> None: ...

    def leave_notify_event(self: FigureCanvasBase,
                           guiEvent: Any = None) -> None: ...

    def enter_notify_event(self: FigureCanvasBase,
                           guiEvent: Any = None,
                           xy: tuple[float, float] = None) -> None: ...

    def inaxes(self: FigureCanvasBase,
               xy: tuple[float, float]) -> Any: ...

    def grab_mouse(self: FigureCanvasBase,
                   ax: Any) -> Any: ...

    def release_mouse(self: FigureCanvasBase,
                      ax: Any) -> None: ...

    def draw(self: FigureCanvasBase,
             *args,
             **kwargs) -> None: ...

    def draw_idle(self: FigureCanvasBase,
                  *args,
                  **kwargs) -> None: ...

    def get_width_height(self: FigureCanvasBase) -> Tuple[int, int]: ...

    def get_supported_filetypes(cls: Type[FigureCanvasBase]) -> dict[Union[str, Any], Union[str, Any]]: ...

    def get_supported_filetypes_grouped(cls: Type[FigureCanvasBase]) -> dict[Any, Any]: ...

    def _get_output_canvas(self: FigureCanvasBase,
                           backend: Optional[str],
                           fmt: str) -> Union[FigureCanvasBase, Any]: ...

    def print_figure(self: FigureCanvasBase,
                     filename: Any,
                     dpi: float = None,
                     facecolor: Any = None,
                     edgecolor: Any = None,
                     orientation: str = 'portrait',
                     format: Optional[str] = None,
                     *,
                     bbox_inches: Any = None,
                     pad_inches: float = None,
                     bbox_extra_artists: Any = None,
                     backend: Optional[str] = None,
                     **kwargs) -> Any: ...

    def get_default_filetype(cls: Type[FigureCanvasBase]) -> Optional[Any]: ...

    @_api.deprecated(
        "3.4", alternative="manager.get_window_title or GUI-specific methods")
    def get_window_title(self: FigureCanvasBase) -> Any: ...

    @_api.deprecated(
        "3.4", alternative="manager.set_window_title or GUI-specific methods")
    def set_window_title(self: FigureCanvasBase,
                         title: Any) -> Optional[Any]: ...

    def get_default_filename(self: FigureCanvasBase) -> Union[str, Any]: ...

    def switch_backends(self: FigureCanvasBase,
                        FigureCanvasClass: Union[str, Any]) -> Any: ...

    def mpl_connect(self: FigureCanvasBase,
                    s: str,
                    func: Callable) -> Any: ...

    def mpl_disconnect(self: FigureCanvasBase,
                       cid: Any) -> Any: ...

    def new_timer(self: FigureCanvasBase,
                  interval: int = None,
                  callbacks: Union[Iterable, tuple] = None) -> TimerBase: ...

    def flush_events(self: FigureCanvasBase) -> None: ...

    def start_event_loop(self: FigureCanvasBase,
                         timeout: int = 0) -> None: ...

    def stop_event_loop(self: FigureCanvasBase) -> None: ...


def key_press_handler(event: KeyEvent,
                      canvas: FigureCanvasBase = None,
                      toolbar: NavigationToolbar2 = None) -> None: ...


def button_press_handler(event: Any,
                         canvas: Any = None,
                         toolbar: Any = None) -> None: ...


class NonGuiException(Exception):
    pass


class FigureManagerBase(object):
    statusbar: ClassVar[Union[_deprecated_property, Any]]
    toolbar: None
    key_press_handler_id: Any
    canvas: {manager, figure}
    button_press_handler_id: Any
    num: Any
    toolmanager: Optional[ToolManager]

    def __init__(self: FigureManagerBase,
                 canvas: {manager, figure},
                 num: Any) -> None: ...

    def show(self: FigureManagerBase) -> None: ...

    def destroy(self: FigureManagerBase) -> None: ...

    def full_screen_toggle(self: FigureManagerBase) -> None: ...

    def resize(self: FigureManagerBase,
               w: Any,
               h: Any) -> None: ...

    @_api.deprecated(
        "3.4", alternative="self.canvas.callbacks.process(event.name, event)")
    def key_press(self: FigureManagerBase,
                  event: Any) -> Optional[Any]: ...

    @_api.deprecated(
        "3.4", alternative="self.canvas.callbacks.process(event.name, event)")
    def button_press(self: FigureManagerBase,
                     event: Any) -> Optional[Any]: ...

    def get_window_title(self: FigureManagerBase) -> str: ...

    def set_window_title(self: FigureManagerBase,
                         title: Union[str, Any]) -> None: ...


cursors: Type[Cursors]


class _Mode(str, Enum):
    NONE: ClassVar[_Mode]
    PAN: ClassVar[_Mode]
    ZOOM: ClassVar[_Mode]

    def __str__(self: _Mode) -> str: ...

    def _navigate_mode(self: _Mode) -> Optional[Any]: ...


class NavigationToolbar2(object):
    toolitems: ClassVar[tuple[
        tuple[str, str, str, str], tuple[str, str, str, str], tuple[str, str, str, str], tuple[None, None, None, None],
        tuple[str, str, str, str], tuple[str, str, str, str], tuple[str, str, str, str], tuple[None, None, None, None],
        tuple[str, str, str, str]]]
    _PanInfo: ClassVar[Type[_PanInfo]]
    _ZoomInfo: ClassVar[Type[_ZoomInfo]]
    mode: _Mode
    subplot_tool: SubplotTool
    canvas: {toolbar}
    _id_press: Any
    _id_drag: Any
    _lastCursor: Cursors
    _pan_info: None
    _draw_time: float
    _id_release: Any
    _zoom_info: None
    _nav_stack: Stack

    def __init__(self: NavigationToolbar2,
                 canvas: {toolbar}) -> None: ...

    def set_message(self: NavigationToolbar2,
                    s: Union[_Mode, Any]) -> None: ...

    def draw_rubberband(self: NavigationToolbar2,
                        event: Union[{x, y, key}, Any],
                        x0: Any,
                        y0: Any,
                        x1: Any,
                        y1: Any) -> None: ...

    def remove_rubberband(self: NavigationToolbar2) -> None: ...

    def home(self: NavigationToolbar2,
             *args) -> None: ...

    def back(self: NavigationToolbar2,
             *args) -> None: ...

    def forward(self: NavigationToolbar2,
                *args) -> None: ...

    @_api.deprecated("3.3", alternative="__init__")
    def _init_toolbar(self: NavigationToolbar2) -> Any: ...

    def _update_cursor(self: NavigationToolbar2,
                       event: Union[Union[KeyEvent, {inaxes}], Any]) -> None: ...

    def _wait_cursor_for_draw_cm(self: NavigationToolbar2) -> Union[Generator[Any, Any, None], Any]: ...

    def _mouse_event_to_message(event: {inaxes}) -> Any: ...

    def mouse_move(self: NavigationToolbar2,
                   event: Any) -> None: ...

    def _zoom_pan_handler(self: NavigationToolbar2,
                          event: Any) -> None: ...

    @_api.deprecated("3.3")
    def press(self: NavigationToolbar2,
              event: Any) -> Optional[Any]: ...

    @_api.deprecated("3.3")
    def release(self: NavigationToolbar2,
                event: Any) -> Optional[Any]: ...

    def pan(self: NavigationToolbar2,
            *args) -> None: ...

    def press_pan(self: NavigationToolbar2,
                  event: {button, x, y}) -> None: ...

    def drag_pan(self: NavigationToolbar2,
                 event: {key, x, y}) -> None: ...

    def release_pan(self: NavigationToolbar2,
                    event: Any) -> None: ...

    def zoom(self: NavigationToolbar2,
             *args) -> None: ...

    def press_zoom(self: NavigationToolbar2,
                   event: {button, x, y}) -> None: ...

    def drag_zoom(self: NavigationToolbar2,
                  event: {x, y, key}) -> None: ...

    def release_zoom(self: NavigationToolbar2,
                     event: {x, key, y}) -> None: ...

    def push_current(self: NavigationToolbar2) -> None: ...

    @_api.deprecated("3.3", alternative="toolbar.canvas.draw_idle()")
    def draw(self: NavigationToolbar2) -> Optional[Any]: ...

    def _draw(self: NavigationToolbar2) -> None: ...

    def _update_view(self: NavigationToolbar2) -> None: ...

    def configure_subplots(self: NavigationToolbar2,
                           *args) -> None: ...

    def save_figure(self: NavigationToolbar2,
                    *args) -> Any: ...

    def set_cursor(self: NavigationToolbar2,
                   cursor: Union[Cursors, Any]) -> None: ...

    def update(self: NavigationToolbar2) -> None: ...

    def set_history_buttons(self: NavigationToolbar2) -> None: ...


class ToolContainerBase(object):
    _icon_extension: ClassVar[str]
    toolmanager: {toolmanager_connect}

    def __init__(self: ToolContainerBase,
                 toolmanager: {toolmanager_connect}) -> None: ...

    def _tool_toggled_cbk(self: ToolContainerBase,
                          event: {tool}) -> None: ...

    def add_tool(self: ToolContainerBase,
                 tool: Any,
                 group: str,
                 position: int = -1) -> None: ...

    def _get_image_filename(self: ToolContainerBase,
                            image: {__add__}) -> Union[Union[None, {__add__}, str], Any]: ...

    def trigger_tool(self: ToolContainerBase,
                     name: str) -> None: ...

    def add_toolitem(self: ToolContainerBase,
                     name: str,
                     group: str,
                     position: int,
                     image: str,
                     description: str,
                     toggle: bool) -> Any: ...

    def toggle_toolitem(self: ToolContainerBase,
                        name: str,
                        toggled: bool) -> Any: ...

    def remove_toolitem(self: ToolContainerBase,
                        name: str) -> Any: ...

    def set_message(self: ToolContainerBase,
                    s: str) -> Any: ...


@_api.deprecated("3.3")
class StatusbarBase(object):
    toolmanager: Any

    def __init__(self: StatusbarBase,
                 toolmanager: Any) -> None: ...

    def _message_cbk(self: StatusbarBase,
                     event: {message}) -> None: ...

    def set_message(self: StatusbarBase,
                    s: str) -> None: ...


class _Backend(object):
    backend_version: ClassVar[str]
    FigureCanvas: ClassVar[None]
    FigureManager: ClassVar[Type[FigureManagerBase]]
    mainloop: ClassVar[None]

    def new_figure_manager(cls: Type[_Backend],
                           num: Any,
                           *args,
                           **kwargs) -> FigureManagerBase: ...

    def new_figure_manager_given_figure(cls: Type[_Backend],
                                        num: Any,
                                        figure: Any) -> FigureManagerBase: ...

    def draw_if_interactive(cls: Type[_Backend]) -> None: ...

    def show(cls: Type[_Backend],
             *,
             block: Any = None) -> None: ...

    def export(cls: {__module__}) -> {__module__}: ...


class ShowBase(_Backend):
    def __call__(self: ShowBase,
                 block: Any = None) -> None: ...
