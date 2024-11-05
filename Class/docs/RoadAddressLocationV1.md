# RoadAddressLocationV1

Location consisting of a single road point or a road segment between two road points

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**primary_point** | [**RoadPointV1**](RoadPointV1.md) |  | 
**secondary_point** | [**RoadPointV1**](RoadPointV1.md) |  | [optional] 
**direction** | **str** | Affected road direction | 
**direction_description** | **str** | Human readable description of the affected direction | [optional] 

## Example

```python
from openapi_client.models.road_address_location_v1 import RoadAddressLocationV1

# TODO update the JSON string below
json = "{}"
# create an instance of RoadAddressLocationV1 from a JSON string
road_address_location_v1_instance = RoadAddressLocationV1.from_json(json)
# print the JSON string representation of the object
print(RoadAddressLocationV1.to_json())

# convert the object into a dict
road_address_location_v1_dict = road_address_location_v1_instance.to_dict()
# create an instance of RoadAddressLocationV1 from a dict
road_address_location_v1_from_dict = RoadAddressLocationV1.from_dict(road_address_location_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


