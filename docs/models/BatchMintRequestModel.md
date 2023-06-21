# starkexpress_api.model.batch_mint_request_model.BatchMintRequestModel

Request model to mint a batch of assets.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Request model to mint a batch of assets. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[users](#users)** | list, tuple,  | tuple,  | The array of assets to mint grouped by user. | 

# users

The array of assets to mint grouped by user.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The array of assets to mint grouped by user. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**MintRequestDataModel**](MintRequestDataModel.md) | [**MintRequestDataModel**](MintRequestDataModel.md) | [**MintRequestDataModel**](MintRequestDataModel.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

