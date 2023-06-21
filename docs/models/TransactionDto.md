# starkexpress_api.model.transaction_dto.TransactionDto

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**transactionId** | str, uuid.UUID,  | str,  | The ID of the transaction. | [optional] value must be a uuid
**starkExTransactionId** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | The sequence ID of the transaction in StarkEx. | [optional] value must be a 64 bit integer
**starkExInstanceId** | str, uuid.UUID,  | str,  | The ID of the StarkEx instance. | [optional] value must be a uuid
**tenantId** | str, uuid.UUID,  | str,  | The ID of the tenant. | [optional] value must be a uuid
**operation** | [**StarkExOperation**](StarkExOperation.md) | [**StarkExOperation**](StarkExOperation.md) |  | [optional] 
**status** | [**TransactionStatus**](TransactionStatus.md) | [**TransactionStatus**](TransactionStatus.md) |  | [optional] 
**creationDate** | str, datetime,  | str,  | The date the transaction was created. | [optional] value must conform to RFC-3339 date-time
**rawTransaction** | [**TransactionModel**](TransactionModel.md) | [**TransactionModel**](TransactionModel.md) |  | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

