from typing import Optional
from typing import Type

from matplotlib._pylab_helpers import Gcf
from object import object


class Gcf(object):
    def get_fig_manager(cls: Type[Gcf],
                        num: Any) -> Optional[Any]: ...

    def destroy(cls: Type[Gcf],
                num: Optional[Any]) -> None: ...

    def destroy_fig(cls: Type[Gcf],
                    fig: Any) -> None: ...

    def destroy_all(cls: Type[Gcf]) -> None: ...

    def has_fignum(cls: Type[Gcf],
                   num: Any) -> bool: ...

    def get_all_fig_managers(cls: Type[Gcf]) -> list: ...

    def get_num_fig_managers(cls: Type[Gcf]) -> int: ...

    def get_active(cls: Type[Gcf]) -> Optional[Any]: ...

    def _set_new_active_manager(cls: Type[Gcf],
                                manager: {canvas, num}) -> None: ...

    def set_active(cls: Type[Gcf],
                   manager: Optional[{canvas, num}]) -> None: ...

    def draw_all(cls: Type[Gcf],
                 force: bool = False) -> None: ...
