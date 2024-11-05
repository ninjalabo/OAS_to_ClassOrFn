# RoadPointV1

A single road point

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**municipality** | **str** | City, town or village. | [optional] 
**province** | **str** | Province eq. Satakunta. | [optional] 
**country** | **str** | Usually Finland, but may be something else eq. Sweden, Norway, Russia. | [optional] 
**road_address** | [**TrafficMessageRoadAddressV1**](TrafficMessageRoadAddressV1.md) |  | 
**road_name** | **str** | Name of the road where the accident happened. | [optional] 
**alert_c_location** | [**AlertCLocationV1**](AlertCLocationV1.md) |  | 

## Example

```python
from openapi_client.models.road_point_v1 import RoadPointV1

# TODO update the JSON string below
json = "{}"
# create an instance of RoadPointV1 from a JSON string
road_point_v1_instance = RoadPointV1.from_json(json)
# print the JSON string representation of the object
print(RoadPointV1.to_json())

# convert the object into a dict
road_point_v1_dict = road_point_v1_instance.to_dict()
# create an instance of RoadPointV1 from a dict
road_point_v1_from_dict = RoadPointV1.from_dict(road_point_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


