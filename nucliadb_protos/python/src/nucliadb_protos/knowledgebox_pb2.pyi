"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import nucliadb_protos.nodewriter_pb2
import nucliadb_protos.utils_pb2
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions
from nucliadb_protos.nodewriter_pb2 import (
    CREATION as CREATION,
    DELETION as DELETION,
    DENSE_F32 as DENSE_F32,
    GarbageCollectorResponse as GarbageCollectorResponse,
    IndexMessage as IndexMessage,
    IndexMessageSource as IndexMessageSource,
    MergeResponse as MergeResponse,
    NewShardRequest as NewShardRequest,
    NewVectorSetRequest as NewVectorSetRequest,
    OpStatus as OpStatus,
    PROCESSOR as PROCESSOR,
    TypeMessage as TypeMessage,
    VectorIndexConfig as VectorIndexConfig,
    VectorType as VectorType,
    WRITER as WRITER,
)
from nucliadb_protos.utils_pb2 import (
    COSINE as COSINE,
    DOT as DOT,
    EXPERIMENTAL as EXPERIMENTAL,
    ExtractedText as ExtractedText,
    Relation as Relation,
    RelationMetadata as RelationMetadata,
    RelationNode as RelationNode,
    ReleaseChannel as ReleaseChannel,
    STABLE as STABLE,
    Security as Security,
    UserVector as UserVector,
    UserVectorSet as UserVectorSet,
    UserVectors as UserVectors,
    UserVectorsList as UserVectorsList,
    Vector as Vector,
    VectorObject as VectorObject,
    VectorSimilarity as VectorSimilarity,
    Vectors as Vectors,
)

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _KnowledgeBoxResponseStatus:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _KnowledgeBoxResponseStatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_KnowledgeBoxResponseStatus.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    OK: _KnowledgeBoxResponseStatus.ValueType  # 0
    CONFLICT: _KnowledgeBoxResponseStatus.ValueType  # 1
    NOTFOUND: _KnowledgeBoxResponseStatus.ValueType  # 2
    ERROR: _KnowledgeBoxResponseStatus.ValueType  # 3

class KnowledgeBoxResponseStatus(_KnowledgeBoxResponseStatus, metaclass=_KnowledgeBoxResponseStatusEnumTypeWrapper): ...

OK: KnowledgeBoxResponseStatus.ValueType  # 0
CONFLICT: KnowledgeBoxResponseStatus.ValueType  # 1
NOTFOUND: KnowledgeBoxResponseStatus.ValueType  # 2
ERROR: KnowledgeBoxResponseStatus.ValueType  # 3
global___KnowledgeBoxResponseStatus = KnowledgeBoxResponseStatus

