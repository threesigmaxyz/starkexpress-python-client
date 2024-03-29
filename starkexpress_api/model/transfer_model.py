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


class TransferModel(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Request model to transfer assets between users.
    """


    class MetaOapg:
        required = {
            "signature",
            "senderVaultId",
            "quantizedAmount",
            "receiverVaultId",
            "expirationTimestamp",
            "nonce",
        }
        
        class properties:
            senderVaultId = schemas.UUIDSchema
            receiverVaultId = schemas.UUIDSchema
            quantizedAmount = schemas.StrSchema
            expirationTimestamp = schemas.Int64Schema
            
            
            class nonce(
                schemas.Int32Schema
            ):
            
            
                class MetaOapg:
                    format = 'int32'
                    inclusive_maximum = 2147483647
                    inclusive_minimum = 0
        
            @staticmethod
            def signature() -> typing.Type['SignatureModel']:
                return SignatureModel
            __annotations__ = {
                "senderVaultId": senderVaultId,
                "receiverVaultId": receiverVaultId,
                "quantizedAmount": quantizedAmount,
                "expirationTimestamp": expirationTimestamp,
                "nonce": nonce,
                "signature": signature,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    signature: 'SignatureModel'
    senderVaultId: MetaOapg.properties.senderVaultId
    quantizedAmount: MetaOapg.properties.quantizedAmount
    receiverVaultId: MetaOapg.properties.receiverVaultId
    expirationTimestamp: MetaOapg.properties.expirationTimestamp
    nonce: MetaOapg.properties.nonce
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["signature"]) -> 'SignatureModel': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["senderVaultId"]) -> MetaOapg.properties.senderVaultId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["quantizedAmount"]) -> MetaOapg.properties.quantizedAmount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["receiverVaultId"]) -> MetaOapg.properties.receiverVaultId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expirationTimestamp"]) -> MetaOapg.properties.expirationTimestamp: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nonce"]) -> MetaOapg.properties.nonce: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["signature"], typing_extensions.Literal["senderVaultId"], typing_extensions.Literal["quantizedAmount"], typing_extensions.Literal["receiverVaultId"], typing_extensions.Literal["expirationTimestamp"], typing_extensions.Literal["nonce"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["signature"]) -> 'SignatureModel': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["senderVaultId"]) -> MetaOapg.properties.senderVaultId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["quantizedAmount"]) -> MetaOapg.properties.quantizedAmount: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["receiverVaultId"]) -> MetaOapg.properties.receiverVaultId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expirationTimestamp"]) -> MetaOapg.properties.expirationTimestamp: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nonce"]) -> MetaOapg.properties.nonce: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["signature"], typing_extensions.Literal["senderVaultId"], typing_extensions.Literal["quantizedAmount"], typing_extensions.Literal["receiverVaultId"], typing_extensions.Literal["expirationTimestamp"], typing_extensions.Literal["nonce"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        signature: 'SignatureModel',
        senderVaultId: typing.Union[MetaOapg.properties.senderVaultId, str, uuid.UUID, ],
        quantizedAmount: typing.Union[MetaOapg.properties.quantizedAmount, str, ],
        receiverVaultId: typing.Union[MetaOapg.properties.receiverVaultId, str, uuid.UUID, ],
        expirationTimestamp: typing.Union[MetaOapg.properties.expirationTimestamp, decimal.Decimal, int, ],
        nonce: typing.Union[MetaOapg.properties.nonce, decimal.Decimal, int, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'TransferModel':
        return super().__new__(
            cls,
            *_args,
            signature=signature,
            senderVaultId=senderVaultId,
            quantizedAmount=quantizedAmount,
            receiverVaultId=receiverVaultId,
            expirationTimestamp=expirationTimestamp,
            nonce=nonce,
            _configuration=_configuration,
        )

from starkexpress_api.model.signature_model import SignatureModel
