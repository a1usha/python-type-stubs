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


def install_repl_displayhook() -> None: ...


def uninstall_repl_displayhook() -> Any: ...


@functools.wraps(matplotlib.set_loglevel)
def set_loglevel(*args,
                 **kwargs) -> None: ...


@_copy_docstring_and_deprecators(Artist.findobj)
def findobj(o: Optional[{findobj}] = None,
            match: Any = None,
            include_self: bool = True) -> Any: """
        Find artist objects.

        Recursively find all `.Artist` instances contained in the artist.

        Parameters
        ----------
        match
            A filter criterion for the matches. This can be

            - *None*: Return all objects contained in artist.
            - A function with signature ``def match(artist: Artist) -> bool``.
              The result will only contain artists for which the function
              returns *True*.
            - A class instance: e.g., `.Line2D`. The result will only contain
              artists of this class or its subclasses (``isinstance`` check).

        include_self : bool
            Include *self* in the list to be checked for a match.

        Returns
        -------
        list of `.Artist`

        """
    ...


def _get_required_interactive_framework(backend_mod: Type[backend_mod]) -> Optional[Any]: ...


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
    def __init__(self: _IoffContext) -> None: ...

    def __enter__(self: _IoffContext) -> None: ...

    def __exit__(self: _IoffContext,
                 exc_type: Any,
                 exc_value: Any,
                 traceback: Any) -> None: ...


class _IonContext(object):
    def __init__(self: _IonContext) -> None: ...

    def __enter__(self: _IonContext) -> None: ...

    def __exit__(self: _IonContext,
                 exc_type: Any,
                 exc_value: Any,
                 traceback: Any) -> None: ...


def ioff() -> _IoffContext: ...


def ion() -> _IonContext: ...


def pause(interval: Any) -> None: ...


@_copy_docstring_and_deprecators(matplotlib.rc)
def rc(group: str,
       **kwargs) -> Optional[Any]: """
    Set the current `.rcParams`.  *group* is the grouping for the rc, e.g.,
    for ``lines.linewidth`` the group is ``lines``, for
    ``axes.facecolor``, the group is ``axes``, and so on.  Group may
    also be a list or tuple of group names, e.g., (*xtick*, *ytick*).
    *kwargs* is a dictionary attribute name/value pairs, e.g.,::

      rc('lines', linewidth=2, color='r')

    sets the current `.rcParams` and is equivalent to::

      rcParams['lines.linewidth'] = 2
      rcParams['lines.color'] = 'r'

    The following aliases are available to save typing for interactive users:

    =====   =================
    Alias   Property
    =====   =================
    'lw'    'linewidth'
    'ls'    'linestyle'
    'c'     'color'
    'fc'    'facecolor'
    'ec'    'edgecolor'
    'mew'   'markeredgewidth'
    'aa'    'antialiased'
    =====   =================

    Thus you could abbreviate the above call as::

          rc('lines', lw=2, c='r')

    Note you can use python's kwargs dictionary facility to store
    dictionaries of default parameters.  e.g., you can customize the
    font rc as follows::

      font = {'family' : 'monospace',
              'weight' : 'bold',
              'size'   : 'larger'}
      rc('font', **font)  # pass in the font dict as kwargs

    This enables you to easily switch between several configurations.  Use
    ``matplotlib.style.use('default')`` or :func:`~matplotlib.rcdefaults` to
    restore the default `.rcParams` after changes.

    Notes
    -----
    Similar functionality is available by using the normal dict interface, i.e.
    ``rcParams.update({"lines.linewidth": 2, ...})`` (but ``rcParams.update``
    does not support abbreviations or grouping).
    """
    ...


@_copy_docstring_and_deprecators(matplotlib.rc_context)
def rc_context(rc: dict[str, str] = None,
               fname: Any = None) -> Generator[Any, Any, None]: """
    Return a context manager for temporarily changing rcParams.

    Parameters
    ----------
    rc : dict
        The rcParams to temporarily set.
    fname : str or path-like
        A file with Matplotlib rc settings. If both *fname* and *rc* are given,
        settings from *rc* take precedence.

    See Also
    --------
    :ref:`customizing-with-matplotlibrc-files`

    Examples
    --------
    Passing explicit values via a dict::

        with mpl.rc_context({'interactive': False}):
            fig, ax = plt.subplots()
            ax.plot(range(3), range(3))
            fig.savefig('example.png')
            plt.close(fig)

    Loading settings from a file::

         with mpl.rc_context(fname='print.rc'):
             plt.plot(x, y)  # uses 'print.rc'

    """
    ...


@_copy_docstring_and_deprecators(matplotlib.rcdefaults)
def rcdefaults() -> Optional[Any]: """
    Restore the `.rcParams` from Matplotlib's internal default style.

    Style-blacklisted `.rcParams` (defined in
    `matplotlib.style.core.STYLE_BLACKLIST`) are not updated.

    See Also
    --------
    matplotlib.rc_file_defaults
        Restore the `.rcParams` from the rc file originally loaded by
        Matplotlib.
    matplotlib.style.use
        Use a specific style file.  Call ``style.use('default')`` to restore
        the default style.
    """
    ...


@_copy_docstring_and_deprecators(matplotlib.artist.getp)
def getp(*args,
         obj: Any,
         **kwargs) -> Optional[Any]: """
    Return the value of an `.Artist`'s *property*, or print all of them.

    Parameters
    ----------
    obj : `.Artist`
        The queried artist; e.g., a `.Line2D`, a `.Text`, or an `~.axes.Axes`.

    property : str or None, default: None
        If *property* is 'somename', this function returns
        ``obj.get_somename()``.

        If is is None (or unset), it *prints* all gettable properties from
        *obj*.  Many properties have aliases for shorter typing, e.g. 'lw' is
        an alias for 'linewidth'.  In the output, aliases and full property
        names will be listed as:

          property or alias = value

        e.g.:

          linewidth or lw = 2

    See Also
    --------
    setp
    """
    ...


@_copy_docstring_and_deprecators(matplotlib.artist.get)
def get(*args,
        obj: Any,
        **kwargs) -> Optional[Any]: ...


@_copy_docstring_and_deprecators(matplotlib.artist.setp)
def setp(*args,
         obj: Any,
         **kwargs) -> Optional[list[Optional[Any]]]: """
    Set one or more properties on an `.Artist`, or list allowed values.

    Parameters
    ----------
    obj : `.Artist` or list of `.Artist`
        The artist(s) whose properties are being set or queried.  When setting
        properties, all artists are affected; when querying the allowed values,
        only the first instance in the sequence is queried.

        For example, two lines can be made thicker and red with a single call:

        >>> x = arange(0, 1, 0.01)
        >>> lines = plot(x, sin(2*pi*x), x, sin(4*pi*x))
        >>> setp(lines, linewidth=2, color='r')

    file : file-like, default: `sys.stdout`
        Where `setp` writes its output when asked to list allowed values.

        >>> with open('output.log') as file:
        ...     setp(line, file=file)

        The default, ``None``, means `sys.stdout`.

    *args, **kwargs
        The properties to set.  The following combinations are supported:

        - Set the linestyle of a line to be dashed:

          >>> line, = plot([1, 2, 3])
          >>> setp(line, linestyle='--')

        - Set multiple properties at once:

          >>> setp(line, linewidth=2, color='r')

        - List allowed values for a line's linestyle:

          >>> setp(line, 'linestyle')
          linestyle: {'-', '--', '-.', ':', '', (offset, on-off-seq), ...}

        - List all properties that can be set, and their allowed values:

          >>> setp(line)
          agg_filter: a filter function, ...
          [long output listing omitted]

        `setp` also supports MATLAB style string/value pairs.  For example, the
        following are equivalent:

        >>> setp(lines, 'linewidth', 2, 'color', 'r')  # MATLAB style
        >>> setp(lines, linewidth=2, color='r')        # Python style

    See Also
    --------
    getp
    """
    ...


def xkcd(scale: Optional[float] = 1,
         length: Optional[float] = 100,
         randomness: Optional[float] = 2) -> _xkcd: ...


class _xkcd(object):
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


def get_fignums() -> list[SupportsLessThan]: ...


def get_figlabels() -> list: ...


def get_current_fig_manager() -> Any: ...


@_copy_docstring_and_deprecators(FigureCanvasBase.mpl_connect)
def connect(s: Any,
            func: Any) -> Any: """
        Bind function *func* to event *s*.

        Parameters
        ----------
        s : str
            One of the following events ids:

            - 'button_press_event'
            - 'button_release_event'
            - 'draw_event'
            - 'key_press_event'
            - 'key_release_event'
            - 'motion_notify_event'
            - 'pick_event'
            - 'resize_event'
            - 'scroll_event'
            - 'figure_enter_event',
            - 'figure_leave_event',
            - 'axes_enter_event',
            - 'axes_leave_event'
            - 'close_event'.

        func : callable
            The callback function to be executed, which must have the
            signature::

                def func(event: Event) -> Any

            For the location events (button and key press/release), if the
            mouse is over the axes, the ``inaxes`` attribute of the event will
            be set to the `~matplotlib.axes.Axes` the event occurs is over, and
            additionally, the variables ``xdata`` and ``ydata`` attributes will
            be set to the mouse location in data coordinates.  See `.KeyEvent`
            and `.MouseEvent` for more info.

        Returns
        -------
        cid
            A connection id that can be used with
            `.FigureCanvasBase.mpl_disconnect`.

        Examples
        --------
        ::

            def on_press(event):
                print('you pressed', event.button, event.xdata, event.ydata)

            cid = canvas.mpl_connect('button_press_event', on_press)
        """
    ...


@_copy_docstring_and_deprecators(FigureCanvasBase.mpl_disconnect)
def disconnect(cid: Any) -> Any: """
        Disconnect the callback with id *cid*.

        Examples
        --------
        ::

            cid = canvas.mpl_connect('button_press_event', on_press)
            # ... later
            canvas.mpl_disconnect(cid)
        """
    ...


def close(fig: Any = None) -> None: ...


def clf() -> None: ...


def draw() -> None: ...


@_copy_docstring_and_deprecators(Figure.savefig)
def savefig(*args,
            **kwargs) -> Any: """
        Save the current figure.

        Call signature::

          savefig(fname, dpi=None, facecolor='w', edgecolor='w',
                  orientation='portrait', papertype=None, format=None,
                  transparent=False, bbox_inches=None, pad_inches=0.1,
                  frameon=None, metadata=None)

        The available output formats depend on the backend being used.

        Parameters
        ----------
        fname : str or path-like or binary file-like
            A path, or a Python file-like object, or
            possibly some backend-dependent object such as
            `matplotlib.backends.backend_pdf.PdfPages`.

            If *format* is set, it determines the output format, and the file
            is saved as *fname*.  Note that *fname* is used verbatim, and there
            is no attempt to make the extension, if any, of *fname* match
            *format*, and no extension is appended.

            If *format* is not set, then the format is inferred from the
            extension of *fname*, if there is one.  If *format* is not
            set and *fname* has no extension, then the file is saved with
            :rc:`savefig.format` and the appropriate extension is appended to
            *fname*.

        Other Parameters
        ----------------
        dpi : float or 'figure', default: :rc:`savefig.dpi`
            The resolution in dots per inch.  If 'figure', use the figure's
            dpi value.

        quality : int, default: :rc:`savefig.jpeg_quality`
            Applicable only if *format* is 'jpg' or 'jpeg', ignored otherwise.

            The image quality, on a scale from 1 (worst) to 95 (best).
            Values above 95 should be avoided; 100 disables portions of
            the JPEG compression algorithm, and results in large files
            with hardly any gain in image quality.

            This parameter is deprecated.

        optimize : bool, default: False
            Applicable only if *format* is 'jpg' or 'jpeg', ignored otherwise.

            Whether the encoder should make an extra pass over the image
            in order to select optimal encoder settings.

            This parameter is deprecated.

        progressive : bool, default: False
            Applicable only if *format* is 'jpg' or 'jpeg', ignored otherwise.

            Whether the image should be stored as a progressive JPEG file.

            This parameter is deprecated.

        facecolor : color or 'auto', default: :rc:`savefig.facecolor`
            The facecolor of the figure.  If 'auto', use the current figure
            facecolor.

        edgecolor : color or 'auto', default: :rc:`savefig.edgecolor`
            The edgecolor of the figure.  If 'auto', use the current figure
            edgecolor.

        orientation : {'landscape', 'portrait'}
            Currently only supported by the postscript backend.

        papertype : str
            One of 'letter', 'legal', 'executive', 'ledger', 'a0' through
            'a10', 'b0' through 'b10'. Only supported for postscript
            output.

        format : str
            The file format, e.g. 'png', 'pdf', 'svg', ... The behavior when
            this is unset is documented under *fname*.

        transparent : bool
            If *True*, the Axes patches will all be transparent; the
            figure patch will also be transparent unless facecolor
            and/or edgecolor are specified via kwargs.
            This is useful, for example, for displaying
            a plot on top of a colored background on a web page.  The
            transparency of these patches will be restored to their
            original values upon exit of this function.

        bbox_inches : str or `.Bbox`, default: :rc:`savefig.bbox`
            Bounding box in inches: only the given portion of the figure is
            saved.  If 'tight', try to figure out the tight bbox of the figure.

        pad_inches : float, default: :rc:`savefig.pad_inches`
            Amount of padding around the figure when bbox_inches is 'tight'.

        bbox_extra_artists : list of `~matplotlib.artist.Artist`, optional
            A list of extra artists that will be considered when the
            tight bbox is calculated.

        backend : str, optional
            Use a non-default backend to render the file, e.g. to render a
            png file with the "cairo" backend rather than the default "agg",
            or a pdf file with the "pgf" backend rather than the default
            "pdf".  Note that the default backend is normally sufficient.  See
            :ref:`the-builtin-backends` for a list of valid backends for each
            file format.  Custom backends can be referenced as "module://...".

        metadata : dict, optional
            Key/value pairs to store in the image metadata. The supported keys
            and defaults depend on the image format and backend:

            - 'png' with Agg backend: See the parameter ``metadata`` of
              `~.FigureCanvasAgg.print_png`.
            - 'pdf' with pdf backend: See the parameter ``metadata`` of
              `~.backend_pdf.PdfPages`.
            - 'svg' with svg backend: See the parameter ``metadata`` of
              `~.FigureCanvasSVG.print_svg`.
            - 'eps' and 'ps' with PS backend: Only 'Creator' is supported.

        pil_kwargs : dict, optional
            Additional keyword arguments that are passed to
            `PIL.Image.Image.save` when saving the figure.
        """
    ...


def figlegend(*args,
              **kwargs) -> Any: ...


@docstring.dedent_interpd
def axes(arg: Any = None,
         **kwargs) -> Any: ...


def delaxes(ax: Optional[{remove}] = None) -> None: ...


def sca(ax: {figure}) -> None: ...


def cla() -> Any: ...


@docstring.dedent_interpd
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


def xticks(ticks: Union[ndarray, Iterable, int, float, None] = None,
           labels: Union[ndarray, Iterable, int, float, None] = None,
           **kwargs) -> Any: ...


def yticks(ticks: Union[ndarray, Iterable, int, float, None] = None,
           labels: Union[ndarray, Iterable, int, float, None] = None,
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


def plotting() -> None: ...


def get_plot_commands() -> list[str]: ...


def colormaps() -> list[str]: ...


def _setup_pyplot_info_docstrings() -> None: ...


@_copy_docstring_and_deprecators(Figure.colorbar)
def colorbar(mappable: Any = None,
             cax: Any = None,
             ax: Any = None,
             **kwargs) -> Any: ...


def clim(vmin: Any = None,
         vmax: Any = None) -> Any: ...


def set_cmap(cmap: Any) -> None: ...


@_copy_docstring_and_deprecators(matplotlib.image.imread)
def imread(fname: Any,
           format: Any = None) -> Any: """
    Read an image from a file into an array.

    Parameters
    ----------
    fname : str or file-like
        The image file to read: a filename, a URL or a file-like object opened
        in read-binary mode.

        Passing a URL is deprecated.  Please open the URL
        for reading and pass the result to Pillow, e.g. with
        ``PIL.Image.open(urllib.request.urlopen(url))``.
    format : str, optional
        The image file format assumed for reading the data. If not
        given, the format is deduced from the filename.  If nothing can
        be deduced, PNG is tried.

    Returns
    -------
    `numpy.array`
        The image data. The returned array has shape

        - (M, N) for grayscale images.
        - (M, N, 3) for RGB images.
        - (M, N, 4) for RGBA images.
    """
    ...


@_copy_docstring_and_deprecators(matplotlib.image.imsave)
def imsave(fname: Any,
           arr: Any,
           **kwargs) -> Any: """
    Save an array as an image file.

    Parameters
    ----------
    fname : str or path-like or file-like
        A path or a file-like object to store the image in.
        If *format* is not set, then the output format is inferred from the
        extension of *fname*, if any, and from :rc:`savefig.format` otherwise.
        If *format* is set, it determines the output format.
    arr : array-like
        The image data. The shape can be one of
        MxN (luminance), MxNx3 (RGB) or MxNx4 (RGBA).
    vmin, vmax : float, optional
        *vmin* and *vmax* set the color scaling for the image by fixing the
        values that map to the colormap color limits. If either *vmin*
        or *vmax* is None, that limit is determined from the *arr*
        min/max value.
    cmap : str or `~matplotlib.colors.Colormap`, default: :rc:`image.cmap`
        A Colormap instance or registered colormap name. The colormap
        maps scalar data to colors. It is ignored for RGB(A) data.
    format : str, optional
        The file format, e.g. 'png', 'pdf', 'svg', ...  The behavior when this
        is unset is documented under *fname*.
    origin : {'upper', 'lower'}, default: :rc:`image.origin`
        Indicates whether the ``(0, 0)`` index of the array is in the upper
        left or lower left corner of the axes.
    dpi : float
        The DPI to store in the metadata of the file.  This does not affect the
        resolution of the output image.  Depending on file format, this may be
        rounded to the nearest integer.
    metadata : dict, optional
        Metadata in the image file.  The supported keys depend on the output
        format, see the documentation of the respective backends for more
        information.
    pil_kwargs : dict, optional
        Keyword arguments passed to `PIL.Image.Image.save`.  If the 'pnginfo'
        key is present, it completely overrides *metadata*, including the
        default 'Software' key.
    """
    ...


def matshow(A: int,
            fignum: Optional[int] = None,
            **kwargs) -> Any: ...


def polar(*args,
          **kwargs) -> PolarAxes: ...


@_copy_docstring_and_deprecators(Figure.figimage)
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
             **kwargs) -> Any: """
        Add a non-resampled image to the figure.

        The image is attached to the lower or upper left corner depending on
        *origin*.

        Parameters
        ----------
        X
            The image data. This is an array of one of the following shapes:

            - MxN: luminance (grayscale) values
            - MxNx3: RGB values
            - MxNx4: RGBA values

        xo, yo : int
            The *x*/*y* image offset in pixels.

        alpha : None or float
            The alpha blending value.

        norm : `matplotlib.colors.Normalize`
            A `.Normalize` instance to map the luminance to the
            interval [0, 1].

        cmap : str or `matplotlib.colors.Colormap`, default: :rc:`image.cmap`
            The colormap to use.

        vmin, vmax : float
            If *norm* is not given, these values set the data limits for the
            colormap.

        origin : {'upper', 'lower'}, default: :rc:`image.origin`
            Indicates where the [0, 0] index of the array is in the upper left
            or lower left corner of the axes.

        resize : bool
            If *True*, resize the figure to match the given image size.

        Returns
        -------
        `matplotlib.image.FigureImage`

        Other Parameters
        ----------------
        **kwargs
            Additional kwargs are `.Artist` kwargs passed on to `.FigureImage`.

        Notes
        -----
        figimage complements the Axes image (`~matplotlib.axes.Axes.imshow`)
        which will be resampled to fit the current Axes.  If you want
        a resampled image to fill the entire figure, you can define an
        `~matplotlib.axes.Axes` with extent [0, 0, 1, 1].

        Examples
        --------
        ::

            f = plt.figure()
            nx = int(f.get_figwidth() * f.dpi)
            ny = int(f.get_figheight() * f.dpi)
            data = np.random.random((ny, nx))
            f.figimage(data)
            plt.show()
        """
    ...


