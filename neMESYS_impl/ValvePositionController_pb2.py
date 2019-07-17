# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ValvePositionController.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import sila2lib.SiLAFramework_pb2 as SiLAFramework__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ValvePositionController.proto',
  package='sila2.de.cetoni.pumps.syringepumps.valvepositioncontroller.v1',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1dValvePositionController.proto\x12=sila2.de.cetoni.pumps.syringepumps.valvepositioncontroller.v1\x1a\x13SiLAFramework.proto\"P\n\x1bSwitchToPosition_Parameters\x12\x31\n\x08Position\x18\x01 \x01(\x0b\x32\x1f.sila2.org.silastandard.Integer\"N\n\x1aSwitchToPosition_Responses\x12\x30\n\x07Success\x18\x01 \x01(\x0b\x32\x1f.sila2.org.silastandard.Boolean\"\x1b\n\x19TogglePosition_Parameters\"L\n\x18TogglePosition_Responses\x12\x30\n\x07Success\x18\x01 \x01(\x0b\x32\x1f.sila2.org.silastandard.Boolean\"\"\n Get_NumberOfPositions_Parameters\"]\n\x1fGet_NumberOfPositions_Responses\x12:\n\x11NumberOfPositions\x18\x01 \x01(\x0b\x32\x1f.sila2.org.silastandard.Integer\"\x1f\n\x1dSubscribe_Position_Parameters\"Q\n\x1cSubscribe_Position_Responses\x12\x31\n\x08Position\x18\x01 \x01(\x0b\x32\x1f.sila2.org.silastandard.Integer2\xda\x06\n\x17ValvePositionController\x12\xc9\x01\n\x10SwitchToPosition\x12Z.sila2.de.cetoni.pumps.syringepumps.valvepositioncontroller.v1.SwitchToPosition_Parameters\x1aY.sila2.de.cetoni.pumps.syringepumps.valvepositioncontroller.v1.SwitchToPosition_Responses\x12\xc3\x01\n\x0eTogglePosition\x12X.sila2.de.cetoni.pumps.syringepumps.valvepositioncontroller.v1.TogglePosition_Parameters\x1aW.sila2.de.cetoni.pumps.syringepumps.valvepositioncontroller.v1.TogglePosition_Responses\x12\xd8\x01\n\x15Get_NumberOfPositions\x12_.sila2.de.cetoni.pumps.syringepumps.valvepositioncontroller.v1.Get_NumberOfPositions_Parameters\x1a^.sila2.de.cetoni.pumps.syringepumps.valvepositioncontroller.v1.Get_NumberOfPositions_Responses\x12\xd1\x01\n\x12Subscribe_Position\x12\\.sila2.de.cetoni.pumps.syringepumps.valvepositioncontroller.v1.Subscribe_Position_Parameters\x1a[.sila2.de.cetoni.pumps.syringepumps.valvepositioncontroller.v1.Subscribe_Position_Responses0\x01\x62\x06proto3')
  ,
  dependencies=[SiLAFramework__pb2.DESCRIPTOR,])




_SWITCHTOPOSITION_PARAMETERS = _descriptor.Descriptor(
  name='SwitchToPosition_Parameters',
  full_name='sila2.de.cetoni.pumps.syringepumps.valvepositioncontroller.v1.SwitchToPosition_Parameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Position', full_name='sila2.de.cetoni.pumps.syringepumps.valvepositioncontroller.v1.SwitchToPosition_Parameters.Position', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=117,
  serialized_end=197,
)


_SWITCHTOPOSITION_RESPONSES = _descriptor.Descriptor(
  name='SwitchToPosition_Responses',
  full_name='sila2.de.cetoni.pumps.syringepumps.valvepositioncontroller.v1.SwitchToPosition_Responses',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Success', full_name='sila2.de.cetoni.pumps.syringepumps.valvepositioncontroller.v1.SwitchToPosition_Responses.Success', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=199,
  serialized_end=277,
)


_TOGGLEPOSITION_PARAMETERS = _descriptor.Descriptor(
  name='TogglePosition_Parameters',
  full_name='sila2.de.cetoni.pumps.syringepumps.valvepositioncontroller.v1.TogglePosition_Parameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
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
  serialized_start=279,
  serialized_end=306,
)


_TOGGLEPOSITION_RESPONSES = _descriptor.Descriptor(
  name='TogglePosition_Responses',
  full_name='sila2.de.cetoni.pumps.syringepumps.valvepositioncontroller.v1.TogglePosition_Responses',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Success', full_name='sila2.de.cetoni.pumps.syringepumps.valvepositioncontroller.v1.TogglePosition_Responses.Success', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=308,
  serialized_end=384,
)


