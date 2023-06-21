# coding: utf-8

"""
    StarkExpress API Docs

    An API for the StarkExpress platform.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from starkexpress_api import schemas  # noqa: F401


class OrderbookLevel2DataDto(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            orderbookId = schemas.UUIDSchema
            
            
            class bids(
                schemas.ListBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneTupleMixin
            ):
            
            
                class MetaOapg:
                    format = 'array'
                    
                    @staticmethod
                    def items() -> typing.Type['OrderbookLevel2EntryDto']:
                        return OrderbookLevel2EntryDto
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[list, tuple, None, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'bids':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class asks(
                schemas.ListBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneTupleMixin
            ):
            
            
                class MetaOapg:
                    format = 'array'
                    
                    @staticmethod
                    def items() -> typing.Type['OrderbookLevel2EntryDto']:
                        return OrderbookLevel2EntryDto
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[list, tuple, None, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'asks':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "orderbookId": orderbookId,
                "bids": bids,
                "asks": asks,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["orderbookId"]) -> MetaOapg.properties.orderbookId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bids"]) -> MetaOapg.properties.bids: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["asks"]) -> MetaOapg.properties.asks: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["orderbookId"], typing_extensions.Literal["bids"], typing_extensions.Literal["asks"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["orderbookId"]) -> typing.Union[MetaOapg.properties.orderbookId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bids"]) -> typing.Union[MetaOapg.properties.bids, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["asks"]) -> typing.Union[MetaOapg.properties.asks, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["orderbookId"], typing_extensions.Literal["bids"], typing_extensions.Literal["asks"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        orderbookId: typing.Union[MetaOapg.properties.orderbookId, str, uuid.UUID, schemas.Unset] = schemas.unset,
        bids: typing.Union[MetaOapg.properties.bids, list, tuple, None, schemas.Unset] = schemas.unset,
        asks: typing.Union[MetaOapg.properties.asks, list, tuple, None, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'OrderbookLevel2DataDto':
        return super().__new__(
            cls,
            *_args,
            orderbookId=orderbookId,
            bids=bids,
            asks=asks,
            _configuration=_configuration,
        )

from starkexpress_api.model.orderbook_level2_entry_dto import OrderbookLevel2EntryDto
