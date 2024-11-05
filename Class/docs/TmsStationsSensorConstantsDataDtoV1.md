# TmsStationsSensorConstantsDataDtoV1

Latest sensor constant values of TMS stations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_updated_time** | **datetime** | Time when data was last updated | 
**stations** | [**List[TmsStationSensorConstantDtoV1]**](TmsStationSensorConstantDtoV1.md) | Stations data | [optional] 

## Example

```python
from openapi_client.models.tms_stations_sensor_constants_data_dto_v1 import TmsStationsSensorConstantsDataDtoV1

# TODO update the JSON string below
json = "{}"
# create an instance of TmsStationsSensorConstantsDataDtoV1 from a JSON string
tms_stations_sensor_constants_data_dto_v1_instance = TmsStationsSensorConstantsDataDtoV1.from_json(json)
# print the JSON string representation of the object
print(TmsStationsSensorConstantsDataDtoV1.to_json())

# convert the object into a dict
tms_stations_sensor_constants_data_dto_v1_dict = tms_stations_sensor_constants_data_dto_v1_instance.to_dict()
# create an instance of TmsStationsSensorConstantsDataDtoV1 from a dict
tms_stations_sensor_constants_data_dto_v1_from_dict = TmsStationsSensorConstantsDataDtoV1.from_dict(tms_stations_sensor_constants_data_dto_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


