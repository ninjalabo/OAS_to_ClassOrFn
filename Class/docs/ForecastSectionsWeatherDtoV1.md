# ForecastSectionsWeatherDtoV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_updated_time** | **datetime** | Data last updated time | 
**forecast_sections** | [**List[ForecastSectionWeatherDtoV1]**](ForecastSectionWeatherDtoV1.md) | Forecast sections | [optional] 

## Example

```python
from openapi_client.models.forecast_sections_weather_dto_v1 import ForecastSectionsWeatherDtoV1

# TODO update the JSON string below
json = "{}"
# create an instance of ForecastSectionsWeatherDtoV1 from a JSON string
forecast_sections_weather_dto_v1_instance = ForecastSectionsWeatherDtoV1.from_json(json)
# print the JSON string representation of the object
print(ForecastSectionsWeatherDtoV1.to_json())

# convert the object into a dict
forecast_sections_weather_dto_v1_dict = forecast_sections_weather_dto_v1_instance.to_dict()
# create an instance of ForecastSectionsWeatherDtoV1 from a dict
forecast_sections_weather_dto_v1_from_dict = ForecastSectionsWeatherDtoV1.from_dict(forecast_sections_weather_dto_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


