# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: PacketHeader.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='PacketHeader.proto',
  package='deepf1.twenty_eighteen.protobuf',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x12PacketHeader.proto\x12\x1f\x64\x65\x65pf1.twenty_eighteen.protobuf\"\xb5\x01\n\x0cPacketHeader\x12\x16\n\x0em_packetFormat\x18\x01 \x01(\r\x12\x17\n\x0fm_packetVersion\x18\x02 \x01(\r\x12\x12\n\nm_packetId\x18\x03 \x01(\r\x12\x14\n\x0cm_sessionUID\x18\x04 \x01(\x04\x12\x15\n\rm_sessionTime\x18\x05 \x01(\x02\x12\x19\n\x11m_frameIdentifier\x18\x06 \x01(\r\x12\x18\n\x10m_playerCarIndex\x18\x07 \x01(\rb\x06proto3')
)




_PACKETHEADER = _descriptor.Descriptor(
  name='PacketHeader',
  full_name='deepf1.twenty_eighteen.protobuf.PacketHeader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='m_packetFormat', full_name='deepf1.twenty_eighteen.protobuf.PacketHeader.m_packetFormat', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='m_packetVersion', full_name='deepf1.twenty_eighteen.protobuf.PacketHeader.m_packetVersion', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='m_packetId', full_name='deepf1.twenty_eighteen.protobuf.PacketHeader.m_packetId', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='m_sessionUID', full_name='deepf1.twenty_eighteen.protobuf.PacketHeader.m_sessionUID', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='m_sessionTime', full_name='deepf1.twenty_eighteen.protobuf.PacketHeader.m_sessionTime', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='m_frameIdentifier', full_name='deepf1.twenty_eighteen.protobuf.PacketHeader.m_frameIdentifier', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='m_playerCarIndex', full_name='deepf1.twenty_eighteen.protobuf.PacketHeader.m_playerCarIndex', index=6,
      number=7, type=13, cpp_type=3, label=1,
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
  serialized_start=56,
  serialized_end=237,
)

DESCRIPTOR.message_types_by_name['PacketHeader'] = _PACKETHEADER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PacketHeader = _reflection.GeneratedProtocolMessageType('PacketHeader', (_message.Message,), {
  'DESCRIPTOR' : _PACKETHEADER,
  '__module__' : 'PacketHeader_pb2'
  # @@protoc_insertion_point(class_scope:deepf1.twenty_eighteen.protobuf.PacketHeader)
  })
_sym_db.RegisterMessage(PacketHeader)


# @@protoc_insertion_point(module_scope)