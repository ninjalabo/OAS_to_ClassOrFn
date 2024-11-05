# LocationPropertiesV1

Location GeoJSON properties object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location_code** | **int** | Unique locationCode for this location | 
**subtype_code** | **str** | Code of location subtype | 
**road_junction** | **str** | Roadnumber for roads. Junctionno: the numbering of exits has only just begun on the very limited Finnish motorway network. The exit numbers will be included. NOTE: the roads, segments and points are not sorted in ascending order | [optional] 
**road_name** | **str** | Roadname if exists, L5.0 always have road name | [optional] 
**first_name** | **str** | For roads and segments this is the name of the starting point. For all other objects (linear (streets), area and point) this is the name of the object | 
**second_name** | **str** | For roads and segments this is the name of the ending point. For point locations the number of the intersecting road | [optional] 
**area_ref** | **int** | Code of the upper order administrative area | [optional] 
**linear_ref** | **int** | For segments and point locations. Describes the code of the segment which these objects belong to. If there are no segments on the road the location code of the road is given instead | [optional] 
**neg_offset** | **int** | For segments and point locations. Segments: describes the code of previous segment on that road. For the first segment on the road this code is 0. Points: describes the code of previous point on that road. For the starting point this code is 0 | [optional] 
**pos_offset** | **int** | For segments and point locations. Segments: describes the code of next segment on that road. For the last segment on the road this code is 0. Points: describes the code of next point on that road. For the last point this code is 0 | [optional] 
**urban** | **bool** | Indicates whether a point is within the city limits (1) or not (0). NOTE: Not actively entered yet | [optional] 
**coordinates_etrs89** | **List[float]** | Point coordinates (LONGITUDE, LATITUDE). Coordinates are in ETRS89 / ETRS-TM35FIN format. | [optional] 
**neg_direction** | **str** | For all L5.0 and for some roads. Text to be used when the incident has an effect only on vehicles driving in the negative direction of the road. ( e.g. Ring 1 westbound) | [optional] 
**pos_direction** | **str** | For all L5.0 and for some roads. Text to be used when the incident has an effect only on vehicles driving in the positive direction of the road. ( e.g. Ring 1 eastbound) | [optional] 
**geocode** | **str** | Point location according to Finnish Transport Agency’s official addressing where Locations on road network are addressed as: Road number;Road part number;Carriageway; Distance from the beginning of the road part | [optional] 
**order_of_point** | **str** | The order of point within line or segment feature | [optional] 
**data_updated_time** | **datetime** | Data last updated time | 
**location_version** | **str** | Location version | [optional] 

## Example

```python
from openapi_client.models.location_properties_v1 import LocationPropertiesV1

# TODO update the JSON string below
json = "{}"
# create an instance of LocationPropertiesV1 from a JSON string
location_properties_v1_instance = LocationPropertiesV1.from_json(json)
# print the JSON string representation of the object
print(LocationPropertiesV1.to_json())

# convert the object into a dict
location_properties_v1_dict = location_properties_v1_instance.to_dict()
# create an instance of LocationPropertiesV1 from a dict
location_properties_v1_from_dict = LocationPropertiesV1.from_dict(location_properties_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


