# starkexpress_api.model.fee_dto.FeeDto

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**vaultId** | str, uuid.UUID,  | str,  | The vault ID of the fee sender. | [optional] value must be a uuid
**vaultChainId** | [**BigInteger**](BigInteger.md) | [**BigInteger**](BigInteger.md) |  | [optional] 
**assetId** | None, str,  | NoneClass, str,  | The StarkEx ID of the fee asset to be collected. | [optional] 
**quantizedAmount** | [**BigInteger**](BigInteger.md) | [**BigInteger**](BigInteger.md) |  | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

