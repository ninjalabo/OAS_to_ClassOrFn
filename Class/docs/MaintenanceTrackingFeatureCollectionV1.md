# MaintenanceTrackingFeatureCollectionV1

GeoJSON Feature Collection of maintenance trackings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | GeoJSON Object Type | 
**data_updated_time** | **datetime** | Data last updated date time | 
**features** | [**List[MaintenanceTrackingFeatureV1]**](MaintenanceTrackingFeatureV1.md) | GeoJSON Feature Objects | 

## Example

```python
from openapi_client.models.maintenance_tracking_feature_collection_v1 import MaintenanceTrackingFeatureCollectionV1

# TODO update the JSON string below
json = "{}"
# create an instance of MaintenanceTrackingFeatureCollectionV1 from a JSON string
maintenance_tracking_feature_collection_v1_instance = MaintenanceTrackingFeatureCollectionV1.from_json(json)
# print the JSON string representation of the object
print(MaintenanceTrackingFeatureCollectionV1.to_json())

# convert the object into a dict
maintenance_tracking_feature_collection_v1_dict = maintenance_tracking_feature_collection_v1_instance.to_dict()
# create an instance of MaintenanceTrackingFeatureCollectionV1 from a dict
maintenance_tracking_feature_collection_v1_from_dict = MaintenanceTrackingFeatureCollectionV1.from_dict(maintenance_tracking_feature_collection_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


