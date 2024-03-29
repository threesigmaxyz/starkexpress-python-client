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


class OrderbookAssetDto(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            assetId = schemas.UUIDSchema
            precision = schemas.Int32Schema
            __annotations__ = {
                "assetId": assetId,
                "precision": precision,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["assetId"]) -> MetaOapg.properties.assetId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["precision"]) -> MetaOapg.properties.precision: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["assetId"], typing_extensions.Literal["precision"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["assetId"]) -> typing.Union[MetaOapg.properties.assetId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["precision"]) -> typing.Union[MetaOapg.properties.precision, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["assetId"], typing_extensions.Literal["precision"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        assetId: typing.Union[MetaOapg.properties.assetId, str, uuid.UUID, schemas.Unset] = schemas.unset,
        precision: typing.Union[MetaOapg.properties.precision, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'OrderbookAssetDto':
        return super().__new__(
            cls,
            *_args,
            assetId=assetId,
            precision=precision,
            _configuration=_configuration,
        )
