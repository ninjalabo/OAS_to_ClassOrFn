# JsonDataResponseModelInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_timestamp** | **datetime** | Data interval start | [optional] 
**count** | **float** | Counter count | [optional] 
**interval** | **float** | Interval length in minutes | [optional] 
**status** | **float** | Counter status | [optional] 

## Example

```python
from openapi_client.models.json_data_response_model_inner import JsonDataResponseModelInner

# TODO update the JSON string below
json = "{}"
# create an instance of JsonDataResponseModelInner from a JSON string
json_data_response_model_inner_instance = JsonDataResponseModelInner.from_json(json)
# print the JSON string representation of the object
print(JsonDataResponseModelInner.to_json())

# convert the object into a dict
json_data_response_model_inner_dict = json_data_response_model_inner_instance.to_dict()
# create an instance of JsonDataResponseModelInner from a dict
json_data_response_model_inner_from_dict = JsonDataResponseModelInner.from_dict(json_data_response_model_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


