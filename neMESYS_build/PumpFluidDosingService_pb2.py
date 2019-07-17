# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: PumpFluidDosingService.proto

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
  name='PumpFluidDosingService.proto',
  package='sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1cPumpFluidDosingService.proto\x12<sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1\x1a\x13SiLAFramework.proto\"M\n\x16\x44\x61taType_ValueWithUnit\x12\x33\n\rValueWithUnit\x18\x01 \x01(\x0b\x32\x1c.sila2.org.silastandard.Real\"\x82\x01\n\x17SetFillLevel_Parameters\x12g\n\tFillLevel\x18\x01 \x01(\x0b\x32T.sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.DataType_ValueWithUnit\"J\n\x16SetFillLevel_Responses\x12\x30\n\x07Success\x18\x01 \x01(\x0b\x32\x1f.sila2.org.silastandard.Boolean\"}\n\x15\x44oseVolume_Parameters\x12\x64\n\x06Volume\x18\x01 \x01(\x0b\x32T.sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.DataType_ValueWithUnit\"H\n\x14\x44oseVolume_Responses\x12\x30\n\x07Success\x18\x01 \x01(\x0b\x32\x1f.sila2.org.silastandard.Boolean\"\x81\x01\n\x17GenerateFlow_Parameters\x12\x66\n\x08\x46lowRate\x18\x01 \x01(\x0b\x32T.sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.DataType_ValueWithUnit\"R\n\"GenerateFlow_IntermediateResponses\x12,\n\x04Test\x18\x01 \x01(\x0b\x32\x1e.sila2.org.silastandard.String\"J\n\x16GenerateFlow_Responses\x12\x30\n\x07Success\x18\x01 \x01(\x0b\x32\x1f.sila2.org.silastandard.Boolean\"\x17\n\x15StopDosage_Parameters\"H\n\x14StopDosage_Responses\x12\x30\n\x07Success\x18\x01 \x01(\x0b\x32\x1f.sila2.org.silastandard.Boolean\"$\n\"Get_MaxSyringeFillLevel_Parameters\"\x96\x01\n!Get_MaxSyringeFillLevel_Responses\x12q\n\x13MaxSyringeFillLevel\x18\x01 \x01(\x0b\x32T.sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.DataType_ValueWithUnit\"\'\n%Subscribe_SyringeFillLevel_Parameters\"\x96\x01\n$Subscribe_SyringeFillLevel_Responses\x12n\n\x10SyringeFillLevel\x18\x01 \x01(\x0b\x32T.sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.DataType_ValueWithUnit\"\x1c\n\x1aGet_MaxFlowRate_Parameters\"\x86\x01\n\x19Get_MaxFlowRate_Responses\x12i\n\x0bMaxFlowRate\x18\x01 \x01(\x0b\x32T.sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.DataType_ValueWithUnit\"\x1c\n\x1aGet_MinFlowRate_Parameters\"\x86\x01\n\x19Get_MinFlowRate_Responses\x12i\n\x0bMinFlowRate\x18\x01 \x01(\x0b\x32T.sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.DataType_ValueWithUnit\"\x1f\n\x1dSubscribe_FlowRate_Parameters\"\x86\x01\n\x1cSubscribe_FlowRate_Responses\x12\x66\n\x08\x46lowRate\x18\x01 \x01(\x0b\x32T.sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.DataType_ValueWithUnit2\xf6\x14\n\x16PumpFluidDosingService\x12\x92\x01\n\x0cSetFillLevel\x12U.sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.SetFillLevel_Parameters\x1a+.sila2.org.silastandard.CommandConfirmation\x12j\n\x11SetFillLevel_Info\x12,.sila2.org.silastandard.CommandExecutionUUID\x1a%.sila2.org.silastandard.ExecutionInfo0\x01\x12\x99\x01\n\x13SetFillLevel_Result\x12,.sila2.org.silastandard.CommandExecutionUUID\x1aT.sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.SetFillLevel_Responses\x12\x8e\x01\n\nDoseVolume\x12S.sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.DoseVolume_Parameters\x1a+.sila2.org.silastandard.CommandConfirmation\x12h\n\x0f\x44oseVolume_Info\x12,.sila2.org.silastandard.CommandExecutionUUID\x1a%.sila2.org.silastandard.ExecutionInfo0\x01\x12\x95\x01\n\x11\x44oseVolume_Result\x12,.sila2.org.silastandard.CommandExecutionUUID\x1aR.sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.DoseVolume_Responses\x12\x92\x01\n\x0cGenerateFlow\x12U.sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.GenerateFlow_Parameters\x1a+.sila2.org.silastandard.CommandConfirmation\x12\xad\x01\n\x19GenerateFlow_Intermediate\x12,.sila2.org.silastandard.CommandExecutionUUID\x1a`.sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.GenerateFlow_IntermediateResponses0\x01\x12j\n\x11GenerateFlow_Info\x12,.sila2.org.silastandard.CommandExecutionUUID\x1a%.sila2.org.silastandard.ExecutionInfo0\x01\x12\x99\x01\n\x13GenerateFlow_Result\x12,.sila2.org.silastandard.CommandExecutionUUID\x1aT.sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.GenerateFlow_Responses\x12\xb5\x01\n\nStopDosage\x12S.sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.StopDosage_Parameters\x1aR.sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.StopDosage_Responses\x12\xdc\x01\n\x17Get_MaxSyringeFillLevel\x12`.sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.Get_MaxSyringeFillLevel_Parameters\x1a_.sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.Get_MaxSyringeFillLevel_Responses\x12\xe7\x01\n\x1aSubscribe_SyringeFillLevel\x12\x63.sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.Subscribe_SyringeFillLevel_Parameters\x1a\x62.sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.Subscribe_SyringeFillLevel_Responses0\x01\x12\xc4\x01\n\x0fGet_MaxFlowRate\x12X.sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.Get_MaxFlowRate_Parameters\x1aW.sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.Get_MaxFlowRate_Responses\x12\xc4\x01\n\x0fGet_MinFlowRate\x12X.sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.Get_MinFlowRate_Parameters\x1aW.sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.Get_MinFlowRate_Responses\x12\xcf\x01\n\x12Subscribe_FlowRate\x12[.sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.Subscribe_FlowRate_Parameters\x1aZ.sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.Subscribe_FlowRate_Responses0\x01\x62\x06proto3')
  ,
  dependencies=[SiLAFramework__pb2.DESCRIPTOR,])




