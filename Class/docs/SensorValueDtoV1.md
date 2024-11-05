# SensorValueDtoV1

Sensor value

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Sensor type id (naturalId) | 
**station_id** | **int** | Id of the road station | 
**name** | **str** | Sensor name | 
**short_name** | **str** | Sensor short name | 
**time_window_start** | **datetime** | Measurement time window start time (only for fixed time window sensors) | [optional] 
**time_window_end** | **datetime** | Measurement time window end time (only for fixed time window sensors) | [optional] 
**measured_time** | **datetime** | Measurement time | 
**value** | **float** | Measured sensor value | 
**reliability** | **str** | Measurement reliability information | [optional] 
**unit** | **str** | Measured sensor value unit | 
**sensor_value_description_fi** | **str** | Additional information of sensor value [fi] | [optional] 
**sensor_value_description_en** | **str** | Additional information of sensor value [en] | [optional] 

## Example

```python
from openapi_client.models.sensor_value_dto_v1 import SensorValueDtoV1

# TODO update the JSON string below
json = "{}"
# create an instance of SensorValueDtoV1 from a JSON string
sensor_value_dto_v1_instance = SensorValueDtoV1.from_json(json)
# print the JSON string representation of the object
print(SensorValueDtoV1.to_json())

# convert the object into a dict
sensor_value_dto_v1_dict = sensor_value_dto_v1_instance.to_dict()
# create an instance of SensorValueDtoV1 from a dict
sensor_value_dto_v1_from_dict = SensorValueDtoV1.from_dict(sensor_value_dto_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


