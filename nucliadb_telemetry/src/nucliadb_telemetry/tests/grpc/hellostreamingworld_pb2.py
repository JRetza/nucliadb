# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nucliadb_telemetry/tests/grpc/hellostreamingworld.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n7nucliadb_telemetry/tests/grpc/hellostreamingworld.proto\x12\x13hellostreamingworld"3\n\x0cHelloRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x15\n\rnum_greetings\x18\x02 \x01(\t"\x1d\n\nHelloReply\x12\x0f\n\x07message\x18\x01 \x01(\t2b\n\x0cMultiGreeter\x12R\n\x08sayHello\x12!.hellostreamingworld.HelloRequest\x1a\x1f.hellostreamingworld.HelloReply"\x00\x30\x01\x42\x0f\n\x07\x65x.grpc\xa2\x02\x03HSWb\x06proto3'
)


_HELLOREQUEST = DESCRIPTOR.message_types_by_name["HelloRequest"]
_HELLOREPLY = DESCRIPTOR.message_types_by_name["HelloReply"]
HelloRequest = _reflection.GeneratedProtocolMessageType(
    "HelloRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _HELLOREQUEST,
        "__module__": "nucliadb_telemetry.tests.grpc.hellostreamingworld_pb2",
        # @@protoc_insertion_point(class_scope:hellostreamingworld.HelloRequest)
    },
)
_sym_db.RegisterMessage(HelloRequest)

HelloReply = _reflection.GeneratedProtocolMessageType(
    "HelloReply",
    (_message.Message,),
    {
        "DESCRIPTOR": _HELLOREPLY,
        "__module__": "nucliadb_telemetry.tests.grpc.hellostreamingworld_pb2",
        # @@protoc_insertion_point(class_scope:hellostreamingworld.HelloReply)
    },
)
_sym_db.RegisterMessage(HelloReply)

_MULTIGREETER = DESCRIPTOR.services_by_name["MultiGreeter"]
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"\n\007ex.grpc\242\002\003HSW"
    _HELLOREQUEST._serialized_start = 80
    _HELLOREQUEST._serialized_end = 131
    _HELLOREPLY._serialized_start = 133
    _HELLOREPLY._serialized_end = 162
    _MULTIGREETER._serialized_start = 164
    _MULTIGREETER._serialized_end = 262
# @@protoc_insertion_point(module_scope)
