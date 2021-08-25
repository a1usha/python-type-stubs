from matplotlib.container import StemContainer as StemContainer
from matplotlib.container import ErrorbarContainer as ErrorbarContainer
from matplotlib.container import BarContainer as BarContainer
from matplotlib.axes._secondary_axes import SecondaryAxis as SecondaryAxis
from matplotlib.axes._base import _process_plot_format as _process_plot_format
from matplotlib.axes._base import _TransformedBoundsLocator as _TransformedBoundsLocator
from matplotlib.axes._base import _AxesBase as _AxesBase
from matplotlib import rcParams as rcParams
from matplotlib import _preprocess_data as _preprocess_data
from matplotlib import _api as _api
from numpy import ma as ma
from numbers import Number as Number
from numbers import Integral as Integral
from typing import Callable
from typing import ClassVar
from typing import Iterable
from typing import Optional
from typing import Sized
from typing import Tuple
from typing import Union

from matplotlib import _api
from matplotlib.axes._axes import Axes
from matplotlib.axes._base import _AxesBase
from matplotlib.axes._secondary_axes import SecondaryAxis
from matplotlib.contour import QuadContourSet
from matplotlib.path import Path
from matplotlib.quiver import Barbs
from matplotlib.quiver import Quiver
from matplotlib.quiver import QuiverKey
from matplotlib.text import Annotation
from numpy.core._multiarray_umath import ndarray

_log: Logger
from typing import Any


