# WeathercamStationPropertiesSimpleV1

Weathercam station properties object with basic information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id of the road station | 
**name** | **str** | Common name of road station | [optional] 
**collection_status** | **str** | Data collection status | [optional] 
**state** | **str** | Road station state | [optional] 
**data_updated_time** | **datetime** | Data last updated date time | [optional] 
**presets** | [**List[WeathercamPresetSimpleV1]**](WeathercamPresetSimpleV1.md) | Weathercam presets | [optional] 

## Example

```python
from openapi_client.models.weathercam_station_properties_simple_v1 import WeathercamStationPropertiesSimpleV1

# TODO update the JSON string below
json = "{}"
# create an instance of WeathercamStationPropertiesSimpleV1 from a JSON string
weathercam_station_properties_simple_v1_instance = WeathercamStationPropertiesSimpleV1.from_json(json)
# print the JSON string representation of the object
print(WeathercamStationPropertiesSimpleV1.to_json())

# convert the object into a dict
weathercam_station_properties_simple_v1_dict = weathercam_station_properties_simple_v1_instance.to_dict()
# create an instance of WeathercamStationPropertiesSimpleV1 from a dict
weathercam_station_properties_simple_v1_from_dict = WeathercamStationPropertiesSimpleV1.from_dict(weathercam_station_properties_simple_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


