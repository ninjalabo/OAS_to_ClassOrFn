# TimePeriodOfDay


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_time_of_period** | **datetime** |  | 
**end_time_of_period** | **datetime** |  | 
**get_time_period_of_day_extension** | [**ExtensionType**](ExtensionType.md) |  | [optional] 

## Example

```python
from openapi_client.models.time_period_of_day import TimePeriodOfDay

# TODO update the JSON string below
json = "{}"
# create an instance of TimePeriodOfDay from a JSON string
time_period_of_day_instance = TimePeriodOfDay.from_json(json)
# print the JSON string representation of the object
print(TimePeriodOfDay.to_json())

# convert the object into a dict
time_period_of_day_dict = time_period_of_day_instance.to_dict()
# create an instance of TimePeriodOfDay from a dict
time_period_of_day_from_dict = TimePeriodOfDay.from_dict(time_period_of_day_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


