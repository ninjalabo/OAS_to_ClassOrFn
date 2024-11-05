# FilterReference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delete_filter** | **bool** |  | [optional] 
**filter_operation_approved** | **bool** |  | [optional] 
**key_filter_reference** | **str** |  | 
**filter_reference_extension** | [**ExtensionType**](ExtensionType.md) |  | [optional] 

## Example

```python
from openapi_client.models.filter_reference import FilterReference

# TODO update the JSON string below
json = "{}"
# create an instance of FilterReference from a JSON string
filter_reference_instance = FilterReference.from_json(json)
# print the JSON string representation of the object
print(FilterReference.to_json())

# convert the object into a dict
filter_reference_dict = filter_reference_instance.to_dict()
# create an instance of FilterReference from a dict
filter_reference_from_dict = FilterReference.from_dict(filter_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


