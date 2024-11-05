# ForecastSectionFeatureV1

GeoJSON feature object of forecast section

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | GeoJSON Object Type | 
**id** | **str** | Forecast section identifier ie. 00004_342_01435_0_274.569:  1. Road number 5 characters ie. 00004,  2. Road section 3 characters ie. 342,  3. Start distance 5 characters ie. 000,  4. Carriageway 1 character,  5. Measure value of link start point. Varying number of characters ie. 274.569,  Refers to Digiroad content at https://aineistot.vayla.fi/digiroad/ | [optional] 
**geometry** | [**ForecastSectionFeatureV1Geometry**](ForecastSectionFeatureV1Geometry.md) |  | 
**properties** | [**ForecastSectionPropertiesV1**](ForecastSectionPropertiesV1.md) |  | 

## Example

```python
from openapi_client.models.forecast_section_feature_v1 import ForecastSectionFeatureV1

# TODO update the JSON string below
json = "{}"
# create an instance of ForecastSectionFeatureV1 from a JSON string
forecast_section_feature_v1_instance = ForecastSectionFeatureV1.from_json(json)
# print the JSON string representation of the object
print(ForecastSectionFeatureV1.to_json())

# convert the object into a dict
forecast_section_feature_v1_dict = forecast_section_feature_v1_instance.to_dict()
# create an instance of ForecastSectionFeatureV1 from a dict
forecast_section_feature_v1_from_dict = ForecastSectionFeatureV1.from_dict(forecast_section_feature_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


