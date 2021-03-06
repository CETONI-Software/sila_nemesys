# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: DigitalInChannelProvider.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import sila2lib.framework.SiLAFramework_pb2 as SiLAFramework__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='DigitalInChannelProvider.proto',
  package='sila2.de.cetoni.io.digitalinchannelprovider.v1',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1e\x44igitalInChannelProvider.proto\x12.sila2.de.cetoni.io.digitalinchannelprovider.v1\x1a\x13SiLAFramework.proto\"?\n\x0e\x44\x61taType_State\x12-\n\x05State\x18\x01 \x01(\x0b\x32\x1e.sila2.org.silastandard.String\"\x1c\n\x1aSubscribe_State_Parameters\"j\n\x19Subscribe_State_Responses\x12M\n\x05State\x18\x01 \x01(\x0b\x32>.sila2.de.cetoni.io.digitalinchannelprovider.v1.DataType_State2\xc9\x01\n\x18\x44igitalInChannelProvider\x12\xac\x01\n\x0fSubscribe_State\x12J.sila2.de.cetoni.io.digitalinchannelprovider.v1.Subscribe_State_Parameters\x1aI.sila2.de.cetoni.io.digitalinchannelprovider.v1.Subscribe_State_Responses\"\x00\x30\x01\x62\x06proto3'
  ,
  dependencies=[SiLAFramework__pb2.DESCRIPTOR,])




_DATATYPE_STATE = _descriptor.Descriptor(
  name='DataType_State',
  full_name='sila2.de.cetoni.io.digitalinchannelprovider.v1.DataType_State',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='State', full_name='sila2.de.cetoni.io.digitalinchannelprovider.v1.DataType_State.State', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=103,
  serialized_end=166,
)


_SUBSCRIBE_STATE_PARAMETERS = _descriptor.Descriptor(
  name='Subscribe_State_Parameters',
  full_name='sila2.de.cetoni.io.digitalinchannelprovider.v1.Subscribe_State_Parameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=168,
  serialized_end=196,
)


_SUBSCRIBE_STATE_RESPONSES = _descriptor.Descriptor(
  name='Subscribe_State_Responses',
  full_name='sila2.de.cetoni.io.digitalinchannelprovider.v1.Subscribe_State_Responses',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='State', full_name='sila2.de.cetoni.io.digitalinchannelprovider.v1.Subscribe_State_Responses.State', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=198,
  serialized_end=304,
)

_DATATYPE_STATE.fields_by_name['State'].message_type = SiLAFramework__pb2._STRING
_SUBSCRIBE_STATE_RESPONSES.fields_by_name['State'].message_type = _DATATYPE_STATE
DESCRIPTOR.message_types_by_name['DataType_State'] = _DATATYPE_STATE
DESCRIPTOR.message_types_by_name['Subscribe_State_Parameters'] = _SUBSCRIBE_STATE_PARAMETERS
DESCRIPTOR.message_types_by_name['Subscribe_State_Responses'] = _SUBSCRIBE_STATE_RESPONSES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DataType_State = _reflection.GeneratedProtocolMessageType('DataType_State', (_message.Message,), {
  'DESCRIPTOR' : _DATATYPE_STATE,
  '__module__' : 'DigitalInChannelProvider_pb2'
  # @@protoc_insertion_point(class_scope:sila2.de.cetoni.io.digitalinchannelprovider.v1.DataType_State)
  })
_sym_db.RegisterMessage(DataType_State)

Subscribe_State_Parameters = _reflection.GeneratedProtocolMessageType('Subscribe_State_Parameters', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBE_STATE_PARAMETERS,
  '__module__' : 'DigitalInChannelProvider_pb2'
  # @@protoc_insertion_point(class_scope:sila2.de.cetoni.io.digitalinchannelprovider.v1.Subscribe_State_Parameters)
  })
_sym_db.RegisterMessage(Subscribe_State_Parameters)

Subscribe_State_Responses = _reflection.GeneratedProtocolMessageType('Subscribe_State_Responses', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBE_STATE_RESPONSES,
  '__module__' : 'DigitalInChannelProvider_pb2'
  # @@protoc_insertion_point(class_scope:sila2.de.cetoni.io.digitalinchannelprovider.v1.Subscribe_State_Responses)
  })
_sym_db.RegisterMessage(Subscribe_State_Responses)



_DIGITALINCHANNELPROVIDER = _descriptor.ServiceDescriptor(
  name='DigitalInChannelProvider',
  full_name='sila2.de.cetoni.io.digitalinchannelprovider.v1.DigitalInChannelProvider',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=307,
  serialized_end=508,
  methods=[
  _descriptor.MethodDescriptor(
    name='Subscribe_State',
    full_name='sila2.de.cetoni.io.digitalinchannelprovider.v1.DigitalInChannelProvider.Subscribe_State',
    index=0,
    containing_service=None,
    input_type=_SUBSCRIBE_STATE_PARAMETERS,
    output_type=_SUBSCRIBE_STATE_RESPONSES,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_DIGITALINCHANNELPROVIDER)

DESCRIPTOR.services_by_name['DigitalInChannelProvider'] = _DIGITALINCHANNELPROVIDER

# @@protoc_insertion_point(module_scope)
