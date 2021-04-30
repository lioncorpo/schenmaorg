# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/protobuf/api.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import source_context_pb2 as google_dot_protobuf_dot_source__context__pb2
from google.protobuf import type_pb2 as google_dot_protobuf_dot_type__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/protobuf/api.proto',
  package='google.protobuf',
  syntax='proto3',
  serialized_options=b'\n\023com.google.protobufB\010ApiProtoP\001Z+google.golang.org/genproto/protobuf/api;api\242\002\003GPB\252\002\036Google.Protobuf.WellKnownTypes',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x19google/protobuf/api.proto\x12\x0fgoogle.protobuf\x1a$google/protobuf/source_context.proto\x1a\x1agoogle/protobuf/type.proto\"\x81\x02\n\x03\x41pi\x12\x0c\n\x04name\x18\x01 \x01(\t\x12(\n\x07methods\x18\x02 \x03(\x0b\x32\x17.google.protobuf.Method\x12(\n\x07options\x18\x03 \x03(\x0b\x32\x17.google.protobuf.Option\x12\x0f\n\x07version\x18\x04 \x01(\t\x12\x36\n\x0esource_context\x18\x05 \x01(\x0b\x32\x1e.google.protobuf.SourceContext\x12&\n\x06mixins\x18\x06 \x03(\x0b\x32\x16.google.protobuf.Mixin\x12\'\n\x06syntax\x18\x07 \x01(\x0e\x32\x17.google.protobuf.Syntax\"\xd5\x01\n\x06Method\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x18\n\x10request_type_url\x18\x02 \x01(\t\x12\x19\n\x11request_streaming\x18\x03 \x01(\x08\x12\x19\n\x11response_type_url\x18\x04 \x01(\t\x12\x1a\n\x12response_streaming\x18\x05 \x01(\x08\x12(\n\x07options\x18\x06 \x03(\x0b\x32\x17.google.protobuf.Option\x12\'\n\x06syntax\x18\x07 \x01(\x0e\x32\x17.google.protobuf.Syntax\"#\n\x05Mixin\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04root\x18\x02 \x01(\tBu\n\x13\x63om.google.protobufB\x08\x41piProtoP\x01Z+google.golang.org/genproto/protobuf/api;api\xa2\x02\x03GPB\xaa\x02\x1eGoogle.Protobuf.WellKnownTypesb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_source__context__pb2.DESCRIPTOR,google_dot_protobuf_dot_type__pb2.DESCRIPTOR,])




_API = _descriptor.Descriptor(
  name='Api',
  full_name='google.protobuf.Api',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.protobuf.Api.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='methods', full_name='google.protobuf.Api.methods', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='options', full_name='google.protobuf.Api.options', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='version', full_name='google.protobuf.Api.version', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='source_context', full_name='google.protobuf.Api.source_context', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mixins', full_name='google.protobuf.Api.mixins', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='syntax', full_name='google.protobuf.Api.syntax', index=6,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=113,
  serialized_end=370,
)


_METHOD = _descriptor.Descriptor(
  name='Method',
  full_name='google.protobuf.Method',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.protobuf.Method.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='request_type_url', full_name='google.protobuf.Method.request_type_url', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='request_streaming', full_name='google.protobuf.Method.request_streaming', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='response_type_url', full_name='google.protobuf.Method.response_type_url', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='response_streaming', full_name='google.protobuf.Method.response_streaming', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='options', full_name='google.protobuf.Method.options', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='syntax', full_name='google.protobuf.Method.syntax', index=6,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=373,
  serialized_end=586,
)


_MIXIN = _descriptor.Descriptor(
  name='Mixin',
  full_name='google.protobuf.Mixin',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.protobuf.Mixin.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='root', full_name='google.protobuf.Mixin.root', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=588,
  serialized_end=623,
)

_API.fields_by_name['methods'].message_type = _METHOD
_API.fields_by_name['options'].message_type = google_dot_protobuf_dot_type__pb2._OPTION
_API.fields_by_name['source_context'].message_type = google_dot_protobuf_dot_source__context__pb2._SOURCECONTEXT
_API.fields_by_name['mixins'].message_type = _MIXIN
_API.fields_by_name['syntax'].enum_type = google_dot_protobuf_dot_type__pb2._SYNTAX
_METHOD.fields_by_name['options'].message_type = google_dot_protobuf_dot_type__pb2._OPTION
_METHOD.fields_by_name['syntax'].enum_type = google_dot_protobuf_dot_type__pb2._SYNTAX
DESCRIPTOR.message_types_by_name['Api'] = _API
DESCRIPTOR.message_types_by_name['Method'] = _METHOD
DESCRIPTOR.message_types_by_name['Mixin'] = _MIXIN
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Api = _reflection.GeneratedProtocolMessageType('Api', (_message.Message,), {
  'DESCRIPTOR' : _API,
  '__module__' : 'google.protobuf.api_pb2'
  # @@protoc_insertion_point(class_scope:google.protobuf.Api)
  })
_sym_db.RegisterMessage(Api)

Method = _reflection.GeneratedProtocolMessageType('Method', (_message.Message,), {
  'DESCRIPTOR' : _METHOD,
  '__module__' : 'google.protobuf.api_pb2'
  # @@protoc_insertion_point(class_scope:google.protobuf.Method)
  })
_sym_db.RegisterMessage(Method)

Mixin = _reflection.GeneratedProtocolMessageType('Mixin', (_message.Message,), {
  'DESCRIPTOR' : _MIXIN,
  '__module__' : 'google.protobuf.api_pb2'
  # @@protoc_insertion_point(class_scope:google.protobuf.Mixin)
  })
_sym_db.RegisterMessage(Mixin)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
