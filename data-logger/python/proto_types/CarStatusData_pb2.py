# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: CarStatusData.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='CarStatusData.proto',
  package='deepf1.twenty_eighteen.protobuf',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x13\x43\x61rStatusData.proto\x12\x1f\x64\x65\x65pf1.twenty_eighteen.protobuf\"\xa3\x05\n\rCarStatusData\x12\x19\n\x11m_tractionControl\x18\x01 \x01(\r\x12\x18\n\x10m_antiLockBrakes\x18\x02 \x01(\r\x12\x11\n\tm_fuelMix\x18\x03 \x01(\r\x12\x18\n\x10m_frontBrakeBias\x18\x04 \x01(\r\x12\x1a\n\x12m_pitLimiterStatus\x18\x05 \x01(\r\x12\x14\n\x0cm_fuelInTank\x18\x06 \x01(\x02\x12\x16\n\x0em_fuelCapacity\x18\x07 \x01(\x02\x12\x10\n\x08m_maxRPM\x18\x08 \x01(\r\x12\x11\n\tm_idleRPM\x18\t \x01(\r\x12\x12\n\nm_maxGears\x18\n \x01(\r\x12\x14\n\x0cm_drsAllowed\x18\x0b \x01(\r\x12\x13\n\x0bm_tyresWear\x18\x0c \x03(\r\x12\x16\n\x0em_tyreCompound\x18\r \x01(\r\x12\x15\n\rm_tyresDamage\x18\x0e \x03(\r\x12\x1d\n\x15m_frontLeftWingDamage\x18\x0f \x01(\r\x12\x1e\n\x16m_frontRightWingDamage\x18\x10 \x01(\r\x12\x18\n\x10m_rearWingDamage\x18\x11 \x01(\r\x12\x16\n\x0em_engineDamage\x18\x12 \x01(\r\x12\x17\n\x0fm_gearBoxDamage\x18\x13 \x01(\r\x12\x17\n\x0fm_exhaustDamage\x18\x14 \x01(\r\x12\x19\n\x11m_vehicleFiaFlags\x18\x15 \x01(\x05\x12\x18\n\x10m_ersStoreEnergy\x18\x16 \x01(\x02\x12\x17\n\x0fm_ersDeployMode\x18\x17 \x01(\r\x12!\n\x19m_ersHarvestedThisLapMGUK\x18\x18 \x01(\x02\x12!\n\x19m_ersHarvestedThisLapMGUH\x18\x19 \x01(\x02\x12\x1c\n\x14m_ersDeployedThisLap\x18\x1a \x01(\x02\x62\x06proto3')
)




_CARSTATUSDATA = _descriptor.Descriptor(
  name='CarStatusData',
  full_name='deepf1.twenty_eighteen.protobuf.CarStatusData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='m_tractionControl', full_name='deepf1.twenty_eighteen.protobuf.CarStatusData.m_tractionControl', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='m_antiLockBrakes', full_name='deepf1.twenty_eighteen.protobuf.CarStatusData.m_antiLockBrakes', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='m_fuelMix', full_name='deepf1.twenty_eighteen.protobuf.CarStatusData.m_fuelMix', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='m_frontBrakeBias', full_name='deepf1.twenty_eighteen.protobuf.CarStatusData.m_frontBrakeBias', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='m_pitLimiterStatus', full_name='deepf1.twenty_eighteen.protobuf.CarStatusData.m_pitLimiterStatus', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='m_fuelInTank', full_name='deepf1.twenty_eighteen.protobuf.CarStatusData.m_fuelInTank', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='m_fuelCapacity', full_name='deepf1.twenty_eighteen.protobuf.CarStatusData.m_fuelCapacity', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='m_maxRPM', full_name='deepf1.twenty_eighteen.protobuf.CarStatusData.m_maxRPM', index=7,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='m_idleRPM', full_name='deepf1.twenty_eighteen.protobuf.CarStatusData.m_idleRPM', index=8,
      number=9, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='m_maxGears', full_name='deepf1.twenty_eighteen.protobuf.CarStatusData.m_maxGears', index=9,
      number=10, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='m_drsAllowed', full_name='deepf1.twenty_eighteen.protobuf.CarStatusData.m_drsAllowed', index=10,
      number=11, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='m_tyresWear', full_name='deepf1.twenty_eighteen.protobuf.CarStatusData.m_tyresWear', index=11,
      number=12, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='m_tyreCompound', full_name='deepf1.twenty_eighteen.protobuf.CarStatusData.m_tyreCompound', index=12,
      number=13, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='m_tyresDamage', full_name='deepf1.twenty_eighteen.protobuf.CarStatusData.m_tyresDamage', index=13,
      number=14, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='m_frontLeftWingDamage', full_name='deepf1.twenty_eighteen.protobuf.CarStatusData.m_frontLeftWingDamage', index=14,
      number=15, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='m_frontRightWingDamage', full_name='deepf1.twenty_eighteen.protobuf.CarStatusData.m_frontRightWingDamage', index=15,
      number=16, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='m_rearWingDamage', full_name='deepf1.twenty_eighteen.protobuf.CarStatusData.m_rearWingDamage', index=16,
      number=17, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='m_engineDamage', full_name='deepf1.twenty_eighteen.protobuf.CarStatusData.m_engineDamage', index=17,
      number=18, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='m_gearBoxDamage', full_name='deepf1.twenty_eighteen.protobuf.CarStatusData.m_gearBoxDamage', index=18,
      number=19, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='m_exhaustDamage', full_name='deepf1.twenty_eighteen.protobuf.CarStatusData.m_exhaustDamage', index=19,
      number=20, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='m_vehicleFiaFlags', full_name='deepf1.twenty_eighteen.protobuf.CarStatusData.m_vehicleFiaFlags', index=20,
      number=21, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='m_ersStoreEnergy', full_name='deepf1.twenty_eighteen.protobuf.CarStatusData.m_ersStoreEnergy', index=21,
      number=22, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='m_ersDeployMode', full_name='deepf1.twenty_eighteen.protobuf.CarStatusData.m_ersDeployMode', index=22,
      number=23, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='m_ersHarvestedThisLapMGUK', full_name='deepf1.twenty_eighteen.protobuf.CarStatusData.m_ersHarvestedThisLapMGUK', index=23,
      number=24, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='m_ersHarvestedThisLapMGUH', full_name='deepf1.twenty_eighteen.protobuf.CarStatusData.m_ersHarvestedThisLapMGUH', index=24,
      number=25, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='m_ersDeployedThisLap', full_name='deepf1.twenty_eighteen.protobuf.CarStatusData.m_ersDeployedThisLap', index=25,
      number=26, type=2, cpp_type=6, label=1,
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
  serialized_start=57,
  serialized_end=732,
)

DESCRIPTOR.message_types_by_name['CarStatusData'] = _CARSTATUSDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CarStatusData = _reflection.GeneratedProtocolMessageType('CarStatusData', (_message.Message,), {
  'DESCRIPTOR' : _CARSTATUSDATA,
  '__module__' : 'CarStatusData_pb2'
  # @@protoc_insertion_point(class_scope:deepf1.twenty_eighteen.protobuf.CarStatusData)
  })
_sym_db.RegisterMessage(CarStatusData)


# @@protoc_insertion_point(module_scope)