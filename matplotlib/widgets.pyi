from typing import Any
from typing import Callable
from typing import Iterable
from typing import Optional
from typing import Tuple
from typing import Union

from matplotlib import _api
from matplotlib.axes._axes import Axes
from matplotlib.widgets import AxesWidget
from matplotlib.widgets import Button
from matplotlib.widgets import CheckButtons
from matplotlib.widgets import Cursor
from matplotlib.widgets import EllipseSelector
from matplotlib.widgets import Lasso
from matplotlib.widgets import LassoSelector
from matplotlib.widgets import LockDraw
from matplotlib.widgets import MultiCursor
from matplotlib.widgets import PolygonSelector
from matplotlib.widgets import RadioButtons
from matplotlib.widgets import RangeSlider
from matplotlib.widgets import RectangleSelector
from matplotlib.widgets import Slider
from matplotlib.widgets import SliderBase
from matplotlib.widgets import SpanSelector
from matplotlib.widgets import SubplotTool
from matplotlib.widgets import TextBox
from matplotlib.widgets import ToolHandles
from matplotlib.widgets import Widget
from matplotlib.widgets import _SelectorWidget
from numpy.core._multiarray_umath import ndarray
from object import object


class LockDraw(object):
    def __init__(self: LockDraw) -> None: ...

    def __call__(self: LockDraw,
                 o: Any) -> Any: ...

    def release(self: LockDraw,
                o: Any) -> Any: ...

    def available(self: LockDraw,
                  o: Any) -> Union[bool, Any]: ...

    def isowner(self: LockDraw,
                o: Any) -> Any: ...

    def locked(self: LockDraw) -> Any: ...


class Widget(object):
    def set_active(self: Widget,
                   active: Any) -> None: ...

    def get_active(self: Widget) -> Any: ...

    def ignore(self: Widget,
               event: Union[Union[{inaxes, canvas}, {canvas, inaxes}, {inaxes}, {button, name, inaxes}, {button, name,
                                                                                                         inaxes}, {
                                      button, inaxes, x, y}, {canvas}, {inaxes, canvas, x}, {inaxes}, {button, inaxes,
                                                                                                       x, y}, {inaxes,
                                                                                                               xdata,
                                                                                                               ydata}, {
                                      inaxes}, {inaxes, button, xdata, ydata}], Any]) -> bool: ...


class AxesWidget(Widget):
    def __init__(self: AxesWidget,
                 ax: Union[Union[{name, set_xticks, set_yticks, set_navigate}, Axes], Any]) -> None: ...

    def connect_event(self: AxesWidget,
                      event: Union[str, Any],
                      callback: Union[Union[Callable[[{canvas, inaxes}], None], Callable[[{inaxes}], None], Callable[
                          [{button, inaxes, x, y}], None], Callable[[{inaxes, canvas, x}], None], Callable[
                                                [{canvas}], None], Callable[[{inaxes}], None], Callable[[Any], None],
                                            Callable[[Any], None], Callable[[{button, inaxes, x, y}], None], Callable[
                                                [{inaxes, xdata, ydata}], None], Callable[[Any], None], Callable[
                                                [Any], bool], Callable[[Any], bool], Callable[[Any], bool], Callable[
                                                [Optional[Any]], None], Callable[[Any], None], Callable[[Any], None],
                                            Callable[[Any], None], Callable[[Any], None], Callable[
                                                [{inaxes, button, xdata, ydata}], None]], Any]) -> None: ...

    def disconnect_events(self: AxesWidget) -> None: ...


class Button(AxesWidget):
    def __init__(self: Button,
                 ax: Any,
                 label: str,
                 image: Any = None,
                 color: Any = '0.85',
                 hovercolor: Any = '0.95') -> None: ...

    def _click(self: Button,
               event: {inaxes, canvas}) -> None: ...

    def _release(self: Button,
                 event: {canvas, inaxes}) -> None: ...

    def _motion(self: Button,
                event: {inaxes}) -> None: ...

    def on_clicked(self: Button,
                   func: Union[Callable[[Any], None], Any]) -> Union[int, Any]: ...

    def disconnect(self: Button,
                   cid: Any) -> None: ...


