# DayWeekMonth


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applicable_daies** | [**List[DayEnum]**](DayEnum.md) |  | [optional] 
**applicable_months** | [**List[MonthOfYearEnum]**](MonthOfYearEnum.md) |  | [optional] 
**get_day_week_month_extension** | [**ExtensionType**](ExtensionType.md) |  | [optional] 

## Example

```python
from openapi_client.models.day_week_month import DayWeekMonth

# TODO update the JSON string below
json = "{}"
# create an instance of DayWeekMonth from a JSON string
day_week_month_instance = DayWeekMonth.from_json(json)
# print the JSON string representation of the object
print(DayWeekMonth.to_json())

# convert the object into a dict
day_week_month_dict = day_week_month_instance.to_dict()
# create an instance of DayWeekMonth from a dict
day_week_month_from_dict = DayWeekMonth.from_dict(day_week_month_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


