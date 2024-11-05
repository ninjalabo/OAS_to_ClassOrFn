# WeekdayTimePeriodV1

Weekday time period

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**weekday** | **str** | Weekday | 
**start_time** | [**LocalTime**](LocalTime.md) |  | 
**end_time** | [**LocalTime**](LocalTime.md) |  | 

## Example

```python
from openapi_client.models.weekday_time_period_v1 import WeekdayTimePeriodV1

# TODO update the JSON string below
json = "{}"
# create an instance of WeekdayTimePeriodV1 from a JSON string
weekday_time_period_v1_instance = WeekdayTimePeriodV1.from_json(json)
# print the JSON string representation of the object
print(WeekdayTimePeriodV1.to_json())

# convert the object into a dict
weekday_time_period_v1_dict = weekday_time_period_v1_instance.to_dict()
# create an instance of WeekdayTimePeriodV1 from a dict
weekday_time_period_v1_from_dict = WeekdayTimePeriodV1.from_dict(weekday_time_period_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


