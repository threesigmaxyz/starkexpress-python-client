# starkexpress_api.model.fee_config_dto.FeeConfigDto

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**feeId** | str, uuid.UUID,  | str,  | The unique identifier of the fee configuration. | [optional] value must be a uuid
**action** | [**FeeAction**](FeeAction.md) | [**FeeAction**](FeeAction.md) |  | [optional] 
**basisPoints** | decimal.Decimal, int,  | decimal.Decimal,  | The basis points (1/100 of a percent) of the fee to take on the operation. | [optional] value must be a 32 bit integer

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

