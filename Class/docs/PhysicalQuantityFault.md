# PhysicalQuantityFault


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fault_last_update_time** | **datetime** |  | 
**get_fault_extension** | [**ExtensionType**](ExtensionType.md) |  | [optional] 
**physical_quantity_fault_type** | [**PhysicalQuantityFaultEnum**](PhysicalQuantityFaultEnum.md) |  | 
**get_physical_quantity_fault_extension** | [**ExtensionType**](ExtensionType.md) |  | [optional] 

## Example

```python
from openapi_client.models.physical_quantity_fault import PhysicalQuantityFault

# TODO update the JSON string below
json = "{}"
# create an instance of PhysicalQuantityFault from a JSON string
physical_quantity_fault_instance = PhysicalQuantityFault.from_json(json)
# print the JSON string representation of the object
print(PhysicalQuantityFault.to_json())

# convert the object into a dict
physical_quantity_fault_dict = physical_quantity_fault_instance.to_dict()
# create an instance of PhysicalQuantityFault from a dict
physical_quantity_fault_from_dict = PhysicalQuantityFault.from_dict(physical_quantity_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


