# WeathercamStationPresetsPublicityHistoryV1

Weathercam station presets publicity changes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id of the road station | 
**data_updated_time** | **datetime** | Time when data was last updated | [optional] 
**presets** | [**List[WeathercamPresetPublicityHistoryV1]**](WeathercamPresetPublicityHistoryV1.md) | Id of the weathercam station | 

## Example

```python
from openapi_client.models.weathercam_station_presets_publicity_history_v1 import WeathercamStationPresetsPublicityHistoryV1

# TODO update the JSON string below
json = "{}"
# create an instance of WeathercamStationPresetsPublicityHistoryV1 from a JSON string
weathercam_station_presets_publicity_history_v1_instance = WeathercamStationPresetsPublicityHistoryV1.from_json(json)
# print the JSON string representation of the object
print(WeathercamStationPresetsPublicityHistoryV1.to_json())

# convert the object into a dict
weathercam_station_presets_publicity_history_v1_dict = weathercam_station_presets_publicity_history_v1_instance.to_dict()
# create an instance of WeathercamStationPresetsPublicityHistoryV1 from a dict
weathercam_station_presets_publicity_history_v1_from_dict = WeathercamStationPresetsPublicityHistoryV1.from_dict(weathercam_station_presets_publicity_history_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


