<a name="__pageTop"></a>
# starkexpress_api.apis.tags.order_api.OrderApi

All URIs are relative to *https://testnet-api.starkexpress.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_order**](#cancel_order) | **delete** /api/v1/orders/{orderId} | Cancel Order (Not Implemented)
[**order_details**](#order_details) | **post** /api/v1/orders/details | Get Order Details (Not Implemented)
[**submit_order**](#submit_order) | **post** /api/v1/orders | Submit Order (Not Implemented)

# **cancel_order**
<a name="cancel_order"></a>
> OrderDto cancel_order(order_id)

Cancel Order (Not Implemented)

This endpoint cancels an active order.

### Example

```python
import starkexpress_api
from starkexpress_api.apis.tags import order_api
from starkexpress_api.model.api_error_response_dto import ApiErrorResponseDto
from starkexpress_api.model.order_dto import OrderDto
from pprint import pprint
# Defining the host is optional and defaults to https://testnet-api.starkexpress.io
# See configuration.py for a list of all supported configuration parameters.
configuration = starkexpress_api.Configuration(
    host = "https://testnet-api.starkexpress.io"
)

# Enter a context with an instance of the API client
with starkexpress_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = order_api.OrderApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'orderId': "orderId_example",
    }
    try:
        # Cancel Order (Not Implemented)
        api_response = api_instance.cancel_order(
            path_params=path_params,
        )
        pprint(api_response)
    except starkexpress_api.ApiException as e:
        print("Exception when calling OrderApi->cancel_order: %s\n" % e)
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
orderId | OrderIdSchema | | 

# OrderIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#cancel_order.ApiResponseFor200) | Returns the cancelled order.
404 | [ApiResponseFor404](#cancel_order.ApiResponseFor404) | Not Found.

#### cancel_order.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**OrderDto**](../../models/OrderDto.md) |  | 


#### cancel_order.ApiResponseFor404
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

# **order_details**
<a name="order_details"></a>
> OrderDetailsDto order_details(order_details_model)

Get Order Details (Not Implemented)

This endpoint allows for fetching details of an order to be signed.

### Example

```python
import starkexpress_api
from starkexpress_api.apis.tags import order_api
from starkexpress_api.model.order_details_dto import OrderDetailsDto
from starkexpress_api.model.order_details_model import OrderDetailsModel
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
    api_instance = order_api.OrderApi(api_client)

    # example passing only required values which don't have defaults set
    body = OrderDetailsModel(
        orderbook_id="orderbook_id_example",
        user_id="user_id_example",
        side=OrderSide("Bid"),
        price=3.14,
        amount=BigInteger(
            bit_count=1,
            bit_length=1,
            int_value=1,
            int_value_exact=1,
            long_value=1,
            long_value_exact=1,
            sign_value=1,
        ),
        sell_data_availability_mode=DataAvailabilityModes("ZkRollup"),
        buy_data_availability_mode=DataAvailabilityModes("ZkRollup"),
    )
    try:
        # Get Order Details (Not Implemented)
        api_response = api_instance.order_details(
            body=body,
        )
        pprint(api_response)
    except starkexpress_api.ApiException as e:
        print("Exception when calling OrderApi->order_details: %s\n" % e)
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
[**OrderDetailsModel**](../../models/OrderDetailsModel.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#order_details.ApiResponseFor200) | Returns the signable order details.
400 | [ApiResponseFor400](#order_details.ApiResponseFor400) | The signable order request was invalid.
404 | [ApiResponseFor404](#order_details.ApiResponseFor404) | Not Found.

#### order_details.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**OrderDetailsDto**](../../models/OrderDetailsDto.md) |  | 


#### order_details.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiErrorResponseDto**](../../models/ApiErrorResponseDto.md) |  | 


#### order_details.ApiResponseFor404
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

# **submit_order**
<a name="submit_order"></a>
> OrderDto submit_order(submit_order_model)

Submit Order (Not Implemented)

This endpoint submits an order to the matching engine.

### Example

```python
import starkexpress_api
from starkexpress_api.apis.tags import order_api
from starkexpress_api.model.submit_order_model import SubmitOrderModel
from starkexpress_api.model.api_error_response_dto import ApiErrorResponseDto
from starkexpress_api.model.order_dto import OrderDto
from pprint import pprint
# Defining the host is optional and defaults to https://testnet-api.starkexpress.io
# See configuration.py for a list of all supported configuration parameters.
configuration = starkexpress_api.Configuration(
    host = "https://testnet-api.starkexpress.io"
)

# Enter a context with an instance of the API client
with starkexpress_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = order_api.OrderApi(api_client)

    # example passing only required values which don't have defaults set
    body = SubmitOrderModel(
        orderbook_id="orderbook_id_example",
        user_id="user_id_example",
        side=OrderSide("Bid"),
        price=3.14,
        amount="amount_example",
        sell_data_availability_mode=DataAvailabilityModes("ZkRollup"),
        buy_data_availability_mode=DataAvailabilityModes("ZkRollup"),
        expiration_timestamp=1,
        nonce=0,
        signature=SignatureModel(
            r="r_example",
            s="s_example",
        ),
    )
    try:
        # Submit Order (Not Implemented)
        api_response = api_instance.submit_order(
            body=body,
        )
        pprint(api_response)
    except starkexpress_api.ApiException as e:
        print("Exception when calling OrderApi->submit_order: %s\n" % e)
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
[**SubmitOrderModel**](../../models/SubmitOrderModel.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#submit_order.ApiResponseFor201) | Returns the created order.
400 | [ApiResponseFor400](#submit_order.ApiResponseFor400) | The order submission request was invalid.

#### submit_order.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**OrderDto**](../../models/OrderDto.md) |  | 


#### submit_order.ApiResponseFor400
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

