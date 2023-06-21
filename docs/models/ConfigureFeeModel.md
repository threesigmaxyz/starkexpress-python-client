# starkexpress_api.model.configure_fee_model.ConfigureFeeModel

Request model to configure the fee model for an operation.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Request model to configure the fee model for an operation. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**basisPoints** | decimal.Decimal, int,  | decimal.Decimal,  | The basis points (1/100 of a percent) of the fee to take on the operation. | value must be a 32 bit integer
**feeAction** | [**FeeAction**](FeeAction.md) | [**FeeAction**](FeeAction.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

