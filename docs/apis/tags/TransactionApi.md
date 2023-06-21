<a name="__pageTop"></a>
# starkexpress_api.apis.tags.transaction_api.TransactionApi

All URIs are relative to *https://testnet-api.starkexpress.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_transactions**](#get_all_transactions) | **get** /api/v1/transactions | Get All Transactions
[**get_transaction**](#get_transaction) | **get** /api/v1/transactions/{transactionId} | Get Transaction

# **get_all_transactions**
<a name="get_all_transactions"></a>
> TransactionDtoPaginatedResponseDto get_all_transactions(page_numberpage_size)

Get All Transactions

This endpoint fetches all transactions submitted by the system, with support for filters and pagination.

### Example

* OAuth Authentication (oauth2):
```python
import starkexpress_api
from starkexpress_api.apis.tags import transaction_api
from starkexpress_api.model.transaction_dto_paginated_response_dto import TransactionDtoPaginatedResponseDto
from starkexpress_api.model.transaction_status import TransactionStatus
from starkexpress_api.model.stark_ex_operation import StarkExOperation
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
    api_instance = transaction_api.TransactionApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'page_number': 1,
        'page_size': 1,
    }
    try:
        # Get All Transactions
        api_response = api_instance.get_all_transactions(
            query_params=query_params,
        )
        pprint(api_response)
    except starkexpress_api.ApiException as e:
        print("Exception when calling TransactionApi->get_all_transactions: %s\n" % e)

    # example passing only optional values
    query_params = {
        'transaction_status': TransactionStatus("Streamed"),
        'transaction_status_comparison': FilterOptions("StartsWith"),
        'starkex_tx_id': 1,
        'starkex_tx_id_comparison': FilterOptions("StartsWith"),
        'tx_type': StarkExOperation("Deposit"),
        'tx_type_comparison': FilterOptions("StartsWith"),
        'page_number': 1,
        'page_size': 1,
        'sort_by': "sort_by_example",
    }
    try:
        # Get All Transactions
        api_response = api_instance.get_all_transactions(
            query_params=query_params,
        )
        pprint(api_response)
    except starkexpress_api.ApiException as e:
        print("Exception when calling TransactionApi->get_all_transactions: %s\n" % e)
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
transaction_status | TransactionStatusSchema | | optional
transaction_status_comparison | TransactionStatusComparisonSchema | | optional
starkex_tx_id | StarkexTxIdSchema | | optional
starkex_tx_id_comparison | StarkexTxIdComparisonSchema | | optional
tx_type | TxTypeSchema | | optional
tx_type_comparison | TxTypeComparisonSchema | | optional
page_number | PageNumberSchema | | 
page_size | PageSizeSchema | | 
sort_by | SortBySchema | | optional


# TransactionStatusSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**TransactionStatus**](../../models/TransactionStatus.md) |  | 


# TransactionStatusComparisonSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**FilterOptions**](../../models/FilterOptions.md) |  | 


# StarkexTxIdSchema

The unique identifier of the StarkEx transaction.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  | The unique identifier of the StarkEx transaction. | 

# StarkexTxIdComparisonSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**FilterOptions**](../../models/FilterOptions.md) |  | 


# TxTypeSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**StarkExOperation**](../../models/StarkExOperation.md) |  | 


# TxTypeComparisonSchema
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
200 | [ApiResponseFor200](#get_all_transactions.ApiResponseFor200) | Returns all transactions submitted by the system (paginated).
401 | [ApiResponseFor401](#get_all_transactions.ApiResponseFor401) | Unauthorized.
403 | [ApiResponseFor403](#get_all_transactions.ApiResponseFor403) | Forbidden.

#### get_all_transactions.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TransactionDtoPaginatedResponseDto**](../../models/TransactionDtoPaginatedResponseDto.md) |  | 


#### get_all_transactions.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_all_transactions.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[oauth2](../../../README.md#oauth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_transaction**
<a name="get_transaction"></a>
> TransactionDto get_transaction(transaction_id)

Get Transaction

This endpoint fetches a specific transaction by ID.

### Example

* OAuth Authentication (oauth2):
```python
import starkexpress_api
from starkexpress_api.apis.tags import transaction_api
from starkexpress_api.model.transaction_dto import TransactionDto
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
    api_instance = transaction_api.TransactionApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'transactionId': "transactionId_example",
    }
    try:
        # Get Transaction
        api_response = api_instance.get_transaction(
            path_params=path_params,
        )
        pprint(api_response)
    except starkexpress_api.ApiException as e:
        print("Exception when calling TransactionApi->get_transaction: %s\n" % e)
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
transactionId | TransactionIdSchema | | 

# TransactionIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_transaction.ApiResponseFor200) | Returns a transaction.
404 | [ApiResponseFor404](#get_transaction.ApiResponseFor404) | Not Found.
401 | [ApiResponseFor401](#get_transaction.ApiResponseFor401) | Unauthorized.
403 | [ApiResponseFor403](#get_transaction.ApiResponseFor403) | Forbidden.

#### get_transaction.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TransactionDto**](../../models/TransactionDto.md) |  | 


#### get_transaction.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiErrorResponseDto**](../../models/ApiErrorResponseDto.md) |  | 


#### get_transaction.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_transaction.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[oauth2](../../../README.md#oauth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

