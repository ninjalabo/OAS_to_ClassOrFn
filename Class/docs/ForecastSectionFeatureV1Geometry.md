# ForecastSectionFeatureV1Geometry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**coordinates** | **List[List[List[float]]]** | An array of LinearRing coordinates. Coordinates are in WGS84 format in decimal degrees: [LONGITUDE, LATITUDE, {ALTITUDE}]. Altitude is optional and measured in meters. | 

## Example

```python
from openapi_client.models.forecast_section_feature_v1_geometry import ForecastSectionFeatureV1Geometry

# TODO update the JSON string below
json = "{}"
# create an instance of ForecastSectionFeatureV1Geometry from a JSON string
forecast_section_feature_v1_geometry_instance = ForecastSectionFeatureV1Geometry.from_json(json)
# print the JSON string representation of the object
print(ForecastSectionFeatureV1Geometry.to_json())

# convert the object into a dict
forecast_section_feature_v1_geometry_dict = forecast_section_feature_v1_geometry_instance.to_dict()
# create an instance of ForecastSectionFeatureV1Geometry from a dict
forecast_section_feature_v1_geometry_from_dict = ForecastSectionFeatureV1Geometry.from_dict(forecast_section_feature_v1_geometry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


