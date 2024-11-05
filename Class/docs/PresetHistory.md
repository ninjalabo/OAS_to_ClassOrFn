# PresetHistory

Weather camera preset's image history.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id of the road station | 
**data_updated_time** | **datetime** | Time when data was last updated | [optional] 
**presets** | [**List[WeathercamPresetHistoryDtoV1]**](WeathercamPresetHistoryDtoV1.md) | Weathercam presets histories | 

## Example

```python
from openapi_client.models.preset_history import PresetHistory

# TODO update the JSON string below
json = "{}"
# create an instance of PresetHistory from a JSON string
preset_history_instance = PresetHistory.from_json(json)
# print the JSON string representation of the object
print(PresetHistory.to_json())

# convert the object into a dict
preset_history_dict = preset_history_instance.to_dict()
# create an instance of PresetHistory from a dict
preset_history_from_dict = PresetHistory.from_dict(preset_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


