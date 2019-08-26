# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: PumpDriveControlService.proto

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
  name='PumpDriveControlService.proto',
  package='sila2.de.cetoni.pumps.syringepumps.pumpdrivecontrolservice.v1',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1dPumpDriveControlService.proto\x12=sila2.de.cetoni.pumps.syringepumps.pumpdrivecontrolservice.v1\x1a\x13SiLAFramework.proto\" \n\x1eInitializePumpDrive_Parameters\"\x1f\n\x1dInitializePumpDrive_Responses\"\x1c\n\x1a\x45nablePumpDrive_Parameters\"\x1b\n\x19\x45nablePumpDrive_Responses\"\x1d\n\x1b\x44isablePumpDrive_Parameters\"\x1c\n\x1a\x44isablePumpDrive_Responses\"%\n#Subscribe_PumpDriveState_Parameters\"]\n\"Subscribe_PumpDriveState_Responses\x12\x37\n\x0ePumpDriveState\x18\x01 \x01(\x0b\x32\x1f.sila2.org.silastandard.Boolean\"!\n\x1fSubscribe_FaultState_Parameters\"U\n\x1eSubscribe_FaultState_Responses\x12\x33\n\nFaultState\x18\x01 \x01(\x0b\x32\x1f.sila2.org.silastandard.Boolean2\xc3\x08\n\x17PumpDriveControlService\x12\xd2\x01\n\x13InitializePumpDrive\x12].sila2.de.cetoni.pumps.syringepumps.pumpdrivecontrolservice.v1.InitializePumpDrive_Parameters\x1a\\.sila2.de.cetoni.pumps.syringepumps.pumpdrivecontrolservice.v1.InitializePumpDrive_Responses\x12\xc6\x01\n\x0f\x45nablePumpDrive\x12Y.sila2.de.cetoni.pumps.syringepumps.pumpdrivecontrolservice.v1.EnablePumpDrive_Parameters\x1aX.sila2.de.cetoni.pumps.syringepumps.pumpdrivecontrolservice.v1.EnablePumpDrive_Responses\x12\xc9\x01\n\x10\x44isablePumpDrive\x12Z.sila2.de.cetoni.pumps.syringepumps.pumpdrivecontrolservice.v1.DisablePumpDrive_Parameters\x1aY.sila2.de.cetoni.pumps.syringepumps.pumpdrivecontrolservice.v1.DisablePumpDrive_Responses\x12\xe3\x01\n\x18Subscribe_PumpDriveState\x12\x62.sila2.de.cetoni.pumps.syringepumps.pumpdrivecontrolservice.v1.Subscribe_PumpDriveState_Parameters\x1a\x61.sila2.de.cetoni.pumps.syringepumps.pumpdrivecontrolservice.v1.Subscribe_PumpDriveState_Responses0\x01\x12\xd7\x01\n\x14Subscribe_FaultState\x12^.sila2.de.cetoni.pumps.syringepumps.pumpdrivecontrolservice.v1.Subscribe_FaultState_Parameters\x1a].sila2.de.cetoni.pumps.syringepumps.pumpdrivecontrolservice.v1.Subscribe_FaultState_Responses0\x01\x62\x06proto3')
  ,
  dependencies=[SiLAFramework__pb2.DESCRIPTOR,])




_INITIALIZEPUMPDRIVE_PARAMETERS = _descriptor.Descriptor(
  name='InitializePumpDrive_Parameters',
  full_name='sila2.de.cetoni.pumps.syringepumps.pumpdrivecontrolservice.v1.InitializePumpDrive_Parameters',
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
  serialized_start=117,
  serialized_end=149,
)


_INITIALIZEPUMPDRIVE_RESPONSES = _descriptor.Descriptor(
  name='InitializePumpDrive_Responses',
  full_name='sila2.de.cetoni.pumps.syringepumps.pumpdrivecontrolservice.v1.InitializePumpDrive_Responses',
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
  serialized_start=151,
  serialized_end=182,
)


_ENABLEPUMPDRIVE_PARAMETERS = _descriptor.Descriptor(
  name='EnablePumpDrive_Parameters',
  full_name='sila2.de.cetoni.pumps.syringepumps.pumpdrivecontrolservice.v1.EnablePumpDrive_Parameters',
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
  serialized_start=184,
  serialized_end=212,
)