class SliderBase(AxesWidget):
    def __init__(self: SliderBase,
                 ax: Union[Axes, Any],
                 orientation: Union[str, Any],
                 closedmin: Union[bool, Any],
                 closedmax: Any,
                 valmin: Any,
                 valmax: Any,
                 valfmt: Any,
                 dragging: Any,
                 valstep: Any) -> Any: ...

    def _stepped_value(self: SliderBase,
                       val: Union[Optional[float], Any]) -> Union[Union[float, int, None], Any]: ...

    def disconnect(self: SliderBase,
                   cid: int) -> None: ...

    def reset(self: SliderBase) -> None: ...


class Slider(SliderBase):
    def __init__(self: Slider,
                 ax: Any,
                 label: str,
                 valmin: float,
                 valmax: float,
                 valinit: float = 0.5,
                 valfmt: str = None,
                 closedmin: bool = True,
                 closedmax: bool = True,
                 slidermin: Slider = None,
                 slidermax: Slider = None,
                 dragging: bool = True,
                 valstep: Union[float, ndarray, Iterable, int] = None,
                 orientation: str = 'horizontal',
                 *,
                 initcolor: Any = 'r',
                 **kwargs) -> Any: ...

    def _value_in_bounds(self: Slider,
                         val: Union[float, Any]) -> Union[Union[None, float, int], Any]: ...

    def _update(self: Slider,
                event: {button, name, inaxes}) -> None: ...

    def _format(self: Slider,
                val: Union[Union[float, int], Any]) -> Union[str, Any]: ...

    def set_val(self: Slider,
                val: float) -> None: ...

    def on_changed(self: Slider,
                   func: Callable) -> int: ...


class RangeSlider(SliderBase):
    def __init__(self: RangeSlider,
                 ax: Any,
                 label: str,
                 valmin: float,
                 valmax: float,
                 valinit: Union[Iterable, tuple[float], None] = None,
                 valfmt: str = None,
                 closedmin: bool = True,
                 closedmax: bool = True,
                 dragging: bool = True,
                 valstep: float = None,
                 orientation: str = "horizontal",
                 **kwargs) -> None: ...

    def _min_in_bounds(self: RangeSlider,
                       min: Optional[Any]) -> Union[Optional[int], Any]: ...

    def _max_in_bounds(self: RangeSlider,
                       max: Optional[Any]) -> Union[Union[None, float, int], Any]: ...

    def _value_in_bounds(self: RangeSlider,
                         vals: {__getitem__}) -> Tuple[
        Union[Union[None, float, int], Any], Union[Union[None, float, int], Any]]: ...

    def _update_val_from_pos(self: RangeSlider,
                             pos: Any) -> None: ...

    def _update(self: RangeSlider,
                event: {button, name, inaxes}) -> None: ...

    def _format(self: RangeSlider,
                val: Union[Union[ndarray, tuple[
                    Union[Union[None, float, int], Any], Union[Union[None, float, int], Any]]], Any]) -> str: ...

    def set_min(self: RangeSlider,
                min: float) -> None: ...

    def set_max(self: RangeSlider,
                max: float) -> None: ...

    def set_val(self: RangeSlider,
                val: Union[Iterable, tuple, ndarray, int, float[float]]) -> Any: ...

    def on_changed(self: RangeSlider,
                   func: Callable) -> int: ...


class CheckButtons(AxesWidget):
    def __init__(self: CheckButtons,
                 ax: Any,
                 labels: Iterable[str],
                 actives: Optional[Iterable[bool]] = None) -> None: ...

    def _clicked(self: CheckButtons,
                 event: {button, inaxes, x, y}) -> None: ...

    def set_active(self: CheckButtons,
                   index: int) -> Any: ...

    def get_status(self: CheckButtons) -> list[Any]: ...

    def on_clicked(self: CheckButtons,
                   func: Any) -> Union[int, Any]: ...

    def disconnect(self: CheckButtons,
                   cid: Any) -> None: ...


