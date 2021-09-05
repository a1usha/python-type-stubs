from palettes import cubehelix_palette as cubehelix_palette
from palettes import diverging_palette as diverging_palette
from palettes import light_palette as light_palette
from palettes import dark_palette as dark_palette
from palettes import color_palette as color_palette
from miscplot import palplot as palplot
from IPython.html.widgets import IntSliderWidget as IntSliderWidget
from IPython.html.widgets import FloatSliderWidget as FloatSliderWidget
from IPython.html.widgets import interact as interact
from IPython.html.widgets import IntSlider as IntSlider
from IPython.html.widgets import FloatSlider as FloatSlider
from IPython.html.widgets import interact as interact
from ipywidgets import IntSlider as IntSlider
from ipywidgets import FloatSlider as FloatSlider
from ipywidgets import interact as interact
from matplotlib.colors import LinearSegmentedColormap as LinearSegmentedColormap
from typing import Any
from typing import Union

from matplotlib.colors import LinearSegmentedColormap
from numpy.matrixlib.defmatrix import matrix
from seaborn.palettes import _ColorPalette

__all__: Any


def _init_mutable_colormap() -> LinearSegmentedColormap: ...


def _update_lut(cmap: Union[LinearSegmentedColormap, Any],
                colors: Union[Union[matrix, _ColorPalette[tuple]], Any]) -> None: ...


def _show_cmap(cmap: Union[LinearSegmentedColormap, Any]) -> None: ...


def choose_colorbrewer_palette(data_type: Any,
                               as_cmap: bool = False) -> Union[LinearSegmentedColormap, list[Any]]: ...


def choose_dark_palette(input: Any = "husl",
                        as_cmap: bool = False) -> Union[LinearSegmentedColormap, list[Any]]: ...


def choose_light_palette(input: Any = "husl",
                         as_cmap: bool = False) -> Union[LinearSegmentedColormap, list[Any]]: ...


def choose_diverging_palette(as_cmap: bool = False) -> Union[LinearSegmentedColormap, list[Any]]: ...


def choose_cubehelix_palette(as_cmap: bool = False) -> Union[LinearSegmentedColormap, list[Any]]: ...