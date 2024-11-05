# CountersModel

GeoJson FeatureCollection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**features** | [**List[CounterFeatureModel]**](CounterFeatureModel.md) |  | 
**type** | **str** | FeatureCollection | 
**data_updated_time** | **datetime** | Data updated timestamp | [optional] 

## Example

```python
from openapi_client.models.counters_model import CountersModel

# TODO update the JSON string below
json = "{}"
# create an instance of CountersModel from a JSON string
counters_model_instance = CountersModel.from_json(json)
# print the JSON string representation of the object
print(CountersModel.to_json())

# convert the object into a dict
counters_model_dict = counters_model_instance.to_dict()
# create an instance of CountersModel from a dict
counters_model_from_dict = CountersModel.from_dict(counters_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


