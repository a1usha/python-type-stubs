from matplotlib.transforms import TransformNode as TransformNode
from pathlib import Path as Path
from io import StringIO as StringIO
from typing import Any


def graphviz_dump_transform(transform: Any,
                            dest: str,
                            *,
                            highlight: Any = None) -> None: ...