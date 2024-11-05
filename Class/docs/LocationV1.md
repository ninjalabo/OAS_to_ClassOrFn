# LocationV1

AlertC location of a traffic situation announcement

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_code** | **int** | AlertC country code defined by RDS (IEC 62106) | 
**location_table_number** | **int** | AlertC location table number. Country code + location table number fully identifies the table. | 
**location_table_version** | **str** | AlertC location table version number | 
**description** | **str** | Textual representation of the location | 

## Example

```python
from openapi_client.models.location_v1 import LocationV1

# TODO update the JSON string below
json = "{}"
# create an instance of LocationV1 from a JSON string
location_v1_instance = LocationV1.from_json(json)
# print the JSON string representation of the object
print(LocationV1.to_json())

# convert the object into a dict
location_v1_dict = location_v1_instance.to_dict()
# create an instance of LocationV1 from a dict
location_v1_from_dict = LocationV1.from_dict(location_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


