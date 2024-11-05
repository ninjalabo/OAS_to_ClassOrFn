# NamedNodeMap


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**length** | **int** |  | [optional] 
**named_item** | [**Node**](Node.md) |  | [optional] 
**named_item_ns** | [**Node**](Node.md) |  | [optional] 

## Example

```python
from openapi_client.models.named_node_map import NamedNodeMap

# TODO update the JSON string below
json = "{}"
# create an instance of NamedNodeMap from a JSON string
named_node_map_instance = NamedNodeMap.from_json(json)
# print the JSON string representation of the object
print(NamedNodeMap.to_json())

# convert the object into a dict
named_node_map_dict = named_node_map_instance.to_dict()
# create an instance of NamedNodeMap from a dict
named_node_map_from_dict = NamedNodeMap.from_dict(named_node_map_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


