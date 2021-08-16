from typing import Any
from typing import Callable
from typing import Iterable
from typing import Optional
from typing import Union

from matplotlib.backend_bases import MouseEvent
from numpy.core._multiarray_umath import ndarray


def allow_rasterization(draw: Any) -> (artist
: {get_rasterized, get_agg_filter, figure}, renderer: {_rasterizing}, args: tuple[Any, ...], kwargs: dict[str, Any]) ->


def _finalize_rasterization(draw: Any) -> (artist
: Any, renderer: {_rasterizing}, args: tuple[Any, ...], kwargs: dict[str, Any]) ->


def _stale_axes_callback(self: {axes},
                         val: Any) -> None: ...


class Artist(object):
    def __init__(self: Artist) -> None: ...

    def __getstate__(self: Artist) -> dict[str, Any]: ...

    def remove(self: Artist) -> Any: ...

    def have_units(self: Artist) -> bool: ...

    def convert_xunits(self: Artist,
                       x: Any) -> Any: ...

    def convert_yunits(self: Artist,
                       y: Any) -> Any: ...

    @property
    def axes(self: Artist) -> Any: ...

    @axes.setter
    def axes(self: Artist,
             new_axes: Optional[{__ne__}]) -> Any: ...

    @property
    def stale(self: Artist) -> bool: ...

    @stale.setter
    def stale(self: Artist,
              val: Any) -> None: ...

    def get_window_extent(self: Artist,
                          renderer: Any) -> Bbox: ...

    def _get_clipping_extent_bbox(self: Artist) -> Optional[Bbox]: ...

    def get_tightbbox(self: Artist,
                      renderer: Any) -> Any: ...

    def add_callback(self: Artist,
                     func: Callable) -> int: ...

    def remove_callback(self: Artist,
                        oid: Any) -> None: ...

    def pchanged(self: Artist) -> None: ...

    def is_transform_set(self: Artist) -> bool: ...

    def set_transform(self: Artist,
                      t: Any) -> None: ...

    def get_transform(self: Artist) -> IdentityTransform: ...

    def get_children(self: Artist) -> list: ...

    def _default_contains(self: Artist,
                          mouseevent: MouseEvent,
                          figure: Optional[{canvas}] = None) -> Union[tuple[bool, dict], tuple[None, dict]]: ...

    def contains(self: Artist,
                 mouseevent: MouseEvent) -> bool: ...

    @_api.deprecated("3.3", alternative="set_picker")
    def set_contains(self: Artist,
                     picker: Callable) -> Any: ...

    @_api.deprecated("3.3", alternative="get_picker")
    def get_contains(self: Artist) -> Any: ...

    def pickable(self: Artist) -> Any: ...

    def pick(self: Artist,
             mouseevent: {inaxes}) -> None: ...

    def set_picker(self: Artist,
                   picker: Union[None, bool, float, Callable]) -> None: ...

    def get_picker(self: Artist) -> Any: ...

    def get_url(self: Artist) -> Any: ...

    def set_url(self: Artist,
                url: str) -> None: ...

    def get_gid(self: Artist) -> Any: ...

    def set_gid(self: Artist,
                gid: str) -> None: ...

    def get_snap(self: Artist) -> bool: ...

    def set_snap(self: Artist,
                 snap: Optional[bool]) -> None: ...

    def get_sketch_params(self: Artist) -> Any: ...

    def set_sketch_params(self: Artist,
                          scale: Optional[float] = None,
                          length: Optional[float] = None,
                          randomness: Optional[float] = None) -> None: ...

    def set_path_effects(self: Artist,
                         path_effects: Any) -> None: ...

    def get_path_effects(self: Artist) -> Optional[Any]: ...

    def get_figure(self: Artist) -> Any: ...

    def set_figure(self: Artist,
                   fig: Any) -> None: ...

    def set_clip_box(self: Artist,
                     clipbox: Any) -> None: ...

    def set_clip_path(self: Artist,
                      path: Any,
                      transform: Any = None) -> Any: ...

    def get_alpha(self: Artist) -> Any: ...

    def get_visible(self: Artist) -> bool: ...

    def get_animated(self: Artist) -> bool: ...

    def get_in_layout(self: Artist) -> bool: ...

    def get_clip_on(self: Artist) -> bool: ...

    def get_clip_box(self: Artist) -> Any: ...

    def get_clip_path(self: Artist) -> Any: ...

    def get_transformed_clip_path_and_affine(self: Artist) -> tuple[None, None]: ...

    def set_clip_on(self: Artist,
                    b: bool) -> None: ...

    def _set_gc_clip(self: Artist,
                     gc: Any) -> None: ...

    def get_rasterized(self: Artist) -> bool: ...

    def set_rasterized(self: Artist,
                       rasterized: bool) -> None: ...

    def get_agg_filter(self: Artist) -> Any: ...

    def set_agg_filter(self: Artist,
                       filter_func: Callable) -> None: ...

    @_api.delete_parameter("3.3", "args")
    @_api.delete_parameter("3.3", "kwargs")
    def draw(self: Artist,
             renderer: Any,
             *args,
             **kwargs) -> Optional[Any]: ...

    def set_alpha(self: Artist,
                  alpha: Union[int, float, complex, None]) -> Any: ...

    def _set_alpha_for_array(self: Artist,
                             alpha: Union[ndarray, Iterable, int, float, complex, None]) -> None: ...

    def set_visible(self: Artist,
                    b: bool) -> None: ...

    def set_animated(self: Artist,
                     b: bool) -> None: ...

    def set_in_layout(self: Artist,
                      in_layout: bool) -> None: ...

    def update(self: Artist,
               props: dict) -> list[Optional[Any]]: ...

    def get_label(self: Artist) -> str: ...

    def set_label(self: Artist,
                  s: object) -> None: ...

    def get_zorder(self: Artist) -> Union[int, float]: ...

    def set_zorder(self: Artist,
                   level: float) -> None: ...

    @property
    def sticky_edges(self: Artist) -> _XYPair: ...

    def update_from(self: Artist,
                    other: {_transform, _transformSet, _visible, _alpha, clipbox, _clipon, _clippath, _label, _sketch,
                            _path_effects, sticky_edges}) -> None: ...

    def properties(self: Artist) -> dict[str, Any]: ...

    def set(self: Artist,
            **kwargs) -> list[Optional[Any]]: ...

    def findobj(self: Artist,
                match: Any = None,
                include_self: bool = True) -> Any: ...

    def get_cursor_data(self: Artist,
                        event: MouseEvent) -> None: ...

    def format_cursor_data(self: Artist,
                           data: {__getitem__}) -> str: ...

    @property
    def mouseover(self: Artist) -> bool: ...

    @mouseover.setter
    def mouseover(self: Artist,
                  val: Any) -> None: ...


