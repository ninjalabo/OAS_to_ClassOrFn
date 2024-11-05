# CatalogueReference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_catalogue_reference** | **str** |  | 
**catalogue_reference_extension** | [**ExtensionType**](ExtensionType.md) |  | [optional] 

## Example

```python
from openapi_client.models.catalogue_reference import CatalogueReference

# TODO update the JSON string below
json = "{}"
# create an instance of CatalogueReference from a JSON string
catalogue_reference_instance = CatalogueReference.from_json(json)
# print the JSON string representation of the object
print(CatalogueReference.to_json())

# convert the object into a dict
catalogue_reference_dict = catalogue_reference_instance.to_dict()
# create an instance of CatalogueReference from a dict
catalogue_reference_from_dict = CatalogueReference.from_dict(catalogue_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


