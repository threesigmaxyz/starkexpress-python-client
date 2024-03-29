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


class BigInteger(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            bitCount = schemas.Int32Schema
            bitLength = schemas.Int32Schema
            intValue = schemas.Int32Schema
            intValueExact = schemas.Int32Schema
            longValue = schemas.Int64Schema
            longValueExact = schemas.Int64Schema
            signValue = schemas.Int32Schema
            __annotations__ = {
                "bitCount": bitCount,
                "bitLength": bitLength,
                "intValue": intValue,
                "intValueExact": intValueExact,
                "longValue": longValue,
                "longValueExact": longValueExact,
                "signValue": signValue,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bitCount"]) -> MetaOapg.properties.bitCount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bitLength"]) -> MetaOapg.properties.bitLength: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["intValue"]) -> MetaOapg.properties.intValue: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["intValueExact"]) -> MetaOapg.properties.intValueExact: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["longValue"]) -> MetaOapg.properties.longValue: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["longValueExact"]) -> MetaOapg.properties.longValueExact: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["signValue"]) -> MetaOapg.properties.signValue: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["bitCount"], typing_extensions.Literal["bitLength"], typing_extensions.Literal["intValue"], typing_extensions.Literal["intValueExact"], typing_extensions.Literal["longValue"], typing_extensions.Literal["longValueExact"], typing_extensions.Literal["signValue"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bitCount"]) -> typing.Union[MetaOapg.properties.bitCount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bitLength"]) -> typing.Union[MetaOapg.properties.bitLength, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["intValue"]) -> typing.Union[MetaOapg.properties.intValue, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["intValueExact"]) -> typing.Union[MetaOapg.properties.intValueExact, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["longValue"]) -> typing.Union[MetaOapg.properties.longValue, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["longValueExact"]) -> typing.Union[MetaOapg.properties.longValueExact, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["signValue"]) -> typing.Union[MetaOapg.properties.signValue, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["bitCount"], typing_extensions.Literal["bitLength"], typing_extensions.Literal["intValue"], typing_extensions.Literal["intValueExact"], typing_extensions.Literal["longValue"], typing_extensions.Literal["longValueExact"], typing_extensions.Literal["signValue"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        bitCount: typing.Union[MetaOapg.properties.bitCount, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        bitLength: typing.Union[MetaOapg.properties.bitLength, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        intValue: typing.Union[MetaOapg.properties.intValue, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        intValueExact: typing.Union[MetaOapg.properties.intValueExact, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        longValue: typing.Union[MetaOapg.properties.longValue, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        longValueExact: typing.Union[MetaOapg.properties.longValueExact, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        signValue: typing.Union[MetaOapg.properties.signValue, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'BigInteger':
        return super().__new__(
            cls,
            *_args,
            bitCount=bitCount,
            bitLength=bitLength,
            intValue=intValue,
            intValueExact=intValueExact,
            longValue=longValue,
            longValueExact=longValueExact,
            signValue=signValue,
            _configuration=_configuration,
        )
