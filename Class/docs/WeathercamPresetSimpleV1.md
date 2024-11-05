# WeathercamPresetSimpleV1

Weathercam preset object with basic information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id of preset | [optional] 
**in_collection** | **bool** | Is preset in collection | [optional] 

## Example

```python
from openapi_client.models.weathercam_preset_simple_v1 import WeathercamPresetSimpleV1

# TODO update the JSON string below
json = "{}"
# create an instance of WeathercamPresetSimpleV1 from a JSON string
weathercam_preset_simple_v1_instance = WeathercamPresetSimpleV1.from_json(json)
# print the JSON string representation of the object
print(WeathercamPresetSimpleV1.to_json())

# convert the object into a dict
weathercam_preset_simple_v1_dict = weathercam_preset_simple_v1_instance.to_dict()
# create an instance of WeathercamPresetSimpleV1 from a dict
weathercam_preset_simple_v1_from_dict = WeathercamPresetSimpleV1.from_dict(weathercam_preset_simple_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


