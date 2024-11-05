# TrafficSignHistoryV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cause** | **str** |  | [optional] 
**rows** | [**List[HistoryTextRowV1]**](HistoryTextRowV1.md) |  | [optional] 
**display_value** | **str** |  | [optional] 
**additional_information** | **str** |  | [optional] 
**effect_date** | **datetime** |  | [optional] 

## Example

```python
from openapi_client.models.traffic_sign_history_v1 import TrafficSignHistoryV1

# TODO update the JSON string below
json = "{}"
# create an instance of TrafficSignHistoryV1 from a JSON string
traffic_sign_history_v1_instance = TrafficSignHistoryV1.from_json(json)
# print the JSON string representation of the object
print(TrafficSignHistoryV1.to_json())

# convert the object into a dict
traffic_sign_history_v1_dict = traffic_sign_history_v1_instance.to_dict()
# create an instance of TrafficSignHistoryV1 from a dict
traffic_sign_history_v1_from_dict = TrafficSignHistoryV1.from_dict(traffic_sign_history_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


