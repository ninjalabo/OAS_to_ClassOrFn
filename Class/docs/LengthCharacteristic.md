# LengthCharacteristic


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comparison_operator** | [**ComparisonOperatorEnum**](ComparisonOperatorEnum.md) |  | 
**vehicle_length** | **float** |  | [optional] 
**get_length_characteristic_extension** | [**ExtensionType**](ExtensionType.md) |  | [optional] 

## Example

```python
from openapi_client.models.length_characteristic import LengthCharacteristic

# TODO update the JSON string below
json = "{}"
# create an instance of LengthCharacteristic from a JSON string
length_characteristic_instance = LengthCharacteristic.from_json(json)
# print the JSON string representation of the object
print(LengthCharacteristic.to_json())

# convert the object into a dict
length_characteristic_dict = length_characteristic_instance.to_dict()
# create an instance of LengthCharacteristic from a dict
length_characteristic_from_dict = LengthCharacteristic.from_dict(length_characteristic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


