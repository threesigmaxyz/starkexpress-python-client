# starkexpress_api.model.transfer_model.TransferModel

Request model to transfer assets between users.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Request model to transfer assets between users. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**signature** | [**SignatureModel**](SignatureModel.md) | [**SignatureModel**](SignatureModel.md) |  | 
**senderVaultId** | str, uuid.UUID,  | str,  | The unique identifier of the transfer sender vault. | value must be a uuid
**quantizedAmount** | str,  | str,  | The amount of the asset to be transferred, in quantized form. | 
**receiverVaultId** | str, uuid.UUID,  | str,  | The unique identifier of the transfer recipient vault. | value must be a uuid
**expirationTimestamp** | decimal.Decimal, int,  | decimal.Decimal,  | The timestamp at which this transfer becomes invalid, in seconds since the Unix epoch. | value must be a 64 bit integer
**nonce** | decimal.Decimal, int,  | decimal.Decimal,  | The unique nonce for the transfer. | value must be a 32 bit integer

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

