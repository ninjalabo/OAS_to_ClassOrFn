# Node


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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
from openapi_client.models.node import Node

# TODO update the JSON string below
json = "{}"
# create an instance of Node from a JSON string
node_instance = Node.from_json(json)
# print the JSON string representation of the object
print(Node.to_json())

# convert the object into a dict
node_dict = node_instance.to_dict()
# create an instance of Node from a dict
node_from_dict = Node.from_dict(node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


