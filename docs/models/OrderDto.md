# starkexpress_api.model.order_dto.OrderDto

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**orderId** | str, uuid.UUID,  | str,  | The ID of the order. | [optional] value must be a uuid
**orderbookId** | str, uuid.UUID,  | str,  | The ID of the orderbook. | [optional] value must be a uuid
**price** | decimal.Decimal, int, float,  | decimal.Decimal,  | The order price. | [optional] value must be a 64 bit float
**originalAmount** | str,  | str,  | The original order amount. | [optional] 
**executedAmount** | str,  | str,  | The executed order amount. | [optional] 
**[fills](#fills)** | list, tuple, None,  | tuple, NoneClass,  | The order fills. | [optional] 

# fills

The order fills.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | The order fills. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**OrderFillDto**](OrderFillDto.md) | [**OrderFillDto**](OrderFillDto.md) | [**OrderFillDto**](OrderFillDto.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

