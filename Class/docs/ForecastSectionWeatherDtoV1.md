# ForecastSectionWeatherDtoV1

Forecast section weather forecasts

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | VERSION 1: Forecast section identifier 15 characters ie. 00004_112_000_0: &lt;br&gt; 1. Road number 5 characters ie. 00004, &lt;br&gt; 2. Road section 3 characters ie. 112, &lt;br&gt; 3. Road section version 3 characters ie. 000, &lt;br&gt; 4. Reserved for future needs 1 characters default 0 &lt;br&gt; &lt;br&gt; VERSION 2: Forecast section identifier ie. 00004_342_01435_0_274.569: &lt;br&gt; 1. Road number 5 characters ie. 00004, &lt;br&gt; 2. Road section 3 characters ie. 342, &lt;br&gt; 3. Start distance 5 characters ie. 000, &lt;br&gt; 4. Carriageway 1 character, &lt;br&gt; 5. Measure value of link start point. Varying number of characters ie. 274.569, &lt;br&gt; Refers to Digiroad content at https://aineistot.vayla.fi/digiroad/ | [optional] 
**forecasts** | [**List[ForecastSectionWeatherForecastDtoV1]**](ForecastSectionWeatherForecastDtoV1.md) | Forecast section&#39;s weather forecasts | [optional] 
**data_updated_time** | **datetime** | Data last updated time | 

## Example

```python
from openapi_client.models.forecast_section_weather_dto_v1 import ForecastSectionWeatherDtoV1

# TODO update the JSON string below
json = "{}"
# create an instance of ForecastSectionWeatherDtoV1 from a JSON string
forecast_section_weather_dto_v1_instance = ForecastSectionWeatherDtoV1.from_json(json)
# print the JSON string representation of the object
print(ForecastSectionWeatherDtoV1.to_json())

# convert the object into a dict
forecast_section_weather_dto_v1_dict = forecast_section_weather_dto_v1_instance.to_dict()
# create an instance of ForecastSectionWeatherDtoV1 from a dict
forecast_section_weather_dto_v1_from_dict = ForecastSectionWeatherDtoV1.from_dict(forecast_section_weather_dto_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


