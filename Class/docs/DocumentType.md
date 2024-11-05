# DocumentType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**public_id** | **str** |  | [optional] 
**system_id** | **str** |  | [optional] 
**entities** | [**NamedNodeMap**](NamedNodeMap.md) |  | [optional] 
**notations** | [**NamedNodeMap**](NamedNodeMap.md) |  | [optional] 
**internal_subset** | **str** |  | [optional] 
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
from openapi_client.models.document_type import DocumentType

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentType from a JSON string
document_type_instance = DocumentType.from_json(json)
# print the JSON string representation of the object
print(DocumentType.to_json())

# convert the object into a dict
document_type_dict = document_type_instance.to_dict()
# create an instance of DocumentType from a dict
document_type_from_dict = DocumentType.from_dict(document_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


