# SpecialDay


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**intersect_with_applicable_days** | **bool** |  | [optional] 
**special_day_type** | [**SpecialDayTypeEnum**](SpecialDayTypeEnum.md) |  | 
**public_event** | [**PublicEventTypeEnum**](PublicEventTypeEnum.md) |  | [optional] 
**named_areas** | [**List[NamedArea]**](NamedArea.md) |  | [optional] 
**get_special_day_extension** | [**ExtensionType**](ExtensionType.md) |  | [optional] 

## Example

```python
from openapi_client.models.special_day import SpecialDay

# TODO update the JSON string below
json = "{}"
# create an instance of SpecialDay from a JSON string
special_day_instance = SpecialDay.from_json(json)
# print the JSON string representation of the object
print(SpecialDay.to_json())

# convert the object into a dict
special_day_dict = special_day_instance.to_dict()
# create an instance of SpecialDay from a dict
special_day_from_dict = SpecialDay.from_dict(special_day_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


