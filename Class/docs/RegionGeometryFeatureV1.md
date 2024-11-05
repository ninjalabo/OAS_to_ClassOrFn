# RegionGeometryFeatureV1

Region area GeoJSON Feature object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | GeoJSON Object Type | 
**geometry** | [**ForecastSectionFeatureV1Geometry**](ForecastSectionFeatureV1Geometry.md) |  | 
**properties** | [**RegionGeometryPropertiesV1**](RegionGeometryPropertiesV1.md) |  | 

## Example

```python
from openapi_client.models.region_geometry_feature_v1 import RegionGeometryFeatureV1

# TODO update the JSON string below
json = "{}"
# create an instance of RegionGeometryFeatureV1 from a JSON string
region_geometry_feature_v1_instance = RegionGeometryFeatureV1.from_json(json)
# print the JSON string representation of the object
print(RegionGeometryFeatureV1.to_json())

# convert the object into a dict
region_geometry_feature_v1_dict = region_geometry_feature_v1_instance.to_dict()
# create an instance of RegionGeometryFeatureV1 from a dict
region_geometry_feature_v1_from_dict = RegionGeometryFeatureV1.from_dict(region_geometry_feature_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


