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


class MintDataModel(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Model containing information to mint an asset.
    """


    class MetaOapg:
        required = {
            "amount",
            "mintingBlob",
            "assetId",
            "dataAvailabilityMode",
        }
        
        class properties:
            
            
            class mintingBlob(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    format = 'hex'
                    min_length = 1
            assetId = schemas.UUIDSchema
            amount = schemas.StrSchema
        
            @staticmethod
            def dataAvailabilityMode() -> typing.Type['DataAvailabilityModes']:
                return DataAvailabilityModes
            __annotations__ = {
                "mintingBlob": mintingBlob,
                "assetId": assetId,
                "amount": amount,
                "dataAvailabilityMode": dataAvailabilityMode,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    amount: MetaOapg.properties.amount
    mintingBlob: MetaOapg.properties.mintingBlob
    assetId: MetaOapg.properties.assetId
    dataAvailabilityMode: 'DataAvailabilityModes'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mintingBlob"]) -> MetaOapg.properties.mintingBlob: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["assetId"]) -> MetaOapg.properties.assetId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dataAvailabilityMode"]) -> 'DataAvailabilityModes': ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["amount"], typing_extensions.Literal["mintingBlob"], typing_extensions.Literal["assetId"], typing_extensions.Literal["dataAvailabilityMode"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mintingBlob"]) -> MetaOapg.properties.mintingBlob: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["assetId"]) -> MetaOapg.properties.assetId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dataAvailabilityMode"]) -> 'DataAvailabilityModes': ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["amount"], typing_extensions.Literal["mintingBlob"], typing_extensions.Literal["assetId"], typing_extensions.Literal["dataAvailabilityMode"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        amount: typing.Union[MetaOapg.properties.amount, str, ],
        mintingBlob: typing.Union[MetaOapg.properties.mintingBlob, str, ],
        assetId: typing.Union[MetaOapg.properties.assetId, str, uuid.UUID, ],
        dataAvailabilityMode: 'DataAvailabilityModes',
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'MintDataModel':
        return super().__new__(
            cls,
            *_args,
            amount=amount,
            mintingBlob=mintingBlob,
            assetId=assetId,
            dataAvailabilityMode=dataAvailabilityMode,
            _configuration=_configuration,
        )

from starkexpress_api.model.data_availability_modes import DataAvailabilityModes