# Polygon

GeoJson Polygon Geometry Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**coordinates** | **List[List[List[float]]]** | An array of LinearRing coordinates. Coordinates are in WGS84 format in decimal degrees: [LONGITUDE, LATITUDE, {ALTITUDE}]. Altitude is optional and measured in meters. | 

## Example

```python
from openapi_client.models.polygon import Polygon

# TODO update the JSON string below
json = "{}"
# create an instance of Polygon from a JSON string
polygon_instance = Polygon.from_json(json)
# print the JSON string representation of the object
print(Polygon.to_json())

# convert the object into a dict
polygon_dict = polygon_instance.to_dict()
# create an instance of Polygon from a dict
polygon_from_dict = Polygon.from_dict(polygon_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


