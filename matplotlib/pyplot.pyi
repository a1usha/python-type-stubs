from ticker import MaxNLocator as MaxNLocator
from ticker import MultipleLocator as MultipleLocator
from ticker import AutoLocator as AutoLocator
from ticker import LogLocator as LogLocator
from ticker import LinearLocator as LinearLocator
from ticker import NullLocator as NullLocator
from ticker import FixedLocator as FixedLocator
from ticker import IndexLocator as IndexLocator
from ticker import Locator as Locator
from ticker import LogFormatterMathtext as LogFormatterMathtext
from ticker import LogFormatterExponent as LogFormatterExponent
from ticker import LogFormatter as LogFormatter
from ticker import ScalarFormatter as ScalarFormatter
from ticker import FormatStrFormatter as FormatStrFormatter
from ticker import FuncFormatter as FuncFormatter
from ticker import NullFormatter as NullFormatter
from ticker import FixedFormatter as FixedFormatter
from ticker import Formatter as Formatter
from ticker import TickHelper as TickHelper
from matplotlib.widgets import Widget as Widget
from matplotlib.widgets import Slider as Slider
from matplotlib.widgets import Button as Button
from matplotlib.widgets import SubplotTool as SubplotTool
from matplotlib.patches import Arrow as Arrow
from matplotlib.patches import Circle as Circle
from matplotlib.patches import Rectangle as Rectangle
from matplotlib.patches import Polygon as Polygon
from matplotlib.text import Annotation as Annotation
from matplotlib.text import Text as Text
from matplotlib.lines import Line2D as Line2D
from matplotlib.colors import Normalize as Normalize
from matplotlib.cm import register_cmap as register_cmap
from matplotlib.cm import get_cmap as get_cmap
from matplotlib import cm as cm
from matplotlib.scale import get_scale_names as get_scale_names
from matplotlib import mlab as mlab
from matplotlib.projections import PolarAxes as PolarAxes
from matplotlib.axes import Subplot as Subplot
from matplotlib.axes import Axes as Axes
from matplotlib.artist import Artist as Artist
from matplotlib.rcsetup import interactive_bk as _interactive_bk
from matplotlib import rcParamsOrig as rcParamsOrig
from matplotlib import get_backend as get_backend
from matplotlib import rcParamsDefault as rcParamsDefault
from matplotlib import rcParams as rcParams
from matplotlib.gridspec import SubplotSpec as SubplotSpec
from matplotlib.gridspec import GridSpec as GridSpec
from matplotlib.figure import figaspect as figaspect
from matplotlib.figure import Figure as Figure
from matplotlib.backend_bases import MouseButton as MouseButton
from matplotlib.backend_bases import FigureCanvasBase as FigureCanvasBase
from matplotlib import docstring as docstring
from matplotlib import cbook as cbook
from matplotlib import interactive as interactive
from matplotlib import _pylab_helpers as _pylab_helpers
from matplotlib import style as style
from matplotlib import rcsetup as rcsetup
from matplotlib import _api as _api
from cycler import cycler as cycler
from numbers import Number as Number
from functools import partial
from typing import Any
from typing import Callable
from typing import Generator
from typing import Iterable
from typing import Optional
from typing import Sized
from typing import Type
from typing import Union

from matplotlib import _api
from matplotlib.backend_bases import FigureManagerBase
from matplotlib.backend_bases import MouseButton
from matplotlib.cm import ScalarMappable
from matplotlib.figure import Figure
from matplotlib.path import Path
from matplotlib.projections.polar import PolarAxes
from matplotlib.pyplot import _IoffContext
from matplotlib.pyplot import _IonContext
from matplotlib.pyplot import _xkcd
from matplotlib.widgets import SubplotTool
from object import object

_code_objs: dict[Union[Callable[[Any, Any, Any, Optional[{__name__}]], Union[
    partial[Any], Callable[[tuple[Any, ...], dict[str, Any]], Any]]], Callable[
                           [Any, Any, Optional[{__name__, __signature__}]], Union[
                               partial[Any], Callable[[tuple[Any, ...], dict[str, Any]], Any]]]], CodeType]

_IP_REGISTERED: None

_INSTALL_FIG_OBSERVER: bool


def _copy_docstring_and_deprecators(method: Union[Union[
                                                      function | function | function | function | function | function | function | function | function | {
                                                          __doc__} | function | function | function | function | function | function | function | function | function | function | function | function | function | function | function | function | function | function | function | function | function | function | function | function | function | function | partial | function | function | function | function | function | function | function | function | function | function | function | function | function | function | function | function | function | function | function | function | function | function | function | function | function | function | function | function | function | function | function | function | function | function | function | function | function | function, Any], Any],
                                    func: Any = None) -> Union[partial[Any], Any]: ...


def install_repl_displayhook() -> None: ...


draw_all: Callable[[bool], None]


def uninstall_repl_displayhook() -> Any: ...


def set_loglevel(*args,
                 **kwargs) -> None: ...


def findobj(o: Optional[{findobj}] = None,
            match: Any = None,
            include_self: bool = True) -> Any: ...


