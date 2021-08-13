from typing import Any
from typing import Callable
from typing import Iterable
from typing import Optional
from typing import Sized
from typing import Type
from typing import Union
from typing import tuple

from matplotlib.cm import ScalarMappable
from matplotlib.path import Path
from numpy.core._multiarray_umath import ndarray


@_copy_docstring_and_deprecators
def rc_context(rc: dict[str, str] = None,
               fname: Any = None) -> Generator[Any, Any, None]: ...


@_copy_docstring_and_deprecators
def rc(group: str,
       **kwargs) -> Optional[Any]: ...


@_copy_docstring_and_deprecators
def rcdefaults() -> Optional[Any]: ...


@functools.wraps
def set_loglevel(*args,
                 **kwargs) -> None: ...


@_copy_docstring_and_deprecators
def acorr(x: Any,
          data: Any = None,
          **kwargs) -> Any: ...


@_copy_docstring_and_deprecators
def angle_spectrum(x: Any,
                   Fs: Any = None,
                   Fc: Any = None,
                   window: Any = None,
                   pad_to: Any = None,
                   sides: Any = None,
                   data: Any = None,
                   xdata: ndarray = ...,
                   ydata: ndarray = ...,
                   linewidth: Optional[Any] = ...,
                   linestyle: str = ...,
                   color: Any = ...,
                   marker: Union[ndarray, str, Path, Sized, Iterable, int, float] = ...,
                   markersize: Any = ...,
                   markeredgewidth: Any = ...,
                   markeredgecolor: str = ...,
                   markerfacecolor: str = ...,
                   markerfacecoloralt: str = ...,
                   fillstyle: Optional[str] = ...,
                   antialiased: Any = ...,
                   dash_capstyle: Any = ...,
                   solid_capstyle: Any = ...,
                   dash_joinstyle: Any = ...,
                   solid_joinstyle: Any = ...,
                   pickradius: float = ...,
                   drawstyle: Any = ...,
                   markevery: Any = ...,
                   **kwargs) -> Any: ...


@_copy_docstring_and_deprecators
def annotate(*args,
             text: Any,
             xy: Any,
             **kwargs) -> Any: ...


@_copy_docstring_and_deprecators
def arrow(x: Any,
          y: Any,
          dx: Any,
          dy: Any,
          **kwargs) -> Any: ...


@_copy_docstring_and_deprecators
def autoscale(enable: bool = True,
              axis: str = 'both',
              tight: Any = None) -> Any: ...


def autumn() -> None: ...


@docstring.dedent_interpd
def axes(arg: Any = None,
         **kwargs) -> Any: ...


@_copy_docstring_and_deprecators
def axhline(y: int = 0,
            xmin: int = 0,
            xmax: int = 1,
            xdata: ndarray = ...,
            ydata: ndarray = ...,
            linewidth: Optional[Any] = ...,
            linestyle: str = ...,
            color: Any = ...,
            marker: Union[ndarray, str, Path, Sized, Iterable, int, float] = ...,
            markersize: Any = ...,
            markeredgewidth: Any = ...,
            markeredgecolor: str = ...,
            markerfacecolor: str = ...,
            markerfacecoloralt: str = ...,
            fillstyle: Optional[str] = ...,
            antialiased: Any = ...,
            dash_capstyle: Any = ...,
            solid_capstyle: Any = ...,
            dash_joinstyle: Any = ...,
            solid_joinstyle: Any = ...,
            pickradius: float = ...,
            drawstyle: Any = ...,
            markevery: Any = ...,
            **kwargs) -> Any: ...


@_copy_docstring_and_deprecators
def axhspan(ymin: Any,
            ymax: Any,
            xmin: int = 0,
            xmax: int = 1,
            xy: Any = ...,
            closed: bool = ...,
            **kwargs) -> Any: ...


@_copy_docstring_and_deprecators
def axis(*args,
         emit: bool = True,
         **kwargs) -> Any: ...