@_copy_docstring_and_deprecators(Figure.text)
def figtext(x: Any,
            y: Any,
            s: Any,
            fontdict: Any = None,
            **kwargs) -> Any: ...


@_copy_docstring_and_deprecators(Figure.gca)
def gca(**kwargs) -> Any: ...


@_copy_docstring_and_deprecators(Figure._gci)
def gci() -> Any: ...


@_copy_docstring_and_deprecators(Figure.ginput)
def ginput(n: int = 1,
           timeout: int = 30,
           show_clicks: bool = True,
           mouse_add: MouseButton = MouseButton.LEFT,
           mouse_pop: MouseButton = MouseButton.RIGHT,
           mouse_stop: MouseButton = MouseButton.MIDDLE) -> Any: """
        Blocking call to interact with a figure.

        Wait until the user clicks *n* times on the figure, and return the
        coordinates of each click in a list.

        There are three possible interactions:

        - Add a point.
        - Remove the most recently added point.
        - Stop the interaction and return the points added so far.

        The actions are assigned to mouse buttons via the arguments
        *mouse_add*, *mouse_pop* and *mouse_stop*.

        Parameters
        ----------
        n : int, default: 1
            Number of mouse clicks to accumulate. If negative, accumulate
            clicks until the input is terminated manually.
        timeout : float, default: 30 seconds
            Number of seconds to wait before timing out. If zero or negative
            will never timeout.
        show_clicks : bool, default: True
            If True, show a red cross at the location of each click.
        mouse_add : `.MouseButton` or None, default: `.MouseButton.LEFT`
            Mouse button used to add points.
        mouse_pop : `.MouseButton` or None, default: `.MouseButton.RIGHT`
            Mouse button used to remove the most recently added point.
        mouse_stop : `.MouseButton` or None, default: `.MouseButton.MIDDLE`
            Mouse button used to stop input.

        Returns
        -------
        list of tuples
            A list of the clicked (x, y) coordinates.

        Notes
        -----
        The keyboard can also be used to select points in case your mouse
        does not have one or more of the buttons.  The delete and backspace
        keys act like right clicking (i.e., remove last point), the enter key
        terminates input and any other key (not already used by the window
        manager) selects a point.
        """
    ...


@_copy_docstring_and_deprecators(Figure.subplots_adjust)
def subplots_adjust(left: Any = None,
                    bottom: Any = None,
                    right: Any = None,
                    top: Any = None,
                    wspace: Any = None,
                    hspace: Any = None) -> Any: ...


@_copy_docstring_and_deprecators(Figure.suptitle)
def suptitle(t: Any,
             **kwargs) -> Any: ...


@_copy_docstring_and_deprecators(Figure.waitforbuttonpress)
def waitforbuttonpress(timeout: int = -1) -> Any: """
        Blocking call to interact with the figure.

        Wait for user input and return True if a key was pressed, False if a
        mouse button was pressed and None if no input was given within
        *timeout* seconds.  Negative values deactivate *timeout*.
        """
    ...


@_copy_docstring_and_deprecators(Axes.acorr)
def acorr(x: Any,
          *,
          data: Any = None,
          **kwargs) -> Any: """
        Plot the autocorrelation of *x*.

        Parameters
        ----------
        x : array-like

        detrend : callable, default: `.mlab.detrend_none` (no detrending)
            A detrending function applied to *x*.  It must have the
            signature ::

                detrend(x: np.ndarray) -> np.ndarray

        normed : bool, default: True
            If ``True``, input vectors are normalised to unit length.

        usevlines : bool, default: True
            Determines the plot style.

            If ``True``, vertical lines are plotted from 0 to the acorr value
            using `.Axes.vlines`. Additionally, a horizontal line is plotted
            at y=0 using `.Axes.axhline`.

            If ``False``, markers are plotted at the acorr values using
            `.Axes.plot`.

        maxlags : int, default: 10
            Number of lags to show. If ``None``, will return all
            ``2 * len(x) - 1`` lags.

        Returns
        -------
        lags : array (length ``2*maxlags+1``)
            The lag vector.
        c : array  (length ``2*maxlags+1``)
            The auto correlation vector.
        line : `.LineCollection` or `.Line2D`
            `.Artist` added to the Axes of the correlation:

            - `.LineCollection` if *usevlines* is True.
            - `.Line2D` if *usevlines* is False.
        b : `.Line2D` or None
            Horizontal line at 0 if *usevlines* is True
            None *usevlines* is False.

        Other Parameters
        ----------------
        linestyle : `.Line2D` property, optional
            The linestyle for plotting the data points.
            Only used if *usevlines* is ``False``.

        marker : str, default: 'o'
            The marker for plotting the data points.
            Only used if *usevlines* is ``False``.

        **kwargs
            Additional parameters are passed to `.Axes.vlines` and
            `.Axes.axhline` if *usevlines* is ``True``; otherwise they are
            passed to `.Axes.plot`.

        Notes
        -----
        The cross correlation is performed with `numpy.correlate` with
        ``mode = "full"``.
        """
    ...


@_copy_docstring_and_deprecators(Axes.angle_spectrum)
def angle_spectrum(x: Any,
                   Fs: Any = None,
                   Fc: Any = None,
                   window: Any = None,
                   pad_to: Any = None,
                   sides: Any = None,
                   *,
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
                   **kwargs) -> Any: """
        Plot the angle spectrum.

        Compute the angle spectrum (wrapped phase spectrum) of *x*.
        Data is padded to a length of *pad_to* and the windowing function
        *window* is applied to the signal.

        Parameters
        ----------
        x : 1-D array or sequence
            Array or sequence containing the data.

        %(Spectral)s

        %(Single_Spectrum)s

        Fc : int, default: 0
            The center frequency of *x*, which offsets the x extents of the
            plot to reflect the frequency range used when a signal is acquired
            and then filtered and downsampled to baseband.

        Returns
        -------
        spectrum : 1-D array
            The values for the angle spectrum in radians (real valued).

        freqs : 1-D array
            The frequencies corresponding to the elements in *spectrum*.

        line : `~matplotlib.lines.Line2D`
            The line created by this function.

        Other Parameters
        ----------------
        **kwargs
            Keyword arguments control the `.Line2D` properties:

            %(Line2D_kwdoc)s

        See Also
        --------
        magnitude_spectrum
            Plots the magnitudes of the corresponding frequencies.
        phase_spectrum
            Plots the unwrapped version of this function.
        specgram
            Can plot the angle spectrum of segments within the signal in a
            colormap.
        """
    ...


@_copy_docstring_and_deprecators(Axes.annotate)
def annotate(*args,
             text: Any,
             xy: Any,
             **kwargs) -> Any: ...


@_copy_docstring_and_deprecators(Axes.arrow)
def arrow(x: Any,
          y: Any,
          dx: Any,
          dy: Any,
          **kwargs) -> Any: """
        Add an arrow to the Axes.

        This draws an arrow from ``(x, y)`` to ``(x+dx, y+dy)``.

        Parameters
        ----------
        x, y : float
            The x and y coordinates of the arrow base.

        dx, dy : float
            The length of the arrow along x and y direction.

        %(FancyArrow)s

        Returns
        -------
        `.FancyArrow`
            The created `.FancyArrow` object.

        Notes
        -----
        The resulting arrow is affected by the Axes aspect ratio and limits.
        This may produce an arrow whose head is not square with its stem. To
        create an arrow whose head is square with its stem,
        use :meth:`annotate` for example:

        >>> ax.annotate("", xy=(0.5, 0.5), xytext=(0, 0),
        ...             arrowprops=dict(arrowstyle="->"))

        """
    ...


@_copy_docstring_and_deprecators(Axes.autoscale)
def autoscale(enable: bool = True,
              axis: str = 'both',
              tight: Any = None) -> Any: ...


@_copy_docstring_and_deprecators(Axes.axhline)
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
            **kwargs) -> Any: """
        Add a horizontal line across the axis.

        Parameters
        ----------
        y : float, default: 0
            y position in data coordinates of the horizontal line.

        xmin : float, default: 0
            Should be between 0 and 1, 0 being the far left of the plot, 1 the
            far right of the plot.

        xmax : float, default: 1
            Should be between 0 and 1, 0 being the far left of the plot, 1 the
            far right of the plot.

        Returns
        -------
        `~matplotlib.lines.Line2D`

        Other Parameters
        ----------------
        **kwargs
            Valid keyword arguments are `.Line2D` properties, with the
            exception of 'transform':

            %(Line2D_kwdoc)s

        See Also
        --------
        hlines : Add horizontal lines in data coordinates.
        axhspan : Add a horizontal span (rectangle) across the axis.
        axline : Add a line with an arbitrary slope.

        Examples
        --------
        * draw a thick red hline at 'y' = 0 that spans the xrange::

            >>> axhline(linewidth=4, color='r')

        * draw a default hline at 'y' = 1 that spans the xrange::

            >>> axhline(y=1)

        * draw a default hline at 'y' = .5 that spans the middle half of
          the xrange::

            >>> axhline(y=.5, xmin=0.25, xmax=0.75)
        """
    ...


@_copy_docstring_and_deprecators(Axes.axhspan)
def axhspan(ymin: Any,
            ymax: Any,
            xmin: int = 0,
            xmax: int = 1,
            xy: Any = ...,
            closed: bool = ...,
            **kwargs) -> Any: """
        Add a horizontal span (rectangle) across the Axes.

        The rectangle spans from *ymin* to *ymax* vertically, and, by default,
        the whole x-axis horizontally.  The x-span can be set using *xmin*
        (default: 0) and *xmax* (default: 1) which are in axis units; e.g.
        ``xmin = 0.5`` always refers to the middle of the x-axis regardless of
        the limits set by `~.Axes.set_xlim`.

        Parameters
        ----------
        ymin : float
            Lower y-coordinate of the span, in data units.
        ymax : float
            Upper y-coordinate of the span, in data units.
        xmin : float, default: 0
            Lower x-coordinate of the span, in x-axis (0-1) units.
        xmax : float, default: 1
            Upper x-coordinate of the span, in x-axis (0-1) units.

        Returns
        -------
        `~matplotlib.patches.Polygon`
            Horizontal span (rectangle) from (xmin, ymin) to (xmax, ymax).

        Other Parameters
        ----------------
        **kwargs : `~matplotlib.patches.Polygon` properties

        %(Polygon_kwdoc)s

        See Also
        --------
        axvspan : Add a vertical span across the Axes.
        """
    ...


@_copy_docstring_and_deprecators(Axes.axis)
def axis(*args,
         emit: bool = True,
         **kwargs) -> Any: ...


@_copy_docstring_and_deprecators(Axes.axline)
def axline(xy1: Any,
           xy2: Any = None,
           *,
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
           **kwargs) -> Any: """
        Add an infinitely long straight line.

        The line can be defined either by two points *xy1* and *xy2*, or
        by one point *xy1* and a *slope*.

        This draws a straight line "on the screen", regardless of the x and y
        scales, and is thus also suitable for drawing exponential decays in
        semilog plots, power laws in loglog plots, etc. However, *slope*
        should only be used with linear scales; It has no clear meaning for
        all other scales, and thus the behavior is undefined. Please specify
        the line using the points *xy1*, *xy2* for non-linear scales.

        The *transform* keyword argument only applies to the points *xy1*,
        *xy2*. The *slope* (if given) is always in data coordinates. This can
        be used e.g. with ``ax.transAxes`` for drawing grid lines with a fixed
        slope.

        Parameters
        ----------
        xy1, xy2 : (float, float)
            Points for the line to pass through.
            Either *xy2* or *slope* has to be given.
        slope : float, optional
            The slope of the line. Either *xy2* or *slope* has to be given.

        Returns
        -------
        `.Line2D`

        Other Parameters
        ----------------
        **kwargs
            Valid kwargs are `.Line2D` properties

            %(Line2D_kwdoc)s

        See Also
        --------
        axhline : for horizontal lines
        axvline : for vertical lines

        Examples
        --------
        Draw a thick red line passing through (0, 0) and (1, 1)::

            >>> axline((0, 0), (1, 1), linewidth=4, color='r')
        """
    ...


@_copy_docstring_and_deprecators(Axes.axvline)
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
            **kwargs) -> Any: """
        Add a vertical line across the Axes.

        Parameters
        ----------
        x : float, default: 0
            x position in data coordinates of the vertical line.

        ymin : float, default: 0
            Should be between 0 and 1, 0 being the bottom of the plot, 1 the
            top of the plot.

        ymax : float, default: 1
            Should be between 0 and 1, 0 being the bottom of the plot, 1 the
            top of the plot.

        Returns
        -------
        `~matplotlib.lines.Line2D`

        Other Parameters
        ----------------
        **kwargs
            Valid keyword arguments are `.Line2D` properties, with the
            exception of 'transform':

            %(Line2D_kwdoc)s

        See Also
        --------
        vlines : Add vertical lines in data coordinates.
        axvspan : Add a vertical span (rectangle) across the axis.
        axline : Add a line with an arbitrary slope.

        Examples
        --------
        * draw a thick red vline at *x* = 0 that spans the yrange::

            >>> axvline(linewidth=4, color='r')

        * draw a default vline at *x* = 1 that spans the yrange::

            >>> axvline(x=1)

        * draw a default vline at *x* = .5 that spans the middle half of
          the yrange::

            >>> axvline(x=.5, ymin=0.25, ymax=0.75)
        """
    ...


@_copy_docstring_and_deprecators(Axes.axvspan)
def axvspan(xmin: Any,
            xmax: Any,
            ymin: int = 0,
            ymax: int = 1,
            xy: Any = ...,
            closed: bool = ...,
            **kwargs) -> Any: """
        Add a vertical span (rectangle) across the Axes.

        The rectangle spans from *xmin* to *xmax* horizontally, and, by
        default, the whole y-axis vertically.  The y-span can be set using
        *ymin* (default: 0) and *ymax* (default: 1) which are in axis units;
        e.g. ``ymin = 0.5`` always refers to the middle of the y-axis
        regardless of the limits set by `~.Axes.set_ylim`.

        Parameters
        ----------
        xmin : float
            Lower x-coordinate of the span, in data units.
        xmax : float
            Upper x-coordinate of the span, in data units.
        ymin : float, default: 0
            Lower y-coordinate of the span, in y-axis units (0-1).
        ymax : float, default: 1
            Upper y-coordinate of the span, in y-axis units (0-1).

        Returns
        -------
        `~matplotlib.patches.Polygon`
            Vertical span (rectangle) from (xmin, ymin) to (xmax, ymax).

        Other Parameters
        ----------------
        **kwargs : `~matplotlib.patches.Polygon` properties

        %(Polygon_kwdoc)s

        See Also
        --------
        axhspan : Add a horizontal span across the Axes.

        Examples
        --------
        Draw a vertical, green, translucent rectangle from x = 1.25 to
        x = 1.55 that spans the yrange of the Axes.

        >>> axvspan(1.25, 1.55, facecolor='g', alpha=0.5)

        """
    ...


@_copy_docstring_and_deprecators(Axes.bar)
def bar(x: Any,
        height: Any,
        width: float = 0.8,
        bottom: Any = None,
        *,
        align: str = 'center',
        data: Any = None,
        xy: tuple[float, float] = ...,
        width: float = ...,
        height: float = ...,
        angle: Any = ...,
        **kwargs) -> Any: r"""
        Make a bar plot.

        The bars are positioned at *x* with the given *align*\ment. Their
        dimensions are given by *height* and *width*. The vertical baseline
        is *bottom* (default 0).

        Many parameters can take either a single value applying to all bars
        or a sequence of values, one for each bar.

        Parameters
        ----------
        x : float or array-like
            The x coordinates of the bars. See also *align* for the
            alignment of the bars to the coordinates.

        height : float or array-like
            The height(s) of the bars.

        width : float or array-like, default: 0.8
            The width(s) of the bars.

        bottom : float or array-like, default: 0
            The y coordinate(s) of the bars bases.

        align : {'center', 'edge'}, default: 'center'
            Alignment of the bars to the *x* coordinates:

            - 'center': Center the base on the *x* positions.
            - 'edge': Align the left edges of the bars with the *x* positions.

            To align the bars on the right edge pass a negative *width* and
            ``align='edge'``.

        Returns
        -------
        `.BarContainer`
            Container with all the bars and optionally errorbars.

        Other Parameters
        ----------------
        color : color or list of color, optional
            The colors of the bar faces.

        edgecolor : color or list of color, optional
            The colors of the bar edges.

        linewidth : float or array-like, optional
            Width of the bar edge(s). If 0, don't draw edges.

        tick_label : str or list of str, optional
            The tick labels of the bars.
            Default: None (Use default numeric labels.)

        xerr, yerr : float or array-like of shape(N,) or shape(2, N), optional
            If not *None*, add horizontal / vertical errorbars to the bar tips.
            The values are +/- sizes relative to the data:

            - scalar: symmetric +/- values for all bars
            - shape(N,): symmetric +/- values for each bar
            - shape(2, N): Separate - and + values for each bar. First row
              contains the lower errors, the second row contains the upper
              errors.
            - *None*: No errorbar. (Default)

            See :doc:`/gallery/statistics/errorbar_features`
            for an example on the usage of ``xerr`` and ``yerr``.

        ecolor : color or list of color, default: 'black'
            The line color of the errorbars.

        capsize : float, default: :rc:`errorbar.capsize`
           The length of the error bar caps in points.

        error_kw : dict, optional
            Dictionary of kwargs to be passed to the `~.Axes.errorbar`
            method. Values of *ecolor* or *capsize* defined here take
            precedence over the independent kwargs.

        log : bool, default: False
            If *True*, set the y-axis to be log scale.

        **kwargs : `.Rectangle` properties

        %(Rectangle_kwdoc)s

        See Also
        --------
        barh : Plot a horizontal bar plot.

        Notes
        -----
        Stacked bars can be achieved by passing individual *bottom* values per
        bar. See :doc:`/gallery/lines_bars_and_markers/bar_stacked`.
        """
    ...


