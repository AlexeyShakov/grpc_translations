from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TranslatedNews(_message.Message):
    __slots__ = ["news"]
    NEWS_FIELD_NUMBER: _ClassVar[int]
    news: _containers.RepeatedCompositeFieldContainer[OneTranslatedNews]
    def __init__(self, news: _Optional[_Iterable[_Union[OneTranslatedNews, _Mapping]]] = ...) -> None: ...

class OneTranslatedNews(_message.Message):
    __slots__ = ["id", "link", "translated_title", "translated_short_description"]
    class IdEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    class LinkEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class TranslatedTitleEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class TranslatedShortDescriptionEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    LINK_FIELD_NUMBER: _ClassVar[int]
    TRANSLATED_TITLE_FIELD_NUMBER: _ClassVar[int]
    TRANSLATED_SHORT_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    id: _containers.ScalarMap[str, int]
    link: _containers.ScalarMap[str, str]
    translated_title: _containers.ScalarMap[str, str]
    translated_short_description: _containers.ScalarMap[str, str]
    def __init__(self, id: _Optional[_Mapping[str, int]] = ..., link: _Optional[_Mapping[str, str]] = ..., translated_title: _Optional[_Mapping[str, str]] = ..., translated_short_description: _Optional[_Mapping[str, str]] = ...) -> None: ...

class TranslatedNewsResponse(_message.Message):
    __slots__ = ["response"]
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    response: str
    def __init__(self, response: _Optional[str] = ...) -> None: ...
