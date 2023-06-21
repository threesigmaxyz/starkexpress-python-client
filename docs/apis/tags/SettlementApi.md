<a name="__pageTop"></a>
# starkexpress_api.apis.tags.settlement_api.SettlementApi

All URIs are relative to *https://testnet-api.starkexpress.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**submit_settlement**](#submit_settlement) | **post** /api/v1/settlements | Submit Settlement

# **submit_settlement**
<a name="submit_settlement"></a>
> [VaultDto] submit_settlement(submit_settlement_model)

Submit Settlement

This endpoint submits an order settlement.

### Example

* OAuth Authentication (oauth2):
```python
import starkexpress_api
from starkexpress_api.apis.tags import settlement_api
from starkexpress_api.model.submit_settlement_model import SubmitSettlementModel
from starkexpress_api.model.vault_dto import VaultDto
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
    api_instance = settlement_api.SettlementApi(api_client)

    # example passing only required values which don't have defaults set
    body = SubmitSettlementModel(
        order_a=SettlementOrderModel(
            buy_vault_id="buy_vault_id_example",
            buy_quantized_amount="buy_quantized_amount_example",
            sell_vault_id="sell_vault_id_example",
            sell_quantized_amount="sell_quantized_amount_example",
            fee_vault_id="fee_vault_id_example",
            fee_quantized_amount="fee_quantized_amount_example",
            nonce=0,
            signature=SignatureModel(
                r="r_example",
                s="s_example",
            ),
            expiration_timestamp=1,
        ),
        order_b=SettlementOrderModel(),
        settlement_info=SettlementInfoModel(
            order_a_fee_destination_vault_id="order_a_fee_destination_vault_id_example",
            order_a_fee_amount="order_a_fee_amount_example",
            order_b_fee_destination_vault_id="order_b_fee_destination_vault_id_example",
            order_b_fee_amount="order_b_fee_amount_example",
        ),
    )
    try:
        # Submit Settlement
        api_response = api_instance.submit_settlement(
            body=body,
        )
        pprint(api_response)
    except starkexpress_api.ApiException as e:
        print("Exception when calling SettlementApi->submit_settlement: %s\n" % e)
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
[**SubmitSettlementModel**](../../models/SubmitSettlementModel.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#submit_settlement.ApiResponseFor200) | Returns the vaults updated by the settlement operation.
400 | [ApiResponseFor400](#submit_settlement.ApiResponseFor400) | The settlement request was invalid.
404 | [ApiResponseFor404](#submit_settlement.ApiResponseFor404) | Not Found.
401 | [ApiResponseFor401](#submit_settlement.ApiResponseFor401) | Unauthorized.
403 | [ApiResponseFor403](#submit_settlement.ApiResponseFor403) | Forbidden.

#### submit_settlement.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**VaultDto**]({{complexTypePrefix}}VaultDto.md) | [**VaultDto**]({{complexTypePrefix}}VaultDto.md) | [**VaultDto**]({{complexTypePrefix}}VaultDto.md) |  | 

#### submit_settlement.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiErrorResponseDto**](../../models/ApiErrorResponseDto.md) |  | 


#### submit_settlement.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiErrorResponseDto**](../../models/ApiErrorResponseDto.md) |  | 


#### submit_settlement.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### submit_settlement.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[oauth2](../../../README.md#oauth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