@_copy_docstring_and_deprecators
def axline(xy1: Any,
           xy2: Any = None,
           slope: Any = None,
           xdata: ndarray = ...,
           ydata: ndarray = ...,
           linewidth: Optional[Any] = ...,
           linestyle: str = ...,
           color: Any = ...,
           marker: Union[ndarray, str, Path, Sized, Iterable, int, float] = ...,
           markersize: Any = ...,
           markeredgewidth: Any = ...,
           markeredgecolor: str = ...,
           markerfacecolor: str = ...,
           markerfacecoloralt: str = ...,
           fillstyle: Optional[str] = ...,
           antialiased: Any = ...,
           dash_capstyle: Any = ...,
           solid_capstyle: Any = ...,
           dash_joinstyle: Any = ...,
           solid_joinstyle: Any = ...,
           pickradius: float = ...,
           drawstyle: Any = ...,
           markevery: Any = ...,
           **kwargs) -> Any: ...


@_copy_docstring_and_deprecators
def axvline(x: int = 0,
            ymin: int = 0,
            ymax: int = 1,
            xdata: ndarray = ...,
            ydata: ndarray = ...,
            linewidth: Optional[Any] = ...,
            linestyle: str = ...,
            color: Any = ...,
            marker: Union[ndarray, str, Path, Sized, Iterable, int, float] = ...,
            markersize: Any = ...,
            markeredgewidth: Any = ...,
            markeredgecolor: str = ...,
            markerfacecolor: str = ...,
            markerfacecoloralt: str = ...,
            fillstyle: Optional[str] = ...,
            antialiased: Any = ...,
            dash_capstyle: Any = ...,
            solid_capstyle: Any = ...,
            dash_joinstyle: Any = ...,
            solid_joinstyle: Any = ...,
            pickradius: float = ...,
            drawstyle: Any = ...,
            markevery: Any = ...,
            **kwargs) -> Any: ...


@_copy_docstring_and_deprecators
def axvspan(xmin: Any,
            xmax: Any,
            ymin: int = 0,
            ymax: int = 1,
            xy: Any = ...,
            closed: bool = ...,
            **kwargs) -> Any: ...


@_copy_docstring_and_deprecators
def bar(x: Any,
        height: Any,
        width: float = 0.8,
        bottom: Any = None,
        align: str = 'center',
        data: Any = None,
        xy: tuple[float, float] = ...,
        width: float = ...,
        height: float = ...,
        angle: Any = ...,
        **kwargs) -> Any: ...


@_copy_docstring_and_deprecators
def bar_label(container: Any,
              labels: Any = None,
              fmt: str = '%g',
              label_type: str = 'edge',
              padding: int = 0,
              **kwargs) -> Any: ...


@_copy_docstring_and_deprecators
def barbs(*args,
          data: Any = None,
          **kwargs) -> Any: ...


@_copy_docstring_and_deprecators
def barh(y: Any,
         width: Any,
         height: float = 0.8,
         left: Any = None,
         align: str = 'center',
         xy: tuple[float, float] = ...,
         width: float = ...,
         height: float = ...,
         angle: Any = ...,
         **kwargs) -> Any: ...


def bone() -> None: ...


def box(on: Optional[bool] = None) -> None: ...


@_copy_docstring_and_deprecators
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
            data: Any = None) -> Any: ...


@_copy_docstring_and_deprecators
def broken_barh(xranges: Any,
                yrange: Any,
                data: Any = None,
                xranges: Any = ...,
                yrange: Any = ...,
                **kwargs) -> Any: ...


def cla() -> Any: ...


@_copy_docstring_and_deprecators
def clabel(CS: Any,
           levels: Any = None,
           **kwargs) -> Any: ...


def clf() -> None: ...


def clim(vmin: Any = None,
         vmax: Any = None) -> Any: ...


def close(fig: Any = None) -> None: ...


@_copy_docstring_and_deprecators
def colorbar(mappable: Any = None,
             cax: Any = None,
             ax: Any = None,
             **kwargs) -> Any: ...


def colormaps() -> list[str]: ...


@_copy_docstring_and_deprecators
def connect(s: Any,
            func: Any) -> Any: ...


@_copy_docstring_and_deprecators
def contour(*args,
            data: Any = None,
            **kwargs) -> Any: ...


@_copy_docstring_and_deprecators
def contourf(*args,
             data: Any = None,
             **kwargs) -> Any: ...


def cool() -> None: ...


def copper() -> None: ...


def delaxes(ax: Optional[{remove}] = None) -> None: ...


@_copy_docstring_and_deprecators
def disconnect(cid: Any) -> Any: ...


