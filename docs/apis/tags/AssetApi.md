<a name="__pageTop"></a>
# starkexpress_api.apis.tags.asset_api.AssetApi

All URIs are relative to *https://testnet-api.starkexpress.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deploy_asset**](#deploy_asset) | **post** /api/v1/assets/deploy | Deploy Asset
[**enable_asset**](#enable_asset) | **post** /api/v1/assets | Enable Asset
[**get_all_assets**](#get_all_assets) | **get** /api/v1/assets | Get All Assets
[**get_asset**](#get_asset) | **get** /api/v1/assets/{assetId} | Get Asset

# **deploy_asset**
<a name="deploy_asset"></a>
> TenantAssetDto deploy_asset(deploy_asset_model)

Deploy Asset

This endpoint allows for deploying an asset and enable it in the tenant system.

### Example

* OAuth Authentication (oauth2):
```python
import starkexpress_api
from starkexpress_api.apis.tags import asset_api
from starkexpress_api.model.tenant_asset_dto import TenantAssetDto
from starkexpress_api.model.deploy_asset_model import DeployAssetModel
from starkexpress_api.model.api_error_response_dto import ApiErrorResponseDto
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
    api_instance = asset_api.AssetApi(api_client)

    # example passing only required values which don't have defaults set
    body = DeployAssetModel(
        type=AssetType("Eth"),
        name="name_example",
        symbol="symbol_example",
        uri="uri_example",
        quantum="quantum_example",
    )
    try:
        # Deploy Asset
        api_response = api_instance.deploy_asset(
            body=body,
        )
        pprint(api_response)
    except starkexpress_api.ApiException as e:
        print("Exception when calling AssetApi->deploy_asset: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DeployAssetModel**](../../models/DeployAssetModel.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#deploy_asset.ApiResponseFor201) | Returns the deployed asset.
400 | [ApiResponseFor400](#deploy_asset.ApiResponseFor400) | The asset deployment request was invalid.
401 | [ApiResponseFor401](#deploy_asset.ApiResponseFor401) | Unauthorized.
403 | [ApiResponseFor403](#deploy_asset.ApiResponseFor403) | Forbidden.

#### deploy_asset.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TenantAssetDto**](../../models/TenantAssetDto.md) |  | 


#### deploy_asset.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiErrorResponseDto**](../../models/ApiErrorResponseDto.md) |  | 


#### deploy_asset.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### deploy_asset.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[oauth2](../../../README.md#oauth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **enable_asset**
<a name="enable_asset"></a>
> TenantAssetDto enable_asset(enable_asset_model)

Enable Asset

This endpoint allows to enable an asset in the tenant system.

### Example

* OAuth Authentication (oauth2):
```python
import starkexpress_api
from starkexpress_api.apis.tags import asset_api
from starkexpress_api.model.tenant_asset_dto import TenantAssetDto
from starkexpress_api.model.enable_asset_model import EnableAssetModel
from starkexpress_api.model.api_error_response_dto import ApiErrorResponseDto
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
    api_instance = asset_api.AssetApi(api_client)

    # example passing only required values which don't have defaults set
    body = EnableAssetModel(
        asset_id="asset_id_example",
    )
    try:
        # Enable Asset
        api_response = api_instance.enable_asset(
            body=body,
        )
        pprint(api_response)
    except starkexpress_api.ApiException as e:
        print("Exception when calling AssetApi->enable_asset: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EnableAssetModel**](../../models/EnableAssetModel.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#enable_asset.ApiResponseFor201) | Returns the enabled asset.
400 | [ApiResponseFor400](#enable_asset.ApiResponseFor400) | The asset enabling request was invalid.
404 | [ApiResponseFor404](#enable_asset.ApiResponseFor404) | Not Found.
401 | [ApiResponseFor401](#enable_asset.ApiResponseFor401) | Unauthorized.
403 | [ApiResponseFor403](#enable_asset.ApiResponseFor403) | Forbidden.

#### enable_asset.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TenantAssetDto**](../../models/TenantAssetDto.md) |  | 


#### enable_asset.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiErrorResponseDto**](../../models/ApiErrorResponseDto.md) |  | 


#### enable_asset.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiErrorResponseDto**](../../models/ApiErrorResponseDto.md) |  | 


#### enable_asset.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### enable_asset.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[oauth2](../../../README.md#oauth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_all_assets**
<a name="get_all_assets"></a>
> TenantAssetDtoPaginatedResponseDto get_all_assets(page_numberpage_size)

Get All Assets

This endpoint fetches all assets enabled in the tenant system, with support for filters and pagination.

### Example

* OAuth Authentication (oauth2):
```python
import starkexpress_api
from starkexpress_api.apis.tags import asset_api
from starkexpress_api.model.asset_type import AssetType
from starkexpress_api.model.filter_options import FilterOptions
from starkexpress_api.model.tenant_asset_dto_paginated_response_dto import TenantAssetDtoPaginatedResponseDto
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
    api_instance = asset_api.AssetApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'page_number': 1,
        'page_size': 1,
    }
    try:
        # Get All Assets
        api_response = api_instance.get_all_assets(
            query_params=query_params,
        )
        pprint(api_response)
    except starkexpress_api.ApiException as e:
        print("Exception when calling AssetApi->get_all_assets: %s\n" % e)

    # example passing only optional values
    query_params = {
        'asset_id': "asset_id_example",
        'asset_type': AssetType("Eth"),
        'asset_type_comparison': FilterOptions("StartsWith"),
        'asset_symbol': "asset_symbol_example",
        'asset_symbol_comparison': FilterOptions("StartsWith"),
        'page_number': 1,
        'page_size': 1,
        'sort_by': "sort_by_example",
    }
    try:
        # Get All Assets
        api_response = api_instance.get_all_assets(
            query_params=query_params,
        )
        pprint(api_response)
    except starkexpress_api.ApiException as e:
        print("Exception when calling AssetApi->get_all_assets: %s\n" % e)
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
asset_id | AssetIdSchema | | optional
asset_type | AssetTypeSchema | | optional
asset_type_comparison | AssetTypeComparisonSchema | | optional
asset_symbol | AssetSymbolSchema | | optional
asset_symbol_comparison | AssetSymbolComparisonSchema | | optional
page_number | PageNumberSchema | | 
page_size | PageSizeSchema | | 
sort_by | SortBySchema | | optional


# AssetIdSchema

The unique identifier of the asset.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  | The unique identifier of the asset. | value must be a uuid

# AssetTypeSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**AssetType**](../../models/AssetType.md) |  | 


# AssetTypeComparisonSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**FilterOptions**](../../models/FilterOptions.md) |  | 


# AssetSymbolSchema

The symbol of the asset.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | The symbol of the asset. | 

# AssetSymbolComparisonSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**FilterOptions**](../../models/FilterOptions.md) |  | 


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
200 | [ApiResponseFor200](#get_all_assets.ApiResponseFor200) | Returns all assets enabled in the tenant system (paginated).
401 | [ApiResponseFor401](#get_all_assets.ApiResponseFor401) | Unauthorized.
403 | [ApiResponseFor403](#get_all_assets.ApiResponseFor403) | Forbidden.

#### get_all_assets.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TenantAssetDtoPaginatedResponseDto**](../../models/TenantAssetDtoPaginatedResponseDto.md) |  | 


#### get_all_assets.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_all_assets.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[oauth2](../../../README.md#oauth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_asset**
<a name="get_asset"></a>
> TenantAssetDto get_asset(asset_id)

Get Asset

This endpoint fetches a specific enabled asset by ID.

### Example

* OAuth Authentication (oauth2):
```python
import starkexpress_api
from starkexpress_api.apis.tags import asset_api
from starkexpress_api.model.tenant_asset_dto import TenantAssetDto
from starkexpress_api.model.api_error_response_dto import ApiErrorResponseDto
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
    api_instance = asset_api.AssetApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'assetId': "assetId_example",
    }
    try:
        # Get Asset
        api_response = api_instance.get_asset(
            path_params=path_params,
        )
        pprint(api_response)
    except starkexpress_api.ApiException as e:
        print("Exception when calling AssetApi->get_asset: %s\n" % e)
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
assetId | AssetIdSchema | | 

# AssetIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_asset.ApiResponseFor200) | Returns an asset enabled in the tenant system.
404 | [ApiResponseFor404](#get_asset.ApiResponseFor404) | Not Found.
401 | [ApiResponseFor401](#get_asset.ApiResponseFor401) | Unauthorized.
403 | [ApiResponseFor403](#get_asset.ApiResponseFor403) | Forbidden.

#### get_asset.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TenantAssetDto**](../../models/TenantAssetDto.md) |  | 


#### get_asset.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiErrorResponseDto**](../../models/ApiErrorResponseDto.md) |  | 


#### get_asset.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_asset.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[oauth2](../../../README.md#oauth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