def _get_required_interactive_framework(backend_mod: Union[Type[backend_mod], Any]) -> Optional[Any]: ...


def switch_backend(newbackend: str) -> None: ...


def _warn_if_gui_out_of_main_thread() -> None: ...


def new_figure_manager(*args,
                       **kwargs) -> FigureManagerBase: ...


def draw_if_interactive(*args,
                        **kwargs) -> None: ...


def show(*args,
         **kwargs) -> None: ...


def isinteractive() -> Optional[Any]: ...


class _IoffContext(object):
    wasinteractive: Optional[Any]

    def __init__(self: _IoffContext) -> None: ...

    def __enter__(self: _IoffContext) -> None: ...

    def __exit__(self: _IoffContext,
                 exc_type: Any,
                 exc_value: Any,
                 traceback: Any) -> None: ...


class _IonContext(object):
    wasinteractive: Optional[Any]

    def __init__(self: _IonContext) -> None: ...

    def __enter__(self: _IonContext) -> None: ...

    def __exit__(self: _IonContext,
                 exc_type: Any,
                 exc_value: Any,
                 traceback: Any) -> None: ...


def ioff() -> _IoffContext: ...


def ion() -> _IonContext: ...


def pause(interval: Any) -> None: ...


def rc(group: Union[str, Any],
       **kwargs) -> Optional[Any]: ...


def rc_context(rc: Union[dict[str, str], Any] = None,
               fname: Any = None) -> Union[Generator[Any, Any, None], Any]: ...


def rcdefaults() -> Optional[Any]: ...


def getp(*args,
         obj: Any,
         **kwargs) -> Optional[Any]: ...


def get(*args,
        obj: Any,
        **kwargs) -> Optional[Any]: ...


def setp(*args,
         obj: Any,
         **kwargs) -> Union[Optional[list[Optional[Any]]], Any]: ...


def xkcd(scale: Optional[float] = 1,
         length: Optional[float] = 100,
         randomness: Optional[float] = 2) -> _xkcd: ...


class _xkcd(object):
    _orig: dict

    def __init__(self: _xkcd,
                 scale: Any,
                 length: Any,
                 randomness: Any) -> Any: ...

    def __enter__(self: _xkcd) -> _xkcd: ...

    def __exit__(self: _xkcd,
                 *args) -> None: ...


def figure(num: Any = None,
           figsize: Any = None,
           dpi: float = None,
           facecolor: Any = None,
           edgecolor: Any = None,
           frameon: bool = True,
           FigureClass: Any = Figure,
           clear: bool = False,
           **kwargs) -> Any: ...


def _auto_draw_if_interactive(fig: Figure,
                              val: Any) -> None: ...


def gcf() -> Any: ...


def fignum_exists(num: Any) -> bool: ...


def get_fignums() -> list[Union[SupportsLessThan, Any]]: ...


def get_figlabels() -> list[Any]: ...


def get_current_fig_manager() -> Any: ...


def connect(s: Any,
            func: Any) -> Any: ...


def disconnect(cid: Any) -> Any: ...


def close(fig: Any = None) -> None: ...


def clf() -> None: ...


def draw() -> None: ...


def savefig(*args,
            **kwargs) -> Any: ...


def figlegend(*args,
              **kwargs) -> Any: ...


def axes(arg: Any = None,
         **kwargs) -> Any: ...


def delaxes(ax: Optional[{remove}] = None) -> None: ...


def sca(ax: {figure}) -> None: ...


def cla() -> Any: ...


def subplot(*args,
            **kwargs) -> Any: ...


@_api.make_keyword_only("3.3", "sharex")
def subplots(nrows: int = 1,
             ncols: int = 1,
             sharex: str = False,
             sharey: str = False,
             squeeze: bool = True,
             subplot_kw: Optional[dict] = None,
             gridspec_kw: Optional[dict] = None,
             **kwargs) -> Any: ...


def subplot_mosaic(mosaic: Any,
                   *,
                   subplot_kw: Optional[dict] = None,
                   gridspec_kw: Optional[dict] = None,
                   empty_sentinel: Optional[object] = '.',
                   **kwargs) -> Any: ...


def subplot2grid(shape: tuple[int, int],
                 loc: tuple[int, int],
                 rowspan: int = 1,
                 colspan: int = 1,
                 fig: Any = None,
                 **kwargs) -> Any: ...


def twinx(ax: Optional[{twinx}] = None) -> Any: ...


def twiny(ax: Optional[{twiny}] = None) -> Any: ...


def subplot_tool(targetfig: Any = None) -> SubplotTool: ...


@_api.make_keyword_only("3.3", "pad")
def tight_layout(pad: float = 1.08,
                 h_pad: float = None,
                 w_pad: float = None,
                 rect: int = None) -> Optional[Any]: ...


def box(on: Optional[bool] = None) -> None: ...


def xlim(*args,
         **kwargs) -> Any: ...


def ylim(*args,
         **kwargs) -> Any: ...


