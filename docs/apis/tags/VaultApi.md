<a name="__pageTop"></a>
# starkexpress_api.apis.tags.vault_api.VaultApi

All URIs are relative to *https://testnet-api.starkexpress.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_vaults**](#get_all_vaults) | **get** /api/v1/vaults | Get All Vaults
[**get_vault**](#get_vault) | **get** /api/v1/vaults/{vaultId} | Get a single Vault

# **get_all_vaults**
<a name="get_all_vaults"></a>
> VaultDtoPaginatedResponseDto get_all_vaults(page_numberpage_size)

Get All Vaults

This endpoint fetches all vaults in the system, with support for filters and pagination.

### Example

* OAuth Authentication (oauth2):
```python
import starkexpress_api
from starkexpress_api.apis.tags import vault_api
from starkexpress_api.model.vault_dto_paginated_response_dto import VaultDtoPaginatedResponseDto
from pprint import pprint
# Defining the host is optional and defaults to https://testnet-api.starkexpress.io
# See configuration.py for a list of all supported configuration parameters.
configuration = starkexpress_api.Configuration(
    host = "https://testnet-api.starkexpress.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = starkexpress_api.Configuration(
    host = "https://testnet-api.starkexpress.io",
    access_token = 'YOUR_ACCESS_TOKEN'
)
# Enter a context with an instance of the API client
with starkexpress_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vault_api.VaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'page_number': 1,
        'page_size': 1,
    }
    try:
        # Get All Vaults
        api_response = api_instance.get_all_vaults(
            query_params=query_params,
        )
        pprint(api_response)
    except starkexpress_api.ApiException as e:
        print("Exception when calling VaultApi->get_all_vaults: %s\n" % e)

    # example passing only optional values
    query_params = {
        'tenant_id': "tenant_id_example",
        'asset_id': "asset_id_example",
        'page_number': 1,
        'page_size': 1,
        'sort_by': "sort_by_example",
    }
    try:
        # Get All Vaults
        api_response = api_instance.get_all_vaults(
            query_params=query_params,
        )
        pprint(api_response)
    except starkexpress_api.ApiException as e:
        print("Exception when calling VaultApi->get_all_vaults: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
tenant_id | TenantIdSchema | | optional
asset_id | AssetIdSchema | | optional
page_number | PageNumberSchema | | 
page_size | PageSizeSchema | | 
sort_by | SortBySchema | | optional


# TenantIdSchema

The unique identifier of the tenant.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  | The unique identifier of the tenant. | value must be a uuid

# AssetIdSchema

The unique identifier of the asset.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  | The unique identifier of the asset. | value must be a uuid

# PageNumberSchema

The page number to retrieve.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  | The page number to retrieve. | value must be a 32 bit integer

# PageSizeSchema

The number of items to retrieve per page.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  | The number of items to retrieve per page. | value must be a 32 bit integer

# SortBySchema

The field to sort the results by.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | The field to sort the results by. | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_all_vaults.ApiResponseFor200) | Returns all vaults in the system (paginated).
401 | [ApiResponseFor401](#get_all_vaults.ApiResponseFor401) | Unauthorized.
403 | [ApiResponseFor403](#get_all_vaults.ApiResponseFor403) | Forbidden.

#### get_all_vaults.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**VaultDtoPaginatedResponseDto**](../../models/VaultDtoPaginatedResponseDto.md) |  | 


#### get_all_vaults.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_all_vaults.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[oauth2](../../../README.md#oauth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_vault**
<a name="get_vault"></a>
> VaultDto get_vault(vault_id)

Get a single Vault

This endpoint fetches a vault identified by its unique id.

### Example

* OAuth Authentication (oauth2):
```python
import starkexpress_api
from starkexpress_api.apis.tags import vault_api
from starkexpress_api.model.vault_dto import VaultDto
from pprint import pprint
# Defining the host is optional and defaults to https://testnet-api.starkexpress.io
# See configuration.py for a list of all supported configuration parameters.
configuration = starkexpress_api.Configuration(
    host = "https://testnet-api.starkexpress.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = starkexpress_api.Configuration(
    host = "https://testnet-api.starkexpress.io",
    access_token = 'YOUR_ACCESS_TOKEN'
)
# Enter a context with an instance of the API client
with starkexpress_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vault_api.VaultApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'vaultId': "vaultId_example",
    }
    try:
        # Get a single Vault
        api_response = api_instance.get_vault(
            path_params=path_params,
        )
        pprint(api_response)
    except starkexpress_api.ApiException as e:
        print("Exception when calling VaultApi->get_vault: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
vaultId | VaultIdSchema | | 

# VaultIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_vault.ApiResponseFor200) | Returns a single vault identified by its id.
401 | [ApiResponseFor401](#get_vault.ApiResponseFor401) | Unauthorized.
403 | [ApiResponseFor403](#get_vault.ApiResponseFor403) | Forbidden.

#### get_vault.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**VaultDto**](../../models/VaultDto.md) |  | 


#### get_vault.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_vault.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[oauth2](../../../README.md#oauth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

