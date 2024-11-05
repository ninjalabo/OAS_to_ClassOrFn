# EmissionsExtensionType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**emissions_extension** | [**EmissionsExtension**](EmissionsExtension.md) |  | [optional] 
**anies** | [**List[Element]**](Element.md) |  | [optional] 

## Example

```python
from openapi_client.models.emissions_extension_type import EmissionsExtensionType

# TODO update the JSON string below
json = "{}"
# create an instance of EmissionsExtensionType from a JSON string
emissions_extension_type_instance = EmissionsExtensionType.from_json(json)
# print the JSON string representation of the object
print(EmissionsExtensionType.to_json())

# convert the object into a dict
emissions_extension_type_dict = emissions_extension_type_instance.to_dict()
# create an instance of EmissionsExtensionType from a dict
emissions_extension_type_from_dict = EmissionsExtensionType.from_dict(emissions_extension_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


