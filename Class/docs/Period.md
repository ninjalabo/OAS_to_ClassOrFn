# Period


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_of_period** | **datetime** |  | [optional] 
**end_of_period** | **datetime** |  | [optional] 
**period_name** | [**MultilingualString**](MultilingualString.md) |  | [optional] 
**recurring_time_period_of_daies** | [**List[TimePeriodOfDay]**](TimePeriodOfDay.md) |  | [optional] 
**recurring_day_week_month_periods** | [**List[DayWeekMonth]**](DayWeekMonth.md) |  | [optional] 
**recurring_special_daies** | [**List[SpecialDay]**](SpecialDay.md) |  | [optional] 
**get_period_extension** | [**ExtensionType**](ExtensionType.md) |  | [optional] 

## Example

```python
from openapi_client.models.period import Period

# TODO update the JSON string below
json = "{}"
# create an instance of Period from a JSON string
period_instance = Period.from_json(json)
# print the JSON string representation of the object
print(Period.to_json())

# convert the object into a dict
period_dict = period_instance.to_dict()
# create an instance of Period from a dict
period_from_dict = Period.from_dict(period_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


