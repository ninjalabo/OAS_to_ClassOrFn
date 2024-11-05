# EstimatedDurationV1

Announcement estimated duration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**minimum** | **str** | Estimated minimum duration using ISO-8601 duration | 
**maximum** | **str** | Estimated maximum duration using ISO-8601 duration | [optional] 
**informal** | **str** | Informal description e.g. 1 - 3 hours | 

## Example

```python
from openapi_client.models.estimated_duration_v1 import EstimatedDurationV1

# TODO update the JSON string below
json = "{}"
# create an instance of EstimatedDurationV1 from a JSON string
estimated_duration_v1_instance = EstimatedDurationV1.from_json(json)
# print the JSON string representation of the object
print(EstimatedDurationV1.to_json())

# convert the object into a dict
estimated_duration_v1_dict = estimated_duration_v1_instance.to_dict()
# create an instance of EstimatedDurationV1 from a dict
estimated_duration_v1_from_dict = EstimatedDurationV1.from_dict(estimated_duration_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


