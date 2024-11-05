# FeatureV1

Characteristics and qualities of the situation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Feature name, e.g.black ice on road, or speed limit | 
**quantity** | **float** | Feature quantity, e.g. 30 in {speed limit, 30, km/h} | [optional] 
**unit** | **str** | Unit of the feature quantity, e.g. km/h in {speed limit, 30, km/h} | [optional] 
**description** | **str** | Further details of the feature, e.g. description of a detour | [optional] 
**time_and_duration** | [**TimeAndDurationV1**](TimeAndDurationV1.md) |  | [optional] 

## Example

```python
from openapi_client.models.feature_v1 import FeatureV1

# TODO update the JSON string below
json = "{}"
# create an instance of FeatureV1 from a JSON string
feature_v1_instance = FeatureV1.from_json(json)
# print the JSON string representation of the object
print(FeatureV1.to_json())

# convert the object into a dict
feature_v1_dict = feature_v1_instance.to_dict()
# create an instance of FeatureV1 from a dict
feature_v1_from_dict = FeatureV1.from_dict(feature_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


