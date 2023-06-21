# starkexpress_api.model.mint_request_data_model.MintRequestDataModel

Request model to mint a batch of assets.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Request model to mint a batch of assets. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[mints](#mints)** | list, tuple,  | tuple,  | The array of assets to mint for the user. | 
**userId** | str, uuid.UUID,  | str,  | The ID of the user for which the assets should be minted. | value must be a uuid

# mints

The array of assets to mint for the user.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The array of assets to mint for the user. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**MintDataModel**](MintDataModel.md) | [**MintDataModel**](MintDataModel.md) | [**MintDataModel**](MintDataModel.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

