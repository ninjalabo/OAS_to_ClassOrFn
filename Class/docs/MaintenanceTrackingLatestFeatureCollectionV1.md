# MaintenanceTrackingLatestFeatureCollectionV1

GeoJSON Feature Collection of maintenance trackings latest values

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | GeoJSON Object Type | 
**data_updated_time** | **datetime** | Data last updated date time | 
**features** | [**List[MaintenanceTrackingLatestFeatureV1]**](MaintenanceTrackingLatestFeatureV1.md) | GeoJSON Feature Objects | 

## Example

```python
from openapi_client.models.maintenance_tracking_latest_feature_collection_v1 import MaintenanceTrackingLatestFeatureCollectionV1

# TODO update the JSON string below
json = "{}"
# create an instance of MaintenanceTrackingLatestFeatureCollectionV1 from a JSON string
maintenance_tracking_latest_feature_collection_v1_instance = MaintenanceTrackingLatestFeatureCollectionV1.from_json(json)
# print the JSON string representation of the object
print(MaintenanceTrackingLatestFeatureCollectionV1.to_json())

# convert the object into a dict
maintenance_tracking_latest_feature_collection_v1_dict = maintenance_tracking_latest_feature_collection_v1_instance.to_dict()
# create an instance of MaintenanceTrackingLatestFeatureCollectionV1 from a dict
maintenance_tracking_latest_feature_collection_v1_from_dict = MaintenanceTrackingLatestFeatureCollectionV1.from_dict(maintenance_tracking_latest_feature_collection_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


