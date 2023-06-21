# starkexpress_api.model.orderbook_level2_data_dto.OrderbookLevel2DataDto

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**orderbookId** | str, uuid.UUID,  | str,  | The ID of the orderbook. | [optional] value must be a uuid
**[bids](#bids)** | list, tuple, None,  | tuple, NoneClass,  | The orderbook bids. | [optional] 
**[asks](#asks)** | list, tuple, None,  | tuple, NoneClass,  | The orderbook asks. | [optional] 

# bids

The orderbook bids.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | The orderbook bids. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**OrderbookLevel2EntryDto**](OrderbookLevel2EntryDto.md) | [**OrderbookLevel2EntryDto**](OrderbookLevel2EntryDto.md) | [**OrderbookLevel2EntryDto**](OrderbookLevel2EntryDto.md) |  | 

# asks

The orderbook asks.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | The orderbook asks. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**OrderbookLevel2EntryDto**](OrderbookLevel2EntryDto.md) | [**OrderbookLevel2EntryDto**](OrderbookLevel2EntryDto.md) | [**OrderbookLevel2EntryDto**](OrderbookLevel2EntryDto.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

