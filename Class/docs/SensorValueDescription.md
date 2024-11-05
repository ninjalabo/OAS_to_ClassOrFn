# SensorValueDescription

Additional information of sensor values

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description_en** | **str** | Sensor description [en] | [optional] 
**description_fi** | **str** | Sensor description [fi] | [optional] 
**sensor_value** | **float** | Sensor value | [optional] 

## Example

```python
from openapi_client.models.sensor_value_description import SensorValueDescription

# TODO update the JSON string below
json = "{}"
# create an instance of SensorValueDescription from a JSON string
sensor_value_description_instance = SensorValueDescription.from_json(json)
# print the JSON string representation of the object
print(SensorValueDescription.to_json())

# convert the object into a dict
sensor_value_description_dict = sensor_value_description_instance.to_dict()
# create an instance of SensorValueDescription from a dict
sensor_value_description_from_dict = SensorValueDescription.from_dict(sensor_value_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


