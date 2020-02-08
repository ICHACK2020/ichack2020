# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='api.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\tapi.proto\"4\n\x07\x61piCall\x12\x0f\n\x07\x63onv_id\x18\x01 \x01(\t\x12\x0b\n\x03uid\x18\x02 \x01(\x08\x12\x0b\n\x03msg\x18\x03 \x01(\t\"Q\n\x0b\x61piResponse\x12\x0f\n\x07\x63onv_id\x18\x01 \x01(\t\x12\x0b\n\x03uid\x18\x02 \x01(\x08\x12\r\n\x05score\x18\x03 \x01(\x02\x12\x15\n\rrolling_score\x18\x04 \x01(\x02\x32[\n\x07Process\x12)\n\tRelevance\x12\x08.apiCall\x1a\x0c.apiResponse\"\x00(\x01\x30\x01\x12%\n\x05Troll\x12\x08.apiCall\x1a\x0c.apiResponse\"\x00(\x01\x30\x01\x62\x06proto3')
)




_APICALL = _descriptor.Descriptor(
  name='apiCall',
  full_name='apiCall',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='conv_id', full_name='apiCall.conv_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uid', full_name='apiCall.uid', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='msg', full_name='apiCall.msg', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=13,
  serialized_end=65,
)


_APIRESPONSE = _descriptor.Descriptor(
  name='apiResponse',
  full_name='apiResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='conv_id', full_name='apiResponse.conv_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uid', full_name='apiResponse.uid', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='score', full_name='apiResponse.score', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rolling_score', full_name='apiResponse.rolling_score', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=67,
  serialized_end=148,
)

DESCRIPTOR.message_types_by_name['apiCall'] = _APICALL
DESCRIPTOR.message_types_by_name['apiResponse'] = _APIRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

apiCall = _reflection.GeneratedProtocolMessageType('apiCall', (_message.Message,), {
  'DESCRIPTOR' : _APICALL,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:apiCall)
  })
_sym_db.RegisterMessage(apiCall)

apiResponse = _reflection.GeneratedProtocolMessageType('apiResponse', (_message.Message,), {
  'DESCRIPTOR' : _APIRESPONSE,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:apiResponse)
  })
_sym_db.RegisterMessage(apiResponse)



_PROCESS = _descriptor.ServiceDescriptor(
  name='Process',
  full_name='Process',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=150,
  serialized_end=241,
  methods=[
  _descriptor.MethodDescriptor(
    name='Relevance',
    full_name='Process.Relevance',
    index=0,
    containing_service=None,
    input_type=_APICALL,
    output_type=_APIRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Troll',
    full_name='Process.Troll',
    index=1,
    containing_service=None,
    input_type=_APICALL,
    output_type=_APIRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_PROCESS)

DESCRIPTOR.services_by_name['Process'] = _PROCESS

# @@protoc_insertion_point(module_scope)
