# WeathercamStationFeatureSimpleV1

Weathercam station GeoJSON Feature object with basic information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | GeoJSON Object Type | 
**id** | **str** | Id of the road station | 
**geometry** | [**Point**](Point.md) |  | 
**properties** | [**WeathercamStationPropertiesSimpleV1**](WeathercamStationPropertiesSimpleV1.md) |  | 

## Example

```python
from openapi_client.models.weathercam_station_feature_simple_v1 import WeathercamStationFeatureSimpleV1

# TODO update the JSON string below
json = "{}"
# create an instance of WeathercamStationFeatureSimpleV1 from a JSON string
weathercam_station_feature_simple_v1_instance = WeathercamStationFeatureSimpleV1.from_json(json)
# print the JSON string representation of the object
print(WeathercamStationFeatureSimpleV1.to_json())

# convert the object into a dict
weathercam_station_feature_simple_v1_dict = weathercam_station_feature_simple_v1_instance.to_dict()
# create an instance of WeathercamStationFeatureSimpleV1 from a dict
weathercam_station_feature_simple_v1_from_dict = WeathercamStationFeatureSimpleV1.from_dict(weathercam_station_feature_simple_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


