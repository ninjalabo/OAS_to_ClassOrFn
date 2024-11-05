# CameraHistory

Weather camera's image history details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_updated_time** | **datetime** | Time when data was last updated | 
**stations** | [**List[PresetHistory]**](PresetHistory.md) | Stations data | [optional] 

## Example

```python
from openapi_client.models.camera_history import CameraHistory

# TODO update the JSON string below
json = "{}"
# create an instance of CameraHistory from a JSON string
camera_history_instance = CameraHistory.from_json(json)
# print the JSON string representation of the object
print(CameraHistory.to_json())

# convert the object into a dict
camera_history_dict = camera_history_instance.to_dict()
# create an instance of CameraHistory from a dict
camera_history_from_dict = CameraHistory.from_dict(camera_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


