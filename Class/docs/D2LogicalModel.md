# D2LogicalModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exchange** | [**Exchange**](Exchange.md) |  | 
**payload_publication** | [**PayloadPublication**](PayloadPublication.md) |  | [optional] 
**d2_logical_model_extension** | [**ExtensionType**](ExtensionType.md) |  | [optional] 

## Example

```python
from openapi_client.models.d2_logical_model import D2LogicalModel

# TODO update the JSON string below
json = "{}"
# create an instance of D2LogicalModel from a JSON string
d2_logical_model_instance = D2LogicalModel.from_json(json)
# print the JSON string representation of the object
print(D2LogicalModel.to_json())

# convert the object into a dict
d2_logical_model_dict = d2_logical_model_instance.to_dict()
# create an instance of D2LogicalModel from a dict
d2_logical_model_from_dict = D2LogicalModel.from_dict(d2_logical_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


