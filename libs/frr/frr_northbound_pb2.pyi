from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Encoding(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    JSON: _ClassVar[Encoding]
    XML: _ClassVar[Encoding]
JSON: Encoding
XML: Encoding

class GetCapabilitiesRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetCapabilitiesResponse(_message.Message):
    __slots__ = ("frr_version", "rollback_support", "supported_modules", "supported_encodings")
    FRR_VERSION_FIELD_NUMBER: _ClassVar[int]
    ROLLBACK_SUPPORT_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_MODULES_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_ENCODINGS_FIELD_NUMBER: _ClassVar[int]
    frr_version: str
    rollback_support: bool
    supported_modules: _containers.RepeatedCompositeFieldContainer[ModuleData]
    supported_encodings: _containers.RepeatedScalarFieldContainer[Encoding]
    def __init__(self, frr_version: _Optional[str] = ..., rollback_support: bool = ..., supported_modules: _Optional[_Iterable[_Union[ModuleData, _Mapping]]] = ..., supported_encodings: _Optional[_Iterable[_Union[Encoding, str]]] = ...) -> None: ...

class GetRequest(_message.Message):
    __slots__ = ("type", "encoding", "with_defaults", "path")
    class DataType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ALL: _ClassVar[GetRequest.DataType]
        CONFIG: _ClassVar[GetRequest.DataType]
        STATE: _ClassVar[GetRequest.DataType]
    ALL: GetRequest.DataType
    CONFIG: GetRequest.DataType
    STATE: GetRequest.DataType
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ENCODING_FIELD_NUMBER: _ClassVar[int]
    WITH_DEFAULTS_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    type: GetRequest.DataType
    encoding: Encoding
    with_defaults: bool
    path: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, type: _Optional[_Union[GetRequest.DataType, str]] = ..., encoding: _Optional[_Union[Encoding, str]] = ..., with_defaults: bool = ..., path: _Optional[_Iterable[str]] = ...) -> None: ...

class GetResponse(_message.Message):
    __slots__ = ("timestamp", "data")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    timestamp: int
    data: DataTree
    def __init__(self, timestamp: _Optional[int] = ..., data: _Optional[_Union[DataTree, _Mapping]] = ...) -> None: ...

class CreateCandidateRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CreateCandidateResponse(_message.Message):
    __slots__ = ("candidate_id",)
    CANDIDATE_ID_FIELD_NUMBER: _ClassVar[int]
    candidate_id: int
    def __init__(self, candidate_id: _Optional[int] = ...) -> None: ...

class DeleteCandidateRequest(_message.Message):
    __slots__ = ("candidate_id",)
    CANDIDATE_ID_FIELD_NUMBER: _ClassVar[int]
    candidate_id: int
    def __init__(self, candidate_id: _Optional[int] = ...) -> None: ...

class DeleteCandidateResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateCandidateRequest(_message.Message):
    __slots__ = ("candidate_id",)
    CANDIDATE_ID_FIELD_NUMBER: _ClassVar[int]
    candidate_id: int
    def __init__(self, candidate_id: _Optional[int] = ...) -> None: ...

class UpdateCandidateResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EditCandidateRequest(_message.Message):
    __slots__ = ("candidate_id", "update", "delete")
    CANDIDATE_ID_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FIELD_NUMBER: _ClassVar[int]
    DELETE_FIELD_NUMBER: _ClassVar[int]
    candidate_id: int
    update: _containers.RepeatedCompositeFieldContainer[PathValue]
    delete: _containers.RepeatedCompositeFieldContainer[PathValue]
    def __init__(self, candidate_id: _Optional[int] = ..., update: _Optional[_Iterable[_Union[PathValue, _Mapping]]] = ..., delete: _Optional[_Iterable[_Union[PathValue, _Mapping]]] = ...) -> None: ...

class EditCandidateResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class LoadToCandidateRequest(_message.Message):
    __slots__ = ("candidate_id", "type", "config")
    class LoadType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MERGE: _ClassVar[LoadToCandidateRequest.LoadType]
        REPLACE: _ClassVar[LoadToCandidateRequest.LoadType]
    MERGE: LoadToCandidateRequest.LoadType
    REPLACE: LoadToCandidateRequest.LoadType
    CANDIDATE_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    candidate_id: int
    type: LoadToCandidateRequest.LoadType
    config: DataTree
    def __init__(self, candidate_id: _Optional[int] = ..., type: _Optional[_Union[LoadToCandidateRequest.LoadType, str]] = ..., config: _Optional[_Union[DataTree, _Mapping]] = ...) -> None: ...

class LoadToCandidateResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CommitRequest(_message.Message):
    __slots__ = ("candidate_id", "phase", "comment")
    class Phase(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        VALIDATE: _ClassVar[CommitRequest.Phase]
        PREPARE: _ClassVar[CommitRequest.Phase]
        ABORT: _ClassVar[CommitRequest.Phase]
        APPLY: _ClassVar[CommitRequest.Phase]
        ALL: _ClassVar[CommitRequest.Phase]
    VALIDATE: CommitRequest.Phase
    PREPARE: CommitRequest.Phase
    ABORT: CommitRequest.Phase
    APPLY: CommitRequest.Phase
    ALL: CommitRequest.Phase
    CANDIDATE_ID_FIELD_NUMBER: _ClassVar[int]
    PHASE_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    candidate_id: int
    phase: CommitRequest.Phase
    comment: str
    def __init__(self, candidate_id: _Optional[int] = ..., phase: _Optional[_Union[CommitRequest.Phase, str]] = ..., comment: _Optional[str] = ...) -> None: ...

class CommitResponse(_message.Message):
    __slots__ = ("transaction_id", "error_message")
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    transaction_id: int
    error_message: str
    def __init__(self, transaction_id: _Optional[int] = ..., error_message: _Optional[str] = ...) -> None: ...

class ListTransactionsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListTransactionsResponse(_message.Message):
    __slots__ = ("id", "client", "date", "comment")
    ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    id: int
    client: str
    date: str
    comment: str
    def __init__(self, id: _Optional[int] = ..., client: _Optional[str] = ..., date: _Optional[str] = ..., comment: _Optional[str] = ...) -> None: ...

class GetTransactionRequest(_message.Message):
    __slots__ = ("transaction_id", "encoding", "with_defaults")
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    ENCODING_FIELD_NUMBER: _ClassVar[int]
    WITH_DEFAULTS_FIELD_NUMBER: _ClassVar[int]
    transaction_id: int
    encoding: Encoding
    with_defaults: bool
    def __init__(self, transaction_id: _Optional[int] = ..., encoding: _Optional[_Union[Encoding, str]] = ..., with_defaults: bool = ...) -> None: ...

class GetTransactionResponse(_message.Message):
    __slots__ = ("config",)
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    config: DataTree
    def __init__(self, config: _Optional[_Union[DataTree, _Mapping]] = ...) -> None: ...

class LockConfigRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class LockConfigResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UnlockConfigRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UnlockConfigResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ExecuteRequest(_message.Message):
    __slots__ = ("path", "input")
    PATH_FIELD_NUMBER: _ClassVar[int]
    INPUT_FIELD_NUMBER: _ClassVar[int]
    path: str
    input: _containers.RepeatedCompositeFieldContainer[PathValue]
    def __init__(self, path: _Optional[str] = ..., input: _Optional[_Iterable[_Union[PathValue, _Mapping]]] = ...) -> None: ...

class ExecuteResponse(_message.Message):
    __slots__ = ("output",)
    OUTPUT_FIELD_NUMBER: _ClassVar[int]
    output: _containers.RepeatedCompositeFieldContainer[PathValue]
    def __init__(self, output: _Optional[_Iterable[_Union[PathValue, _Mapping]]] = ...) -> None: ...

class ModuleData(_message.Message):
    __slots__ = ("name", "organization", "revision")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    name: str
    organization: str
    revision: str
    def __init__(self, name: _Optional[str] = ..., organization: _Optional[str] = ..., revision: _Optional[str] = ...) -> None: ...

class PathValue(_message.Message):
    __slots__ = ("path", "value")
    PATH_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    path: str
    value: str
    def __init__(self, path: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class DataTree(_message.Message):
    __slots__ = ("encoding", "data")
    ENCODING_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    encoding: Encoding
    data: str
    def __init__(self, encoding: _Optional[_Union[Encoding, str]] = ..., data: _Optional[str] = ...) -> None: ...
