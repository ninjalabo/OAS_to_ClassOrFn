# ForecastSectionFeatureSimpleV1

GeoJSON feature object of simple forecast section

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | GeoJSON Object Type | 
**id** | **str** | Forecast section identifier 15 characters ie. 00004_112_000_0, see properties id description. | 
**geometry** | [**LineString**](LineString.md) |  | 
**properties** | [**ForecastSectionPropertiesSimpleV1**](ForecastSectionPropertiesSimpleV1.md) |  | 

## Example

```python
from openapi_client.models.forecast_section_feature_simple_v1 import ForecastSectionFeatureSimpleV1

# TODO update the JSON string below
json = "{}"
# create an instance of ForecastSectionFeatureSimpleV1 from a JSON string
forecast_section_feature_simple_v1_instance = ForecastSectionFeatureSimpleV1.from_json(json)
# print the JSON string representation of the object
print(ForecastSectionFeatureSimpleV1.to_json())

# convert the object into a dict
forecast_section_feature_simple_v1_dict = forecast_section_feature_simple_v1_instance.to_dict()
# create an instance of ForecastSectionFeatureSimpleV1 from a dict
forecast_section_feature_simple_v1_from_dict = ForecastSectionFeatureSimpleV1.from_dict(forecast_section_feature_simple_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


