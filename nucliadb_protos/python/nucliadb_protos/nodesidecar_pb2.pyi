"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import nucliadb_protos.noderesources_pb2
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions
from nucliadb_protos.noderesources_pb2 import (
    EmptyQuery as EmptyQuery,
    EmptyResponse as EmptyResponse,
    IndexMetadata as IndexMetadata,
    IndexParagraph as IndexParagraph,
    IndexParagraphs as IndexParagraphs,
    ParagraphMetadata as ParagraphMetadata,
    Position as Position,
    Resource as Resource,
    ResourceID as ResourceID,
    SentenceMetadata as SentenceMetadata,
    Shard as Shard,
    ShardCleaned as ShardCleaned,
    ShardCreated as ShardCreated,
    ShardId as ShardId,
    ShardIds as ShardIds,
    ShardList as ShardList,
    ShardMetadata as ShardMetadata,
    TextInformation as TextInformation,
    VectorSentence as VectorSentence,
    VectorSetID as VectorSetID,
    VectorSetList as VectorSetList,
)

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class Counter(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCES_FIELD_NUMBER: builtins.int
    PARAGRAPHS_FIELD_NUMBER: builtins.int
    resources: builtins.int
    paragraphs: builtins.int
    def __init__(
        self,
        *,
        resources: builtins.int = ...,
        paragraphs: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["paragraphs", b"paragraphs", "resources", b"resources"]) -> None: ...

global___Counter = Counter

@typing_extensions.final
class ShadowShardResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SUCCESS_FIELD_NUMBER: builtins.int
    SHARD_FIELD_NUMBER: builtins.int
    success: builtins.bool
    @property
    def shard(self) -> nucliadb_protos.noderesources_pb2.ShardId: ...
    def __init__(
        self,
        *,
        success: builtins.bool = ...,
        shard: nucliadb_protos.noderesources_pb2.ShardId | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["shard", b"shard"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["shard", b"shard", "success", b"success"]) -> None: ...

global___ShadowShardResponse = ShadowShardResponse
