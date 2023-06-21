<a name="__pageTop"></a>
# starkexpress_api.apis.tags.fee_api.FeeApi

All URIs are relative to *https://testnet-api.starkexpress.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**configure_fee_model**](#configure_fee_model) | **post** /api/v1/fees | Configure Fee Model
[**get_fee_model**](#get_fee_model) | **get** /api/v1/fees/{feeId} | Get Fee Model

# **configure_fee_model**
<a name="configure_fee_model"></a>
> FeeConfigDto configure_fee_model(configure_fee_model)

Configure Fee Model

This endpoint allows to configure the fee model for a specific operation.

### Example

```python
import starkexpress_api
from starkexpress_api.apis.tags import fee_api
from starkexpress_api.model.fee_config_dto import FeeConfigDto
from starkexpress_api.model.configure_fee_model import ConfigureFeeModel
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
    api_instance = fee_api.FeeApi(api_client)

    # example passing only required values which don't have defaults set
    body = ConfigureFeeModel(
        fee_action=FeeAction("Transfer"),
        basis_points=0,
    )
    try:
        # Configure Fee Model
        api_response = api_instance.configure_fee_model(
            body=body,
        )
        pprint(api_response)
    except starkexpress_api.ApiException as e:
        print("Exception when calling FeeApi->configure_fee_model: %s\n" % e)
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
[**ConfigureFeeModel**](../../models/ConfigureFeeModel.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#configure_fee_model.ApiResponseFor201) | Returns the configured operation fee.
400 | [ApiResponseFor400](#configure_fee_model.ApiResponseFor400) | The fee model configuration request was invalid.

#### configure_fee_model.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FeeConfigDto**](../../models/FeeConfigDto.md) |  | 


#### configure_fee_model.ApiResponseFor400
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

# **get_fee_model**
<a name="get_fee_model"></a>
> FeeConfigDto get_fee_model(fee_id)

Get Fee Model

This endpoint fetches a configured operation fee by ID.

### Example

```python
import starkexpress_api
from starkexpress_api.apis.tags import fee_api
from starkexpress_api.model.fee_config_dto import FeeConfigDto
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
    api_instance = fee_api.FeeApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'feeId': "feeId_example",
    }
    try:
        # Get Fee Model
        api_response = api_instance.get_fee_model(
            path_params=path_params,
        )
        pprint(api_response)
    except starkexpress_api.ApiException as e:
        print("Exception when calling FeeApi->get_fee_model: %s\n" % e)
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
feeId | FeeIdSchema | | 

# FeeIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_fee_model.ApiResponseFor200) | Returns a configured operation fee.
404 | [ApiResponseFor404](#get_fee_model.ApiResponseFor404) | Not Found.

#### get_fee_model.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FeeConfigDto**](../../models/FeeConfigDto.md) |  | 


#### get_fee_model.ApiResponseFor404
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

