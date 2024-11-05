# TmsStationFeatureSimpleV1

Tms station GeoJSON Feature object with basic information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | GeoJSON Object Type | 
**id** | **int** | Id of the road station | 
**geometry** | [**Point**](Point.md) |  | 
**properties** | [**TmsStationPropertiesSimpleV1**](TmsStationPropertiesSimpleV1.md) |  | 

## Example

```python
from openapi_client.models.tms_station_feature_simple_v1 import TmsStationFeatureSimpleV1

# TODO update the JSON string below
json = "{}"
# create an instance of TmsStationFeatureSimpleV1 from a JSON string
tms_station_feature_simple_v1_instance = TmsStationFeatureSimpleV1.from_json(json)
# print the JSON string representation of the object
print(TmsStationFeatureSimpleV1.to_json())

# convert the object into a dict
tms_station_feature_simple_v1_dict = tms_station_feature_simple_v1_instance.to_dict()
# create an instance of TmsStationFeatureSimpleV1 from a dict
tms_station_feature_simple_v1_from_dict = TmsStationFeatureSimpleV1.from_dict(tms_station_feature_simple_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


