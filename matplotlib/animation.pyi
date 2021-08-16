from typing import Any
from typing import Callable
from typing import Iterable
from typing import Optional
from typing import Union
from typing import tuple

from matplotlib.animation import MovieWriter


def adjusted_figsize(w: float,
                     h: float,
                     dpi: float,
                     n: int) -> float: ...


class MovieWriterRegistry(object):
    def __init__(self: MovieWriterRegistry) -> None: ...

    def register(self: MovieWriterRegistry,
                 name: str) -> (writer_cls: Any) ->

    def is_available(self: MovieWriterRegistry,
                     name: str) -> bool: ...

    def __iter__(self: MovieWriterRegistry) -> Generator[Any, Any, None]: ...

    def list(self: MovieWriterRegistry) -> list: ...

    def __getitem__(self: MovieWriterRegistry,
                    name: Any) -> Any: ...


class AbstractMovieWriter(ABC):
    def __init__(self: AbstractMovieWriter,
                 fps: int = 5,
                 metadata: Any = None,
                 codec: Any = None,
                 bitrate: Any = None) -> None: ...

    @abc.abstractmethod
    def setup(self: AbstractMovieWriter,
              fig: Any,
              outfile: str,
              dpi: float = None) -> Any: ...

    @property
    def frame_size(self: AbstractMovieWriter) -> tuple[int, int]: ...

    @abc.abstractmethod
    def grab_frame(self: AbstractMovieWriter,
                   **kwargs) -> Any: ...

    @abc.abstractmethod
    def finish(self: AbstractMovieWriter) -> Any: ...

    @contextlib.contextmanager
    def saving(self: AbstractMovieWriter,
               fig: Any,
               outfile: Any,
               dpi: Any,
               *args,
               **kwargs) -> Generator[AbstractMovieWriter, Any, None]: ...


class MovieWriter(AbstractMovieWriter):
    def __init__(self: MovieWriter,
                 fps: int = 5,
                 codec: Optional[str] = None,
                 bitrate: int = None,
                 extra_args: Optional[Iterable[str]] = None,
                 metadata: Any = None) -> Any: ...

    def _adjust_frame_size(self: MovieWriter) -> tuple[Any, Any]: ...

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

    @classmethod
    def bin_path(cls: Type[MovieWriter]) -> str: ...

    @classmethod
    def isAvailable(cls: Type[MovieWriter]) -> Any: ...


class FileMovieWriter(MovieWriter):
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
    @property
    def clear_temp(self: FileMovieWriter) -> Optional[bool]: ...

    @clear_temp.setter
    def clear_temp(self: FileMovieWriter,
                   value: Any) -> None: ...

    @property
    def frame_format(self: FileMovieWriter) -> Any: ...

    @frame_format.setter
    def frame_format(self: FileMovieWriter,
                     frame_format: Any) -> None: ...

    def _base_temp_name(self: FileMovieWriter) -> str: ...

    def grab_frame(self: FileMovieWriter,
                   **kwargs) -> None: ...

    def finish(self: FileMovieWriter) -> None: ...

    def _cleanup(self: FileMovieWriter) -> None: ...


@writers.register('pillow')
class PillowWriter(AbstractMovieWriter):
    @classmethod
    def isAvailable(cls: Type[PillowWriter]) -> bool: ...

    def setup(self: PillowWriter,
              fig: Any,
              outfile: str,
              dpi: float = None) -> None: ...

    def grab_frame(self: PillowWriter,
                   **kwargs) -> None: ...

    def finish(self: PillowWriter) -> None: ...


class FFMpegBase(object):
    @property
    def output_args(self: FFMpegBase) -> list[str]: ...

    @classmethod
    def isAvailable(cls: Type[FFMpegBase]) -> Any: ...


@writers.register('ffmpeg')
class FFMpegWriter(FFMpegBase, MovieWriter):
    def _args(self: FFMpegWriter) -> list[str]: ...


@writers.register('ffmpeg_file')
class FFMpegFileWriter(FFMpegBase, FileMovieWriter):
    def _args(self: FFMpegFileWriter) -> list[str]: ...


@_api.deprecated('3.3')
class AVConvBase(FFMpegBase):
    pass


@writers.register('avconv')
class AVConvWriter(AVConvBase, FFMpegWriter):
    pass


@writers.register('avconv_file')
class AVConvFileWriter(AVConvBase, FFMpegFileWriter):
    pass


class ImageMagickBase(object):
    @property
    def delay(self: ImageMagickBase) -> float: ...

    @property
    def output_args(self: ImageMagickBase) -> list: ...

    @classmethod
    def bin_path(cls: Type[ImageMagickBase]) -> Any: ...

    @classmethod
    def isAvailable(cls: Type[ImageMagickBase]) -> bool: ...


@writers.register('imagemagick')
class ImageMagickWriter(ImageMagickBase, MovieWriter):
    def _args(self: ImageMagickWriter) -> list[str]: ...


@writers.register('imagemagick_file')
class ImageMagickFileWriter(ImageMagickBase, FileMovieWriter):
    def _args(self: ImageMagickFileWriter) -> list[str]: ...


def _included_frames(paths: list,
                     frame_format: Any) -> str: ...


def _embedded_frames(frame_list: list,
                     frame_format: {__eq__}) -> str: ...


@writers.register('html')
class HTMLWriter(FileMovieWriter):
    @classmethod
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

    def new_frame_seq(self: Animation) -> Iterator: ...

    def new_saved_frame_seq(self: Animation) -> Iterator: ...

    def _draw_next_frame(self: Animation,
                         framedata: Any,
                         blit: bool) -> None: ...

    def _init_draw(self: Animation) -> None: ...

    def _pre_draw(self: Animation,
                  framedata: Any,
                  blit: Any) -> None: ...

    def _draw_frame(self: Animation,
                    framedata: Any) -> Any: ...

    def _post_draw(self: Animation,
                   framedata: Optional[Any],
                   blit: bool) -> None: ...

    def _blit_draw(self: Animation,
                   artists: list) -> None: ...

    def _blit_clear(self: Animation,
                    artists: list) -> None: ...

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

    def new_frame_seq(self: FuncAnimation) -> Iterator: ...

    def new_saved_frame_seq(self: FuncAnimation) -> Union[Iterator, islice, Generator[Any, Any, None]]: ...

    def _init_draw(self: FuncAnimation) -> Any: ...

    def _draw_frame(self: FuncAnimation,
                    framedata: Any) -> Any: ...
