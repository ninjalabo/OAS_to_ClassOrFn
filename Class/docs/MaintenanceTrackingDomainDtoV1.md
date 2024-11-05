# MaintenanceTrackingDomainDtoV1

Maintenance tracking domain

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the maintenance tracking domain | 
**source** | **str** | Source and owner of the data | 
**data_updated_time** | **datetime** | Data last updated time | 

## Example

```python
from openapi_client.models.maintenance_tracking_domain_dto_v1 import MaintenanceTrackingDomainDtoV1

# TODO update the JSON string below
json = "{}"
# create an instance of MaintenanceTrackingDomainDtoV1 from a JSON string
maintenance_tracking_domain_dto_v1_instance = MaintenanceTrackingDomainDtoV1.from_json(json)
# print the JSON string representation of the object
print(MaintenanceTrackingDomainDtoV1.to_json())

# convert the object into a dict
maintenance_tracking_domain_dto_v1_dict = maintenance_tracking_domain_dto_v1_instance.to_dict()
# create an instance of MaintenanceTrackingDomainDtoV1 from a dict
maintenance_tracking_domain_dto_v1_from_dict = MaintenanceTrackingDomainDtoV1.from_dict(maintenance_tracking_domain_dto_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


