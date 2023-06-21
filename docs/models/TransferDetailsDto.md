# starkexpress_api.model.transfer_details_dto.TransferDetailsDto

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**senderStarkKey** | None, str,  | NoneClass, str,  | The STARK key of the sender. | [optional] 
**senderVaultChainId** | str,  | str,  | The vault chain ID of the sender. | [optional] 
**senderVaultId** | str, uuid.UUID,  | str,  | The vault ID of the sender. | [optional] value must be a uuid
**receiverStarkKey** | None, str,  | NoneClass, str,  | The STARK key of the receiver. | [optional] 
**receiverVaultChainId** | str,  | str,  | The vault chain ID of the receiver. | [optional] 
**receiverVaultId** | str, uuid.UUID,  | str,  | The vault ID of the receiver. | [optional] value must be a uuid
**assetId** | None, str,  | NoneClass, str,  | The StarkEx ID of the asset being transferred. | [optional] 
**quantizedAmount** | str,  | str,  | The amount of the asset to be transferred, in quantized form. | [optional] 
**feeVaultChainId** | str,  | str,  | The vault chain ID of the fee sender. | [optional] 
**feeVaultId** | str, uuid.UUID,  | str,  | The vault ID of the fee sender. | [optional] value must be a uuid
**feeQuantizedAmount** | str,  | str,  | The amount of the fee asset to be collected, in quantized form. | [optional] 
**feeAssetId** | None, str,  | NoneClass, str,  | The StarkEx ID of the fee asset to be collected. | [optional] 
**expirationTimestamp** | decimal.Decimal, int,  | decimal.Decimal,  | The timestamp at which this transfer becomes invalid, in seconds since the Unix epoch. | [optional] value must be a 64 bit integer
**nonce** | decimal.Decimal, int,  | decimal.Decimal,  | The unique nonce for the transfer. | [optional] value must be a 32 bit integer
**signablePayload** | None, str,  | NoneClass, str,  | The signable payload for the transfer. | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

