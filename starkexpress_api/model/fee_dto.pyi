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


class FeeDto(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            vaultId = schemas.UUIDSchema
        
            @staticmethod
            def vaultChainId() -> typing.Type['BigInteger']:
                return BigInteger
            
            
            class assetId(
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
                ) -> 'assetId':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def quantizedAmount() -> typing.Type['BigInteger']:
                return BigInteger
            __annotations__ = {
                "vaultId": vaultId,
                "vaultChainId": vaultChainId,
                "assetId": assetId,
                "quantizedAmount": quantizedAmount,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["vaultId"]) -> MetaOapg.properties.vaultId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["vaultChainId"]) -> 'BigInteger': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["assetId"]) -> MetaOapg.properties.assetId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["quantizedAmount"]) -> 'BigInteger': ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["vaultId"], typing_extensions.Literal["vaultChainId"], typing_extensions.Literal["assetId"], typing_extensions.Literal["quantizedAmount"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["vaultId"]) -> typing.Union[MetaOapg.properties.vaultId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["vaultChainId"]) -> typing.Union['BigInteger', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["assetId"]) -> typing.Union[MetaOapg.properties.assetId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["quantizedAmount"]) -> typing.Union['BigInteger', schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["vaultId"], typing_extensions.Literal["vaultChainId"], typing_extensions.Literal["assetId"], typing_extensions.Literal["quantizedAmount"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        vaultId: typing.Union[MetaOapg.properties.vaultId, str, uuid.UUID, schemas.Unset] = schemas.unset,
        vaultChainId: typing.Union['BigInteger', schemas.Unset] = schemas.unset,
        assetId: typing.Union[MetaOapg.properties.assetId, None, str, schemas.Unset] = schemas.unset,
        quantizedAmount: typing.Union['BigInteger', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'FeeDto':
        return super().__new__(
            cls,
            *_args,
            vaultId=vaultId,
            vaultChainId=vaultChainId,
            assetId=assetId,
            quantizedAmount=quantizedAmount,
            _configuration=_configuration,
        )

from starkexpress_api.model.big_integer import BigInteger
