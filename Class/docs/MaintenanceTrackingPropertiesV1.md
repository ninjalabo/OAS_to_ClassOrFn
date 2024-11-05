# MaintenanceTrackingPropertiesV1

Maintenance tracking properties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Id for the tracking | 
**previous_id** | **int** | Id for the previous tracking if known | [optional] 
**sending_time** | **datetime** | Time when tracking was reported | 
**created** | **datetime** | Creation time of tracking | 
**tasks** | **List[str]** | Tasks done during maintenance work | 
**start_time** | **datetime** | Start time of maintenance work tasks | 
**end_time** | **datetime** | End time of maintenance work tasks | 
**direction** | **float** | Direction of the last observation | [optional] 
**domain** | **str** | Domain of the data | [optional] 
**source** | **str** | Source and owner of the data | [optional] 

## Example

```python
from openapi_client.models.maintenance_tracking_properties_v1 import MaintenanceTrackingPropertiesV1

# TODO update the JSON string below
json = "{}"
# create an instance of MaintenanceTrackingPropertiesV1 from a JSON string
maintenance_tracking_properties_v1_instance = MaintenanceTrackingPropertiesV1.from_json(json)
# print the JSON string representation of the object
print(MaintenanceTrackingPropertiesV1.to_json())

# convert the object into a dict
maintenance_tracking_properties_v1_dict = maintenance_tracking_properties_v1_instance.to_dict()
# create an instance of MaintenanceTrackingPropertiesV1 from a dict
maintenance_tracking_properties_v1_from_dict = MaintenanceTrackingPropertiesV1.from_dict(maintenance_tracking_properties_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


