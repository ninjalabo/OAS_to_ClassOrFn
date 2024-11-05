# WeathercamPresetHistoryDtoV1

Weather camera preset's image history.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Weathercam preset&#39;s id | 
**data_updated_time** | **datetime** | Time when data was last updated | [optional] 
**history** | [**List[WeathercamPresetHistoryItemDtoV1]**](WeathercamPresetHistoryItemDtoV1.md) | Weathercam preset&#39;s history | 

## Example

```python
from openapi_client.models.weathercam_preset_history_dto_v1 import WeathercamPresetHistoryDtoV1

# TODO update the JSON string below
json = "{}"
# create an instance of WeathercamPresetHistoryDtoV1 from a JSON string
weathercam_preset_history_dto_v1_instance = WeathercamPresetHistoryDtoV1.from_json(json)
# print the JSON string representation of the object
print(WeathercamPresetHistoryDtoV1.to_json())

# convert the object into a dict
weathercam_preset_history_dto_v1_dict = weathercam_preset_history_dto_v1_instance.to_dict()
# create an instance of WeathercamPresetHistoryDtoV1 from a dict
weathercam_preset_history_dto_v1_from_dict = WeathercamPresetHistoryDtoV1.from_dict(weathercam_preset_history_dto_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


