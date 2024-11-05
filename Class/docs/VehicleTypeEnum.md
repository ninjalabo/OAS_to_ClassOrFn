# VehicleTypeEnum


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | [optional] 
**get_extended_value** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.vehicle_type_enum import VehicleTypeEnum

# TODO update the JSON string below
json = "{}"
# create an instance of VehicleTypeEnum from a JSON string
vehicle_type_enum_instance = VehicleTypeEnum.from_json(json)
# print the JSON string representation of the object
print(VehicleTypeEnum.to_json())

# convert the object into a dict
vehicle_type_enum_dict = vehicle_type_enum_instance.to_dict()
# create an instance of VehicleTypeEnum from a dict
vehicle_type_enum_from_dict = VehicleTypeEnum.from_dict(vehicle_type_enum_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


