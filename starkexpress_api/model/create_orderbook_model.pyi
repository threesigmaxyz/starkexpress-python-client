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


class CreateOrderbookModel(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Request model to create an orderbook.
    """


    class MetaOapg:
        required = {
            "baseAssetId",
            "quoteAssetPrecision",
            "quoteAssetId",
            "baseAssetPrecision",
        }
        
        class properties:
            baseAssetId = schemas.UUIDSchema
            quoteAssetId = schemas.UUIDSchema
            baseAssetPrecision = schemas.Int32Schema
            quoteAssetPrecision = schemas.Int32Schema
            __annotations__ = {
                "baseAssetId": baseAssetId,
                "quoteAssetId": quoteAssetId,
                "baseAssetPrecision": baseAssetPrecision,
                "quoteAssetPrecision": quoteAssetPrecision,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    baseAssetId: MetaOapg.properties.baseAssetId
    quoteAssetPrecision: MetaOapg.properties.quoteAssetPrecision
    quoteAssetId: MetaOapg.properties.quoteAssetId
    baseAssetPrecision: MetaOapg.properties.baseAssetPrecision
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["baseAssetId"]) -> MetaOapg.properties.baseAssetId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["quoteAssetPrecision"]) -> MetaOapg.properties.quoteAssetPrecision: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["quoteAssetId"]) -> MetaOapg.properties.quoteAssetId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["baseAssetPrecision"]) -> MetaOapg.properties.baseAssetPrecision: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["baseAssetId"], typing_extensions.Literal["quoteAssetPrecision"], typing_extensions.Literal["quoteAssetId"], typing_extensions.Literal["baseAssetPrecision"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["baseAssetId"]) -> MetaOapg.properties.baseAssetId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["quoteAssetPrecision"]) -> MetaOapg.properties.quoteAssetPrecision: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["quoteAssetId"]) -> MetaOapg.properties.quoteAssetId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["baseAssetPrecision"]) -> MetaOapg.properties.baseAssetPrecision: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["baseAssetId"], typing_extensions.Literal["quoteAssetPrecision"], typing_extensions.Literal["quoteAssetId"], typing_extensions.Literal["baseAssetPrecision"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        baseAssetId: typing.Union[MetaOapg.properties.baseAssetId, str, uuid.UUID, ],
        quoteAssetPrecision: typing.Union[MetaOapg.properties.quoteAssetPrecision, decimal.Decimal, int, ],
        quoteAssetId: typing.Union[MetaOapg.properties.quoteAssetId, str, uuid.UUID, ],
        baseAssetPrecision: typing.Union[MetaOapg.properties.baseAssetPrecision, decimal.Decimal, int, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'CreateOrderbookModel':
        return super().__new__(
            cls,
            *_args,
            baseAssetId=baseAssetId,
            quoteAssetPrecision=quoteAssetPrecision,
            quoteAssetId=quoteAssetId,
            baseAssetPrecision=baseAssetPrecision,
            _configuration=_configuration,
        )