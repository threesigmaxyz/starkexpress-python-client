# starkexpress_api.model.vault_dto_paginated_response_dto.VaultDtoPaginatedResponseDto

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[data](#data)** | list, tuple, None,  | tuple, NoneClass,  | The data in the paginated response. | [optional] 
**pagination** | [**PaginationDto**](PaginationDto.md) | [**PaginationDto**](PaginationDto.md) |  | [optional] 
**totalCount** | decimal.Decimal, int,  | decimal.Decimal,  | The total count of results available. | [optional] value must be a 32 bit integer

# data

The data in the paginated response.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | The data in the paginated response. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**VaultDto**](VaultDto.md) | [**VaultDto**](VaultDto.md) | [**VaultDto**](VaultDto.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

