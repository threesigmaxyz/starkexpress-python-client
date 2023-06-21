# starkexpress_api.model.deposit_details_model.DepositDetailsModel

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**amount** | str,  | str,  | The amount of the asset to be deposited. | 
**assetId** | str, uuid.UUID,  | str,  | The ID of the vault&#x27;s asset. | value must be a uuid
**userId** | str, uuid.UUID,  | str,  | The ID of the user for which the vault should be allocated. | value must be a uuid
**dataAvailabilityMode** | [**DataAvailabilityModes**](DataAvailabilityModes.md) | [**DataAvailabilityModes**](DataAvailabilityModes.md) |  | 
**tokenId** | None, str,  | NoneClass, str,  | The hexadecimal string representation of the vault&#x27;s asset token ID, if applicable (ie. ERC-721/ERC-1155). | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

