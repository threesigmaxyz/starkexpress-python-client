# starkexpress_api.model.vault_dto.VaultDto

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**vaultId** | str, uuid.UUID,  | str,  | The ID of the vault. | [optional] value must be a uuid
**vaultChainId** | str,  | str,  | The StarkEx ID of the vault. | [optional] 
**starkExAddress** | None, str,  | NoneClass, str,  | The address of the StarkEx instance associated with the vault. | [optional] 
**assetSymbol** | None, str,  | NoneClass, str,  | The symbol of the asset associated with the vault. | [optional] 
**tokenId** | None, str,  | NoneClass, str,  | The token id of the asset associated with the vault, if the asset is an ERC721 or ERC1155. | [optional] 
**mintingBlob** | None, str,  | NoneClass, str,  | The minting blob of the asset associated with the vault, if the asset is a Mintable ERC20, ERC721 or ERC1155. | [optional] 
**assetStarkExId** | None, str,  | NoneClass, str,  | The StarkEx ID of the asset associated with the vault. | [optional] 
**userStarkKey** | None, str,  | NoneClass, str,  | The STARK key of the user associated with the vault. | [optional] 
**availableBalance** | str,  | str,  | The available balance of the vault. | [optional] 
**accountingBalance** | str,  | str,  | The accounting balance of the vault. | [optional] 
**dataAvailabilityMode** | [**DataAvailabilityModes**](DataAvailabilityModes.md) | [**DataAvailabilityModes**](DataAvailabilityModes.md) |  | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

