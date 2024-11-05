# CounterModel

Counting Site Metadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | Domain name | [optional] 
**name** | **str** | Counter name | [optional] 
**interval** | **int** | Data recording interval in minutes | [optional] 
**last_data_timestamp** | **datetime** | Timestamp of last data | [optional] 
**removed_timestamp** | **datetime** | Removal timestamp | [optional] 
**id** | **int** | Counter id | [optional] 
**user_type** | **int** | Counter type | [optional] 
**data_updated_time** | **datetime** | Data updated timestamp | [optional] 
**direction** | **int** | Counter direction | [optional] 

## Example

```python
from openapi_client.models.counter_model import CounterModel

# TODO update the JSON string below
json = "{}"
# create an instance of CounterModel from a JSON string
counter_model_instance = CounterModel.from_json(json)
# print the JSON string representation of the object
print(CounterModel.to_json())

# convert the object into a dict
counter_model_dict = counter_model_instance.to_dict()
# create an instance of CounterModel from a dict
counter_model_from_dict = CounterModel.from_dict(counter_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