_DATATYPE_VALUEWITHUNIT = _descriptor.Descriptor(
  name='DataType_ValueWithUnit',
  full_name='sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.DataType_ValueWithUnit',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ValueWithUnit', full_name='sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.DataType_ValueWithUnit.ValueWithUnit', index=0,
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
  serialized_start=115,
  serialized_end=192,
)


_SETFILLLEVEL_PARAMETERS = _descriptor.Descriptor(
  name='SetFillLevel_Parameters',
  full_name='sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.SetFillLevel_Parameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='FillLevel', full_name='sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.SetFillLevel_Parameters.FillLevel', index=0,
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
  serialized_start=195,
  serialized_end=325,
)


_SETFILLLEVEL_RESPONSES = _descriptor.Descriptor(
  name='SetFillLevel_Responses',
  full_name='sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.SetFillLevel_Responses',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Success', full_name='sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.SetFillLevel_Responses.Success', index=0,
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
  serialized_start=327,
  serialized_end=401,
)


_DOSEVOLUME_PARAMETERS = _descriptor.Descriptor(
  name='DoseVolume_Parameters',
  full_name='sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.DoseVolume_Parameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Volume', full_name='sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.DoseVolume_Parameters.Volume', index=0,
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
  serialized_start=403,
  serialized_end=528,
)


_DOSEVOLUME_RESPONSES = _descriptor.Descriptor(
  name='DoseVolume_Responses',
  full_name='sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.DoseVolume_Responses',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Success', full_name='sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.DoseVolume_Responses.Success', index=0,
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
  serialized_start=530,
  serialized_end=602,
)


