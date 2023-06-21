# starkexpress_api.model.submit_order_model.SubmitOrderModel

Request model to submit an orderbook order.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Request model to submit an orderbook order. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**amount** | str,  | str,  | The order amount. | 
**side** | [**OrderSide**](OrderSide.md) | [**OrderSide**](OrderSide.md) |  | 
**orderbookId** | str, uuid.UUID,  | str,  | The ID of the orderbook. | value must be a uuid
**signature** | [**SignatureModel**](SignatureModel.md) | [**SignatureModel**](SignatureModel.md) |  | 
**price** | decimal.Decimal, int, float,  | decimal.Decimal,  | The order price. | value must be a 64 bit float
**sellDataAvailabilityMode** | [**DataAvailabilityModes**](DataAvailabilityModes.md) | [**DataAvailabilityModes**](DataAvailabilityModes.md) |  | 
**expirationTimestamp** | decimal.Decimal, int,  | decimal.Decimal,  | The timestamp at which this order becomes invalid, in seconds since the Unix epoch. | value must be a 64 bit integer
**buyDataAvailabilityMode** | [**DataAvailabilityModes**](DataAvailabilityModes.md) | [**DataAvailabilityModes**](DataAvailabilityModes.md) |  | 
**nonce** | decimal.Decimal, int,  | decimal.Decimal,  | The unique nonce for the order. | value must be a 32 bit integer
**userId** | str, uuid.UUID,  | str,  | The unique identifier of the user submitting the order. | value must be a uuid

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

