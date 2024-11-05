# WidthCharacteristic


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comparison_operator** | [**ComparisonOperatorEnum**](ComparisonOperatorEnum.md) |  | 
**vehicle_width** | **float** |  | [optional] 
**get_width_characteristic_extension** | [**ExtensionType**](ExtensionType.md) |  | [optional] 

## Example

```python
from openapi_client.models.width_characteristic import WidthCharacteristic

# TODO update the JSON string below
json = "{}"
# create an instance of WidthCharacteristic from a JSON string
width_characteristic_instance = WidthCharacteristic.from_json(json)
# print the JSON string representation of the object
print(WidthCharacteristic.to_json())

# convert the object into a dict
width_characteristic_dict = width_characteristic_instance.to_dict()
# create an instance of WidthCharacteristic from a dict
width_characteristic_from_dict = WidthCharacteristic.from_dict(width_characteristic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