def draw() -> None: ...


def draw_if_interactive(*args,
                        **kwargs) -> None: ...


@_copy_docstring_and_deprecators
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
             data: Any = None,
             **kwargs) -> Any: ...


@_copy_docstring_and_deprecators
def eventplot(positions: Any,
              orientation: str = 'horizontal',
              lineoffsets: int = 1,
              linelengths: int = 1,
              linewidths: Any = None,
              colors: Any = None,
              linestyles: str = 'solid',
              data: Any = None,
              **kwargs) -> Any: ...


@_copy_docstring_and_deprecators
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


def figlegend(*args,
              **kwargs) -> Any: ...


def fignum_exists(num: Any) -> bool: ...


@_copy_docstring_and_deprecators
def figtext(x: Any,
            y: Any,
            s: Any,
            fontdict: Any = None,
            **kwargs) -> Any: ...


def figure(num: Any = None,
           figsize: Any = None,
           dpi: float = None,
           facecolor: Any = None,
           edgecolor: Any = None,
           frameon: bool = True,
           FigureClass: Any = Figure,
           clear: bool = False,
           **kwargs) -> Any: ...


@_copy_docstring_and_deprecators
def fill(*args,
         data: Any = None,
         xy: Any = ...,
         closed: bool = ...,
         **kwargs) -> Any: ...


@_copy_docstring_and_deprecators
def fill_between(x: Any,
                 y1: Any,
                 y2: int = 0,
                 where: Any = None,
                 interpolate: bool = False,
                 step: Any = None,
                 data: Any = None,
                 **kwargs) -> Any: ...


@_copy_docstring_and_deprecators
def fill_betweenx(y: Any,
                  x1: Any,
                  x2: int = 0,
                  where: Any = None,
                  step: Any = None,
                  interpolate: bool = False,
                  data: Any = None,
                  **kwargs) -> Any: ...


@_copy_docstring_and_deprecators
def findobj(o: Optional[{findobj}] = None,
            match: Any = None,
            include_self: bool = True) -> Any: ...


def flag() -> None: ...


@_copy_docstring_and_deprecators
def gca(**kwargs) -> Any: ...


def gcf() -> Any: ...


@_copy_docstring_and_deprecators
def gci() -> Any: ...


@_copy_docstring_and_deprecators
def get(*args,
        obj: Any,
        **kwargs) -> Optional[Any]: ...


def get_current_fig_manager() -> Any: ...


def get_figlabels() -> list: ...


def get_fignums() -> list[SupportsLessThan]: ...


def get_plot_commands() -> list[str]: ...


@_copy_docstring_and_deprecators
def getp(*args,
         obj: Any,
         **kwargs) -> Optional[Any]: ...


@_copy_docstring_and_deprecators
def ginput(n: int = 1,
           timeout: int = 30,
           show_clicks: bool = True,
           mouse_add: MouseButton = MouseButton.LEFT,
           mouse_pop: MouseButton = MouseButton.RIGHT,
           mouse_stop: MouseButton = MouseButton.MIDDLE) -> Any: ...


def gray() -> None: ...


@_copy_docstring_and_deprecators
def grid(b: Any = None,
         which: str = 'major',
         axis: str = 'both',
         **kwargs) -> Any: ...


@_copy_docstring_and_deprecators
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
           reduce_C_function: Union[{__name__}, Callable, functools.pyi, (args: Union[Iterable, tuple], kwargs: dict),
           mincnt: Any = None,
           marginals: bool = False,
           data: Any = None,
           verts: Any = ...,
           sizes: Any = ...,
           closed: Any = ...,
           **kwargs) -> Any: ...


@_copy_docstring_and_deprecators
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
         data: Any = None,
         edgecolor: Any = ...,
         facecolor: Any = ...,
         color: Any = ...,
         linewidth: int = ...,
         linestyle: str = ...,
         antialiased: Optional[Any] = ...,
         hatch: Any = ...,
         fill: bool = ...,
         capstyle: Any = ...,
         joinstyle: Any = ...,
         **kwargs) -> Any: ...


@_copy_docstring_and_deprecators
def hist2d(x: Any,
           y: Any,
           bins: int = 10,
           range: Any = None,
           density: bool = False,
           weights: Any = None,
           cmin: Any = None,
           cmax: Any = None,
           data: Any = None,
           **kwargs) -> Any: ...