@_copy_docstring_and_deprecators(Axes.barbs)
def barbs(*args,
          data: Any = None,
          **kwargs) -> Any: """
        %(barbs_doc)s
        """
    ...


@_copy_docstring_and_deprecators(Axes.barh)
def barh(y: Any,
         width: Any,
         height: float = 0.8,
         left: Any = None,
         *,
         align: str = 'center',
         xy: tuple[float, float] = ...,
         width: float = ...,
         height: float = ...,
         angle: Any = ...,
         **kwargs) -> Any: r"""
        Make a horizontal bar plot.

        The bars are positioned at *y* with the given *align*\ment. Their
        dimensions are given by *width* and *height*. The horizontal baseline
        is *left* (default 0).

        Many parameters can take either a single value applying to all bars
        or a sequence of values, one for each bar.

        Parameters
        ----------
        y : float or array-like
            The y coordinates of the bars. See also *align* for the
            alignment of the bars to the coordinates.

        width : float or array-like
            The width(s) of the bars.

        height : float or array-like, default: 0.8
            The heights of the bars.

        left : float or array-like, default: 0
            The x coordinates of the left sides of the bars.

        align : {'center', 'edge'}, default: 'center'
            Alignment of the base to the *y* coordinates*:

            - 'center': Center the bars on the *y* positions.
            - 'edge': Align the bottom edges of the bars with the *y*
              positions.

            To align the bars on the top edge pass a negative *height* and
            ``align='edge'``.

        Returns
        -------
        `.BarContainer`
            Container with all the bars and optionally errorbars.

        Other Parameters
        ----------------
        color : color or list of color, optional
            The colors of the bar faces.

        edgecolor : color or list of color, optional
            The colors of the bar edges.

        linewidth : float or array-like, optional
            Width of the bar edge(s). If 0, don't draw edges.

        tick_label : str or list of str, optional
            The tick labels of the bars.
            Default: None (Use default numeric labels.)

        xerr, yerr : float or array-like of shape(N,) or shape(2, N), optional
            If not ``None``, add horizontal / vertical errorbars to the
            bar tips. The values are +/- sizes relative to the data:

            - scalar: symmetric +/- values for all bars
            - shape(N,): symmetric +/- values for each bar
            - shape(2, N): Separate - and + values for each bar. First row
              contains the lower errors, the second row contains the upper
              errors.
            - *None*: No errorbar. (default)

            See :doc:`/gallery/statistics/errorbar_features`
            for an example on the usage of ``xerr`` and ``yerr``.

        ecolor : color or list of color, default: 'black'
            The line color of the errorbars.

        capsize : float, default: :rc:`errorbar.capsize`
           The length of the error bar caps in points.

        error_kw : dict, optional
            Dictionary of kwargs to be passed to the `~.Axes.errorbar`
            method. Values of *ecolor* or *capsize* defined here take
            precedence over the independent kwargs.

        log : bool, default: False
            If ``True``, set the x-axis to be log scale.

        **kwargs : `.Rectangle` properties

        %(Rectangle_kwdoc)s

        See Also
        --------
        bar : Plot a vertical bar plot.

        Notes
        -----
        Stacked bars can be achieved by passing individual *left* values per
        bar. See
        :doc:`/gallery/lines_bars_and_markers/horizontal_barchart_distribution`
        .
        """
    ...


@_copy_docstring_and_deprecators(Axes.bar_label)
def bar_label(container: Any,
              labels: Any = None,
              *,
              fmt: str = '%g',
              label_type: str = 'edge',
              padding: int = 0,
              **kwargs) -> Any: """
        Label a bar plot.

        Adds labels to bars in the given `.BarContainer`.
        You may need to adjust the axis limits to fit the labels.

        Parameters
        ----------
        container : `.BarContainer`
            Container with all the bars and optionally errorbars, likely
            returned from `.bar` or `.barh`.

        labels : array-like, optional
            A list of label texts, that should be displayed. If not given, the
            label texts will be the data values formatted with *fmt*.

        fmt : str, default: '%g'
            A format string for the label.

        label_type : {'edge', 'center'}, default: 'edge'
            The label type. Possible values:

            - 'edge': label placed at the end-point of the bar segment, and the
              value displayed will be the position of that end-point.
            - 'center': label placed in the center of the bar segment, and the
              value displayed will be the length of that segment.
              (useful for stacked bars, i.e.,
              :doc:`/gallery/lines_bars_and_markers/bar_label_demo`)

        padding : float, default: 0
            Distance of label from the end of the bar, in points.

        **kwargs
            Any remaining keyword arguments are passed through to
            `.Axes.annotate`.

        Returns
        -------
        list of `.Text`
            A list of `.Text` instances for the labels.
        """
    ...


@_copy_docstring_and_deprecators(Axes.boxplot)
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
            data: Any = None) -> Any: """
        Make a box and whisker plot.

        Make a box and whisker plot for each column of *x* or each
        vector in sequence *x*.  The box extends from the lower to
        upper quartile values of the data, with a line at the median.
        The whiskers extend from the box to show the range of the
        data.  Flier points are those past the end of the whiskers.

        Parameters
        ----------
        x : Array or a sequence of vectors.
            The input data.

        notch : bool, default: False
            Whether to draw a notched box plot (`True`), or a rectangular box
            plot (`False`).  The notches represent the confidence interval (CI)
            around the median.  The documentation for *bootstrap* describes how
            the locations of the notches are computed by default, but their
            locations may also be overridden by setting the *conf_intervals*
            parameter.

            .. note::

                In cases where the values of the CI are less than the
                lower quartile or greater than the upper quartile, the
                notches will extend beyond the box, giving it a
                distinctive "flipped" appearance. This is expected
                behavior and consistent with other statistical
                visualization packages.

        sym : str, optional
            The default symbol for flier points.  An empty string ('') hides
            the fliers.  If `None`, then the fliers default to 'b+'.  More
            control is provided by the *flierprops* parameter.

        vert : bool, default: True
            If `True`, draws vertical boxes.
            If `False`, draw horizontal boxes.

        whis : float or (float, float), default: 1.5
            The position of the whiskers.

            If a float, the lower whisker is at the lowest datum above
            ``Q1 - whis*(Q3-Q1)``, and the upper whisker at the highest datum
            below ``Q3 + whis*(Q3-Q1)``, where Q1 and Q3 are the first and
            third quartiles.  The default value of ``whis = 1.5`` corresponds
            to Tukey's original definition of boxplots.

            If a pair of floats, they indicate the percentiles at which to
            draw the whiskers (e.g., (5, 95)).  In particular, setting this to
            (0, 100) results in whiskers covering the whole range of the data.

            In the edge case where ``Q1 == Q3``, *whis* is automatically set
            to (0, 100) (cover the whole range of the data) if *autorange* is
            True.

            Beyond the whiskers, data are considered outliers and are plotted
            as individual points.

        bootstrap : int, optional
            Specifies whether to bootstrap the confidence intervals
            around the median for notched boxplots. If *bootstrap* is
            None, no bootstrapping is performed, and notches are
            calculated using a Gaussian-based asymptotic approximation
            (see McGill, R., Tukey, J.W., and Larsen, W.A., 1978, and
            Kendall and Stuart, 1967). Otherwise, bootstrap specifies
            the number of times to bootstrap the median to determine its
            95% confidence intervals. Values between 1000 and 10000 are
            recommended.

        usermedians : 1D array-like, optional
            A 1D array-like of length ``len(x)``.  Each entry that is not
            `None` forces the value of the median for the corresponding
            dataset.  For entries that are `None`, the medians are computed
            by Matplotlib as normal.

        conf_intervals : array-like, optional
            A 2D array-like of shape ``(len(x), 2)``.  Each entry that is not
            None forces the location of the corresponding notch (which is
            only drawn if *notch* is `True`).  For entries that are `None`,
            the notches are computed by the method specified by the other
            parameters (e.g., *bootstrap*).

        positions : array-like, optional
            The positions of the boxes. The ticks and limits are
            automatically set to match the positions. Defaults to
            ``range(1, N+1)`` where N is the number of boxes to be drawn.

        widths : float or array-like
            The widths of the boxes.  The default is 0.5, or ``0.15*(distance
            between extreme positions)``, if that is smaller.

        patch_artist : bool, default: False
            If `False` produces boxes with the Line2D artist. Otherwise,
            boxes and drawn with Patch artists.

        labels : sequence, optional
            Labels for each dataset (one per dataset).

        manage_ticks : bool, default: True
            If True, the tick locations and labels will be adjusted to match
            the boxplot positions.

        autorange : bool, default: False
            When `True` and the data are distributed such that the 25th and
            75th percentiles are equal, *whis* is set to (0, 100) such
            that the whisker ends are at the minimum and maximum of the data.

        meanline : bool, default: False
            If `True` (and *showmeans* is `True`), will try to render the
            mean as a line spanning the full width of the box according to
            *meanprops* (see below).  Not recommended if *shownotches* is also
            True.  Otherwise, means will be shown as points.

        zorder : float, default: ``Line2D.zorder = 2``
            The zorder of the boxplot.

        Returns
        -------
        dict
          A dictionary mapping each component of the boxplot to a list
          of the `.Line2D` instances created. That dictionary has the
          following keys (assuming vertical boxplots):

          - ``boxes``: the main body of the boxplot showing the
            quartiles and the median's confidence intervals if
            enabled.

          - ``medians``: horizontal lines at the median of each box.

          - ``whiskers``: the vertical lines extending to the most
            extreme, non-outlier data points.

          - ``caps``: the horizontal lines at the ends of the
            whiskers.

          - ``fliers``: points representing data that extend beyond
            the whiskers (fliers).

          - ``means``: points or lines representing the means.

        Other Parameters
        ----------------
        showcaps : bool, default: True
            Show the caps on the ends of whiskers.
        showbox : bool, default: True
            Show the central box.
        showfliers : bool, default: True
            Show the outliers beyond the caps.
        showmeans : bool, default: False
            Show the arithmetic means.
        capprops : dict, default: None
            The style of the caps.
        boxprops : dict, default: None
            The style of the box.
        whiskerprops : dict, default: None
            The style of the whiskers.
        flierprops : dict, default: None
            The style of the fliers.
        medianprops : dict, default: None
            The style of the median.
        meanprops : dict, default: None
            The style of the mean.

        Notes
        -----
        Box plots provide insight into distribution properties of the data.
        However, they can be challenging to interpret for the unfamiliar
        reader. The figure below illustrates the different visual features of
        a box plot.

        .. image:: /_static/boxplot_explanation.png
           :alt: Illustration of box plot features
           :scale: 50 %

        The whiskers mark the range of the non-outlier data. The most common
        definition of non-outlier is ``[Q1 - 1.5xIQR, Q3 + 1.5xIQR]``, which
        is also the default in this function. Other whisker meanings can be
        applied via the *whis* parameter.

        See `Box plot <https://en.wikipedia.org/wiki/Box_plot>`_ on Wikipedia
        for further information.

        Violin plots (`~.Axes.violinplot`) add even more detail about the
        statistical distribution by plotting the kernel density estimation
        (KDE) as an estimation of the probability density function.
        """
    ...


@_copy_docstring_and_deprecators(Axes.broken_barh)
def broken_barh(xranges: Any,
                yrange: Any,
                *,
                data: Any = None,
                xranges: Any = ...,
                yrange: Any = ...,
                **kwargs) -> Any: """
        Plot a horizontal sequence of rectangles.

        A rectangle is drawn for each element of *xranges*. All rectangles
        have the same vertical position and size defined by *yrange*.

        This is a convenience function for instantiating a
        `.BrokenBarHCollection`, adding it to the Axes and autoscaling the
        view.

        Parameters
        ----------
        xranges : sequence of tuples (*xmin*, *xwidth*)
            The x-positions and extends of the rectangles. For each tuple
            (*xmin*, *xwidth*) a rectangle is drawn from *xmin* to *xmin* +
            *xwidth*.
        yrange : (*ymin*, *yheight*)
            The y-position and extend for all the rectangles.

        Returns
        -------
        `~.collections.BrokenBarHCollection`

        Other Parameters
        ----------------
        **kwargs : `.BrokenBarHCollection` properties

            Each *kwarg* can be either a single argument applying to all
            rectangles, e.g.::

                facecolors='black'

            or a sequence of arguments over which is cycled, e.g.::

                facecolors=('black', 'blue')

            would create interleaving black and blue rectangles.

            Supported keywords:

            %(BrokenBarHCollection_kwdoc)s
        """
    ...


@_copy_docstring_and_deprecators(Axes.clabel)
def clabel(CS: Any,
           levels: Any = None,
           **kwargs) -> Any: """
        Label a contour plot.

        Adds labels to line contours in given `.ContourSet`.

        Parameters
        ----------
        CS : `~.ContourSet` instance
            Line contours to label.

        levels : array-like, optional
            A list of level values, that should be labeled. The list must be
            a subset of ``CS.levels``. If not given, all levels are labeled.

        **kwargs
            All other parameters are documented in `~.ContourLabeler.clabel`.
        """
    ...


@_copy_docstring_and_deprecators(Axes.cohere)
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
           *,
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
           **kwargs) -> Any: r"""
        Plot the coherence between *x* and *y*.

        Plot the coherence between *x* and *y*.  Coherence is the
        normalized cross spectral density:

        .. math::

          C_{xy} = \frac{|P_{xy}|^2}{P_{xx}P_{yy}}

        Parameters
        ----------
        %(Spectral)s

        %(PSD)s

        noverlap : int, default: 0 (no overlap)
            The number of points of overlap between blocks.

        Fc : int, default: 0
            The center frequency of *x*, which offsets the x extents of the
            plot to reflect the frequency range used when a signal is acquired
            and then filtered and downsampled to baseband.

        Returns
        -------
        Cxy : 1-D array
            The coherence vector.

        freqs : 1-D array
            The frequencies for the elements in *Cxy*.

        Other Parameters
        ----------------
        **kwargs
            Keyword arguments control the `.Line2D` properties:

            %(Line2D_kwdoc)s

        References
        ----------
        Bendat & Piersol -- Random Data: Analysis and Measurement Procedures,
        John Wiley & Sons (1986)
        """
    ...


@_copy_docstring_and_deprecators(Axes.contour)
def contour(*args,
            data: Any = None,
            **kwargs) -> Any: ...


@_copy_docstring_and_deprecators(Axes.contourf)
def contourf(*args,
             data: Any = None,
             **kwargs) -> Any: ...


@_copy_docstring_and_deprecators(Axes.csd)
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
        **kwargs) -> Any: r"""
        Plot the cross-spectral density.

        The cross spectral density :math:`P_{xy}` by Welch's average
        periodogram method.  The vectors *x* and *y* are divided into
        *NFFT* length segments.  Each segment is detrended by function
        *detrend* and windowed by function *window*.  *noverlap* gives
        the length of the overlap between segments.  The product of
        the direct FFTs of *x* and *y* are averaged over each segment
        to compute :math:`P_{xy}`, with a scaling to correct for power
        loss due to windowing.

        If len(*x*) < *NFFT* or len(*y*) < *NFFT*, they will be zero
        padded to *NFFT*.

        Parameters
        ----------
        x, y : 1-D arrays or sequences
            Arrays or sequences containing the data.

        %(Spectral)s

        %(PSD)s

        noverlap : int, default: 0 (no overlap)
            The number of points of overlap between segments.

        Fc : int, default: 0
            The center frequency of *x*, which offsets the x extents of the
            plot to reflect the frequency range used when a signal is acquired
            and then filtered and downsampled to baseband.

        return_line : bool, default: False
            Whether to include the line object plotted in the returned values.

        Returns
        -------
        Pxy : 1-D array
            The values for the cross spectrum :math:`P_{xy}` before scaling
            (complex valued).

        freqs : 1-D array
            The frequencies corresponding to the elements in *Pxy*.

        line : `~matplotlib.lines.Line2D`
            The line created by this function.
            Only returned if *return_line* is True.

        Other Parameters
        ----------------
        **kwargs
            Keyword arguments control the `.Line2D` properties:

            %(Line2D_kwdoc)s

        See Also
        --------
        psd : is equivalent to setting ``y = x``.

        Notes
        -----
        For plotting, the power is plotted as
        :math:`10 \log_{10}(P_{xy})` for decibels, though :math:`P_{xy}` itself
        is returned.

        References
        ----------
        Bendat & Piersol -- Random Data: Analysis and Measurement Procedures,
        John Wiley & Sons (1986)
        """
    ...


@_copy_docstring_and_deprecators(Axes.errorbar)
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
             **kwargs) -> Any: """
        Plot y versus x as lines and/or markers with attached errorbars.

        *x*, *y* define the data locations, *xerr*, *yerr* define the errorbar
        sizes. By default, this draws the data markers/lines as well the
        errorbars. Use fmt='none' to draw errorbars without any data markers.

        Parameters
        ----------
        x, y : float or array-like
            The data positions.

        xerr, yerr : float or array-like, shape(N,) or shape(2, N), optional
            The errorbar sizes:

            - scalar: Symmetric +/- values for all data points.
            - shape(N,): Symmetric +/-values for each data point.
            - shape(2, N): Separate - and + values for each bar. First row
              contains the lower errors, the second row contains the upper
              errors.
            - *None*: No errorbar.

            Note that all error arrays should have *positive* values.

            See :doc:`/gallery/statistics/errorbar_features`
            for an example on the usage of ``xerr`` and ``yerr``.

        fmt : str, default: ''
            The format for the data points / data lines. See `.plot` for
            details.

            Use 'none' (case insensitive) to plot errorbars without any data
            markers.

        ecolor : color, default: None
            The color of the errorbar lines.  If None, use the color of the
            line connecting the markers.

        elinewidth : float, default: None
            The linewidth of the errorbar lines. If None, the linewidth of
            the current style is used.

        capsize : float, default: :rc:`errorbar.capsize`
            The length of the error bar caps in points.

        capthick : float, default: None
            An alias to the keyword argument *markeredgewidth* (a.k.a. *mew*).
            This setting is a more sensible name for the property that
            controls the thickness of the error bar cap in points. For
            backwards compatibility, if *mew* or *markeredgewidth* are given,
            then they will over-ride *capthick*. This may change in future
            releases.

        barsabove : bool, default: False
            If True, will plot the errorbars above the plot
            symbols. Default is below.

        lolims, uplims, xlolims, xuplims : bool, default: False
            These arguments can be used to indicate that a value gives only
            upper/lower limits.  In that case a caret symbol is used to
            indicate this. *lims*-arguments may be scalars, or array-likes of
            the same length as *xerr* and *yerr*.  To use limits with inverted
            axes, `~.Axes.set_xlim` or `~.Axes.set_ylim` must be called before
            :meth:`errorbar`.  Note the tricky parameter names: setting e.g.
            *lolims* to True means that the y-value is a *lower* limit of the
            True value, so, only an *upward*-pointing arrow will be drawn!

        errorevery : int or (int, int), default: 1
            draws error bars on a subset of the data. *errorevery* =N draws
            error bars on the points (x[::N], y[::N]).
            *errorevery* =(start, N) draws error bars on the points
            (x[start::N], y[start::N]). e.g. errorevery=(6, 3)
            adds error bars to the data at (x[6], x[9], x[12], x[15], ...).
            Used to avoid overlapping error bars when two series share x-axis
            values.

        Returns
        -------
        `.ErrorbarContainer`
            The container contains:

            - plotline: `.Line2D` instance of x, y plot markers and/or line.
            - caplines: A tuple of `.Line2D` instances of the error bar caps.
            - barlinecols: A tuple of `.LineCollection` with the horizontal and
              vertical error ranges.

        Other Parameters
        ----------------
        **kwargs
            All other keyword arguments are passed on to the `~.Axes.plot` call
            drawing the markers. For example, this code makes big red squares
            with thick green edges::

                x, y, yerr = rand(3, 10)
                errorbar(x, y, yerr, marker='s', mfc='red',
                         mec='green', ms=20, mew=4)

            where *mfc*, *mec*, *ms* and *mew* are aliases for the longer
            property names, *markerfacecolor*, *markeredgecolor*, *markersize*
            and *markeredgewidth*.

            Valid kwargs for the marker properties are `.Line2D` properties:

            %(Line2D_kwdoc)s
        """
    ...


