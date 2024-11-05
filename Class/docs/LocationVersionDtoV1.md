# LocationVersionDtoV1

Location Version Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** | Location version string | 
**data_updated_time** | **datetime** | Data last updated time | 

## Example

```python
from openapi_client.models.location_version_dto_v1 import LocationVersionDtoV1

# TODO update the JSON string below
json = "{}"
# create an instance of LocationVersionDtoV1 from a JSON string
location_version_dto_v1_instance = LocationVersionDtoV1.from_json(json)
# print the JSON string representation of the object
print(LocationVersionDtoV1.to_json())

# convert the object into a dict
location_version_dto_v1_dict = location_version_dto_v1_instance.to_dict()
# create an instance of LocationVersionDtoV1 from a dict
location_version_dto_v1_from_dict = LocationVersionDtoV1.from_dict(location_version_dto_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


