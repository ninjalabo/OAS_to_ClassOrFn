# VehicleCharacteristics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fuel_types** | [**List[FuelTypeEnum]**](FuelTypeEnum.md) |  | [optional] 
**load_type** | [**LoadTypeEnum**](LoadTypeEnum.md) |  | [optional] 
**vehicle_equipment** | [**VehicleEquipmentEnum**](VehicleEquipmentEnum.md) |  | [optional] 
**vehicle_types** | [**List[VehicleTypeEnum]**](VehicleTypeEnum.md) |  | [optional] 
**vehicle_usage** | [**VehicleUsageEnum**](VehicleUsageEnum.md) |  | [optional] 
**year_of_first_registration** | **int** |  | [optional] 
**gross_weight_characteristics** | [**List[GrossWeightCharacteristic]**](GrossWeightCharacteristic.md) |  | [optional] 
**height_characteristics** | [**List[HeightCharacteristic]**](HeightCharacteristic.md) |  | [optional] 
**length_characteristics** | [**List[LengthCharacteristic]**](LengthCharacteristic.md) |  | [optional] 
**width_characteristics** | [**List[WidthCharacteristic]**](WidthCharacteristic.md) |  | [optional] 
**heaviest_axle_weight_characteristics** | [**List[HeaviestAxleWeightCharacteristic]**](HeaviestAxleWeightCharacteristic.md) |  | [optional] 
**number_of_axles_characteristics** | [**List[NumberOfAxlesCharacteristic]**](NumberOfAxlesCharacteristic.md) |  | [optional] 
**emissions** | [**Emissions**](Emissions.md) |  | [optional] 
**get_vehicle_characteristics_extension** | [**ExtensionType**](ExtensionType.md) |  | [optional] 

## Example

```python
from openapi_client.models.vehicle_characteristics import VehicleCharacteristics

# TODO update the JSON string below
json = "{}"
# create an instance of VehicleCharacteristics from a JSON string
vehicle_characteristics_instance = VehicleCharacteristics.from_json(json)
# print the JSON string representation of the object
print(VehicleCharacteristics.to_json())

# convert the object into a dict
vehicle_characteristics_dict = vehicle_characteristics_instance.to_dict()
# create an instance of VehicleCharacteristics from a dict
vehicle_characteristics_from_dict = VehicleCharacteristics.from_dict(vehicle_characteristics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