@_copy_docstring_and_deprecators(Axes.eventplot)
def eventplot(positions: Any,
              orientation: str = 'horizontal',
              lineoffsets: int = 1,
              linelengths: int = 1,
              linewidths: Any = None,
              colors: Any = None,
              linestyles: str = 'solid',
              *,
              data: Any = None,
              **kwargs) -> Any: """
        Plot identical parallel lines at the given positions.

        This type of plot is commonly used in neuroscience for representing
        neural events, where it is usually called a spike raster, dot raster,
        or raster plot.

        However, it is useful in any situation where you wish to show the
        timing or position of multiple sets of discrete events, such as the
        arrival times of people to a business on each day of the month or the
        date of hurricanes each year of the last century.

        Parameters
        ----------
        positions : array-like or list of array-like
            A 1D array-like defines the positions of one sequence of events.

            Multiple groups of events may be passed as a list of array-likes.
            Each group can be styled independently by passing lists of values
            to *lineoffsets*, *linelengths*, *linewidths*, *colors* and
            *linestyles*.

            Note that *positions* can be a 2D array, but in practice different
            event groups usually have different counts so that one will use a
            list of different-length arrays rather than a 2D array.

        orientation : {'horizontal', 'vertical'}, default: 'horizontal'
            The direction of the event sequence:

            - 'horizontal': the events are arranged horizontally.
              The indicator lines are vertical.
            - 'vertical': the events are arranged vertically.
              The indicator lines are horizontal.

        lineoffsets : float or array-like, default: 1
            The offset of the center of the lines from the origin, in the
            direction orthogonal to *orientation*.

            If *positions* is 2D, this can be a sequence with length matching
            the length of *positions*.

        linelengths : float or array-like, default: 1
            The total height of the lines (i.e. the lines stretches from
            ``lineoffset - linelength/2`` to ``lineoffset + linelength/2``).

            If *positions* is 2D, this can be a sequence with length matching
            the length of *positions*.

        linewidths : float or array-like, default: :rc:`lines.linewidth`
            The line width(s) of the event lines, in points.

            If *positions* is 2D, this can be a sequence with length matching
            the length of *positions*.

        colors : color or list of colors, default: :rc:`lines.color`
            The color(s) of the event lines.

            If *positions* is 2D, this can be a sequence with length matching
            the length of *positions*.

        linestyles : str or tuple or list of such values, default: 'solid'
            Default is 'solid'. Valid strings are ['solid', 'dashed',
            'dashdot', 'dotted', '-', '--', '-.', ':']. Dash tuples
            should be of the form::

                (offset, onoffseq),

            where *onoffseq* is an even length tuple of on and off ink
            in points.

            If *positions* is 2D, this can be a sequence with length matching
            the length of *positions*.

        **kwargs
            Other keyword arguments are line collection properties.  See
            `.LineCollection` for a list of the valid properties.

        Returns
        -------
        list of `.EventCollection`
            The `.EventCollection` that were added.

        Notes
        -----
        For *linelengths*, *linewidths*, *colors*, and *linestyles*, if only
        a single value is given, that value is applied to all lines.  If an
        array-like is given, it must have the same length as *positions*, and
        each value will be applied to the corresponding row of the array.

        Examples
        --------
        .. plot:: gallery/lines_bars_and_markers/eventplot_demo.py
        """
    ...


@_copy_docstring_and_deprecators(Axes.fill)
def fill(*args,
         data: Any = None,
         xy: Any = ...,
         closed: bool = ...,
         **kwargs) -> Any: """
        Plot filled polygons.

        Parameters
        ----------
        *args : sequence of x, y, [color]
            Each polygon is defined by the lists of *x* and *y* positions of
            its nodes, optionally followed by a *color* specifier. See
            :mod:`matplotlib.colors` for supported color specifiers. The
            standard color cycle is used for polygons without a color
            specifier.

            You can plot multiple polygons by providing multiple *x*, *y*,
            *[color]* groups.

            For example, each of the following is legal::

                ax.fill(x, y)                    # a polygon with default color
                ax.fill(x, y, "b")               # a blue polygon
                ax.fill(x, y, x2, y2)            # two polygons
                ax.fill(x, y, "b", x2, y2, "r")  # a blue and a red polygon

        data : indexable object, optional
            An object with labelled data. If given, provide the label names to
            plot in *x* and *y*, e.g.::

                ax.fill("time", "signal",
                        data={"time": [0, 1, 2], "signal": [0, 1, 0]})

        Returns
        -------
        list of `~matplotlib.patches.Polygon`

        Other Parameters
        ----------------
        **kwargs : `~matplotlib.patches.Polygon` properties

        Notes
        -----
        Use :meth:`fill_between` if you would like to fill the region between
        two curves.
        """
    ...


@_copy_docstring_and_deprecators(Axes.fill_between)
def fill_between(x: Any,
                 y1: Any,
                 y2: int = 0,
                 where: Any = None,
                 interpolate: bool = False,
                 step: Any = None,
                 *,
                 data: Any = None,
                 **kwargs) -> Any: ...


@_copy_docstring_and_deprecators(Axes.fill_betweenx)
def fill_betweenx(y: Any,
                  x1: Any,
                  x2: int = 0,
                  where: Any = None,
                  step: Any = None,
                  interpolate: bool = False,
                  *,
                  data: Any = None,
                  **kwargs) -> Any: ...


@_copy_docstring_and_deprecators(Axes.grid)
def grid(b: Any = None,
         which: str = 'major',
         axis: str = 'both',
         **kwargs) -> Any: """
        Toggle the gridlines, and optionally set the properties of the lines.
        """
    ...


@_copy_docstring_and_deprecators(Axes.hexbin)
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
           *,
           data: Any = None,
           verts: Any = ...,
           sizes: Any = ...,
           closed: Any = ...,
           **kwargs) -> Any: """
        Make a 2D hexagonal binning plot of points *x*, *y*.

        If *C* is *None*, the value of the hexagon is determined by the number
        of points in the hexagon. Otherwise, *C* specifies values at the
        coordinate (x[i], y[i]). For each hexagon, these values are reduced
        using *reduce_C_function*.

        Parameters
        ----------
        x, y : array-like
            The data positions. *x* and *y* must be of the same length.

        C : array-like, optional
            If given, these values are accumulated in the bins. Otherwise,
            every point has a value of 1. Must be of the same length as *x*
            and *y*.

        gridsize : int or (int, int), default: 100
            If a single int, the number of hexagons in the *x*-direction.
            The number of hexagons in the *y*-direction is chosen such that
            the hexagons are approximately regular.

            Alternatively, if a tuple (*nx*, *ny*), the number of hexagons
            in the *x*-direction and the *y*-direction.

        bins : 'log' or int or sequence, default: None
            Discretization of the hexagon values.

            - If *None*, no binning is applied; the color of each hexagon
              directly corresponds to its count value.
            - If 'log', use a logarithmic scale for the colormap.
              Internally, :math:`log_{10}(i+1)` is used to determine the
              hexagon color. This is equivalent to ``norm=LogNorm()``.
            - If an integer, divide the counts in the specified number
              of bins, and color the hexagons accordingly.
            - If a sequence of values, the values of the lower bound of
              the bins to be used.

        xscale : {'linear', 'log'}, default: 'linear'
            Use a linear or log10 scale on the horizontal axis.

        yscale : {'linear', 'log'}, default: 'linear'
            Use a linear or log10 scale on the vertical axis.

        mincnt : int > 0, default: *None*
            If not *None*, only display cells with more than *mincnt*
            number of points in the cell.

        marginals : bool, default: *False*
            If marginals is *True*, plot the marginal density as
            colormapped rectangles along the bottom of the x-axis and
            left of the y-axis.

        extent : float, default: *None*
            The limits of the bins. The default assigns the limits
            based on *gridsize*, *x*, *y*, *xscale* and *yscale*.

            If *xscale* or *yscale* is set to 'log', the limits are
            expected to be the exponent for a power of 10. E.g. for
            x-limits of 1 and 50 in 'linear' scale and y-limits
            of 10 and 1000 in 'log' scale, enter (1, 50, 1, 3).

            Order of scalars is (left, right, bottom, top).

        Returns
        -------
        `~matplotlib.collections.PolyCollection`
            A `.PolyCollection` defining the hexagonal bins.

            - `.PolyCollection.get_offsets` contains a Mx2 array containing
              the x, y positions of the M hexagon centers.
            - `.PolyCollection.get_array` contains the values of the M
              hexagons.

            If *marginals* is *True*, horizontal
            bar and vertical bar (both PolyCollections) will be attached
            to the return collection as attributes *hbar* and *vbar*.

        Other Parameters
        ----------------
        cmap : str or `~matplotlib.colors.Colormap`, default: :rc:`image.cmap`
            The Colormap instance or registered colormap name used to map
            the bin values to colors.

        norm : `~matplotlib.colors.Normalize`, optional
            The Normalize instance scales the bin values to the canonical
            colormap range [0, 1] for mapping to colors. By default, the data
            range is mapped to the colorbar range using linear scaling.

        vmin, vmax : float, default: None
            The colorbar range. If *None*, suitable min/max values are
            automatically chosen by the `~.Normalize` instance (defaults to
            the respective min/max values of the bins in case of the default
            linear scaling).
            It is deprecated to use *vmin*/*vmax* when *norm* is given.

        alpha : float between 0 and 1, optional
            The alpha blending value, between 0 (transparent) and 1 (opaque).

        linewidths : float, default: *None*
            If *None*, defaults to 1.0.

        edgecolors : {'face', 'none', *None*} or color, default: 'face'
            The color of the hexagon edges. Possible values are:

            - 'face': Draw the edges in the same color as the fill color.
            - 'none': No edges are drawn. This can sometimes lead to unsightly
              unpainted pixels between the hexagons.
            - *None*: Draw outlines in the default color.
            - An explicit color.

        reduce_C_function : callable, default: `numpy.mean`
            The function to aggregate *C* within the bins. It is ignored if
            *C* is not given. This must have the signature::

                def reduce_C_function(C: array) -> float

            Commonly used functions are:

            - `numpy.mean`: average of the points
            - `numpy.sum`: integral of the point values
            - `numpy.amax`: value taken from the largest point

        **kwargs : `~matplotlib.collections.PolyCollection` properties
            All other keyword arguments are passed on to `.PolyCollection`:

            %(PolyCollection_kwdoc)s

        """
    ...


@_copy_docstring_and_deprecators(Axes.hist)
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
         color: Any = ...,
         linewidth: int = ...,
         linestyle: str = ...,
         antialiased: Optional[Any] = ...,
         hatch: Any = ...,
         fill: bool = ...,
         capstyle: Any = ...,
         joinstyle: Any = ...,
         **kwargs) -> Any: """
        Plot a histogram.

        Compute and draw the histogram of *x*.  The return value is a tuple
        (*n*, *bins*, *patches*) or ([*n0*, *n1*, ...], *bins*, [*patches0*,
        *patches1*, ...]) if the input contains multiple data.  See the
        documentation of the *weights* parameter to draw a histogram of
        already-binned data.

        Multiple data can be provided via *x* as a list of datasets
        of potentially different length ([*x0*, *x1*, ...]), or as
        a 2D ndarray in which each column is a dataset.  Note that
        the ndarray form is transposed relative to the list form.

        Masked arrays are not supported.

        The *bins*, *range*, *weights*, and *density* parameters behave as in
        `numpy.histogram`.

        Parameters
        ----------
        x : (n,) array or sequence of (n,) arrays
            Input values, this takes either a single array or a sequence of
            arrays which are not required to be of the same length.

        bins : int or sequence or str, default: :rc:`hist.bins`
            If *bins* is an integer, it defines the number of equal-width bins
            in the range.

            If *bins* is a sequence, it defines the bin edges, including the
            left edge of the first bin and the right edge of the last bin;
            in this case, bins may be unequally spaced.  All but the last
            (righthand-most) bin is half-open.  In other words, if *bins* is::

                [1, 2, 3, 4]

            then the first bin is ``[1, 2)`` (including 1, but excluding 2) and
            the second ``[2, 3)``.  The last bin, however, is ``[3, 4]``, which
            *includes* 4.

            If *bins* is a string, it is one of the binning strategies
            supported by `numpy.histogram_bin_edges`: 'auto', 'fd', 'doane',
            'scott', 'stone', 'rice', 'sturges', or 'sqrt'.

        range : tuple or None, default: None
            The lower and upper range of the bins. Lower and upper outliers
            are ignored. If not provided, *range* is ``(x.min(), x.max())``.
            Range has no effect if *bins* is a sequence.

            If *bins* is a sequence or *range* is specified, autoscaling
            is based on the specified bin range instead of the
            range of x.

        density : bool, default: False
            If ``True``, draw and return a probability density: each bin
            will display the bin's raw count divided by the total number of
            counts *and the bin width*
            (``density = counts / (sum(counts) * np.diff(bins))``),
            so that the area under the histogram integrates to 1
            (``np.sum(density * np.diff(bins)) == 1``).

            If *stacked* is also ``True``, the sum of the histograms is
            normalized to 1.

        weights : (n,) array-like or None, default: None
            An array of weights, of the same shape as *x*.  Each value in
            *x* only contributes its associated weight towards the bin count
            (instead of 1).  If *density* is ``True``, the weights are
            normalized, so that the integral of the density over the range
            remains 1.

            This parameter can be used to draw a histogram of data that has
            already been binned, e.g. using `numpy.histogram` (by treating each
            bin as a single point with a weight equal to its count) ::

                counts, bins = np.histogram(data)
                plt.hist(bins[:-1], bins, weights=counts)

            (or you may alternatively use `~.bar()`).

        cumulative : bool or -1, default: False
            If ``True``, then a histogram is computed where each bin gives the
            counts in that bin plus all bins for smaller values. The last bin
            gives the total number of datapoints.

            If *density* is also ``True`` then the histogram is normalized such
            that the last bin equals 1.

            If *cumulative* is a number less than 0 (e.g., -1), the direction
            of accumulation is reversed.  In this case, if *density* is also
            ``True``, then the histogram is normalized such that the first bin
            equals 1.

        bottom : array-like, scalar, or None, default: None
            Location of the bottom of each bin, ie. bins are drawn from
            ``bottom`` to ``bottom + hist(x, bins)`` If a scalar, the bottom
            of each bin is shifted by the same amount. If an array, each bin
            is shifted independently and the length of bottom must match the
            number of bins. If None, defaults to 0.

        histtype : {'bar', 'barstacked', 'step', 'stepfilled'}, default: 'bar'
            The type of histogram to draw.

            - 'bar' is a traditional bar-type histogram.  If multiple data
              are given the bars are arranged side by side.
            - 'barstacked' is a bar-type histogram where multiple
              data are stacked on top of each other.
            - 'step' generates a lineplot that is by default unfilled.
            - 'stepfilled' generates a lineplot that is by default filled.

        align : {'left', 'mid', 'right'}, default: 'mid'
            The horizontal alignment of the histogram bars.

            - 'left': bars are centered on the left bin edges.
            - 'mid': bars are centered between the bin edges.
            - 'right': bars are centered on the right bin edges.

        orientation : {'vertical', 'horizontal'}, default: 'vertical'
            If 'horizontal', `~.Axes.barh` will be used for bar-type histograms
            and the *bottom* kwarg will be the left edges.

        rwidth : float or None, default: None
            The relative width of the bars as a fraction of the bin width.  If
            ``None``, automatically compute the width.

            Ignored if *histtype* is 'step' or 'stepfilled'.

        log : bool, default: False
            If ``True``, the histogram axis will be set to a log scale.

        color : color or array-like of colors or None, default: None
            Color or sequence of colors, one per dataset.  Default (``None``)
            uses the standard line color sequence.

        label : str or None, default: None
            String, or sequence of strings to match multiple datasets.  Bar
            charts yield multiple patches per dataset, but only the first gets
            the label, so that `~.Axes.legend` will work as expected.

        stacked : bool, default: False
            If ``True``, multiple data are stacked on top of each other If
            ``False`` multiple data are arranged side by side if histtype is
            'bar' or on top of each other if histtype is 'step'

        Returns
        -------
        n : array or list of arrays
            The values of the histogram bins. See *density* and *weights* for a
            description of the possible semantics.  If input *x* is an array,
            then this is an array of length *nbins*. If input is a sequence of
            arrays ``[data1, data2, ...]``, then this is a list of arrays with
            the values of the histograms for each of the arrays in the same
            order.  The dtype of the array *n* (or of its element arrays) will
            always be float even if no weighting or normalization is used.

        bins : array
            The edges of the bins. Length nbins + 1 (nbins left edges and right
            edge of last bin).  Always a single array even when multiple data
            sets are passed in.

        patches : `.BarContainer` or list of a single `.Polygon` or list of \
such objects
            Container of individual artists used to create the histogram
            or list of such containers if there are multiple input datasets.

        Other Parameters
        ----------------
        **kwargs
            `~matplotlib.patches.Patch` properties

        See Also
        --------
        hist2d : 2D histograms

        Notes
        -----
        For large numbers of bins (>1000), 'step' and 'stepfilled' can be
        significantly faster than 'bar' and 'barstacked'.

        """
    ...


