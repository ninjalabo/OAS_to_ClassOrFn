# TmsStationSensorsDtoV1

Available sensors of TMS stations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_updated_time** | **datetime** | Data last updated date time | 
**data_last_checked_time** | **datetime** | Data last checked date time | 
**sensors** | [**List[TmsStationSensorDtoV1]**](TmsStationSensorDtoV1.md) | Available sensors of road stations | 

## Example

```python
from openapi_client.models.tms_station_sensors_dto_v1 import TmsStationSensorsDtoV1

# TODO update the JSON string below
json = "{}"
# create an instance of TmsStationSensorsDtoV1 from a JSON string
tms_station_sensors_dto_v1_instance = TmsStationSensorsDtoV1.from_json(json)
# print the JSON string representation of the object
print(TmsStationSensorsDtoV1.to_json())

# convert the object into a dict
tms_station_sensors_dto_v1_dict = tms_station_sensors_dto_v1_instance.to_dict()
# create an instance of TmsStationSensorsDtoV1 from a dict
tms_station_sensors_dto_v1_from_dict = TmsStationSensorsDtoV1.from_dict(tms_station_sensors_dto_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