class TextBox(AxesWidget):
    def __init__(self: TextBox,
                 ax: Any,
                 label: str,
                 initial: str = '',
                 color: Any = '.95',
                 hovercolor: Any = '1',
                 label_pad: float = .01) -> None: ...

    def text(self: TextBox) -> Any: ...

    def _rendercursor(self: TextBox) -> None: ...

    def _release(self: TextBox,
                 event: {canvas}) -> None: ...

    def _keypress(self: TextBox,
                  event: Any) -> None: ...

    def set_val(self: TextBox,
                val: Any) -> None: ...

    def begin_typing(self: TextBox,
                     x: Any) -> None: ...

    def stop_typing(self: TextBox) -> None: ...

    def position_cursor(self: TextBox,
                        x: Any) -> None: ...

    def _click(self: TextBox,
               event: {inaxes, canvas, x}) -> None: ...

    def _resize(self: TextBox,
                event: Any) -> None: ...

    def _motion(self: TextBox,
                event: {inaxes}) -> None: ...

    def on_text_change(self: TextBox,
                       func: Any) -> Union[int, Any]: ...

    def on_submit(self: TextBox,
                  func: Any) -> Union[int, Any]: ...

    def disconnect(self: TextBox,
                   cid: Any) -> None: ...


class RadioButtons(AxesWidget):
    def __init__(self: RadioButtons,
                 ax: Any,
                 labels: Iterable[str],
                 active: int = 0,
                 activecolor: Any = 'blue') -> None: ...

    def _clicked(self: RadioButtons,
                 event: {button, inaxes, x, y}) -> None: ...

    def set_active(self: RadioButtons,
                   index: Union[int, Any]) -> Any: ...

    def on_clicked(self: RadioButtons,
                   func: {__self__, __func__}) -> Union[int, Any]: ...

    def disconnect(self: RadioButtons,
                   cid: Any) -> None: ...


class SubplotTool(Widget):
    def __init__(self: SubplotTool,
                 targetfig: Any,
                 toolfig: Any) -> None: ...

    def _on_slider_changed(self: SubplotTool,
                           _: Any) -> None: ...

    def _on_reset(self: SubplotTool,
                  event: Any) -> None: ...

    @_api.deprecated("3.3")
    def funcleft(self: SubplotTool,
                 val: Any) -> Optional[Any]: ...

    @_api.deprecated("3.3")
    def funcright(self: SubplotTool,
                  val: Any) -> Optional[Any]: ...

    @_api.deprecated("3.3")
    def funcbottom(self: SubplotTool,
                   val: Any) -> Optional[Any]: ...

    @_api.deprecated("3.3")
    def functop(self: SubplotTool,
                val: Any) -> Optional[Any]: ...

    @_api.deprecated("3.3")
    def funcwspace(self: SubplotTool,
                   val: Any) -> Optional[Any]: ...

    @_api.deprecated("3.3")
    def funchspace(self: SubplotTool,
                   val: Any) -> Optional[Any]: ...


class Cursor(AxesWidget):
    def __init__(self: Cursor,
                 ax: Axes,
                 horizOn: bool = True,
                 vertOn: bool = True,
                 useblit: bool = False,
                 **kwargs) -> None: ...

    def clear(self: Cursor,
              event: Any) -> None: ...

    def onmove(self: Cursor,
               event: {inaxes, xdata, ydata}) -> None: ...

    def _update(self: Cursor) -> bool: ...


class MultiCursor(Widget):
    def __init__(self: MultiCursor,
                 canvas: Any,
                 axes: {__getitem__},
                 useblit: bool = True,
                 horizOn: bool = False,
                 vertOn: bool = True,
                 **kwargs) -> None: ...

    def connect(self: MultiCursor) -> None: ...

    def disconnect(self: MultiCursor) -> None: ...

    def clear(self: MultiCursor,
              event: Any) -> None: ...

    def onmove(self: MultiCursor,
               event: {inaxes}) -> None: ...

    def _update(self: MultiCursor) -> None: ...


