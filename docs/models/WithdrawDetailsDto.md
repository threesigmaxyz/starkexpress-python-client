# starkexpress_api.model.withdraw_details_dto.WithdrawDetailsDto

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**vault** | [**VaultDto**](VaultDto.md) | [**VaultDto**](VaultDto.md) |  | [optional] 
**operatorContractAddress** | None, str,  | NoneClass, str,  | The smart contract address that processes on-chain withdraws. | [optional] 
**withdrawFunction** | None, str,  | NoneClass, str,  | The withdraw function to use on-chain. | [optional] 
**starkKey** | None, str,  | NoneClass, str,  | The user&#x27;s public STARK key | [optional] 
**assetType** | None, str,  | NoneClass, str,  | The asset type identifier. | [optional] 
**tokenId** | None, str,  | NoneClass, str,  | The token Id for ERC-721 and ERC-1155 assets. | [optional] 
**mintingBlob** | None, str,  | NoneClass, str,  | The minting blob for Mintable ERC-20, ERC-721 and ERC-1155 assets. | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

