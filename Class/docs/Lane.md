# Lane


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lane_number** | **int** |  | [optional] 
**lane_usage** | [**LaneEnum**](LaneEnum.md) |  | [optional] 
**get_lane_extension** | [**ExtensionType**](ExtensionType.md) |  | [optional] 

## Example

```python
from openapi_client.models.lane import Lane

# TODO update the JSON string below
json = "{}"
# create an instance of Lane from a JSON string
lane_instance = Lane.from_json(json)
# print the JSON string representation of the object
print(Lane.to_json())

# convert the object into a dict
lane_dict = lane_instance.to_dict()
# create an instance of Lane from a dict
lane_from_dict = Lane.from_dict(lane_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


