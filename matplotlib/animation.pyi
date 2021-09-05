from matplotlib import cbook as cbook
from matplotlib import _api as _api
from matplotlib._animation_data import STYLE_INCLUDE as STYLE_INCLUDE
from matplotlib._animation_data import JS_INCLUDE as JS_INCLUDE
from matplotlib._animation_data import INCLUDED_FRAMES as INCLUDED_FRAMES
from matplotlib._animation_data import DISPLAY_TEMPLATE as DISPLAY_TEMPLATE
from PIL import Image as Image
from tempfile import TemporaryDirectory as TemporaryDirectory
from pathlib import Path as Path
from io import TextIOWrapper as TextIOWrapper
from io import BytesIO as BytesIO
from abc import ABC
from itertools import islice
from typing import Any
from typing import Callable
from typing import ClassVar
from typing import Generator
from typing import Iterable
from typing import Iterator
from typing import Optional
from typing import Tuple
from typing import Type
from typing import Union

from matplotlib import _api
from matplotlib.animation import AbstractMovieWriter
from matplotlib.animation import Animation
from matplotlib.animation import ArtistAnimation
from matplotlib.animation import FFMpegBase
from matplotlib.animation import FFMpegFileWriter
from matplotlib.animation import FFMpegWriter
from matplotlib.animation import FileMovieWriter
from matplotlib.animation import FuncAnimation
from matplotlib.animation import HTMLWriter
from matplotlib.animation import ImageMagickBase
from matplotlib.animation import ImageMagickFileWriter
from matplotlib.animation import ImageMagickWriter
from matplotlib.animation import MovieWriter
from matplotlib.animation import MovieWriterRegistry
from matplotlib.animation import PillowWriter
from matplotlib.animation import TimedAnimation
from object import object


def adjusted_figsize(w: float,
                     h: float,
                     dpi: float,
                     n: int) -> float: ...


class MovieWriterRegistry(object):
    _registered: dict[Any, Any]

    def __init__(self: MovieWriterRegistry) -> None: ...

    def register(self: MovieWriterRegistry,
                 name: Union[str, Any]) -> Callable[[Any], Any]: ...

    def is_available(self: MovieWriterRegistry,
                     name: str) -> bool: ...

    def __iter__(self: MovieWriterRegistry) -> Generator[Any, Any, None]: ...

    def list(self: MovieWriterRegistry) -> list[Any]: ...

    def __getitem__(self: MovieWriterRegistry,
                    name: Any) -> Any: ...


writers: MovieWriterRegistry


class AbstractMovieWriter(ABC):
    codec: Union[Optional[str], Any]
    metadata: Union[dict[Any, Any], Any]
    fig: Any
    outfile: str
    fps: int
    bitrate: Optional[Any]
    dpi: Union[float, Any]

    def __init__(self: AbstractMovieWriter,
                 fps: int = 5,
                 metadata: Any = None,
                 codec: Any = None,
                 bitrate: Any = None) -> None: ...

    def setup(self: AbstractMovieWriter,
              fig: Any,
              outfile: str,
              dpi: float = None) -> Any: ...

    def frame_size(self: AbstractMovieWriter) -> Tuple[int, int]: ...

    def grab_frame(self: AbstractMovieWriter,
                   **kwargs) -> Any: ...

    def finish(self: AbstractMovieWriter) -> Any: ...

    def saving(self: AbstractMovieWriter,
               fig: Any,
               outfile: Any,
               dpi: Any,
               *args,
               **kwargs) -> Union[Generator[AbstractMovieWriter, Any, None], Any]: ...


class MovieWriter(AbstractMovieWriter):
    exec_key: ClassVar[deprecate_privatize_attribute]
    args_key: ClassVar[deprecate_privatize_attribute]
    supported_formats: ClassVar[list[str]]
    frame_format: str
    extra_args: Optional[Iterable[str]]
    _w: Any
    _h: Any
    _proc: Union[Popen[str], Popen[bytes], Popen[Any]]

    def __init__(self: MovieWriter,
                 fps: int = 5,
                 codec: Optional[str] = None,
                 bitrate: int = None,
                 extra_args: Optional[Iterable[str]] = None,
                 metadata: Any = None) -> Any: ...

    def _adjust_frame_size(self: MovieWriter) -> Tuple[Any, Any]: ...

    def setup(self: MovieWriter,
              fig: Any,
              outfile: str,
              dpi: float = None) -> None: ...

    def _run(self: MovieWriter) -> None: ...

    def finish(self: MovieWriter) -> None: ...

    def grab_frame(self: MovieWriter,
                   **kwargs) -> None: ...

    def _args(self: MovieWriter) -> NotImplementedError: ...

    def _cleanup(self: MovieWriter) -> Any: ...

    @_api.deprecated("3.4")
    def cleanup(self: MovieWriter) -> Optional[Any]: ...

    def bin_path(cls: Type[MovieWriter]) -> str: ...

    def isAvailable(cls: Type[MovieWriter]) -> Any: ...