@_copy_docstring_and_deprecators
def hlines(y: Any,
           xmin: Any,
           xmax: Any,
           colors: Any = None,
           linestyles: str = 'solid',
           label: str = '',
           data: Any = None,
           segments: list = ...,
           zorder: Any = ...,
           **kwargs) -> Any: ...


def hot() -> None: ...


def hsv() -> None: ...


@_copy_docstring_and_deprecators
def imread(fname: Any,
           format: Any = None) -> Any: ...


@_copy_docstring_and_deprecators
def imsave(fname: Any,
           arr: Any,
           **kwargs) -> Any: ...


@_copy_docstring_and_deprecators
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
           filternorm: bool = True,
           filterrad: float = 4.0,
           resample: Any = None,
           url: Any = None,
           data: Any = None,
           **kwargs) -> Any: ...


def inferno() -> None: ...


def install_repl_displayhook() -> None: ...


def ioff() -> _IoffContext: ...


def ion() -> _IonContext: ...


def isinteractive() -> Optional[Any]: ...


def jet() -> None: ...


@_copy_docstring_and_deprecators
def legend(*args,
           **kwargs) -> Any: ...


@_copy_docstring_and_deprecators
def locator_params(axis: str = 'both',
                   tight: Any = None,
                   **kwargs) -> Any: ...


@_copy_docstring_and_deprecators
def loglog(*args,
           **kwargs) -> Any: ...


def magma() -> None: ...


@_copy_docstring_and_deprecators
def magnitude_spectrum(x: Any,
                       Fs: Any = None,
                       Fc: Any = None,
                       window: Any = None,
                       pad_to: Any = None,
                       sides: Any = None,
                       scale: Any = None,
                       data: Any = None,
                       xdata: ndarray = ...,
                       ydata: ndarray = ...,
                       linewidth: Optional[Any] = ...,
                       linestyle: str = ...,
                       color: Any = ...,
                       marker: Union[ndarray, str, Path, Sized, Iterable, int, float] = ...,
                       markersize: Any = ...,
                       markeredgewidth: Any = ...,
                       markeredgecolor: str = ...,
                       markerfacecolor: str = ...,
                       markerfacecoloralt: str = ...,
                       fillstyle: Optional[str] = ...,
                       antialiased: Any = ...,
                       dash_capstyle: Any = ...,
                       solid_capstyle: Any = ...,
                       dash_joinstyle: Any = ...,
                       solid_joinstyle: Any = ...,
                       pickradius: float = ...,
                       drawstyle: Any = ...,
                       markevery: Any = ...,
                       **kwargs) -> Any: ...


@_copy_docstring_and_deprecators
def margins(*args,
            x: Any = None,
            y: Any = None,
            tight: bool = True) -> Any: ...


def matshow(A: int,
            fignum: Optional[int] = None,
            **kwargs) -> Any: ...


@_copy_docstring_and_deprecators
def minorticks_off() -> Any: ...


@_copy_docstring_and_deprecators
def minorticks_on() -> Any: ...


def new_figure_manager(*args,
                       **kwargs) -> FigureManagerBase: ...


def nipy_spectral() -> None: ...


def pause(interval: Any) -> None: ...


@_copy_docstring_and_deprecators
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


@_copy_docstring_and_deprecators
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
               antialiased: Any = ...,
               shading: Any = ...,
               **kwargs) -> Any: ...


@_copy_docstring_and_deprecators
def phase_spectrum(x: Any,
                   Fs: Any = None,
                   Fc: Any = None,
                   window: Any = None,
                   pad_to: Any = None,
                   sides: Any = None,
                   data: Any = None,
                   xdata: ndarray = ...,
                   ydata: ndarray = ...,
                   linewidth: Optional[Any] = ...,
                   linestyle: str = ...,
                   color: Any = ...,
                   marker: Union[ndarray, str, Path, Sized, Iterable, int, float] = ...,
                   markersize: Any = ...,
                   markeredgewidth: Any = ...,
                   markeredgecolor: str = ...,
                   markerfacecolor: str = ...,
                   markerfacecoloralt: str = ...,
                   fillstyle: Optional[str] = ...,
                   antialiased: Any = ...,
                   dash_capstyle: Any = ...,
                   solid_capstyle: Any = ...,
                   dash_joinstyle: Any = ...,
                   solid_joinstyle: Any = ...,
                   pickradius: float = ...,
                   drawstyle: Any = ...,
                   markevery: Any = ...,
                   **kwargs) -> Any: ...


