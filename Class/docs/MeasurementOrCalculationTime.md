# MeasurementOrCalculationTime


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_meaning** | [**TimeMeaningEnum**](TimeMeaningEnum.md) |  | [optional] 
**time_value** | **datetime** |  | [optional] 
**period** | [**Period**](Period.md) |  | [optional] 
**get_measurement_or_calculation_time_extension** | [**ExtensionType**](ExtensionType.md) |  | [optional] 
**time_precision** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.measurement_or_calculation_time import MeasurementOrCalculationTime

# TODO update the JSON string below
json = "{}"
# create an instance of MeasurementOrCalculationTime from a JSON string
measurement_or_calculation_time_instance = MeasurementOrCalculationTime.from_json(json)
# print the JSON string representation of the object
print(MeasurementOrCalculationTime.to_json())

# convert the object into a dict
measurement_or_calculation_time_dict = measurement_or_calculation_time_instance.to_dict()
# create an instance of MeasurementOrCalculationTime from a dict
measurement_or_calculation_time_from_dict = MeasurementOrCalculationTime.from_dict(measurement_or_calculation_time_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


