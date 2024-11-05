# LocationFeatureV1

Location GeoJSON feature object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | GeoJSON Object Type | 
**id** | **int** | Unique locationCode for this location | 
**geometry** | [**Point**](Point.md) |  | 
**properties** | [**LocationPropertiesV1**](LocationPropertiesV1.md) |  | 

## Example

```python
from openapi_client.models.location_feature_v1 import LocationFeatureV1

# TODO update the JSON string below
json = "{}"
# create an instance of LocationFeatureV1 from a JSON string
location_feature_v1_instance = LocationFeatureV1.from_json(json)
# print the JSON string representation of the object
print(LocationFeatureV1.to_json())

# convert the object into a dict
location_feature_v1_dict = location_feature_v1_instance.to_dict()
# create an instance of LocationFeatureV1 from a dict
location_feature_v1_from_dict = LocationFeatureV1.from_dict(location_feature_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


