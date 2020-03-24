# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bnet/entity.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='bnet/entity.proto',
  package='bnet.protocol',
  serialized_pb=_b('\n\x11\x62net/entity.proto\x12\rbnet.protocol\"%\n\x08\x45ntityId\x12\x0c\n\x04high\x18\x01 \x02(\x06\x12\x0b\n\x03low\x18\x02 \x02(\x06\"i\n\x08Identity\x12+\n\naccount_id\x18\x01 \x01(\x0b\x32\x17.bnet.protocol.EntityId\x12\x30\n\x0fgame_account_id\x18\x02 \x01(\x0b\x32\x17.bnet.protocol.EntityId\"s\n\x0b\x41\x63\x63ountInfo\x12\x1b\n\x0c\x61\x63\x63ount_paid\x18\x01 \x01(\x08:\x05\x66\x61lse\x12\x15\n\ncountry_id\x18\x02 \x01(\x07:\x01\x30\x12\x12\n\nbattle_tag\x18\x03 \x01(\t\x12\x1c\n\rmanual_review\x18\x04 \x01(\x08:\x05\x66\x61lse')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_ENTITYID = _descriptor.Descriptor(
  name='EntityId',
  full_name='bnet.protocol.EntityId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='high', full_name='bnet.protocol.EntityId.high', index=0,
      number=1, type=6, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='low', full_name='bnet.protocol.EntityId.low', index=1,
      number=2, type=6, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=36,
  serialized_end=73,
)


_IDENTITY = _descriptor.Descriptor(
  name='Identity',
  full_name='bnet.protocol.Identity',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='account_id', full_name='bnet.protocol.Identity.account_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='game_account_id', full_name='bnet.protocol.Identity.game_account_id', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=75,
  serialized_end=180,
)


_ACCOUNTINFO = _descriptor.Descriptor(
  name='AccountInfo',
  full_name='bnet.protocol.AccountInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='account_paid', full_name='bnet.protocol.AccountInfo.account_paid', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='country_id', full_name='bnet.protocol.AccountInfo.country_id', index=1,
      number=2, type=7, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='battle_tag', full_name='bnet.protocol.AccountInfo.battle_tag', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='manual_review', full_name='bnet.protocol.AccountInfo.manual_review', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=182,
  serialized_end=297,
)

_IDENTITY.fields_by_name['account_id'].message_type = _ENTITYID
_IDENTITY.fields_by_name['game_account_id'].message_type = _ENTITYID
DESCRIPTOR.message_types_by_name['EntityId'] = _ENTITYID
DESCRIPTOR.message_types_by_name['Identity'] = _IDENTITY
DESCRIPTOR.message_types_by_name['AccountInfo'] = _ACCOUNTINFO

EntityId = _reflection.GeneratedProtocolMessageType('EntityId', (_message.Message,), dict(
  DESCRIPTOR = _ENTITYID,
  __module__ = 'bnet.entity_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.EntityId)
  ))
_sym_db.RegisterMessage(EntityId)

Identity = _reflection.GeneratedProtocolMessageType('Identity', (_message.Message,), dict(
  DESCRIPTOR = _IDENTITY,
  __module__ = 'bnet.entity_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.Identity)
  ))
_sym_db.RegisterMessage(Identity)

AccountInfo = _reflection.GeneratedProtocolMessageType('AccountInfo', (_message.Message,), dict(
  DESCRIPTOR = _ACCOUNTINFO,
  __module__ = 'bnet.entity_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.AccountInfo)
  ))
_sym_db.RegisterMessage(AccountInfo)


# @@protoc_insertion_point(module_scope)