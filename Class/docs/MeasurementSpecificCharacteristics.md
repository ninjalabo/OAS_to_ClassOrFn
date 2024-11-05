# MeasurementSpecificCharacteristics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accuracy** | **float** |  | [optional] 
**computation_method** | [**ComputationMethodEnum**](ComputationMethodEnum.md) |  | [optional] 
**default_measurement_height** | **float** |  | [optional] 
**measurement_side** | [**DirectionEnum**](DirectionEnum.md) |  | [optional] 
**period** | **float** |  | [optional] 
**smoothing_factor** | **float** |  | [optional] 
**specific_measurement_value_type** | [**MeasuredOrDerivedDataTypeEnum**](MeasuredOrDerivedDataTypeEnum.md) |  | 
**specific_vehicle_characteristics** | [**VehicleCharacteristics**](VehicleCharacteristics.md) |  | [optional] 
**specific_lanes** | [**List[Lane]**](Lane.md) |  | [optional] 
**axle_characteristics** | [**AxleCharacteristics**](AxleCharacteristics.md) |  | [optional] 
**get_measurement_specific_characteristics_extension** | [**ExtensionType**](ExtensionType.md) |  | [optional] 

## Example

```python
from openapi_client.models.measurement_specific_characteristics import MeasurementSpecificCharacteristics

# TODO update the JSON string below
json = "{}"
# create an instance of MeasurementSpecificCharacteristics from a JSON string
measurement_specific_characteristics_instance = MeasurementSpecificCharacteristics.from_json(json)
# print the JSON string representation of the object
print(MeasurementSpecificCharacteristics.to_json())

# convert the object into a dict
measurement_specific_characteristics_dict = measurement_specific_characteristics_instance.to_dict()
# create an instance of MeasurementSpecificCharacteristics from a dict
measurement_specific_characteristics_from_dict = MeasurementSpecificCharacteristics.from_dict(measurement_specific_characteristics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


