# starkexpress_api.model.settlement_order_model.SettlementOrderModel

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**buyVaultId** | str, uuid.UUID,  | str,  | The unique identifier of the buy vault. | value must be a uuid
**signature** | [**SignatureModel**](SignatureModel.md) | [**SignatureModel**](SignatureModel.md) |  | 
**buyQuantizedAmount** | str,  | str,  | The amount of the asset to be settled, in quantized form. | 
**expirationTimestamp** | decimal.Decimal, int,  | decimal.Decimal,  | The timestamp at which this transfer becomes invalid, in seconds since the Unix epoch. | value must be a 64 bit integer
**sellQuantizedAmount** | str,  | str,  | The amount of the asset to be settled, in quantized form. | 
**nonce** | decimal.Decimal, int,  | decimal.Decimal,  | The unique nonce for the transfer. | value must be a 32 bit integer
**sellVaultId** | str, uuid.UUID,  | str,  | The unique identifier of the sell vault. | value must be a uuid
**feeVaultId** | None, str, uuid.UUID,  | NoneClass, str,  | The unique identifier of the transfer sender vault. | [optional] value must be a uuid
**feeQuantizedAmount** | None, str,  | NoneClass, str,  | The amount of the fee asset to be collected, in quantized form. | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

