from matplotlib.backends.qt_editor import _formlayout as _formlayout
from matplotlib.backends.qt_compat import QtGui as QtGui
from matplotlib import image as mimage
from matplotlib import markers as markers
from matplotlib import colors as mcolors
from matplotlib import cm as cm
from matplotlib import cbook as cbook

LINESTYLES: dict[str, str]
DRAWSTYLES: dict[str, str]
MARKERS: dict[Union[str, Any], Union[str, Any]]
from typing import Any


def figure_edit(
        axes: {get_xlim, get_ylim, get_title, get_xlabel, get_xscale, get_ylabel, get_yscale, xaxis, yaxis, get_lines,
               images, collections},
        parent: Any = None) -> Any: ...