# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bnet/game_utilities_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import bnet.attribute_pb2
import bnet.entity_pb2
import bnet.game_utilities_types_pb2
import bnet.rpc_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='bnet/game_utilities_service.proto',
  package='bnet.protocol.game_utilities',
  serialized_pb=_b('\n!bnet/game_utilities_service.proto\x12\x1c\x62net.protocol.game_utilities\x1a\x14\x62net/attribute.proto\x1a\x11\x62net/entity.proto\x1a\x1f\x62net/game_utilities_types.proto\x1a\x0e\x62net/rpc.proto\"\xd2\x01\n\rClientRequest\x12\x35\n\tattribute\x18\x01 \x03(\x0b\x32\".bnet.protocol.attribute.Attribute\x12&\n\x04host\x18\x02 \x01(\x0b\x32\x18.bnet.protocol.ProcessId\x12\x30\n\x0f\x62net_account_id\x18\x03 \x01(\x0b\x32\x17.bnet.protocol.EntityId\x12\x30\n\x0fgame_account_id\x18\x04 \x01(\x0b\x32\x17.bnet.protocol.EntityId\"G\n\x0e\x43lientResponse\x12\x35\n\tattribute\x18\x01 \x03(\x0b\x32\".bnet.protocol.attribute.Attribute\"\x7f\n\rServerRequest\x12\x35\n\tattribute\x18\x01 \x03(\x0b\x32\".bnet.protocol.attribute.Attribute\x12\x0f\n\x07program\x18\x02 \x02(\x07\x12&\n\x04host\x18\x03 \x01(\x0b\x32\x18.bnet.protocol.ProcessId\"G\n\x0eServerResponse\x12\x35\n\tattribute\x18\x01 \x03(\x0b\x32\".bnet.protocol.attribute.Attribute\"\xd0\x01\n\x1dPresenceChannelCreatedRequest\x12#\n\x02id\x18\x01 \x02(\x0b\x32\x17.bnet.protocol.EntityId\x12\x30\n\x0fgame_account_id\x18\x03 \x01(\x0b\x32\x17.bnet.protocol.EntityId\x12\x30\n\x0f\x62net_account_id\x18\x04 \x01(\x0b\x32\x17.bnet.protocol.EntityId\x12&\n\x04host\x18\x05 \x01(\x0b\x32\x18.bnet.protocol.ProcessId\"\x8c\x01\n\x19GetPlayerVariablesRequest\x12G\n\x10player_variables\x18\x01 \x03(\x0b\x32-.bnet.protocol.game_utilities.PlayerVariables\x12&\n\x04host\x18\x02 \x01(\x0b\x32\x18.bnet.protocol.ProcessId\"e\n\x1aGetPlayerVariablesResponse\x12G\n\x10player_variables\x18\x01 \x03(\x0b\x32-.bnet.protocol.game_utilities.PlayerVariables\"y\n\x1dGameAccountOnlineNotification\x12\x30\n\x0fgame_account_id\x18\x01 \x02(\x0b\x32\x17.bnet.protocol.EntityId\x12&\n\x04host\x18\x02 \x01(\x0b\x32\x18.bnet.protocol.ProcessId\"z\n\x1eGameAccountOfflineNotification\x12\x30\n\x0fgame_account_id\x18\x01 \x02(\x0b\x32\x17.bnet.protocol.EntityId\x12&\n\x04host\x18\x02 \x01(\x0b\x32\x18.bnet.protocol.ProcessId')
  ,
  dependencies=[bnet.attribute_pb2.DESCRIPTOR,bnet.entity_pb2.DESCRIPTOR,bnet.game_utilities_types_pb2.DESCRIPTOR,bnet.rpc_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_CLIENTREQUEST = _descriptor.Descriptor(
  name='ClientRequest',
  full_name='bnet.protocol.game_utilities.ClientRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='attribute', full_name='bnet.protocol.game_utilities.ClientRequest.attribute', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='host', full_name='bnet.protocol.game_utilities.ClientRequest.host', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bnet_account_id', full_name='bnet.protocol.game_utilities.ClientRequest.bnet_account_id', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='game_account_id', full_name='bnet.protocol.game_utilities.ClientRequest.game_account_id', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  serialized_start=158,
  serialized_end=368,
)


_CLIENTRESPONSE = _descriptor.Descriptor(
  name='ClientResponse',
  full_name='bnet.protocol.game_utilities.ClientResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='attribute', full_name='bnet.protocol.game_utilities.ClientResponse.attribute', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=370,
  serialized_end=441,
)


_SERVERREQUEST = _descriptor.Descriptor(
  name='ServerRequest',
  full_name='bnet.protocol.game_utilities.ServerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='attribute', full_name='bnet.protocol.game_utilities.ServerRequest.attribute', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='program', full_name='bnet.protocol.game_utilities.ServerRequest.program', index=1,
      number=2, type=7, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='host', full_name='bnet.protocol.game_utilities.ServerRequest.host', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=443,
  serialized_end=570,
)


_SERVERRESPONSE = _descriptor.Descriptor(
  name='ServerResponse',
  full_name='bnet.protocol.game_utilities.ServerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='attribute', full_name='bnet.protocol.game_utilities.ServerResponse.attribute', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=572,
  serialized_end=643,
)


_PRESENCECHANNELCREATEDREQUEST = _descriptor.Descriptor(
  name='PresenceChannelCreatedRequest',
  full_name='bnet.protocol.game_utilities.PresenceChannelCreatedRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='bnet.protocol.game_utilities.PresenceChannelCreatedRequest.id', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='game_account_id', full_name='bnet.protocol.game_utilities.PresenceChannelCreatedRequest.game_account_id', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bnet_account_id', full_name='bnet.protocol.game_utilities.PresenceChannelCreatedRequest.bnet_account_id', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='host', full_name='bnet.protocol.game_utilities.PresenceChannelCreatedRequest.host', index=3,
      number=5, type=11, cpp_type=10, label=1,
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
  serialized_start=646,
  serialized_end=854,
)


_GETPLAYERVARIABLESREQUEST = _descriptor.Descriptor(
  name='GetPlayerVariablesRequest',
  full_name='bnet.protocol.game_utilities.GetPlayerVariablesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='player_variables', full_name='bnet.protocol.game_utilities.GetPlayerVariablesRequest.player_variables', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='host', full_name='bnet.protocol.game_utilities.GetPlayerVariablesRequest.host', index=1,
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
  serialized_start=857,
  serialized_end=997,
)


_GETPLAYERVARIABLESRESPONSE = _descriptor.Descriptor(
  name='GetPlayerVariablesResponse',
  full_name='bnet.protocol.game_utilities.GetPlayerVariablesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='player_variables', full_name='bnet.protocol.game_utilities.GetPlayerVariablesResponse.player_variables', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=999,
  serialized_end=1100,
)


_GAMEACCOUNTONLINENOTIFICATION = _descriptor.Descriptor(
  name='GameAccountOnlineNotification',
  full_name='bnet.protocol.game_utilities.GameAccountOnlineNotification',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='game_account_id', full_name='bnet.protocol.game_utilities.GameAccountOnlineNotification.game_account_id', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='host', full_name='bnet.protocol.game_utilities.GameAccountOnlineNotification.host', index=1,
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
  serialized_start=1102,
  serialized_end=1223,
)


_GAMEACCOUNTOFFLINENOTIFICATION = _descriptor.Descriptor(
  name='GameAccountOfflineNotification',
  full_name='bnet.protocol.game_utilities.GameAccountOfflineNotification',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='game_account_id', full_name='bnet.protocol.game_utilities.GameAccountOfflineNotification.game_account_id', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='host', full_name='bnet.protocol.game_utilities.GameAccountOfflineNotification.host', index=1,
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
  serialized_start=1225,
  serialized_end=1347,
)

_CLIENTREQUEST.fields_by_name['attribute'].message_type = bnet.attribute_pb2._ATTRIBUTE
_CLIENTREQUEST.fields_by_name['host'].message_type = bnet.rpc_pb2._PROCESSID
_CLIENTREQUEST.fields_by_name['bnet_account_id'].message_type = bnet.entity_pb2._ENTITYID
_CLIENTREQUEST.fields_by_name['game_account_id'].message_type = bnet.entity_pb2._ENTITYID
_CLIENTRESPONSE.fields_by_name['attribute'].message_type = bnet.attribute_pb2._ATTRIBUTE
_SERVERREQUEST.fields_by_name['attribute'].message_type = bnet.attribute_pb2._ATTRIBUTE
_SERVERREQUEST.fields_by_name['host'].message_type = bnet.rpc_pb2._PROCESSID
_SERVERRESPONSE.fields_by_name['attribute'].message_type = bnet.attribute_pb2._ATTRIBUTE
_PRESENCECHANNELCREATEDREQUEST.fields_by_name['id'].message_type = bnet.entity_pb2._ENTITYID
_PRESENCECHANNELCREATEDREQUEST.fields_by_name['game_account_id'].message_type = bnet.entity_pb2._ENTITYID
_PRESENCECHANNELCREATEDREQUEST.fields_by_name['bnet_account_id'].message_type = bnet.entity_pb2._ENTITYID
_PRESENCECHANNELCREATEDREQUEST.fields_by_name['host'].message_type = bnet.rpc_pb2._PROCESSID
_GETPLAYERVARIABLESREQUEST.fields_by_name['player_variables'].message_type = bnet.game_utilities_types_pb2._PLAYERVARIABLES
_GETPLAYERVARIABLESREQUEST.fields_by_name['host'].message_type = bnet.rpc_pb2._PROCESSID
_GETPLAYERVARIABLESRESPONSE.fields_by_name['player_variables'].message_type = bnet.game_utilities_types_pb2._PLAYERVARIABLES
_GAMEACCOUNTONLINENOTIFICATION.fields_by_name['game_account_id'].message_type = bnet.entity_pb2._ENTITYID
_GAMEACCOUNTONLINENOTIFICATION.fields_by_name['host'].message_type = bnet.rpc_pb2._PROCESSID
_GAMEACCOUNTOFFLINENOTIFICATION.fields_by_name['game_account_id'].message_type = bnet.entity_pb2._ENTITYID
_GAMEACCOUNTOFFLINENOTIFICATION.fields_by_name['host'].message_type = bnet.rpc_pb2._PROCESSID
DESCRIPTOR.message_types_by_name['ClientRequest'] = _CLIENTREQUEST
DESCRIPTOR.message_types_by_name['ClientResponse'] = _CLIENTRESPONSE
DESCRIPTOR.message_types_by_name['ServerRequest'] = _SERVERREQUEST
DESCRIPTOR.message_types_by_name['ServerResponse'] = _SERVERRESPONSE
DESCRIPTOR.message_types_by_name['PresenceChannelCreatedRequest'] = _PRESENCECHANNELCREATEDREQUEST
DESCRIPTOR.message_types_by_name['GetPlayerVariablesRequest'] = _GETPLAYERVARIABLESREQUEST
DESCRIPTOR.message_types_by_name['GetPlayerVariablesResponse'] = _GETPLAYERVARIABLESRESPONSE
DESCRIPTOR.message_types_by_name['GameAccountOnlineNotification'] = _GAMEACCOUNTONLINENOTIFICATION
DESCRIPTOR.message_types_by_name['GameAccountOfflineNotification'] = _GAMEACCOUNTOFFLINENOTIFICATION

ClientRequest = _reflection.GeneratedProtocolMessageType('ClientRequest', (_message.Message,), dict(
  DESCRIPTOR = _CLIENTREQUEST,
  __module__ = 'bnet.game_utilities_service_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.game_utilities.ClientRequest)
  ))
_sym_db.RegisterMessage(ClientRequest)

ClientResponse = _reflection.GeneratedProtocolMessageType('ClientResponse', (_message.Message,), dict(
  DESCRIPTOR = _CLIENTRESPONSE,
  __module__ = 'bnet.game_utilities_service_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.game_utilities.ClientResponse)
  ))
_sym_db.RegisterMessage(ClientResponse)

ServerRequest = _reflection.GeneratedProtocolMessageType('ServerRequest', (_message.Message,), dict(
  DESCRIPTOR = _SERVERREQUEST,
  __module__ = 'bnet.game_utilities_service_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.game_utilities.ServerRequest)
  ))
_sym_db.RegisterMessage(ServerRequest)

ServerResponse = _reflection.GeneratedProtocolMessageType('ServerResponse', (_message.Message,), dict(
  DESCRIPTOR = _SERVERRESPONSE,
  __module__ = 'bnet.game_utilities_service_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.game_utilities.ServerResponse)
  ))
_sym_db.RegisterMessage(ServerResponse)

PresenceChannelCreatedRequest = _reflection.GeneratedProtocolMessageType('PresenceChannelCreatedRequest', (_message.Message,), dict(
  DESCRIPTOR = _PRESENCECHANNELCREATEDREQUEST,
  __module__ = 'bnet.game_utilities_service_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.game_utilities.PresenceChannelCreatedRequest)
  ))
_sym_db.RegisterMessage(PresenceChannelCreatedRequest)

GetPlayerVariablesRequest = _reflection.GeneratedProtocolMessageType('GetPlayerVariablesRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETPLAYERVARIABLESREQUEST,
  __module__ = 'bnet.game_utilities_service_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.game_utilities.GetPlayerVariablesRequest)
  ))
