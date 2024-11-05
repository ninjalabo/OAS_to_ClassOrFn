# LocationFeatureCollectionV1

Location GeoJSON feature collection object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | GeoJSON Object Type | 
**locations_version** | **str** | Locations version | 
**data_updated_time** | **datetime** | Data last updated date time | 
**features** | [**List[LocationFeatureV1]**](LocationFeatureV1.md) | GeoJSON Feature Objects | 

## Example

```python
from openapi_client.models.location_feature_collection_v1 import LocationFeatureCollectionV1

# TODO update the JSON string below
json = "{}"
# create an instance of LocationFeatureCollectionV1 from a JSON string
location_feature_collection_v1_instance = LocationFeatureCollectionV1.from_json(json)
# print the JSON string representation of the object
print(LocationFeatureCollectionV1.to_json())

# convert the object into a dict
location_feature_collection_v1_dict = location_feature_collection_v1_instance.to_dict()
# create an instance of LocationFeatureCollectionV1 from a dict
location_feature_collection_v1_from_dict = LocationFeatureCollectionV1.from_dict(location_feature_collection_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


