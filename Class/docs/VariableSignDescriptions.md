# VariableSignDescriptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sign_types** | [**List[CodeDescription]**](CodeDescription.md) |  | [optional] 
**data_updated_time** | **datetime** | Data last updated time | 

## Example

```python
from openapi_client.models.variable_sign_descriptions import VariableSignDescriptions

# TODO update the JSON string below
json = "{}"
# create an instance of VariableSignDescriptions from a JSON string
variable_sign_descriptions_instance = VariableSignDescriptions.from_json(json)
# print the JSON string representation of the object
print(VariableSignDescriptions.to_json())

# convert the object into a dict
variable_sign_descriptions_dict = variable_sign_descriptions_instance.to_dict()
# create an instance of VariableSignDescriptions from a dict
variable_sign_descriptions_from_dict = VariableSignDescriptions.from_dict(variable_sign_descriptions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


