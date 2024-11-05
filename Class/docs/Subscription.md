# Subscription


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delete_subscription** | **bool** |  | [optional] 
**delivery_interval** | **float** |  | [optional] 
**operating_mode** | **str** |  | 
**subscription_start_time** | **datetime** |  | 
**subscription_state** | **str** |  | 
**subscription_stop_time** | **datetime** |  | [optional] 
**update_method** | **str** |  | 
**targets** | [**List[Target]**](Target.md) |  | 
**filter_reference** | [**FilterReference**](FilterReference.md) |  | [optional] 
**catalogue_reference** | [**CatalogueReference**](CatalogueReference.md) |  | [optional] 
**subscription_extension** | [**ExtensionType**](ExtensionType.md) |  | [optional] 

## Example

```python
from openapi_client.models.subscription import Subscription

# TODO update the JSON string below
json = "{}"
# create an instance of Subscription from a JSON string
subscription_instance = Subscription.from_json(json)
# print the JSON string representation of the object
print(Subscription.to_json())

# convert the object into a dict
subscription_dict = subscription_instance.to_dict()
# create an instance of Subscription from a dict
subscription_from_dict = Subscription.from_dict(subscription_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


