# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: server.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'server.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cserver.proto\x12\thw1.tasks\"\xaa\x01\n\x08Response\x12\r\n\x05token\x18\x01 \x01(\t\x12\x0e\n\x04info\x18\x02 \x01(\tH\x00\x12\x0f\n\x05\x65rror\x18\x03 \x01(\tH\x00\x12-\n\x0bunknownTask\x18\x07 \x01(\x0b\x32\x16.hw1.tasks.UnknownTaskH\x01\x12)\n\tadderTask\x18\x08 \x01(\x0b\x32\x14.hw1.tasks.AdderTaskH\x01\x42\x06\n\x04\x64\x61taB\x06\n\x04taskJ\x04\x08\x04\x10\x07\"\r\n\x0bUnknownTask\"\x1a\n\tBeginData\x12\r\n\x05\x65mail\x18\x01 \x01(\t\"!\n\tAdderTask\x12\t\n\x01\x61\x18\x01 \x01(\x03\x12\t\n\x01\x62\x18\x02 \x01(\x02\"2\n\x11\x41\x64\x64\x65rTaskResponse\x12\r\n\x05token\x18\x01 \x01(\t\x12\x0e\n\x06result\x18\x02 \x01(\x01\x32z\n\x08Homework\x12\x32\n\x05\x42\x65gin\x12\x14.hw1.tasks.BeginData\x1a\x13.hw1.tasks.Response\x12:\n\x05\x41\x64\x64\x65r\x12\x1c.hw1.tasks.AdderTaskResponse\x1a\x13.hw1.tasks.ResponseB\x02P\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'server_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'P\001'
  _globals['_RESPONSE']._serialized_start=28
  _globals['_RESPONSE']._serialized_end=198
  _globals['_UNKNOWNTASK']._serialized_start=200
  _globals['_UNKNOWNTASK']._serialized_end=213
  _globals['_BEGINDATA']._serialized_start=215
  _globals['_BEGINDATA']._serialized_end=241
  _globals['_ADDERTASK']._serialized_start=243
  _globals['_ADDERTASK']._serialized_end=276
  _globals['_ADDERTASKRESPONSE']._serialized_start=278
  _globals['_ADDERTASKRESPONSE']._serialized_end=328
  _globals['_HOMEWORK']._serialized_start=330
  _globals['_HOMEWORK']._serialized_end=452
# @@protoc_insertion_point(module_scope)