_GET_NUMBEROFPOSITIONS_PARAMETERS = _descriptor.Descriptor(
  name='Get_NumberOfPositions_Parameters',
  full_name='sila2.de.cetoni.pumps.syringepumps.valvepositioncontroller.v1.Get_NumberOfPositions_Parameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
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
  serialized_start=386,
  serialized_end=420,
)


_GET_NUMBEROFPOSITIONS_RESPONSES = _descriptor.Descriptor(
  name='Get_NumberOfPositions_Responses',
  full_name='sila2.de.cetoni.pumps.syringepumps.valvepositioncontroller.v1.Get_NumberOfPositions_Responses',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='NumberOfPositions', full_name='sila2.de.cetoni.pumps.syringepumps.valvepositioncontroller.v1.Get_NumberOfPositions_Responses.NumberOfPositions', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=422,
  serialized_end=515,
)


_SUBSCRIBE_POSITION_PARAMETERS = _descriptor.Descriptor(
  name='Subscribe_Position_Parameters',
  full_name='sila2.de.cetoni.pumps.syringepumps.valvepositioncontroller.v1.Subscribe_Position_Parameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
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
  serialized_start=517,
  serialized_end=548,
)


_SUBSCRIBE_POSITION_RESPONSES = _descriptor.Descriptor(
  name='Subscribe_Position_Responses',
  full_name='sila2.de.cetoni.pumps.syringepumps.valvepositioncontroller.v1.Subscribe_Position_Responses',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Position', full_name='sila2.de.cetoni.pumps.syringepumps.valvepositioncontroller.v1.Subscribe_Position_Responses.Position', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=550,
  serialized_end=631,
)

_SWITCHTOPOSITION_PARAMETERS.fields_by_name['Position'].message_type = SiLAFramework__pb2._INTEGER
_SWITCHTOPOSITION_RESPONSES.fields_by_name['Success'].message_type = SiLAFramework__pb2._BOOLEAN
_TOGGLEPOSITION_RESPONSES.fields_by_name['Success'].message_type = SiLAFramework__pb2._BOOLEAN
_GET_NUMBEROFPOSITIONS_RESPONSES.fields_by_name['NumberOfPositions'].message_type = SiLAFramework__pb2._INTEGER
_SUBSCRIBE_POSITION_RESPONSES.fields_by_name['Position'].message_type = SiLAFramework__pb2._INTEGER
DESCRIPTOR.message_types_by_name['SwitchToPosition_Parameters'] = _SWITCHTOPOSITION_PARAMETERS
DESCRIPTOR.message_types_by_name['SwitchToPosition_Responses'] = _SWITCHTOPOSITION_RESPONSES
DESCRIPTOR.message_types_by_name['TogglePosition_Parameters'] = _TOGGLEPOSITION_PARAMETERS
DESCRIPTOR.message_types_by_name['TogglePosition_Responses'] = _TOGGLEPOSITION_RESPONSES
DESCRIPTOR.message_types_by_name['Get_NumberOfPositions_Parameters'] = _GET_NUMBEROFPOSITIONS_PARAMETERS
DESCRIPTOR.message_types_by_name['Get_NumberOfPositions_Responses'] = _GET_NUMBEROFPOSITIONS_RESPONSES
DESCRIPTOR.message_types_by_name['Subscribe_Position_Parameters'] = _SUBSCRIBE_POSITION_PARAMETERS
DESCRIPTOR.message_types_by_name['Subscribe_Position_Responses'] = _SUBSCRIBE_POSITION_RESPONSES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SwitchToPosition_Parameters = _reflection.GeneratedProtocolMessageType('SwitchToPosition_Parameters', (_message.Message,), {
  'DESCRIPTOR' : _SWITCHTOPOSITION_PARAMETERS,
  '__module__' : 'ValvePositionController_pb2'
  # @@protoc_insertion_point(class_scope:sila2.de.cetoni.pumps.syringepumps.valvepositioncontroller.v1.SwitchToPosition_Parameters)
  })
_sym_db.RegisterMessage(SwitchToPosition_Parameters)

SwitchToPosition_Responses = _reflection.GeneratedProtocolMessageType('SwitchToPosition_Responses', (_message.Message,), {
  'DESCRIPTOR' : _SWITCHTOPOSITION_RESPONSES,
  '__module__' : 'ValvePositionController_pb2'
  # @@protoc_insertion_point(class_scope:sila2.de.cetoni.pumps.syringepumps.valvepositioncontroller.v1.SwitchToPosition_Responses)
  })
_sym_db.RegisterMessage(SwitchToPosition_Responses)

TogglePosition_Parameters = _reflection.GeneratedProtocolMessageType('TogglePosition_Parameters', (_message.Message,), {
  'DESCRIPTOR' : _TOGGLEPOSITION_PARAMETERS,
  '__module__' : 'ValvePositionController_pb2'
  # @@protoc_insertion_point(class_scope:sila2.de.cetoni.pumps.syringepumps.valvepositioncontroller.v1.TogglePosition_Parameters)
  })
