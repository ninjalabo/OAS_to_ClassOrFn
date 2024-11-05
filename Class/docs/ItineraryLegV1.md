# ItineraryLegV1

ItineraryLeg is one leg of the route

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**road_leg** | [**ItineraryRoadLegV1**](ItineraryRoadLegV1.md) |  | [optional] 
**street_name** | **str** | Name of the street if leg is on the street network | [optional] 

## Example

```python
from openapi_client.models.itinerary_leg_v1 import ItineraryLegV1

# TODO update the JSON string below
json = "{}"
# create an instance of ItineraryLegV1 from a JSON string
itinerary_leg_v1_instance = ItineraryLegV1.from_json(json)
# print the JSON string representation of the object
print(ItineraryLegV1.to_json())

# convert the object into a dict
itinerary_leg_v1_dict = itinerary_leg_v1_instance.to_dict()
# create an instance of ItineraryLegV1 from a dict
itinerary_leg_v1_from_dict = ItineraryLegV1.from_dict(itinerary_leg_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


