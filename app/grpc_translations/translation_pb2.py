# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: translation.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11translation.proto\"\x1e\n\x04News\x12\x16\n\x04news\x18\x01 \x03(\x0b\x32\x08.OneNews\"b\n\x07OneNews\x12\'\n\x08one_news\x18\x01 \x03(\x0b\x32\x15.OneNews.OneNewsEntry\x1a.\n\x0cOneNewsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\" \n\x0cNewsResponse\x12\x10\n\x08response\x18\x01 \x01(\t23\n\x0eNewsTranslator\x12!\n\x07GetNews\x12\x05.News\x1a\r.NewsResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'translation_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _ONENEWS_ONENEWSENTRY._options = None
  _ONENEWS_ONENEWSENTRY._serialized_options = b'8\001'
  _globals['_NEWS']._serialized_start=21
  _globals['_NEWS']._serialized_end=51
  _globals['_ONENEWS']._serialized_start=53
  _globals['_ONENEWS']._serialized_end=151
  _globals['_ONENEWS_ONENEWSENTRY']._serialized_start=105
  _globals['_ONENEWS_ONENEWSENTRY']._serialized_end=151
  _globals['_NEWSRESPONSE']._serialized_start=153
  _globals['_NEWSRESPONSE']._serialized_end=185
  _globals['_NEWSTRANSLATOR']._serialized_start=187
  _globals['_NEWSTRANSLATOR']._serialized_end=238
# @@protoc_insertion_point(module_scope)