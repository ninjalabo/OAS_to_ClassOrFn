# WeatherStationSensorsDtoV1

Available sensors of weather stations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_updated_time** | **datetime** | Data last updated date time | 
**data_last_checked_time** | **datetime** | Data last checked date time | 
**sensors** | [**List[WeatherStationSensorDtoV1]**](WeatherStationSensorDtoV1.md) | Available sensors of road stations | 

## Example

```python
from openapi_client.models.weather_station_sensors_dto_v1 import WeatherStationSensorsDtoV1

# TODO update the JSON string below
json = "{}"
# create an instance of WeatherStationSensorsDtoV1 from a JSON string
weather_station_sensors_dto_v1_instance = WeatherStationSensorsDtoV1.from_json(json)
# print the JSON string representation of the object
print(WeatherStationSensorsDtoV1.to_json())

# convert the object into a dict
weather_station_sensors_dto_v1_dict = weather_station_sensors_dto_v1_instance.to_dict()
# create an instance of WeatherStationSensorsDtoV1 from a dict
weather_station_sensors_dto_v1_from_dict = WeatherStationSensorsDtoV1.from_dict(weather_station_sensors_dto_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


