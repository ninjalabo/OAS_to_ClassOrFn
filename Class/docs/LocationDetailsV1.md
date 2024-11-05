# LocationDetailsV1

LocationDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**area_location** | [**AreaLocationV1**](AreaLocationV1.md) |  | [optional] 
**road_address_location** | [**RoadAddressLocationV1**](RoadAddressLocationV1.md) |  | [optional] 

## Example

```python
from openapi_client.models.location_details_v1 import LocationDetailsV1

# TODO update the JSON string below
json = "{}"
# create an instance of LocationDetailsV1 from a JSON string
location_details_v1_instance = LocationDetailsV1.from_json(json)
# print the JSON string representation of the object
print(LocationDetailsV1.to_json())

# convert the object into a dict
location_details_v1_dict = location_details_v1_instance.to_dict()
# create an instance of LocationDetailsV1 from a dict
location_details_v1_from_dict = LocationDetailsV1.from_dict(location_details_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


