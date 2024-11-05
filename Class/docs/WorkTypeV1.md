# WorkTypeV1

Work type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Worktype | 
**description** | **str** | Description | 

## Example

```python
from openapi_client.models.work_type_v1 import WorkTypeV1

# TODO update the JSON string below
json = "{}"
# create an instance of WorkTypeV1 from a JSON string
work_type_v1_instance = WorkTypeV1.from_json(json)
# print the JSON string representation of the object
print(WorkTypeV1.to_json())

# convert the object into a dict
work_type_v1_dict = work_type_v1_instance.to_dict()
# create an instance of WorkTypeV1 from a dict
work_type_v1_from_dict = WorkTypeV1.from_dict(work_type_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


