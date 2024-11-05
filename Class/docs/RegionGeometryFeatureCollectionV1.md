# RegionGeometryFeatureCollectionV1

GeoJSON Feature Collection of Region Geometries

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | GeoJSON Object Type | 
**data_updated_time** | **datetime** | Data last updated date time | 
**features** | [**List[RegionGeometryFeatureV1]**](RegionGeometryFeatureV1.md) | GeoJSON Feature Objects | 

## Example

```python
from openapi_client.models.region_geometry_feature_collection_v1 import RegionGeometryFeatureCollectionV1

# TODO update the JSON string below
json = "{}"
# create an instance of RegionGeometryFeatureCollectionV1 from a JSON string
region_geometry_feature_collection_v1_instance = RegionGeometryFeatureCollectionV1.from_json(json)
# print the JSON string representation of the object
print(RegionGeometryFeatureCollectionV1.to_json())

# convert the object into a dict
region_geometry_feature_collection_v1_dict = region_geometry_feature_collection_v1_instance.to_dict()
# create an instance of RegionGeometryFeatureCollectionV1 from a dict
region_geometry_feature_collection_v1_from_dict = RegionGeometryFeatureCollectionV1.from_dict(region_geometry_feature_collection_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


