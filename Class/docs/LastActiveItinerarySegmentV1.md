# LastActiveItinerarySegmentV1

The itinerary segment of this special transport that is or was last active.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_time** | **datetime** | The time when the transport may start this segment. | 
**end_time** | **datetime** | Time by which the transport has finished this segment. | 
**legs** | [**List[ItineraryLegV1]**](ItineraryLegV1.md) | Route legs. | 

## Example

```python
from openapi_client.models.last_active_itinerary_segment_v1 import LastActiveItinerarySegmentV1

# TODO update the JSON string below
json = "{}"
# create an instance of LastActiveItinerarySegmentV1 from a JSON string
last_active_itinerary_segment_v1_instance = LastActiveItinerarySegmentV1.from_json(json)
# print the JSON string representation of the object
print(LastActiveItinerarySegmentV1.to_json())

# convert the object into a dict
last_active_itinerary_segment_v1_dict = last_active_itinerary_segment_v1_instance.to_dict()
# create an instance of LastActiveItinerarySegmentV1 from a dict
last_active_itinerary_segment_v1_from_dict = LastActiveItinerarySegmentV1.from_dict(last_active_itinerary_segment_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


