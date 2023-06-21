# starkexpress_api.model.transfer_details_model.TransferDetailsModel

Request model to fetch details for a signable transfer.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Request model to fetch details for a signable transfer. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**receiverDataAvailabilityMode** | [**DataAvailabilityModes**](DataAvailabilityModes.md) | [**DataAvailabilityModes**](DataAvailabilityModes.md) |  | 
**amount** | str,  | str,  | The amount of the asset to be transferred. | 
**senderUserId** | str, uuid.UUID,  | str,  | The unique identifier of the user sending the transfer. | value must be a uuid
**assetId** | str, uuid.UUID,  | str,  | The unique identifier of the asset being transferred. | value must be a uuid
**senderDataAvailabilityMode** | [**DataAvailabilityModes**](DataAvailabilityModes.md) | [**DataAvailabilityModes**](DataAvailabilityModes.md) |  | 
**receiverUserId** | str, uuid.UUID,  | str,  | The unique identifier of the user receiving the transfer. | value must be a uuid
**tokenId** | None, str,  | NoneClass, str,  | The hexadecimal string representation of the token ID, if applicable (ie. ERC-721/ERC-1155). | [optional] 
**mintingBlob** | None, str,  | NoneClass, str,  | The hexadecimal string representation of the minting blob, if applicable (ie. Mintable ERC-20/ERC-721/ERC-1155). | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

