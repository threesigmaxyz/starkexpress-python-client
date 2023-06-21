<a name="__pageTop"></a>
# starkexpress_api.apis.tags.user_api.UserApi

All URIs are relative to *https://testnet-api.starkexpress.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**e_ip712_details**](#e_ip712_details) | **get** /api/v1/users/register-details | Get EIP712 data to be signed
[**get_all_users**](#get_all_users) | **get** /api/v1/users | Get All Users
[**get_user**](#get_user) | **get** /api/v1/users/{userId} | Get User
[**register_user**](#register_user) | **post** /api/v1/users | Register new User

# **e_ip712_details**
<a name="e_ip712_details"></a>
> RegisterDetailsDto e_ip712_details(usernamestark_keyaddress)

Get EIP712 data to be signed

This endpoint return the typed data to be signed with EIP712 that is used on user registration.

### Example

* OAuth Authentication (oauth2):
```python
import starkexpress_api
from starkexpress_api.apis.tags import user_api
from starkexpress_api.model.register_details_dto import RegisterDetailsDto
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
    api_instance = user_api.UserApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'username': "username_example",
        'stark_key': "stark_key_example",
        'address': "address_example",
    }
    try:
        # Get EIP712 data to be signed
        api_response = api_instance.e_ip712_details(
            query_params=query_params,
        )
        pprint(api_response)
    except starkexpress_api.ApiException as e:
        print("Exception when calling UserApi->e_ip712_details: %s\n" % e)
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
username | UsernameSchema | | 
stark_key | StarkKeySchema | | 
address | AddressSchema | | 


# UsernameSchema

The username of the user.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | The username of the user. | 

# StarkKeySchema

The STARK key of the user.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | The STARK key of the user. | 

# AddressSchema

The Ethereum address associated with the user.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | The Ethereum address associated with the user. | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#e_ip712_details.ApiResponseFor200) | Returns the EIP712 typed data.
404 | [ApiResponseFor404](#e_ip712_details.ApiResponseFor404) | Not Found.
401 | [ApiResponseFor401](#e_ip712_details.ApiResponseFor401) | Unauthorized.
403 | [ApiResponseFor403](#e_ip712_details.ApiResponseFor403) | Forbidden.

#### e_ip712_details.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RegisterDetailsDto**](../../models/RegisterDetailsDto.md) |  | 


#### e_ip712_details.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiErrorResponseDto**](../../models/ApiErrorResponseDto.md) |  | 


#### e_ip712_details.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### e_ip712_details.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[oauth2](../../../README.md#oauth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_all_users**
<a name="get_all_users"></a>
> UserDtoPaginatedResponseDto get_all_users(page_numberpage_size)

Get All Users

This endpoint fetches all users.

### Example

* OAuth Authentication (oauth2):
```python
import starkexpress_api
from starkexpress_api.apis.tags import user_api
from starkexpress_api.model.user_dto_paginated_response_dto import UserDtoPaginatedResponseDto
from starkexpress_api.model.filter_options import FilterOptions
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
    api_instance = user_api.UserApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'page_number': 1,
        'page_size': 1,
    }
    try:
        # Get All Users
        api_response = api_instance.get_all_users(
            query_params=query_params,
        )
        pprint(api_response)
    except starkexpress_api.ApiException as e:
        print("Exception when calling UserApi->get_all_users: %s\n" % e)

    # example passing only optional values
    query_params = {
        'username': "username_example",
        'username_comparison': FilterOptions("StartsWith"),
        'address': "address_example",
        'creation_date': "creation_date_example",
        'creation_date_comparison': FilterOptions("StartsWith"),
        'page_number': 1,
        'page_size': 1,
        'sort_by': "sort_by_example",
    }
    try:
        # Get All Users
        api_response = api_instance.get_all_users(
            query_params=query_params,
        )
        pprint(api_response)
    except starkexpress_api.ApiException as e:
        print("Exception when calling UserApi->get_all_users: %s\n" % e)
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
username | UsernameSchema | | optional
username_comparison | UsernameComparisonSchema | | optional
address | AddressSchema | | optional
creation_date | CreationDateSchema | | optional
creation_date_comparison | CreationDateComparisonSchema | | optional
page_number | PageNumberSchema | | 
page_size | PageSizeSchema | | 
sort_by | SortBySchema | | optional


# UsernameSchema

The username of the user.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | The username of the user. | 

# UsernameComparisonSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**FilterOptions**](../../models/FilterOptions.md) |  | 


# AddressSchema

The Ethereum address associated with the user.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | The Ethereum address associated with the user. | 

# CreationDateSchema

The creation date of the user.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | The creation date of the user. | 

# CreationDateComparisonSchema
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
200 | [ApiResponseFor200](#get_all_users.ApiResponseFor200) | Returns all users.
401 | [ApiResponseFor401](#get_all_users.ApiResponseFor401) | Unauthorized.
403 | [ApiResponseFor403](#get_all_users.ApiResponseFor403) | Forbidden.

#### get_all_users.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UserDtoPaginatedResponseDto**](../../models/UserDtoPaginatedResponseDto.md) |  | 


#### get_all_users.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_all_users.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[oauth2](../../../README.md#oauth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_user**
<a name="get_user"></a>
> UserWithVaultsDto get_user(user_id)

Get User

This endpoint fetches a specific user by ID.

### Example

* OAuth Authentication (oauth2):
```python
import starkexpress_api
from starkexpress_api.apis.tags import user_api
from starkexpress_api.model.user_with_vaults_dto import UserWithVaultsDto
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
    api_instance = user_api.UserApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'userId': "userId_example",
    }
    try:
        # Get User
        api_response = api_instance.get_user(
            path_params=path_params,
        )
        pprint(api_response)
    except starkexpress_api.ApiException as e:
        print("Exception when calling UserApi->get_user: %s\n" % e)
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
userId | UserIdSchema | | 

# UserIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_user.ApiResponseFor200) | Returns an user.
404 | [ApiResponseFor404](#get_user.ApiResponseFor404) | Not Found.
401 | [ApiResponseFor401](#get_user.ApiResponseFor401) | Unauthorized.
403 | [ApiResponseFor403](#get_user.ApiResponseFor403) | Forbidden.

#### get_user.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UserWithVaultsDto**](../../models/UserWithVaultsDto.md) |  | 


#### get_user.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiErrorResponseDto**](../../models/ApiErrorResponseDto.md) |  | 


#### get_user.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_user.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[oauth2](../../../README.md#oauth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **register_user**
<a name="register_user"></a>
> UserDto register_user(register_user_model)

Register new User

This endpoint registers a user.

### Example

* OAuth Authentication (oauth2):
```python
import starkexpress_api
from starkexpress_api.apis.tags import user_api
from starkexpress_api.model.register_user_model import RegisterUserModel
from starkexpress_api.model.user_dto import UserDto
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
    api_instance = user_api.UserApi(api_client)

    # example passing only required values which don't have defaults set
    body = RegisterUserModel(
        username="username_example",
        stark_key="stark_key_example",
        stark_signature=SignatureModel(
            r="r_example",
            s="s_example",
        ),
        address="address_example",
        eip712_signature="eip712_signature_example",
    )
    try:
        # Register new User
        api_response = api_instance.register_user(
            body=body,
        )
        pprint(api_response)
    except starkexpress_api.ApiException as e:
        print("Exception when calling UserApi->register_user: %s\n" % e)
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
[**RegisterUserModel**](../../models/RegisterUserModel.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#register_user.ApiResponseFor201) | Returns the newly registered user.
400 | [ApiResponseFor400](#register_user.ApiResponseFor400) | The user registration request was invalid.
401 | [ApiResponseFor401](#register_user.ApiResponseFor401) | Unauthorized.
403 | [ApiResponseFor403](#register_user.ApiResponseFor403) | Forbidden.

#### register_user.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UserDto**](../../models/UserDto.md) |  | 


#### register_user.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiErrorResponseDto**](../../models/ApiErrorResponseDto.md) |  | 


#### register_user.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### register_user.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[oauth2](../../../README.md#oauth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

