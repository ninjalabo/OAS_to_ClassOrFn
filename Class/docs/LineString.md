# LineString

GeoJson LineString Geometry Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**coordinates** | **List[List[float]]** | An array of Point coordinates. Coordinates are in WGS84 format in decimal degrees: [LONGITUDE, LATITUDE, {ALTITUDE}]. Altitude is optional and measured in meters. | 

## Example

```python
from openapi_client.models.line_string import LineString

# TODO update the JSON string below
json = "{}"
# create an instance of LineString from a JSON string
line_string_instance = LineString.from_json(json)
# print the JSON string representation of the object
print(LineString.to_json())

# convert the object into a dict
line_string_dict = line_string_instance.to_dict()
# create an instance of LineString from a dict
line_string_from_dict = LineString.from_dict(line_string_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


