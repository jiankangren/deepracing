# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: TimestampedImage.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='TimestampedImage.proto',
  package='deepf1.protobuf',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x16TimestampedImage.proto\x12\x0f\x64\x65\x65pf1.protobuf\"9\n\x10TimestampedImage\x12\x12\n\nimage_file\x18\x01 \x01(\t\x12\x11\n\ttimestamp\x18\x02 \x01(\x01\x62\x06proto3')
)




_TIMESTAMPEDIMAGE = _descriptor.Descriptor(
  name='TimestampedImage',
  full_name='deepf1.protobuf.TimestampedImage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='image_file', full_name='deepf1.protobuf.TimestampedImage.image_file', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='deepf1.protobuf.TimestampedImage.timestamp', index=1,
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
  serialized_start=43,
  serialized_end=100,
)

DESCRIPTOR.message_types_by_name['TimestampedImage'] = _TIMESTAMPEDIMAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TimestampedImage = _reflection.GeneratedProtocolMessageType('TimestampedImage', (_message.Message,), {
  'DESCRIPTOR' : _TIMESTAMPEDIMAGE,
  '__module__' : 'TimestampedImage_pb2'
  # @@protoc_insertion_point(class_scope:deepf1.protobuf.TimestampedImage)
  })
_sym_db.RegisterMessage(TimestampedImage)


# @@protoc_insertion_point(module_scope)
