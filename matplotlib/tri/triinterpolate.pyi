from typing import Any
from typing import Iterable
from typing import Optional
from typing import Tuple
from typing import Union

from matplotlib.tri.triinterpolate import CubicTriInterpolator
from matplotlib.tri.triinterpolate import LinearTriInterpolator
from matplotlib.tri.triinterpolate import TriInterpolator
from matplotlib.tri.triinterpolate import _DOF_estimator
from matplotlib.tri.triinterpolate import _DOF_estimator_geom
from matplotlib.tri.triinterpolate import _DOF_estimator_min_E
from matplotlib.tri.triinterpolate import _DOF_estimator_user
from matplotlib.tri.triinterpolate import _ReducedHCT_Element
from matplotlib.tri.triinterpolate import _Sparse_Matrix_coo
from numpy.core._multiarray_umath import ndarray
from object import object


class TriInterpolator(object):
    def __init__(self: TriInterpolator,
                 triangulation: Any,
                 z: Any,
                 trifinder: Any = None) -> Any: ...

    def _interpolate_multikeys(self: TriInterpolator,
                               x: Union[ndarray, Iterable, int, float],
                               y: Union[ndarray, Iterable, int, float],
                               tri_index: Union[ndarray, Iterable, int, float[int], None] = None,
                               return_keys: str = ('z',)) -> list[Any]: ...

    def _interpolate_single_key(self: TriInterpolator,
                                return_key: str,
                                tri_index: int,
                                x: int,
                                y: int) -> Any: ...


class LinearTriInterpolator(TriInterpolator):
    def __init__(self: LinearTriInterpolator,
                 triangulation: Any,
                 z: Any,
                 trifinder: Any = None) -> None: ...

    def __call__(self: LinearTriInterpolator,
                 x: Any,
                 y: Any) -> Any: ...

    def gradient(self: LinearTriInterpolator,
                 x: Any,
                 y: Any) -> list[Any]: ...

    def _interpolate_single_key(self: LinearTriInterpolator,
                                return_key: str,
                                tri_index: int,
                                x: int,
                                y: int) -> Union[int, Any]: ...


class CubicTriInterpolator(TriInterpolator):
    def __init__(self: CubicTriInterpolator,
                 triangulation: Any,
                 z: Any,
                 kind: Optional[str] = 'min_E',
                 trifinder: Any = None,
                 dz: Any = None) -> None: ...

    def __call__(self: CubicTriInterpolator,
                 x: Any,
                 y: Any) -> Any: ...

    def gradient(self: CubicTriInterpolator,
                 x: Any,
                 y: Any) -> list[Any]: ...

    def _interpolate_single_key(self: CubicTriInterpolator,
                                return_key: str,
                                tri_index: int,
                                x: int,
                                y: int) -> Any: ...

    def _compute_dof(self: CubicTriInterpolator,
                     kind: str,
                     dz: Any = None) -> Any: ...

    def _get_alpha_vec(x: Any,
                       y: Any,
                       tris_pts: int) -> Any: ...

    def _get_jacobian(tris_pts: int) -> Any: ...

    def _compute_tri_eccentricities(tris_pts: int) -> Any: ...


class _ReducedHCT_Element(object):
    def get_function_values(self: _ReducedHCT_Element,
                            alpha: Any,
                            ecc: Any,
                            dofs: Any) -> Any: ...

    def get_function_derivatives(self: _ReducedHCT_Element,
                                 alpha: Any,
                                 J: Union[tuple[Any, Any, Any, Any], Any],
                                 ecc: Any,
                                 dofs: {__matmul__}) -> None: ...

    def get_function_hessians(self: _ReducedHCT_Element,
                              alpha: Any,
                              J: Any,
                              ecc: Any,
                              dofs: {__matmul__}) -> ndarray: ...

    def get_d2Sidksij2(self: _ReducedHCT_Element,
                       alpha: Any,
                       ecc: Any) -> ndarray: ...

    def get_bending_matrices(self: _ReducedHCT_Element,
                             J: Union[tuple[Any, Any, Any, Any], Any],
                             ecc: Any) -> Any: ...

    def get_Hrot_from_J(self: _ReducedHCT_Element,
                        J: Union[tuple[Any, Any, Any, Any], Any],
                        return_area: bool = False) -> Union[Tuple[Any, Union[float, Any]], Any]: ...

    def get_Kff_and_Ff(self: _ReducedHCT_Element,
                       J: Union[tuple[Any, Any, Any, Any], Any],
                       ecc: Any,
                       triangles: Any,
                       Uc: Any) -> Any: ...


