# WeatherSensorValueHistoryDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**road_station_id** | **int** | Road station id | [optional] 
**sensor_id** | **int** | Sensor id | [optional] 
**sensor_value** | **float** | Sensor value | [optional] 
**measured** | **datetime** |  | [optional] 
**reliability** | **str** | Measurement reliability information | [optional] 
**measured_time** | **datetime** | Value&#39;s measured date time | [optional] 

## Example

```python
from openapi_client.models.weather_sensor_value_history_dto import WeatherSensorValueHistoryDto

# TODO update the JSON string below
json = "{}"
# create an instance of WeatherSensorValueHistoryDto from a JSON string
weather_sensor_value_history_dto_instance = WeatherSensorValueHistoryDto.from_json(json)
# print the JSON string representation of the object
print(WeatherSensorValueHistoryDto.to_json())

# convert the object into a dict
weather_sensor_value_history_dto_dict = weather_sensor_value_history_dto_instance.to_dict()
# create an instance of WeatherSensorValueHistoryDto from a dict
weather_sensor_value_history_dto_from_dict = WeatherSensorValueHistoryDto.from_dict(weather_sensor_value_history_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


