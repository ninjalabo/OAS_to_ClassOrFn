# Attr


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**value** | **str** |  | [optional] 
**specified** | **bool** |  | [optional] 
**owner_element** | [**Element**](Element.md) |  | [optional] 
**schema_type_info** | [**TypeInfo**](TypeInfo.md) |  | [optional] 
**id** | **bool** |  | [optional] 
**attributes** | [**NamedNodeMap**](NamedNodeMap.md) |  | [optional] 
**local_name** | **str** |  | [optional] 
**node_name** | **str** |  | [optional] 
**node_value** | **str** |  | [optional] 
**parent_node** | [**Node**](Node.md) |  | [optional] 
**child_nodes** | [**NodeList**](NodeList.md) |  | [optional] 
**first_child** | [**Node**](Node.md) |  | [optional] 
**last_child** | [**Node**](Node.md) |  | [optional] 
**previous_sibling** | [**Node**](Node.md) |  | [optional] 
**next_sibling** | [**Node**](Node.md) |  | [optional] 
**owner_document** | [**Document**](Document.md) |  | [optional] 
**namespace_uri** | **str** |  | [optional] 
**base_uri** | **str** |  | [optional] 
**text_content** | **str** |  | [optional] 
**prefix** | **str** |  | [optional] 
**node_type** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.attr import Attr

# TODO update the JSON string below
json = "{}"
# create an instance of Attr from a JSON string
attr_instance = Attr.from_json(json)
# print the JSON string representation of the object
print(Attr.to_json())

# convert the object into a dict
attr_dict = attr_instance.to_dict()
# create an instance of Attr from a dict
attr_from_dict = Attr.from_dict(attr_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


