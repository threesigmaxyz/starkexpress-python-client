# starkexpress_api.model.deposit_details_dto.DepositDetailsDto

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**operatorContractAddress** | None, str,  | NoneClass, str,  | The smart contract address that processes on-chain deposits. | [optional] 
**assetContractAddress** | None, str,  | NoneClass, str,  | The asset&#x27;s smart contract address. | [optional] 
**depositFunction** | None, str,  | NoneClass, str,  | The deposit function to use on-chain. | [optional] 
**starkKey** | None, str,  | NoneClass, str,  | The user&#x27;s public STARK key | [optional] 
**assetType** | None, str,  | NoneClass, str,  | The asset type identifier. | [optional] 
**tokenId** | None, str,  | NoneClass, str,  | The token Id for ERC-721 and ERC-1155 assets. | [optional] 
**vaultId** | str,  | str,  | The user&#x27;s vault id. | [optional] 
**quantizedAmount** | None, str,  | NoneClass, str,  | The quantized amount to deposit ERC-20 and ERC-1155 assets. | [optional] 
**amount** | None, str,  | NoneClass, str,  | The amount to deposit ETH. | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