class ArtistInspector(object):
    def __init__(self: ArtistInspector,
                 o: Any) -> None: ...

    def get_aliases(self: ArtistInspector) -> dict: ...

    def get_valid_values(self: ArtistInspector,
                         attr: str) -> Optional[str]: ...

    def _replace_path(self: ArtistInspector,
                      source_class: Any) -> Any: ...

    def get_setters(self: ArtistInspector) -> list[str]: ...

    def is_alias(self: ArtistInspector,
                 o: Union[Callable, Callable]) -> bool: ...

    def aliased_name(self: ArtistInspector,
                     s: str) -> str: ...

    def aliased_name_rest(self: ArtistInspector,
                          s: str,
                          target: Any) -> str: ...

    def pprint_setters(self: ArtistInspector,
                       prop: Any = None,
                       leadingspace: int = 2) -> Union[str, list[str]]: ...

    def pprint_setters_rest(self: ArtistInspector,
                            prop: Any = None,
                            leadingspace: int = 4) -> Union[str, list[str]]: ...

    def properties(self: ArtistInspector) -> dict[str, Any]: ...

    def pprint_getters(self: ArtistInspector) -> list[str]: ...


def getp(obj: Any,
         property: Optional[str] = None) -> Optional[Any]: ...


def setp(*args,
         obj: Any,
         file: Any = None,
         **kwargs) -> Optional[list[Optional[Any]]]: ...


def kwdoc(artist: Any) -> str: ...