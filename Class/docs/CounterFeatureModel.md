# CounterFeatureModel

GeoJson Feature

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**geometry** | **object** | GeoJSON geometry | 
**type** | **str** | Feature | 
**properties** | [**CounterModel**](CounterModel.md) |  | 

## Example

```python
from openapi_client.models.counter_feature_model import CounterFeatureModel

# TODO update the JSON string below
json = "{}"
# create an instance of CounterFeatureModel from a JSON string
counter_feature_model_instance = CounterFeatureModel.from_json(json)
# print the JSON string representation of the object
print(CounterFeatureModel.to_json())

# convert the object into a dict
counter_feature_model_dict = counter_feature_model_instance.to_dict()
# create an instance of CounterFeatureModel from a dict
counter_feature_model_from_dict = CounterFeatureModel.from_dict(counter_feature_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


