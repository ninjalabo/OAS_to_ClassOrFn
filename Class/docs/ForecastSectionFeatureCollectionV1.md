# ForecastSectionFeatureCollectionV1

GeoJSON feature collection of forecast sections

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | GeoJSON Object Type | 
**data_updated_time** | **datetime** | Data last updated date time | 
**features** | [**List[ForecastSectionFeatureV1]**](ForecastSectionFeatureV1.md) | GeoJSON Feature Objects | 

## Example

```python
from openapi_client.models.forecast_section_feature_collection_v1 import ForecastSectionFeatureCollectionV1

# TODO update the JSON string below
json = "{}"
# create an instance of ForecastSectionFeatureCollectionV1 from a JSON string
forecast_section_feature_collection_v1_instance = ForecastSectionFeatureCollectionV1.from_json(json)
# print the JSON string representation of the object
print(ForecastSectionFeatureCollectionV1.to_json())

# convert the object into a dict
forecast_section_feature_collection_v1_dict = forecast_section_feature_collection_v1_instance.to_dict()
# create an instance of ForecastSectionFeatureCollectionV1 from a dict
forecast_section_feature_collection_v1_from_dict = ForecastSectionFeatureCollectionV1.from_dict(forecast_section_feature_collection_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


