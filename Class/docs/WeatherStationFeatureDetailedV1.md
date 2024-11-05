# WeatherStationFeatureDetailedV1

Weather station GeoJSON feature object with detailed information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | GeoJSON Object Type | 
**id** | **int** | Id of the road station | 
**geometry** | [**Point**](Point.md) |  | 
**properties** | [**WeatherStationPropertiesDetailedV1**](WeatherStationPropertiesDetailedV1.md) |  | 

## Example

```python
from openapi_client.models.weather_station_feature_detailed_v1 import WeatherStationFeatureDetailedV1

# TODO update the JSON string below
json = "{}"
# create an instance of WeatherStationFeatureDetailedV1 from a JSON string
weather_station_feature_detailed_v1_instance = WeatherStationFeatureDetailedV1.from_json(json)
# print the JSON string representation of the object
print(WeatherStationFeatureDetailedV1.to_json())

# convert the object into a dict
weather_station_feature_detailed_v1_dict = weather_station_feature_detailed_v1_instance.to_dict()
# create an instance of WeatherStationFeatureDetailedV1 from a dict
weather_station_feature_detailed_v1_from_dict = WeatherStationFeatureDetailedV1.from_dict(weather_station_feature_detailed_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


