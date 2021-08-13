class classproperty(object):
    def __init__(self: classproperty,
                 fget: Any,
                 fset: Any = None,
                 fdel: Any = None,
                 doc: Any = None) -> Any: ...

    def __get__(self: classproperty,
                instance: Any,
                owner: Any) -> Any: ...

    @property
    def fget(self: classproperty) -> Any: ...
