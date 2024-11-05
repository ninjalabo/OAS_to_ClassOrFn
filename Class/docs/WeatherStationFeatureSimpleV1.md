# WeatherStationFeatureSimpleV1

Weather station GeoJSON Feature object with basic information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | GeoJSON Object Type | 
**id** | **int** | Id of the road station | 
**geometry** | [**Point**](Point.md) |  | 
**properties** | [**WeatherStationPropertiesSimpleV1**](WeatherStationPropertiesSimpleV1.md) |  | 

## Example

```python
from openapi_client.models.weather_station_feature_simple_v1 import WeatherStationFeatureSimpleV1

# TODO update the JSON string below
json = "{}"
# create an instance of WeatherStationFeatureSimpleV1 from a JSON string
weather_station_feature_simple_v1_instance = WeatherStationFeatureSimpleV1.from_json(json)
# print the JSON string representation of the object
print(WeatherStationFeatureSimpleV1.to_json())

# convert the object into a dict
weather_station_feature_simple_v1_dict = weather_station_feature_simple_v1_instance.to_dict()
# create an instance of WeatherStationFeatureSimpleV1 from a dict
weather_station_feature_simple_v1_from_dict = WeatherStationFeatureSimpleV1.from_dict(weather_station_feature_simple_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