@_copy_docstring_and_deprecators
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
        center: tuple[int, int] = (0, 0),
        frame: bool = False,
        rotatelabels: bool = False,
        normalize: Any = None,
        data: Any = None) -> Any: ...


def pink() -> None: ...


def plasma() -> None: ...


@_copy_docstring_and_deprecators
def plot(*args,
         scalex: bool = True,
         scaley: bool = True,
         data: Any = None,
         xdata: ndarray = ...,
         ydata: ndarray = ...,
         linewidth: Optional[Any] = ...,
         linestyle: str = ...,
         color: Any = ...,
         marker: Union[ndarray, str, Path, Sized, Iterable, int, float] = ...,
         markersize: Any = ...,
         markeredgewidth: Any = ...,
         markeredgecolor: str = ...,
         markerfacecolor: str = ...,
         markerfacecoloralt: str = ...,
         fillstyle: Optional[str] = ...,
         antialiased: Any = ...,
         dash_capstyle: Any = ...,
         solid_capstyle: Any = ...,
         dash_joinstyle: Any = ...,
         solid_joinstyle: Any = ...,
         pickradius: float = ...,
         drawstyle: Any = ...,
         markevery: Any = ...,
         **kwargs) -> Any: ...


@_copy_docstring_and_deprecators
def plot_date(x: Any,
              y: Any,
              fmt: str = 'o',
              tz: Any = None,
              xdate: bool = True,
              ydate: bool = False,
              data: Any = None,
              xdata: ndarray = ...,
              ydata: ndarray = ...,
              linewidth: Optional[Any] = ...,
              linestyle: str = ...,
              color: Any = ...,
              marker: Union[ndarray, str, Path, Sized, Iterable, int, float] = ...,
              markersize: Any = ...,
              markeredgewidth: Any = ...,
              markeredgecolor: str = ...,
              markerfacecolor: str = ...,
              markerfacecoloralt: str = ...,
              fillstyle: Optional[str] = ...,
              antialiased: Any = ...,
              dash_capstyle: Any = ...,
              solid_capstyle: Any = ...,
              dash_joinstyle: Any = ...,
              solid_joinstyle: Any = ...,
              pickradius: float = ...,
              drawstyle: Any = ...,
              markevery: Any = ...,
              **kwargs) -> Any: ...


def polar(*args,
          **kwargs) -> PolarAxes: ...


def prism() -> None: ...


@_copy_docstring_and_deprecators
def quiver(*args,
           data: Any = None,
           **kwargs) -> Any: ...


@_copy_docstring_and_deprecators
def quiverkey(Q: Any,
              X: Any,
              Y: Any,
              U: Any,
              label: Any,
              **kwargs) -> Any: ...


@_copy_docstring_and_deprecators
def rc(group: str,
       **kwargs) -> Optional[Any]: ...


@_copy_docstring_and_deprecators
def rc_context(rc: dict[str, str] = None,
               fname: Any = None) -> Generator[Any, Any, None]: ...


@_copy_docstring_and_deprecators
def rcdefaults() -> Optional[Any]: ...


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
           rotation: float = ...,
           linespacing: Any = ...,
           rotation_mode: Optional[str] = ...,
           usetex: Any = ...,
           wrap: bool = ...,
           transform_rotates_text: bool = ...,
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
           rotation: float = ...,
           linespacing: Any = ...,
           rotation_mode: Optional[str] = ...,
           usetex: Any = ...,
           wrap: bool = ...,
           transform_rotates_text: bool = ...,
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
           rotation: float = ...,
           linespacing: Any = ...,
           rotation_mode: Optional[str] = ...,
           usetex: Any = ...,
           wrap: bool = ...,
           transform_rotates_text: bool = ...,
           **kwargs) -> Any: ...


@_copy_docstring_and_deprecators
def savefig(*args,
            **kwargs) -> Any: ...


def sca(ax: {figure}) -> None: ...


