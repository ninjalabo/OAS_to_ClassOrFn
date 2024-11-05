# LocationSubtypeDtoV1

Location subtype

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subtype_code** | **str** | Code of location subtype | 
**description_fi** | **str** | Description of subtype in finnish | 
**description_en** | **str** | Description of subtype in english | 

## Example

```python
from openapi_client.models.location_subtype_dto_v1 import LocationSubtypeDtoV1

# TODO update the JSON string below
json = "{}"
# create an instance of LocationSubtypeDtoV1 from a JSON string
location_subtype_dto_v1_instance = LocationSubtypeDtoV1.from_json(json)
# print the JSON string representation of the object
print(LocationSubtypeDtoV1.to_json())

# convert the object into a dict
location_subtype_dto_v1_dict = location_subtype_dto_v1_instance.to_dict()
# create an instance of LocationSubtypeDtoV1 from a dict
location_subtype_dto_v1_from_dict = LocationSubtypeDtoV1.from_dict(location_subtype_dto_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


