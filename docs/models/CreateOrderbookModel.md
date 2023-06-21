# starkexpress_api.model.create_orderbook_model.CreateOrderbookModel

Request model to create an orderbook.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Request model to create an orderbook. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**baseAssetId** | str, uuid.UUID,  | str,  | The ID of the orderbook base asset. | value must be a uuid
**quoteAssetPrecision** | decimal.Decimal, int,  | decimal.Decimal,  | The orderbook quote asset decimal precision. | value must be a 32 bit integer
**quoteAssetId** | str, uuid.UUID,  | str,  | The ID of the orderbook quote asset. | value must be a uuid
**baseAssetPrecision** | decimal.Decimal, int,  | decimal.Decimal,  | The orderbook base asset decimal precision. | value must be a 32 bit integer

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