def xticks(ticks: Union[Union[Iterable, int, float, None], Any] = None,
           labels: Union[Union[Iterable, int, float, None], Any] = None,
           **kwargs) -> Any: ...


def yticks(ticks: Union[Union[Iterable, int, float, None], Any] = None,
           labels: Union[Union[Iterable, int, float, None], Any] = None,
           **kwargs) -> Any: ...


def rgrids(radii: Any = None,
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


def thetagrids(angles: Any = None,
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


def plotting() -> None: ...


def get_plot_commands() -> list[str]: ...


def colormaps() -> list[Union[str, Any]]: ...


def _setup_pyplot_info_docstrings() -> None: ...


def colorbar(mappable: Any = None,
             cax: Any = None,
             ax: Any = None,
             **kwargs) -> Any: ...


def clim(vmin: Any = None,
         vmax: Any = None) -> Any: ...


def set_cmap(cmap: Any) -> None: ...


def imread(fname: Any,
           format: Any = None) -> Any: ...


def imsave(fname: Any,
           arr: Any,
           **kwargs) -> Any: ...


def matshow(A: int,
            fignum: Union[Optional[int], Any] = None,
            **kwargs) -> Any: ...


def polar(*args,
          **kwargs) -> Union[PolarAxes, Any]: ...


def figimage(X: Any,
             xo: int = 0,
             yo: int = 0,
             alpha: Any = None,
             norm: Any = None,
             cmap: Any = None,
             vmin: Any = None,
             vmax: Any = None,
             origin: Any = None,
             resize: bool = False,
             **kwargs) -> Any: ...


def figtext(x: Any,
            y: Any,
            s: Any,
            fontdict: Any = None,
            **kwargs) -> Any: ...


def gca(**kwargs) -> Any: ...


def gci() -> Any: ...


def ginput(n: int = 1,
           timeout: int = 30,
           show_clicks: bool = True,
           mouse_add: MouseButton = MouseButton.LEFT,
           mouse_pop: MouseButton = MouseButton.RIGHT,
           mouse_stop: MouseButton = MouseButton.MIDDLE) -> Any: ...


def subplots_adjust(left: Any = None,
                    bottom: Any = None,
                    right: Any = None,
                    top: Any = None,
                    wspace: Any = None,
                    hspace: Any = None) -> Any: ...


def suptitle(t: Any,
             **kwargs) -> Any: ...


def waitforbuttonpress(timeout: int = -1) -> Any: ...


def acorr(x: Any,
          *,
          data: Any = None,
          **kwargs) -> Any: ...


def angle_spectrum(x: Any,
                   Fs: Any = None,
                   Fc: Any = None,
                   window: Any = None,
                   pad_to: Any = None,
                   sides: Any = None,
                   *,
                   data: Any = None,
                   xdata: Any = ...,
                   ydata: Any = ...,
                   linewidth: Optional[Any] = ...,
                   linestyle: Union[str, Any] = ...,
                   color: Any = ...,
                   marker: Union[str, Path, Sized, Iterable, int, float] = ...,
                   markersize: Any = ...,
                   markeredgewidth: Any = ...,
                   markeredgecolor: Union[str, Any] = ...,
                   markerfacecolor: Union[str, Any] = ...,
                   markerfacecoloralt: Union[str, Any] = ...,
                   fillstyle: Union[Optional[str], Any] = ...,
                   antialiased: Any = ...,
                   dash_capstyle: Any = ...,
                   solid_capstyle: Any = ...,
                   dash_joinstyle: Any = ...,
                   solid_joinstyle: Any = ...,
                   pickradius: float = ...,
                   drawstyle: Any = ...,
                   markevery: Any = ...,
                   **kwargs) -> Any: ...


def annotate(*args,
             text: Any,
             xy: Any,
             **kwargs) -> Any: ...


def arrow(x: Any,
          y: Any,
          dx: Any,
          dy: Any,
          **kwargs) -> Any: ...


def autoscale(enable: bool = True,
              axis: str = 'both',
              tight: Any = None) -> Any: ...


def axhline(y: int = 0,
            xmin: int = 0,
            xmax: int = 1,
            xdata: Any = ...,
            ydata: Any = ...,
            linewidth: Optional[Any] = ...,
            linestyle: Union[str, Any] = ...,
            color: Any = ...,
            marker: Union[str, Path, Sized, Iterable, int, float] = ...,
            markersize: Any = ...,
            markeredgewidth: Any = ...,
            markeredgecolor: Union[str, Any] = ...,
            markerfacecolor: Union[str, Any] = ...,
            markerfacecoloralt: Union[str, Any] = ...,
            fillstyle: Union[Optional[str], Any] = ...,
            antialiased: Any = ...,
            dash_capstyle: Any = ...,
            solid_capstyle: Any = ...,
            dash_joinstyle: Any = ...,
            solid_joinstyle: Any = ...,
            pickradius: float = ...,
            drawstyle: Any = ...,
            markevery: Any = ...,
            **kwargs) -> Any: ...


def axhspan(ymin: Any,
            ymax: Any,
            xmin: int = 0,
            xmax: int = 1,
            xy: Any = ...,
            closed: bool = ...,
            **kwargs) -> Any: ...


def axis(*args,
         emit: bool = True,
         **kwargs) -> Any: ...


def axline(xy1: Any,
           xy2: Any = None,
           *,
           slope: Any = None,
           xdata: Any = ...,
           ydata: Any = ...,
           linewidth: Optional[Any] = ...,
           linestyle: Union[str, Any] = ...,
           color: Any = ...,
           marker: Union[str, Path, Sized, Iterable, int, float] = ...,
           markersize: Any = ...,
           markeredgewidth: Any = ...,
           markeredgecolor: Union[str, Any] = ...,
           markerfacecolor: Union[str, Any] = ...,
           markerfacecoloralt: Union[str, Any] = ...,
           fillstyle: Union[Optional[str], Any] = ...,
           antialiased: Any = ...,
           dash_capstyle: Any = ...,
           solid_capstyle: Any = ...,
           dash_joinstyle: Any = ...,
           solid_joinstyle: Any = ...,
           pickradius: float = ...,
           drawstyle: Any = ...,
           markevery: Any = ...,
           **kwargs) -> Any: ...


def axvline(x: int = 0,
            ymin: int = 0,
            ymax: int = 1,
            xdata: Any = ...,
            ydata: Any = ...,
            linewidth: Optional[Any] = ...,
            linestyle: Union[str, Any] = ...,
            color: Any = ...,
            marker: Union[str, Path, Sized, Iterable, int, float] = ...,
            markersize: Any = ...,
            markeredgewidth: Any = ...,
            markeredgecolor: Union[str, Any] = ...,
            markerfacecolor: Union[str, Any] = ...,
            markerfacecoloralt: Union[str, Any] = ...,
            fillstyle: Union[Optional[str], Any] = ...,
            antialiased: Any = ...,
            dash_capstyle: Any = ...,
            solid_capstyle: Any = ...,
            dash_joinstyle: Any = ...,
            solid_joinstyle: Any = ...,
            pickradius: float = ...,
            drawstyle: Any = ...,
            markevery: Any = ...,
            **kwargs) -> Any: ...


def axvspan(xmin: Any,
            xmax: Any,
            ymin: int = 0,
            ymax: int = 1,
            xy: Any = ...,
            closed: bool = ...,
            **kwargs) -> Any: ...


def bar(x: Any,
        height: Any,
        width: float = 0.8,
        bottom: Any = None,
        *,
        align: str = 'center',
        data: Any = None,
        xy: tuple[float, float] = ...,
        angle: Any = ...,
        **kwargs) -> Any: ...


def barbs(*args,
          data: Any = None,
          **kwargs) -> Any: ...


def barh(y: Any,
         width: Any,
         height: float = 0.8,
         left: Any = None,
         *,
         align: str = 'center',
         xy: tuple[float, float] = ...,
         angle: Any = ...,
         **kwargs) -> Any: ...


def bar_label(container: Any,
              labels: Any = None,
              *,
              fmt: str = '%g',
              label_type: str = 'edge',
              padding: int = 0,
              **kwargs) -> Any: ...


def boxplot(x: Any,
            notch: Any = None,
            sym: Any = None,
            vert: Any = None,
            whis: Any = None,
            positions: Any = None,
            widths: Any = None,
            patch_artist: Any = None,
            bootstrap: Any = None,
            usermedians: Any = None,
            conf_intervals: Any = None,
            meanline: Any = None,
            showmeans: Any = None,
            showcaps: Any = None,
            showbox: Any = None,
            showfliers: Any = None,
            boxprops: Any = None,
            labels: Any = None,
            flierprops: Any = None,
            medianprops: Any = None,
            meanprops: Any = None,
            capprops: Any = None,
            whiskerprops: Any = None,
            manage_ticks: bool = True,
            autorange: bool = False,
            zorder: Any = None,
            *,
            data: Any = None) -> Any: ...


def broken_barh(xranges: Any,
                yrange: Any,
                *,
                data: Any = None,
                **kwargs) -> Any: ...


def clabel(CS: Any,
           levels: Any = None,
           **kwargs) -> Any: ...


def cohere(x: Any,
           y: Any,
           NFFT: int = 256,
           Fs: int = 2,
           Fc: int = 0,
           detrend: Callable[[Any, int], Any] = mlab.detrend_none,
           window: Callable[[{__len__}], Any] = mlab.window_hanning,
           noverlap: int = 0,
           pad_to: Any = None,
           sides: str = 'default',
           scale_by_freq: Any = None,
           *,
           data: Any = None,
           xdata: Any = ...,
           ydata: Any = ...,
           linewidth: Optional[Any] = ...,
           linestyle: Union[str, Any] = ...,
           color: Any = ...,
           marker: Union[str, Path, Sized, Iterable, int, float] = ...,
           markersize: Any = ...,
           markeredgewidth: Any = ...,
           markeredgecolor: Union[str, Any] = ...,
           markerfacecolor: Union[str, Any] = ...,
           markerfacecoloralt: Union[str, Any] = ...,
           fillstyle: Union[Optional[str], Any] = ...,
           antialiased: Any = ...,
           dash_capstyle: Any = ...,
           solid_capstyle: Any = ...,
           dash_joinstyle: Any = ...,
           solid_joinstyle: Any = ...,
           pickradius: float = ...,
           drawstyle: Any = ...,
           markevery: Any = ...,
           **kwargs) -> Any: ...


def contour(*args,
            data: Any = None,
            **kwargs) -> Any: ...


def contourf(*args,
             data: Any = None,
             **kwargs) -> Any: ...


def csd(x: Any,
        y: Any,
        NFFT: Any = None,
        Fs: Any = None,
        Fc: Any = None,
        detrend: Any = None,
        window: Any = None,
        noverlap: Any = None,
        pad_to: Any = None,
        sides: Any = None,
        scale_by_freq: Any = None,
        return_line: Any = None,
        *,
        data: Any = None,
        xdata: Any = ...,
        ydata: Any = ...,
        linewidth: Optional[Any] = ...,
        linestyle: Union[str, Any] = ...,
        color: Any = ...,
        marker: Union[str, Path, Sized, Iterable, int, float] = ...,
        markersize: Any = ...,
        markeredgewidth: Any = ...,
        markeredgecolor: Union[str, Any] = ...,
        markerfacecolor: Union[str, Any] = ...,
        markerfacecoloralt: Union[str, Any] = ...,
        fillstyle: Union[Optional[str], Any] = ...,
        antialiased: Any = ...,
        dash_capstyle: Any = ...,
        solid_capstyle: Any = ...,
        dash_joinstyle: Any = ...,
        solid_joinstyle: Any = ...,
        pickradius: float = ...,
        drawstyle: Any = ...,
        markevery: Any = ...,
        **kwargs) -> Any: ...


def errorbar(x: Any,
             y: Any,
             yerr: Any = None,
             xerr: Any = None,
             fmt: str = '',
             ecolor: Any = None,
             elinewidth: Any = None,
             capsize: Any = None,
             barsabove: bool = False,
             lolims: bool = False,
             uplims: bool = False,
             xlolims: bool = False,
             xuplims: bool = False,
             errorevery: int = 1,
             capthick: Any = None,
             *,
             data: Any = None,
             **kwargs) -> Any: ...


def eventplot(positions: Any,
              orientation: str = 'horizontal',
              lineoffsets: int = 1,
              linelengths: int = 1,
              linewidths: Any = None,
              colors: Any = None,
              linestyles: str = 'solid',
              *,
              data: Any = None,
              **kwargs) -> Any: ...


def fill(*args,
         data: Any = None,
         xy: Any = ...,
         closed: bool = ...,
         **kwargs) -> Any: ...


def fill_between(x: Any,
                 y1: Any,
                 y2: int = 0,
                 where: Any = None,
                 interpolate: bool = False,
                 step: Any = None,
                 *,
                 data: Any = None,
                 **kwargs) -> Any: ...


def fill_betweenx(y: Any,
                  x1: Any,
                  x2: int = 0,
                  where: Any = None,
                  step: Any = None,
                  interpolate: bool = False,
                  *,
                  data: Any = None,
                  **kwargs) -> Any: ...


def grid(b: Any = None,
         which: str = 'major',
         axis: str = 'both',
         **kwargs) -> Any: ...


def hexbin(x: Any,
           y: Any,
           C: Any = None,
           gridsize: int = 100,
           bins: Any = None,
           xscale: str = 'linear',
           yscale: str = 'linear',
           extent: Any = None,
           cmap: Any = None,
           norm: Any = None,
           vmin: Any = None,
           vmax: Any = None,
           alpha: Any = None,
           linewidths: Any = None,
           edgecolors: str = 'face',
           reduce_C_function: Callable[
               [Union[Union[Iterable, int, float], Any], Union[None, int, Iterable, tuple[int]], Optional[object], Any,
                Optional[bool], Any, Union[Union[Iterable, int, float[bool], None], Any]], Any] = np.mean,
           mincnt: Any = None,
           marginals: bool = False,
           *,
           data: Any = None,
           verts: Any = ...,
           sizes: Any = ...,
           closed: Any = ...,
           **kwargs) -> Any: ...


def hist(x: Any,
         bins: Any = None,
         range: Any = None,
         density: bool = False,
         weights: Any = None,
         cumulative: bool = False,
         bottom: Any = None,
         histtype: str = 'bar',
         align: str = 'mid',
         orientation: str = 'vertical',
         rwidth: Any = None,
         log: bool = False,
         color: Any = None,
         label: Any = None,
         stacked: bool = False,
         *,
         data: Any = None,
         edgecolor: Any = ...,
         facecolor: Any = ...,
         linewidth: int = ...,
         linestyle: str = ...,
         antialiased: Optional[Any] = ...,
         hatch: Any = ...,
         fill: bool = ...,
         capstyle: Any = ...,
         joinstyle: Any = ...,
         **kwargs) -> Any: ...


def stairs(values: Any,
           edges: Any = None,
           *,
           orientation: str = 'vertical',
           baseline: int = 0,
           fill: bool = False,
           data: Any = None,
           **kwargs) -> Any: ...


def hist2d(x: Any,
           y: Any,
           bins: int = 10,
           range: Any = None,
           density: bool = False,
           weights: Any = None,
           cmin: Any = None,
           cmax: Any = None,
           *,
           data: Any = None,
           **kwargs) -> Any: ...


def hlines(y: Any,
           xmin: Any,
           xmax: Any,
           colors: Any = None,
           linestyles: str = 'solid',
           label: str = '',
           *,
           data: Any = None,
           segments: list = ...,
           zorder: Any = ...,
           **kwargs) -> Any: ...


def imshow(X: Any,
           cmap: Any = None,
           norm: Any = None,
           aspect: Any = None,
           interpolation: Any = None,
           alpha: Any = None,
           vmin: Any = None,
           vmax: Any = None,
           origin: Any = None,
           extent: Any = None,
           *,
           filternorm: bool = True,
           filterrad: float = 4.0,
           resample: Any = None,
           url: Any = None,
           data: Any = None,
           **kwargs) -> Any: ...


def legend(*args,
           **kwargs) -> Any: ...


def locator_params(axis: str = 'both',
                   tight: Any = None,
                   **kwargs) -> Any: ...


def loglog(*args,
           **kwargs) -> Any: ...


def magnitude_spectrum(x: Any,
                       Fs: Any = None,
                       Fc: Any = None,
                       window: Any = None,
                       pad_to: Any = None,
                       sides: Any = None,
                       scale: Any = None,
                       *,
                       data: Any = None,
                       xdata: Any = ...,
                       ydata: Any = ...,
                       linewidth: Optional[Any] = ...,
                       linestyle: Union[str, Any] = ...,
                       color: Any = ...,
                       marker: Union[str, Path, Sized, Iterable, int, float] = ...,
                       markersize: Any = ...,
                       markeredgewidth: Any = ...,
                       markeredgecolor: Union[str, Any] = ...,
                       markerfacecolor: Union[str, Any] = ...,
                       markerfacecoloralt: Union[str, Any] = ...,
                       fillstyle: Union[Optional[str], Any] = ...,
                       antialiased: Any = ...,
                       dash_capstyle: Any = ...,
                       solid_capstyle: Any = ...,
                       dash_joinstyle: Any = ...,
                       solid_joinstyle: Any = ...,
                       pickradius: float = ...,
                       drawstyle: Any = ...,
                       markevery: Any = ...,
                       **kwargs) -> Any: ...


def margins(*args,
            x: Any = None,
            y: Any = None,
            tight: bool = True) -> Any: ...


def minorticks_off() -> Any: ...


def minorticks_on() -> Any: ...


def pcolor(*args,
           shading: Any = None,
           alpha: Any = None,
           norm: Any = None,
           cmap: Any = None,
           vmin: Any = None,
           vmax: Any = None,
           data: Any = None,
           verts: Any = ...,
           sizes: Any = ...,
           closed: Any = ...,
           **kwargs) -> Any: ...


def pcolormesh(*args,
               alpha: Any = None,
               norm: Any = None,
               cmap: Any = None,
               vmin: Any = None,
               vmax: Any = None,
               shading: Any = None,
               antialiased: bool = False,
               data: Any = None,
               meshWidth: Any = ...,
               meshHeight: Any = ...,
               coordinates: Any = ...,
               **kwargs) -> Any: ...


def phase_spectrum(x: Any,
                   Fs: Any = None,
                   Fc: Any = None,
                   window: Any = None,
                   pad_to: Any = None,
                   sides: Any = None,
                   *,
                   data: Any = None,
                   xdata: Any = ...,
                   ydata: Any = ...,
                   linewidth: Optional[Any] = ...,
                   linestyle: Union[str, Any] = ...,
                   color: Any = ...,
                   marker: Union[str, Path, Sized, Iterable, int, float] = ...,
                   markersize: Any = ...,
                   markeredgewidth: Any = ...,
                   markeredgecolor: Union[str, Any] = ...,
                   markerfacecolor: Union[str, Any] = ...,
                   markerfacecoloralt: Union[str, Any] = ...,
                   fillstyle: Union[Optional[str], Any] = ...,
                   antialiased: Any = ...,
                   dash_capstyle: Any = ...,
                   solid_capstyle: Any = ...,
                   dash_joinstyle: Any = ...,
                   solid_joinstyle: Any = ...,
                   pickradius: float = ...,
                   drawstyle: Any = ...,
                   markevery: Any = ...,
                   **kwargs) -> Any: ...


def pie(x: Any,
        explode: Any = None,
        labels: Any = None,
        colors: Any = None,
        autopct: Any = None,
        pctdistance: float = 0.6,
        shadow: bool = False,
        labeldistance: float = 1.1,
        startangle: int = 0,
        radius: int = 1,
        counterclock: bool = True,
        wedgeprops: Any = None,
        textprops: Any = None,
        center: Union[tuple[int, int], Any] = (0, 0),
        frame: bool = False,
        rotatelabels: bool = False,
        *,
        normalize: Any = None,
        data: Any = None) -> Any: ...


def plot(*args,
         scalex: bool = True,
         scaley: bool = True,
         data: Any = None,
         xdata: Any = ...,
         ydata: Any = ...,
         linewidth: Optional[Any] = ...,
         linestyle: Union[str, Any] = ...,
         color: Any = ...,
         marker: Union[str, Path, Sized, Iterable, int, float] = ...,
         markersize: Any = ...,
         markeredgewidth: Any = ...,
         markeredgecolor: Union[str, Any] = ...,
         markerfacecolor: Union[str, Any] = ...,
         markerfacecoloralt: Union[str, Any] = ...,
         fillstyle: Union[Optional[str], Any] = ...,
         antialiased: Any = ...,
         dash_capstyle: Any = ...,
         solid_capstyle: Any = ...,
         dash_joinstyle: Any = ...,
         solid_joinstyle: Any = ...,
         pickradius: float = ...,
         drawstyle: Any = ...,
         markevery: Any = ...,
         **kwargs) -> Any: ...


def plot_date(x: Any,
              y: Any,
              fmt: str = 'o',
              tz: Any = None,
              xdate: bool = True,
              ydate: bool = False,
              *,
              data: Any = None,
              xdata: Any = ...,
              ydata: Any = ...,
              linewidth: Optional[Any] = ...,
              linestyle: Union[str, Any] = ...,
              color: Any = ...,
              marker: Union[str, Path, Sized, Iterable, int, float] = ...,
              markersize: Any = ...,
              markeredgewidth: Any = ...,
              markeredgecolor: Union[str, Any] = ...,
              markerfacecolor: Union[str, Any] = ...,
              markerfacecoloralt: Union[str, Any] = ...,
              fillstyle: Union[Optional[str], Any] = ...,
              antialiased: Any = ...,
              dash_capstyle: Any = ...,
              solid_capstyle: Any = ...,
              dash_joinstyle: Any = ...,
              solid_joinstyle: Any = ...,
              pickradius: float = ...,
              drawstyle: Any = ...,
              markevery: Any = ...,
              **kwargs) -> Any: ...


def psd(x: Any,
        NFFT: Any = None,
        Fs: Any = None,
        Fc: Any = None,
        detrend: Any = None,
        window: Any = None,
        noverlap: Any = None,
        pad_to: Any = None,
        sides: Any = None,
        scale_by_freq: Any = None,
        return_line: Any = None,
        *,
        data: Any = None,
        xdata: Any = ...,
        ydata: Any = ...,
        linewidth: Optional[Any] = ...,
        linestyle: Union[str, Any] = ...,
        color: Any = ...,
        marker: Union[str, Path, Sized, Iterable, int, float] = ...,
        markersize: Any = ...,
        markeredgewidth: Any = ...,
        markeredgecolor: Union[str, Any] = ...,
        markerfacecolor: Union[str, Any] = ...,
        markerfacecoloralt: Union[str, Any] = ...,
        fillstyle: Union[Optional[str], Any] = ...,
        antialiased: Any = ...,
        dash_capstyle: Any = ...,
        solid_capstyle: Any = ...,
        dash_joinstyle: Any = ...,
        solid_joinstyle: Any = ...,
        pickradius: float = ...,
        drawstyle: Any = ...,
        markevery: Any = ...,
        **kwargs) -> Any: ...


def quiver(*args,
           data: Any = None,
           **kwargs) -> Any: ...


def quiverkey(Q: Any,
              X: Any,
              Y: Any,
              U: Any,
              label: Any,
              **kwargs) -> Any: ...


def scatter(x: Any,
            y: Any,
            s: Any = None,
            c: Any = None,
            marker: Any = None,
            cmap: Any = None,
            norm: Any = None,
            vmin: Any = None,
            vmax: Any = None,
            alpha: Any = None,
            linewidths: Any = None,
            *,
            edgecolors: Any = None,
            plotnonfinite: bool = False,
            data: Any = None,
            facecolors: Any = ...,
            linestyles: Any = ...,
            capstyle: Any = ...,
            joinstyle: Any = ...,
            antialiaseds: Any = ...,
            offsets: Any = ...,
            transOffset: Any = ...,
            pickradius: float = ...,
            hatch: str = ...,
            urls: Union[Iterable[str], list[None]] = ...,
            offset_position: Union[str, Any] = ...,
            zorder: Any = ...,
            **kwargs) -> Any: ...


def semilogx(*args,
             **kwargs) -> Any: ...


def semilogy(*args,
             **kwargs) -> Any: ...


def specgram(x: Any,
             NFFT: Any = None,
             Fs: Any = None,
             Fc: Any = None,
             detrend: Any = None,
             window: Any = None,
             noverlap: Any = None,
             cmap: Any = None,
             xextent: Any = None,
             pad_to: Any = None,
             sides: Any = None,
             scale_by_freq: Any = None,
             mode: Any = None,
             scale: Any = None,
             vmin: Any = None,
             vmax: Any = None,
             *,
             data: Any = None,
             **kwargs) -> Any: ...


def spy(Z: Any,
        precision: int = 0,
        marker: Any = None,
        markersize: Any = None,
        aspect: str = 'equal',
        origin: str = 'upper',
        **kwargs) -> Union[ScalarMappable, Any]: ...


def stackplot(*args,
              x: Any,
              labels: Union[tuple, Any] = (),
              colors: Any = None,
              baseline: str = 'zero',
              data: Any = None,
              **kwargs) -> Any: ...


def stem(*args,
         linefmt: Any = None,
         markerfmt: Any = None,
         basefmt: Any = None,
         bottom: int = 0,
         label: Any = None,
         use_line_collection: bool = True,
         orientation: str = 'vertical',
         data: Any = None) -> Any: ...


def step(*args,
         x: Any,
         y: Any,
         where: str = 'pre',
         data: Any = None,
         **kwargs) -> Any: ...


def streamplot(x: Any,
               y: Any,
               u: Any,
               v: Any,
               density: int = 1,
               linewidth: Any = None,
               color: Any = None,
               cmap: Any = None,
               norm: Any = None,
               arrowsize: int = 1,
               arrowstyle: str = '-|>',
               minlength: float = 0.1,
               transform: Any = None,
               zorder: Any = None,
               start_points: Any = None,
               maxlength: float = 4.0,
               integration_direction: str = 'both',
               *,
               data: Any = None) -> Any: ...


def table(cellText: Any = None,
          cellColours: Any = None,
          cellLoc: str = 'right',
          colWidths: Any = None,
          rowLabels: Any = None,
          rowColours: Any = None,
          rowLoc: str = 'left',
          colLabels: Any = None,
          colColours: Any = None,
          colLoc: str = 'center',
          loc: str = 'bottom',
          bbox: Any = None,
          edges: str = 'closed',
          **kwargs) -> Any: ...


def text(x: Any,
         y: Any,
         s: Any,
         fontdict: Any = None,
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


def tick_params(axis: str = 'both',
                **kwargs) -> Any: ...


def ticklabel_format(*,
                     axis: str = 'both',
                     style: str = '',
                     scilimits: Any = None,
                     useOffset: Any = None,
                     useLocale: Any = None,
                     useMathText: Any = None) -> Any: ...


def tricontour(*args,
               **kwargs) -> Any: ...


def tricontourf(*args,
                **kwargs) -> Any: ...


def tripcolor(*args,
              alpha: float = 1.0,
              norm: Any = None,
              cmap: Any = None,
              vmin: Any = None,
              vmax: Any = None,
              shading: str = 'flat',
              facecolors: Any = None,
              **kwargs) -> Any: ...


def triplot(*args,
            **kwargs) -> Any: ...


def violinplot(dataset: Any,
               positions: Any = None,
               vert: bool = True,
               widths: float = 0.5,
               showmeans: bool = False,
               showextrema: bool = True,
               showmedians: bool = False,
               quantiles: Any = None,
               points: int = 100,
               bw_method: Any = None,
               *,
               data: Any = None) -> Any: ...


def vlines(x: Any,
           ymin: Any,
           ymax: Any,
           colors: Any = None,
           linestyles: str = 'solid',
           label: str = '',
           *,
           data: Any = None,
           segments: list = ...,
           zorder: Any = ...,
           **kwargs) -> Any: ...


def xcorr(x: Any,
          y: Any,
          normed: bool = True,
          detrend: Callable[[Any, int], Any] = mlab.detrend_none,
          usevlines: bool = True,
          maxlags: int = 10,
          *,
          data: Any = None,
          **kwargs) -> Any: ...


def sci(im: Union[ScalarMappable, Any]) -> Any: ...


def title(label: Any,
          fontdict: Any = None,
          loc: Any = None,
          pad: Any = None,
          *,
          y: Any = None,
          x: Any = ...,
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


def xlabel(xlabel: Any,
           fontdict: Any = None,
           labelpad: Any = None,
           *,
           loc: Any = None,
           **kwargs) -> Any: ...


def ylabel(ylabel: Any,
           fontdict: Any = None,
           labelpad: Any = None,
           *,
           loc: Any = None,
           **kwargs) -> Any: ...


def xscale(value: Any,
           **kwargs) -> Any: ...


def yscale(value: Any,
           **kwargs) -> Any: ...


def autumn() -> None: ...


def bone() -> None: ...


def cool() -> None: ...


def copper() -> None: ...


def flag() -> None: ...


def gray() -> None: ...


def hot() -> None: ...


def hsv() -> None: ...


def jet() -> None: ...


def pink() -> None: ...


def prism() -> None: ...


def spring() -> None: ...


def summer() -> None: ...


def winter() -> None: ...


def magma() -> None: ...


def inferno() -> None: ...


def plasma() -> None: ...


def viridis() -> None: ...


def nipy_spectral() -> None: ...