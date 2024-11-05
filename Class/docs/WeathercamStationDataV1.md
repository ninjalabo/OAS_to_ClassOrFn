# WeathercamStationDataV1

Weathercam stations' data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id of the road station | 
**data_updated_time** | **datetime** | Time when data was last updated | [optional] 
**presets** | [**List[WeathercamPresetDataV1]**](WeathercamPresetDataV1.md) | Weathercam presets data | 

## Example

```python
from openapi_client.models.weathercam_station_data_v1 import WeathercamStationDataV1

# TODO update the JSON string below
json = "{}"
# create an instance of WeathercamStationDataV1 from a JSON string
weathercam_station_data_v1_instance = WeathercamStationDataV1.from_json(json)
# print the JSON string representation of the object
print(WeathercamStationDataV1.to_json())

# convert the object into a dict
weathercam_station_data_v1_dict = weathercam_station_data_v1_instance.to_dict()
# create an instance of WeathercamStationDataV1 from a dict
weathercam_station_data_v1_from_dict = WeathercamStationDataV1.from_dict(weathercam_station_data_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


