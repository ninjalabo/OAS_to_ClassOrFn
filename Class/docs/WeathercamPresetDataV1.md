# WeathercamPresetDataV1

Weathercam preset's latest image capture data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id of the weathercam preset | 
**measured_time** | **datetime** | Latest measurement time | 

## Example

```python
from openapi_client.models.weathercam_preset_data_v1 import WeathercamPresetDataV1

# TODO update the JSON string below
json = "{}"
# create an instance of WeathercamPresetDataV1 from a JSON string
weathercam_preset_data_v1_instance = WeathercamPresetDataV1.from_json(json)
# print the JSON string representation of the object
print(WeathercamPresetDataV1.to_json())

# convert the object into a dict
weathercam_preset_data_v1_dict = weathercam_preset_data_v1_instance.to_dict()
# create an instance of WeathercamPresetDataV1 from a dict
weathercam_preset_data_v1_from_dict = WeathercamPresetDataV1.from_dict(weathercam_preset_data_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


