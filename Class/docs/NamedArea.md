# NamedArea


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**area_name** | [**MultilingualString**](MultilingualString.md) |  | 
**named_area_type** | [**NamedAreaTypeEnumG**](NamedAreaTypeEnumG.md) |  | [optional] 
**country** | **str** |  | [optional] 
**named_area_extension_g** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.named_area import NamedArea

# TODO update the JSON string below
json = "{}"
# create an instance of NamedArea from a JSON string
named_area_instance = NamedArea.from_json(json)
# print the JSON string representation of the object
print(NamedArea.to_json())

# convert the object into a dict
named_area_dict = named_area_instance.to_dict()
# create an instance of NamedArea from a dict
named_area_from_dict = NamedArea.from_dict(named_area_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


