# TmsStationDataDtoV1

TMS station data with sensor values

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Id of the road station | 
**tms_number** | **int** | TMS station number | 
**data_updated_time** | **datetime** | Time when data was last updated | [optional] 
**sensor_values** | [**List[SensorValueDtoV1]**](SensorValueDtoV1.md) | Measured sensor values of the station | 

## Example

```python
from openapi_client.models.tms_station_data_dto_v1 import TmsStationDataDtoV1

# TODO update the JSON string below
json = "{}"
# create an instance of TmsStationDataDtoV1 from a JSON string
tms_station_data_dto_v1_instance = TmsStationDataDtoV1.from_json(json)
# print the JSON string representation of the object
print(TmsStationDataDtoV1.to_json())

# convert the object into a dict
tms_station_data_dto_v1_dict = tms_station_data_dto_v1_instance.to_dict()
# create an instance of TmsStationDataDtoV1 from a dict
tms_station_data_dto_v1_from_dict = TmsStationDataDtoV1.from_dict(tms_station_data_dto_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


