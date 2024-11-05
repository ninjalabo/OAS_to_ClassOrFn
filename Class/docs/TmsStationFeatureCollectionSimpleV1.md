# TmsStationFeatureCollectionSimpleV1

GeoJSON feature collection of TMS stations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | GeoJSON Object Type | 
**data_updated_time** | **datetime** | Data last updated date time | 
**features** | [**List[TmsStationFeatureSimpleV1]**](TmsStationFeatureSimpleV1.md) | GeoJSON Feature Objects | 

## Example

```python
from openapi_client.models.tms_station_feature_collection_simple_v1 import TmsStationFeatureCollectionSimpleV1

# TODO update the JSON string below
json = "{}"
# create an instance of TmsStationFeatureCollectionSimpleV1 from a JSON string
tms_station_feature_collection_simple_v1_instance = TmsStationFeatureCollectionSimpleV1.from_json(json)
# print the JSON string representation of the object
print(TmsStationFeatureCollectionSimpleV1.to_json())

# convert the object into a dict
tms_station_feature_collection_simple_v1_dict = tms_station_feature_collection_simple_v1_instance.to_dict()
# create an instance of TmsStationFeatureCollectionSimpleV1 from a dict
tms_station_feature_collection_simple_v1_from_dict = TmsStationFeatureCollectionSimpleV1.from_dict(tms_station_feature_collection_simple_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


