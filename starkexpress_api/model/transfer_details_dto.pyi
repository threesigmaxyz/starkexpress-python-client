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


class TransferDetailsDto(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            
            
            class senderStarkKey(
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
                ) -> 'senderStarkKey':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            senderVaultChainId = schemas.StrSchema
            senderVaultId = schemas.UUIDSchema
            
            
            class receiverStarkKey(
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
                ) -> 'receiverStarkKey':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            receiverVaultChainId = schemas.StrSchema
            receiverVaultId = schemas.UUIDSchema
            
            
            class assetId(
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
                ) -> 'assetId':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            quantizedAmount = schemas.StrSchema
            feeVaultChainId = schemas.StrSchema
            feeVaultId = schemas.UUIDSchema
            feeQuantizedAmount = schemas.StrSchema
            
            
            class feeAssetId(
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
                ) -> 'feeAssetId':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            expirationTimestamp = schemas.Int64Schema
            nonce = schemas.Int32Schema
            
            
            class signablePayload(
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
                ) -> 'signablePayload':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "senderStarkKey": senderStarkKey,
                "senderVaultChainId": senderVaultChainId,
                "senderVaultId": senderVaultId,
                "receiverStarkKey": receiverStarkKey,
                "receiverVaultChainId": receiverVaultChainId,
                "receiverVaultId": receiverVaultId,
                "assetId": assetId,
                "quantizedAmount": quantizedAmount,
                "feeVaultChainId": feeVaultChainId,
                "feeVaultId": feeVaultId,
                "feeQuantizedAmount": feeQuantizedAmount,
                "feeAssetId": feeAssetId,
                "expirationTimestamp": expirationTimestamp,
                "nonce": nonce,
                "signablePayload": signablePayload,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["senderStarkKey"]) -> MetaOapg.properties.senderStarkKey: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["senderVaultChainId"]) -> MetaOapg.properties.senderVaultChainId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["senderVaultId"]) -> MetaOapg.properties.senderVaultId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["receiverStarkKey"]) -> MetaOapg.properties.receiverStarkKey: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["receiverVaultChainId"]) -> MetaOapg.properties.receiverVaultChainId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["receiverVaultId"]) -> MetaOapg.properties.receiverVaultId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["assetId"]) -> MetaOapg.properties.assetId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["quantizedAmount"]) -> MetaOapg.properties.quantizedAmount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["feeVaultChainId"]) -> MetaOapg.properties.feeVaultChainId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["feeVaultId"]) -> MetaOapg.properties.feeVaultId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["feeQuantizedAmount"]) -> MetaOapg.properties.feeQuantizedAmount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["feeAssetId"]) -> MetaOapg.properties.feeAssetId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expirationTimestamp"]) -> MetaOapg.properties.expirationTimestamp: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nonce"]) -> MetaOapg.properties.nonce: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["signablePayload"]) -> MetaOapg.properties.signablePayload: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["senderStarkKey"], typing_extensions.Literal["senderVaultChainId"], typing_extensions.Literal["senderVaultId"], typing_extensions.Literal["receiverStarkKey"], typing_extensions.Literal["receiverVaultChainId"], typing_extensions.Literal["receiverVaultId"], typing_extensions.Literal["assetId"], typing_extensions.Literal["quantizedAmount"], typing_extensions.Literal["feeVaultChainId"], typing_extensions.Literal["feeVaultId"], typing_extensions.Literal["feeQuantizedAmount"], typing_extensions.Literal["feeAssetId"], typing_extensions.Literal["expirationTimestamp"], typing_extensions.Literal["nonce"], typing_extensions.Literal["signablePayload"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["senderStarkKey"]) -> typing.Union[MetaOapg.properties.senderStarkKey, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["senderVaultChainId"]) -> typing.Union[MetaOapg.properties.senderVaultChainId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["senderVaultId"]) -> typing.Union[MetaOapg.properties.senderVaultId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["receiverStarkKey"]) -> typing.Union[MetaOapg.properties.receiverStarkKey, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["receiverVaultChainId"]) -> typing.Union[MetaOapg.properties.receiverVaultChainId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["receiverVaultId"]) -> typing.Union[MetaOapg.properties.receiverVaultId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["assetId"]) -> typing.Union[MetaOapg.properties.assetId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["quantizedAmount"]) -> typing.Union[MetaOapg.properties.quantizedAmount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["feeVaultChainId"]) -> typing.Union[MetaOapg.properties.feeVaultChainId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["feeVaultId"]) -> typing.Union[MetaOapg.properties.feeVaultId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["feeQuantizedAmount"]) -> typing.Union[MetaOapg.properties.feeQuantizedAmount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["feeAssetId"]) -> typing.Union[MetaOapg.properties.feeAssetId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expirationTimestamp"]) -> typing.Union[MetaOapg.properties.expirationTimestamp, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nonce"]) -> typing.Union[MetaOapg.properties.nonce, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["signablePayload"]) -> typing.Union[MetaOapg.properties.signablePayload, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["senderStarkKey"], typing_extensions.Literal["senderVaultChainId"], typing_extensions.Literal["senderVaultId"], typing_extensions.Literal["receiverStarkKey"], typing_extensions.Literal["receiverVaultChainId"], typing_extensions.Literal["receiverVaultId"], typing_extensions.Literal["assetId"], typing_extensions.Literal["quantizedAmount"], typing_extensions.Literal["feeVaultChainId"], typing_extensions.Literal["feeVaultId"], typing_extensions.Literal["feeQuantizedAmount"], typing_extensions.Literal["feeAssetId"], typing_extensions.Literal["expirationTimestamp"], typing_extensions.Literal["nonce"], typing_extensions.Literal["signablePayload"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        senderStarkKey: typing.Union[MetaOapg.properties.senderStarkKey, None, str, schemas.Unset] = schemas.unset,
        senderVaultChainId: typing.Union[MetaOapg.properties.senderVaultChainId, str, schemas.Unset] = schemas.unset,
        senderVaultId: typing.Union[MetaOapg.properties.senderVaultId, str, uuid.UUID, schemas.Unset] = schemas.unset,
        receiverStarkKey: typing.Union[MetaOapg.properties.receiverStarkKey, None, str, schemas.Unset] = schemas.unset,
        receiverVaultChainId: typing.Union[MetaOapg.properties.receiverVaultChainId, str, schemas.Unset] = schemas.unset,
        receiverVaultId: typing.Union[MetaOapg.properties.receiverVaultId, str, uuid.UUID, schemas.Unset] = schemas.unset,
        assetId: typing.Union[MetaOapg.properties.assetId, None, str, schemas.Unset] = schemas.unset,
        quantizedAmount: typing.Union[MetaOapg.properties.quantizedAmount, str, schemas.Unset] = schemas.unset,
        feeVaultChainId: typing.Union[MetaOapg.properties.feeVaultChainId, str, schemas.Unset] = schemas.unset,
        feeVaultId: typing.Union[MetaOapg.properties.feeVaultId, str, uuid.UUID, schemas.Unset] = schemas.unset,
        feeQuantizedAmount: typing.Union[MetaOapg.properties.feeQuantizedAmount, str, schemas.Unset] = schemas.unset,
        feeAssetId: typing.Union[MetaOapg.properties.feeAssetId, None, str, schemas.Unset] = schemas.unset,
        expirationTimestamp: typing.Union[MetaOapg.properties.expirationTimestamp, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        nonce: typing.Union[MetaOapg.properties.nonce, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        signablePayload: typing.Union[MetaOapg.properties.signablePayload, None, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'TransferDetailsDto':
        return super().__new__(
            cls,
            *_args,
            senderStarkKey=senderStarkKey,
            senderVaultChainId=senderVaultChainId,
            senderVaultId=senderVaultId,
            receiverStarkKey=receiverStarkKey,
            receiverVaultChainId=receiverVaultChainId,
            receiverVaultId=receiverVaultId,
            assetId=assetId,
            quantizedAmount=quantizedAmount,
            feeVaultChainId=feeVaultChainId,
            feeVaultId=feeVaultId,
            feeQuantizedAmount=feeQuantizedAmount,
            feeAssetId=feeAssetId,
            expirationTimestamp=expirationTimestamp,
            nonce=nonce,
            signablePayload=signablePayload,
            _configuration=_configuration,
        )
