# GeometryObject

GeoJson Geometry Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | GeoJson Geometry Object type | 
**coordinates** | **List[object]** | GeoJson Geometry Object coordinates | 

## Example

```python
from openapi_client.models.geometry_object import GeometryObject

# TODO update the JSON string below
json = "{}"
# create an instance of GeometryObject from a JSON string
geometry_object_instance = GeometryObject.from_json(json)
# print the JSON string representation of the object
print(GeometryObject.to_json())

# convert the object into a dict
geometry_object_dict = geometry_object_instance.to_dict()
# create an instance of GeometryObject from a dict
geometry_object_from_dict = GeometryObject.from_dict(geometry_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


