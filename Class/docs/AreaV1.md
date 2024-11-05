# AreaV1

AlertC area

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the area | 
**location_code** | **int** | Location code of the area, number of the road point in AlertC location table | 
**type** | [**AreaTypeV1**](AreaTypeV1.md) |  | 

## Example

```python
from openapi_client.models.area_v1 import AreaV1

# TODO update the JSON string below
json = "{}"
# create an instance of AreaV1 from a JSON string
area_v1_instance = AreaV1.from_json(json)
# print the JSON string representation of the object
print(AreaV1.to_json())

# convert the object into a dict
area_v1_dict = area_v1_instance.to_dict()
# create an instance of AreaV1 from a dict
area_v1_from_dict = AreaV1.from_dict(area_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


