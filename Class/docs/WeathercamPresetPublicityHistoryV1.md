# WeathercamPresetPublicityHistoryV1

Weathercam station preset's publicity changes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id of the weathercam preset | 
**measured_time** | **datetime** | The time when change took place. Same as the last modified date of the related image version. | [optional] 
**publishable_to** | **bool** | New state for publicity | [optional] 
**modified_time** | **datetime** | Modification time of the history. | [optional] 

## Example

```python
from openapi_client.models.weathercam_preset_publicity_history_v1 import WeathercamPresetPublicityHistoryV1

# TODO update the JSON string below
json = "{}"
# create an instance of WeathercamPresetPublicityHistoryV1 from a JSON string
weathercam_preset_publicity_history_v1_instance = WeathercamPresetPublicityHistoryV1.from_json(json)
# print the JSON string representation of the object
print(WeathercamPresetPublicityHistoryV1.to_json())

# convert the object into a dict
weathercam_preset_publicity_history_v1_dict = weathercam_preset_publicity_history_v1_instance.to_dict()
# create an instance of WeathercamPresetPublicityHistoryV1 from a dict
weathercam_preset_publicity_history_v1_from_dict = WeathercamPresetPublicityHistoryV1.from_dict(weathercam_preset_publicity_history_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


