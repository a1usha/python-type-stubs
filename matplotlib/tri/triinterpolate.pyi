from typing import Optional
from typing import Any
from typing import Union
from numpy.core._multiarray_umath import ndarray
from typing import Any
from typing import tuple
from typing import Any
from typing import Any
from typing import Any
from numpy.core._multiarray_umath import ndarray
from typing import Any
from numpy.core._multiarray_umath import ndarray
from typing import Union
from typing import Any
from typing import Optional
from typing import Any
from typing import Optional
from typing import Any
from typing import Any
from typing import Optional
from typing import Any
from typing import Optional
from typing import Any
from typing import Optional
from typing import Optional
from typing import Union
from typing import Iterable
from numpy.core._multiarray_umath import ndarray
from typing import Union
from typing import Iterable
from numpy.core._multiarray_umath import ndarray
from typing import Optional
from typing import Any
from numpy.core._multiarray_umath import ndarray
from typing import Any
from typing import Optional
from typing import Union
from typing import Iterable
from numpy.core._multiarray_umath import ndarray
from typing import Union
from typing import Iterable
from numpy.core._multiarray_umath import ndarray
from typing import Union
from typing import Iterable
from numpy.core._multiarray_umath import ndarray
from typing import tuple
from typing import Any
from typing import tuple
from typing import tuple
from typing import Any
from typing import tuple
from typing import tuple
from typing import Any
from typing import tuple
from typing import Union
from typing import Any
from typing import Iterable
from numpy.core._multiarray_umath import ndarray


class _Sparse_Matrix_coo(object):
    def __init__(self: _Sparse_Matrix_coo, vals: Any, rows: Any, cols: Any, shape: Any) -> None: ...

    def dot(self: _Sparse_Matrix_coo, V: Union[ndarray, Iterable, int, float, None]) -> ndarray[int]: ...

    def compress_csc(self: _Sparse_Matrix_coo) -> None: ...

    def compress_csr(self: _Sparse_Matrix_coo) -> None: ...

    def to_dense(self: _Sparse_Matrix_coo) -> ndarray: ...

    def __str__(self: _Sparse_Matrix_coo) -> None: ...

    def diag(self: _Sparse_Matrix_coo) -> ndarray: ...


class _ReducedHCT_Element(object):
    def get_function_values(self: _ReducedHCT_Element, alpha: Any, ecc: Any, dofs: Any) -> Any: ...

    def get_function_derivatives(self: _ReducedHCT_Element, alpha: Any, J: Any, ecc: Any,
                                 dofs: {__matmul__}) -> None: ...

    def get_function_hessians(self: _ReducedHCT_Element, alpha: Any, J: Any, ecc: Any,
                              dofs: {__matmul__}) -> ndarray: ...

    def get_d2Sidksij2(self: _ReducedHCT_Element, alpha: Any, ecc: Any) -> ndarray: ...

    def get_bending_matrices(self: _ReducedHCT_Element, J: tuple[Any, Any, Any, Any], ecc: Any) -> Any: ...

    def get_Hrot_from_J(self: _ReducedHCT_Element, J: tuple[Any, Any, Any, Any], return_area: bool = False) -> tuple[
        Any, float]: ...

    def get_Kff_and_Ff(self: _ReducedHCT_Element, J: tuple[Any, Any, Any, Any], ecc: Any, triangles: Any,
                       Uc: Any) -> Any: ...


class TriInterpolator(object):
    def __init__(self: TriInterpolator, triangulation: Any, z: Any, trifinder: Any = None) -> Any: ...

    def _interpolate_multikeys(self: TriInterpolator, x: Union[ndarray, Iterable, int, float],
                               y: Union[ndarray, Iterable, int, float],
                               tri_index: Union[ndarray, Iterable, int, float[int], None] = None,
                               return_keys: str = ('z',)) -> list: ...

    def _interpolate_single_key(self: TriInterpolator, return_key: str, tri_index: int, x: int, y: int) -> Any: ...


