from matplotlib import docstring as docstring
from matplotlib import _api as _api
from numbers import Number as Number
from typing import Any
from typing import Callable
from typing import ClassVar
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


def detrend_linear(y: Any) -> Union[Optional[ndarray], Any]: ...


def stride_windows(x: int,
                   n: int,
                   noverlap: int = None,
                   axis: int = 0) -> Union[Optional[ndarray], Any]: ...


def _spectral_helper(x: Union[Union[{__len__}, ndarray, Iterable, int, float], Any],
                     y: Optional[Any] = None,
                     NFFT: Union[int, Any] = None,
                     Fs: Union[int, Any] = None,
                     detrend_func: Union[Callable[[Any, int], Any], Any] = None,
                     window: Union[Callable[[{__len__}], Optional[Any]], Any] = None,
                     noverlap: Union[int, Any] = None,
                     pad_to: Union[int, Any] = None,
                     sides: Union[str, Any] = None,
                     scale_by_freq: Union[bool, Any] = None,
                     mode: Union[Union[{__ne__}, str], Any] = None) -> Tuple[
    Union[Union[ndarray, int, float, complex], Any], Optional[ndarray], None]: ...


def _single_spectrum_helper(mode: {__ne__},
                            x: {__len__},
                            Fs: Any = None,
                            window: Any = None,
                            pad_to: Any = None,
                            sides: Any = None) -> Tuple[
    Union[Union[None, ndarray, int, float, complex], Any], Optional[ndarray]]: ...


def psd(x: Any,
        NFFT: Union[int, Any] = None,
        Fs: Union[int, Any] = None,
        detrend: Union[Callable[[Any, int], Any], Any] = None,
        window: Union[Callable[[{__len__}], Optional[Any]], Any] = None,
        noverlap: int = None,
        pad_to: Any = None,
        sides: Union[str, Any] = None,
        scale_by_freq: Any = None) -> Any: ...


_single_spectrum_docs: str

complex_spectrum: partial[tuple[Union[Union[None, ndarray, int, float, complex], Any], Optional[ndarray]]]

__doc__: str
__doc__: str
__doc__: str
__doc__: str

magnitude_spectrum: partial[tuple[Union[Union[None, ndarray, int, float, complex], Any], Optional[ndarray]]]

__doc__: str
__doc__: str
__doc__: str
__doc__: str

angle_spectrum: partial[tuple[Union[Union[None, ndarray, int, float, complex], Any], Optional[ndarray]]]

__doc__: str
__doc__: str
__doc__: str
__doc__: str

phase_spectrum: partial[tuple[Union[Union[None, ndarray, int, float, complex], Any], Optional[ndarray]]]

__doc__: str
__doc__: str
__doc__: str
__doc__: str


def csd(x: Any,
        y: Any,
        NFFT: Union[int, Any] = None,
        Fs: Union[int, Any] = None,
        detrend: Union[Callable[[Any, int], Any], Any] = None,
        window: Union[Callable[[{__len__}], Optional[Any]], Any] = None,
        noverlap: int = None,
        pad_to: Any = None,
        sides: Union[str, Any] = None,
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
           detrend: Callable[[Any, int], Any] = detrend_none,
           window: Callable[[{__len__}], Optional[Any]] = window_hanning,
           noverlap: int = 0,
           pad_to: Any = None,
           sides: str = 'default',
           scale_by_freq: Any = None) -> Any: ...


class GaussianKDE(object):
    covariance_factor: ClassVar[Callable[[GaussianKDE], None]]
    __call__: ClassVar[Callable[[GaussianKDE, Any], Any]]
    data_covariance: Union[list[Any], Any]
    inv_cov: Union[Union[None, float, complex], Any]
    data_inv_cov: Union[ndarray, Any]
    norm_factor: Any
    dim: Any
    _bw_method: Callable
    covariance: Union[Union[list[Any], float, complex], Any]
    covariance_factor: Callable[[], Any]
    factor: Union[Union[None, str, int, float, complex, Callable], Any]
    dataset: Union[list[Any], Any]
    num_dp: Any

    def __init__(self: GaussianKDE,
                 dataset: Union[ndarray, Iterable, int, float],
                 bw_method: Union[str, int, float, complex, Callable, None] = None) -> Any: ...

    def scotts_factor(self: GaussianKDE) -> None: ...

    def silverman_factor(self: GaussianKDE) -> None: ...

    def evaluate(self: GaussianKDE,
                 points: Any) -> Any: ...