_ENABLEPUMPDRIVE_RESPONSES = _descriptor.Descriptor(
  name='EnablePumpDrive_Responses',
  full_name='sila2.de.cetoni.pumps.syringepumps.pumpdrivecontrolservice.v1.EnablePumpDrive_Responses',
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
  serialized_start=214,
  serialized_end=241,
)


_DISABLEPUMPDRIVE_PARAMETERS = _descriptor.Descriptor(
  name='DisablePumpDrive_Parameters',
  full_name='sila2.de.cetoni.pumps.syringepumps.pumpdrivecontrolservice.v1.DisablePumpDrive_Parameters',
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
  serialized_start=243,
  serialized_end=272,
)


_DISABLEPUMPDRIVE_RESPONSES = _descriptor.Descriptor(
  name='DisablePumpDrive_Responses',
  full_name='sila2.de.cetoni.pumps.syringepumps.pumpdrivecontrolservice.v1.DisablePumpDrive_Responses',
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
  serialized_start=274,
  serialized_end=302,
)


_SUBSCRIBE_PUMPDRIVESTATE_PARAMETERS = _descriptor.Descriptor(
  name='Subscribe_PumpDriveState_Parameters',
  full_name='sila2.de.cetoni.pumps.syringepumps.pumpdrivecontrolservice.v1.Subscribe_PumpDriveState_Parameters',
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
  serialized_start=304,
  serialized_end=341,
)


_SUBSCRIBE_PUMPDRIVESTATE_RESPONSES = _descriptor.Descriptor(
  name='Subscribe_PumpDriveState_Responses',
  full_name='sila2.de.cetoni.pumps.syringepumps.pumpdrivecontrolservice.v1.Subscribe_PumpDriveState_Responses',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='PumpDriveState', full_name='sila2.de.cetoni.pumps.syringepumps.pumpdrivecontrolservice.v1.Subscribe_PumpDriveState_Responses.PumpDriveState', index=0,
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
  serialized_start=343,
  serialized_end=436,
)


_SUBSCRIBE_FAULTSTATE_PARAMETERS = _descriptor.Descriptor(
  name='Subscribe_FaultState_Parameters',
  full_name='sila2.de.cetoni.pumps.syringepumps.pumpdrivecontrolservice.v1.Subscribe_FaultState_Parameters',
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
  serialized_start=438,
  serialized_end=471,
)


_SUBSCRIBE_FAULTSTATE_RESPONSES = _descriptor.Descriptor(
  name='Subscribe_FaultState_Responses',
  full_name='sila2.de.cetoni.pumps.syringepumps.pumpdrivecontrolservice.v1.Subscribe_FaultState_Responses',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='FaultState', full_name='sila2.de.cetoni.pumps.syringepumps.pumpdrivecontrolservice.v1.Subscribe_FaultState_Responses.FaultState', index=0,
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
  serialized_start=473,
  serialized_end=558,
)

_SUBSCRIBE_PUMPDRIVESTATE_RESPONSES.fields_by_name['PumpDriveState'].message_type = SiLAFramework__pb2._BOOLEAN
_SUBSCRIBE_FAULTSTATE_RESPONSES.fields_by_name['FaultState'].message_type = SiLAFramework__pb2._BOOLEAN
DESCRIPTOR.message_types_by_name['InitializePumpDrive_Parameters'] = _INITIALIZEPUMPDRIVE_PARAMETERS
DESCRIPTOR.message_types_by_name['InitializePumpDrive_Responses'] = _INITIALIZEPUMPDRIVE_RESPONSES
DESCRIPTOR.message_types_by_name['EnablePumpDrive_Parameters'] = _ENABLEPUMPDRIVE_PARAMETERS
DESCRIPTOR.message_types_by_name['EnablePumpDrive_Responses'] = _ENABLEPUMPDRIVE_RESPONSES
DESCRIPTOR.message_types_by_name['DisablePumpDrive_Parameters'] = _DISABLEPUMPDRIVE_PARAMETERS
DESCRIPTOR.message_types_by_name['DisablePumpDrive_Responses'] = _DISABLEPUMPDRIVE_RESPONSES
DESCRIPTOR.message_types_by_name['Subscribe_PumpDriveState_Parameters'] = _SUBSCRIBE_PUMPDRIVESTATE_PARAMETERS
DESCRIPTOR.message_types_by_name['Subscribe_PumpDriveState_Responses'] = _SUBSCRIBE_PUMPDRIVESTATE_RESPONSES
DESCRIPTOR.message_types_by_name['Subscribe_FaultState_Parameters'] = _SUBSCRIBE_FAULTSTATE_PARAMETERS
DESCRIPTOR.message_types_by_name['Subscribe_FaultState_Responses'] = _SUBSCRIBE_FAULTSTATE_RESPONSES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InitializePumpDrive_Parameters = _reflection.GeneratedProtocolMessageType('InitializePumpDrive_Parameters', (_message.Message,), {
  'DESCRIPTOR' : _INITIALIZEPUMPDRIVE_PARAMETERS,
  '__module__' : 'PumpDriveControlService_pb2'
  # @@protoc_insertion_point(class_scope:sila2.de.cetoni.pumps.syringepumps.pumpdrivecontrolservice.v1.InitializePumpDrive_Parameters)
  })