@_copy_docstring_and_deprecators
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
            edgecolors: Any = None,
            plotnonfinite: bool = False,
            data: Any = None,
            edgecolors: Any = ...,
            facecolors: Any = ...,
            linewidths: Any = ...,
            linestyles: Any = ...,
            capstyle: Any = ...,
            joinstyle: Any = ...,
            antialiaseds: Any = ...,
            offsets: Any = ...,
            transOffset: Any = ...,
            norm: Any = ...,
            cmap: Any = ...,
            pickradius: float = ...,
            hatch: str = ...,
            urls: Union[Iterable[str], list[None]] = ...,
            offset_position: str = ...,
            zorder: Any = ...,
            **kwargs) -> Any: ...


@_copy_docstring_and_deprecators
def sci(im: ScalarMappable) -> Any: ...


@_copy_docstring_and_deprecators
def semilogx(*args,
             **kwargs) -> Any: ...


@_copy_docstring_and_deprecators
def semilogy(*args,
             **kwargs) -> Any: ...


def set_cmap(cmap: Any) -> None: ...


@_copy_docstring_and_deprecators
def setp(*args,
         obj: Any,
         **kwargs) -> Optional[list[Optional[Any]]]: ...


def show(*args,
         **kwargs) -> None: ...


def spring() -> None: ...


@_copy_docstring_and_deprecators
def spy(Z: Any,
        precision: int = 0,
        marker: Any = None,
        markersize: Any = None,
        aspect: str = 'equal',
        origin: str = 'upper',
        **kwargs) -> ScalarMappable: ...


@_copy_docstring_and_deprecators
def stem(*args,
         linefmt: Any = None,
         markerfmt: Any = None,
         basefmt: Any = None,
         bottom: int = 0,
         label: Any = None,
         use_line_collection: bool = True,
         orientation: str = 'vertical',
         data: Any = None) -> Any: ...


@_copy_docstring_and_deprecators
def step(*args,
         x: Any,
         y: Any,
         where: str = 'pre',
         data: Any = None,
         **kwargs) -> Any: ...


@_copy_docstring_and_deprecators
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
               data: Any = None) -> Any: ...


@docstring.dedent_interpd
def subplot(*args,
            **kwargs) -> Any: ...


def subplot2grid(shape: tuple[int, int],
                 loc: tuple[int, int],
                 rowspan: int = 1,
                 colspan: int = 1,
                 fig: Any = None,
                 **kwargs) -> Any: ...


def subplot_mosaic(mosaic: Any,
                   subplot_kw: Optional[dict] = None,
                   gridspec_kw: Optional[dict] = None,
                   empty_sentinel: Optional[object] = '.',
                   **kwargs) -> Any: ...


def subplot_tool(targetfig: Any = None) -> SubplotTool: ...


@_api.make_keyword_only
def subplots(nrows: int = 1,
             ncols: int = 1,
             sharex: str = False,
             sharey: str = False,
             squeeze: bool = True,
             subplot_kw: Optional[dict] = None,
             gridspec_kw: Optional[dict] = None,
             **kwargs) -> Any: ...


@_copy_docstring_and_deprecators
def subplots_adjust(left: Any = None,
                    bottom: Any = None,
                    right: Any = None,
                    top: Any = None,
                    wspace: Any = None,
                    hspace: Any = None) -> Any: ...


def summer() -> None: ...


@_copy_docstring_and_deprecators
def suptitle(t: Any,
             **kwargs) -> Any: ...


def switch_backend(newbackend: str) -> None: ...


@_copy_docstring_and_deprecators
def text(x: Any,
         y: Any,
         s: Any,
         fontdict: Any = None,
         x: Any = ...,
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
               rotation: float = ...,
               linespacing: Any = ...,
               rotation_mode: Optional[str] = ...,
               usetex: Any = ...,
               wrap: bool = ...,
               transform_rotates_text: bool = ...,
               **kwargs) -> Any: ...


@_copy_docstring_and_deprecators
def tick_params(axis: str = 'both',
                **kwargs) -> Any: ...


@_copy_docstring_and_deprecators
def ticklabel_format(axis: str = 'both',
                     style: str = '',
                     scilimits: Any = None,
                     useOffset: Any = None,
                     useLocale: Any = None,
                     useMathText: Any = None) -> Any: ...


