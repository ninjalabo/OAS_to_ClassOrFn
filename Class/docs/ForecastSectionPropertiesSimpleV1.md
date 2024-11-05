# ForecastSectionPropertiesSimpleV1

Simple forecast section properties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Forecast section identifier 15 characters ie. 00004_112_000_0:  1. Road number 5 characters ie. 00004,  2. Road section 3 characters ie. 112,  3. Road section version 3 characters ie. 000,  4. Reserved for future needs 1 characters default 0 | [optional] 
**description** | **str** | Forecast section description | [optional] 
**road_section_number** | **int** | Road section number | [optional] 
**road_number** | **int** | Forecast section road number | [optional] 
**road_section_version_number** | **int** | Road section version number | [optional] 
**data_updated_time** | **datetime** | Data last updated date time | 

## Example

```python
from openapi_client.models.forecast_section_properties_simple_v1 import ForecastSectionPropertiesSimpleV1

# TODO update the JSON string below
json = "{}"
# create an instance of ForecastSectionPropertiesSimpleV1 from a JSON string
forecast_section_properties_simple_v1_instance = ForecastSectionPropertiesSimpleV1.from_json(json)
# print the JSON string representation of the object
print(ForecastSectionPropertiesSimpleV1.to_json())

# convert the object into a dict
forecast_section_properties_simple_v1_dict = forecast_section_properties_simple_v1_instance.to_dict()
# create an instance of ForecastSectionPropertiesSimpleV1 from a dict
forecast_section_properties_simple_v1_from_dict = ForecastSectionPropertiesSimpleV1.from_dict(forecast_section_properties_simple_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


