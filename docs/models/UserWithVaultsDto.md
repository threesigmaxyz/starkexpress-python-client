# starkexpress_api.model.user_with_vaults_dto.UserWithVaultsDto

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**user** | [**UserDto**](UserDto.md) | [**UserDto**](UserDto.md) |  | [optional] 
**[vaultsPerAsset](#vaultsPerAsset)** | dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | The user vaults grouped by the asset id. | [optional] 

# vaultsPerAsset

The user vaults grouped by the asset id.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | The user vaults grouped by the asset id. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[any_string_name](#any_string_name)** | list, tuple,  | tuple,  | any string name can be used but the value must be the correct type | [optional] 

# any_string_name

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**VaultDto**](VaultDto.md) | [**VaultDto**](VaultDto.md) | [**VaultDto**](VaultDto.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