class _SelectorWidget(AxesWidget):
    def __init__(self: _SelectorWidget,
                 ax: Union[Union[{name, set_xticks, set_yticks, set_navigate}, Axes], Any],
                 onselect: Union[function, Any],
                 useblit: bool = False,
                 button: Any = None,
                 state_modifier_keys: Union[dict[Any, str], Any] = None) -> None: ...

    def set_active(self: _SelectorWidget,
                   active: Any) -> None: ...

    def update_background(self: _SelectorWidget,
                          event: Optional[Any]) -> None: ...

    def connect_default_events(self: _SelectorWidget) -> None: ...

    def ignore(self: _SelectorWidget,
               event: Union[Union[{inaxes, canvas}, {canvas, inaxes}, {inaxes}, {button, name, inaxes}, {button, name,
                                                                                                         inaxes}, {
                                      button, inaxes, x, y}, {canvas}, {inaxes, canvas, x}, {inaxes}, {button, inaxes,
                                                                                                       x, y}, {inaxes,
                                                                                                               xdata,
                                                                                                               ydata}, {
                                      inaxes}, {inaxes, button, xdata, ydata}], Any]) -> Union[bool, Any]: ...

    def update(self: _SelectorWidget) -> bool: ...

    def _get_data(self: _SelectorWidget,
                  event: Union[{key}, Any]) -> Union[Tuple[None, None], Tuple[ndarray, ndarray]]: ...

    def _clean_event(self: _SelectorWidget,
                     event: Union[{key}, Any]) -> Union[{key}, Any]: ...

    def press(self: _SelectorWidget,
              event: Any) -> bool: ...

    def _press(self: _SelectorWidget,
               event: Any) -> None: ...

    def release(self: _SelectorWidget,
                event: Any) -> bool: ...

    def _release(self: _SelectorWidget,
                 event: Any) -> None: ...

    def onmove(self: _SelectorWidget,
               event: Any) -> bool: ...

    def _onmove(self: _SelectorWidget,
                event: Any) -> None: ...

    def on_scroll(self: _SelectorWidget,
                  event: Any) -> None: ...

    def _on_scroll(self: _SelectorWidget,
                   event: Any) -> None: ...

    def on_key_press(self: _SelectorWidget,
                     event: Any) -> None: ...

    def _on_key_press(self: _SelectorWidget,
                      event: Any) -> None: ...

    def on_key_release(self: _SelectorWidget,
                       event: Any) -> None: ...

    def _on_key_release(self: _SelectorWidget,
                        event: Any) -> None: ...

    def set_visible(self: _SelectorWidget,
                    visible: Union[bool, Any]) -> None: ...


class SpanSelector(_SelectorWidget):
    def __init__(self: SpanSelector,
                 ax: Axes,
                 onselect: Any,
                 direction: str,
                 minspan: float = None,
                 useblit: bool = False,
                 rectprops: dict = None,
                 onmove_callback: Any = None,
                 span_stays: bool = False,
                 button: Any = None) -> None: ...

    def new_axes(self: SpanSelector,
                 ax: Union[Axes, Any]) -> None: ...

    def ignore(self: SpanSelector,
               event: Union[Union[{inaxes, canvas}, {canvas, inaxes}, {inaxes}, {button, name, inaxes}, {button, name,
                                                                                                         inaxes}, {
                                      button, inaxes, x, y}, {canvas}, {inaxes, canvas, x}, {inaxes}, {button, inaxes,
                                                                                                       x, y}, {inaxes,
                                                                                                               xdata,
                                                                                                               ydata}, {
                                      inaxes}, {inaxes, button, xdata, ydata}], Any]) -> Union[bool, Any]: ...

    def _press(self: SpanSelector,
               event: {xdata, ydata}) -> bool: ...

    def _release(self: SpanSelector,
                 event: {xdata, ydata}) -> Optional[bool]: ...

    def _onmove(self: SpanSelector,
                event: Any) -> Optional[bool]: ...

    def _set_span_xy(self: SpanSelector,
                     event: Union[{xdata, ydata}, Any]) -> None: ...


class ToolHandles(object):
    def __init__(self: ToolHandles,
                 ax: Axes,
                 x: int,
                 y: int,
                 marker: str = 'o',
                 marker_props: dict = None,
                 useblit: bool = True) -> None: ...

    def x(self: ToolHandles) -> Union[ndarray, Any]: ...

    def y(self: ToolHandles) -> Union[ndarray, Any]: ...

    def set_data(self: ToolHandles,
                 pts: Union[list[int], Any],
                 y: Union[list[int], Any] = None) -> None: ...

    def set_visible(self: ToolHandles,
                    val: Any) -> None: ...

    def set_animated(self: ToolHandles,
                     val: Any) -> None: ...

    def closest(self: ToolHandles,
                x: Any,
                y: Any) -> Tuple[ndarray[int], Any]: ...


