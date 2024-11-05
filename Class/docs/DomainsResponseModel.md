# DomainsResponseModel

Counting Site Domain

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**added_timestamp** | **datetime** | Domain added | [optional] 
**name** | **str** | Domain name | [optional] 
**description** | **str** | Domain description | [optional] 
**removed_timestamp** | **datetime** | Domain removed | [optional] 

## Example

```python
from openapi_client.models.domains_response_model import DomainsResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of DomainsResponseModel from a JSON string
domains_response_model_instance = DomainsResponseModel.from_json(json)
# print the JSON string representation of the object
print(DomainsResponseModel.to_json())

# convert the object into a dict
domains_response_model_dict = domains_response_model_instance.to_dict()
# create an instance of DomainsResponseModel from a dict
domains_response_model_from_dict = DomainsResponseModel.from_dict(domains_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


