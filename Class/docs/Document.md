# Document


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**doctype** | [**DocumentType**](DocumentType.md) |  | [optional] 
**document_element** | [**Element**](Element.md) |  | [optional] 
**input_encoding** | **str** |  | [optional] 
**xml_encoding** | **str** |  | [optional] 
**xml_standalone** | **bool** |  | [optional] 
**xml_version** | **str** |  | [optional] 
**strict_error_checking** | **bool** |  | [optional] 
**document_uri** | **str** |  | [optional] 
**dom_config** | [**DOMConfiguration**](DOMConfiguration.md) |  | [optional] 
**implementation** | **object** |  | [optional] 
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
from openapi_client.models.document import Document

# TODO update the JSON string below
json = "{}"
# create an instance of Document from a JSON string
document_instance = Document.from_json(json)
# print the JSON string representation of the object
print(Document.to_json())

# convert the object into a dict
document_dict = document_instance.to_dict()
# create an instance of Document from a dict
document_from_dict = Document.from_dict(document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


