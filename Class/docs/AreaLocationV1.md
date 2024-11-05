# AreaLocationV1

Location consisting of one or more areas

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**areas** | [**List[AreaV1]**](AreaV1.md) | List of areas | 

## Example

```python
from openapi_client.models.area_location_v1 import AreaLocationV1

# TODO update the JSON string below
json = "{}"
# create an instance of AreaLocationV1 from a JSON string
area_location_v1_instance = AreaLocationV1.from_json(json)
# print the JSON string representation of the object
print(AreaLocationV1.to_json())

# convert the object into a dict
area_location_v1_dict = area_location_v1_instance.to_dict()
# create an instance of AreaLocationV1 from a dict
area_location_v1_from_dict = AreaLocationV1.from_dict(area_location_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


