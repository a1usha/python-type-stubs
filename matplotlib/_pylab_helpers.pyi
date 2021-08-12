from typing import Optional
from typing import Any
from typing import Optional
from typing import Any


class Gcf(object):
    def get_fig_manager(cls: Type[Gcf], num: Any) -> Optional[Any]: ...

    def destroy(cls: Type[Gcf], num: Optional[Any]) -> None: ...

    def destroy_fig(cls: Type[Gcf], fig: Any) -> None: ...

    def destroy_all(cls: Type[Gcf]) -> None: ...

    def has_fignum(cls: Type[Gcf], num: Any) -> bool: ...

    def get_all_fig_managers(cls: Type[Gcf]) -> list: ...

    def get_num_fig_managers(cls: Type[Gcf]) -> int: ...

    def get_active(cls: Type[Gcf]) -> Optional[Any]: ...

    def _set_new_active_manager(cls: Type[Gcf], manager: {canvas, num}) -> None: ...

    def set_active(cls: Type[Gcf], manager: Optional[Any]) -> None: ...

    def draw_all(cls: Type[Gcf], force: bool = False) -> None: ...
