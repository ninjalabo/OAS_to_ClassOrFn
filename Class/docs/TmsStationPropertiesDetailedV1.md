# TmsStationPropertiesDetailedV1

Tms station properties object with basic information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Id of the road station | 
**tms_number** | **int** | TMS station number | 
**name** | **str** | Common name of road station | [optional] 
**collection_status** | **str** | Data collection status | [optional] 
**state** | **str** | Road station state | [optional] 
**data_updated_time** | **datetime** | Data last updated date time | [optional] 
**collection_interval** | **int** | Data collection interval [s] | [optional] 
**names** | **Dict[str, str]** | Map of names [fi, sv, en] | [optional] 
**road_address** | [**StationRoadAddressV1**](StationRoadAddressV1.md) |  | [optional] 
**livi_id** | **str** | Id in road registry | [optional] 
**country** | **str** | Country where station is located | [optional] 
**start_time** | **datetime** | Station established date time | [optional] 
**repair_maintenance_time** | **datetime** | Repair maintenance date time | [optional] 
**annual_maintenance_time** | **datetime** | Annual maintenance date time | [optional] 
**purpose** | **str** | Purpose of the road station | [optional] 
**municipality** | **str** | Municipality | [optional] 
**municipality_code** | **int** | Municipality code | [optional] 
**province** | **str** | Province | [optional] 
**province_code** | **int** | Province code | [optional] 
**direction1_municipality** | **str** | Direction 1 municipality (1 &#x3D; According to the road register address increasing direction. I.e. on the road 4 to Lahti, if we are in Korso.) | 
**direction1_municipality_code** | **int** | Direction 1 municipality code | [optional] 
**direction2_municipality** | **str** | Direction 2 municipality (2 &#x3D; According to the road register address decreasing direction. I.e. on the road 4 to Helsinki, if we are in Korso.) | 
**direction2_municipality_code** | **int** | Direction 2 municipality code | [optional] 
**station_type** | **str** | TMS station type | [optional] 
**calculator_device_type** | **str** | Type of calculation device | [optional] 
**sensors** | **List[int]** | Tms Station Sensors ids | [optional] 
**free_flow_speed1** | **float** | Free flow speed to direction 1 [km/h] | [optional] 
**free_flow_speed2** | **float** | Free flow speed to direction 2 [km/h] | [optional] 

## Example

```python
from openapi_client.models.tms_station_properties_detailed_v1 import TmsStationPropertiesDetailedV1

# TODO update the JSON string below
json = "{}"
# create an instance of TmsStationPropertiesDetailedV1 from a JSON string
tms_station_properties_detailed_v1_instance = TmsStationPropertiesDetailedV1.from_json(json)
# print the JSON string representation of the object
print(TmsStationPropertiesDetailedV1.to_json())

# convert the object into a dict
tms_station_properties_detailed_v1_dict = tms_station_properties_detailed_v1_instance.to_dict()
# create an instance of TmsStationPropertiesDetailedV1 from a dict
tms_station_properties_detailed_v1_from_dict = TmsStationPropertiesDetailedV1.from_dict(tms_station_properties_detailed_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


