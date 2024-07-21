from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Ad_Request(_message.Message):
    __slots__ = ("id", "min_cpc")
    ID_FIELD_NUMBER: _ClassVar[int]
    MIN_CPC_FIELD_NUMBER: _ClassVar[int]
    id: int
    min_cpc: int
    def __init__(self, id: _Optional[int] = ..., min_cpc: _Optional[int] = ...) -> None: ...

class Ad_Reply(_message.Message):
    __slots__ = ("title", "image")
    TITLE_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    title: str
    image: str
    def __init__(self, title: _Optional[str] = ..., image: _Optional[str] = ...) -> None: ...
