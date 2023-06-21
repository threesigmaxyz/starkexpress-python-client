# starkexpress_api.model.deploy_asset_model.DeployAssetModel

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**symbol** | str,  | str,  | The token&#x27;s symbol (eg. USDC). | 
**name** | str,  | str,  | The token&#x27;s name (eg. USD Coin). | 
**type** | [**AssetType**](AssetType.md) | [**AssetType**](AssetType.md) |  | 
**uri** | None, str,  | NoneClass, str,  | The token&#x27;s metadata uri (for ERC-721 and ERC-1155 tokens). | [optional] 
**quantum** | str,  | str,  | The token&#x27;s StarkEx asset quantum (for ERC-20 and ERC-1155 tokens). | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

