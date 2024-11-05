# WeathercamPresetDetailedV1

Weathercam preset object with detailed information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id of preset | [optional] 
**presentation_name** | **str** | PresentationName (Preset name 1, direction) | [optional] 
**in_collection** | **bool** | Is preset in collection | [optional] 
**resolution** | **str** | Resolution of camera [px x px] | [optional] 
**direction_code** | **str** | Preset direction:&lt;br&gt; 0 &#x3D; Unknown direction.&lt;br&gt; 1 &#x3D; According to the road register address increasing direction. I.e. on the road 4 to Lahti, if we are in Korso.&lt;br&gt; 2 &#x3D; According to the road register address decreasing direction. I.e. on the road 4 to Helsinki, if we are in Korso.&lt;br&gt; 3 &#x3D; Increasing direction of the crossing road.&lt;br&gt; 4 &#x3D; Decreasing direction of the crossing road.&lt;br&gt; 5-99 &#x3D; Special directions | 
**image_url** | **str** | Image url | [optional] 
**direction** | [**WeathercamPresetDirectionV1**](WeathercamPresetDirectionV1.md) |  | 

## Example

```python
from openapi_client.models.weathercam_preset_detailed_v1 import WeathercamPresetDetailedV1

# TODO update the JSON string below
json = "{}"
# create an instance of WeathercamPresetDetailedV1 from a JSON string
weathercam_preset_detailed_v1_instance = WeathercamPresetDetailedV1.from_json(json)
# print the JSON string representation of the object
print(WeathercamPresetDetailedV1.to_json())

# convert the object into a dict
weathercam_preset_detailed_v1_dict = weathercam_preset_detailed_v1_instance.to_dict()
# create an instance of WeathercamPresetDetailedV1 from a dict
weathercam_preset_detailed_v1_from_dict = WeathercamPresetDetailedV1.from_dict(weathercam_preset_detailed_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


