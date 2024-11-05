# WeathercamStationPropertiesDetailedV1

Weathercam station properties object with detailed information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id of the road station | 
**name** | **str** | Common name of road station | [optional] 
**camera_type** | **str** | Type of camera | [optional] 
**nearest_weather_station_id** | **int** | Nearest weather station id | [optional] 
**collection_status** | **str** | Data collection status | [optional] 
**state** | **str** | Road station state | [optional] 
**data_updated_time** | **datetime** | Data last updated date time | [optional] 
**collection_interval** | **int** | Data collection interval [s] | [optional] 
**names** | **Dict[str, str]** | Map of names [fi, sv, en] | [optional] 
**road_address** | [**StationRoadAddressV1**](StationRoadAddressV1.md) |  | [optional] 
**livi_id** | **str** | Id in road registry | [optional] 
**country** | **str** | Country where station is located | [optional] 
**start_time** | **datetime** | Station established date time | [optional] 
**repair_maintenance_time** | **datetime** | Repair maintenance date time | [optional] 
**annual_maintenance_time** | **datetime** | Annual maintenance date time | [optional] 
**purpose** | **str** | Purpose of the road station | [optional] 
**municipality** | **str** | Municipality | [optional] 
**municipality_code** | **int** | Municipality code | [optional] 
**province** | **str** | Province | [optional] 
**province_code** | **int** | Province code | [optional] 
**presets** | [**List[WeathercamPresetDetailedV1]**](WeathercamPresetDetailedV1.md) | Weathercam presets | [optional] 

## Example

```python
from openapi_client.models.weathercam_station_properties_detailed_v1 import WeathercamStationPropertiesDetailedV1

# TODO update the JSON string below
json = "{}"
# create an instance of WeathercamStationPropertiesDetailedV1 from a JSON string
weathercam_station_properties_detailed_v1_instance = WeathercamStationPropertiesDetailedV1.from_json(json)
# print the JSON string representation of the object
print(WeathercamStationPropertiesDetailedV1.to_json())

# convert the object into a dict
weathercam_station_properties_detailed_v1_dict = weathercam_station_properties_detailed_v1_instance.to_dict()
# create an instance of WeathercamStationPropertiesDetailedV1 from a dict
weathercam_station_properties_detailed_v1_from_dict = WeathercamStationPropertiesDetailedV1.from_dict(weathercam_station_properties_detailed_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


