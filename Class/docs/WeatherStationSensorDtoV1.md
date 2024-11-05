# WeatherStationSensorDtoV1

Weather road station sensor

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Sensor id | 
**name** | **str** | Sensor name [fi] | [optional] 
**short_name** | **str** | Short name for sensor [fi] | [optional] 
**unit** | **str** | Unit of sensor value | [optional] 
**accuracy** | **int** | Sensor accuracy | [optional] 
**sensor_value_descriptions** | [**List[SensorValueDescription]**](SensorValueDescription.md) | Descriptions for sensor values | [optional] 
**presentation_names** | **Dict[str, str]** | Map of presentation names [fi, sv, en] | [optional] 
**descriptions** | **Dict[str, str]** | Map of sensor descriptions [fi, sv, en] | [optional] 
**direction** | [**RoadStationSensorDirection**](RoadStationSensorDirection.md) |  | [optional] 
**description** | **str** | Sensor description [fi] | [optional] 

## Example

```python
from openapi_client.models.weather_station_sensor_dto_v1 import WeatherStationSensorDtoV1

# TODO update the JSON string below
json = "{}"
# create an instance of WeatherStationSensorDtoV1 from a JSON string
weather_station_sensor_dto_v1_instance = WeatherStationSensorDtoV1.from_json(json)
# print the JSON string representation of the object
print(WeatherStationSensorDtoV1.to_json())

# convert the object into a dict
weather_station_sensor_dto_v1_dict = weather_station_sensor_dto_v1_instance.to_dict()
# create an instance of WeatherStationSensorDtoV1 from a dict
weather_station_sensor_dto_v1_from_dict = WeatherStationSensorDtoV1.from_dict(weather_station_sensor_dto_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


