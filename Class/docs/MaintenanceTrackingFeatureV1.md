# MaintenanceTrackingFeatureV1

GeoJSON Feature Object of maintenance tracking.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | GeoJSON Feature Object | 
**properties** | [**MaintenanceTrackingPropertiesV1**](MaintenanceTrackingPropertiesV1.md) |  | 
**geometry** | [**ForecastSectionFeatureV1Geometry**](ForecastSectionFeatureV1Geometry.md) |  | 

## Example

```python
from openapi_client.models.maintenance_tracking_feature_v1 import MaintenanceTrackingFeatureV1

# TODO update the JSON string below
json = "{}"
# create an instance of MaintenanceTrackingFeatureV1 from a JSON string
maintenance_tracking_feature_v1_instance = MaintenanceTrackingFeatureV1.from_json(json)
# print the JSON string representation of the object
print(MaintenanceTrackingFeatureV1.to_json())

# convert the object into a dict
maintenance_tracking_feature_v1_dict = maintenance_tracking_feature_v1_instance.to_dict()
# create an instance of MaintenanceTrackingFeatureV1 from a dict
maintenance_tracking_feature_v1_from_dict = MaintenanceTrackingFeatureV1.from_dict(maintenance_tracking_feature_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


