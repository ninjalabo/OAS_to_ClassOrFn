# VariableSignFeatureV1

GeoJSON Feature Object of variable sign

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | GeoJSON Object Type | 
**geometry** | [**Point**](Point.md) |  | 
**properties** | [**VariableSignPropertiesV1**](VariableSignPropertiesV1.md) |  | 

## Example

```python
from openapi_client.models.variable_sign_feature_v1 import VariableSignFeatureV1

# TODO update the JSON string below
json = "{}"
# create an instance of VariableSignFeatureV1 from a JSON string
variable_sign_feature_v1_instance = VariableSignFeatureV1.from_json(json)
# print the JSON string representation of the object
print(VariableSignFeatureV1.to_json())

# convert the object into a dict
variable_sign_feature_v1_dict = variable_sign_feature_v1_instance.to_dict()
# create an instance of VariableSignFeatureV1 from a dict
variable_sign_feature_v1_from_dict = VariableSignFeatureV1.from_dict(variable_sign_feature_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


