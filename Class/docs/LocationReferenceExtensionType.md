# LocationReferenceExtensionType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**facility_location** | [**FacilityLocation**](FacilityLocation.md) |  | [optional] 
**anies** | [**List[Element]**](Element.md) |  | [optional] 

## Example

```python
from openapi_client.models.location_reference_extension_type import LocationReferenceExtensionType

# TODO update the JSON string below
json = "{}"
# create an instance of LocationReferenceExtensionType from a JSON string
location_reference_extension_type_instance = LocationReferenceExtensionType.from_json(json)
# print the JSON string representation of the object
print(LocationReferenceExtensionType.to_json())

# convert the object into a dict
location_reference_extension_type_dict = location_reference_extension_type_instance.to_dict()
# create an instance of LocationReferenceExtensionType from a dict
location_reference_extension_type_from_dict = LocationReferenceExtensionType.from_dict(location_reference_extension_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


