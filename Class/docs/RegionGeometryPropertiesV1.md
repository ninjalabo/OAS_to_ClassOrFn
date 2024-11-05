# RegionGeometryPropertiesV1

Region geometry properties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location_code** | **int** | The Alert-C code of the region | 
**name** | **str** | The name of the region | 
**type** | [**AreaTypeV1**](AreaTypeV1.md) |  | 
**effective_date** | **datetime** | The moment, when the data comes into effect | 

## Example

```python
from openapi_client.models.region_geometry_properties_v1 import RegionGeometryPropertiesV1

# TODO update the JSON string below
json = "{}"
# create an instance of RegionGeometryPropertiesV1 from a JSON string
region_geometry_properties_v1_instance = RegionGeometryPropertiesV1.from_json(json)
# print the JSON string representation of the object
print(RegionGeometryPropertiesV1.to_json())

# convert the object into a dict
region_geometry_properties_v1_dict = region_geometry_properties_v1_instance.to_dict()
# create an instance of RegionGeometryPropertiesV1 from a dict
region_geometry_properties_v1_from_dict = RegionGeometryPropertiesV1.from_dict(region_geometry_properties_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


