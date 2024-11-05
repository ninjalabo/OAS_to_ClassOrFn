# TrafficAnnouncementV1

Announcement time and duration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language** | **str** | Language of the announcement, always fi. A subset of ISO 639-1 in upper case. | 
**title** | **str** | Short description about the situation | 
**location** | [**LocationV1**](LocationV1.md) |  | [optional] 
**location_details** | [**LocationDetailsV1**](LocationDetailsV1.md) |  | [optional] 
**features** | [**List[FeatureV1]**](FeatureV1.md) | Features of the announcement | [optional] 
**road_work_phases** | [**List[RoadWorkPhaseV1]**](RoadWorkPhaseV1.md) | Contains the phases of this road maintenance work | [optional] 
**early_closing** | **str** | Road work was closed before the planned time. &#39;CLOSED&#39; means the road work closed after its start time, possibly skipping some phases. &#39;CANCELED&#39; means the road work was canceled before its start time. Note: This field is null if the road work closes normally. | [optional] 
**comment** | **str** | Free comment | [optional] 
**time_and_duration** | [**TimeAndDurationV1**](TimeAndDurationV1.md) |  | [optional] 
**additional_information** | **str** | Additional information. | [optional] 
**sender** | **str** | Name of the sender | 
**last_active_itinerary_segment** | [**LastActiveItinerarySegmentV1**](LastActiveItinerarySegmentV1.md) |  | [optional] 

## Example

```python
from openapi_client.models.traffic_announcement_v1 import TrafficAnnouncementV1

# TODO update the JSON string below
json = "{}"
# create an instance of TrafficAnnouncementV1 from a JSON string
traffic_announcement_v1_instance = TrafficAnnouncementV1.from_json(json)
# print the JSON string representation of the object
print(TrafficAnnouncementV1.to_json())

# convert the object into a dict
traffic_announcement_v1_dict = traffic_announcement_v1_instance.to_dict()
# create an instance of TrafficAnnouncementV1 from a dict
traffic_announcement_v1_from_dict = TrafficAnnouncementV1.from_dict(traffic_announcement_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


