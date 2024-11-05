# ForecastSectionWeatherForecastDtoV1

Forecast section's weather forecast

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | **datetime** | Observation or forecast time depending on type | [optional] 
**type** | **str** | Tells if object is an observation or a forecast. (OBSERVATION, FORECAST) | [optional] 
**forecast_name** | **str** | Name of the forecast | [optional] 
**daylight** | **bool** | Tells if there is daylight: true/false | [optional] 
**road_temperature** | **float** | Road temperature at given time. If not available value is not set | [optional] 
**temperature** | **float** | Air temperature | [optional] 
**wind_speed** | **float** | Wind speed in m/s | [optional] 
**wind_direction** | **int** | Wind direction in degrees. 0 when there is no wind or the direction is variable. 90 degrees is arrow to the east (count clockwise) | [optional] 
**overall_road_condition** | **str** | Overall road condition | [optional] 
**weather_symbol** | **str** | Weather symbol code. See corresponding symbols at https://www.vaisala.com/en/vaisala-weather-symbols. Symbols are allowed to be used in user&#39;s applications but any further modification and redistribution is denied. | [optional] 
**reliability** | **str** | Forecast reliability | [optional] 
**forecast_condition_reason** | [**ForecastConditionReasonDtoV1**](ForecastConditionReasonDtoV1.md) |  | [optional] 
**data_updated_time** | **datetime** | Data last updated time | 

## Example

```python
from openapi_client.models.forecast_section_weather_forecast_dto_v1 import ForecastSectionWeatherForecastDtoV1

# TODO update the JSON string below
json = "{}"
# create an instance of ForecastSectionWeatherForecastDtoV1 from a JSON string
forecast_section_weather_forecast_dto_v1_instance = ForecastSectionWeatherForecastDtoV1.from_json(json)
# print the JSON string representation of the object
print(ForecastSectionWeatherForecastDtoV1.to_json())

# convert the object into a dict
forecast_section_weather_forecast_dto_v1_dict = forecast_section_weather_forecast_dto_v1_instance.to_dict()
# create an instance of ForecastSectionWeatherForecastDtoV1 from a dict
forecast_section_weather_forecast_dto_v1_from_dict = ForecastSectionWeatherForecastDtoV1.from_dict(forecast_section_weather_forecast_dto_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


