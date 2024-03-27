# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nucliadb_protos/audit.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from nucliadb_protos import nodereader_pb2 as nucliadb__protos_dot_nodereader__pb2
try:
  nucliadb__protos_dot_noderesources__pb2 = nucliadb__protos_dot_nodereader__pb2.nucliadb__protos_dot_noderesources__pb2
except AttributeError:
  nucliadb__protos_dot_noderesources__pb2 = nucliadb__protos_dot_nodereader__pb2.nucliadb_protos.noderesources_pb2
try:
  nucliadb__protos_dot_utils__pb2 = nucliadb__protos_dot_nodereader__pb2.nucliadb__protos_dot_utils__pb2
except AttributeError:
  nucliadb__protos_dot_utils__pb2 = nucliadb__protos_dot_nodereader__pb2.nucliadb_protos.utils_pb2
try:
  nucliadb__protos_dot_utils__pb2 = nucliadb__protos_dot_nodereader__pb2.nucliadb__protos_dot_utils__pb2
except AttributeError:
  nucliadb__protos_dot_utils__pb2 = nucliadb__protos_dot_nodereader__pb2.nucliadb_protos.utils_pb2
from nucliadb_protos import resources_pb2 as nucliadb__protos_dot_resources__pb2
try:
  nucliadb__protos_dot_utils__pb2 = nucliadb__protos_dot_resources__pb2.nucliadb__protos_dot_utils__pb2
except AttributeError:
  nucliadb__protos_dot_utils__pb2 = nucliadb__protos_dot_resources__pb2.nucliadb_protos.utils_pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bnucliadb_protos/audit.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a nucliadb_protos/nodereader.proto\x1a\x1fnucliadb_protos/resources.proto\"\xde\x01\n\nAuditField\x12\'\n\x06\x61\x63tion\x18\x01 \x01(\x0e\x32\x17.AuditField.FieldAction\x12\x0c\n\x04size\x18\x02 \x01(\x05\x12\x16\n\nsize_delta\x18\x03 \x01(\x05\x42\x02\x18\x01\x12\x10\n\x08\x66ield_id\x18\x04 \x01(\t\x12(\n\nfield_type\x18\x05 \x01(\x0e\x32\x14.resources.FieldType\x12\x10\n\x08\x66ilename\x18\x06 \x01(\t\"3\n\x0b\x46ieldAction\x12\t\n\x05\x41\x44\x44\x45\x44\x10\x00\x12\x0c\n\x08MODIFIED\x10\x01\x12\x0b\n\x07\x44\x45LETED\x10\x02\"4\n\x0e\x41uditKBCounter\x12\x12\n\nparagraphs\x18\x02 \x01(\x03\x12\x0e\n\x06\x66ields\x18\x03 \x01(\x03\"+\n\x0b\x43hatContext\x12\x0e\n\x06\x61uthor\x18\x01 \x01(\t\x12\x0c\n\x04text\x18\x02 \x01(\t\"\xa9\x01\n\tChatAudit\x12\x10\n\x08question\x18\x01 \x01(\t\x12\x13\n\x06\x61nswer\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x1f\n\x12rephrased_question\x18\x03 \x01(\tH\x01\x88\x01\x01\x12\x1d\n\x07\x63ontext\x18\x04 \x03(\x0b\x32\x0c.ChatContext\x12\x13\n\x0blearning_id\x18\x05 \x01(\tB\t\n\x07_answerB\x15\n\x13_rephrased_question\"\x81\x05\n\x0c\x41uditRequest\x12%\n\x04type\x18\x01 \x01(\x0e\x32\x17.AuditRequest.AuditType\x12\x0c\n\x04kbid\x18\x02 \x01(\t\x12\x0e\n\x06userid\x18\x04 \x01(\t\x12(\n\x04time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0e\n\x06\x66ields\x18\x06 \x03(\t\x12)\n\x06search\x18\x07 \x01(\x0b\x32\x19.nodereader.SearchRequest\x12\x0e\n\x06timeit\x18\x08 \x01(\x02\x12\x0e\n\x06origin\x18\t \x01(\t\x12\x0b\n\x03rid\x18\n \x01(\t\x12\x0c\n\x04task\x18\x0b \x01(\t\x12\x11\n\tresources\x18\x0c \x01(\x05\x12*\n\x0e\x66ield_metadata\x18\r \x03(\x0b\x32\x12.resources.FieldID\x12!\n\x0c\x66ields_audit\x18\x0e \x03(\x0b\x32\x0b.AuditField\x12 \n\x0b\x63lient_type\x18\x10 \x01(\x0e\x32\x0b.ClientType\x12\x10\n\x08trace_id\x18\x11 \x01(\t\x12#\n\nkb_counter\x18\x12 \x01(\x0b\x32\x0f.AuditKBCounter\x12\x18\n\x04\x63hat\x18\x13 \x01(\x0b\x32\n.ChatAudit\x12\x0f\n\x07success\x18\x14 \x01(\x08\"\xa5\x01\n\tAuditType\x12\x0b\n\x07VISITED\x10\x00\x12\x0c\n\x08MODIFIED\x10\x01\x12\x0b\n\x07\x44\x45LETED\x10\x02\x12\x07\n\x03NEW\x10\x03\x12\x0b\n\x07STARTED\x10\x04\x12\x0b\n\x07STOPPED\x10\x05\x12\n\n\x06SEARCH\x10\x06\x12\r\n\tPROCESSED\x10\x07\x12\x0e\n\nKB_DELETED\x10\x08\x12\x0b\n\x07SUGGEST\x10\t\x12\x0b\n\x07INDEXED\x10\n\x12\x08\n\x04\x43HAT\x10\x0b*\\\n\nClientType\x12\x07\n\x03\x41PI\x10\x00\x12\x07\n\x03WEB\x10\x01\x12\n\n\x06WIDGET\x10\x02\x12\x0b\n\x07\x44\x45SKTOP\x10\x03\x12\r\n\tDASHBOARD\x10\x04\x12\x14\n\x10\x43HROME_EXTENSION\x10\x05\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'nucliadb_protos.audit_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _AUDITFIELD.fields_by_name['size_delta']._options = None
  _AUDITFIELD.fields_by_name['size_delta']._serialized_options = b'\030\001'
  _globals['_CLIENTTYPE']._serialized_start=1271
  _globals['_CLIENTTYPE']._serialized_end=1363
  _globals['_AUDITFIELD']._serialized_start=132
  _globals['_AUDITFIELD']._serialized_end=354
  _globals['_AUDITFIELD_FIELDACTION']._serialized_start=303
  _globals['_AUDITFIELD_FIELDACTION']._serialized_end=354
  _globals['_AUDITKBCOUNTER']._serialized_start=356
  _globals['_AUDITKBCOUNTER']._serialized_end=408
  _globals['_CHATCONTEXT']._serialized_start=410
  _globals['_CHATCONTEXT']._serialized_end=453
  _globals['_CHATAUDIT']._serialized_start=456
  _globals['_CHATAUDIT']._serialized_end=625
  _globals['_AUDITREQUEST']._serialized_start=628
  _globals['_AUDITREQUEST']._serialized_end=1269
  _globals['_AUDITREQUEST_AUDITTYPE']._serialized_start=1104
  _globals['_AUDITREQUEST_AUDITTYPE']._serialized_end=1269
# @@protoc_insertion_point(module_scope)
