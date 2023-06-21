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


class StarkExOperation(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    
    @schemas.classproperty
    def DEPOSIT(cls):
        return cls("Deposit")
    
    @schemas.classproperty
    def WITHDRAWAL(cls):
        return cls("Withdrawal")
    
    @schemas.classproperty
    def MINT(cls):
        return cls("Mint")
    
    @schemas.classproperty
    def MULTI_TRANSACTION(cls):
        return cls("MultiTransaction")
    
    @schemas.classproperty
    def TRANSFER(cls):
        return cls("Transfer")
    
    @schemas.classproperty
    def FULL_WITHDRAWAL(cls):
        return cls("FullWithdrawal")
    
    @schemas.classproperty
    def FALSE_FULL_WITHDRAWAL(cls):
        return cls("FalseFullWithdrawal")
    
    @schemas.classproperty
    def SETTLEMENT(cls):
        return cls("Settlement")
