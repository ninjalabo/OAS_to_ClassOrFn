# UpdateInfosDtoV1

Info about API data updates (update intervals, last updated times)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_updated_time** | **datetime** | Data last updated time | 
**update_times** | [**List[UpdateInfoDtoV1]**](UpdateInfoDtoV1.md) | Update times for APIs | [optional] 

## Example

```python
from openapi_client.models.update_infos_dto_v1 import UpdateInfosDtoV1

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateInfosDtoV1 from a JSON string
update_infos_dto_v1_instance = UpdateInfosDtoV1.from_json(json)
# print the JSON string representation of the object
print(UpdateInfosDtoV1.to_json())

# convert the object into a dict
update_infos_dto_v1_dict = update_infos_dto_v1_instance.to_dict()
# create an instance of UpdateInfosDtoV1 from a dict
update_infos_dto_v1_from_dict = UpdateInfosDtoV1.from_dict(update_infos_dto_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


