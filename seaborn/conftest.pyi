from typing import Any
from typing import Generator
from typing import Optional
from typing import Union

from pandas.core.frame import DataFrame
from pandas.core.series import Series


def has_verdana() -> bool: ...


def remove_pandas_unit_conversion() -> Optional[Any]: ...


def close_figs() -> Union[Generator[Any, Any, None], Any]: ...


def random_seed() -> Optional[Any]: ...


def rng() -> Any: ...


def wide_df(rng: {normal}) -> Union[DataFrame, Any]: ...


def wide_array(wide_df: Any) -> Any: ...


def flat_series(rng: {normal}) -> Union[Series, Any]: ...


def flat_array(flat_series: Any) -> Any: ...


def flat_list(flat_series: {tolist}) -> Any: ...


def flat_data(rng: {normal},
              request: {param}) -> Union[Union[list, Series], Any]: ...


def wide_list_of_series(rng: {normal}) -> Union[list[Series], Any]: ...


def wide_list_of_arrays(wide_list_of_series: Any) -> Union[list[Any], Any]: ...


def wide_list_of_lists(wide_list_of_series: Any) -> Union[list[Any], Any]: ...


def wide_dict_of_series(wide_list_of_series: Any) -> Union[dict, Any]: ...


def wide_dict_of_arrays(wide_list_of_series: Any) -> Union[dict, Any]: ...


def wide_dict_of_lists(wide_list_of_series: Any) -> Union[dict, Any]: ...


def long_df(rng: {uniform, normal, lognormal, choice}) -> Union[DataFrame, Any]: ...


def long_dict(long_df: {to_dict}) -> Any: ...


def repeated_df(rng: {normal, choice}) -> Union[DataFrame, Any]: ...


def missing_df(rng: {permutation},
               long_df: {copy}) -> Any: ...


def object_df(rng: Any,
              long_df: {copy}) -> Any: ...


def null_series(flat_series: {index}) -> Union[Series, Any]: ...