class RectangleSelector(_SelectorWidget):
    def __init__(self: RectangleSelector,
                 ax: Any,
                 onselect: function,
                 drawtype: str = 'box',
                 minspanx: float = 0,
                 minspany: float = 0,
                 useblit: bool = False,
                 lineprops: Optional[dict] = None,
                 rectprops: Optional[dict] = None,
                 spancoords: str = 'data',
                 button: Any = None,
                 maxdist: float = 10,
                 marker_props: dict = None,
                 interactive: bool = False,
                 state_modifier_keys: Optional[dict] = None) -> None: ...

    def _press(self: RectangleSelector,
               event: Any) -> None: ...

    def _release(self: RectangleSelector,
                 event: Any) -> Optional[bool]: ...

    def _onmove(self: RectangleSelector,
                event: Any) -> None: ...

    def _rect_bbox(self: RectangleSelector) -> Tuple[Any, Any, Any, Any]: ...

    def corners(self: RectangleSelector) -> Tuple[Tuple[Any, Any, Any, Any], Tuple[Any, Any, Any, Any]]: ...

    def edge_centers(self: RectangleSelector) -> Tuple[Tuple[Any, Union[float, Any], Any, Union[float, Any]], Tuple[
        Union[float, Any], Any, Union[float, Any], Any]]: ...

    def center(self: RectangleSelector) -> Tuple[Union[float, Any], Union[float, Any]]: ...

    def extents(self: RectangleSelector) -> Tuple[Any, Any, Any, Any]: ...

    def extents(self: RectangleSelector,
                extents: Any) -> None: ...

    def draw_shape(self: RectangleSelector,
                   extents: Any) -> None: ...

    def _set_active_handle(self: RectangleSelector,
                           event: {x, y}) -> None: ...

    def geometry(self: RectangleSelector) -> ndarray: ...


class EllipseSelector(RectangleSelector):
    def draw_shape(self: EllipseSelector,
                   extents: Any) -> None: ...

    def _rect_bbox(self: EllipseSelector) -> Union[
        Tuple[Union[float, Any], Union[float, Any], Any, Any], Tuple[Any, Any, Any, Any]]: ...


class LassoSelector(_SelectorWidget):
    def __init__(self: LassoSelector,
                 ax: Any,
                 onselect: function = None,
                 useblit: bool = True,
                 lineprops: Optional[{update}] = None,
                 button: Any = None) -> None: ...

    def onpress(self: LassoSelector,
                event: Any) -> None: ...

    def _press(self: LassoSelector,
               event: {xdata, ydata}) -> None: ...

    def onrelease(self: LassoSelector,
                  event: Any) -> None: ...

    def _release(self: LassoSelector,
                 event: Any) -> None: ...

    def _onmove(self: LassoSelector,
                event: {xdata, ydata}) -> None: ...


class PolygonSelector(_SelectorWidget):
    def __init__(self: PolygonSelector,
                 ax: Any,
                 onselect: function,
                 useblit: bool = False,
                 lineprops: dict = None,
                 markerprops: Any = None,
                 vertex_select_radius: int = 15) -> None: ...

    def _press(self: PolygonSelector,
               event: Any) -> None: ...

    def _release(self: PolygonSelector,
                 event: Any) -> None: ...

    def onmove(self: PolygonSelector,
               event: Any) -> bool: ...

    def _onmove(self: PolygonSelector,
                event: Any) -> None: ...

    def _on_key_press(self: PolygonSelector,
                      event: Any) -> None: ...

    def _on_key_release(self: PolygonSelector,
                        event: {key}) -> None: ...

    def _draw_polygon(self: PolygonSelector) -> None: ...

    def verts(self: PolygonSelector) -> list[Tuple[int, int]]: ...


class Lasso(AxesWidget):
    def __init__(self: Lasso,
                 ax: Any,
                 xy: tuple[float, float],
                 callback: Callable = None,
                 useblit: bool = True) -> None: ...

    def onrelease(self: Lasso,
                  event: Any) -> None: ...

    def onmove(self: Lasso,
               event: {inaxes, button, xdata, ydata}) -> None: ...