class FileMovieWriter(MovieWriter):
    _temp_paths: list[Any]
    _tmpdir: Union[TemporaryDirectory[AnyStr], TemporaryDirectory[Union[Union[str, bytes], Any]]]
    frame_format: Optional[Any]
    _frame_format: Any
    fig: Any
    _clear_temp: Optional[bool]
    outfile: str
    fname_format_str: str
    _frame_counter: int
    temp_prefix: str
    dpi: Union[float, Any]

    def __init__(self: FileMovieWriter,
                 *args,
                 **kwargs) -> None: ...

    @_api.delete_parameter("3.3", "clear_temp")
    def setup(self: FileMovieWriter,
              fig: Any,
              outfile: str,
              dpi: float = None,
              frame_prefix: Optional[str] = None,
              clear_temp: Optional[bool] = True) -> Optional[Any]: ...

    def __del__(self: FileMovieWriter) -> None: ...

    @_api.deprecated("3.3")
    def clear_temp(self: FileMovieWriter) -> Optional[bool]: ...

    def clear_temp(self: FileMovieWriter,
                   value: Any) -> None: ...

    def frame_format(self: FileMovieWriter) -> Any: ...

    def frame_format(self: FileMovieWriter,
                     frame_format: Any) -> None: ...

    def _base_temp_name(self: FileMovieWriter) -> str: ...

    def grab_frame(self: FileMovieWriter,
                   **kwargs) -> None: ...

    def finish(self: FileMovieWriter) -> None: ...

    def _cleanup(self: FileMovieWriter) -> None: ...


class PillowWriter(AbstractMovieWriter):
    _frames: list[Any]

    def isAvailable(cls: Type[PillowWriter]) -> bool: ...

    def setup(self: PillowWriter,
              fig: Any,
              outfile: str,
              dpi: float = None) -> None: ...

    def grab_frame(self: PillowWriter,
                   **kwargs) -> None: ...

    def finish(self: PillowWriter) -> None: ...


class FFMpegBase(object):
    _exec_key: ClassVar[str]
    _args_key: ClassVar[str]
    codec: str

    def output_args(self: FFMpegBase) -> list[Union[str, Any]]: ...

    def isAvailable(cls: Type[FFMpegBase]) -> Any: ...


class FFMpegWriter(FFMpegBase, MovieWriter):
    def _args(self: FFMpegWriter) -> list[Union[str, Any]]: ...


class FFMpegFileWriter(FFMpegBase, FileMovieWriter):
    supported_formats: ClassVar[list[str]]

    def _args(self: FFMpegFileWriter) -> list[Union[str, Any]]: ...


@_api.deprecated('3.3')
class AVConvBase(FFMpegBase):
    _exec_key: ClassVar[str]
    _args_key: ClassVar[str]
    isAvailable: ClassVar[classmethod]
    pass


class AVConvWriter(AVConvBase, FFMpegWriter):
    pass


class AVConvFileWriter(AVConvBase, FFMpegFileWriter):
    pass


class ImageMagickBase(object):
    _exec_key: ClassVar[str]
    _args_key: ClassVar[str]

    def delay(self: ImageMagickBase) -> Union[float, Any]: ...

    def output_args(self: ImageMagickBase) -> list[Any]: ...

    def bin_path(cls: Type[ImageMagickBase]) -> Any: ...

    def isAvailable(cls: Type[ImageMagickBase]) -> Union[bool, Any]: ...


class ImageMagickWriter(ImageMagickBase, MovieWriter):
    def _args(self: ImageMagickWriter) -> list[Union[str, Any]]: ...


class ImageMagickFileWriter(ImageMagickBase, FileMovieWriter):
    supported_formats: ClassVar[list[str]]

    def _args(self: ImageMagickFileWriter) -> list[Union[str, Any]]: ...


def _included_frames(paths: Union[list[Any], Any],
                     frame_format: Any) -> str: ...


def _embedded_frames(frame_list: Union[list[Any], Any],
                     frame_format: {__eq__}) -> str: ...


class HTMLWriter(FileMovieWriter):
    supported_formats: ClassVar[list[str]]
    args_key: ClassVar[Union[_deprecated_property, Any]]
    _total_bytes: int
    _clear_temp: bool
    embed_frames: bool
    default_mode: str
    _saved_frames: list[Any]
    _bytes_limit: Any
    _hit_limit: bool

    def isAvailable(cls: Type[HTMLWriter]) -> bool: ...

    def __init__(self: HTMLWriter,
                 fps: int = 30,
                 codec: Any = None,
                 bitrate: Any = None,
                 extra_args: Any = None,
                 metadata: Any = None,
                 embed_frames: bool = False,
                 default_mode: str = 'loop',
                 embed_limit: Any = None) -> None: ...

    def setup(self: HTMLWriter,
              fig: Any,
              outfile: str,
              dpi: float,
              frame_dir: Any = None) -> None: ...

    def grab_frame(self: HTMLWriter,
                   **kwargs) -> None: ...

    def finish(self: HTMLWriter) -> None: ...


