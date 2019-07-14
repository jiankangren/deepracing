# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: TimestampedPacketMotionData.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import PacketMotionData_pb2 as PacketMotionData__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='TimestampedPacketMotionData.proto',
  package='deepf1.twenty_eighteen.protobuf',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n!TimestampedPacketMotionData.proto\x12\x1f\x64\x65\x65pf1.twenty_eighteen.protobuf\x1a\x16PacketMotionData.proto\"w\n\x1bTimestampedPacketMotionData\x12\x45\n\nudp_packet\x18\x01 \x01(\x0b\x32\x31.deepf1.twenty_eighteen.protobuf.PacketMotionData\x12\x11\n\ttimestamp\x18\x02 \x01(\x01\x62\x06proto3')
  ,
  dependencies=[PacketMotionData__pb2.DESCRIPTOR,])




_TIMESTAMPEDPACKETMOTIONDATA = _descriptor.Descriptor(
  name='TimestampedPacketMotionData',
  full_name='deepf1.twenty_eighteen.protobuf.TimestampedPacketMotionData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='udp_packet', full_name='deepf1.twenty_eighteen.protobuf.TimestampedPacketMotionData.udp_packet', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='deepf1.twenty_eighteen.protobuf.TimestampedPacketMotionData.timestamp', index=1,
      number=2, type=1, cpp_type=5, label=1,
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
  serialized_start=94,
  serialized_end=213,
)

_TIMESTAMPEDPACKETMOTIONDATA.fields_by_name['udp_packet'].message_type = PacketMotionData__pb2._PACKETMOTIONDATA
DESCRIPTOR.message_types_by_name['TimestampedPacketMotionData'] = _TIMESTAMPEDPACKETMOTIONDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TimestampedPacketMotionData = _reflection.GeneratedProtocolMessageType('TimestampedPacketMotionData', (_message.Message,), {
  'DESCRIPTOR' : _TIMESTAMPEDPACKETMOTIONDATA,
  '__module__' : 'TimestampedPacketMotionData_pb2'
  # @@protoc_insertion_point(class_scope:deepf1.twenty_eighteen.protobuf.TimestampedPacketMotionData)
  })
_sym_db.RegisterMessage(TimestampedPacketMotionData)


# @@protoc_insertion_point(module_scope)