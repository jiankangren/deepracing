# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: TimestampedPacketLapData.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import PacketLapData_pb2 as PacketLapData__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='TimestampedPacketLapData.proto',
  package='deepf1.twenty_eighteen.protobuf',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1eTimestampedPacketLapData.proto\x12\x1f\x64\x65\x65pf1.twenty_eighteen.protobuf\x1a\x13PacketLapData.proto\"q\n\x18TimestampedPacketLapData\x12\x42\n\nudp_packet\x18\x01 \x01(\x0b\x32..deepf1.twenty_eighteen.protobuf.PacketLapData\x12\x11\n\ttimestamp\x18\x02 \x01(\x01\x62\x06proto3')
  ,
  dependencies=[PacketLapData__pb2.DESCRIPTOR,])




_TIMESTAMPEDPACKETLAPDATA = _descriptor.Descriptor(
  name='TimestampedPacketLapData',
  full_name='deepf1.twenty_eighteen.protobuf.TimestampedPacketLapData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='udp_packet', full_name='deepf1.twenty_eighteen.protobuf.TimestampedPacketLapData.udp_packet', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='deepf1.twenty_eighteen.protobuf.TimestampedPacketLapData.timestamp', index=1,
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
  serialized_start=88,
  serialized_end=201,
)

_TIMESTAMPEDPACKETLAPDATA.fields_by_name['udp_packet'].message_type = PacketLapData__pb2._PACKETLAPDATA
DESCRIPTOR.message_types_by_name['TimestampedPacketLapData'] = _TIMESTAMPEDPACKETLAPDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TimestampedPacketLapData = _reflection.GeneratedProtocolMessageType('TimestampedPacketLapData', (_message.Message,), {
  'DESCRIPTOR' : _TIMESTAMPEDPACKETLAPDATA,
  '__module__' : 'TimestampedPacketLapData_pb2'
  # @@protoc_insertion_point(class_scope:deepf1.twenty_eighteen.protobuf.TimestampedPacketLapData)
  })
_sym_db.RegisterMessage(TimestampedPacketLapData)


# @@protoc_insertion_point(module_scope)