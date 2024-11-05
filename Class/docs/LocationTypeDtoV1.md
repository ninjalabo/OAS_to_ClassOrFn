# LocationTypeDtoV1

Location type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type_code** | **str** | Code of location type | 
**description_fi** | **str** | Description of type in finnish | 
**description_en** | **str** | Description of type in english | 

## Example

```python
from openapi_client.models.location_type_dto_v1 import LocationTypeDtoV1

# TODO update the JSON string below
json = "{}"
# create an instance of LocationTypeDtoV1 from a JSON string
location_type_dto_v1_instance = LocationTypeDtoV1.from_json(json)
# print the JSON string representation of the object
print(LocationTypeDtoV1.to_json())

# convert the object into a dict
location_type_dto_v1_dict = location_type_dto_v1_instance.to_dict()
# create an instance of LocationTypeDtoV1 from a dict
location_type_dto_v1_from_dict = LocationTypeDtoV1.from_dict(location_type_dto_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


