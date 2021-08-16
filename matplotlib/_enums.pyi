class _AutoStringNameEnum(Enum):
    def _generate_next_value_(name: _AutoStringNameEnum,
                              start: Any,
                              count: Any,
                              last_values: Any) -> _AutoStringNameEnum: ...

    def __hash__(self: _AutoStringNameEnum) -> int: ...


def _deprecate_case_insensitive_join_cap(s: {lower, __ne__}) -> Any: ...


class JoinStyle(str, _AutoStringNameEnum):
    def __init__(self: JoinStyle,
                 s: Any) -> None: ...

    @staticmethod
    def demo() -> None: ...


class CapStyle(str, _AutoStringNameEnum):
    def __init__(self: CapStyle,
                 s: Any) -> None: ...

    @staticmethod
    def demo() -> None: ...