_GENERATEFLOW_PARAMETERS = _descriptor.Descriptor(
  name='GenerateFlow_Parameters',
  full_name='sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.GenerateFlow_Parameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='FlowRate', full_name='sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.GenerateFlow_Parameters.FlowRate', index=0,
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
  serialized_start=605,
  serialized_end=734,
)


_GENERATEFLOW_INTERMEDIATERESPONSES = _descriptor.Descriptor(
  name='GenerateFlow_IntermediateResponses',
  full_name='sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.GenerateFlow_IntermediateResponses',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Test', full_name='sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.GenerateFlow_IntermediateResponses.Test', index=0,
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
  serialized_start=736,
  serialized_end=818,
)


_GENERATEFLOW_RESPONSES = _descriptor.Descriptor(
  name='GenerateFlow_Responses',
  full_name='sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.GenerateFlow_Responses',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Success', full_name='sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.GenerateFlow_Responses.Success', index=0,
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
  serialized_start=820,
  serialized_end=894,
)


_STOPDOSAGE_PARAMETERS = _descriptor.Descriptor(
  name='StopDosage_Parameters',
  full_name='sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.StopDosage_Parameters',
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
  serialized_start=896,
  serialized_end=919,
)


_STOPDOSAGE_RESPONSES = _descriptor.Descriptor(
  name='StopDosage_Responses',
  full_name='sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.StopDosage_Responses',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Success', full_name='sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.StopDosage_Responses.Success', index=0,
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
  serialized_start=921,
  serialized_end=993,
)


_GET_MAXSYRINGEFILLLEVEL_PARAMETERS = _descriptor.Descriptor(
  name='Get_MaxSyringeFillLevel_Parameters',
  full_name='sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.Get_MaxSyringeFillLevel_Parameters',
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
  serialized_start=995,
  serialized_end=1031,
)


_GET_MAXSYRINGEFILLLEVEL_RESPONSES = _descriptor.Descriptor(
  name='Get_MaxSyringeFillLevel_Responses',
  full_name='sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.Get_MaxSyringeFillLevel_Responses',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='MaxSyringeFillLevel', full_name='sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.Get_MaxSyringeFillLevel_Responses.MaxSyringeFillLevel', index=0,
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
  serialized_start=1034,
  serialized_end=1184,
)


_SUBSCRIBE_SYRINGEFILLLEVEL_PARAMETERS = _descriptor.Descriptor(
  name='Subscribe_SyringeFillLevel_Parameters',
  full_name='sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.Subscribe_SyringeFillLevel_Parameters',
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
  serialized_start=1186,
  serialized_end=1225,
)


_SUBSCRIBE_SYRINGEFILLLEVEL_RESPONSES = _descriptor.Descriptor(
  name='Subscribe_SyringeFillLevel_Responses',
  full_name='sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.Subscribe_SyringeFillLevel_Responses',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='SyringeFillLevel', full_name='sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.Subscribe_SyringeFillLevel_Responses.SyringeFillLevel', index=0,
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
  serialized_start=1228,
  serialized_end=1378,
)


_GET_MAXFLOWRATE_PARAMETERS = _descriptor.Descriptor(
  name='Get_MaxFlowRate_Parameters',
  full_name='sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.Get_MaxFlowRate_Parameters',
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
  serialized_start=1380,
  serialized_end=1408,
)


_GET_MAXFLOWRATE_RESPONSES = _descriptor.Descriptor(
  name='Get_MaxFlowRate_Responses',
  full_name='sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.Get_MaxFlowRate_Responses',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='MaxFlowRate', full_name='sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.Get_MaxFlowRate_Responses.MaxFlowRate', index=0,
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
  serialized_start=1411,
  serialized_end=1545,
)


_GET_MINFLOWRATE_PARAMETERS = _descriptor.Descriptor(
  name='Get_MinFlowRate_Parameters',
  full_name='sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.Get_MinFlowRate_Parameters',
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
  serialized_start=1547,
  serialized_end=1575,
)


_GET_MINFLOWRATE_RESPONSES = _descriptor.Descriptor(
  name='Get_MinFlowRate_Responses',
  full_name='sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.Get_MinFlowRate_Responses',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='MinFlowRate', full_name='sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.Get_MinFlowRate_Responses.MinFlowRate', index=0,
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
  serialized_start=1578,
  serialized_end=1712,
)


