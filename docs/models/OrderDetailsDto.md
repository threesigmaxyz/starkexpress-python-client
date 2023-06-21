# starkexpress_api.model.order_details_dto.OrderDetailsDto

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**starkKey** | None, str,  | NoneClass, str,  | The STARK key of the user. | [optional] 
**sellQuantizedAmount** | str,  | str,  | The amount to be sold, in quantized form. | [optional] 
**buyQuantizedAmount** | str,  | str,  | The amount to be bough, in quantized form. | [optional] 
**sellVaultChainId** | str,  | str,  | The vault chain ID for the asset being sold. | [optional] 
**buyVaultChainId** | str,  | str,  | The vault chain ID for the asset being bought. | [optional] 
**fee** | [**FeeDto**](FeeDto.md) | [**FeeDto**](FeeDto.md) |  | [optional] 
**expirationTimestamp** | decimal.Decimal, int,  | decimal.Decimal,  | The timestamp at which this order becomes invalid, in seconds since the Unix epoch. | [optional] value must be a 64 bit integer
**nonce** | decimal.Decimal, int,  | decimal.Decimal,  | The unique nonce for the order. | [optional] value must be a 32 bit integer
**signablePayload** | None, str,  | NoneClass, str,  | The signable payload for the order. | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

