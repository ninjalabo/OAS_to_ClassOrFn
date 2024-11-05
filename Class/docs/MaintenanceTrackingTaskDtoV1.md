# MaintenanceTrackingTaskDtoV1

Maintenance tracking task

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name_fi** | **str** |  | [optional] 
**name_en** | **str** |  | [optional] 
**name_sv** | **str** |  | [optional] 
**data_updated_time** | **datetime** | Data last updated time | 

## Example

```python
from openapi_client.models.maintenance_tracking_task_dto_v1 import MaintenanceTrackingTaskDtoV1

# TODO update the JSON string below
json = "{}"
# create an instance of MaintenanceTrackingTaskDtoV1 from a JSON string
maintenance_tracking_task_dto_v1_instance = MaintenanceTrackingTaskDtoV1.from_json(json)
# print the JSON string representation of the object
print(MaintenanceTrackingTaskDtoV1.to_json())

# convert the object into a dict
maintenance_tracking_task_dto_v1_dict = maintenance_tracking_task_dto_v1_instance.to_dict()
# create an instance of MaintenanceTrackingTaskDtoV1 from a dict
maintenance_tracking_task_dto_v1_from_dict = MaintenanceTrackingTaskDtoV1.from_dict(maintenance_tracking_task_dto_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


