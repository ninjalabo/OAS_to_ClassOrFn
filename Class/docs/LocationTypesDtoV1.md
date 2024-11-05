# LocationTypesDtoV1

TMS/Alert-C Location types and location subtypes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_updated_time** | **datetime** | Data last updated time | 
**version** | **str** | Version of TMS/Alert-C material | 
**location_types** | [**List[LocationTypeDtoV1]**](LocationTypeDtoV1.md) | Location types | 
**location_subtypes** | [**List[LocationSubtypeDtoV1]**](LocationSubtypeDtoV1.md) | Location subtypes | 

## Example

```python
from openapi_client.models.location_types_dto_v1 import LocationTypesDtoV1

# TODO update the JSON string below
json = "{}"
# create an instance of LocationTypesDtoV1 from a JSON string
location_types_dto_v1_instance = LocationTypesDtoV1.from_json(json)
# print the JSON string representation of the object
print(LocationTypesDtoV1.to_json())

# convert the object into a dict
location_types_dto_v1_dict = location_types_dto_v1_instance.to_dict()
# create an instance of LocationTypesDtoV1 from a dict
location_types_dto_v1_from_dict = LocationTypesDtoV1.from_dict(location_types_dto_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


