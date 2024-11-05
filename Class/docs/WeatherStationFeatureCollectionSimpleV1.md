# WeatherStationFeatureCollectionSimpleV1

GeoJSON Feature Collection of weather stations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | GeoJSON Object Type | 
**data_updated_time** | **datetime** | Data last updated date time | 
**features** | [**List[WeatherStationFeatureSimpleV1]**](WeatherStationFeatureSimpleV1.md) | GeoJSON Feature Objects | 

## Example

```python
from openapi_client.models.weather_station_feature_collection_simple_v1 import WeatherStationFeatureCollectionSimpleV1

# TODO update the JSON string below
json = "{}"
# create an instance of WeatherStationFeatureCollectionSimpleV1 from a JSON string
weather_station_feature_collection_simple_v1_instance = WeatherStationFeatureCollectionSimpleV1.from_json(json)
# print the JSON string representation of the object
print(WeatherStationFeatureCollectionSimpleV1.to_json())

# convert the object into a dict
weather_station_feature_collection_simple_v1_dict = weather_station_feature_collection_simple_v1_instance.to_dict()
# create an instance of WeatherStationFeatureCollectionSimpleV1 from a dict
weather_station_feature_collection_simple_v1_from_dict = WeatherStationFeatureCollectionSimpleV1.from_dict(weather_station_feature_collection_simple_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