@_copy_docstring_and_deprecators(Axes.stairs)
def stairs(values: Any,
           edges: Any = None,
           *,
           orientation: str = 'vertical',
           baseline: int = 0,
           fill: bool = False,
           data: Any = None,
           values: Any = ...,
           edges: Any = ...,
           orientation: Any = ...,
           baseline: Any = ...,
           **kwargs) -> Any: """
        A stepwise constant function as a line with bounding edges
        or a filled plot.

        Parameters
        ----------
        values : array-like
            The step heights.

        edges : array-like
            The edge positions, with ``len(edges) == len(vals) + 1``,
            between which the curve takes on vals values.

        orientation : {'vertical', 'horizontal'}, default: 'vertical'
            The direction of the steps. Vertical means that *values* are along
            the y-axis, and edges are along the x-axis.

        baseline : float, array-like or None, default: 0
            The bottom value of the bounding edges or when
            ``fill=True``, position of lower edge. If *fill* is
            True or an array is passed to *baseline*, a closed
            path is drawn.

        fill : bool, default: False
            Whether the area under the step curve should be filled.

        Returns
        -------
        StepPatch : `matplotlib.patches.StepPatch`

        Other Parameters
        ----------------
        **kwargs
            `~matplotlib.patches.StepPatch` properties

        """
    ...


@_copy_docstring_and_deprecators(Axes.hist2d)
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
           **kwargs) -> Any: """
        Make a 2D histogram plot.

        Parameters
        ----------
        x, y : array-like, shape (n, )
            Input values

        bins : None or int or [int, int] or array-like or [array, array]

            The bin specification:

            - If int, the number of bins for the two dimensions
              (nx=ny=bins).
            - If ``[int, int]``, the number of bins in each dimension
              (nx, ny = bins).
            - If array-like, the bin edges for the two dimensions
              (x_edges=y_edges=bins).
            - If ``[array, array]``, the bin edges in each dimension
              (x_edges, y_edges = bins).

            The default value is 10.

        range : array-like shape(2, 2), optional
            The leftmost and rightmost edges of the bins along each dimension
            (if not specified explicitly in the bins parameters): ``[[xmin,
            xmax], [ymin, ymax]]``. All values outside of this range will be
            considered outliers and not tallied in the histogram.

        density : bool, default: False
            Normalize histogram.  See the documentation for the *density*
            parameter of `~.Axes.hist` for more details.

        weights : array-like, shape (n, ), optional
            An array of values w_i weighing each sample (x_i, y_i).

        cmin, cmax : float, default: None
            All bins that has count less than *cmin* or more than *cmax* will
            not be displayed (set to NaN before passing to imshow) and these
            count values in the return value count histogram will also be set
            to nan upon return.

        Returns
        -------
        h : 2D array
            The bi-dimensional histogram of samples x and y. Values in x are
            histogrammed along the first dimension and values in y are
            histogrammed along the second dimension.
        xedges : 1D array
            The bin edges along the x axis.
        yedges : 1D array
            The bin edges along the y axis.
        image : `~.matplotlib.collections.QuadMesh`

        Other Parameters
        ----------------
        cmap : Colormap or str, optional
            A `.colors.Colormap` instance.  If not set, use rc settings.

        norm : Normalize, optional
            A `.colors.Normalize` instance is used to
            scale luminance data to ``[0, 1]``. If not set, defaults to
            `.colors.Normalize()`.

        vmin/vmax : None or scalar, optional
            Arguments passed to the `~.colors.Normalize` instance.

        alpha : ``0 <= scalar <= 1`` or ``None``, optional
            The alpha blending value.

        **kwargs
            Additional parameters are passed along to the
            `~.Axes.pcolormesh` method and `~matplotlib.collections.QuadMesh`
            constructor.

        See Also
        --------
        hist : 1D histogram plotting

        Notes
        -----
        - Currently ``hist2d`` calculates its own axis limits, and any limits
          previously set are ignored.
        - Rendering the histogram with a logarithmic color scale is
          accomplished by passing a `.colors.LogNorm` instance to the *norm*
          keyword argument. Likewise, power-law normalization (similar
          in effect to gamma correction) can be accomplished with
          `.colors.PowerNorm`.
        """
    ...


@_copy_docstring_and_deprecators(Axes.hlines)
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
           **kwargs) -> Any: """
        Plot horizontal lines at each *y* from *xmin* to *xmax*.

        Parameters
        ----------
        y : float or array-like
            y-indexes where to plot the lines.

        xmin, xmax : float or array-like
            Respective beginning and end of each line. If scalars are
            provided, all lines will have same length.

        colors : list of colors, default: :rc:`lines.color`

        linestyles : {'solid', 'dashed', 'dashdot', 'dotted'}, optional

        label : str, default: ''

        Returns
        -------
        `~matplotlib.collections.LineCollection`

        Other Parameters
        ----------------
        **kwargs :  `~matplotlib.collections.LineCollection` properties.

        See Also
        --------
        vlines : vertical lines
        axhline : horizontal line across the Axes
        """
    ...


@_copy_docstring_and_deprecators(Axes.imshow)
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
           **kwargs) -> Any: """
        Display data as an image, i.e., on a 2D regular raster.

        The input may either be actual RGB(A) data, or 2D scalar data, which
        will be rendered as a pseudocolor image. For displaying a grayscale
        image set up the colormapping using the parameters
        ``cmap='gray', vmin=0, vmax=255``.

        The number of pixels used to render an image is set by the Axes size
        and the *dpi* of the figure. This can lead to aliasing artifacts when
        the image is resampled because the displayed image size will usually
        not match the size of *X* (see
        :doc:`/gallery/images_contours_and_fields/image_antialiasing`).
        The resampling can be controlled via the *interpolation* parameter
        and/or :rc:`image.interpolation`.

        Parameters
        ----------
        X : array-like or PIL image
            The image data. Supported array shapes are:

            - (M, N): an image with scalar data. The values are mapped to
              colors using normalization and a colormap. See parameters *norm*,
              *cmap*, *vmin*, *vmax*.
            - (M, N, 3): an image with RGB values (0-1 float or 0-255 int).
            - (M, N, 4): an image with RGBA values (0-1 float or 0-255 int),
              i.e. including transparency.

            The first two dimensions (M, N) define the rows and columns of
            the image.

            Out-of-range RGB(A) values are clipped.

        cmap : str or `~matplotlib.colors.Colormap`, default: :rc:`image.cmap`
            The Colormap instance or registered colormap name used to map
            scalar data to colors. This parameter is ignored for RGB(A) data.

        norm : `~matplotlib.colors.Normalize`, optional
            The `.Normalize` instance used to scale scalar data to the [0, 1]
            range before mapping to colors using *cmap*. By default, a linear
            scaling mapping the lowest value to 0 and the highest to 1 is used.
            This parameter is ignored for RGB(A) data.

        aspect : {'equal', 'auto'} or float, default: :rc:`image.aspect`
            The aspect ratio of the Axes.  This parameter is particularly
            relevant for images since it determines whether data pixels are
            square.

            This parameter is a shortcut for explicitly calling
            `.Axes.set_aspect`. See there for further details.

            - 'equal': Ensures an aspect ratio of 1. Pixels will be square
              (unless pixel sizes are explicitly made non-square in data
              coordinates using *extent*).
            - 'auto': The Axes is kept fixed and the aspect is adjusted so
              that the data fit in the Axes. In general, this will result in
              non-square pixels.

        interpolation : str, default: :rc:`image.interpolation`
            The interpolation method used.

            Supported values are 'none', 'antialiased', 'nearest', 'bilinear',
            'bicubic', 'spline16', 'spline36', 'hanning', 'hamming', 'hermite',
            'kaiser', 'quadric', 'catrom', 'gaussian', 'bessel', 'mitchell',
            'sinc', 'lanczos', 'blackman'.

            If *interpolation* is 'none', then no interpolation is performed
            on the Agg, ps, pdf and svg backends. Other backends will fall back
            to 'nearest'. Note that most SVG renderers perform interpolation at
            rendering and that the default interpolation method they implement
            may differ.

            If *interpolation* is the default 'antialiased', then 'nearest'
            interpolation is used if the image is upsampled by more than a
            factor of three (i.e. the number of display pixels is at least
            three times the size of the data array).  If the upsampling rate is
            smaller than 3, or the image is downsampled, then 'hanning'
            interpolation is used to act as an anti-aliasing filter, unless the
            image happens to be upsampled by exactly a factor of two or one.

            See
            :doc:`/gallery/images_contours_and_fields/interpolation_methods`
            for an overview of the supported interpolation methods, and
            :doc:`/gallery/images_contours_and_fields/image_antialiasing` for
            a discussion of image antialiasing.

            Some interpolation methods require an additional radius parameter,
            which can be set by *filterrad*. Additionally, the antigrain image
            resize filter is controlled by the parameter *filternorm*.

        alpha : float or array-like, optional
            The alpha blending value, between 0 (transparent) and 1 (opaque).
            If *alpha* is an array, the alpha blending values are applied pixel
            by pixel, and *alpha* must have the same shape as *X*.

        vmin, vmax : float, optional
            When using scalar data and no explicit *norm*, *vmin* and *vmax*
            define the data range that the colormap covers. By default,
            the colormap covers the complete value range of the supplied
            data. It is deprecated to use *vmin*/*vmax* when *norm* is given.
            When using RGB(A) data, parameters *vmin*/*vmax* are ignored.

        origin : {'upper', 'lower'}, default: :rc:`image.origin`
            Place the [0, 0] index of the array in the upper left or lower
            left corner of the Axes. The convention (the default) 'upper' is
            typically used for matrices and images.

            Note that the vertical axis points upward for 'lower'
            but downward for 'upper'.

            See the :doc:`/tutorials/intermediate/imshow_extent` tutorial for
            examples and a more detailed description.

        extent : floats (left, right, bottom, top), optional
            The bounding box in data coordinates that the image will fill.
            The image is stretched individually along x and y to fill the box.

            The default extent is determined by the following conditions.
            Pixels have unit size in data coordinates. Their centers are on
            integer coordinates, and their center coordinates range from 0 to
            columns-1 horizontally and from 0 to rows-1 vertically.

            Note that the direction of the vertical axis and thus the default
            values for top and bottom depend on *origin*:

            - For ``origin == 'upper'`` the default is
              ``(-0.5, numcols-0.5, numrows-0.5, -0.5)``.
            - For ``origin == 'lower'`` the default is
              ``(-0.5, numcols-0.5, -0.5, numrows-0.5)``.

            See the :doc:`/tutorials/intermediate/imshow_extent` tutorial for
            examples and a more detailed description.

        filternorm : bool, default: True
            A parameter for the antigrain image resize filter (see the
            antigrain documentation).  If *filternorm* is set, the filter
            normalizes integer values and corrects the rounding errors. It
            doesn't do anything with the source floating point values, it
            corrects only integers according to the rule of 1.0 which means
            that any sum of pixel weights must be equal to 1.0.  So, the
            filter function must produce a graph of the proper shape.

        filterrad : float > 0, default: 4.0
            The filter radius for filters that have a radius parameter, i.e.
            when interpolation is one of: 'sinc', 'lanczos' or 'blackman'.

        resample : bool, default: :rc:`image.resample`
            When *True*, use a full resampling method.  When *False*, only
            resample when the output image is larger than the input image.

        url : str, optional
            Set the url of the created `.AxesImage`. See `.Artist.set_url`.

        Returns
        -------
        `~matplotlib.image.AxesImage`

        Other Parameters
        ----------------
        **kwargs : `~matplotlib.artist.Artist` properties
            These parameters are passed on to the constructor of the
            `.AxesImage` artist.

        See Also
        --------
        matshow : Plot a matrix or an array as an image.

        Notes
        -----
        Unless *extent* is used, pixel centers will be located at integer
        coordinates. In other words: the origin will coincide with the center
        of pixel (0, 0).

        There are two common representations for RGB images with an alpha
        channel:

        -   Straight (unassociated) alpha: R, G, and B channels represent the
            color of the pixel, disregarding its opacity.
        -   Premultiplied (associated) alpha: R, G, and B channels represent
            the color of the pixel, adjusted for its opacity by multiplication.

        `~matplotlib.pyplot.imshow` expects RGB images adopting the straight
        (unassociated) alpha representation.
        """
    ...


@_copy_docstring_and_deprecators(Axes.legend)
def legend(*args,
           **kwargs) -> Any: """
        Place a legend on the Axes.

        Call signatures::

            legend()
            legend(labels)
            legend(handles, labels)

        The call signatures correspond to these three different ways to use
        this method:

        **1. Automatic detection of elements to be shown in the legend**

        The elements to be added to the legend are automatically determined,
        when you do not pass in any extra arguments.

        In this case, the labels are taken from the artist. You can specify
        them either at artist creation or by calling the
        :meth:`~.Artist.set_label` method on the artist::

            ax.plot([1, 2, 3], label='Inline label')
            ax.legend()

        or::

            line, = ax.plot([1, 2, 3])
            line.set_label('Label via method')
            ax.legend()

        Specific lines can be excluded from the automatic legend element
        selection by defining a label starting with an underscore.
        This is default for all artists, so calling `.Axes.legend` without
        any arguments and without setting the labels manually will result in
        no legend being drawn.


        **2. Labeling existing plot elements**

        To make a legend for lines which already exist on the Axes
        (via plot for instance), simply call this function with an iterable
        of strings, one for each legend item. For example::

            ax.plot([1, 2, 3])
            ax.legend(['A simple line'])

        Note: This call signature is discouraged, because the relation between
        plot elements and labels is only implicit by their order and can
        easily be mixed up.


        **3. Explicitly defining the elements in the legend**

        For full control of which artists have a legend entry, it is possible
        to pass an iterable of legend artists followed by an iterable of
        legend labels respectively::

            ax.legend([line1, line2, line3], ['label1', 'label2', 'label3'])

        Parameters
        ----------
        handles : sequence of `.Artist`, optional
            A list of Artists (lines, patches) to be added to the legend.
            Use this together with *labels*, if you need full control on what
            is shown in the legend and the automatic mechanism described above
            is not sufficient.

            The length of handles and labels should be the same in this
            case. If they are not, they are truncated to the smaller length.

        labels : list of str, optional
            A list of labels to show next to the artists.
            Use this together with *handles*, if you need full control on what
            is shown in the legend and the automatic mechanism described above
            is not sufficient.

        Returns
        -------
        `~matplotlib.legend.Legend`

        Other Parameters
        ----------------
        %(_legend_kw_doc)s

        See Also
        --------
        .Figure.legend

        Notes
        -----
        Some artists are not supported by this function.  See
        :doc:`/tutorials/intermediate/legend_guide` for details.

        Examples
        --------
        .. plot:: gallery/text_labels_and_annotations/legend.py
        """
    ...


@_copy_docstring_and_deprecators(Axes.locator_params)
def locator_params(axis: str = 'both',
                   tight: Any = None,
                   **kwargs) -> Any: ...


@_copy_docstring_and_deprecators(Axes.loglog)
def loglog(*args,
           **kwargs) -> Any: """
        Make a plot with log scaling on both the x and y axis.

        Call signatures::

            loglog([x], y, [fmt], data=None, **kwargs)
            loglog([x], y, [fmt], [x2], y2, [fmt2], ..., **kwargs)

        This is just a thin wrapper around `.plot` which additionally changes
        both the x-axis and the y-axis to log scaling. All of the concepts and
        parameters of plot can be used here as well.

        The additional parameters *base*, *subs* and *nonpositive* control the
        x/y-axis properties. They are just forwarded to `.Axes.set_xscale` and
        `.Axes.set_yscale`. To use different properties on the x-axis and the
        y-axis, use e.g.
        ``ax.set_xscale("log", base=10); ax.set_yscale("log", base=2)``.

        Parameters
        ----------
        base : float, default: 10
            Base of the logarithm.

        subs : sequence, optional
            The location of the minor ticks. If *None*, reasonable locations
            are automatically chosen depending on the number of decades in the
            plot. See `.Axes.set_xscale`/`.Axes.set_yscale` for details.

        nonpositive : {'mask', 'clip'}, default: 'mask'
            Non-positive values can be masked as invalid, or clipped to a very
            small positive number.

        Returns
        -------
        list of `~.Line2D`
            Objects representing the plotted data.

        Other Parameters
        ----------------
        **kwargs
            All parameters supported by `.plot`.
        """
    ...


@_copy_docstring_and_deprecators(Axes.magnitude_spectrum)
def magnitude_spectrum(x: Any,
                       Fs: Any = None,
                       Fc: Any = None,
                       window: Any = None,
                       pad_to: Any = None,
                       sides: Any = None,
                       scale: Any = None,
                       *,
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
                       **kwargs) -> Any: """
        Plot the magnitude spectrum.

        Compute the magnitude spectrum of *x*.  Data is padded to a
        length of *pad_to* and the windowing function *window* is applied to
        the signal.

        Parameters
        ----------
        x : 1-D array or sequence
            Array or sequence containing the data.

        %(Spectral)s

        %(Single_Spectrum)s

        scale : {'default', 'linear', 'dB'}
            The scaling of the values in the *spec*.  'linear' is no scaling.
            'dB' returns the values in dB scale, i.e., the dB amplitude
            (20 * log10). 'default' is 'linear'.

        Fc : int, default: 0
            The center frequency of *x*, which offsets the x extents of the
            plot to reflect the frequency range used when a signal is acquired
            and then filtered and downsampled to baseband.

        Returns
        -------
        spectrum : 1-D array
            The values for the magnitude spectrum before scaling (real valued).

        freqs : 1-D array
            The frequencies corresponding to the elements in *spectrum*.

        line : `~matplotlib.lines.Line2D`
            The line created by this function.

        Other Parameters
        ----------------
        **kwargs
            Keyword arguments control the `.Line2D` properties:

            %(Line2D_kwdoc)s

        See Also
        --------
        psd
            Plots the power spectral density.
        angle_spectrum
            Plots the angles of the corresponding frequencies.
        phase_spectrum
            Plots the phase (unwrapped angle) of the corresponding frequencies.
        specgram
            Can plot the magnitude spectrum of segments within the signal in a
            colormap.
        """
    ...


@_copy_docstring_and_deprecators(Axes.margins)
def margins(*args,
            x: Any = None,
            y: Any = None,
            tight: bool = True) -> Any: ...


@_copy_docstring_and_deprecators(Axes.minorticks_off)
def minorticks_off() -> Any: ...


@_copy_docstring_and_deprecators(Axes.minorticks_on)
def minorticks_on() -> Any: ...


