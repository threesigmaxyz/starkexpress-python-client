# starkexpress_api.model.register_user_model.RegisterUserModel

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**address** | str,  | str,  | The Ethereum address associated with the user. | 
**starkSignature** | [**SignatureModel**](SignatureModel.md) | [**SignatureModel**](SignatureModel.md) |  | 
**eip712Signature** | str,  | str,  | The EIP-712 Signature of the Username, Stark Key and Address. | 
**starkKey** | str,  | str,  | The STARK key of the user. | 
**username** | str,  | str,  | The username of the user. | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