class _DOF_estimator_min_E(_DOF_estimator_geom):
    def __init__(self: _DOF_estimator_min_E,
                 Interpolator: {_eccs, _pts, _tris_pts, _z, _triangles, _unit_x, _unit_y}) -> None: ...

    def compute_dz(self: _DOF_estimator_min_E) -> ndarray: ...


class _DOF_estimator_geom(_DOF_estimator):
    def compute_dz(self: _DOF_estimator_geom) -> object: ...

    def compute_geom_weights(self: _DOF_estimator_geom) -> ndarray: ...

    def compute_geom_grads(self: _DOF_estimator_geom) -> ndarray: ...


class CubicTriInterpolator(TriInterpolator):
    def __init__(self: CubicTriInterpolator, triangulation: Any, z: Any, kind: Optional[str] = 'min_E',
                 trifinder: Any = None, dz: Any = None) -> None: ...

    def __call__(self: CubicTriInterpolator, x: Any, y: Any) -> Any: ...

    def gradient(self: CubicTriInterpolator, x: Any, y: Any) -> list: ...

    def _interpolate_single_key(self: CubicTriInterpolator, return_key: str, tri_index: int, x: int, y: int) -> Any: ...

    def _compute_dof(self: CubicTriInterpolator, kind: str, dz: Any = None) -> Any: ...

    def _get_alpha_vec(x: Any, y: Any, tris_pts: int) -> Any: ...

    def _get_jacobian(tris_pts: int) -> Any: ...

    def _compute_tri_eccentricities(tris_pts: int) -> Any: ...


class LinearTriInterpolator(TriInterpolator):
    def __init__(self: LinearTriInterpolator, triangulation: Any, z: Any, trifinder: Any = None) -> None: ...

    def __call__(self: LinearTriInterpolator, x: Any, y: Any) -> Any: ...

    def gradient(self: LinearTriInterpolator, x: Any, y: Any) -> list: ...

    def _interpolate_single_key(self: LinearTriInterpolator, return_key: str, tri_index: int, x: int,
                                y: int) -> int: ...


class _DOF_estimator_user(_DOF_estimator):
    def compute_dz(self: _DOF_estimator_user, dz: Any) -> object: ...


class _DOF_estimator(object):
    def __init__(self: _DOF_estimator, interpolator: {_eccs}, , **kwargs) -> None: ...

    def compute_dz(self: _DOF_estimator, , **kwargs) -> Any: ...

    def compute_dof_from_df(self: _DOF_estimator) -> Any: ...

    def get_dof_vec(tri_z: Any, tri_dz: int, J: {__matmul__}) -> Any: ...


def _transpose_vectorized(M: Optional[ndarray]) -> ndarray: ...


def _cg(A: _Sparse_Matrix_coo, b: Union[ndarray, Iterable, int, float],
        x0: Union[ndarray, Iterable, int, float, None] = None, tol: Optional[float] = 1.e-10,
        maxiter: Optional[int] = 1000) -> array.pyi: ...


def _roll_vectorized(M: Optional[Any], roll_indices: Optional[Any], axis: int) -> ndarray: ...


def _scalar_vectorized(scalar: Optional[float], M: Optional[Any]) -> Any: ...


def _to_matrix_vectorized(M: Union[
    list[Union[list[int], list]], list[list[None]], list[list], list[Union[list[float], list]], list[
        Union[list[float], list[float]]], list[list[Union[ndarray, int]]]]) -> Any: ...


def _extract_submatrices(M: ndarray, block_indices: ndarray[int], block_size: int, axis: int) -> ndarray: ...


def _safe_inv22_vectorized(M: Union[tuple[Any, Any, Any, Any], ndarray]) -> ndarray: ...


def _pseudo_inv22sym_vectorized(M: Optional[Any]) -> ndarray: ...