_sym_db.RegisterMessage(TogglePosition_Parameters)

TogglePosition_Responses = _reflection.GeneratedProtocolMessageType('TogglePosition_Responses', (_message.Message,), {
  'DESCRIPTOR' : _TOGGLEPOSITION_RESPONSES,
  '__module__' : 'ValvePositionController_pb2'
  # @@protoc_insertion_point(class_scope:sila2.de.cetoni.pumps.syringepumps.valvepositioncontroller.v1.TogglePosition_Responses)
  })
_sym_db.RegisterMessage(TogglePosition_Responses)

Get_NumberOfPositions_Parameters = _reflection.GeneratedProtocolMessageType('Get_NumberOfPositions_Parameters', (_message.Message,), {
  'DESCRIPTOR' : _GET_NUMBEROFPOSITIONS_PARAMETERS,
  '__module__' : 'ValvePositionController_pb2'
  # @@protoc_insertion_point(class_scope:sila2.de.cetoni.pumps.syringepumps.valvepositioncontroller.v1.Get_NumberOfPositions_Parameters)
  })
_sym_db.RegisterMessage(Get_NumberOfPositions_Parameters)

Get_NumberOfPositions_Responses = _reflection.GeneratedProtocolMessageType('Get_NumberOfPositions_Responses', (_message.Message,), {
  'DESCRIPTOR' : _GET_NUMBEROFPOSITIONS_RESPONSES,
  '__module__' : 'ValvePositionController_pb2'
  # @@protoc_insertion_point(class_scope:sila2.de.cetoni.pumps.syringepumps.valvepositioncontroller.v1.Get_NumberOfPositions_Responses)
  })
_sym_db.RegisterMessage(Get_NumberOfPositions_Responses)

Subscribe_Position_Parameters = _reflection.GeneratedProtocolMessageType('Subscribe_Position_Parameters', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBE_POSITION_PARAMETERS,
  '__module__' : 'ValvePositionController_pb2'
  # @@protoc_insertion_point(class_scope:sila2.de.cetoni.pumps.syringepumps.valvepositioncontroller.v1.Subscribe_Position_Parameters)
  })
_sym_db.RegisterMessage(Subscribe_Position_Parameters)

Subscribe_Position_Responses = _reflection.GeneratedProtocolMessageType('Subscribe_Position_Responses', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBE_POSITION_RESPONSES,
  '__module__' : 'ValvePositionController_pb2'
  # @@protoc_insertion_point(class_scope:sila2.de.cetoni.pumps.syringepumps.valvepositioncontroller.v1.Subscribe_Position_Responses)
  })
_sym_db.RegisterMessage(Subscribe_Position_Responses)



_VALVEPOSITIONCONTROLLER = _descriptor.ServiceDescriptor(
  name='ValvePositionController',
  full_name='sila2.de.cetoni.pumps.syringepumps.valvepositioncontroller.v1.ValvePositionController',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=634,
  serialized_end=1492,
  methods=[
  _descriptor.MethodDescriptor(
    name='SwitchToPosition',
    full_name='sila2.de.cetoni.pumps.syringepumps.valvepositioncontroller.v1.ValvePositionController.SwitchToPosition',
    index=0,
    containing_service=None,
    input_type=_SWITCHTOPOSITION_PARAMETERS,
    output_type=_SWITCHTOPOSITION_RESPONSES,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='TogglePosition',
    full_name='sila2.de.cetoni.pumps.syringepumps.valvepositioncontroller.v1.ValvePositionController.TogglePosition',
    index=1,
    containing_service=None,
    input_type=_TOGGLEPOSITION_PARAMETERS,
    output_type=_TOGGLEPOSITION_RESPONSES,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Get_NumberOfPositions',
    full_name='sila2.de.cetoni.pumps.syringepumps.valvepositioncontroller.v1.ValvePositionController.Get_NumberOfPositions',
    index=2,
    containing_service=None,
    input_type=_GET_NUMBEROFPOSITIONS_PARAMETERS,
    output_type=_GET_NUMBEROFPOSITIONS_RESPONSES,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Subscribe_Position',
    full_name='sila2.de.cetoni.pumps.syringepumps.valvepositioncontroller.v1.ValvePositionController.Subscribe_Position',
    index=3,
    containing_service=None,
    input_type=_SUBSCRIBE_POSITION_PARAMETERS,
    output_type=_SUBSCRIBE_POSITION_RESPONSES,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_VALVEPOSITIONCONTROLLER)

DESCRIPTOR.services_by_name['ValvePositionController'] = _VALVEPOSITIONCONTROLLER

# @@protoc_insertion_point(module_scope)
