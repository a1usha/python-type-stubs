from typing import Any

latex_to_cmex: dict[Union[str, Any], Union[int, Any]]
latex_to_standard: dict[Union[str, Any], Union[tuple[str, int], Any]]
type12uni: dict[Union[str, Any], Union[int, Any]]
uni2type1: dict
tex2uni: dict[Union[str, Any], Union[int, Any]]
stix_virtual_fonts: dict[str, Union[
    dict[str, list[Union[tuple[int, int, str, int], Any]]], list[tuple[int, int, str, int]], list[
        Union[tuple[int, int, str, int], Any]], dict[
        str, Union[list[Union[tuple[int, int, str, int], Any]], list[tuple[int, int, str, int]]]], dict[
        str, list[tuple[int, int, str, int]]]]]
latex_to_bakoma: dict[Union[str, Any], Union[tuple[str, int], Any]]