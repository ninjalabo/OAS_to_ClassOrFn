# WeatherStationsDataDtoV1

Latest measurement data from Weather stations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_updated_time** | **datetime** | Time when data was last updated | 
**stations** | [**List[WeatherStationDataDtoV1]**](WeatherStationDataDtoV1.md) | Stations data | [optional] 

## Example

```python
from openapi_client.models.weather_stations_data_dto_v1 import WeatherStationsDataDtoV1

# TODO update the JSON string below
json = "{}"
# create an instance of WeatherStationsDataDtoV1 from a JSON string
weather_stations_data_dto_v1_instance = WeatherStationsDataDtoV1.from_json(json)
# print the JSON string representation of the object
print(WeatherStationsDataDtoV1.to_json())

# convert the object into a dict
weather_stations_data_dto_v1_dict = weather_stations_data_dto_v1_instance.to_dict()
# create an instance of WeatherStationsDataDtoV1 from a dict
weather_stations_data_dto_v1_from_dict = WeatherStationsDataDtoV1.from_dict(weather_stations_data_dto_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