_SUBSCRIBE_FLOWRATE_PARAMETERS = _descriptor.Descriptor(
  name='Subscribe_FlowRate_Parameters',
  full_name='sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.Subscribe_FlowRate_Parameters',
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
  serialized_start=1714,
  serialized_end=1745,
)


_SUBSCRIBE_FLOWRATE_RESPONSES = _descriptor.Descriptor(
  name='Subscribe_FlowRate_Responses',
  full_name='sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.Subscribe_FlowRate_Responses',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='FlowRate', full_name='sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.Subscribe_FlowRate_Responses.FlowRate', index=0,
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
  serialized_start=1748,
  serialized_end=1882,
)

_DATATYPE_VALUEWITHUNIT.fields_by_name['ValueWithUnit'].message_type = SiLAFramework__pb2._REAL
_SETFILLLEVEL_PARAMETERS.fields_by_name['FillLevel'].message_type = _DATATYPE_VALUEWITHUNIT
_SETFILLLEVEL_RESPONSES.fields_by_name['Success'].message_type = SiLAFramework__pb2._BOOLEAN
_DOSEVOLUME_PARAMETERS.fields_by_name['Volume'].message_type = _DATATYPE_VALUEWITHUNIT
_DOSEVOLUME_RESPONSES.fields_by_name['Success'].message_type = SiLAFramework__pb2._BOOLEAN
_GENERATEFLOW_PARAMETERS.fields_by_name['FlowRate'].message_type = _DATATYPE_VALUEWITHUNIT
_GENERATEFLOW_INTERMEDIATERESPONSES.fields_by_name['Test'].message_type = SiLAFramework__pb2._STRING
_GENERATEFLOW_RESPONSES.fields_by_name['Success'].message_type = SiLAFramework__pb2._BOOLEAN
_STOPDOSAGE_RESPONSES.fields_by_name['Success'].message_type = SiLAFramework__pb2._BOOLEAN
_GET_MAXSYRINGEFILLLEVEL_RESPONSES.fields_by_name['MaxSyringeFillLevel'].message_type = _DATATYPE_VALUEWITHUNIT
_SUBSCRIBE_SYRINGEFILLLEVEL_RESPONSES.fields_by_name['SyringeFillLevel'].message_type = _DATATYPE_VALUEWITHUNIT
_GET_MAXFLOWRATE_RESPONSES.fields_by_name['MaxFlowRate'].message_type = _DATATYPE_VALUEWITHUNIT
_GET_MINFLOWRATE_RESPONSES.fields_by_name['MinFlowRate'].message_type = _DATATYPE_VALUEWITHUNIT
_SUBSCRIBE_FLOWRATE_RESPONSES.fields_by_name['FlowRate'].message_type = _DATATYPE_VALUEWITHUNIT
DESCRIPTOR.message_types_by_name['DataType_ValueWithUnit'] = _DATATYPE_VALUEWITHUNIT
DESCRIPTOR.message_types_by_name['SetFillLevel_Parameters'] = _SETFILLLEVEL_PARAMETERS
DESCRIPTOR.message_types_by_name['SetFillLevel_Responses'] = _SETFILLLEVEL_RESPONSES
DESCRIPTOR.message_types_by_name['DoseVolume_Parameters'] = _DOSEVOLUME_PARAMETERS
DESCRIPTOR.message_types_by_name['DoseVolume_Responses'] = _DOSEVOLUME_RESPONSES
DESCRIPTOR.message_types_by_name['GenerateFlow_Parameters'] = _GENERATEFLOW_PARAMETERS
DESCRIPTOR.message_types_by_name['GenerateFlow_IntermediateResponses'] = _GENERATEFLOW_INTERMEDIATERESPONSES
DESCRIPTOR.message_types_by_name['GenerateFlow_Responses'] = _GENERATEFLOW_RESPONSES
DESCRIPTOR.message_types_by_name['StopDosage_Parameters'] = _STOPDOSAGE_PARAMETERS
DESCRIPTOR.message_types_by_name['StopDosage_Responses'] = _STOPDOSAGE_RESPONSES
DESCRIPTOR.message_types_by_name['Get_MaxSyringeFillLevel_Parameters'] = _GET_MAXSYRINGEFILLLEVEL_PARAMETERS
DESCRIPTOR.message_types_by_name['Get_MaxSyringeFillLevel_Responses'] = _GET_MAXSYRINGEFILLLEVEL_RESPONSES
DESCRIPTOR.message_types_by_name['Subscribe_SyringeFillLevel_Parameters'] = _SUBSCRIBE_SYRINGEFILLLEVEL_PARAMETERS
DESCRIPTOR.message_types_by_name['Subscribe_SyringeFillLevel_Responses'] = _SUBSCRIBE_SYRINGEFILLLEVEL_RESPONSES
DESCRIPTOR.message_types_by_name['Get_MaxFlowRate_Parameters'] = _GET_MAXFLOWRATE_PARAMETERS
DESCRIPTOR.message_types_by_name['Get_MaxFlowRate_Responses'] = _GET_MAXFLOWRATE_RESPONSES
DESCRIPTOR.message_types_by_name['Get_MinFlowRate_Parameters'] = _GET_MINFLOWRATE_PARAMETERS
DESCRIPTOR.message_types_by_name['Get_MinFlowRate_Responses'] = _GET_MINFLOWRATE_RESPONSES
DESCRIPTOR.message_types_by_name['Subscribe_FlowRate_Parameters'] = _SUBSCRIBE_FLOWRATE_PARAMETERS
DESCRIPTOR.message_types_by_name['Subscribe_FlowRate_Responses'] = _SUBSCRIBE_FLOWRATE_RESPONSES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DataType_ValueWithUnit = _reflection.GeneratedProtocolMessageType('DataType_ValueWithUnit', (_message.Message,), {
  'DESCRIPTOR' : _DATATYPE_VALUEWITHUNIT,
  '__module__' : 'PumpFluidDosingService_pb2'
  # @@protoc_insertion_point(class_scope:sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.DataType_ValueWithUnit)
  })