@_api.make_keyword_only
def tight_layout(pad: float = 1.08,
                 h_pad: float = None,
                 w_pad: float = None,
                 rect: int = None) -> Optional[Any]: ...


@_copy_docstring_and_deprecators
def title(label: Any,
          fontdict: Any = None,
          loc: Any = None,
          pad: Any = None,
          y: Any = None,
          x: Any = ...,
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


@_copy_docstring_and_deprecators
def tricontour(*args,
               **kwargs) -> Any: ...


@_copy_docstring_and_deprecators
def tricontourf(*args,
                **kwargs) -> Any: ...


@_copy_docstring_and_deprecators
def tripcolor(*args,
              alpha: float = 1.0,
              norm: Any = None,
              cmap: Any = None,
              vmin: Any = None,
              vmax: Any = None,
              shading: str = 'flat',
              facecolors: Any = None,
              **kwargs) -> Any: ...


@_copy_docstring_and_deprecators
def triplot(*args,
            **kwargs) -> Any: ...


def twinx(ax: Optional[{twinx}] = None) -> Any: ...


def twiny(ax: Optional[{twiny}] = None) -> Any: ...


def uninstall_repl_displayhook() -> Any: ...


@_copy_docstring_and_deprecators
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
               data: Any = None) -> Any: ...


def viridis() -> None: ...


@_copy_docstring_and_deprecators
def vlines(x: Any,
           ymin: Any,
           ymax: Any,
           colors: Any = None,
           linestyles: str = 'solid',
           label: str = '',
           data: Any = None,
           segments: list = ...,
           zorder: Any = ...,
           **kwargs) -> Any: ...


@_copy_docstring_and_deprecators
def waitforbuttonpress(timeout: int = -1) -> Any: ...


def winter() -> None: ...


@_copy_docstring_and_deprecators
def xcorr(x: Any,
          y: Any,
          normed: bool = True,
          detrend: (x: Any, axis: int),
          usevlines: bool = True,
          maxlags: int = 10,
          data: Any = None,
          **kwargs) -> Any: ...


def xkcd(scale: Optional[float] = 1,
         length: Optional[float] = 100,
         randomness: Optional[float] = 2) -> _xkcd: ...


@_copy_docstring_and_deprecators
def xlabel(xlabel: Any,
           fontdict: Any = None,
           labelpad: Any = None,
           loc: Any = None,
           **kwargs) -> Any: ...


def xlim(*args,
         **kwargs) -> Any: ...


@_copy_docstring_and_deprecators
def xscale(value: Any,
           **kwargs) -> Any: ...


def xticks(ticks: Union[ndarray, Iterable, int, float, None] = None,
           labels: Union[ndarray, Iterable, int, float, None] = None,
           **kwargs) -> Any: ...


@_copy_docstring_and_deprecators
def ylabel(ylabel: Any,
           fontdict: Any = None,
           labelpad: Any = None,
           loc: Any = None,
           **kwargs) -> Any: ...


def ylim(*args,
         **kwargs) -> Any: ...


@_copy_docstring_and_deprecators
def yscale(value: Any,
           **kwargs) -> Any: ...


def yticks(ticks: Union[ndarray, Iterable, int, float, None] = None,
           labels: Union[ndarray, Iterable, int, float, None] = None,
           **kwargs) -> Any: ...


@_copy_docstring_and_deprecators
def imread(fname: Any,
           format: Any = None) -> Any: ...


@_copy_docstring_and_deprecators
def imsave(fname: Any,
           arr: Any,
           **kwargs) -> Any: ...


class _IonContext(object):
    def __init__(self: _IonContext) -> None: ...

    def __enter__(self: _IonContext) -> None: ...

    def __exit__(self: _IonContext,
                 exc_type: Any,
                 exc_value: Any,
                 traceback: Any) -> None: ...


class _xkcd(object):
    def __init__(self: _xkcd,
                 scale: Any,
                 length: Any,
                 randomness: Any) -> Any: ...

    def __enter__(self: _xkcd) -> _xkcd: ...

    def __exit__(self: _xkcd,
                 *args) -> None: ...


