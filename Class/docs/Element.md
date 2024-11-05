# Element


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_type_info** | [**TypeInfo**](TypeInfo.md) |  | [optional] 
**attribute_node_ns** | [**Attr**](Attr.md) |  | [optional] 
**attribute_node** | [**Attr**](Attr.md) |  | [optional] 
**tag_name** | **str** |  | [optional] 
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
from openapi_client.models.element import Element

# TODO update the JSON string below
json = "{}"
# create an instance of Element from a JSON string
element_instance = Element.from_json(json)
# print the JSON string representation of the object
print(Element.to_json())

# convert the object into a dict
element_dict = element_instance.to_dict()
# create an instance of Element from a dict
element_from_dict = Element.from_dict(element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


