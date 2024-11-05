# WeathercamStationFeatureCollectionSimpleV1

Weathercam GeoJSON FeatureCollection object with basic information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | GeoJSON Object Type | 
**data_updated_time** | **datetime** | Data last updated date time | 
**features** | [**List[WeathercamStationFeatureSimpleV1]**](WeathercamStationFeatureSimpleV1.md) | GeoJSON Feature Objects | 

## Example

```python
from openapi_client.models.weathercam_station_feature_collection_simple_v1 import WeathercamStationFeatureCollectionSimpleV1

# TODO update the JSON string below
json = "{}"
# create an instance of WeathercamStationFeatureCollectionSimpleV1 from a JSON string
weathercam_station_feature_collection_simple_v1_instance = WeathercamStationFeatureCollectionSimpleV1.from_json(json)
# print the JSON string representation of the object
print(WeathercamStationFeatureCollectionSimpleV1.to_json())

# convert the object into a dict
weathercam_station_feature_collection_simple_v1_dict = weathercam_station_feature_collection_simple_v1_instance.to_dict()
# create an instance of WeathercamStationFeatureCollectionSimpleV1 from a dict
weathercam_station_feature_collection_simple_v1_from_dict = WeathercamStationFeatureCollectionSimpleV1.from_dict(weathercam_station_feature_collection_simple_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


