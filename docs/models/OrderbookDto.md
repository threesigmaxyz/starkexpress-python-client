# starkexpress_api.model.orderbook_dto.OrderbookDto

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**orderbookId** | str, uuid.UUID,  | str,  | The ID of the orderbook. | [optional] value must be a uuid
**symbol** | None, str,  | NoneClass, str,  | The orderbook symbol. | [optional] 
**baseAsset** | [**OrderbookAssetDto**](OrderbookAssetDto.md) | [**OrderbookAssetDto**](OrderbookAssetDto.md) |  | [optional] 
**quoteAsset** | [**OrderbookAssetDto**](OrderbookAssetDto.md) | [**OrderbookAssetDto**](OrderbookAssetDto.md) |  | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

