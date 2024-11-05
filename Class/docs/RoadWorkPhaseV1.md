# RoadWorkPhaseV1

A single phase in a larger road work

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | id | 
**location** | [**LocationV1**](LocationV1.md) |  | [optional] 
**location_details** | [**LocationDetailsV1**](LocationDetailsV1.md) |  | [optional] 
**working_hours** | [**List[WeekdayTimePeriodV1]**](WeekdayTimePeriodV1.md) | WorkingHours of an traffic situation announcement | 
**comment** | **str** | Free comment | [optional] 
**time_and_duration** | [**TimeAndDurationV1**](TimeAndDurationV1.md) |  | 
**work_types** | [**List[WorkTypeV1]**](WorkTypeV1.md) | The types of work that are carried out | [optional] 
**restrictions** | [**List[RestrictionV1]**](RestrictionV1.md) | Restrictions on traffic | [optional] 
**restrictions_liftable** | **bool** | Restrictions can be lifted for abnormal transports | [optional] 
**severity** | **str** | Severity of the disruption to traffic. How severely this road work phase disrupts traffic. LOW - no disruption, HIGH - disruption, HIGHEST - significant disruption | 
**slow_traffic_times** | [**List[WeekdayTimePeriodV1]**](WeekdayTimePeriodV1.md) | Time periods when the road work is expected to cause slow moving traffic. | [optional] 
**queuing_traffic_times** | [**List[WeekdayTimePeriodV1]**](WeekdayTimePeriodV1.md) | Time periods when the road work is expected to cause queuing of the traffic. | [optional] 

## Example

```python
from openapi_client.models.road_work_phase_v1 import RoadWorkPhaseV1

# TODO update the JSON string below
json = "{}"
# create an instance of RoadWorkPhaseV1 from a JSON string
road_work_phase_v1_instance = RoadWorkPhaseV1.from_json(json)
# print the JSON string representation of the object
print(RoadWorkPhaseV1.to_json())

# convert the object into a dict
road_work_phase_v1_dict = road_work_phase_v1_instance.to_dict()
# create an instance of RoadWorkPhaseV1 from a dict
road_work_phase_v1_from_dict = RoadWorkPhaseV1.from_dict(road_work_phase_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


