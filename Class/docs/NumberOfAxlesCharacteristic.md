# NumberOfAxlesCharacteristic


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comparison_operator** | [**ComparisonOperatorEnum**](ComparisonOperatorEnum.md) |  | 
**number_of_axles** | **int** |  | 
**get_number_of_axles_characteristic_extension** | [**ExtensionType**](ExtensionType.md) |  | [optional] 

## Example

```python
from openapi_client.models.number_of_axles_characteristic import NumberOfAxlesCharacteristic

# TODO update the JSON string below
json = "{}"
# create an instance of NumberOfAxlesCharacteristic from a JSON string
number_of_axles_characteristic_instance = NumberOfAxlesCharacteristic.from_json(json)
# print the JSON string representation of the object
print(NumberOfAxlesCharacteristic.to_json())

# convert the object into a dict
number_of_axles_characteristic_dict = number_of_axles_characteristic_instance.to_dict()
# create an instance of NumberOfAxlesCharacteristic from a dict
number_of_axles_characteristic_from_dict = NumberOfAxlesCharacteristic.from_dict(number_of_axles_characteristic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


