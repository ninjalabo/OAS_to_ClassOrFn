# VariableSignPropertiesV1

Variable Sign properties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id | [optional] 
**type** | **str** | Type | [optional] 
**road_address** | **str** | Sign location as road address | [optional] 
**direction** | **str** | Direction of variable sign, increasing or decreasing road address | [optional] 
**carriageway** | **str** | Variable sign placement: SINGLE &#x3D; Single carriageway rod RIGHT &#x3D; First carriageway on the right in the direction of the road number LEFT &#x3D; Second carriageway on the left in the direction of the road number BETWEEN &#x3D; Between the carriageways | [optional] 
**display_value** | **str** | Value that is displayed on the device | [optional] 
**additional_information** | **str** | Additional information displayed on the device | [optional] 
**effect_date** | **datetime** | Information is effect after this date | [optional] 
**cause** | **str** | Cause for changing the sign: Automaatti &#x3D; Automatic Käsiohjaus &#x3D; By hand | [optional] 
**reliability** | **str** | Variable sign reliability | [optional] 
**text_rows** | [**List[SignTextRowV1]**](SignTextRowV1.md) | Text rows if sign contains a screen | [optional] 

## Example

```python
from openapi_client.models.variable_sign_properties_v1 import VariableSignPropertiesV1

# TODO update the JSON string below
json = "{}"
# create an instance of VariableSignPropertiesV1 from a JSON string
variable_sign_properties_v1_instance = VariableSignPropertiesV1.from_json(json)
# print the JSON string representation of the object
print(VariableSignPropertiesV1.to_json())

# convert the object into a dict
variable_sign_properties_v1_dict = variable_sign_properties_v1_instance.to_dict()
# create an instance of VariableSignPropertiesV1 from a dict
variable_sign_properties_v1_from_dict = VariableSignPropertiesV1.from_dict(variable_sign_properties_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


