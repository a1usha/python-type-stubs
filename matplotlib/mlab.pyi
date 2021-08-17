from typing import Any
from typing import Callable
from typing import Iterable
from typing import Optional
from typing import Tuple
from typing import Union

from matplotlib.mlab import GaussianKDE
from numpy.core._multiarray_umath import ndarray
from object import object


def window_hanning(x: {__len__}) -> Optional[Any]: ...


def window_none(x: Any) -> Any: ...


def detrend(x: Union[ndarray, Iterable, int, float],
            key: str = None,
            axis: int = None) -> Any: ...


def detrend_mean(x: Union[ndarray, Iterable, int, float],
                 axis: int = None) -> None: ...


def detrend_none(x: Any,
                 axis: int = None) -> Any: ...


def detrend_linear(y: Any) -> Optional[ndarray]: ...


def stride_windows(x: int,
                   n: int,
                   noverlap: int = None,
                   axis: int = 0) -> Optional[ndarray]: ...


def _spectral_helper(x: Union[{__len__}, ndarray, Iterable, int, float],
                     y: Optional[Any] = None,
                     NFFT: int = None,
                     Fs: int = None,
                     detrend_func: (x: Any, axis: int),
                     window: (x: {__len__}),
                     noverlap: int = None,
                     pad_to: int = None,
                     sides: str = None,
                     scale_by_freq: bool = None,
                     mode: Union[{__ne__}, str] = None) -> Tuple[
    Union[ndarray, int, float, complex], Optional[ndarray], None]: ...


def _single_spectrum_helper(mode: {__ne__},
                            x: {__len__},
                            Fs: Any = None,
                            window: Any = None,
                            pad_to: Any = None,
                            sides: Any = None) -> Tuple[
    Union[None, ndarray, int, float, complex], Optional[ndarray]]: ...


def psd(x: Any,
        NFFT: int = None,
        Fs: int = None,
        detrend: (x: Any, axis: int),
        window: (x: {__len__}),
        noverlap: int = None,
        pad_to: Any = None,
        sides: str = None,
        scale_by_freq: Any = None) -> Any: ...


def csd(x: Any,
        y: Any,
        NFFT: int = None,
        Fs: int = None,
        detrend: (x: Any, axis: int),
        window: (x: {__len__}),
        noverlap: int = None,
        pad_to: Any = None,
        sides: str = None,
        scale_by_freq: Any = None) -> Any: ...


def specgram(x: Union[ndarray, Iterable, int, float],
             NFFT: Any = None,
             Fs: Any = None,
             detrend: Any = None,
             window: Any = None,
             noverlap: int = None,
             pad_to: Any = None,
             sides: Any = None,
             scale_by_freq: Any = None,
             mode: str = None) -> Any: ...


def cohere(x: {__len__},
           y: Any,
           NFFT: int = 256,
           Fs: int = 2,
           detrend: (x: Any, axis: int),
           window: (x: {__len__}),
           noverlap: int = 0,
           pad_to: Any = None,
           sides: str = 'default',
           scale_by_freq: Any = None) -> Any: ...


class GaussianKDE(object):
    def __init__(self: GaussianKDE,
                 dataset: Union[ndarray, Iterable, int, float],
                 bw_method: Union[str, int, float, complex, Callable, None] = None) -> Any: ...

    def scotts_factor(self: GaussianKDE) -> None: ...

    def silverman_factor(self: GaussianKDE) -> None: ...

    def evaluate(self: GaussianKDE,
                 points: Any) -> Any: ...
