<a name="__pageTop"></a>
# starkexpress_api.apis.tags.orderbook_api.OrderbookApi

All URIs are relative to *https://testnet-api.starkexpress.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_orderbook**](#create_orderbook) | **post** /api/v1/orderbooks | Create Orderbook (Not Implemented)
[**get_orderbook**](#get_orderbook) | **get** /api/v1/orderbooks/{orderbookId} | Get Orderbook (Not Implemented)
[**get_orderbook_level1_data**](#get_orderbook_level1_data) | **get** /api/v1/orderbooks/{orderbookId}/l1 | Get Orderbook L1 Data (Not Implemented)
[**get_orderbook_level2_data**](#get_orderbook_level2_data) | **get** /api/v1/orderbooks/{orderbookId}/l2 | Get Orderbook L2 Data (Not Implemented)

# **create_orderbook**
<a name="create_orderbook"></a>
> OrderbookDto create_orderbook(create_orderbook_model)

Create Orderbook (Not Implemented)

This endpoint creates an orderbook.

### Example

```python
import starkexpress_api
from starkexpress_api.apis.tags import orderbook_api
from starkexpress_api.model.orderbook_dto import OrderbookDto
from starkexpress_api.model.create_orderbook_model import CreateOrderbookModel
from starkexpress_api.model.api_error_response_dto import ApiErrorResponseDto
from pprint import pprint
# Defining the host is optional and defaults to https://testnet-api.starkexpress.io
# See configuration.py for a list of all supported configuration parameters.
configuration = starkexpress_api.Configuration(
    host = "https://testnet-api.starkexpress.io"
)

# Enter a context with an instance of the API client
with starkexpress_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = orderbook_api.OrderbookApi(api_client)

    # example passing only required values which don't have defaults set
    body = CreateOrderbookModel(
        base_asset_id="base_asset_id_example",
        quote_asset_id="quote_asset_id_example",
        base_asset_precision=1,
        quote_asset_precision=1,
    )
    try:
        # Create Orderbook (Not Implemented)
        api_response = api_instance.create_orderbook(
            body=body,
        )
        pprint(api_response)
    except starkexpress_api.ApiException as e:
        print("Exception when calling OrderbookApi->create_orderbook: %s\n" % e)
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
[**CreateOrderbookModel**](../../models/CreateOrderbookModel.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#create_orderbook.ApiResponseFor201) | Returns the created orderbook.
400 | [ApiResponseFor400](#create_orderbook.ApiResponseFor400) | The orderbook creation request was invalid.

#### create_orderbook.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**OrderbookDto**](../../models/OrderbookDto.md) |  | 


#### create_orderbook.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiErrorResponseDto**](../../models/ApiErrorResponseDto.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_orderbook**
<a name="get_orderbook"></a>
> OrderbookDto get_orderbook(orderbook_id)

Get Orderbook (Not Implemented)

This endpoint fetches orderbook metadata by ID.

### Example

```python
import starkexpress_api
from starkexpress_api.apis.tags import orderbook_api
from starkexpress_api.model.orderbook_dto import OrderbookDto
from starkexpress_api.model.api_error_response_dto import ApiErrorResponseDto
from pprint import pprint
# Defining the host is optional and defaults to https://testnet-api.starkexpress.io
# See configuration.py for a list of all supported configuration parameters.
configuration = starkexpress_api.Configuration(
    host = "https://testnet-api.starkexpress.io"
)

# Enter a context with an instance of the API client
with starkexpress_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = orderbook_api.OrderbookApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'orderbookId': "orderbookId_example",
    }
    try:
        # Get Orderbook (Not Implemented)
        api_response = api_instance.get_orderbook(
            path_params=path_params,
        )
        pprint(api_response)
    except starkexpress_api.ApiException as e:
        print("Exception when calling OrderbookApi->get_orderbook: %s\n" % e)
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
orderbookId | OrderbookIdSchema | | 

# OrderbookIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_orderbook.ApiResponseFor200) | Returns orderbook metadata.
404 | [ApiResponseFor404](#get_orderbook.ApiResponseFor404) | Not Found.

#### get_orderbook.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**OrderbookDto**](../../models/OrderbookDto.md) |  | 


#### get_orderbook.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiErrorResponseDto**](../../models/ApiErrorResponseDto.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_orderbook_level1_data**
<a name="get_orderbook_level1_data"></a>
> OrderbookLevel1DataDto get_orderbook_level1_data(orderbook_id)

Get Orderbook L1 Data (Not Implemented)

This endpoint fetches orderbook level 1 data by ID.

### Example

```python
import starkexpress_api
from starkexpress_api.apis.tags import orderbook_api
from starkexpress_api.model.orderbook_level1_data_dto import OrderbookLevel1DataDto
from starkexpress_api.model.api_error_response_dto import ApiErrorResponseDto
from pprint import pprint
# Defining the host is optional and defaults to https://testnet-api.starkexpress.io
# See configuration.py for a list of all supported configuration parameters.
configuration = starkexpress_api.Configuration(
    host = "https://testnet-api.starkexpress.io"
)

# Enter a context with an instance of the API client
with starkexpress_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = orderbook_api.OrderbookApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'orderbookId': "orderbookId_example",
    }
    try:
        # Get Orderbook L1 Data (Not Implemented)
        api_response = api_instance.get_orderbook_level1_data(
            path_params=path_params,
        )
        pprint(api_response)
    except starkexpress_api.ApiException as e:
        print("Exception when calling OrderbookApi->get_orderbook_level1_data: %s\n" % e)
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
orderbookId | OrderbookIdSchema | | 

# OrderbookIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_orderbook_level1_data.ApiResponseFor200) | Returns orderbook level 1 data.
404 | [ApiResponseFor404](#get_orderbook_level1_data.ApiResponseFor404) | Not Found.

#### get_orderbook_level1_data.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**OrderbookLevel1DataDto**](../../models/OrderbookLevel1DataDto.md) |  | 


#### get_orderbook_level1_data.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiErrorResponseDto**](../../models/ApiErrorResponseDto.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_orderbook_level2_data**
<a name="get_orderbook_level2_data"></a>
> OrderbookLevel2DataDto get_orderbook_level2_data(orderbook_id)

Get Orderbook L2 Data (Not Implemented)

This endpoint fetches orderbook level 2 data by ID.

### Example

```python
import starkexpress_api
from starkexpress_api.apis.tags import orderbook_api
from starkexpress_api.model.orderbook_level2_data_dto import OrderbookLevel2DataDto
from starkexpress_api.model.api_error_response_dto import ApiErrorResponseDto
from pprint import pprint
# Defining the host is optional and defaults to https://testnet-api.starkexpress.io
# See configuration.py for a list of all supported configuration parameters.
configuration = starkexpress_api.Configuration(
    host = "https://testnet-api.starkexpress.io"
)

# Enter a context with an instance of the API client
with starkexpress_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = orderbook_api.OrderbookApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'orderbookId': "orderbookId_example",
    }
    query_params = {
    }
    try:
        # Get Orderbook L2 Data (Not Implemented)
        api_response = api_instance.get_orderbook_level2_data(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except starkexpress_api.ApiException as e:
        print("Exception when calling OrderbookApi->get_orderbook_level2_data: %s\n" % e)

    # example passing only optional values
    path_params = {
        'orderbookId': "orderbookId_example",
    }
    query_params = {
        'depth': 1,
    }
    try:
        # Get Orderbook L2 Data (Not Implemented)
        api_response = api_instance.get_orderbook_level2_data(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except starkexpress_api.ApiException as e:
        print("Exception when calling OrderbookApi->get_orderbook_level2_data: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
depth | DepthSchema | | optional


# DepthSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
orderbookId | OrderbookIdSchema | | 

# OrderbookIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_orderbook_level2_data.ApiResponseFor200) | Returns orderbook level 2 data.
404 | [ApiResponseFor404](#get_orderbook_level2_data.ApiResponseFor404) | Not Found.

#### get_orderbook_level2_data.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**OrderbookLevel2DataDto**](../../models/OrderbookLevel2DataDto.md) |  | 


#### get_orderbook_level2_data.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiErrorResponseDto**](../../models/ApiErrorResponseDto.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