class _IoffContext(object):
    def __init__(self: _IoffContext) -> None: ...

    def __enter__(self: _IoffContext) -> None: ...

    def __exit__(self: _IoffContext,
                 exc_type: Any,
                 exc_value: Any,
                 traceback: Any) -> None: ...


def plotting() -> None: ...


def _warn_if_gui_out_of_main_thread() -> None: ...


def _get_required_interactive_framework(backend_mod: Type[backend_mod]) -> Optional[Any]: ...


def _setup_pyplot_info_docstrings() -> None: ...


def _auto_draw_if_interactive(fig: Figure,
                              val: Any) -> None: ...


@_copy_docstring_and_deprecators
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
             data: Any = None,
             **kwargs) -> Any: ...


@_copy_docstring_and_deprecators
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
        data: Any = None,
        xdata: ndarray = ...,
        ydata: ndarray = ...,
        linewidth: Optional[Any] = ...,
        linestyle: str = ...,
        color: Any = ...,
        marker: Union[ndarray, str, Path, Sized, Iterable, int, float] = ...,
        markersize: Any = ...,
        markeredgewidth: Any = ...,
        markeredgecolor: str = ...,
        markerfacecolor: str = ...,
        markerfacecoloralt: str = ...,
        fillstyle: Optional[str] = ...,
        antialiased: Any = ...,
        dash_capstyle: Any = ...,
        solid_capstyle: Any = ...,
        dash_joinstyle: Any = ...,
        solid_joinstyle: Any = ...,
        pickradius: float = ...,
        drawstyle: Any = ...,
        markevery: Any = ...,
        **kwargs) -> Any: ...


@_copy_docstring_and_deprecators
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
        data: Any = None,
        xdata: ndarray = ...,
        ydata: ndarray = ...,
        linewidth: Optional[Any] = ...,
        linestyle: str = ...,
        color: Any = ...,
        marker: Union[ndarray, str, Path, Sized, Iterable, int, float] = ...,
        markersize: Any = ...,
        markeredgewidth: Any = ...,
        markeredgecolor: str = ...,
        markerfacecolor: str = ...,
        markerfacecoloralt: str = ...,
        fillstyle: Optional[str] = ...,
        antialiased: Any = ...,
        dash_capstyle: Any = ...,
        solid_capstyle: Any = ...,
        dash_joinstyle: Any = ...,
        solid_joinstyle: Any = ...,
        pickradius: float = ...,
        drawstyle: Any = ...,
        markevery: Any = ...,
        **kwargs) -> Any: ...


@_copy_docstring_and_deprecators
def stackplot(*args,
              x: Any,
              labels: tuple = (),
              colors: Any = None,
              baseline: str = 'zero',
              data: Any = None,
              **kwargs) -> Any: ...


@_copy_docstring_and_deprecators
def stairs(values: Any,
           edges: Any = None,
           orientation: str = 'vertical',
           baseline: int = 0,
           fill: bool = False,
           data: Any = None,
           values: Any = ...,
           edges: Any = ...,
           orientation: Any = ...,
           baseline: Any = ...,
           **kwargs) -> Any: ...


@_copy_docstring_and_deprecators
def cohere(x: Any,
           y: Any,
           NFFT: int = 256,
           Fs: int = 2,
           Fc: int = 0,
           detrend: (x: Any, axis: int),
           window: (x: {__len__}),
           noverlap: int = 0,
           pad_to: Any = None,
           sides: str = 'default',
           scale_by_freq: Any = None,
           data: Any = None,
           xdata: ndarray = ...,
           ydata: ndarray = ...,
           linewidth: Optional[Any] = ...,
           linestyle: str = ...,
           color: Any = ...,
           marker: Union[ndarray, str, Path, Sized, Iterable, int, float] = ...,
           markersize: Any = ...,
           markeredgewidth: Any = ...,
           markeredgecolor: str = ...,
           markerfacecolor: str = ...,
           markerfacecoloralt: str = ...,
           fillstyle: Optional[str] = ...,
           antialiased: Any = ...,
           dash_capstyle: Any = ...,
           solid_capstyle: Any = ...,
           dash_joinstyle: Any = ...,
           solid_joinstyle: Any = ...,
           pickradius: float = ...,
           drawstyle: Any = ...,
           markevery: Any = ...,
           **kwargs) -> Any: ...


@_copy_docstring_and_deprecators
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