_sym_db.RegisterMessage(InitializePumpDrive_Parameters)

InitializePumpDrive_Responses = _reflection.GeneratedProtocolMessageType('InitializePumpDrive_Responses', (_message.Message,), {
  'DESCRIPTOR' : _INITIALIZEPUMPDRIVE_RESPONSES,
  '__module__' : 'PumpDriveControlService_pb2'
  # @@protoc_insertion_point(class_scope:sila2.de.cetoni.pumps.syringepumps.pumpdrivecontrolservice.v1.InitializePumpDrive_Responses)
  })
_sym_db.RegisterMessage(InitializePumpDrive_Responses)

EnablePumpDrive_Parameters = _reflection.GeneratedProtocolMessageType('EnablePumpDrive_Parameters', (_message.Message,), {
  'DESCRIPTOR' : _ENABLEPUMPDRIVE_PARAMETERS,
  '__module__' : 'PumpDriveControlService_pb2'
  # @@protoc_insertion_point(class_scope:sila2.de.cetoni.pumps.syringepumps.pumpdrivecontrolservice.v1.EnablePumpDrive_Parameters)
  })
_sym_db.RegisterMessage(EnablePumpDrive_Parameters)

EnablePumpDrive_Responses = _reflection.GeneratedProtocolMessageType('EnablePumpDrive_Responses', (_message.Message,), {
  'DESCRIPTOR' : _ENABLEPUMPDRIVE_RESPONSES,
  '__module__' : 'PumpDriveControlService_pb2'
  # @@protoc_insertion_point(class_scope:sila2.de.cetoni.pumps.syringepumps.pumpdrivecontrolservice.v1.EnablePumpDrive_Responses)
  })
_sym_db.RegisterMessage(EnablePumpDrive_Responses)

DisablePumpDrive_Parameters = _reflection.GeneratedProtocolMessageType('DisablePumpDrive_Parameters', (_message.Message,), {
  'DESCRIPTOR' : _DISABLEPUMPDRIVE_PARAMETERS,
  '__module__' : 'PumpDriveControlService_pb2'
  # @@protoc_insertion_point(class_scope:sila2.de.cetoni.pumps.syringepumps.pumpdrivecontrolservice.v1.DisablePumpDrive_Parameters)
  })
_sym_db.RegisterMessage(DisablePumpDrive_Parameters)

DisablePumpDrive_Responses = _reflection.GeneratedProtocolMessageType('DisablePumpDrive_Responses', (_message.Message,), {
  'DESCRIPTOR' : _DISABLEPUMPDRIVE_RESPONSES,
  '__module__' : 'PumpDriveControlService_pb2'
  # @@protoc_insertion_point(class_scope:sila2.de.cetoni.pumps.syringepumps.pumpdrivecontrolservice.v1.DisablePumpDrive_Responses)
  })
_sym_db.RegisterMessage(DisablePumpDrive_Responses)

Subscribe_PumpDriveState_Parameters = _reflection.GeneratedProtocolMessageType('Subscribe_PumpDriveState_Parameters', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBE_PUMPDRIVESTATE_PARAMETERS,
  '__module__' : 'PumpDriveControlService_pb2'
  # @@protoc_insertion_point(class_scope:sila2.de.cetoni.pumps.syringepumps.pumpdrivecontrolservice.v1.Subscribe_PumpDriveState_Parameters)
  })
