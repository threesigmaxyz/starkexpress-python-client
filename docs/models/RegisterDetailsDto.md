# starkexpress_api.model.register_details_dto.RegisterDetailsDto

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**domain** | [**DomainDto**](DomainDto.md) | [**DomainDto**](DomainDto.md) |  | [optional] 
**[types](#types)** | dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | The types in the EIP712 message. | [optional] 
**primaryType** | None, str,  | NoneClass, str,  | The message primary type. | [optional] 
**[message](#message)** | list, tuple, None,  | tuple, NoneClass,  | The register details message to be signed. | [optional] 
**[domainRawValues](#domainRawValues)** | list, tuple, None,  | tuple, NoneClass,  | The STARK key of the sender. | [optional] 

# types

The types in the EIP712 message.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | The types in the EIP712 message. | 

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
[**MemberDescriptionDto**](MemberDescriptionDto.md) | [**MemberDescriptionDto**](MemberDescriptionDto.md) | [**MemberDescriptionDto**](MemberDescriptionDto.md) |  | 

# message

The register details message to be signed.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | The register details message to be signed. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**MemberValueDto**](MemberValueDto.md) | [**MemberValueDto**](MemberValueDto.md) | [**MemberValueDto**](MemberValueDto.md) |  | 

# domainRawValues

The STARK key of the sender.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | The STARK key of the sender. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**MemberValueDto**](MemberValueDto.md) | [**MemberValueDto**](MemberValueDto.md) | [**MemberValueDto**](MemberValueDto.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

