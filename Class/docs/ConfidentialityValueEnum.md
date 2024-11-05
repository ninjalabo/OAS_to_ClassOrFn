# ConfidentialityValueEnum


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | [optional] 
**get_extended_value** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.confidentiality_value_enum import ConfidentialityValueEnum

# TODO update the JSON string below
json = "{}"
# create an instance of ConfidentialityValueEnum from a JSON string
confidentiality_value_enum_instance = ConfidentialityValueEnum.from_json(json)
# print the JSON string representation of the object
print(ConfidentialityValueEnum.to_json())

# convert the object into a dict
confidentiality_value_enum_dict = confidentiality_value_enum_instance.to_dict()
# create an instance of ConfidentialityValueEnum from a dict
confidentiality_value_enum_from_dict = ConfidentialityValueEnum.from_dict(confidentiality_value_enum_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


