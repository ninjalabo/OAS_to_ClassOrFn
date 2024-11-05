# RoadSegmentDtoV1

Forecast section road segments. Refers to https://aineistot.vayla.fi/digiroad/

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_distance** | **int** | Road segment start distance | [optional] 
**end_distance** | **int** | Road segment end distance | [optional] 
**carriageway** | **int** | Road segment carriageway | [optional] 

## Example

```python
from openapi_client.models.road_segment_dto_v1 import RoadSegmentDtoV1

# TODO update the JSON string below
json = "{}"
# create an instance of RoadSegmentDtoV1 from a JSON string
road_segment_dto_v1_instance = RoadSegmentDtoV1.from_json(json)
# print the JSON string representation of the object
print(RoadSegmentDtoV1.to_json())

# convert the object into a dict
road_segment_dto_v1_dict = road_segment_dto_v1_instance.to_dict()
# create an instance of RoadSegmentDtoV1 from a dict
road_segment_dto_v1_from_dict = RoadSegmentDtoV1.from_dict(road_segment_dto_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


