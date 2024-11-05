# MaintenanceTrackingLatestFeatureV1

GeoJSON Feature Object of latest maintenance tracking.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | GeoJSON Object Type | 
**properties** | [**MaintenanceTrackingLatestPropertiesV1**](MaintenanceTrackingLatestPropertiesV1.md) |  | 
**geometry** | [**ForecastSectionFeatureV1Geometry**](ForecastSectionFeatureV1Geometry.md) |  | 

## Example

```python
from openapi_client.models.maintenance_tracking_latest_feature_v1 import MaintenanceTrackingLatestFeatureV1

# TODO update the JSON string below
json = "{}"
# create an instance of MaintenanceTrackingLatestFeatureV1 from a JSON string
maintenance_tracking_latest_feature_v1_instance = MaintenanceTrackingLatestFeatureV1.from_json(json)
# print the JSON string representation of the object
print(MaintenanceTrackingLatestFeatureV1.to_json())

# convert the object into a dict
maintenance_tracking_latest_feature_v1_dict = maintenance_tracking_latest_feature_v1_instance.to_dict()
# create an instance of MaintenanceTrackingLatestFeatureV1 from a dict
maintenance_tracking_latest_feature_v1_from_dict = MaintenanceTrackingLatestFeatureV1.from_dict(maintenance_tracking_latest_feature_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


