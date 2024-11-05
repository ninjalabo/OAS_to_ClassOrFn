# TimeAndDurationV1

Announcement time and duration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_time** | **datetime** | Start time of the situation | 
**end_time** | **datetime** | End time of the situation. If the end time has been passed, the situation can be assumed to be over. If end time is not given, there will be follow-up announcement about the situation. | [optional] 
**estimated_duration** | [**EstimatedDurationV1**](EstimatedDurationV1.md) |  | [optional] 

## Example

```python
from openapi_client.models.time_and_duration_v1 import TimeAndDurationV1

# TODO update the JSON string below
json = "{}"
# create an instance of TimeAndDurationV1 from a JSON string
time_and_duration_v1_instance = TimeAndDurationV1.from_json(json)
# print the JSON string representation of the object
print(TimeAndDurationV1.to_json())

# convert the object into a dict
time_and_duration_v1_dict = time_and_duration_v1_instance.to_dict()
# create an instance of TimeAndDurationV1 from a dict
time_and_duration_v1_from_dict = TimeAndDurationV1.from_dict(time_and_duration_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