_sym_db.RegisterMessage(DataType_ValueWithUnit)

SetFillLevel_Parameters = _reflection.GeneratedProtocolMessageType('SetFillLevel_Parameters', (_message.Message,), {
  'DESCRIPTOR' : _SETFILLLEVEL_PARAMETERS,
  '__module__' : 'PumpFluidDosingService_pb2'
  # @@protoc_insertion_point(class_scope:sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.SetFillLevel_Parameters)
  })
_sym_db.RegisterMessage(SetFillLevel_Parameters)

SetFillLevel_Responses = _reflection.GeneratedProtocolMessageType('SetFillLevel_Responses', (_message.Message,), {
  'DESCRIPTOR' : _SETFILLLEVEL_RESPONSES,
  '__module__' : 'PumpFluidDosingService_pb2'
  # @@protoc_insertion_point(class_scope:sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.SetFillLevel_Responses)
  })
_sym_db.RegisterMessage(SetFillLevel_Responses)

DoseVolume_Parameters = _reflection.GeneratedProtocolMessageType('DoseVolume_Parameters', (_message.Message,), {
  'DESCRIPTOR' : _DOSEVOLUME_PARAMETERS,
  '__module__' : 'PumpFluidDosingService_pb2'
  # @@protoc_insertion_point(class_scope:sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.DoseVolume_Parameters)
  })
_sym_db.RegisterMessage(DoseVolume_Parameters)

DoseVolume_Responses = _reflection.GeneratedProtocolMessageType('DoseVolume_Responses', (_message.Message,), {
  'DESCRIPTOR' : _DOSEVOLUME_RESPONSES,
  '__module__' : 'PumpFluidDosingService_pb2'
  # @@protoc_insertion_point(class_scope:sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.DoseVolume_Responses)
  })
_sym_db.RegisterMessage(DoseVolume_Responses)

GenerateFlow_Parameters = _reflection.GeneratedProtocolMessageType('GenerateFlow_Parameters', (_message.Message,), {
  'DESCRIPTOR' : _GENERATEFLOW_PARAMETERS,
  '__module__' : 'PumpFluidDosingService_pb2'
  # @@protoc_insertion_point(class_scope:sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.GenerateFlow_Parameters)
  })
