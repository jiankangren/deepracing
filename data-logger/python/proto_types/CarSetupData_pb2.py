# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: CarSetupData.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='CarSetupData.proto',
  package='deepf1.twenty_eighteen.protobuf',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x12\x43\x61rSetupData.proto\x12\x1f\x64\x65\x65pf1.twenty_eighteen.protobuf\"\xf3\x03\n\x0c\x43\x61rSetupData\x12\x13\n\x0bm_frontWing\x18\x01 \x01(\r\x12\x12\n\nm_rearWing\x18\x02 \x01(\r\x12\x14\n\x0cm_onThrottle\x18\x03 \x01(\r\x12\x15\n\rm_offThrottle\x18\x04 \x01(\r\x12\x15\n\rm_frontCamber\x18\x05 \x01(\x02\x12\x14\n\x0cm_rearCamber\x18\x06 \x01(\x02\x12\x12\n\nm_frontToe\x18\x07 \x01(\x02\x12\x11\n\tm_rearToe\x18\x08 \x01(\x02\x12\x19\n\x11m_frontSuspension\x18\t \x01(\r\x12\x18\n\x10m_rearSuspension\x18\n \x01(\r\x12\x1a\n\x12m_frontAntiRollBar\x18\x0b \x01(\r\x12\x19\n\x11m_rearAntiRollBar\x18\x0c \x01(\r\x12\x1f\n\x17m_frontSuspensionHeight\x18\r \x01(\r\x12\x1e\n\x16m_rearSuspensionHeight\x18\x0e \x01(\r\x12\x17\n\x0fm_brakePressure\x18\x0f \x01(\r\x12\x13\n\x0bm_brakeBias\x18\x10 \x01(\r\x12\x1b\n\x13m_frontTyrePressure\x18\x11 \x01(\x02\x12\x1a\n\x12m_rearTyrePressure\x18\x12 \x01(\x02\x12\x11\n\tm_ballast\x18\x13 \x01(\r\x12\x12\n\nm_fuelLoad\x18\x14 \x01(\x02\x62\x06proto3')
)




_CARSETUPDATA = _descriptor.Descriptor(
  name='CarSetupData',
  full_name='deepf1.twenty_eighteen.protobuf.CarSetupData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='m_frontWing', full_name='deepf1.twenty_eighteen.protobuf.CarSetupData.m_frontWing', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='m_rearWing', full_name='deepf1.twenty_eighteen.protobuf.CarSetupData.m_rearWing', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='m_onThrottle', full_name='deepf1.twenty_eighteen.protobuf.CarSetupData.m_onThrottle', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='m_offThrottle', full_name='deepf1.twenty_eighteen.protobuf.CarSetupData.m_offThrottle', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='m_frontCamber', full_name='deepf1.twenty_eighteen.protobuf.CarSetupData.m_frontCamber', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='m_rearCamber', full_name='deepf1.twenty_eighteen.protobuf.CarSetupData.m_rearCamber', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='m_frontToe', full_name='deepf1.twenty_eighteen.protobuf.CarSetupData.m_frontToe', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='m_rearToe', full_name='deepf1.twenty_eighteen.protobuf.CarSetupData.m_rearToe', index=7,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='m_frontSuspension', full_name='deepf1.twenty_eighteen.protobuf.CarSetupData.m_frontSuspension', index=8,
      number=9, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='m_rearSuspension', full_name='deepf1.twenty_eighteen.protobuf.CarSetupData.m_rearSuspension', index=9,
      number=10, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='m_frontAntiRollBar', full_name='deepf1.twenty_eighteen.protobuf.CarSetupData.m_frontAntiRollBar', index=10,
      number=11, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='m_rearAntiRollBar', full_name='deepf1.twenty_eighteen.protobuf.CarSetupData.m_rearAntiRollBar', index=11,
      number=12, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='m_frontSuspensionHeight', full_name='deepf1.twenty_eighteen.protobuf.CarSetupData.m_frontSuspensionHeight', index=12,
      number=13, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='m_rearSuspensionHeight', full_name='deepf1.twenty_eighteen.protobuf.CarSetupData.m_rearSuspensionHeight', index=13,
      number=14, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='m_brakePressure', full_name='deepf1.twenty_eighteen.protobuf.CarSetupData.m_brakePressure', index=14,
      number=15, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='m_brakeBias', full_name='deepf1.twenty_eighteen.protobuf.CarSetupData.m_brakeBias', index=15,
      number=16, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='m_frontTyrePressure', full_name='deepf1.twenty_eighteen.protobuf.CarSetupData.m_frontTyrePressure', index=16,
      number=17, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='m_rearTyrePressure', full_name='deepf1.twenty_eighteen.protobuf.CarSetupData.m_rearTyrePressure', index=17,
      number=18, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='m_ballast', full_name='deepf1.twenty_eighteen.protobuf.CarSetupData.m_ballast', index=18,
      number=19, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='m_fuelLoad', full_name='deepf1.twenty_eighteen.protobuf.CarSetupData.m_fuelLoad', index=19,
      number=20, type=2, cpp_type=6, label=1,
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
  serialized_start=56,
  serialized_end=555,
)

DESCRIPTOR.message_types_by_name['CarSetupData'] = _CARSETUPDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CarSetupData = _reflection.GeneratedProtocolMessageType('CarSetupData', (_message.Message,), {
  'DESCRIPTOR' : _CARSETUPDATA,
  '__module__' : 'CarSetupData_pb2'
  # @@protoc_insertion_point(class_scope:deepf1.twenty_eighteen.protobuf.CarSetupData)
  })
_sym_db.RegisterMessage(CarSetupData)


# @@protoc_insertion_point(module_scope)