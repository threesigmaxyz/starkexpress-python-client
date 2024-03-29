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


class AssetType(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    
    @schemas.classproperty
    def ETH(cls):
        return cls("Eth")
    
    @schemas.classproperty
    def ERC20(cls):
        return cls("Erc20")
    
    @schemas.classproperty
    def ERC721(cls):
        return cls("Erc721")
    
    @schemas.classproperty
    def ERC1155(cls):
        return cls("Erc1155")
    
    @schemas.classproperty
    def MINTABLE_ERC20(cls):
        return cls("MintableErc20")
    
    @schemas.classproperty
    def MINTABLE_ERC721(cls):
        return cls("MintableErc721")
