# MultilingualStringValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | [optional] 
**lang** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.multilingual_string_value import MultilingualStringValue

# TODO update the JSON string below
json = "{}"
# create an instance of MultilingualStringValue from a JSON string
multilingual_string_value_instance = MultilingualStringValue.from_json(json)
# print the JSON string representation of the object
print(MultilingualStringValue.to_json())

# convert the object into a dict
multilingual_string_value_dict = multilingual_string_value_instance.to_dict()
# create an instance of MultilingualStringValue from a dict
multilingual_string_value_from_dict = MultilingualStringValue.from_dict(multilingual_string_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


