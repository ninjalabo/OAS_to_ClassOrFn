# TmsStationFeatureDetailedV1

 Tms station GeoJSON feature object with detailed information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | GeoJSON Object Type | 
**id** | **int** | Id of the road station | 
**geometry** | [**Point**](Point.md) |  | 
**properties** | [**TmsStationPropertiesDetailedV1**](TmsStationPropertiesDetailedV1.md) |  | 

## Example

```python
from openapi_client.models.tms_station_feature_detailed_v1 import TmsStationFeatureDetailedV1

# TODO update the JSON string below
json = "{}"
# create an instance of TmsStationFeatureDetailedV1 from a JSON string
tms_station_feature_detailed_v1_instance = TmsStationFeatureDetailedV1.from_json(json)
# print the JSON string representation of the object
print(TmsStationFeatureDetailedV1.to_json())

# convert the object into a dict
tms_station_feature_detailed_v1_dict = tms_station_feature_detailed_v1_instance.to_dict()
# create an instance of TmsStationFeatureDetailedV1 from a dict
tms_station_feature_detailed_v1_from_dict = TmsStationFeatureDetailedV1.from_dict(tms_station_feature_detailed_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