_sym_db.RegisterMessage(GenerateFlow_Parameters)

GenerateFlow_IntermediateResponses = _reflection.GeneratedProtocolMessageType('GenerateFlow_IntermediateResponses', (_message.Message,), {
  'DESCRIPTOR' : _GENERATEFLOW_INTERMEDIATERESPONSES,
  '__module__' : 'PumpFluidDosingService_pb2'
  # @@protoc_insertion_point(class_scope:sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.GenerateFlow_IntermediateResponses)
  })
_sym_db.RegisterMessage(GenerateFlow_IntermediateResponses)

GenerateFlow_Responses = _reflection.GeneratedProtocolMessageType('GenerateFlow_Responses', (_message.Message,), {
  'DESCRIPTOR' : _GENERATEFLOW_RESPONSES,
  '__module__' : 'PumpFluidDosingService_pb2'
  # @@protoc_insertion_point(class_scope:sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.GenerateFlow_Responses)
  })
_sym_db.RegisterMessage(GenerateFlow_Responses)

StopDosage_Parameters = _reflection.GeneratedProtocolMessageType('StopDosage_Parameters', (_message.Message,), {
  'DESCRIPTOR' : _STOPDOSAGE_PARAMETERS,
  '__module__' : 'PumpFluidDosingService_pb2'
  # @@protoc_insertion_point(class_scope:sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.StopDosage_Parameters)
  })
_sym_db.RegisterMessage(StopDosage_Parameters)

StopDosage_Responses = _reflection.GeneratedProtocolMessageType('StopDosage_Responses', (_message.Message,), {
  'DESCRIPTOR' : _STOPDOSAGE_RESPONSES,
  '__module__' : 'PumpFluidDosingService_pb2'
  # @@protoc_insertion_point(class_scope:sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.StopDosage_Responses)
  })
_sym_db.RegisterMessage(StopDosage_Responses)

Get_MaxSyringeFillLevel_Parameters = _reflection.GeneratedProtocolMessageType('Get_MaxSyringeFillLevel_Parameters', (_message.Message,), {
  'DESCRIPTOR' : _GET_MAXSYRINGEFILLLEVEL_PARAMETERS,
  '__module__' : 'PumpFluidDosingService_pb2'
  # @@protoc_insertion_point(class_scope:sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.Get_MaxSyringeFillLevel_Parameters)
  })
_sym_db.RegisterMessage(Get_MaxSyringeFillLevel_Parameters)

Get_MaxSyringeFillLevel_Responses = _reflection.GeneratedProtocolMessageType('Get_MaxSyringeFillLevel_Responses', (_message.Message,), {
  'DESCRIPTOR' : _GET_MAXSYRINGEFILLLEVEL_RESPONSES,
  '__module__' : 'PumpFluidDosingService_pb2'
  # @@protoc_insertion_point(class_scope:sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.Get_MaxSyringeFillLevel_Responses)
  })
_sym_db.RegisterMessage(Get_MaxSyringeFillLevel_Responses)

Subscribe_SyringeFillLevel_Parameters = _reflection.GeneratedProtocolMessageType('Subscribe_SyringeFillLevel_Parameters', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBE_SYRINGEFILLLEVEL_PARAMETERS,
  '__module__' : 'PumpFluidDosingService_pb2'
  # @@protoc_insertion_point(class_scope:sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.Subscribe_SyringeFillLevel_Parameters)
  })
_sym_db.RegisterMessage(Subscribe_SyringeFillLevel_Parameters)

Subscribe_SyringeFillLevel_Responses = _reflection.GeneratedProtocolMessageType('Subscribe_SyringeFillLevel_Responses', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBE_SYRINGEFILLLEVEL_RESPONSES,
  '__module__' : 'PumpFluidDosingService_pb2'
  # @@protoc_insertion_point(class_scope:sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.Subscribe_SyringeFillLevel_Responses)
  })
_sym_db.RegisterMessage(Subscribe_SyringeFillLevel_Responses)

