# MaintenanceTrackingLatestPropertiesV1

Maintenance tracking properties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Id for the tracking | 
**time** | **datetime** | Time of latest tracking | 
**created** | **datetime** | Creation time of tracking | 
**tasks** | **List[str]** | Tasks done during maintenance work | 
**direction** | **float** | Direction of the last observation | [optional] 
**domain** | **str** | Domain of the data | [optional] 
**source** | **str** | Source and owner of the data | [optional] 

## Example

```python
from openapi_client.models.maintenance_tracking_latest_properties_v1 import MaintenanceTrackingLatestPropertiesV1

# TODO update the JSON string below
json = "{}"
# create an instance of MaintenanceTrackingLatestPropertiesV1 from a JSON string
maintenance_tracking_latest_properties_v1_instance = MaintenanceTrackingLatestPropertiesV1.from_json(json)
# print the JSON string representation of the object
print(MaintenanceTrackingLatestPropertiesV1.to_json())

# convert the object into a dict
maintenance_tracking_latest_properties_v1_dict = maintenance_tracking_latest_properties_v1_instance.to_dict()
# create an instance of MaintenanceTrackingLatestPropertiesV1 from a dict
maintenance_tracking_latest_properties_v1_from_dict = MaintenanceTrackingLatestPropertiesV1.from_dict(maintenance_tracking_latest_properties_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


