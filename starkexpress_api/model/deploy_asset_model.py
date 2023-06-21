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


class DeployAssetModel(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "symbol",
            "name",
            "type",
        }
        
        class properties:
        
            @staticmethod
            def type() -> typing.Type['AssetType']:
                return AssetType
            
            
            class name(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    format = 'string'
                    min_length = 1
            
            
            class symbol(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    format = 'string'
                    min_length = 1
            
            
            class uri(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'string'
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'uri':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            quantum = schemas.StrSchema
            __annotations__ = {
                "type": type,
                "name": name,
                "symbol": symbol,
                "uri": uri,
                "quantum": quantum,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    symbol: MetaOapg.properties.symbol
    name: MetaOapg.properties.name
    type: 'AssetType'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["symbol"]) -> MetaOapg.properties.symbol: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> 'AssetType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["uri"]) -> MetaOapg.properties.uri: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["quantum"]) -> MetaOapg.properties.quantum: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["symbol"], typing_extensions.Literal["name"], typing_extensions.Literal["type"], typing_extensions.Literal["uri"], typing_extensions.Literal["quantum"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["symbol"]) -> MetaOapg.properties.symbol: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> 'AssetType': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["uri"]) -> typing.Union[MetaOapg.properties.uri, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["quantum"]) -> typing.Union[MetaOapg.properties.quantum, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["symbol"], typing_extensions.Literal["name"], typing_extensions.Literal["type"], typing_extensions.Literal["uri"], typing_extensions.Literal["quantum"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        symbol: typing.Union[MetaOapg.properties.symbol, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        type: 'AssetType',
        uri: typing.Union[MetaOapg.properties.uri, None, str, schemas.Unset] = schemas.unset,
        quantum: typing.Union[MetaOapg.properties.quantum, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'DeployAssetModel':
        return super().__new__(
            cls,
            *_args,
            symbol=symbol,
            name=name,
            type=type,
            uri=uri,
            quantum=quantum,
            _configuration=_configuration,
        )

from starkexpress_api.model.asset_type import AssetType
