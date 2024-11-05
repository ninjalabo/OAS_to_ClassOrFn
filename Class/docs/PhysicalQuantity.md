# PhysicalQuantity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**forecast** | **bool** |  | [optional] 
**measurement_equipment_type_used** | [**MultilingualString**](MultilingualString.md) |  | [optional] 
**pertinent_location** | [**LocationReference**](LocationReference.md) |  | [optional] 
**physical_quantity_faults** | [**List[PhysicalQuantityFault]**](PhysicalQuantityFault.md) |  | [optional] 
**source** | [**Source**](Source.md) |  | [optional] 
**information_manager_override** | [**InternationalIdentifier**](InternationalIdentifier.md) |  | [optional] 
**get_physical_quantity_extension** | [**ExtensionType**](ExtensionType.md) |  | [optional] 

## Example

```python
from openapi_client.models.physical_quantity import PhysicalQuantity

# TODO update the JSON string below
json = "{}"
# create an instance of PhysicalQuantity from a JSON string
physical_quantity_instance = PhysicalQuantity.from_json(json)
# print the JSON string representation of the object
print(PhysicalQuantity.to_json())

# convert the object into a dict
physical_quantity_dict = physical_quantity_instance.to_dict()
# create an instance of PhysicalQuantity from a dict
physical_quantity_from_dict = PhysicalQuantity.from_dict(physical_quantity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