class Animation(object):
    _first_draw_id: Any
    _html_representation: str
    _fig: Any
    _close_id: Any
    event_source: Optional[object]
    _drawn_artists: list[Any]
    _video_size: str
    frame_seq: Iterator[Any]
    _blit_cache: dict[Any, Any]
    _resize_id: Any
    _blit: Union[bool, Any]
    _base64_video: str
    _draw_was_started: bool

    def __init__(self: Animation,
                 fig: Any,
                 event_source: Optional[object] = None,
                 blit: bool = False) -> None: ...

    def __del__(self: Animation) -> None: ...

    def _start(self: Animation,
               *args) -> None: ...

    def _stop(self: Animation,
              *args) -> None: ...

    def save(self: Animation,
             filename: str,
             writer: Union[MovieWriter, str] = None,
             fps: Optional[int] = None,
             dpi: float = None,
             codec: str = None,
             bitrate: int = None,
             extra_args: Optional[Iterable[str]] = None,
             metadata: Any = None,
             extra_anim: Iterable = None,
             savefig_kwargs: dict = None,
             *,
             progress_callback: Optional[function] = None) -> Any: ...

    def _step(self: Animation,
              *args) -> bool: ...

    def new_frame_seq(self: Animation) -> Iterator[Any]: ...

    def new_saved_frame_seq(self: Animation) -> Iterator[Any]: ...

    def _draw_next_frame(self: Animation,
                         framedata: Any,
                         blit: Union[bool, Any]) -> None: ...

    def _init_draw(self: Animation) -> None: ...

    def _pre_draw(self: Animation,
                  framedata: Any,
                  blit: Any) -> None: ...

    def _draw_frame(self: Animation,
                    framedata: Any) -> Any: ...

    def _post_draw(self: Animation,
                   framedata: Optional[Any],
                   blit: Union[bool, Any]) -> None: ...

    def _blit_draw(self: Animation,
                   artists: Union[list[Any], Any]) -> None: ...

    def _blit_clear(self: Animation,
                    artists: Union[list[Any], Any]) -> None: ...

    def _setup_blit(self: Animation) -> None: ...

    def _on_resize(self: Animation,
                   event: Any) -> None: ...

    def _end_redraw(self: Animation,
                    event: Any) -> None: ...

    def to_html5_video(self: Animation,
                       embed_limit: Optional[float] = None) -> str: ...

    def to_jshtml(self: Animation,
                  fps: Any = None,
                  embed_frames: bool = True,
                  default_mode: Any = None) -> str: ...

    def _repr_html_(self: Animation) -> str: ...

    def pause(self: Animation) -> None: ...

    def resume(self: Animation) -> None: ...


class TimedAnimation(Animation):
    _interval: int
    _repeat_delay: int
    repeat: bool
    frame_seq: Iterator[Any]

    def __init__(self: TimedAnimation,
                 fig: Any,
                 interval: int = 200,
                 repeat_delay: int = 0,
                 repeat: bool = True,
                 event_source: Optional[object] = None,
                 *args,
                 **kwargs) -> None: ...

    def _step(self: TimedAnimation,
              *args) -> bool: ...


class ArtistAnimation(TimedAnimation):
    _drawn_artists: list[Any]
    _framedata: Iterable

    def __init__(self: ArtistAnimation,
                 fig: Any,
                 artists: Iterable,
                 *args,
                 **kwargs) -> None: ...

    def _init_draw(self: ArtistAnimation) -> None: ...

    def _pre_draw(self: ArtistAnimation,
                  framedata: Any,
                  blit: Any) -> None: ...

    def _draw_frame(self: ArtistAnimation,
                    artists: {__iter__}) -> None: ...


class FuncAnimation(TimedAnimation):
    save_count: int
    _tee_from: Optional[int]
    _args: tuple
    _iter_gen: Callable[[], Iterator[Any]]
    _func: Callable
    _cache_frame_data: bool
    _init_func: Optional[Callable]
    _drawn_artists: Any
    _save_seq: list[Any]
    _old_saved_seq: list[Any]

    def __init__(self: FuncAnimation,
                 fig: Any,
                 func: Callable,
                 frames: Optional[int] = None,
                 init_func: Optional[Callable] = None,
                 fargs: Union[Iterable, tuple, None] = None,
                 save_count: int = None,
                 *,
                 cache_frame_data: bool = True,
                 **kwargs) -> None: ...

    def new_frame_seq(self: FuncAnimation) -> Iterator[Any]: ...

    def new_saved_frame_seq(self: FuncAnimation) -> Union[Iterator[Any], islice[Any], Generator[Any, Any, None]]: ...

    def _init_draw(self: FuncAnimation) -> Any: ...

    def _draw_frame(self: FuncAnimation,
                    framedata: Any) -> Any: ...
