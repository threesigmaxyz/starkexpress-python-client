# starkexpress_api.model.orderbook_level1_data_dto.OrderbookLevel1DataDto

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**orderbookId** | str, uuid.UUID,  | str,  | The ID of the orderbook. | [optional] value must be a uuid
**bidPrice** | decimal.Decimal, int, float,  | decimal.Decimal,  | The highest posted price where someone is willing to buy an asset. | [optional] value must be a 64 bit float
**bidSize** | str,  | str,  | The number of asset shares that users are trying to buy at the bid price. | [optional] 
**askPrice** | decimal.Decimal, int, float,  | decimal.Decimal,  | The lowest posted price where someone is willing to sell an asset. | [optional] value must be a 64 bit float
**askSize** | str,  | str,  | The number of asset shares that users are trying to sell at the bid ask. | [optional] 
**lastPrice** | decimal.Decimal, int, float,  | decimal.Decimal,  | The price at which the last transaction occurred. | [optional] value must be a 64 bit float
**lastSize** | str,  | str,  | The number of asset shares involved in the last transaction. | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

