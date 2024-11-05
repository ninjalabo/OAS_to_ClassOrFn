# HeaviestAxleWeightCharacteristic


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comparison_operator** | [**ComparisonOperatorEnum**](ComparisonOperatorEnum.md) |  | 
**heaviest_axle_weight** | **float** |  | [optional] 
**get_heaviest_axle_weight_characteristic_extension** | [**ExtensionType**](ExtensionType.md) |  | [optional] 

## Example

```python
from openapi_client.models.heaviest_axle_weight_characteristic import HeaviestAxleWeightCharacteristic

# TODO update the JSON string below
json = "{}"
# create an instance of HeaviestAxleWeightCharacteristic from a JSON string
heaviest_axle_weight_characteristic_instance = HeaviestAxleWeightCharacteristic.from_json(json)
# print the JSON string representation of the object
print(HeaviestAxleWeightCharacteristic.to_json())

# convert the object into a dict
heaviest_axle_weight_characteristic_dict = heaviest_axle_weight_characteristic_instance.to_dict()
# create an instance of HeaviestAxleWeightCharacteristic from a dict
heaviest_axle_weight_characteristic_from_dict = HeaviestAxleWeightCharacteristic.from_dict(heaviest_axle_weight_characteristic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


