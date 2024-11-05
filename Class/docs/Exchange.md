# Exchange


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changed_flag** | **str** |  | [optional] 
**client_identification** | **str** |  | [optional] 
**delivery_break** | **bool** |  | [optional] 
**deny_reason** | **str** |  | [optional] 
**historical_start_date** | **datetime** |  | [optional] 
**historical_stop_date** | **datetime** |  | [optional] 
**keep_alive** | **bool** |  | [optional] 
**request_type** | **str** |  | [optional] 
**response** | **str** |  | [optional] 
**subscription_reference** | **str** |  | [optional] 
**supplier_identification** | [**InternationalIdentifier**](InternationalIdentifier.md) |  | 
**target** | [**Target**](Target.md) |  | [optional] 
**subscription** | [**Subscription**](Subscription.md) |  | [optional] 
**filter_references** | [**List[FilterReference]**](FilterReference.md) |  | [optional] 
**catalogue_references** | [**List[CatalogueReference]**](CatalogueReference.md) |  | [optional] 
**exchange_extension** | [**ExtensionType**](ExtensionType.md) |  | [optional] 

## Example

```python
from openapi_client.models.exchange import Exchange

# TODO update the JSON string below
json = "{}"
# create an instance of Exchange from a JSON string
exchange_instance = Exchange.from_json(json)
# print the JSON string representation of the object
print(Exchange.to_json())

# convert the object into a dict
exchange_dict = exchange_instance.to_dict()
# create an instance of Exchange from a dict
exchange_from_dict = Exchange.from_dict(exchange_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