Get_MaxFlowRate_Parameters = _reflection.GeneratedProtocolMessageType('Get_MaxFlowRate_Parameters', (_message.Message,), {
  'DESCRIPTOR' : _GET_MAXFLOWRATE_PARAMETERS,
  '__module__' : 'PumpFluidDosingService_pb2'
  # @@protoc_insertion_point(class_scope:sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.Get_MaxFlowRate_Parameters)
  })
_sym_db.RegisterMessage(Get_MaxFlowRate_Parameters)

Get_MaxFlowRate_Responses = _reflection.GeneratedProtocolMessageType('Get_MaxFlowRate_Responses', (_message.Message,), {
  'DESCRIPTOR' : _GET_MAXFLOWRATE_RESPONSES,
  '__module__' : 'PumpFluidDosingService_pb2'
  # @@protoc_insertion_point(class_scope:sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.Get_MaxFlowRate_Responses)
  })
_sym_db.RegisterMessage(Get_MaxFlowRate_Responses)

Get_MinFlowRate_Parameters = _reflection.GeneratedProtocolMessageType('Get_MinFlowRate_Parameters', (_message.Message,), {
  'DESCRIPTOR' : _GET_MINFLOWRATE_PARAMETERS,
  '__module__' : 'PumpFluidDosingService_pb2'
  # @@protoc_insertion_point(class_scope:sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.Get_MinFlowRate_Parameters)
  })
_sym_db.RegisterMessage(Get_MinFlowRate_Parameters)

Get_MinFlowRate_Responses = _reflection.GeneratedProtocolMessageType('Get_MinFlowRate_Responses', (_message.Message,), {
  'DESCRIPTOR' : _GET_MINFLOWRATE_RESPONSES,
  '__module__' : 'PumpFluidDosingService_pb2'
  # @@protoc_insertion_point(class_scope:sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.Get_MinFlowRate_Responses)
  })
_sym_db.RegisterMessage(Get_MinFlowRate_Responses)

Subscribe_FlowRate_Parameters = _reflection.GeneratedProtocolMessageType('Subscribe_FlowRate_Parameters', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBE_FLOWRATE_PARAMETERS,
  '__module__' : 'PumpFluidDosingService_pb2'
  # @@protoc_insertion_point(class_scope:sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.Subscribe_FlowRate_Parameters)
  })
_sym_db.RegisterMessage(Subscribe_FlowRate_Parameters)

Subscribe_FlowRate_Responses = _reflection.GeneratedProtocolMessageType('Subscribe_FlowRate_Responses', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBE_FLOWRATE_RESPONSES,
  '__module__' : 'PumpFluidDosingService_pb2'
  # @@protoc_insertion_point(class_scope:sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.Subscribe_FlowRate_Responses)
  })
_sym_db.RegisterMessage(Subscribe_FlowRate_Responses)



