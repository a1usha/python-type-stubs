from matplotlib import _api as _api
from typing import Tuple
from typing import Union

_log: Logger
from typing import Any


def do_constrained_layout(fig: Any,
                          renderer: Any,
                          h_pad: float,
                          w_pad: float,
                          hspace: float = None,
                          wspace: float = None) -> None: ...


def _check_no_collapsed_axes(fig: {subfigs, axes}) -> bool: ...


def _get_margin_from_padding(object: {_subplotspec},
                             *,
                             w_pad: int = 0,
                             h_pad: int = 0,
                             hspace: int = 0,
                             wspace: int = 0) -> dict[str, Union[Union[int, float], Any]]: ...


def _make_layout_margins(fig: {subfigs, _localaxes},
                         renderer: Any,
                         *,
                         w_pad: int = 0,
                         h_pad: int = 0,
                         hspace: int = 0,
                         wspace: int = 0) -> None: ...


def _make_margin_suptitles(fig: {transFigure, transSubfigure, subfigs, _suptitle, _supxlabel, _supylabel},
                           renderer: Any,
                           *,
                           w_pad: int = 0,
                           h_pad: int = 0) -> None: ...


def _match_submerged_margins(fig: {subfigs, get_axes}) -> None: ...


def _get_cb_parent_spans(cbax: Union[{_colorbar_info}, Any]) -> Tuple[range, range]: ...


def _get_pos_and_bbox(ax: {figure, get_position, get_tightbbox},
                      renderer: Any) -> Any: ...


def _reposition_axes(fig: {transFigure, transSubfigure, subfigs, _localaxes},
                     renderer: Any,
                     *,
                     w_pad: int = 0,
                     h_pad: int = 0,
                     hspace: int = 0,
                     wspace: int = 0) -> None: ...


def _reposition_colorbar(cbax: Any,
                         renderer: Any,
                         *,
                         offset: Union[dict[str, int], Any] = None) -> Union[dict[str, int], Any]: ...


def _reset_margins(fig: {subfigs, axes, _layoutgrid}) -> None: ...


def _colorbar_get_pad(cax: {_colorbar_info}) -> Any: ...