class _DOF_estimator(object):
    def __init__(self: _DOF_estimator,
                 interpolator: Union[{_eccs}, Any],
                 **kwargs) -> None: ...

    def compute_dz(self: _DOF_estimator,
                   **kwargs) -> Any: ...

    def compute_dof_from_df(self: _DOF_estimator) -> Any: ...

    def get_dof_vec(tri_z: Any,
                    tri_dz: int,
                    J: Union[tuple[Any, Any, Any, Any], Any]) -> Any: ...


class _DOF_estimator_user(_DOF_estimator):
    def compute_dz(self: _DOF_estimator_user,
                   dz: Any) -> Any: ...


class _DOF_estimator_geom(_DOF_estimator):
    def compute_dz(self: _DOF_estimator_geom) -> Any: ...

    def compute_geom_weights(self: _DOF_estimator_geom) -> ndarray: ...

    def compute_geom_grads(self: _DOF_estimator_geom) -> ndarray: ...


class _DOF_estimator_min_E(_DOF_estimator_geom):
    def __init__(self: _DOF_estimator_min_E,
                 Interpolator: {_eccs, _pts, _tris_pts, _z, _triangles, _unit_x, _unit_y}) -> None: ...

    def compute_dz(self: _DOF_estimator_min_E) -> ndarray: ...


class _Sparse_Matrix_coo(object):
    def __init__(self: _Sparse_Matrix_coo,
                 vals: Any,
                 rows: Any,
                 cols: Any,
                 shape: Any) -> None: ...

    def dot(self: _Sparse_Matrix_coo,
            V: Union[Union[ndarray, Iterable, int, float, None], Any]) -> ndarray[int]: ...

    def compress_csc(self: _Sparse_Matrix_coo) -> None: ...

    def compress_csr(self: _Sparse_Matrix_coo) -> None: ...

    def to_dense(self: _Sparse_Matrix_coo) -> ndarray: ...

    def __str__(self: _Sparse_Matrix_coo) -> None: ...

    def diag(self: _Sparse_Matrix_coo) -> ndarray: ...


def _cg(A: _Sparse_Matrix_coo,
        b: Union[ndarray, Iterable, int, float],
        x0: Union[ndarray, Iterable, int, float, None] = None,
        tol: Optional[float] = 1.e-10,
        maxiter: Optional[int] = 1000) -> array.pyi: ...


def _safe_inv22_vectorized(M: Union[Union[tuple[Any, Any, Any, Any], ndarray], Any]) -> ndarray: ...


def _pseudo_inv22sym_vectorized(M: Optional[Any]) -> ndarray: ...


def _scalar_vectorized(scalar: Union[Optional[float], Any],
                       M: Optional[Any]) -> Any: ...


def _transpose_vectorized(M: Union[Optional[ndarray], Any]) -> ndarray: ...


def _roll_vectorized(M: Optional[Any],
                     roll_indices: Optional[Any],
                     axis: Union[int, Any]) -> ndarray: ...


def _to_matrix_vectorized(M: Union[Union[
                                       list[Union[list[Union[int, Any]], list[Any]]], list[list[None]], list[list[Any]],
                                       list[Union[list[Union[float, Any]], list[Any]]], list[
                                           Union[list[float], list[Union[float, Any]]]], list[
                                           list[Union[Union[ndarray, int], Any]]]], Any]) -> Any: ...


def _extract_submatrices(M: Union[ndarray, Any],
                         block_indices: Union[ndarray[int], Any],
                         block_size: Union[int, Any],
                         axis: Union[int, Any]) -> ndarray: ...