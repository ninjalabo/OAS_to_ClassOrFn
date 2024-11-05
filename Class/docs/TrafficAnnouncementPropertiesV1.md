# TrafficAnnouncementPropertiesV1

Traffic Announcement properties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**situation_id** | **str** | Situation id | 
**situation_type** | [**SituationTypeV1**](SituationTypeV1.md) |  | 
**traffic_announcement_type** | **str** | Traffic Announcement type | [optional] 
**version** | **int** | Announcement version | 
**release_time** | **datetime** | Announcement release time | 
**version_time** | **datetime** | Announcement version time | 
**announcements** | [**List[TrafficAnnouncementV1]**](TrafficAnnouncementV1.md) | Contains announcement&#39;s different language versions available. | 
**contact** | [**ContactV1**](ContactV1.md) |  | [optional] 
**data_updated_time** | **datetime** | Data last updated date time | 

## Example

```python
from openapi_client.models.traffic_announcement_properties_v1 import TrafficAnnouncementPropertiesV1

# TODO update the JSON string below
json = "{}"
# create an instance of TrafficAnnouncementPropertiesV1 from a JSON string
traffic_announcement_properties_v1_instance = TrafficAnnouncementPropertiesV1.from_json(json)
# print the JSON string representation of the object
print(TrafficAnnouncementPropertiesV1.to_json())

# convert the object into a dict
traffic_announcement_properties_v1_dict = traffic_announcement_properties_v1_instance.to_dict()
# create an instance of TrafficAnnouncementPropertiesV1 from a dict
traffic_announcement_properties_v1_from_dict = TrafficAnnouncementPropertiesV1.from_dict(traffic_announcement_properties_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


