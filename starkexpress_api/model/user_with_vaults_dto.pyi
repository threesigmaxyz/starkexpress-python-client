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


class UserWithVaultsDto(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def user() -> typing.Type['UserDto']:
                return UserDto
            
            
            class vaultsPerAsset(
                schemas.DictBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneFrozenDictMixin
            ):
            
            
                class MetaOapg:
                    
                    
                    class additional_properties(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            @staticmethod
                            def items() -> typing.Type['VaultDto']:
                                return VaultDto
                    
                        def __new__(
                            cls,
                            _arg: typing.Union[typing.Tuple['VaultDto'], typing.List['VaultDto']],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'additional_properties':
                            return super().__new__(
                                cls,
                                _arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> 'VaultDto':
                            return super().__getitem__(i)
            
                
                def __getitem__(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                def get_item_oapg(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    return super().get_item_oapg(name)
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, None, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[MetaOapg.additional_properties, list, tuple, ],
                ) -> 'vaultsPerAsset':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "user": user,
                "vaultsPerAsset": vaultsPerAsset,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user"]) -> 'UserDto': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["vaultsPerAsset"]) -> MetaOapg.properties.vaultsPerAsset: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["user"], typing_extensions.Literal["vaultsPerAsset"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user"]) -> typing.Union['UserDto', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["vaultsPerAsset"]) -> typing.Union[MetaOapg.properties.vaultsPerAsset, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["user"], typing_extensions.Literal["vaultsPerAsset"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        user: typing.Union['UserDto', schemas.Unset] = schemas.unset,
        vaultsPerAsset: typing.Union[MetaOapg.properties.vaultsPerAsset, dict, frozendict.frozendict, None, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'UserWithVaultsDto':
        return super().__new__(
            cls,
            *_args,
            user=user,
            vaultsPerAsset=vaultsPerAsset,
            _configuration=_configuration,
        )

from starkexpress_api.model.user_dto import UserDto
from starkexpress_api.model.vault_dto import VaultDto
