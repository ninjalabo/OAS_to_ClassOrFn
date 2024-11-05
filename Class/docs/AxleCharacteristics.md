# AxleCharacteristics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maximum_weight** | **float** |  | [optional] 
**minimum_weight** | **float** |  | [optional] 
**get_axle_characteristics_extension** | [**ExtensionType**](ExtensionType.md) |  | [optional] 

## Example

```python
from openapi_client.models.axle_characteristics import AxleCharacteristics

# TODO update the JSON string below
json = "{}"
# create an instance of AxleCharacteristics from a JSON string
axle_characteristics_instance = AxleCharacteristics.from_json(json)
# print the JSON string representation of the object
print(AxleCharacteristics.to_json())

# convert the object into a dict
axle_characteristics_dict = axle_characteristics_instance.to_dict()
# create an instance of AxleCharacteristics from a dict
axle_characteristics_from_dict = AxleCharacteristics.from_dict(axle_characteristics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


