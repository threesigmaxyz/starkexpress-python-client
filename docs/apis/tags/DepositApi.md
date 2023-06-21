<a name="__pageTop"></a>
# starkexpress_api.apis.tags.deposit_api.DepositApi

All URIs are relative to *https://testnet-api.starkexpress.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deposit_details**](#deposit_details) | **post** /api/v1/vaults/deposit-details | Returns the deposit details for a given asset.

# **deposit_details**
<a name="deposit_details"></a>
> DepositDetailsDto deposit_details(deposit_details_model)

Returns the deposit details for a given asset.

This endpoint returns the deposit details for a given user, asset, and data availability mode.

### Example

* OAuth Authentication (oauth2):
```python
import starkexpress_api
from starkexpress_api.apis.tags import deposit_api
from starkexpress_api.model.deposit_details_model import DepositDetailsModel
from starkexpress_api.model.deposit_details_dto import DepositDetailsDto
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
    api_instance = deposit_api.DepositApi(api_client)

    # example passing only required values which don't have defaults set
    body = DepositDetailsModel(
        user_id="user_id_example",
        asset_id="asset_id_example",
        data_availability_mode=DataAvailabilityModes("ZkRollup"),
        token_id="token_id_example",
        amount="amount_example",
    )
    try:
        # Returns the deposit details for a given asset.
        api_response = api_instance.deposit_details(
            body=body,
        )
        pprint(api_response)
    except starkexpress_api.ApiException as e:
        print("Exception when calling DepositApi->deposit_details: %s\n" % e)
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
[**DepositDetailsModel**](../../models/DepositDetailsModel.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#deposit_details.ApiResponseFor200) | Returns the deposit details.
400 | [ApiResponseFor400](#deposit_details.ApiResponseFor400) | The deposit details request was invalid.
404 | [ApiResponseFor404](#deposit_details.ApiResponseFor404) | Not Found.
401 | [ApiResponseFor401](#deposit_details.ApiResponseFor401) | Unauthorized.
403 | [ApiResponseFor403](#deposit_details.ApiResponseFor403) | Forbidden.

#### deposit_details.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DepositDetailsDto**](../../models/DepositDetailsDto.md) |  | 


#### deposit_details.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiErrorResponseDto**](../../models/ApiErrorResponseDto.md) |  | 


#### deposit_details.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiErrorResponseDto**](../../models/ApiErrorResponseDto.md) |  | 


#### deposit_details.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### deposit_details.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[oauth2](../../../README.md#oauth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

