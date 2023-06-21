# starkexpress_api.model.mint_data_model.MintDataModel

Model containing information to mint an asset.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Model containing information to mint an asset. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**amount** | str,  | str,  | The amount of the asset to be minted. | 
**mintingBlob** | str,  | str,  | The hexadecimal string representation of the data to be associated with the asset being minted. | 
**assetId** | str, uuid.UUID,  | str,  | The unique identifier of the asset being minted. | value must be a uuid
**dataAvailabilityMode** | [**DataAvailabilityModes**](DataAvailabilityModes.md) | [**DataAvailabilityModes**](DataAvailabilityModes.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