@typing.final
class KnowledgeBoxID(google.protobuf.message.Message):
    """ID"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SLUG_FIELD_NUMBER: builtins.int
    UUID_FIELD_NUMBER: builtins.int
    slug: builtins.str
    uuid: builtins.str
    def __init__(
        self,
        *,
        slug: builtins.str = ...,
        uuid: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["slug", b"slug", "uuid", b"uuid"]) -> None: ...

global___KnowledgeBoxID = KnowledgeBoxID

@typing.final
class KnowledgeBoxConfig(google.protobuf.message.Message):
    """CONFIG"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TITLE_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    SLUG_FIELD_NUMBER: builtins.int
    MIGRATION_VERSION_FIELD_NUMBER: builtins.int
    ENABLED_FILTERS_FIELD_NUMBER: builtins.int
    ENABLED_INSIGHTS_FIELD_NUMBER: builtins.int
    DISABLE_VECTORS_FIELD_NUMBER: builtins.int
    RELEASE_CHANNEL_FIELD_NUMBER: builtins.int
    title: builtins.str
    description: builtins.str
    slug: builtins.str
    migration_version: builtins.int
    disable_vectors: builtins.bool
    release_channel: nucliadb_protos.utils_pb2.ReleaseChannel.ValueType
    """DEPRECATED: duplicated field also stored in `writer.proto Shards`"""
    @property
    def enabled_filters(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def enabled_insights(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        title: builtins.str = ...,
        description: builtins.str = ...,
        slug: builtins.str = ...,
        migration_version: builtins.int = ...,
        enabled_filters: collections.abc.Iterable[builtins.str] | None = ...,
        enabled_insights: collections.abc.Iterable[builtins.str] | None = ...,
        disable_vectors: builtins.bool = ...,
        release_channel: nucliadb_protos.utils_pb2.ReleaseChannel.ValueType = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["description", b"description", "disable_vectors", b"disable_vectors", "enabled_filters", b"enabled_filters", "enabled_insights", b"enabled_insights", "migration_version", b"migration_version", "release_channel", b"release_channel", "slug", b"slug", "title", b"title"]) -> None: ...

global___KnowledgeBoxConfig = KnowledgeBoxConfig

@typing.final
class KnowledgeBoxNew(google.protobuf.message.Message):
    """NEW"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SLUG_FIELD_NUMBER: builtins.int
    CONFIG_FIELD_NUMBER: builtins.int
    FORCEUUID_FIELD_NUMBER: builtins.int
    SIMILARITY_FIELD_NUMBER: builtins.int
    VECTOR_DIMENSION_FIELD_NUMBER: builtins.int
    DEFAULT_MIN_SCORE_FIELD_NUMBER: builtins.int
    MATRYOSHKA_DIMENSIONS_FIELD_NUMBER: builtins.int
    LEARNING_CONFIG_FIELD_NUMBER: builtins.int
    RELEASE_CHANNEL_FIELD_NUMBER: builtins.int
    slug: builtins.str
    forceuuid: builtins.str
    """this fields are only set by backend when creating hosted KBs"""
    similarity: nucliadb_protos.utils_pb2.VectorSimilarity.ValueType
    vector_dimension: builtins.int
    default_min_score: builtins.float
    learning_config: builtins.str
    """this field are only used by NucliaDB Writer API when creating a KB. Used
    in onprem scenarios
    DEPRECATED: onprem don't forward requests to ingest gRPC anymore
    """
    release_channel: nucliadb_protos.utils_pb2.ReleaseChannel.ValueType
    """release channel, although not used when backend creates hosted KBs, it's
    recomputed and changed depending on the environment
    """
    @property
    def config(self) -> global___KnowledgeBoxConfig: ...
    @property
    def matryoshka_dimensions(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    def __init__(
        self,
        *,
        slug: builtins.str = ...,
        config: global___KnowledgeBoxConfig | None = ...,
        forceuuid: builtins.str = ...,
        similarity: nucliadb_protos.utils_pb2.VectorSimilarity.ValueType = ...,
        vector_dimension: builtins.int | None = ...,
        default_min_score: builtins.float | None = ...,
        matryoshka_dimensions: collections.abc.Iterable[builtins.int] | None = ...,
        learning_config: builtins.str = ...,
        release_channel: nucliadb_protos.utils_pb2.ReleaseChannel.ValueType = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["_default_min_score", b"_default_min_score", "_vector_dimension", b"_vector_dimension", "config", b"config", "default_min_score", b"default_min_score", "vector_dimension", b"vector_dimension"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["_default_min_score", b"_default_min_score", "_vector_dimension", b"_vector_dimension", "config", b"config", "default_min_score", b"default_min_score", "forceuuid", b"forceuuid", "learning_config", b"learning_config", "matryoshka_dimensions", b"matryoshka_dimensions", "release_channel", b"release_channel", "similarity", b"similarity", "slug", b"slug", "vector_dimension", b"vector_dimension"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["_default_min_score", b"_default_min_score"]) -> typing.Literal["default_min_score"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["_vector_dimension", b"_vector_dimension"]) -> typing.Literal["vector_dimension"] | None: ...

global___KnowledgeBoxNew = KnowledgeBoxNew

@typing.final
class NewKnowledgeBoxResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    STATUS_FIELD_NUMBER: builtins.int
    UUID_FIELD_NUMBER: builtins.int
    status: global___KnowledgeBoxResponseStatus.ValueType
    uuid: builtins.str
    def __init__(
        self,
        *,
        status: global___KnowledgeBoxResponseStatus.ValueType = ...,
        uuid: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["status", b"status", "uuid", b"uuid"]) -> None: ...

global___NewKnowledgeBoxResponse = NewKnowledgeBoxResponse

@typing.final
class KnowledgeBoxUpdate(google.protobuf.message.Message):
    """UPDATE"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SLUG_FIELD_NUMBER: builtins.int
    UUID_FIELD_NUMBER: builtins.int
    CONFIG_FIELD_NUMBER: builtins.int
    slug: builtins.str
    uuid: builtins.str
    @property
    def config(self) -> global___KnowledgeBoxConfig: ...
    def __init__(
        self,
        *,
        slug: builtins.str = ...,
        uuid: builtins.str = ...,
        config: global___KnowledgeBoxConfig | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["config", b"config"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["config", b"config", "slug", b"slug", "uuid", b"uuid"]) -> None: ...

global___KnowledgeBoxUpdate = KnowledgeBoxUpdate

@typing.final
class UpdateKnowledgeBoxResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    STATUS_FIELD_NUMBER: builtins.int
    UUID_FIELD_NUMBER: builtins.int
    status: global___KnowledgeBoxResponseStatus.ValueType
    uuid: builtins.str
    def __init__(
        self,
        *,
        status: global___KnowledgeBoxResponseStatus.ValueType = ...,
        uuid: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["status", b"status", "uuid", b"uuid"]) -> None: ...

global___UpdateKnowledgeBoxResponse = UpdateKnowledgeBoxResponse

@typing.final
class DeleteKnowledgeBoxResponse(google.protobuf.message.Message):
    """DELETE"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    STATUS_FIELD_NUMBER: builtins.int
    status: global___KnowledgeBoxResponseStatus.ValueType
    def __init__(
        self,
        *,
        status: global___KnowledgeBoxResponseStatus.ValueType = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["status", b"status"]) -> None: ...

global___DeleteKnowledgeBoxResponse = DeleteKnowledgeBoxResponse

@typing.final
class Label(google.protobuf.message.Message):
    """Labels on a Knowledge Box"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TITLE_FIELD_NUMBER: builtins.int
    RELATED_FIELD_NUMBER: builtins.int
    TEXT_FIELD_NUMBER: builtins.int
    URI_FIELD_NUMBER: builtins.int
    title: builtins.str
    related: builtins.str
    text: builtins.str
    uri: builtins.str
    def __init__(
        self,
        *,
        title: builtins.str = ...,
        related: builtins.str = ...,
        text: builtins.str = ...,
        uri: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["related", b"related", "text", b"text", "title", b"title", "uri", b"uri"]) -> None: ...

global___Label = Label

@typing.final
class LabelSet(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _LabelSetKind:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _LabelSetKindEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[LabelSet._LabelSetKind.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        RESOURCES: LabelSet._LabelSetKind.ValueType  # 0
        PARAGRAPHS: LabelSet._LabelSetKind.ValueType  # 1
        SENTENCES: LabelSet._LabelSetKind.ValueType  # 2
        SELECTIONS: LabelSet._LabelSetKind.ValueType  # 3

    class LabelSetKind(_LabelSetKind, metaclass=_LabelSetKindEnumTypeWrapper): ...
    RESOURCES: LabelSet.LabelSetKind.ValueType  # 0
    PARAGRAPHS: LabelSet.LabelSetKind.ValueType  # 1
    SENTENCES: LabelSet.LabelSetKind.ValueType  # 2
    SELECTIONS: LabelSet.LabelSetKind.ValueType  # 3

    TITLE_FIELD_NUMBER: builtins.int
    COLOR_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    MULTIPLE_FIELD_NUMBER: builtins.int
    KIND_FIELD_NUMBER: builtins.int
    title: builtins.str
    color: builtins.str
    multiple: builtins.bool
    @property
    def labels(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Label]: ...
    @property
    def kind(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[global___LabelSet.LabelSetKind.ValueType]: ...
    def __init__(
        self,
        *,
        title: builtins.str = ...,
        color: builtins.str = ...,
        labels: collections.abc.Iterable[global___Label] | None = ...,
        multiple: builtins.bool = ...,
        kind: collections.abc.Iterable[global___LabelSet.LabelSetKind.ValueType] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["color", b"color", "kind", b"kind", "labels", b"labels", "multiple", b"multiple", "title", b"title"]) -> None: ...

global___LabelSet = LabelSet

@typing.final
class Labels(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class LabelsetEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        @property
        def value(self) -> global___LabelSet: ...
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: global___LabelSet | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["value", b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["key", b"key", "value", b"value"]) -> None: ...

    LABELSET_FIELD_NUMBER: builtins.int
    @property
    def labelset(self) -> google.protobuf.internal.containers.MessageMap[builtins.str, global___LabelSet]: ...
    def __init__(
        self,
        *,
        labelset: collections.abc.Mapping[builtins.str, global___LabelSet] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["labelset", b"labelset"]) -> None: ...

global___Labels = Labels

@typing.final
class Entity(google.protobuf.message.Message):
    """Entities on a Knowledge Box"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VALUE_FIELD_NUMBER: builtins.int
    REPRESENTS_FIELD_NUMBER: builtins.int
    MERGED_FIELD_NUMBER: builtins.int
    DELETED_FIELD_NUMBER: builtins.int
    value: builtins.str
    merged: builtins.bool
    deleted: builtins.bool
    @property
    def represents(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        value: builtins.str = ...,
        represents: collections.abc.Iterable[builtins.str] | None = ...,
        merged: builtins.bool = ...,
        deleted: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["deleted", b"deleted", "merged", b"merged", "represents", b"represents", "value", b"value"]) -> None: ...

global___Entity = Entity

@typing.final
class EntitiesGroupSummary(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TITLE_FIELD_NUMBER: builtins.int
    COLOR_FIELD_NUMBER: builtins.int
    CUSTOM_FIELD_NUMBER: builtins.int
    title: builtins.str
    color: builtins.str
    custom: builtins.bool
    def __init__(
        self,
        *,
        title: builtins.str = ...,
        color: builtins.str = ...,
        custom: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["color", b"color", "custom", b"custom", "title", b"title"]) -> None: ...

global___EntitiesGroupSummary = EntitiesGroupSummary

@typing.final
class EntitiesGroup(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class EntitiesEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        @property
        def value(self) -> global___Entity: ...
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: global___Entity | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["value", b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["key", b"key", "value", b"value"]) -> None: ...

    ENTITIES_FIELD_NUMBER: builtins.int
    TITLE_FIELD_NUMBER: builtins.int
    COLOR_FIELD_NUMBER: builtins.int
    CUSTOM_FIELD_NUMBER: builtins.int
    title: builtins.str
    color: builtins.str
    custom: builtins.bool
    @property
    def entities(self) -> google.protobuf.internal.containers.MessageMap[builtins.str, global___Entity]: ...
    def __init__(
        self,
        *,
        entities: collections.abc.Mapping[builtins.str, global___Entity] | None = ...,
        title: builtins.str = ...,
        color: builtins.str = ...,
        custom: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["color", b"color", "custom", b"custom", "entities", b"entities", "title", b"title"]) -> None: ...

global___EntitiesGroup = EntitiesGroup

@typing.final
class DeletedEntitiesGroups(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ENTITIES_GROUPS_FIELD_NUMBER: builtins.int
    @property
    def entities_groups(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        entities_groups: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["entities_groups", b"entities_groups"]) -> None: ...

global___DeletedEntitiesGroups = DeletedEntitiesGroups

@typing.final
class EntitiesGroups(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class EntitiesGroupsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        @property
        def value(self) -> global___EntitiesGroup: ...
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: global___EntitiesGroup | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["value", b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["key", b"key", "value", b"value"]) -> None: ...

    ENTITIES_GROUPS_FIELD_NUMBER: builtins.int
    @property
    def entities_groups(self) -> google.protobuf.internal.containers.MessageMap[builtins.str, global___EntitiesGroup]: ...
    def __init__(
        self,
        *,
        entities_groups: collections.abc.Mapping[builtins.str, global___EntitiesGroup] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["entities_groups", b"entities_groups"]) -> None: ...

global___EntitiesGroups = EntitiesGroups

@typing.final
class EntityGroupDuplicateIndex(google.protobuf.message.Message):
    """
    Structure to represent all duplicates defined in a kb
        - call it an "Index" because it should include flattened version of all duplicated entries
        - this allows 1 call to pull all duplicates
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class EntityDuplicates(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        DUPLICATES_FIELD_NUMBER: builtins.int
        @property
        def duplicates(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
        def __init__(
            self,
            *,
            duplicates: collections.abc.Iterable[builtins.str] | None = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["duplicates", b"duplicates"]) -> None: ...

    @typing.final
    class EntityGroupDuplicates(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        @typing.final
        class EntitiesEntry(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor

            KEY_FIELD_NUMBER: builtins.int
            VALUE_FIELD_NUMBER: builtins.int
            key: builtins.str
            @property
            def value(self) -> global___EntityGroupDuplicateIndex.EntityDuplicates: ...
            def __init__(
                self,
                *,
                key: builtins.str = ...,
                value: global___EntityGroupDuplicateIndex.EntityDuplicates | None = ...,
            ) -> None: ...
            def HasField(self, field_name: typing.Literal["value", b"value"]) -> builtins.bool: ...
            def ClearField(self, field_name: typing.Literal["key", b"key", "value", b"value"]) -> None: ...

        ENTITIES_FIELD_NUMBER: builtins.int
        @property
        def entities(self) -> google.protobuf.internal.containers.MessageMap[builtins.str, global___EntityGroupDuplicateIndex.EntityDuplicates]: ...
        def __init__(
            self,
            *,
            entities: collections.abc.Mapping[builtins.str, global___EntityGroupDuplicateIndex.EntityDuplicates] | None = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["entities", b"entities"]) -> None: ...

    @typing.final
    class EntitiesGroupsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        @property
        def value(self) -> global___EntityGroupDuplicateIndex.EntityGroupDuplicates: ...
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: global___EntityGroupDuplicateIndex.EntityGroupDuplicates | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["value", b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["key", b"key", "value", b"value"]) -> None: ...

    ENTITIES_GROUPS_FIELD_NUMBER: builtins.int
    @property
    def entities_groups(self) -> google.protobuf.internal.containers.MessageMap[builtins.str, global___EntityGroupDuplicateIndex.EntityGroupDuplicates]: ...
    def __init__(
        self,
        *,
        entities_groups: collections.abc.Mapping[builtins.str, global___EntityGroupDuplicateIndex.EntityGroupDuplicates] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["entities_groups", b"entities_groups"]) -> None: ...

global___EntityGroupDuplicateIndex = EntityGroupDuplicateIndex

@typing.final
class VectorSet(google.protobuf.message.Message):
    """Vectorsets"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DIMENSION_FIELD_NUMBER: builtins.int
    SIMILARITY_FIELD_NUMBER: builtins.int
    dimension: builtins.int
    similarity: nucliadb_protos.utils_pb2.VectorSimilarity.ValueType
    def __init__(
        self,
        *,
        dimension: builtins.int = ...,
        similarity: nucliadb_protos.utils_pb2.VectorSimilarity.ValueType = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["dimension", b"dimension", "similarity", b"similarity"]) -> None: ...

global___VectorSet = VectorSet

@typing.final
class VectorSets(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class VectorsetsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        @property
        def value(self) -> global___VectorSet: ...
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: global___VectorSet | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["value", b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["key", b"key", "value", b"value"]) -> None: ...

    VECTORSETS_FIELD_NUMBER: builtins.int
    @property
    def vectorsets(self) -> google.protobuf.internal.containers.MessageMap[builtins.str, global___VectorSet]: ...
    def __init__(
        self,
        *,
        vectorsets: collections.abc.Mapping[builtins.str, global___VectorSet] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["vectorsets", b"vectorsets"]) -> None: ...

global___VectorSets = VectorSets

@typing.final
class VectorSetConfig(google.protobuf.message.Message):
    """Configuration values for a vectorset"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VECTORSET_ID_FIELD_NUMBER: builtins.int
    VECTORSET_INDEX_CONFIG_FIELD_NUMBER: builtins.int
    MATRYOSHKA_DIMENSIONS_FIELD_NUMBER: builtins.int
    vectorset_id: builtins.str
    @property
    def vectorset_index_config(self) -> nucliadb_protos.nodewriter_pb2.VectorIndexConfig: ...
    @property
    def matryoshka_dimensions(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]:
        """list of possible subdivisions of the matryoshka embeddings (if the model
        supports it)
        """

    def __init__(
        self,
        *,
        vectorset_id: builtins.str = ...,
        vectorset_index_config: nucliadb_protos.nodewriter_pb2.VectorIndexConfig | None = ...,
        matryoshka_dimensions: collections.abc.Iterable[builtins.int] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["vectorset_index_config", b"vectorset_index_config"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["matryoshka_dimensions", b"matryoshka_dimensions", "vectorset_id", b"vectorset_id", "vectorset_index_config", b"vectorset_index_config"]) -> None: ...

global___VectorSetConfig = VectorSetConfig

@typing.final
class KnowledgeBoxVectorSetsConfig(google.protobuf.message.Message):
    """KB vectorsets and their configuration"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VECTORSETS_FIELD_NUMBER: builtins.int
    @property
    def vectorsets(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___VectorSetConfig]: ...
    def __init__(
        self,
        *,
        vectorsets: collections.abc.Iterable[global___VectorSetConfig] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["vectorsets", b"vectorsets"]) -> None: ...

global___KnowledgeBoxVectorSetsConfig = KnowledgeBoxVectorSetsConfig

@typing.final
class TermSynonyms(google.protobuf.message.Message):
    """Synonyms of a Knowledge Box"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SYNONYMS_FIELD_NUMBER: builtins.int
    @property
    def synonyms(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        synonyms: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["synonyms", b"synonyms"]) -> None: ...

global___TermSynonyms = TermSynonyms

@typing.final
class Synonyms(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class TermsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        @property
        def value(self) -> global___TermSynonyms: ...
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: global___TermSynonyms | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["value", b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["key", b"key", "value", b"value"]) -> None: ...

    TERMS_FIELD_NUMBER: builtins.int
    @property
    def terms(self) -> google.protobuf.internal.containers.MessageMap[builtins.str, global___TermSynonyms]: ...
    def __init__(
        self,
        *,
        terms: collections.abc.Mapping[builtins.str, global___TermSynonyms] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["terms", b"terms"]) -> None: ...

global___Synonyms = Synonyms

@typing.final
class SemanticModelMetadata(google.protobuf.message.Message):
    """Metadata of the model associated to the KB"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SIMILARITY_FUNCTION_FIELD_NUMBER: builtins.int
    VECTOR_DIMENSION_FIELD_NUMBER: builtins.int
    DEFAULT_MIN_SCORE_FIELD_NUMBER: builtins.int
    MATRYOSHKA_DIMENSIONS_FIELD_NUMBER: builtins.int
    similarity_function: nucliadb_protos.utils_pb2.VectorSimilarity.ValueType
    vector_dimension: builtins.int
    default_min_score: builtins.float
    @property
    def matryoshka_dimensions(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]:
        """list of possible subdivisions of the matryoshka embeddings (if the model
        supports it)
        """

    def __init__(
        self,
        *,
        similarity_function: nucliadb_protos.utils_pb2.VectorSimilarity.ValueType = ...,
        vector_dimension: builtins.int | None = ...,
        default_min_score: builtins.float | None = ...,
        matryoshka_dimensions: collections.abc.Iterable[builtins.int] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["_default_min_score", b"_default_min_score", "_vector_dimension", b"_vector_dimension", "default_min_score", b"default_min_score", "vector_dimension", b"vector_dimension"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["_default_min_score", b"_default_min_score", "_vector_dimension", b"_vector_dimension", "default_min_score", b"default_min_score", "matryoshka_dimensions", b"matryoshka_dimensions", "similarity_function", b"similarity_function", "vector_dimension", b"vector_dimension"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["_default_min_score", b"_default_min_score"]) -> typing.Literal["default_min_score"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["_vector_dimension", b"_vector_dimension"]) -> typing.Literal["vector_dimension"] | None: ...

global___SemanticModelMetadata = SemanticModelMetadata

@typing.final
class KBConfiguration(google.protobuf.message.Message):
    """Do not update this model without confirmation of internal Learning Config API

    Deprecated
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SEMANTIC_MODEL_FIELD_NUMBER: builtins.int
    GENERATIVE_MODEL_FIELD_NUMBER: builtins.int
    NER_MODEL_FIELD_NUMBER: builtins.int
    ANONYMIZATION_MODEL_FIELD_NUMBER: builtins.int
    VISUAL_LABELING_FIELD_NUMBER: builtins.int
    semantic_model: builtins.str
    generative_model: builtins.str
    ner_model: builtins.str
    anonymization_model: builtins.str
    visual_labeling: builtins.str
    def __init__(
        self,
        *,
        semantic_model: builtins.str = ...,
        generative_model: builtins.str = ...,
        ner_model: builtins.str = ...,
        anonymization_model: builtins.str = ...,
        visual_labeling: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["anonymization_model", b"anonymization_model", "generative_model", b"generative_model", "ner_model", b"ner_model", "semantic_model", b"semantic_model", "visual_labeling", b"visual_labeling"]) -> None: ...

global___KBConfiguration = KBConfiguration
