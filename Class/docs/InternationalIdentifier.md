# InternationalIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country** | **str** |  | 
**national_identifier** | **str** |  | 
**get_international_identifier_extension** | [**ExtensionType**](ExtensionType.md) |  | [optional] 
**international_identifier_extension** | [**ExtensionType**](ExtensionType.md) |  | [optional] 

## Example

```python
from openapi_client.models.international_identifier import InternationalIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of InternationalIdentifier from a JSON string
international_identifier_instance = InternationalIdentifier.from_json(json)
# print the JSON string representation of the object
print(InternationalIdentifier.to_json())

# convert the object into a dict
international_identifier_dict = international_identifier_instance.to_dict()
# create an instance of InternationalIdentifier from a dict
international_identifier_from_dict = InternationalIdentifier.from_dict(international_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