@_copy_docstring_and_deprecators(Axes.pcolor)
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
           **kwargs) -> Any: r"""
        Create a pseudocolor plot with a non-regular rectangular grid.

        Call signature::

            pcolor([X, Y,] C, **kwargs)

        *X* and *Y* can be used to specify the corners of the quadrilaterals.

        .. hint::

            ``pcolor()`` can be very slow for large arrays. In most
            cases you should use the similar but much faster
            `~.Axes.pcolormesh` instead. See
            :ref:`Differences between pcolor() and pcolormesh()
            <differences-pcolor-pcolormesh>` for a discussion of the
            differences.

        Parameters
        ----------
        C : 2D array-like
            The color-mapped values.

        X, Y : array-like, optional
            The coordinates of the corners of quadrilaterals of a pcolormesh::

                (X[i+1, j], Y[i+1, j])       (X[i+1, j+1], Y[i+1, j+1])
                                      +-----+
                                      |     |
                                      +-----+
                    (X[i, j], Y[i, j])       (X[i, j+1], Y[i, j+1])

            Note that the column index corresponds to the x-coordinate, and
            the row index corresponds to y. For details, see the
            :ref:`Notes <axes-pcolormesh-grid-orientation>` section below.

            If ``shading='flat'`` the dimensions of *X* and *Y* should be one
            greater than those of *C*, and the quadrilateral is colored due
            to the value at ``C[i, j]``.  If *X*, *Y* and *C* have equal
            dimensions, a warning will be raised and the last row and column
            of *C* will be ignored.

            If ``shading='nearest'``, the dimensions of *X* and *Y* should be
            the same as those of *C* (if not, a ValueError will be raised). The
            color ``C[i, j]`` will be centered on ``(X[i, j], Y[i, j])``.

            If *X* and/or *Y* are 1-D arrays or column vectors they will be
            expanded as needed into the appropriate 2D arrays, making a
            rectangular grid.

        shading : {'flat', 'nearest', 'auto'}, optional
            The fill style for the quadrilateral; defaults to 'flat' or
            :rc:`pcolor.shading`. Possible values:

            - 'flat': A solid color is used for each quad. The color of the
              quad (i, j), (i+1, j), (i, j+1), (i+1, j+1) is given by
              ``C[i, j]``. The dimensions of *X* and *Y* should be
              one greater than those of *C*; if they are the same as *C*,
              then a deprecation warning is raised, and the last row
              and column of *C* are dropped.
            - 'nearest': Each grid point will have a color centered on it,
              extending halfway between the adjacent grid centers.  The
              dimensions of *X* and *Y* must be the same as *C*.
            - 'auto': Choose 'flat' if dimensions of *X* and *Y* are one
              larger than *C*.  Choose 'nearest' if dimensions are the same.

            See :doc:`/gallery/images_contours_and_fields/pcolormesh_grids`
            for more description.

        cmap : str or `~matplotlib.colors.Colormap`, default: :rc:`image.cmap`
            A Colormap instance or registered colormap name. The colormap
            maps the *C* values to colors.

        norm : `~matplotlib.colors.Normalize`, optional
            The Normalize instance scales the data values to the canonical
            colormap range [0, 1] for mapping to colors. By default, the data
            range is mapped to the colorbar range using linear scaling.

        vmin, vmax : float, default: None
            The colorbar range. If *None*, suitable min/max values are
            automatically chosen by the `~.Normalize` instance (defaults to
            the respective min/max values of *C* in case of the default linear
            scaling).
            It is deprecated to use *vmin*/*vmax* when *norm* is given.

        edgecolors : {'none', None, 'face', color, color sequence}, optional
            The color of the edges. Defaults to 'none'. Possible values:

            - 'none' or '': No edge.
            - *None*: :rc:`patch.edgecolor` will be used. Note that currently
              :rc:`patch.force_edgecolor` has to be True for this to work.
            - 'face': Use the adjacent face color.
            - A color or sequence of colors will set the edge color.

            The singular form *edgecolor* works as an alias.

        alpha : float, default: None
            The alpha blending value of the face color, between 0 (transparent)
            and 1 (opaque). Note: The edgecolor is currently not affected by
            this.

        snap : bool, default: False
            Whether to snap the mesh to pixel boundaries.

        Returns
        -------
        `matplotlib.collections.Collection`

        Other Parameters
        ----------------
        antialiaseds : bool, default: False
            The default *antialiaseds* is False if the default
            *edgecolors*\ ="none" is used.  This eliminates artificial lines
            at patch boundaries, and works regardless of the value of alpha.
            If *edgecolors* is not "none", then the default *antialiaseds*
            is taken from :rc:`patch.antialiased`.
            Stroking the edges may be preferred if *alpha* is 1, but will
            cause artifacts otherwise.

        **kwargs
            Additionally, the following arguments are allowed. They are passed
            along to the `~matplotlib.collections.PolyCollection` constructor:

        %(PolyCollection_kwdoc)s

        See Also
        --------
        pcolormesh : for an explanation of the differences between
            pcolor and pcolormesh.
        imshow : If *X* and *Y* are each equidistant, `~.Axes.imshow` can be a
            faster alternative.

        Notes
        -----
        **Masked arrays**

        *X*, *Y* and *C* may be masked arrays. If either ``C[i, j]``, or one
        of the vertices surrounding ``C[i, j]`` (*X* or *Y* at
        ``[i, j], [i+1, j], [i, j+1], [i+1, j+1]``) is masked, nothing is
        plotted.

        .. _axes-pcolor-grid-orientation:

        **Grid orientation**

        The grid orientation follows the standard matrix convention: An array
        *C* with shape (nrows, ncolumns) is plotted with the column number as
        *X* and the row number as *Y*.
        """
    ...


@_copy_docstring_and_deprecators(Axes.pcolormesh)
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
               **kwargs) -> Any: """
        Create a pseudocolor plot with a non-regular rectangular grid.

        Call signature::

            pcolormesh([X, Y,] C, **kwargs)

        *X* and *Y* can be used to specify the corners of the quadrilaterals.

        .. hint::

           `~.Axes.pcolormesh` is similar to `~.Axes.pcolor`. It is much faster
           and preferred in most cases. For a detailed discussion on the
           differences see :ref:`Differences between pcolor() and pcolormesh()
           <differences-pcolor-pcolormesh>`.

        Parameters
        ----------
        C : 2D array-like
            The color-mapped values.

        X, Y : array-like, optional
            The coordinates of the corners of quadrilaterals of a pcolormesh::

                (X[i+1, j], Y[i+1, j])       (X[i+1, j+1], Y[i+1, j+1])
                                      +-----+
                                      |     |
                                      +-----+
                    (X[i, j], Y[i, j])       (X[i, j+1], Y[i, j+1])

            Note that the column index corresponds to the x-coordinate, and
            the row index corresponds to y. For details, see the
            :ref:`Notes <axes-pcolormesh-grid-orientation>` section below.

            If ``shading='flat'`` the dimensions of *X* and *Y* should be one
            greater than those of *C*, and the quadrilateral is colored due
            to the value at ``C[i, j]``.  If *X*, *Y* and *C* have equal
            dimensions, a warning will be raised and the last row and column
            of *C* will be ignored.

            If ``shading='nearest'`` or ``'gouraud'``, the dimensions of *X*
            and *Y* should be the same as those of *C* (if not, a ValueError
            will be raised).  For ``'nearest'`` the color ``C[i, j]`` is
            centered on ``(X[i, j], Y[i, j])``.  For ``'gouraud'``, a smooth
            interpolation is caried out between the quadrilateral corners.

            If *X* and/or *Y* are 1-D arrays or column vectors they will be
            expanded as needed into the appropriate 2D arrays, making a
            rectangular grid.

        cmap : str or `~matplotlib.colors.Colormap`, default: :rc:`image.cmap`
            A Colormap instance or registered colormap name. The colormap
            maps the *C* values to colors.

        norm : `~matplotlib.colors.Normalize`, optional
            The Normalize instance scales the data values to the canonical
            colormap range [0, 1] for mapping to colors. By default, the data
            range is mapped to the colorbar range using linear scaling.

        vmin, vmax : float, default: None
            The colorbar range. If *None*, suitable min/max values are
            automatically chosen by the `~.Normalize` instance (defaults to
            the respective min/max values of *C* in case of the default linear
            scaling).
            It is deprecated to use *vmin*/*vmax* when *norm* is given.

        edgecolors : {'none', None, 'face', color, color sequence}, optional
            The color of the edges. Defaults to 'none'. Possible values:

            - 'none' or '': No edge.
            - *None*: :rc:`patch.edgecolor` will be used. Note that currently
              :rc:`patch.force_edgecolor` has to be True for this to work.
            - 'face': Use the adjacent face color.
            - A color or sequence of colors will set the edge color.

            The singular form *edgecolor* works as an alias.

        alpha : float, default: None
            The alpha blending value, between 0 (transparent) and 1 (opaque).

        shading : {'flat', 'nearest', 'gouraud', 'auto'}, optional
            The fill style for the quadrilateral; defaults to
            'flat' or :rc:`pcolor.shading`. Possible values:

            - 'flat': A solid color is used for each quad. The color of the
              quad (i, j), (i+1, j), (i, j+1), (i+1, j+1) is given by
              ``C[i, j]``. The dimensions of *X* and *Y* should be
              one greater than those of *C*; if they are the same as *C*,
              then a deprecation warning is raised, and the last row
              and column of *C* are dropped.
            - 'nearest': Each grid point will have a color centered on it,
              extending halfway between the adjacent grid centers.  The
              dimensions of *X* and *Y* must be the same as *C*.
            - 'gouraud': Each quad will be Gouraud shaded: The color of the
              corners (i', j') are given by ``C[i', j']``. The color values of
              the area in between is interpolated from the corner values.
              The dimensions of *X* and *Y* must be the same as *C*. When
              Gouraud shading is used, *edgecolors* is ignored.
            - 'auto': Choose 'flat' if dimensions of *X* and *Y* are one
              larger than *C*.  Choose 'nearest' if dimensions are the same.

            See :doc:`/gallery/images_contours_and_fields/pcolormesh_grids`
            for more description.

        snap : bool, default: False
            Whether to snap the mesh to pixel boundaries.

        rasterized: bool, optional
            Rasterize the pcolormesh when drawing vector graphics.  This can
            speed up rendering and produce smaller files for large data sets.
            See also :doc:`/gallery/misc/rasterization_demo`.

        Returns
        -------
        `matplotlib.collections.QuadMesh`

        Other Parameters
        ----------------
        **kwargs
            Additionally, the following arguments are allowed. They are passed
            along to the `~matplotlib.collections.QuadMesh` constructor:

        %(QuadMesh_kwdoc)s

        See Also
        --------
        pcolor : An alternative implementation with slightly different
            features. For a detailed discussion on the differences see
            :ref:`Differences between pcolor() and pcolormesh()
            <differences-pcolor-pcolormesh>`.
        imshow : If *X* and *Y* are each equidistant, `~.Axes.imshow` can be a
            faster alternative.

        Notes
        -----
        **Masked arrays**

        *C* may be a masked array. If ``C[i, j]`` is masked, the corresponding
        quadrilateral will be transparent. Masking of *X* and *Y* is not
        supported. Use `~.Axes.pcolor` if you need this functionality.

        .. _axes-pcolormesh-grid-orientation:

        **Grid orientation**

        The grid orientation follows the standard matrix convention: An array
        *C* with shape (nrows, ncolumns) is plotted with the column number as
        *X* and the row number as *Y*.

        .. _differences-pcolor-pcolormesh:

        **Differences between pcolor() and pcolormesh()**

        Both methods are used to create a pseudocolor plot of a 2D array
        using quadrilaterals.

        The main difference lies in the created object and internal data
        handling:
        While `~.Axes.pcolor` returns a `.PolyCollection`, `~.Axes.pcolormesh`
        returns a `.QuadMesh`. The latter is more specialized for the given
        purpose and thus is faster. It should almost always be preferred.

        There is also a slight difference in the handling of masked arrays.
        Both `~.Axes.pcolor` and `~.Axes.pcolormesh` support masked arrays
        for *C*. However, only `~.Axes.pcolor` supports masked arrays for *X*
        and *Y*. The reason lies in the internal handling of the masked values.
        `~.Axes.pcolor` leaves out the respective polygons from the
        PolyCollection. `~.Axes.pcolormesh` sets the facecolor of the masked
        elements to transparent. You can see the difference when using
        edgecolors. While all edges are drawn irrespective of masking in a
        QuadMesh, the edge between two adjacent masked quadrilaterals in
        `~.Axes.pcolor` is not drawn as the corresponding polygons do not
        exist in the PolyCollection.

        Another difference is the support of Gouraud shading in
        `~.Axes.pcolormesh`, which is not available with `~.Axes.pcolor`.

        """
    ...


@_copy_docstring_and_deprecators(Axes.phase_spectrum)
def phase_spectrum(x: Any,
                   Fs: Any = None,
                   Fc: Any = None,
                   window: Any = None,
                   pad_to: Any = None,
                   sides: Any = None,
                   *,
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
                   **kwargs) -> Any: """
        Plot the phase spectrum.

        Compute the phase spectrum (unwrapped angle spectrum) of *x*.
        Data is padded to a length of *pad_to* and the windowing function
        *window* is applied to the signal.

        Parameters
        ----------
        x : 1-D array or sequence
            Array or sequence containing the data

        %(Spectral)s

        %(Single_Spectrum)s

        Fc : int, default: 0
            The center frequency of *x*, which offsets the x extents of the
            plot to reflect the frequency range used when a signal is acquired
            and then filtered and downsampled to baseband.

        Returns
        -------
        spectrum : 1-D array
            The values for the phase spectrum in radians (real valued).

        freqs : 1-D array
            The frequencies corresponding to the elements in *spectrum*.

        line : `~matplotlib.lines.Line2D`
            The line created by this function.

        Other Parameters
        ----------------
        **kwargs
            Keyword arguments control the `.Line2D` properties:

            %(Line2D_kwdoc)s

        See Also
        --------
        magnitude_spectrum
            Plots the magnitudes of the corresponding frequencies.
        angle_spectrum
            Plots the wrapped version of this function.
        specgram
            Can plot the phase spectrum of segments within the signal in a
            colormap.
        """
    ...


@_copy_docstring_and_deprecators(Axes.pie)
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
        *,
        normalize: Any = None,
        data: Any = None) -> Any: """
        Plot a pie chart.

        Make a pie chart of array *x*.  The fractional area of each wedge is
        given by ``x/sum(x)``.  If ``sum(x) < 1``, then the values of *x* give
        the fractional area directly and the array will not be normalized. The
        resulting pie will have an empty wedge of size ``1 - sum(x)``.

        The wedges are plotted counterclockwise, by default starting from the
        x-axis.

        Parameters
        ----------
        x : 1D array-like
            The wedge sizes.

        explode : array-like, default: None
            If not *None*, is a ``len(x)`` array which specifies the fraction
            of the radius with which to offset each wedge.

        labels : list, default: None
            A sequence of strings providing the labels for each wedge

        colors : array-like, default: None
            A sequence of colors through which the pie chart will cycle.  If
            *None*, will use the colors in the currently active cycle.

        autopct : None or str or callable, default: None
            If not *None*, is a string or function used to label the wedges
            with their numeric value.  The label will be placed inside the
            wedge.  If it is a format string, the label will be ``fmt % pct``.
            If it is a function, it will be called.

        pctdistance : float, default: 0.6
            The ratio between the center of each pie slice and the start of
            the text generated by *autopct*.  Ignored if *autopct* is *None*.

        shadow : bool, default: False
            Draw a shadow beneath the pie.

        normalize : None or bool, default: None
            When *True*, always make a full pie by normalizing x so that
            ``sum(x) == 1``. *False* makes a partial pie if ``sum(x) <= 1``
            and raises a `ValueError` for ``sum(x) > 1``.

            When *None*, defaults to *True* if ``sum(x) >= 1`` and *False* if
            ``sum(x) < 1``.

            Please note that the previous default value of *None* is now
            deprecated, and the default will change to *True* in the next
            release. Please pass ``normalize=False`` explicitly if you want to
            draw a partial pie.

        labeldistance : float or None, default: 1.1
            The radial distance at which the pie labels are drawn.
            If set to ``None``, label are not drawn, but are stored for use in
            ``legend()``

        startangle : float, default: 0 degrees
            The angle by which the start of the pie is rotated,
            counterclockwise from the x-axis.

        radius : float, default: 1
            The radius of the pie.

        counterclock : bool, default: True
            Specify fractions direction, clockwise or counterclockwise.

        wedgeprops : dict, default: None
            Dict of arguments passed to the wedge objects making the pie.
            For example, you can pass in ``wedgeprops = {'linewidth': 3}``
            to set the width of the wedge border lines equal to 3.
            For more details, look at the doc/arguments of the wedge object.
            By default ``clip_on=False``.

        textprops : dict, default: None
            Dict of arguments to pass to the text objects.

        center : (float, float), default: (0, 0)
            The coordinates of the center of the chart.

        frame : bool, default: False
            Plot Axes frame with the chart if true.

        rotatelabels : bool, default: False
            Rotate each label to the angle of the corresponding slice if true.

        Returns
        -------
        patches : list
            A sequence of `matplotlib.patches.Wedge` instances

        texts : list
            A list of the label `.Text` instances.

        autotexts : list
            A list of `.Text` instances for the numeric labels. This will only
            be returned if the parameter *autopct* is not *None*.

        Notes
        -----
        The pie chart will probably look best if the figure and Axes are
        square, or the Axes aspect is equal.
        This method sets the aspect ratio of the axis to "equal".
        The Axes aspect ratio can be controlled with `.Axes.set_aspect`.
        """
    ...


