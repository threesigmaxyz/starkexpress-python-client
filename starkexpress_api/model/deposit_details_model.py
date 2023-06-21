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


class DepositDetailsModel(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "amount",
            "assetId",
            "userId",
            "dataAvailabilityMode",
        }
        
        class properties:
            userId = schemas.UUIDSchema
            assetId = schemas.UUIDSchema
        
            @staticmethod
            def dataAvailabilityMode() -> typing.Type['DataAvailabilityModes']:
                return DataAvailabilityModes
            amount = schemas.StrSchema
            
            
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
            __annotations__ = {
                "userId": userId,
                "assetId": assetId,
                "dataAvailabilityMode": dataAvailabilityMode,
                "amount": amount,
                "tokenId": tokenId,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    amount: MetaOapg.properties.amount
    assetId: MetaOapg.properties.assetId
    userId: MetaOapg.properties.userId
    dataAvailabilityMode: 'DataAvailabilityModes'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["assetId"]) -> MetaOapg.properties.assetId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["userId"]) -> MetaOapg.properties.userId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dataAvailabilityMode"]) -> 'DataAvailabilityModes': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tokenId"]) -> MetaOapg.properties.tokenId: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["amount"], typing_extensions.Literal["assetId"], typing_extensions.Literal["userId"], typing_extensions.Literal["dataAvailabilityMode"], typing_extensions.Literal["tokenId"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["assetId"]) -> MetaOapg.properties.assetId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["userId"]) -> MetaOapg.properties.userId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dataAvailabilityMode"]) -> 'DataAvailabilityModes': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tokenId"]) -> typing.Union[MetaOapg.properties.tokenId, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["amount"], typing_extensions.Literal["assetId"], typing_extensions.Literal["userId"], typing_extensions.Literal["dataAvailabilityMode"], typing_extensions.Literal["tokenId"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        amount: typing.Union[MetaOapg.properties.amount, str, ],
        assetId: typing.Union[MetaOapg.properties.assetId, str, uuid.UUID, ],
        userId: typing.Union[MetaOapg.properties.userId, str, uuid.UUID, ],
        dataAvailabilityMode: 'DataAvailabilityModes',
        tokenId: typing.Union[MetaOapg.properties.tokenId, None, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'DepositDetailsModel':
        return super().__new__(
            cls,
            *_args,
            amount=amount,
            assetId=assetId,
            userId=userId,
            dataAvailabilityMode=dataAvailabilityMode,
            tokenId=tokenId,
            _configuration=_configuration,
        )

from starkexpress_api.model.data_availability_modes import DataAvailabilityModes
