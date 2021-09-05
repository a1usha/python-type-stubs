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
from object import object


def window_hanning(x: {__len__}) -> Any: ...


def window_none(x: Any) -> Any: ...


def detrend(x: Union[Union[Iterable, int, float], Any],
            key: str = None,
            axis: int = None) -> Any: ...


def detrend_mean(x: Union[Union[Iterable, int, float], Any],
                 axis: int = None) -> Any: ...


def detrend_none(x: Any,
                 axis: int = None) -> Any: ...


def detrend_linear(y: Any) -> Any: ...


def stride_windows(x: int,
                   n: int,
                   noverlap: int = None,
                   axis: int = 0) -> Any: ...


def _spectral_helper(x: Union[Union[{__len__}, Iterable, int, float], Any],
                     y: Optional[Any] = None,
                     NFFT: Union[int, Any] = None,
                     Fs: Union[int, Any] = None,
                     detrend_func: Union[Callable[[Any, int], Any], Any] = None,
                     window: Union[Callable[[{__len__}], Any], Any] = None,
                     noverlap: Union[int, Any] = None,
                     pad_to: Union[int, Any] = None,
                     sides: Union[str, Any] = None,
                     scale_by_freq: Union[bool, Any] = None,
                     mode: Union[Union[{__ne__}, str], Any] = None) -> Tuple[
    Union[Union[int, float, complex], Any], Any, Union[float, Any]]: ...


def _single_spectrum_helper(mode: {__ne__},
                            x: {__len__},
                            Fs: Any = None,
                            window: Any = None,
                            pad_to: Any = None,
                            sides: Any = None) -> Tuple[Union[Union[int, float, complex], Any], Any]: ...


def psd(x: Any,
        NFFT: Union[int, Any] = None,
        Fs: Union[int, Any] = None,
        detrend: Union[Callable[[Any, int], Any], Any] = None,
        window: Union[Callable[[{__len__}], Any], Any] = None,
        noverlap: int = None,
        pad_to: Any = None,
        sides: Union[str, Any] = None,
        scale_by_freq: Any = None) -> Any: ...


_single_spectrum_docs: str

complex_spectrum: partial[tuple[Union[Union[int, float, complex], Any], Any]]

magnitude_spectrum: partial[tuple[Union[Union[int, float, complex], Any], Any]]

angle_spectrum: partial[tuple[Union[Union[int, float, complex], Any], Any]]

phase_spectrum: partial[tuple[Union[Union[int, float, complex], Any], Any]]


def csd(x: Any,
        y: Any,
        NFFT: Union[int, Any] = None,
        Fs: Union[int, Any] = None,
        detrend: Union[Callable[[Any, int], Any], Any] = None,
        window: Union[Callable[[{__len__}], Any], Any] = None,
        noverlap: int = None,
        pad_to: Any = None,
        sides: Union[str, Any] = None,
        scale_by_freq: Any = None) -> Any: ...


def specgram(x: Union[Union[Iterable, int, float], Any],
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
           window: Callable[[{__len__}], Any] = window_hanning,
           noverlap: int = 0,
           pad_to: Any = None,
           sides: str = 'default',
           scale_by_freq: Any = None) -> Any: ...


class GaussianKDE(object):
    covariance_factor: ClassVar[Callable[[GaussianKDE], Any]]
    __call__: ClassVar[Callable[[GaussianKDE, Any], Any]]
    data_covariance: Union[list[Any], Any]
    inv_cov: Union[Union[float, complex], Any]
    data_inv_cov: Any
    norm_factor: Any
    dim: Any
    _bw_method: Callable
    covariance: Union[Union[list[Any], float, complex], Any]
    covariance_factor: Callable[[], Any]
    factor: Union[Union[str, int, float, complex, Callable, None], Any]
    dataset: Union[list[Any], Any]
    num_dp: Any

    def __init__(self: GaussianKDE,
                 dataset: Union[Union[Iterable, int, float], Any],
                 bw_method: Union[str, int, float, complex, Callable, None] = None) -> Any: ...

    def scotts_factor(self: GaussianKDE) -> Any: ...

    def silverman_factor(self: GaussianKDE) -> Any: ...

    def evaluate(self: GaussianKDE,
                 points: Any) -> Any: ...
