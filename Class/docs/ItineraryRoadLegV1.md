# ItineraryRoadLegV1

ItineraryRoadLeg is route leg that is on the road network.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**road_number** | **int** | Number of the road. | [optional] 
**road_name** | **str** | Name of the road. | [optional] 
**start_area** | **str** | Description of the place on the road, where this leg starts. | [optional] 
**end_area** | **str** | Description of the place on the road, where this leg ends. | [optional] 

## Example

```python
from openapi_client.models.itinerary_road_leg_v1 import ItineraryRoadLegV1

# TODO update the JSON string below
json = "{}"
# create an instance of ItineraryRoadLegV1 from a JSON string
itinerary_road_leg_v1_instance = ItineraryRoadLegV1.from_json(json)
# print the JSON string representation of the object
print(ItineraryRoadLegV1.to_json())

# convert the object into a dict
itinerary_road_leg_v1_dict = itinerary_road_leg_v1_instance.to_dict()
# create an instance of ItineraryRoadLegV1 from a dict
itinerary_road_leg_v1_from_dict = ItineraryRoadLegV1.from_dict(itinerary_road_leg_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