_PUMPFLUIDDOSINGSERVICE = _descriptor.ServiceDescriptor(
  name='PumpFluidDosingService',
  full_name='sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.PumpFluidDosingService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1885,
  serialized_end=4563,
  methods=[
  _descriptor.MethodDescriptor(
    name='SetFillLevel',
    full_name='sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.PumpFluidDosingService.SetFillLevel',
    index=0,
    containing_service=None,
    input_type=_SETFILLLEVEL_PARAMETERS,
    output_type=SiLAFramework__pb2._COMMANDCONFIRMATION,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SetFillLevel_Info',
    full_name='sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.PumpFluidDosingService.SetFillLevel_Info',
    index=1,
    containing_service=None,
    input_type=SiLAFramework__pb2._COMMANDEXECUTIONUUID,
    output_type=SiLAFramework__pb2._EXECUTIONINFO,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SetFillLevel_Result',
    full_name='sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.PumpFluidDosingService.SetFillLevel_Result',
    index=2,
    containing_service=None,
    input_type=SiLAFramework__pb2._COMMANDEXECUTIONUUID,
    output_type=_SETFILLLEVEL_RESPONSES,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DoseVolume',
    full_name='sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.PumpFluidDosingService.DoseVolume',
    index=3,
    containing_service=None,
    input_type=_DOSEVOLUME_PARAMETERS,
    output_type=SiLAFramework__pb2._COMMANDCONFIRMATION,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DoseVolume_Info',
    full_name='sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.PumpFluidDosingService.DoseVolume_Info',
    index=4,
    containing_service=None,
    input_type=SiLAFramework__pb2._COMMANDEXECUTIONUUID,
    output_type=SiLAFramework__pb2._EXECUTIONINFO,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DoseVolume_Result',
    full_name='sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.PumpFluidDosingService.DoseVolume_Result',
    index=5,
    containing_service=None,
    input_type=SiLAFramework__pb2._COMMANDEXECUTIONUUID,
    output_type=_DOSEVOLUME_RESPONSES,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GenerateFlow',
    full_name='sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.PumpFluidDosingService.GenerateFlow',
    index=6,
    containing_service=None,
    input_type=_GENERATEFLOW_PARAMETERS,
    output_type=SiLAFramework__pb2._COMMANDCONFIRMATION,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GenerateFlow_Intermediate',
    full_name='sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.PumpFluidDosingService.GenerateFlow_Intermediate',
    index=7,
    containing_service=None,
    input_type=SiLAFramework__pb2._COMMANDEXECUTIONUUID,
    output_type=_GENERATEFLOW_INTERMEDIATERESPONSES,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GenerateFlow_Info',
    full_name='sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.PumpFluidDosingService.GenerateFlow_Info',
    index=8,
    containing_service=None,
    input_type=SiLAFramework__pb2._COMMANDEXECUTIONUUID,
    output_type=SiLAFramework__pb2._EXECUTIONINFO,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GenerateFlow_Result',
    full_name='sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.PumpFluidDosingService.GenerateFlow_Result',
    index=9,
    containing_service=None,
    input_type=SiLAFramework__pb2._COMMANDEXECUTIONUUID,
    output_type=_GENERATEFLOW_RESPONSES,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='StopDosage',
    full_name='sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.PumpFluidDosingService.StopDosage',
    index=10,
    containing_service=None,
    input_type=_STOPDOSAGE_PARAMETERS,
    output_type=_STOPDOSAGE_RESPONSES,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Get_MaxSyringeFillLevel',
    full_name='sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.PumpFluidDosingService.Get_MaxSyringeFillLevel',
    index=11,
    containing_service=None,
    input_type=_GET_MAXSYRINGEFILLLEVEL_PARAMETERS,
    output_type=_GET_MAXSYRINGEFILLLEVEL_RESPONSES,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Subscribe_SyringeFillLevel',
    full_name='sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.PumpFluidDosingService.Subscribe_SyringeFillLevel',
    index=12,
    containing_service=None,
    input_type=_SUBSCRIBE_SYRINGEFILLLEVEL_PARAMETERS,
    output_type=_SUBSCRIBE_SYRINGEFILLLEVEL_RESPONSES,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Get_MaxFlowRate',
    full_name='sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.PumpFluidDosingService.Get_MaxFlowRate',
    index=13,
    containing_service=None,
    input_type=_GET_MAXFLOWRATE_PARAMETERS,
    output_type=_GET_MAXFLOWRATE_RESPONSES,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Get_MinFlowRate',
    full_name='sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.PumpFluidDosingService.Get_MinFlowRate',
    index=14,
    containing_service=None,
    input_type=_GET_MINFLOWRATE_PARAMETERS,
    output_type=_GET_MINFLOWRATE_RESPONSES,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Subscribe_FlowRate',
    full_name='sila2.de.cetoni.pumps.syringepumps.pumpfluiddosingservice.v1.PumpFluidDosingService.Subscribe_FlowRate',
    index=15,
    containing_service=None,
    input_type=_SUBSCRIBE_FLOWRATE_PARAMETERS,
    output_type=_SUBSCRIBE_FLOWRATE_RESPONSES,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_PUMPFLUIDDOSINGSERVICE)

DESCRIPTOR.services_by_name['PumpFluidDosingService'] = _PUMPFLUIDDOSINGSERVICE

# @@protoc_insertion_point(module_scope)
