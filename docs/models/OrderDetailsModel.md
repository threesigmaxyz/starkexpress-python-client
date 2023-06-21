# starkexpress_api.model.order_details_model.OrderDetailsModel

Request model to fetch details for a signable order.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Request model to fetch details for a signable order. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**amount** | [**BigInteger**](BigInteger.md) | [**BigInteger**](BigInteger.md) |  | 
**side** | [**OrderSide**](OrderSide.md) | [**OrderSide**](OrderSide.md) |  | 
**orderbookId** | str, uuid.UUID,  | str,  | The ID of the orderbook. | value must be a uuid
**price** | decimal.Decimal, int, float,  | decimal.Decimal,  | The order price. | value must be a 64 bit float
**sellDataAvailabilityMode** | [**DataAvailabilityModes**](DataAvailabilityModes.md) | [**DataAvailabilityModes**](DataAvailabilityModes.md) |  | 
**buyDataAvailabilityMode** | [**DataAvailabilityModes**](DataAvailabilityModes.md) | [**DataAvailabilityModes**](DataAvailabilityModes.md) |  | 
**userId** | str, uuid.UUID,  | str,  | The unique identifier of the user submitting the order. | value must be a uuid

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

