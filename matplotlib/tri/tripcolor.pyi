from matplotlib.tri.triangulation import Triangulation as Triangulation
from matplotlib.colors import Normalize as Normalize
from matplotlib.collections import TriMesh as TriMesh
from matplotlib.collections import PolyCollection as PolyCollection
from matplotlib import _api as _api
from typing import Any
from typing import Union

from matplotlib.collections import PolyCollection
from matplotlib.collections import TriMesh


def tripcolor(*args,
              ax: {grid, update_datalim, autoscale_view, add_collection},
              alpha: float = 1.0,
              norm: Any = None,
              cmap: Any = None,
              vmin: Any = None,
              vmax: Any = None,
              shading: str = 'flat',
              facecolors: Any = None,
              **kwargs) -> Union[TriMesh, PolyCollection]: ...