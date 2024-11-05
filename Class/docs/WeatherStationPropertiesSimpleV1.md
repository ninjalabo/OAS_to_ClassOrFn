# WeatherStationPropertiesSimpleV1

Weather station properties object with basic information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Id of the road station | 
**name** | **str** | Common name of road station | [optional] 
**collection_status** | **str** | Data collection status | [optional] 
**state** | **str** | Road station state | [optional] 
**data_updated_time** | **datetime** | Data last updated date time | [optional] 

## Example

```python
from openapi_client.models.weather_station_properties_simple_v1 import WeatherStationPropertiesSimpleV1

# TODO update the JSON string below
json = "{}"
# create an instance of WeatherStationPropertiesSimpleV1 from a JSON string
weather_station_properties_simple_v1_instance = WeatherStationPropertiesSimpleV1.from_json(json)
# print the JSON string representation of the object
print(WeatherStationPropertiesSimpleV1.to_json())

# convert the object into a dict
weather_station_properties_simple_v1_dict = weather_station_properties_simple_v1_instance.to_dict()
# create an instance of WeatherStationPropertiesSimpleV1 from a dict
weather_station_properties_simple_v1_from_dict = WeatherStationPropertiesSimpleV1.from_dict(weather_station_properties_simple_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


