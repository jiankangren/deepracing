# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: LapData.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='LapData.proto',
  package='deepf1.twenty_eighteen.protobuf',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\rLapData.proto\x12\x1f\x64\x65\x65pf1.twenty_eighteen.protobuf\"\x9a\x03\n\x07LapData\x12\x15\n\rm_lastLapTime\x18\x01 \x01(\x02\x12\x18\n\x10m_currentLapTime\x18\x02 \x01(\x02\x12\x15\n\rm_bestLapTime\x18\x03 \x01(\x02\x12\x15\n\rm_sector1Time\x18\x04 \x01(\x02\x12\x15\n\rm_sector2Time\x18\x05 \x01(\x02\x12\x15\n\rm_lapDistance\x18\x06 \x01(\x02\x12\x17\n\x0fm_totalDistance\x18\x07 \x01(\x02\x12\x18\n\x10m_safetyCarDelta\x18\x08 \x01(\x02\x12\x15\n\rm_carPosition\x18\t \x01(\r\x12\x17\n\x0fm_currentLapNum\x18\n \x01(\r\x12\x13\n\x0bm_pitStatus\x18\x0b \x01(\r\x12\x10\n\x08m_sector\x18\x0c \x01(\r\x12\x1b\n\x13m_currentLapInvalid\x18\r \x01(\r\x12\x13\n\x0bm_penalties\x18\x0e \x01(\r\x12\x16\n\x0em_gridPosition\x18\x0f \x01(\r\x12\x16\n\x0em_driverStatus\x18\x10 \x01(\r\x12\x16\n\x0em_resultStatus\x18\x11 \x01(\rb\x06proto3')
)




_LAPDATA = _descriptor.Descriptor(
  name='LapData',
  full_name='deepf1.twenty_eighteen.protobuf.LapData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='m_lastLapTime', full_name='deepf1.twenty_eighteen.protobuf.LapData.m_lastLapTime', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='m_currentLapTime', full_name='deepf1.twenty_eighteen.protobuf.LapData.m_currentLapTime', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='m_bestLapTime', full_name='deepf1.twenty_eighteen.protobuf.LapData.m_bestLapTime', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='m_sector1Time', full_name='deepf1.twenty_eighteen.protobuf.LapData.m_sector1Time', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='m_sector2Time', full_name='deepf1.twenty_eighteen.protobuf.LapData.m_sector2Time', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='m_lapDistance', full_name='deepf1.twenty_eighteen.protobuf.LapData.m_lapDistance', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='m_totalDistance', full_name='deepf1.twenty_eighteen.protobuf.LapData.m_totalDistance', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='m_safetyCarDelta', full_name='deepf1.twenty_eighteen.protobuf.LapData.m_safetyCarDelta', index=7,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='m_carPosition', full_name='deepf1.twenty_eighteen.protobuf.LapData.m_carPosition', index=8,
      number=9, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='m_currentLapNum', full_name='deepf1.twenty_eighteen.protobuf.LapData.m_currentLapNum', index=9,
      number=10, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='m_pitStatus', full_name='deepf1.twenty_eighteen.protobuf.LapData.m_pitStatus', index=10,
      number=11, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='m_sector', full_name='deepf1.twenty_eighteen.protobuf.LapData.m_sector', index=11,
      number=12, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='m_currentLapInvalid', full_name='deepf1.twenty_eighteen.protobuf.LapData.m_currentLapInvalid', index=12,
      number=13, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='m_penalties', full_name='deepf1.twenty_eighteen.protobuf.LapData.m_penalties', index=13,
      number=14, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='m_gridPosition', full_name='deepf1.twenty_eighteen.protobuf.LapData.m_gridPosition', index=14,
      number=15, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='m_driverStatus', full_name='deepf1.twenty_eighteen.protobuf.LapData.m_driverStatus', index=15,
      number=16, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='m_resultStatus', full_name='deepf1.twenty_eighteen.protobuf.LapData.m_resultStatus', index=16,
      number=17, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=51,
  serialized_end=461,
)

DESCRIPTOR.message_types_by_name['LapData'] = _LAPDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LapData = _reflection.GeneratedProtocolMessageType('LapData', (_message.Message,), {
  'DESCRIPTOR' : _LAPDATA,
  '__module__' : 'LapData_pb2'
  # @@protoc_insertion_point(class_scope:deepf1.twenty_eighteen.protobuf.LapData)
  })
_sym_db.RegisterMessage(LapData)


# @@protoc_insertion_point(module_scope)