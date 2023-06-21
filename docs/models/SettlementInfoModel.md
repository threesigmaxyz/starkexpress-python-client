# starkexpress_api.model.settlement_info_model.SettlementInfoModel

Settlement details model.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Settlement details model. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**orderAFeeDestinationVaultId** | None, str, uuid.UUID,  | NoneClass, str,  | The unique identifier of the destination vault for the order A fee. | [optional] value must be a uuid
**orderAFeeAmount** | None, str,  | NoneClass, str,  | The order A fee amount. | [optional] 
**orderBFeeDestinationVaultId** | None, str, uuid.UUID,  | NoneClass, str,  | The unique identifier of the destination vault for the order B fee. | [optional] value must be a uuid
**orderBFeeAmount** | None, str,  | NoneClass, str,  | The order B fee amount. | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

