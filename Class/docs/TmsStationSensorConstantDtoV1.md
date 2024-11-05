# TmsStationSensorConstantDtoV1

Sensor constant of TMS Station

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Id of the road station | 
**data_updated_time** | **datetime** | Time when data was last updated | [optional] 
**sensor_constant_values** | [**List[TmsSensorConstantValueDtoV1]**](TmsSensorConstantValueDtoV1.md) | TMS Stations sensor constant values | 

## Example

```python
from openapi_client.models.tms_station_sensor_constant_dto_v1 import TmsStationSensorConstantDtoV1

# TODO update the JSON string below
json = "{}"
# create an instance of TmsStationSensorConstantDtoV1 from a JSON string
tms_station_sensor_constant_dto_v1_instance = TmsStationSensorConstantDtoV1.from_json(json)
# print the JSON string representation of the object
print(TmsStationSensorConstantDtoV1.to_json())

# convert the object into a dict
tms_station_sensor_constant_dto_v1_dict = tms_station_sensor_constant_dto_v1_instance.to_dict()
# create an instance of TmsStationSensorConstantDtoV1 from a dict
tms_station_sensor_constant_dto_v1_from_dict = TmsStationSensorConstantDtoV1.from_dict(tms_station_sensor_constant_dto_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


