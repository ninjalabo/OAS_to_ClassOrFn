# WeathercamStationsPresetsPublicityHistoryV1

Weathercam stations presets publicity changes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_updated_time** | **datetime** | Latest history change time. Use this value as parameter for next query in api. | [optional] 
**stations** | [**List[WeathercamStationPresetsPublicityHistoryV1]**](WeathercamStationPresetsPublicityHistoryV1.md) | Stations data | [optional] 

## Example

```python
from openapi_client.models.weathercam_stations_presets_publicity_history_v1 import WeathercamStationsPresetsPublicityHistoryV1

# TODO update the JSON string below
json = "{}"
# create an instance of WeathercamStationsPresetsPublicityHistoryV1 from a JSON string
weathercam_stations_presets_publicity_history_v1_instance = WeathercamStationsPresetsPublicityHistoryV1.from_json(json)
# print the JSON string representation of the object
print(WeathercamStationsPresetsPublicityHistoryV1.to_json())

# convert the object into a dict
weathercam_stations_presets_publicity_history_v1_dict = weathercam_stations_presets_publicity_history_v1_instance.to_dict()
# create an instance of WeathercamStationsPresetsPublicityHistoryV1 from a dict
weathercam_stations_presets_publicity_history_v1_from_dict = WeathercamStationsPresetsPublicityHistoryV1.from_dict(weathercam_stations_presets_publicity_history_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


