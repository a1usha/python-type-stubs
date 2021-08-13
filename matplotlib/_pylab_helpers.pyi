from typing import Any
from typing import Optional


class Gcf(object):
    @classmethod
    def get_fig_manager(cls: Type[Gcf],
                        num: Any) -> Optional[Any]: ...

    @classmethod
    def destroy(cls: Type[Gcf],
                num: Optional[Any]) -> None: ...

    @classmethod
    def destroy_fig(cls: Type[Gcf],
                    fig: Any) -> None: ...

    @classmethod
    def destroy_all(cls: Type[Gcf]) -> None: ...

    @classmethod
    def has_fignum(cls: Type[Gcf],
                   num: Any) -> bool: ...

    @classmethod
    def get_all_fig_managers(cls: Type[Gcf]) -> list: ...

    @classmethod
    def get_num_fig_managers(cls: Type[Gcf]) -> int: ...

    @classmethod
    def get_active(cls: Type[Gcf]) -> Optional[Any]: ...

    @classmethod
    def _set_new_active_manager(cls: Type[Gcf],
                                manager: {canvas, num}) -> None: ...

    @classmethod
    def set_active(cls: Type[Gcf],
                   manager: Optional[Any]) -> None: ...

    @classmethod
    def draw_all(cls: Type[Gcf],
                 force: bool = False) -> None: ...