_sym_db.RegisterMessage(GetPlayerVariablesRequest)

GetPlayerVariablesResponse = _reflection.GeneratedProtocolMessageType('GetPlayerVariablesResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETPLAYERVARIABLESRESPONSE,
  __module__ = 'bnet.game_utilities_service_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.game_utilities.GetPlayerVariablesResponse)
  ))
_sym_db.RegisterMessage(GetPlayerVariablesResponse)

GameAccountOnlineNotification = _reflection.GeneratedProtocolMessageType('GameAccountOnlineNotification', (_message.Message,), dict(
  DESCRIPTOR = _GAMEACCOUNTONLINENOTIFICATION,
  __module__ = 'bnet.game_utilities_service_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.game_utilities.GameAccountOnlineNotification)
  ))
_sym_db.RegisterMessage(GameAccountOnlineNotification)

GameAccountOfflineNotification = _reflection.GeneratedProtocolMessageType('GameAccountOfflineNotification', (_message.Message,), dict(
  DESCRIPTOR = _GAMEACCOUNTOFFLINENOTIFICATION,
  __module__ = 'bnet.game_utilities_service_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.game_utilities.GameAccountOfflineNotification)
  ))
_sym_db.RegisterMessage(GameAccountOfflineNotification)


# @@protoc_insertion_point(module_scope)
