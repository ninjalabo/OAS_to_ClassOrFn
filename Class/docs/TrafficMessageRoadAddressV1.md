# TrafficMessageRoadAddressV1

Location in road address (road number + number of the road section + distance from the beginning of the road section

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**road** | **int** | Number of the road | 
**road_section** | **int** | Number of the road section | 
**distance** | **int** | Distance from the beginning of the road section. | 

## Example

```python
from openapi_client.models.traffic_message_road_address_v1 import TrafficMessageRoadAddressV1

# TODO update the JSON string below
json = "{}"
# create an instance of TrafficMessageRoadAddressV1 from a JSON string
traffic_message_road_address_v1_instance = TrafficMessageRoadAddressV1.from_json(json)
# print the JSON string representation of the object
print(TrafficMessageRoadAddressV1.to_json())

# convert the object into a dict
traffic_message_road_address_v1_dict = traffic_message_road_address_v1_instance.to_dict()
# create an instance of TrafficMessageRoadAddressV1 from a dict
traffic_message_road_address_v1_from_dict = TrafficMessageRoadAddressV1.from_dict(traffic_message_road_address_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


