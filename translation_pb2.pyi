from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class News(_message.Message):
    __slots__ = ["news"]
    NEWS_FIELD_NUMBER: _ClassVar[int]
    news: _containers.RepeatedCompositeFieldContainer[OneNews]
    def __init__(self, news: _Optional[_Iterable[_Union[OneNews, _Mapping]]] = ...) -> None: ...

class OneNews(_message.Message):
    __slots__ = ["one_news"]
    class OneNewsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ONE_NEWS_FIELD_NUMBER: _ClassVar[int]
    one_news: _containers.ScalarMap[str, str]
    def __init__(self, one_news: _Optional[_Mapping[str, str]] = ...) -> None: ...

class NewsResponse(_message.Message):
    __slots__ = ["response"]
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    response: str
    def __init__(self, response: _Optional[str] = ...) -> None: ...
