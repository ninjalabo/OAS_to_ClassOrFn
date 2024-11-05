# TmsStationsDataDtoV1

Latest measurement data from TMS stations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_updated_time** | **datetime** | Time when data was last updated | 
**stations** | [**List[TmsStationDataDtoV1]**](TmsStationDataDtoV1.md) | Stations data | [optional] 

## Example

```python
from openapi_client.models.tms_stations_data_dto_v1 import TmsStationsDataDtoV1

# TODO update the JSON string below
json = "{}"
# create an instance of TmsStationsDataDtoV1 from a JSON string
tms_stations_data_dto_v1_instance = TmsStationsDataDtoV1.from_json(json)
# print the JSON string representation of the object
print(TmsStationsDataDtoV1.to_json())

# convert the object into a dict
tms_stations_data_dto_v1_dict = tms_stations_data_dto_v1_instance.to_dict()
# create an instance of TmsStationsDataDtoV1 from a dict
tms_stations_data_dto_v1_from_dict = TmsStationsDataDtoV1.from_dict(tms_stations_data_dto_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


