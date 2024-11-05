# InformationStatusEnum


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | [optional] 
**get_extended_value** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.information_status_enum import InformationStatusEnum

# TODO update the JSON string below
json = "{}"
# create an instance of InformationStatusEnum from a JSON string
information_status_enum_instance = InformationStatusEnum.from_json(json)
# print the JSON string representation of the object
print(InformationStatusEnum.to_json())

# convert the object into a dict
information_status_enum_dict = information_status_enum_instance.to_dict()
# create an instance of InformationStatusEnum from a dict
information_status_enum_from_dict = InformationStatusEnum.from_dict(information_status_enum_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


