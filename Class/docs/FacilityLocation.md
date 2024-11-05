# FacilityLocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_zone** | **str** |  | [optional] 
**address** | [**Address**](Address.md) |  | [optional] 

## Example

```python
from openapi_client.models.facility_location import FacilityLocation

# TODO update the JSON string below
json = "{}"
# create an instance of FacilityLocation from a JSON string
facility_location_instance = FacilityLocation.from_json(json)
# print the JSON string representation of the object
print(FacilityLocation.to_json())

# convert the object into a dict
facility_location_dict = facility_location_instance.to_dict()
# create an instance of FacilityLocation from a dict
facility_location_from_dict = FacilityLocation.from_dict(facility_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