@_copy_docstring_and_deprecators(Axes.plot)
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
         **kwargs) -> Any: """
        Plot y versus x as lines and/or markers.

        Call signatures::

            plot([x], y, [fmt], *, data=None, **kwargs)
            plot([x], y, [fmt], [x2], y2, [fmt2], ..., **kwargs)

        The coordinates of the points or line nodes are given by *x*, *y*.

        The optional parameter *fmt* is a convenient way for defining basic
        formatting like color, marker and linestyle. It's a shortcut string
        notation described in the *Notes* section below.

        >>> plot(x, y)        # plot x and y using default line style and color
        >>> plot(x, y, 'bo')  # plot x and y using blue circle markers
        >>> plot(y)           # plot y using x as index array 0..N-1
        >>> plot(y, 'r+')     # ditto, but with red plusses

        You can use `.Line2D` properties as keyword arguments for more
        control on the appearance. Line properties and *fmt* can be mixed.
        The following two calls yield identical results:

        >>> plot(x, y, 'go--', linewidth=2, markersize=12)
        >>> plot(x, y, color='green', marker='o', linestyle='dashed',
        ...      linewidth=2, markersize=12)

        When conflicting with *fmt*, keyword arguments take precedence.


        **Plotting labelled data**

        There's a convenient way for plotting objects with labelled data (i.e.
        data that can be accessed by index ``obj['y']``). Instead of giving
        the data in *x* and *y*, you can provide the object in the *data*
        parameter and just give the labels for *x* and *y*::

        >>> plot('xlabel', 'ylabel', data=obj)

        All indexable objects are supported. This could e.g. be a `dict`, a
        `pandas.DataFrame` or a structured numpy array.


        **Plotting multiple sets of data**

        There are various ways to plot multiple sets of data.

        - The most straight forward way is just to call `plot` multiple times.
          Example:

          >>> plot(x1, y1, 'bo')
          >>> plot(x2, y2, 'go')

        - If *x* and/or *y* are 2D arrays a separate data set will be drawn
          for every column. If both *x* and *y* are 2D, they must have the
          same shape. If only one of them is 2D with shape (N, m) the other
          must have length N and will be used for every data set m.

          Example:

          >>> x = [1, 2, 3]
          >>> y = np.array([[1, 2], [3, 4], [5, 6]])
          >>> plot(x, y)

          is equivalent to:

          >>> for col in range(y.shape[1]):
          ...     plot(x, y[:, col])

        - The third way is to specify multiple sets of *[x]*, *y*, *[fmt]*
          groups::

          >>> plot(x1, y1, 'g^', x2, y2, 'g-')

          In this case, any additional keyword argument applies to all
          datasets. Also this syntax cannot be combined with the *data*
          parameter.

        By default, each line is assigned a different style specified by a
        'style cycle'. The *fmt* and line property parameters are only
        necessary if you want explicit deviations from these defaults.
        Alternatively, you can also change the style cycle using
        :rc:`axes.prop_cycle`.


        Parameters
        ----------
        x, y : array-like or scalar
            The horizontal / vertical coordinates of the data points.
            *x* values are optional and default to ``range(len(y))``.

            Commonly, these parameters are 1D arrays.

            They can also be scalars, or two-dimensional (in that case, the
            columns represent separate data sets).

            These arguments cannot be passed as keywords.

        fmt : str, optional
            A format string, e.g. 'ro' for red circles. See the *Notes*
            section for a full description of the format strings.

            Format strings are just an abbreviation for quickly setting
            basic line properties. All of these and more can also be
            controlled by keyword arguments.

            This argument cannot be passed as keyword.

        data : indexable object, optional
            An object with labelled data. If given, provide the label names to
            plot in *x* and *y*.

            .. note::
                Technically there's a slight ambiguity in calls where the
                second label is a valid *fmt*. ``plot('n', 'o', data=obj)``
                could be ``plt(x, y)`` or ``plt(y, fmt)``. In such cases,
                the former interpretation is chosen, but a warning is issued.
                You may suppress the warning by adding an empty format string
                ``plot('n', 'o', '', data=obj)``.

        Returns
        -------
        list of `.Line2D`
            A list of lines representing the plotted data.

        Other Parameters
        ----------------
        scalex, scaley : bool, default: True
            These parameters determine if the view limits are adapted to the
            data limits. The values are passed on to `autoscale_view`.

        **kwargs : `.Line2D` properties, optional
            *kwargs* are used to specify properties like a line label (for
            auto legends), linewidth, antialiasing, marker face color.
            Example::

            >>> plot([1, 2, 3], [1, 2, 3], 'go-', label='line 1', linewidth=2)
            >>> plot([1, 2, 3], [1, 4, 9], 'rs', label='line 2')

            If you specify multiple lines with one plot call, the kwargs apply
            to all those lines. In case the label object is iterable, each
            element is used as labels for each set of data.

            Here is a list of available `.Line2D` properties:

            %(Line2D_kwdoc)s

        See Also
        --------
        scatter : XY scatter plot with markers of varying size and/or color (
            sometimes also called bubble chart).

        Notes
        -----
        **Format Strings**

        A format string consists of a part for color, marker and line::

            fmt = '[marker][line][color]'

        Each of them is optional. If not provided, the value from the style
        cycle is used. Exception: If ``line`` is given, but no ``marker``,
        the data will be a line without markers.

        Other combinations such as ``[color][marker][line]`` are also
        supported, but note that their parsing may be ambiguous.

        **Markers**

        =============   ===============================
        character       description
        =============   ===============================
        ``'.'``         point marker
        ``','``         pixel marker
        ``'o'``         circle marker
        ``'v'``         triangle_down marker
        ``'^'``         triangle_up marker
        ``'<'``         triangle_left marker
        ``'>'``         triangle_right marker
        ``'1'``         tri_down marker
        ``'2'``         tri_up marker
        ``'3'``         tri_left marker
        ``'4'``         tri_right marker
        ``'8'``         octagon marker
        ``'s'``         square marker
        ``'p'``         pentagon marker
        ``'P'``         plus (filled) marker
        ``'*'``         star marker
        ``'h'``         hexagon1 marker
        ``'H'``         hexagon2 marker
        ``'+'``         plus marker
        ``'x'``         x marker
        ``'X'``         x (filled) marker
        ``'D'``         diamond marker
        ``'d'``         thin_diamond marker
        ``'|'``         vline marker
        ``'_'``         hline marker
        =============   ===============================

        **Line Styles**

        =============    ===============================
        character        description
        =============    ===============================
        ``'-'``          solid line style
        ``'--'``         dashed line style
        ``'-.'``         dash-dot line style
        ``':'``          dotted line style
        =============    ===============================

        Example format strings::

            'b'    # blue markers with default shape
            'or'   # red circles
            '-g'   # green solid line
            '--'   # dashed line with default color
            '^k:'  # black triangle_up markers connected by a dotted line

        **Colors**

        The supported color abbreviations are the single letter codes

        =============    ===============================
        character        color
        =============    ===============================
        ``'b'``          blue
        ``'g'``          green
        ``'r'``          red
        ``'c'``          cyan
        ``'m'``          magenta
        ``'y'``          yellow
        ``'k'``          black
        ``'w'``          white
        =============    ===============================

        and the ``'CN'`` colors that index into the default property cycle.

        If the color is the only part of the format string, you can
        additionally use any  `matplotlib.colors` spec, e.g. full names
        (``'green'``) or hex strings (``'#008000'``).
        """
    ...


@_copy_docstring_and_deprecators(Axes.plot_date)
def plot_date(x: Any,
              y: Any,
              fmt: str = 'o',
              tz: Any = None,
              xdate: bool = True,
              ydate: bool = False,
              *,
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
              **kwargs) -> Any: """
        Plot co-ercing the axis to treat floats as dates.

        Similar to `.plot`, this plots *y* vs. *x* as lines or markers.
        However, the axis labels are formatted as dates depending on *xdate*
        and *ydate*.  Note that `.plot` will work with `datetime` and
        `numpy.datetime64` objects without resorting to this method.

        Parameters
        ----------
        x, y : array-like
            The coordinates of the data points. If *xdate* or *ydate* is
            *True*, the respective values *x* or *y* are interpreted as
            :ref:`Matplotlib dates <date-format>`.

        fmt : str, optional
            The plot format string. For details, see the corresponding
            parameter in `.plot`.

        tz : timezone string or `datetime.tzinfo`, default: :rc:`timezone`
            The time zone to use in labeling dates.

        xdate : bool, default: True
            If *True*, the *x*-axis will be interpreted as Matplotlib dates.

        ydate : bool, default: False
            If *True*, the *y*-axis will be interpreted as Matplotlib dates.

        Returns
        -------
        list of `~.Line2D`
            Objects representing the plotted data.

        Other Parameters
        ----------------
        **kwargs
            Keyword arguments control the `.Line2D` properties:

            %(Line2D_kwdoc)s

        See Also
        --------
        matplotlib.dates : Helper functions on dates.
        matplotlib.dates.date2num : Convert dates to num.
        matplotlib.dates.num2date : Convert num to dates.
        matplotlib.dates.drange : Create an equally spaced sequence of dates.

        Notes
        -----
        If you are using custom date tickers and formatters, it may be
        necessary to set the formatters/locators after the call to
        `.plot_date`. `.plot_date` will set the default tick locator to
        `.AutoDateLocator` (if the tick locator is not already set to a
        `.DateLocator` instance) and the default tick formatter to
        `.AutoDateFormatter` (if the tick formatter is not already set to a
        `.DateFormatter` instance).
        """
    ...


@_copy_docstring_and_deprecators(Axes.psd)
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
        **kwargs) -> Any: r"""
        Plot the power spectral density.

        The power spectral density :math:`P_{xx}` by Welch's average
        periodogram method.  The vector *x* is divided into *NFFT* length
        segments.  Each segment is detrended by function *detrend* and
        windowed by function *window*.  *noverlap* gives the length of
        the overlap between segments.  The :math:`|\mathrm{fft}(i)|^2`
        of each segment :math:`i` are averaged to compute :math:`P_{xx}`,
        with a scaling to correct for power loss due to windowing.

        If len(*x*) < *NFFT*, it will be zero padded to *NFFT*.

        Parameters
        ----------
        x : 1-D array or sequence
            Array or sequence containing the data

        %(Spectral)s

        %(PSD)s

        noverlap : int, default: 0 (no overlap)
            The number of points of overlap between segments.

        Fc : int, default: 0
            The center frequency of *x*, which offsets the x extents of the
            plot to reflect the frequency range used when a signal is acquired
            and then filtered and downsampled to baseband.

        return_line : bool, default: False
            Whether to include the line object plotted in the returned values.

        Returns
        -------
        Pxx : 1-D array
            The values for the power spectrum :math:`P_{xx}` before scaling
            (real valued).

        freqs : 1-D array
            The frequencies corresponding to the elements in *Pxx*.

        line : `~matplotlib.lines.Line2D`
            The line created by this function.
            Only returned if *return_line* is True.

        Other Parameters
        ----------------
        **kwargs
            Keyword arguments control the `.Line2D` properties:

            %(Line2D_kwdoc)s

        See Also
        --------
        specgram
            Differs in the default overlap; in not returning the mean of the
            segment periodograms; in returning the times of the segments; and
            in plotting a colormap instead of a line.
        magnitude_spectrum
            Plots the magnitude spectrum.
        csd
            Plots the spectral density between two signals.

        Notes
        -----
        For plotting, the power is plotted as
        :math:`10\log_{10}(P_{xx})` for decibels, though *Pxx* itself
        is returned.

        References
        ----------
        Bendat & Piersol -- Random Data: Analysis and Measurement Procedures,
        John Wiley & Sons (1986)
        """
    ...


@_copy_docstring_and_deprecators(Axes.quiver)
def quiver(*args,
           data: Any = None,
           **kwargs) -> Any: ...


@_copy_docstring_and_deprecators(Axes.quiverkey)
def quiverkey(Q: Any,
              X: Any,
              Y: Any,
              U: Any,
              label: Any,
              **kwargs) -> Any: ...


@_copy_docstring_and_deprecators(Axes.scatter)
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
            **kwargs) -> Any: """
        A scatter plot of *y* vs. *x* with varying marker size and/or color.

        Parameters
        ----------
        x, y : float or array-like, shape (n, )
            The data positions.

        s : float or array-like, shape (n, ), optional
            The marker size in points**2.
            Default is ``rcParams['lines.markersize'] ** 2``.

        c : array-like or list of colors or color, optional
            The marker colors. Possible values:

            - A scalar or sequence of n numbers to be mapped to colors using
              *cmap* and *norm*.
            - A 2D array in which the rows are RGB or RGBA.
            - A sequence of colors of length n.
            - A single color format string.

            Note that *c* should not be a single numeric RGB or RGBA sequence
            because that is indistinguishable from an array of values to be
            colormapped. If you want to specify the same RGB or RGBA value for
            all points, use a 2D array with a single row.  Otherwise, value-
            matching will have precedence in case of a size matching with *x*
            and *y*.

            If you wish to specify a single color for all points
            prefer the *color* keyword argument.

            Defaults to `None`. In that case the marker color is determined
            by the value of *color*, *facecolor* or *facecolors*. In case
            those are not specified or `None`, the marker color is determined
            by the next color of the ``Axes``' current "shape and fill" color
            cycle. This cycle defaults to :rc:`axes.prop_cycle`.

        marker : `~.markers.MarkerStyle`, default: :rc:`scatter.marker`
            The marker style. *marker* can be either an instance of the class
            or the text shorthand for a particular marker.
            See :mod:`matplotlib.markers` for more information about marker
            styles.

        cmap : str or `~matplotlib.colors.Colormap`, default: :rc:`image.cmap`
            A `.Colormap` instance or registered colormap name. *cmap* is only
            used if *c* is an array of floats.

        norm : `~matplotlib.colors.Normalize`, default: None
            If *c* is an array of floats, *norm* is used to scale the color
            data, *c*, in the range 0 to 1, in order to map into the colormap
            *cmap*.
            If *None*, use the default `.colors.Normalize`.

        vmin, vmax : float, default: None
            *vmin* and *vmax* are used in conjunction with the default norm to
            map the color array *c* to the colormap *cmap*. If None, the
            respective min and max of the color array is used.
            It is deprecated to use *vmin*/*vmax* when *norm* is given.

        alpha : float, default: None
            The alpha blending value, between 0 (transparent) and 1 (opaque).

        linewidths : float or array-like, default: :rc:`lines.linewidth`
            The linewidth of the marker edges. Note: The default *edgecolors*
            is 'face'. You may want to change this as well.

        edgecolors : {'face', 'none', *None*} or color or sequence of color, \
default: :rc:`scatter.edgecolors`
            The edge color of the marker. Possible values:

            - 'face': The edge color will always be the same as the face color.
            - 'none': No patch boundary will be drawn.
            - A color or sequence of colors.

            For non-filled markers, *edgecolors* is ignored. Instead, the color
            is determined like with 'face', i.e. from *c*, *colors*, or
            *facecolors*.

        plotnonfinite : bool, default: False
            Whether to plot points with nonfinite *c* (i.e. ``inf``, ``-inf``
            or ``nan``). If ``True`` the points are drawn with the *bad*
            colormap color (see `.Colormap.set_bad`).

        Returns
        -------
        `~matplotlib.collections.PathCollection`

        Other Parameters
        ----------------
        **kwargs : `~matplotlib.collections.Collection` properties

        See Also
        --------
        plot : To plot scatter plots when markers are identical in size and
            color.

        Notes
        -----
        * The `.plot` function will be faster for scatterplots where markers
          don't vary in size or color.

        * Any or all of *x*, *y*, *s*, and *c* may be masked arrays, in which
          case all masks will be combined and only unmasked points will be
          plotted.

        * Fundamentally, scatter works with 1D arrays; *x*, *y*, *s*, and *c*
          may be input as N-D arrays, but within scatter they will be
          flattened. The exception is *c*, which will be flattened only if its
          size matches the size of *x* and *y*.

        """
    ...


@_copy_docstring_and_deprecators(Axes.semilogx)
def semilogx(*args,
             **kwargs) -> Any: """
        Make a plot with log scaling on the x axis.

        Call signatures::

            semilogx([x], y, [fmt], data=None, **kwargs)
            semilogx([x], y, [fmt], [x2], y2, [fmt2], ..., **kwargs)

        This is just a thin wrapper around `.plot` which additionally changes
        the x-axis to log scaling. All of the concepts and parameters of plot
        can be used here as well.

        The additional parameters *base*, *subs*, and *nonpositive* control the
        x-axis properties. They are just forwarded to `.Axes.set_xscale`.

        Parameters
        ----------
        base : float, default: 10
            Base of the x logarithm.

        subs : array-like, optional
            The location of the minor xticks. If *None*, reasonable locations
            are automatically chosen depending on the number of decades in the
            plot. See `.Axes.set_xscale` for details.

        nonpositive : {'mask', 'clip'}, default: 'mask'
            Non-positive values in x can be masked as invalid, or clipped to a
            very small positive number.

        Returns
        -------
        list of `~.Line2D`
            Objects representing the plotted data.

        Other Parameters
        ----------------
        **kwargs
            All parameters supported by `.plot`.
        """
    ...


@_copy_docstring_and_deprecators(Axes.semilogy)
def semilogy(*args,
             **kwargs) -> Any: """
        Make a plot with log scaling on the y axis.

        Call signatures::

            semilogy([x], y, [fmt], data=None, **kwargs)
            semilogy([x], y, [fmt], [x2], y2, [fmt2], ..., **kwargs)

        This is just a thin wrapper around `.plot` which additionally changes
        the y-axis to log scaling. All of the concepts and parameters of plot
        can be used here as well.

        The additional parameters *base*, *subs*, and *nonpositive* control the
        y-axis properties. They are just forwarded to `.Axes.set_yscale`.

        Parameters
        ----------
        base : float, default: 10
            Base of the y logarithm.

        subs : array-like, optional
            The location of the minor yticks. If *None*, reasonable locations
            are automatically chosen depending on the number of decades in the
            plot. See `.Axes.set_yscale` for details.

        nonpositive : {'mask', 'clip'}, default: 'mask'
            Non-positive values in y can be masked as invalid, or clipped to a
            very small positive number.

        Returns
        -------
        list of `~.Line2D`
            Objects representing the plotted data.

        Other Parameters
        ----------------
        **kwargs
            All parameters supported by `.plot`.
        """
    ...


@_copy_docstring_and_deprecators(Axes.specgram)
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
             **kwargs) -> Any: """
        Plot a spectrogram.

        Compute and plot a spectrogram of data in *x*.  Data are split into
        *NFFT* length segments and the spectrum of each section is
        computed.  The windowing function *window* is applied to each
        segment, and the amount of overlap of each segment is
        specified with *noverlap*. The spectrogram is plotted as a colormap
        (using imshow).

        Parameters
        ----------
        x : 1-D array or sequence
            Array or sequence containing the data.

        %(Spectral)s

        %(PSD)s

        mode : {'default', 'psd', 'magnitude', 'angle', 'phase'}
            What sort of spectrum to use.  Default is 'psd', which takes the
            power spectral density.  'magnitude' returns the magnitude
            spectrum.  'angle' returns the phase spectrum without unwrapping.
            'phase' returns the phase spectrum with unwrapping.

        noverlap : int, default: 128
            The number of points of overlap between blocks.

        scale : {'default', 'linear', 'dB'}
            The scaling of the values in the *spec*.  'linear' is no scaling.
            'dB' returns the values in dB scale.  When *mode* is 'psd',
            this is dB power (10 * log10).  Otherwise this is dB amplitude
            (20 * log10). 'default' is 'dB' if *mode* is 'psd' or
            'magnitude' and 'linear' otherwise.  This must be 'linear'
            if *mode* is 'angle' or 'phase'.

        Fc : int, default: 0
            The center frequency of *x*, which offsets the x extents of the
            plot to reflect the frequency range used when a signal is acquired
            and then filtered and downsampled to baseband.

        cmap : `.Colormap`, default: :rc:`image.cmap`

        xextent : *None* or (xmin, xmax)
            The image extent along the x-axis. The default sets *xmin* to the
            left border of the first bin (*spectrum* column) and *xmax* to the
            right border of the last bin. Note that for *noverlap>0* the width
            of the bins is smaller than those of the segments.

        **kwargs
            Additional keyword arguments are passed on to `~.axes.Axes.imshow`
            which makes the specgram image. The origin keyword argument
            is not supported.

        Returns
        -------
        spectrum : 2D array
            Columns are the periodograms of successive segments.

        freqs : 1-D array
            The frequencies corresponding to the rows in *spectrum*.

        t : 1-D array
            The times corresponding to midpoints of segments (i.e., the columns
            in *spectrum*).

        im : `.AxesImage`
            The image created by imshow containing the spectrogram.

        See Also
        --------
        psd
            Differs in the default overlap; in returning the mean of the
            segment periodograms; in not returning times; and in generating a
            line plot instead of colormap.
        magnitude_spectrum
            A single spectrum, similar to having a single segment when *mode*
            is 'magnitude'. Plots a line instead of a colormap.
        angle_spectrum
            A single spectrum, similar to having a single segment when *mode*
            is 'angle'. Plots a line instead of a colormap.
        phase_spectrum
            A single spectrum, similar to having a single segment when *mode*
            is 'phase'. Plots a line instead of a colormap.

        Notes
        -----
        The parameters *detrend* and *scale_by_freq* do only apply when *mode*
        is set to 'psd'.
        """
    ...


