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


class SubmitOrderModel(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Request model to submit an orderbook order.
    """


    class MetaOapg:
        required = {
            "amount",
            "side",
            "orderbookId",
            "signature",
            "price",
            "sellDataAvailabilityMode",
            "expirationTimestamp",
            "buyDataAvailabilityMode",
            "nonce",
            "userId",
        }
        
        class properties:
            orderbookId = schemas.UUIDSchema
            userId = schemas.UUIDSchema
        
            @staticmethod
            def side() -> typing.Type['OrderSide']:
                return OrderSide
            price = schemas.Float64Schema
            amount = schemas.StrSchema
        
            @staticmethod
            def sellDataAvailabilityMode() -> typing.Type['DataAvailabilityModes']:
                return DataAvailabilityModes
        
            @staticmethod
            def buyDataAvailabilityMode() -> typing.Type['DataAvailabilityModes']:
                return DataAvailabilityModes
            expirationTimestamp = schemas.Int64Schema
            
            
            class nonce(
                schemas.Int32Schema
            ):
                pass
        
            @staticmethod
            def signature() -> typing.Type['SignatureModel']:
                return SignatureModel
            __annotations__ = {
                "orderbookId": orderbookId,
                "userId": userId,
                "side": side,
                "price": price,
                "amount": amount,
                "sellDataAvailabilityMode": sellDataAvailabilityMode,
                "buyDataAvailabilityMode": buyDataAvailabilityMode,
                "expirationTimestamp": expirationTimestamp,
                "nonce": nonce,
                "signature": signature,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    amount: MetaOapg.properties.amount
    side: 'OrderSide'
    orderbookId: MetaOapg.properties.orderbookId
    signature: 'SignatureModel'
    price: MetaOapg.properties.price
    sellDataAvailabilityMode: 'DataAvailabilityModes'
    expirationTimestamp: MetaOapg.properties.expirationTimestamp
    buyDataAvailabilityMode: 'DataAvailabilityModes'
    nonce: MetaOapg.properties.nonce
    userId: MetaOapg.properties.userId
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["side"]) -> 'OrderSide': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["orderbookId"]) -> MetaOapg.properties.orderbookId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["signature"]) -> 'SignatureModel': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["price"]) -> MetaOapg.properties.price: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sellDataAvailabilityMode"]) -> 'DataAvailabilityModes': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expirationTimestamp"]) -> MetaOapg.properties.expirationTimestamp: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["buyDataAvailabilityMode"]) -> 'DataAvailabilityModes': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nonce"]) -> MetaOapg.properties.nonce: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["userId"]) -> MetaOapg.properties.userId: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["amount"], typing_extensions.Literal["side"], typing_extensions.Literal["orderbookId"], typing_extensions.Literal["signature"], typing_extensions.Literal["price"], typing_extensions.Literal["sellDataAvailabilityMode"], typing_extensions.Literal["expirationTimestamp"], typing_extensions.Literal["buyDataAvailabilityMode"], typing_extensions.Literal["nonce"], typing_extensions.Literal["userId"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["side"]) -> 'OrderSide': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["orderbookId"]) -> MetaOapg.properties.orderbookId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["signature"]) -> 'SignatureModel': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["price"]) -> MetaOapg.properties.price: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sellDataAvailabilityMode"]) -> 'DataAvailabilityModes': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expirationTimestamp"]) -> MetaOapg.properties.expirationTimestamp: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["buyDataAvailabilityMode"]) -> 'DataAvailabilityModes': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nonce"]) -> MetaOapg.properties.nonce: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["userId"]) -> MetaOapg.properties.userId: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["amount"], typing_extensions.Literal["side"], typing_extensions.Literal["orderbookId"], typing_extensions.Literal["signature"], typing_extensions.Literal["price"], typing_extensions.Literal["sellDataAvailabilityMode"], typing_extensions.Literal["expirationTimestamp"], typing_extensions.Literal["buyDataAvailabilityMode"], typing_extensions.Literal["nonce"], typing_extensions.Literal["userId"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        amount: typing.Union[MetaOapg.properties.amount, str, ],
        side: 'OrderSide',
        orderbookId: typing.Union[MetaOapg.properties.orderbookId, str, uuid.UUID, ],
        signature: 'SignatureModel',
        price: typing.Union[MetaOapg.properties.price, decimal.Decimal, int, float, ],
        sellDataAvailabilityMode: 'DataAvailabilityModes',
        expirationTimestamp: typing.Union[MetaOapg.properties.expirationTimestamp, decimal.Decimal, int, ],
        buyDataAvailabilityMode: 'DataAvailabilityModes',
        nonce: typing.Union[MetaOapg.properties.nonce, decimal.Decimal, int, ],
        userId: typing.Union[MetaOapg.properties.userId, str, uuid.UUID, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'SubmitOrderModel':
        return super().__new__(
            cls,
            *_args,
            amount=amount,
            side=side,
            orderbookId=orderbookId,
            signature=signature,
            price=price,
            sellDataAvailabilityMode=sellDataAvailabilityMode,
            expirationTimestamp=expirationTimestamp,
            buyDataAvailabilityMode=buyDataAvailabilityMode,
            nonce=nonce,
            userId=userId,
            _configuration=_configuration,
        )

from starkexpress_api.model.data_availability_modes import DataAvailabilityModes
from starkexpress_api.model.order_side import OrderSide
from starkexpress_api.model.signature_model import SignatureModel
