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


class DepositDetailsDto(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            
            
            class operatorContractAddress(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'hex'
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'operatorContractAddress':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class assetContractAddress(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'hex'
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'assetContractAddress':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class depositFunction(
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
                ) -> 'depositFunction':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class starkKey(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'hex'
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'starkKey':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class assetType(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'hex'
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'assetType':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class tokenId(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'hex'
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'tokenId':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            vaultId = schemas.StrSchema
            
            
            class quantizedAmount(
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
                ) -> 'quantizedAmount':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class amount(
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
                ) -> 'amount':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "operatorContractAddress": operatorContractAddress,
                "assetContractAddress": assetContractAddress,
                "depositFunction": depositFunction,
                "starkKey": starkKey,
                "assetType": assetType,
                "tokenId": tokenId,
                "vaultId": vaultId,
                "quantizedAmount": quantizedAmount,
                "amount": amount,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["operatorContractAddress"]) -> MetaOapg.properties.operatorContractAddress: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["assetContractAddress"]) -> MetaOapg.properties.assetContractAddress: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["depositFunction"]) -> MetaOapg.properties.depositFunction: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["starkKey"]) -> MetaOapg.properties.starkKey: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["assetType"]) -> MetaOapg.properties.assetType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tokenId"]) -> MetaOapg.properties.tokenId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["vaultId"]) -> MetaOapg.properties.vaultId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["quantizedAmount"]) -> MetaOapg.properties.quantizedAmount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["operatorContractAddress"], typing_extensions.Literal["assetContractAddress"], typing_extensions.Literal["depositFunction"], typing_extensions.Literal["starkKey"], typing_extensions.Literal["assetType"], typing_extensions.Literal["tokenId"], typing_extensions.Literal["vaultId"], typing_extensions.Literal["quantizedAmount"], typing_extensions.Literal["amount"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["operatorContractAddress"]) -> typing.Union[MetaOapg.properties.operatorContractAddress, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["assetContractAddress"]) -> typing.Union[MetaOapg.properties.assetContractAddress, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["depositFunction"]) -> typing.Union[MetaOapg.properties.depositFunction, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["starkKey"]) -> typing.Union[MetaOapg.properties.starkKey, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["assetType"]) -> typing.Union[MetaOapg.properties.assetType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tokenId"]) -> typing.Union[MetaOapg.properties.tokenId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["vaultId"]) -> typing.Union[MetaOapg.properties.vaultId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["quantizedAmount"]) -> typing.Union[MetaOapg.properties.quantizedAmount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amount"]) -> typing.Union[MetaOapg.properties.amount, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["operatorContractAddress"], typing_extensions.Literal["assetContractAddress"], typing_extensions.Literal["depositFunction"], typing_extensions.Literal["starkKey"], typing_extensions.Literal["assetType"], typing_extensions.Literal["tokenId"], typing_extensions.Literal["vaultId"], typing_extensions.Literal["quantizedAmount"], typing_extensions.Literal["amount"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        operatorContractAddress: typing.Union[MetaOapg.properties.operatorContractAddress, None, str, schemas.Unset] = schemas.unset,
        assetContractAddress: typing.Union[MetaOapg.properties.assetContractAddress, None, str, schemas.Unset] = schemas.unset,
        depositFunction: typing.Union[MetaOapg.properties.depositFunction, None, str, schemas.Unset] = schemas.unset,
        starkKey: typing.Union[MetaOapg.properties.starkKey, None, str, schemas.Unset] = schemas.unset,
        assetType: typing.Union[MetaOapg.properties.assetType, None, str, schemas.Unset] = schemas.unset,
        tokenId: typing.Union[MetaOapg.properties.tokenId, None, str, schemas.Unset] = schemas.unset,
        vaultId: typing.Union[MetaOapg.properties.vaultId, str, schemas.Unset] = schemas.unset,
        quantizedAmount: typing.Union[MetaOapg.properties.quantizedAmount, None, str, schemas.Unset] = schemas.unset,
        amount: typing.Union[MetaOapg.properties.amount, None, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'DepositDetailsDto':
        return super().__new__(
            cls,
            *_args,
            operatorContractAddress=operatorContractAddress,
            assetContractAddress=assetContractAddress,
            depositFunction=depositFunction,
            starkKey=starkKey,
            assetType=assetType,
            tokenId=tokenId,
            vaultId=vaultId,
            quantizedAmount=quantizedAmount,
            amount=amount,
            _configuration=_configuration,
        )