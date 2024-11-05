# VariableSignFeatureCollectionV1

GeoJSON Feature Collection of variable signs

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | GeoJSON Object Type | 
**data_updated_time** | **datetime** | Data last updated date time | 
**features** | [**List[VariableSignFeatureV1]**](VariableSignFeatureV1.md) | GeoJSON Feature Objects | 

## Example

```python
from openapi_client.models.variable_sign_feature_collection_v1 import VariableSignFeatureCollectionV1

# TODO update the JSON string below
json = "{}"
# create an instance of VariableSignFeatureCollectionV1 from a JSON string
variable_sign_feature_collection_v1_instance = VariableSignFeatureCollectionV1.from_json(json)
# print the JSON string representation of the object
print(VariableSignFeatureCollectionV1.to_json())

# convert the object into a dict
variable_sign_feature_collection_v1_dict = variable_sign_feature_collection_v1_instance.to_dict()
# create an instance of VariableSignFeatureCollectionV1 from a dict
variable_sign_feature_collection_v1_from_dict = VariableSignFeatureCollectionV1.from_dict(variable_sign_feature_collection_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