_sym_db.RegisterMessage(Subscribe_PumpDriveState_Parameters)

Subscribe_PumpDriveState_Responses = _reflection.GeneratedProtocolMessageType('Subscribe_PumpDriveState_Responses', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBE_PUMPDRIVESTATE_RESPONSES,
  '__module__' : 'PumpDriveControlService_pb2'
  # @@protoc_insertion_point(class_scope:sila2.de.cetoni.pumps.syringepumps.pumpdrivecontrolservice.v1.Subscribe_PumpDriveState_Responses)
  })
_sym_db.RegisterMessage(Subscribe_PumpDriveState_Responses)

Subscribe_FaultState_Parameters = _reflection.GeneratedProtocolMessageType('Subscribe_FaultState_Parameters', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBE_FAULTSTATE_PARAMETERS,
  '__module__' : 'PumpDriveControlService_pb2'
  # @@protoc_insertion_point(class_scope:sila2.de.cetoni.pumps.syringepumps.pumpdrivecontrolservice.v1.Subscribe_FaultState_Parameters)
  })
_sym_db.RegisterMessage(Subscribe_FaultState_Parameters)

Subscribe_FaultState_Responses = _reflection.GeneratedProtocolMessageType('Subscribe_FaultState_Responses', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBE_FAULTSTATE_RESPONSES,
  '__module__' : 'PumpDriveControlService_pb2'
  # @@protoc_insertion_point(class_scope:sila2.de.cetoni.pumps.syringepumps.pumpdrivecontrolservice.v1.Subscribe_FaultState_Responses)
  })
_sym_db.RegisterMessage(Subscribe_FaultState_Responses)



_PUMPDRIVECONTROLSERVICE = _descriptor.ServiceDescriptor(
  name='PumpDriveControlService',
  full_name='sila2.de.cetoni.pumps.syringepumps.pumpdrivecontrolservice.v1.PumpDriveControlService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=561,
  serialized_end=1652,
  methods=[
  _descriptor.MethodDescriptor(
    name='InitializePumpDrive',
    full_name='sila2.de.cetoni.pumps.syringepumps.pumpdrivecontrolservice.v1.PumpDriveControlService.InitializePumpDrive',
    index=0,
    containing_service=None,
    input_type=_INITIALIZEPUMPDRIVE_PARAMETERS,
    output_type=_INITIALIZEPUMPDRIVE_RESPONSES,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='EnablePumpDrive',
    full_name='sila2.de.cetoni.pumps.syringepumps.pumpdrivecontrolservice.v1.PumpDriveControlService.EnablePumpDrive',
    index=1,
    containing_service=None,
    input_type=_ENABLEPUMPDRIVE_PARAMETERS,
    output_type=_ENABLEPUMPDRIVE_RESPONSES,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DisablePumpDrive',
    full_name='sila2.de.cetoni.pumps.syringepumps.pumpdrivecontrolservice.v1.PumpDriveControlService.DisablePumpDrive',
    index=2,
    containing_service=None,
    input_type=_DISABLEPUMPDRIVE_PARAMETERS,
    output_type=_DISABLEPUMPDRIVE_RESPONSES,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Subscribe_PumpDriveState',
    full_name='sila2.de.cetoni.pumps.syringepumps.pumpdrivecontrolservice.v1.PumpDriveControlService.Subscribe_PumpDriveState',
    index=3,
    containing_service=None,
    input_type=_SUBSCRIBE_PUMPDRIVESTATE_PARAMETERS,
    output_type=_SUBSCRIBE_PUMPDRIVESTATE_RESPONSES,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Subscribe_FaultState',
    full_name='sila2.de.cetoni.pumps.syringepumps.pumpdrivecontrolservice.v1.PumpDriveControlService.Subscribe_FaultState',
    index=4,
    containing_service=None,
    input_type=_SUBSCRIBE_FAULTSTATE_PARAMETERS,
    output_type=_SUBSCRIBE_FAULTSTATE_RESPONSES,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_PUMPDRIVECONTROLSERVICE)

DESCRIPTOR.services_by_name['PumpDriveControlService'] = _PUMPDRIVECONTROLSERVICE

# @@protoc_insertion_point(module_scope)
