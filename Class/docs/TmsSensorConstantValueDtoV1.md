# TmsSensorConstantValueDtoV1

Sensor constant value

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the sensor constant | 
**value** | **int** | Value of the sensor constant | 
**valid_from** | **str** | Validity start in format mm-dd ie. value 01-31 is 31th of January | 
**valid_to** | **str** | Validity end in format mm-dd ie. value 01-31 is 31th of January | 

## Example

```python
from openapi_client.models.tms_sensor_constant_value_dto_v1 import TmsSensorConstantValueDtoV1

# TODO update the JSON string below
json = "{}"
# create an instance of TmsSensorConstantValueDtoV1 from a JSON string
tms_sensor_constant_value_dto_v1_instance = TmsSensorConstantValueDtoV1.from_json(json)
# print the JSON string representation of the object
print(TmsSensorConstantValueDtoV1.to_json())

# convert the object into a dict
tms_sensor_constant_value_dto_v1_dict = tms_sensor_constant_value_dto_v1_instance.to_dict()
# create an instance of TmsSensorConstantValueDtoV1 from a dict
tms_sensor_constant_value_dto_v1_from_dict = TmsSensorConstantValueDtoV1.from_dict(tms_sensor_constant_value_dto_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


