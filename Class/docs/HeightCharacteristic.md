# HeightCharacteristic


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comparison_operator** | [**ComparisonOperatorEnum**](ComparisonOperatorEnum.md) |  | 
**vehicle_height** | **float** |  | [optional] 
**get_height_characteristic_extension** | [**ExtensionType**](ExtensionType.md) |  | [optional] 

## Example

```python
from openapi_client.models.height_characteristic import HeightCharacteristic

# TODO update the JSON string below
json = "{}"
# create an instance of HeightCharacteristic from a JSON string
height_characteristic_instance = HeightCharacteristic.from_json(json)
# print the JSON string representation of the object
print(HeightCharacteristic.to_json())

# convert the object into a dict
height_characteristic_dict = height_characteristic_instance.to_dict()
# create an instance of HeightCharacteristic from a dict
height_characteristic_from_dict = HeightCharacteristic.from_dict(height_characteristic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


