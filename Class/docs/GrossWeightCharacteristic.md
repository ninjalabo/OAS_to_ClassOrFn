# GrossWeightCharacteristic


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comparison_operator** | [**ComparisonOperatorEnum**](ComparisonOperatorEnum.md) |  | 
**gross_vehicle_weight** | **float** |  | [optional] 
**type_of_weight** | [**WeightTypeEnum**](WeightTypeEnum.md) |  | 
**get_gross_weight_characteristic_extension** | [**ExtensionType**](ExtensionType.md) |  | [optional] 

## Example

```python
from openapi_client.models.gross_weight_characteristic import GrossWeightCharacteristic

# TODO update the JSON string below
json = "{}"
# create an instance of GrossWeightCharacteristic from a JSON string
gross_weight_characteristic_instance = GrossWeightCharacteristic.from_json(json)
# print the JSON string representation of the object
print(GrossWeightCharacteristic.to_json())

# convert the object into a dict
gross_weight_characteristic_dict = gross_weight_characteristic_instance.to_dict()
# create an instance of GrossWeightCharacteristic from a dict
gross_weight_characteristic_from_dict = GrossWeightCharacteristic.from_dict(gross_weight_characteristic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