class Axes(_AxesBase):
    __doc__: ClassVar[str]
    __doc__: ClassVar[str]
    fill_between: ClassVar[Union[partial[Any], Callable[[Any, tuple[Any, ...], Any, dict[str, Any]], Any]]]
    fill_betweenx: ClassVar[Union[partial[Any], Callable[[Any, tuple[Any, ...], Any, dict[str, Any]], Any]]]
    __doc__: ClassVar[Union[str, Any]]
    __doc__: ClassVar[Union[str, Any]]
    table: ClassVar[{__doc__}]
    stackplot: ClassVar[Any]
    streamplot: ClassVar[Any]
    tricontour: ClassVar[{__doc__}]
    tricontourf: ClassVar[{__doc__}]
    tripcolor: ClassVar[Callable[
        [{grid, update_datalim, autoscale_view, add_collection}, tuple[Any, ...], float, Any, Any, Any, Any, str, Any,
         dict[str, Any]], Union[TriMesh, PolyCollection]]]
    triplot: ClassVar[Callable[[Any, tuple[Any, ...], dict[str, Any]], Any]]
    legend_: Legend
    _autotitlepos: bool

    def get_title(self: Axes,
                  loc: str = "center") -> str: ...

    def set_title(self: Axes,
                  label: str,
                  fontdict: dict = None,
                  loc: str = None,
                  pad: float = None,
                  *,
                  y: float = None,
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

    def get_legend_handles_labels(self: Axes,
                                  legend_handler_map: Any = None) -> Tuple[list[Any], list[Any]]: ...

    def legend(self: Axes,
               *args,
               **kwargs) -> Any: ...

    def _remove_legend(self: Axes,
                       legend: Any) -> None: ...

    def inset_axes(self: Axes,
                   bounds: Any,
                   *,
                   transform: Any = None,
                   zorder: Union[int, float, complex] = 5,
                   **kwargs) -> Any: ...

    def indicate_inset(self: Axes,
                       bounds: Any,
                       inset_ax: Any = None,
                       *,
                       transform: Any = None,
                       facecolor: Any = 'none',
                       edgecolor: Any = '0.5',
                       alpha: float = 0.5,
                       zorder: float = 4.99,
                       **kwargs) -> Any: ...

    def indicate_inset_zoom(self: Axes,
                            inset_ax: Any,
                            **kwargs) -> Any: ...

    def secondary_xaxis(self: Axes,
                        location: Any,
                        *,
                        functions: Any = None,
                        **kwargs) -> Union[SecondaryAxis, Any]: ...

    def secondary_yaxis(self: Axes,
                        location: Any,
                        *,
                        functions: Any = None,
                        **kwargs) -> Union[SecondaryAxis, Any]: ...

    def text(self: Axes,
             x: float,
             y: float,
             s: str,
             fontdict: dict = None,
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

    @_api.rename_parameter("3.3", "s", "text")
    def annotate(self: Axes,
                 text: Union[str, Any],
                 xy: Any,
                 *args,
                 **kwargs) -> Union[Annotation, Any]: ...

    def axhline(self: Axes,
                y: float = 0,
                xmin: float = 0,
                xmax: float = 1,
                xdata: Union[ndarray, Any] = ...,
                ydata: Union[ndarray, Any] = ...,
                linewidth: Optional[Any] = ...,
                linestyle: Union[str, Any] = ...,
                color: Any = ...,
                marker: Union[ndarray, str, Path, Sized, Iterable, int, float] = ...,
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

    def axvline(self: Axes,
                x: float = 0,
                ymin: float = 0,
                ymax: float = 1,
                xdata: Union[ndarray, Any] = ...,
                ydata: Union[ndarray, Any] = ...,
                linewidth: Optional[Any] = ...,
                linestyle: Union[str, Any] = ...,
                color: Any = ...,
                marker: Union[ndarray, str, Path, Sized, Iterable, int, float] = ...,
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

    def _check_no_units(vals: Union[list[float], Any],
                        names: Union[list[str], Any]) -> Any: ...

    def axline(self: Axes,
               xy1: tuple[float, float],
               xy2: tuple[float, float] = None,
               *,
               slope: Optional[float] = None,
               xdata: Union[ndarray, Any] = ...,
               ydata: Union[ndarray, Any] = ...,
               linewidth: Optional[Any] = ...,
               linestyle: Union[str, Any] = ...,
               color: Any = ...,
               marker: Union[ndarray, str, Path, Sized, Iterable, int, float] = ...,
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

    def axhspan(self: Axes,
                ymin: float,
                ymax: float,
                xmin: float = 0,
                xmax: float = 1,
                xy: Any = ...,
                closed: bool = ...,
                **kwargs) -> Any: ...

    def axvspan(self: Axes,
                xmin: float,
                xmax: float,
                ymin: float = 0,
                ymax: float = 1,
                xy: Any = ...,
                closed: bool = ...,
                **kwargs) -> Any: ...

    def hlines(self: Axes,
               y: Union[float, ndarray, Iterable, int],
               xmin: Union[float, ndarray, Iterable, int],
               xmax: Union[float, ndarray, Iterable, int],
               colors: Iterable = None,
               linestyles: Optional[str] = 'solid',
               label: str = '',
               segments: list = ...,
               zorder: Any = ...,
               **kwargs) -> Any: ...

    def vlines(self: Axes,
               x: Union[float, ndarray, Iterable, int],
               ymin: Union[float, ndarray, Iterable, int],
               ymax: Union[float, ndarray, Iterable, int],
               colors: Iterable = None,
               linestyles: Optional[str] = 'solid',
               label: str = '',
               segments: list = ...,
               zorder: Any = ...,
               **kwargs) -> Any: ...

    def eventplot(self: Axes,
                  positions: Union[ndarray, Iterable, int, float, Iterable[ndarray]],
                  orientation: str = 'horizontal',
                  lineoffsets: Union[float, ndarray, Iterable, int] = 1,
                  linelengths: Union[float, ndarray, Iterable, int] = 1,
                  linewidths: Union[float, ndarray, Iterable, int] = None,
                  colors: Union[Iterable, Any] = None,
                  linestyles: Any = 'solid',
                  **kwargs) -> Any: ...

    def plot(self: Axes,
             scalex: bool = True,
             scaley: bool = True,
             data: Any = None,
             xdata: Union[ndarray, Any] = ...,
             ydata: Union[ndarray, Any] = ...,
             linewidth: Optional[Any] = ...,
             linestyle: Union[str, Any] = ...,
             color: Any = ...,
             marker: Union[ndarray, str, Path, Sized, Iterable, int, float] = ...,
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
             *args,
             **kwargs) -> Any: ...

    def plot_date(self: Axes,
                  x: Union[ndarray, Iterable, int, float],
                  y: Union[ndarray, Iterable, int, float],
                  fmt: Optional[str] = 'o',
                  tz: Any = None,
                  xdate: bool = True,
                  ydate: bool = False,
                  xdata: Union[ndarray, Any] = ...,
                  ydata: Union[ndarray, Any] = ...,
                  linewidth: Optional[Any] = ...,
                  linestyle: Union[str, Any] = ...,
                  color: Any = ...,
                  marker: Union[ndarray, str, Path, Sized, Iterable, int, float] = ...,
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

    def loglog(self: Axes,
               *args,
               **kwargs) -> Any: ...

    def semilogx(self: Axes,
                 *args,
                 **kwargs) -> Any: ...

    def semilogy(self: Axes,
                 *args,
                 **kwargs) -> Any: ...

    def acorr(self: Axes,
              x: Union[ndarray, Iterable, int, float],
              **kwargs) -> Any: ...

    def xcorr(self: Axes,
              x: Any,
              y: Any,
              normed: bool = True,
              detrend: Callable = mlab.detrend_none,
              usevlines: bool = True,
              maxlags: int = 10,
              **kwargs) -> Any: ...

    def step(self: Axes,
             x: Union[ndarray, Iterable, int, float],
             y: Union[ndarray, Iterable, int, float],
             where: str = 'pre',
             data: Any = None,
             *args,
             **kwargs) -> Any: ...

    def _convert_dx(dx: Union[Union[None, float, ndarray, Iterable, int], Any],
                    x0: Union[Union[int, float, ndarray, Iterable], Any],
                    xconv: Union[ndarray, Any],
                    convert: Union[Union[Callable[[Any], Any], Callable[[Any], Any], Callable[[Any], Any], Callable[
                        [Any], Any], Callable[[Any], Any]], Any]) -> Union[Optional[list[Optional[Any]]], Any]: ...

    def bar(self: Axes,
            x: Union[float, ndarray, Iterable, int],
            height: Union[float, ndarray, Iterable, int],
            width: Union[float, ndarray, Iterable, int] = 0.8,
            bottom: Union[float, ndarray, Iterable, int] = None,
            *,
            align: str = "center",
            xy: tuple[float, float] = ...,
            angle: Any = ...,
            **kwargs) -> Any: ...

    def barh(self: Axes,
             y: Union[float, ndarray, Iterable, int],
             width: Union[float, ndarray, Iterable, int],
             height: Union[float, ndarray, Iterable, int] = 0.8,
             left: Union[float, ndarray, Iterable, int] = None,
             *,
             align: str = "center",
             xy: tuple[float, float] = ...,
             angle: Any = ...,
             **kwargs) -> Any: ...

    def bar_label(self: Axes,
                  container: Any,
                  labels: Union[ndarray, Iterable, int, float, None] = None,
                  *,
                  fmt: str = "%g",
                  label_type: str = "edge",
                  padding: float = 0,
                  **kwargs) -> Any: ...

    def broken_barh(self: Axes,
                    xranges: Any,
                    yrange: Any,
                    **kwargs) -> Any: ...

    def stem(self: Axes,
             linefmt: Optional[str] = None,
             markerfmt: Optional[str] = None,
             basefmt: str = None,
             bottom: float = 0,
             label: str = None,
             use_line_collection: bool = True,
             orientation: str = 'vertical',
             *args) -> Any: ...

    def pie(self: Axes,
            x: int,
            explode: Union[ndarray, Iterable, int, float] = None,
            labels: Iterable = None,
            colors: Union[ndarray, Iterable, int, float] = None,
            autopct: Union[None, str, Callable] = None,
            pctdistance: float = 0.6,
            shadow: bool = False,
            labeldistance: Optional[float] = 1.1,
            startangle: float = 0,
            radius: float = 1,
            counterclock: bool = True,
            wedgeprops: dict = None,
            textprops: dict = None,
            center: int = (0, 0),
            frame: bool = False,
            rotatelabels: bool = False,
            *,
            normalize: Optional[bool] = None) -> list: ...

    def errorbar(self: Axes,
                 x: Union[float, ndarray, Iterable, int],
                 y: Union[float, ndarray, Iterable, int],
                 yerr: Union[float, ndarray, Iterable, int, None] = None,
                 xerr: Union[float, ndarray, Iterable, int, None] = None,
                 fmt: str = '',
                 ecolor: Any = None,
                 elinewidth: float = None,
                 capsize: float = None,
                 barsabove: bool = False,
                 lolims: bool = False,
                 uplims: bool = False,
                 xlolims: bool = False,
                 xuplims: bool = False,
                 errorevery: Any = 1,
                 capthick: float = None,
                 **kwargs) -> Any: ...

    def boxplot(self: Axes,
                x: Any,
                notch: bool = None,
                sym: Optional[str] = None,
                vert: bool = None,
                whis: Any = None,
                positions: Union[ndarray, Iterable, int, float, None] = None,
                widths: Union[float, ndarray, Iterable, int] = None,
                patch_artist: bool = None,
                bootstrap: Optional[int] = None,
                usermedians: Optional[int] = None,
                conf_intervals: Union[ndarray, Iterable, int, float, None] = None,
                meanline: bool = None,
                showmeans: Any = None,
                showcaps: Any = None,
                showbox: Any = None,
                showfliers: Any = None,
                boxprops: Any = None,
                labels: Optional[Iterable] = None,
                flierprops: Any = None,
                medianprops: Any = None,
                meanprops: Any = None,
                capprops: Any = None,
                whiskerprops: Any = None,
                manage_ticks: bool = True,
                autorange: bool = False,
                zorder: float = None) -> dict: ...

    def bxp(self: Axes,
            bxpstats: Iterable,
            positions: Union[ndarray, Iterable, int, float] = None,
            widths: Union[ndarray, Iterable, int, float] = None,
            vert: bool = True,
            patch_artist: bool = False,
            shownotches: bool = False,
            showmeans: bool = False,
            showcaps: bool = True,
            showbox: bool = True,
            showfliers: bool = True,
            boxprops: Any = None,
            whiskerprops: Any = None,
            flierprops: Any = None,
            medianprops: Any = None,
            capprops: Any = None,
            meanprops: Any = None,
            meanline: bool = False,
            manage_ticks: bool = True,
            zorder: float = None) -> dict: ...

    def _parse_scatter_color_args(c: Union[Optional[Iterable], Any],
                                  edgecolors: str,
                                  kwargs: dict,
                                  xsize: int,
                                  get_next_color_func: Callable) -> Any: ...

    def scatter(self: Axes,
                x: Union[float, ndarray, Iterable, int],
                y: Union[float, ndarray, Iterable, int],
                s: Union[float, ndarray, Iterable, int, None] = None,
                c: Union[Union[ndarray, Iterable, int, float, None], Any] = None,
                marker: Any = None,
                cmap: Any = None,
                norm: Any = None,
                vmin: float = None,
                vmax: float = None,
                alpha: float = None,
                linewidths: Union[float, ndarray, Iterable, int] = None,
                *,
                edgecolors: str = None,
                plotnonfinite: bool = False,
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

    def hexbin(self: Axes,
               x: Union[ndarray, Iterable, int, float],
               y: Union[ndarray, Iterable, int, float],
               C: Union[ndarray, Iterable, int, float, None] = None,
               gridsize: Any = 100,
               bins: Any = None,
               xscale: str = 'linear',
               yscale: str = 'linear',
               extent: float = None,
               cmap: Any = None,
               norm: Any = None,
               vmin: Any = None,
               vmax: Any = None,
               alpha: Any = None,
               linewidths: Any = None,
               edgecolors: str = 'face',
               reduce_C_function: Union[Union[{__name__}, Callable, functools.pyi, Callable[
                   [Union[Iterable, tuple], dict], Any]], Any] = np.mean,
               mincnt: Any = None,
               marginals: bool = False,
               verts: Any = ...,
               sizes: Any = ...,
               closed: Any = ...,
               **kwargs) -> Any: ...

    def arrow(self: Axes,
              x: float,
              y: float,
              dx: float,
              dy: float,
              **kwargs) -> Any: ...

    def quiverkey(self: Axes,
                  Q: Any,
                  X: Any,
                  Y: Any,
                  U: Any,
                  label: Any,
                  **kwargs) -> Union[QuiverKey, Any]: ...

    def _quiver_units(self: Axes,
                      args: Union[tuple[Any, ...], Any],
                      kw: Union[dict[str, Any], Any]) -> Union[Tuple[Any, ...], Any]: ...

    def quiver(self: Axes,
               *args,
               **kwargs) -> Union[Quiver, Any]: ...

    def barbs(self: Axes,
              *args,
              **kwargs) -> Union[Barbs, Any]: ...

    def fill(self: Axes,
             data: Any = None,
             xy: Any = ...,
             closed: bool = ...,
             *args,
             **kwargs) -> Any: ...

    def _fill_between_x_or_y(self: Axes,
                             ind_dir: Union[str, Any],
                             ind: Any,
                             dep1: Any,
                             dep2: int = 0,
                             *,
                             where: Any = None,
                             interpolate: bool = False,
                             step: Optional[str] = None,
                             verts: Any = ...,
                             sizes: Any = ...,
                             closed: Any = ...,
                             **kwargs) -> Any: ...

    def fill_between(self: Axes,
                     x: Any,
                     y1: Any,
                     y2: int = 0,
                     where: Any = None,
                     interpolate: bool = False,
                     step: Any = None,
                     **kwargs) -> Any: ...

    def fill_betweenx(self: Axes,
                      y: Any,
                      x1: Any,
                      x2: int = 0,
                      where: Any = None,
                      step: Any = None,
                      interpolate: bool = False,
                      **kwargs) -> Any: ...

    def imshow(self: Axes,
               X: Any,
               cmap: Any = None,
               norm: Any = None,
               aspect: str = None,
               interpolation: str = None,
               alpha: Union[float, ndarray, Iterable, int, None] = None,
               vmin: Optional[float] = None,
               vmax: Optional[float] = None,
               origin: str = None,
               extent: Any = None,
               *,
               filternorm: bool = True,
               filterrad: Any = 4.0,
               resample: bool = None,
               url: Optional[str] = None,
               **kwargs) -> Any: ...

    def _pcolorargs(self: Axes,
                    funcname: Union[str, Any],
                    shading: str = 'flat',
                    *args,
                    **kwargs) -> Union[Tuple[Any, Any, Union[ndarray, Iterable, int, float, None], str], Tuple[
        Union[Optional[ndarray], Any], Union[Optional[ndarray], Any], Union[
            ndarray, Iterable, int, float, None], str]]: ...

    def pcolor(self: Axes,
               shading: Optional[str] = None,
               alpha: float = None,
               norm: Any = None,
               cmap: Any = None,
               vmin: float = None,
               vmax: float = None,
               verts: Any = ...,
               sizes: Any = ...,
               closed: Any = ...,
               *args,
               **kwargs) -> Any: ...

    def pcolormesh(self: Axes,
                   alpha: float = None,
                   norm: Any = None,
                   cmap: Any = None,
                   vmin: float = None,
                   vmax: float = None,
                   shading: Optional[str] = None,
                   antialiased: bool = False,
                   meshWidth: Any = ...,
                   meshHeight: Any = ...,
                   coordinates: Any = ...,
                   *args,
                   **kwargs) -> Any: ...

    def pcolorfast(self: Axes,
                   alpha: float = None,
                   norm: Any = None,
                   cmap: Any = None,
                   vmin: float = None,
                   vmax: float = None,
                   *args,
                   **kwargs) -> Any: ...

    def contour(self: Axes,
                *args,
                **kwargs) -> Union[QuadContourSet, Any]: ...

    def contourf(self: Axes,
                 *args,
                 **kwargs) -> Union[QuadContourSet, Any]: ...

    def clabel(self: Axes,
               CS: Any,
               levels: Union[ndarray, Iterable, int, float, None] = None,
               **kwargs) -> Any: ...

    def hist(self: Axes,
             x: Any,
             bins: Union[int, Iterable, str] = None,
             range: Union[Iterable, tuple, None] = None,
             density: bool = False,
             weights: Any = None,
             cumulative: Any = False,
             bottom: Union[ndarray, Iterable, int, float, complex] = None,
             histtype: str = 'bar',
             align: str = 'mid',
             orientation: str = 'vertical',
             rwidth: Optional[float] = None,
             log: bool = False,
             color: Union[Union[ndarray, Iterable, int, float, None], Any] = None,
             label: Optional[str] = None,
             stacked: bool = False,
             edgecolor: Any = ...,
             facecolor: Any = ...,
             linewidth: int = ...,
             linestyle: str = ...,
             antialiased: Optional[Any] = ...,
             hatch: Any = ...,
             fill: bool = ...,
             capstyle: Any = ...,
             joinstyle: Any = ...,
             **kwargs) -> Union[array.pyi, list]: ...

    def stairs(self: Axes,
               values: Union[ndarray, Iterable, int, float],
               edges: Union[ndarray, Iterable, int, float] = None,
               *,
               orientation: str = 'vertical',
               baseline: Union[float, ndarray, Iterable, int, None] = 0,
               fill: bool = False,
               **kwargs) -> Any: ...

    def hist2d(self: Axes,
               x: Union[ndarray, Iterable, int, float],
               y: Union[ndarray, Iterable, int, float],
               bins: Any = 10,
               range: Optional[int] = None,
               density: bool = False,
               weights: Union[ndarray, Iterable, int, float, None] = None,
               cmin: float = None,
               cmax: float = None,
               **kwargs) -> Any: ...

    def psd(self: Axes,
            x: Any,
            NFFT: Any = None,
            Fs: Any = None,
            Fc: int = None,
            detrend: Any = None,
            window: Any = None,
            noverlap: int = None,
            pad_to: Any = None,
            sides: Any = None,
            scale_by_freq: Any = None,
            return_line: bool = None,
            xdata: Union[ndarray, Any] = ...,
            ydata: Union[ndarray, Any] = ...,
            linewidth: Optional[Any] = ...,
            linestyle: Union[str, Any] = ...,
            color: Any = ...,
            marker: Union[ndarray, str, Path, Sized, Iterable, int, float] = ...,
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

    def csd(self: Axes,
            x: Any,
            y: Any,
            NFFT: Any = None,
            Fs: Any = None,
            Fc: int = None,
            detrend: Any = None,
            window: Any = None,
            noverlap: int = None,
            pad_to: Any = None,
            sides: Any = None,
            scale_by_freq: Any = None,
            return_line: bool = None,
            xdata: Union[ndarray, Any] = ...,
            ydata: Union[ndarray, Any] = ...,
            linewidth: Optional[Any] = ...,
            linestyle: Union[str, Any] = ...,
            color: Any = ...,
            marker: Union[ndarray, str, Path, Sized, Iterable, int, float] = ...,
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

    def magnitude_spectrum(self: Axes,
                           x: Any,
                           Fs: Any = None,
                           Fc: int = None,
                           window: Any = None,
                           pad_to: Any = None,
                           sides: Any = None,
                           scale: str = None,
                           xdata: Union[ndarray, Any] = ...,
                           ydata: Union[ndarray, Any] = ...,
                           linewidth: Optional[Any] = ...,
                           linestyle: Union[str, Any] = ...,
                           color: Any = ...,
                           marker: Union[ndarray, str, Path, Sized, Iterable, int, float] = ...,
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

    def angle_spectrum(self: Axes,
                       x: Any,
                       Fs: Any = None,
                       Fc: int = None,
                       window: Any = None,
                       pad_to: Any = None,
                       sides: Any = None,
                       xdata: Union[ndarray, Any] = ...,
                       ydata: Union[ndarray, Any] = ...,
                       linewidth: Optional[Any] = ...,
                       linestyle: Union[str, Any] = ...,
                       color: Any = ...,
                       marker: Union[ndarray, str, Path, Sized, Iterable, int, float] = ...,
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

    def phase_spectrum(self: Axes,
                       x: Any,
                       Fs: Any = None,
                       Fc: int = None,
                       window: Any = None,
                       pad_to: Any = None,
                       sides: Any = None,
                       xdata: Union[ndarray, Any] = ...,
                       ydata: Union[ndarray, Any] = ...,
                       linewidth: Optional[Any] = ...,
                       linestyle: Union[str, Any] = ...,
                       color: Any = ...,
                       marker: Union[ndarray, str, Path, Sized, Iterable, int, float] = ...,
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

    def cohere(self: Axes,
               x: Any,
               y: Any,
               NFFT: int = 256,
               Fs: int = 2,
               Fc: int = 0,
               detrend: Callable[[Any, int], Any] = mlab.detrend_none,
               window: Callable[[{__len__}], Optional[Any]] = mlab.window_hanning,
               noverlap: int = 0,
               pad_to: Any = None,
               sides: str = 'default',
               scale_by_freq: Any = None,
               xdata: Union[ndarray, Any] = ...,
               ydata: Union[ndarray, Any] = ...,
               linewidth: Optional[Any] = ...,
               linestyle: Union[str, Any] = ...,
               color: Any = ...,
               marker: Union[ndarray, str, Path, Sized, Iterable, int, float] = ...,
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

    def specgram(self: Axes,
                 x: Any,
                 NFFT: Any = None,
                 Fs: Any = None,
                 Fc: int = None,
                 detrend: Any = None,
                 window: Any = None,
                 noverlap: int = None,
                 cmap: Any = None,
                 xextent: Any = None,
                 pad_to: Any = None,
                 sides: Any = None,
                 scale_by_freq: Any = None,
                 mode: str = None,
                 scale: str = None,
                 vmin: Any = None,
                 vmax: Any = None,
                 **kwargs) -> Any: ...

    def spy(self: Axes,
            Z: Any,
            precision: Any = 0,
            marker: Any = None,
            markersize: Any = None,
            aspect: Union[str, None, float] = 'equal',
            origin: str = "upper",
            **kwargs) -> Any: ...

    def matshow(self: Axes,
                Z: Any,
                **kwargs) -> Any: ...

    def violinplot(self: Axes,
                   dataset: Any,
                   positions: Union[ndarray, Iterable, int, float] = None,
                   vert: bool = True,
                   widths: Union[ndarray, Iterable, int, float] = 0.5,
                   showmeans: bool = False,
                   showextrema: bool = True,
                   showmedians: bool = False,
                   quantiles: Union[ndarray, Iterable, int, float] = None,
                   points: int = 100,
                   bw_method: Union[str, int, float, complex, Callable, None] = None) -> dict: ...

    def violin(self: Axes,
               vpstats: Iterable,
               positions: Union[ndarray, Iterable, int, float] = None,
               vert: bool = True,
               widths: Union[ndarray, Iterable, int, float] = 0.5,
               showmeans: bool = False,
               showextrema: bool = True,
               showmedians: bool = False) -> dict: ...