@_copy_docstring_and_deprecators(Axes.spy)
def spy(Z: Any,
        precision: int = 0,
        marker: Any = None,
        markersize: Any = None,
        aspect: str = 'equal',
        origin: str = 'upper',
        **kwargs) -> ScalarMappable: """
        Plot the sparsity pattern of a 2D array.

        This visualizes the non-zero values of the array.

        Two plotting styles are available: image and marker. Both
        are available for full arrays, but only the marker style
        works for `scipy.sparse.spmatrix` instances.

        **Image style**

        If *marker* and *markersize* are *None*, `~.Axes.imshow` is used. Any
        extra remaining keyword arguments are passed to this method.

        **Marker style**

        If *Z* is a `scipy.sparse.spmatrix` or *marker* or *markersize* are
        *None*, a `.Line2D` object will be returned with the value of marker
        determining the marker type, and any remaining keyword arguments
        passed to `~.Axes.plot`.

        Parameters
        ----------
        Z : (M, N) array-like
            The array to be plotted.

        precision : float or 'present', default: 0
            If *precision* is 0, any non-zero value will be plotted. Otherwise,
            values of :math:`|Z| > precision` will be plotted.

            For `scipy.sparse.spmatrix` instances, you can also
            pass 'present'. In this case any value present in the array
            will be plotted, even if it is identically zero.

        aspect : {'equal', 'auto', None} or float, default: 'equal'
            The aspect ratio of the Axes.  This parameter is particularly
            relevant for images since it determines whether data pixels are
            square.

            This parameter is a shortcut for explicitly calling
            `.Axes.set_aspect`. See there for further details.

            - 'equal': Ensures an aspect ratio of 1. Pixels will be square.
            - 'auto': The Axes is kept fixed and the aspect is adjusted so
              that the data fit in the Axes. In general, this will result in
              non-square pixels.
            - *None*: Use :rc:`image.aspect`.

        origin : {'upper', 'lower'}, default: :rc:`image.origin`
            Place the [0, 0] index of the array in the upper left or lower left
            corner of the Axes. The convention 'upper' is typically used for
            matrices and images.

        Returns
        -------
        `~matplotlib.image.AxesImage` or `.Line2D`
            The return type depends on the plotting style (see above).

        Other Parameters
        ----------------
        **kwargs
            The supported additional parameters depend on the plotting style.

            For the image style, you can pass the following additional
            parameters of `~.Axes.imshow`:

            - *cmap*
            - *alpha*
            - *url*
            - any `.Artist` properties (passed on to the `.AxesImage`)

            For the marker style, you can pass any `.Line2D` property except
            for *linestyle*:

            %(Line2D_kwdoc)s
        """
    ...


@_copy_docstring_and_deprecators(Axes.stackplot)
def stackplot(*args,
              x: Any,
              labels: tuple = (),
              colors: Any = None,
              baseline: str = 'zero',
              data: Any = None,
              **kwargs) -> Any: ...


@_copy_docstring_and_deprecators(Axes.stem)
def stem(*args,
         linefmt: Any = None,
         markerfmt: Any = None,
         basefmt: Any = None,
         bottom: int = 0,
         label: Any = None,
         use_line_collection: bool = True,
         orientation: str = 'vertical',
         data: Any = None) -> Any: """
        Create a stem plot.

        A stem plot draws lines perpendicular to a baseline at each location
        *locs* from the baseline to *heads*, and places a marker there. For
        vertical stem plots (the default), the *locs* are *x* positions, and
        the *heads* are *y* values. For horizontal stem plots, the *locs* are
        *y* positions, and the *heads* are *x* values.

        Call signature::

          stem([locs,] heads, linefmt=None, markerfmt=None, basefmt=None)

        The *locs*-positions are optional. The formats may be provided either
        as positional or as keyword-arguments.

        Parameters
        ----------
        locs : array-like, default: (0, 1, ..., len(heads) - 1)
            For vertical stem plots, the x-positions of the stems.
            For horizontal stem plots, the y-positions of the stems.

        heads : array-like
            For vertical stem plots, the y-values of the stem heads.
            For horizontal stem plots, the x-values of the stem heads.

        linefmt : str, optional
            A string defining the color and/or linestyle of the vertical lines:

            =========  =============
            Character  Line Style
            =========  =============
            ``'-'``    solid line
            ``'--'``   dashed line
            ``'-.'``   dash-dot line
            ``':'``    dotted line
            =========  =============

            Default: 'C0-', i.e. solid line with the first color of the color
            cycle.

            Note: Markers specified through this parameter (e.g. 'x') will be
            silently ignored (unless using ``use_line_collection=False``).
            Instead, markers should be specified using *markerfmt*.

        markerfmt : str, optional
            A string defining the color and/or shape of the markers at the stem
            heads.  Default: 'C0o', i.e. filled circles with the first color of
            the color cycle.

        basefmt : str, default: 'C3-' ('C2-' in classic mode)
            A format string defining the properties of the baseline.

        orientation : str, default: 'vertical'
            If 'vertical', will produce a plot with stems oriented vertically,
            otherwise the stems will be oriented horizontally.

        bottom : float, default: 0
            The y/x-position of the baseline (depending on orientation).

        label : str, default: None
            The label to use for the stems in legends.

        use_line_collection : bool, default: True
            If ``True``, store and plot the stem lines as a
            `~.collections.LineCollection` instead of individual lines, which
            significantly increases performance.  If ``False``, defaults to the
            old behavior of using a list of `.Line2D` objects.  This parameter
            may be deprecated in the future.

        Returns
        -------
        `.StemContainer`
            The container may be treated like a tuple
            (*markerline*, *stemlines*, *baseline*)

        Notes
        -----
        .. seealso::
            The MATLAB function
            `stem <https://www.mathworks.com/help/matlab/ref/stem.html>`_
            which inspired this method.
        """
    ...


@_copy_docstring_and_deprecators(Axes.step)
def step(*args,
         x: Any,
         y: Any,
         where: str = 'pre',
         data: Any = None,
         **kwargs) -> Any: """
        Make a step plot.

        Call signatures::

            step(x, y, [fmt], *, data=None, where='pre', **kwargs)
            step(x, y, [fmt], x2, y2, [fmt2], ..., *, where='pre', **kwargs)

        This is just a thin wrapper around `.plot` which changes some
        formatting options. Most of the concepts and parameters of plot can be
        used here as well.

        .. note::

            This method uses a standard plot with a step drawstyle: The *x*
            values are the reference positions and steps extend left/right/both
            directions depending on *where*.

            For the common case where you know the values and edges of the
            steps, use `~.Axes.stairs` instead.

        Parameters
        ----------
        x : array-like
            1D sequence of x positions. It is assumed, but not checked, that
            it is uniformly increasing.

        y : array-like
            1D sequence of y levels.

        fmt : str, optional
            A format string, e.g. 'g' for a green line. See `.plot` for a more
            detailed description.

            Note: While full format strings are accepted, it is recommended to
            only specify the color. Line styles are currently ignored (use
            the keyword argument *linestyle* instead). Markers are accepted
            and plotted on the given positions, however, this is a rarely
            needed feature for step plots.

        data : indexable object, optional
            An object with labelled data. If given, provide the label names to
            plot in *x* and *y*.

        where : {'pre', 'post', 'mid'}, default: 'pre'
            Define where the steps should be placed:

            - 'pre': The y value is continued constantly to the left from
              every *x* position, i.e. the interval ``(x[i-1], x[i]]`` has the
              value ``y[i]``.
            - 'post': The y value is continued constantly to the right from
              every *x* position, i.e. the interval ``[x[i], x[i+1])`` has the
              value ``y[i]``.
            - 'mid': Steps occur half-way between the *x* positions.

        Returns
        -------
        list of `.Line2D`
            Objects representing the plotted data.

        Other Parameters
        ----------------
        **kwargs
            Additional parameters are the same as those for `.plot`.

        Notes
        -----
        .. [notes section required to get data note injection right]
        """
    ...


@_copy_docstring_and_deprecators(Axes.streamplot)
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


@_copy_docstring_and_deprecators(Axes.table)
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


@_copy_docstring_and_deprecators(Axes.text)
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
         **kwargs) -> Any: """
        Add text to the Axes.

        Add the text *s* to the Axes at location *x*, *y* in data coordinates.

        Parameters
        ----------
        x, y : float
            The position to place the text. By default, this is in data
            coordinates. The coordinate system can be changed using the
            *transform* parameter.

        s : str
            The text.

        fontdict : dict, default: None
            A dictionary to override the default text properties. If fontdict
            is None, the defaults are determined by `.rcParams`.

        Returns
        -------
        `.Text`
            The created `.Text` instance.

        Other Parameters
        ----------------
        **kwargs : `~matplotlib.text.Text` properties.
            Other miscellaneous text parameters.

            %(Text_kwdoc)s

        Examples
        --------
        Individual keyword arguments can be used to override any given
        parameter::

            >>> text(x, y, s, fontsize=12)

        The default transform specifies that text is in data coords,
        alternatively, you can specify text in axis coords ((0, 0) is
        lower-left and (1, 1) is upper-right).  The example below places
        text in the center of the Axes::

            >>> text(0.5, 0.5, 'matplotlib', horizontalalignment='center',
            ...      verticalalignment='center', transform=ax.transAxes)

        You can put a rectangular box around the text instance (e.g., to
        set a background color) by using the keyword *bbox*.  *bbox* is
        a dictionary of `~matplotlib.patches.Rectangle`
        properties.  For example::

            >>> text(x, y, s, bbox=dict(facecolor='red', alpha=0.5))
        """
    ...


@_copy_docstring_and_deprecators(Axes.tick_params)
def tick_params(axis: str = 'both',
                **kwargs) -> Any: ...


@_copy_docstring_and_deprecators(Axes.ticklabel_format)
def ticklabel_format(*,
                     axis: str = 'both',
                     style: str = '',
                     scilimits: Any = None,
                     useOffset: Any = None,
                     useLocale: Any = None,
                     useMathText: Any = None) -> Any: ...


@_copy_docstring_and_deprecators(Axes.tricontour)
def tricontour(*args,
               **kwargs) -> Any: ...


@_copy_docstring_and_deprecators(Axes.tricontourf)
def tricontourf(*args,
                **kwargs) -> Any: ...


@_copy_docstring_and_deprecators(Axes.tripcolor)
def tripcolor(*args,
              alpha: float = 1.0,
              norm: Any = None,
              cmap: Any = None,
              vmin: Any = None,
              vmax: Any = None,
              shading: str = 'flat',
              facecolors: Any = None,
              **kwargs) -> Any: ...


@_copy_docstring_and_deprecators(Axes.triplot)
def triplot(*args,
            **kwargs) -> Any: ...


@_copy_docstring_and_deprecators(Axes.violinplot)
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
               data: Any = None) -> Any: """
        Make a violin plot.

        Make a violin plot for each column of *dataset* or each vector in
        sequence *dataset*.  Each filled area extends to represent the
        entire data range, with optional lines at the mean, the median,
        the minimum, the maximum, and user-specified quantiles.

        Parameters
        ----------
        dataset : Array or a sequence of vectors.
          The input data.

        positions : array-like, default: [1, 2, ..., n]
          The positions of the violins. The ticks and limits are
          automatically set to match the positions.

        vert : bool, default: True.
          If true, creates a vertical violin plot.
          Otherwise, creates a horizontal violin plot.

        widths : array-like, default: 0.5
          Either a scalar or a vector that sets the maximal width of
          each violin. The default is 0.5, which uses about half of the
          available horizontal space.

        showmeans : bool, default: False
          If `True`, will toggle rendering of the means.

        showextrema : bool, default: True
          If `True`, will toggle rendering of the extrema.

        showmedians : bool, default: False
          If `True`, will toggle rendering of the medians.

        quantiles : array-like, default: None
          If not None, set a list of floats in interval [0, 1] for each violin,
          which stands for the quantiles that will be rendered for that
          violin.

        points : int, default: 100
          Defines the number of points to evaluate each of the
          gaussian kernel density estimations at.

        bw_method : str, scalar or callable, optional
          The method used to calculate the estimator bandwidth.  This can be
          'scott', 'silverman', a scalar constant or a callable.  If a
          scalar, this will be used directly as `kde.factor`.  If a
          callable, it should take a `GaussianKDE` instance as its only
          parameter and return a scalar. If None (default), 'scott' is used.

        Returns
        -------
        dict
          A dictionary mapping each component of the violinplot to a
          list of the corresponding collection instances created. The
          dictionary has the following keys:

          - ``bodies``: A list of the `~.collections.PolyCollection`
            instances containing the filled area of each violin.

          - ``cmeans``: A `~.collections.LineCollection` instance that marks
            the mean values of each of the violin's distribution.

          - ``cmins``: A `~.collections.LineCollection` instance that marks
            the bottom of each violin's distribution.

          - ``cmaxes``: A `~.collections.LineCollection` instance that marks
            the top of each violin's distribution.

          - ``cbars``: A `~.collections.LineCollection` instance that marks
            the centers of each violin's distribution.

          - ``cmedians``: A `~.collections.LineCollection` instance that
            marks the median values of each of the violin's distribution.

          - ``cquantiles``: A `~.collections.LineCollection` instance created
            to identify the quantile values of each of the violin's
            distribution.

        """
    ...


@_copy_docstring_and_deprecators(Axes.vlines)
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
           **kwargs) -> Any: """
        Plot vertical lines at each *x* from *ymin* to *ymax*.

        Parameters
        ----------
        x : float or array-like
            x-indexes where to plot the lines.

        ymin, ymax : float or array-like
            Respective beginning and end of each line. If scalars are
            provided, all lines will have same length.

        colors : list of colors, default: :rc:`lines.color`

        linestyles : {'solid', 'dashed', 'dashdot', 'dotted'}, optional

        label : str, default: ''

        Returns
        -------
        `~matplotlib.collections.LineCollection`

        Other Parameters
        ----------------
        **kwargs : `~matplotlib.collections.LineCollection` properties.

        See Also
        --------
        hlines : horizontal lines
        axvline : vertical line across the Axes
        """
    ...


@_copy_docstring_and_deprecators(Axes.xcorr)
def xcorr(x: Any,
          y: Any,
          normed: bool = True,
          detrend: (x: Any, axis: int),
          usevlines: bool = True,
          maxlags: int = 10,
          *,
          data: Any = None,
          **kwargs) -> Any: r"""
        Plot the cross correlation between *x* and *y*.

        The correlation with lag k is defined as
        :math:`\sum_n x[n+k] \cdot y^*[n]`, where :math:`y^*` is the complex
        conjugate of :math:`y`.

        Parameters
        ----------
        x, y : array-like of length n

        detrend : callable, default: `.mlab.detrend_none` (no detrending)
            A detrending function applied to *x* and *y*.  It must have the
            signature ::

                detrend(x: np.ndarray) -> np.ndarray

        normed : bool, default: True
            If ``True``, input vectors are normalised to unit length.

        usevlines : bool, default: True
            Determines the plot style.

            If ``True``, vertical lines are plotted from 0 to the xcorr value
            using `.Axes.vlines`. Additionally, a horizontal line is plotted
            at y=0 using `.Axes.axhline`.

            If ``False``, markers are plotted at the xcorr values using
            `.Axes.plot`.

        maxlags : int, default: 10
            Number of lags to show. If None, will return all ``2 * len(x) - 1``
            lags.

        Returns
        -------
        lags : array (length ``2*maxlags+1``)
            The lag vector.
        c : array  (length ``2*maxlags+1``)
            The auto correlation vector.
        line : `.LineCollection` or `.Line2D`
            `.Artist` added to the Axes of the correlation:

            - `.LineCollection` if *usevlines* is True.
            - `.Line2D` if *usevlines* is False.
        b : `.Line2D` or None
            Horizontal line at 0 if *usevlines* is True
            None *usevlines* is False.

        Other Parameters
        ----------------
        linestyle : `.Line2D` property, optional
            The linestyle for plotting the data points.
            Only used if *usevlines* is ``False``.

        marker : str, default: 'o'
            The marker for plotting the data points.
            Only used if *usevlines* is ``False``.

        **kwargs
            Additional parameters are passed to `.Axes.vlines` and
            `.Axes.axhline` if *usevlines* is ``True``; otherwise they are
            passed to `.Axes.plot`.

        Notes
        -----
        The cross correlation is performed with `numpy.correlate` with
        ``mode = "full"``.
        """
    ...


@_copy_docstring_and_deprecators(Axes._sci)
def sci(im: ScalarMappable) -> Any: ...


@_copy_docstring_and_deprecators(Axes.set_title)
def title(label: Any,
          fontdict: Any = None,
          loc: Any = None,
          pad: Any = None,
          *,
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
          **kwargs) -> Any: """
        Set a title for the Axes.

        Set one of the three available Axes titles. The available titles
        are positioned above the Axes in the center, flush with the left
        edge, and flush with the right edge.

        Parameters
        ----------
        label : str
            Text to use for the title

        fontdict : dict
            A dictionary controlling the appearance of the title text,
            the default *fontdict* is::

               {'fontsize': rcParams['axes.titlesize'],
                'fontweight': rcParams['axes.titleweight'],
                'color': rcParams['axes.titlecolor'],
                'verticalalignment': 'baseline',
                'horizontalalignment': loc}

        loc : {'center', 'left', 'right'}, default: :rc:`axes.titlelocation`
            Which title to set.

        y : float, default: :rc:`axes.titley`
            Vertical Axes loation for the title (1.0 is the top).  If
            None (the default), y is determined automatically to avoid
            decorators on the Axes.

        pad : float, default: :rc:`axes.titlepad`
            The offset of the title from the top of the Axes, in points.

        Returns
        -------
        `.Text`
            The matplotlib text instance representing the title

        Other Parameters
        ----------------
        **kwargs : `.Text` properties
            Other keyword arguments are text properties, see `.Text` for a list
            of valid text properties.
        """
    ...


@_copy_docstring_and_deprecators(Axes.set_xlabel)
def xlabel(xlabel: Any,
           fontdict: Any = None,
           labelpad: Any = None,
           *,
           loc: Any = None,
           **kwargs) -> Any: ...


@_copy_docstring_and_deprecators(Axes.set_ylabel)
def ylabel(ylabel: Any,
           fontdict: Any = None,
           labelpad: Any = None,
           *,
           loc: Any = None,
           **kwargs) -> Any: ...


@_copy_docstring_and_deprecators(Axes.set_xscale)
def xscale(value: Any,
           **kwargs) -> Any: ...


@_copy_docstring_and_deprecators(Axes.set_yscale)
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