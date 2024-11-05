# WeathercamStationFeatureV1Detailed

 Weathercam station GeoJSON feature object with detailed information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | GeoJSON Object Type | 
**id** | **str** | Id of the road station | 
**geometry** | [**Point**](Point.md) |  | 
**properties** | [**WeathercamStationPropertiesDetailedV1**](WeathercamStationPropertiesDetailedV1.md) |  | 

## Example

```python
from openapi_client.models.weathercam_station_feature_v1_detailed import WeathercamStationFeatureV1Detailed

# TODO update the JSON string below
json = "{}"
# create an instance of WeathercamStationFeatureV1Detailed from a JSON string
weathercam_station_feature_v1_detailed_instance = WeathercamStationFeatureV1Detailed.from_json(json)
# print the JSON string representation of the object
print(WeathercamStationFeatureV1Detailed.to_json())

# convert the object into a dict
weathercam_station_feature_v1_detailed_dict = weathercam_station_feature_v1_detailed_instance.to_dict()
# create an instance of WeathercamStationFeatureV1Detailed from a dict
weathercam_station_feature_v1_detailed_from_dict = WeathercamStationFeatureV1Detailed.from_dict(weathercam_station_feature_v1_detailed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


