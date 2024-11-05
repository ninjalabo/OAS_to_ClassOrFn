# AlertCLocationV1

AlertC location

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location_code** | **int** | AlertC location code. Number of the location point in AlertC location table | 
**name** | **str** | Location point name | 
**distance** | **int** | Distance of the road point from the AlertC location point | [optional] 

## Example

```python
from openapi_client.models.alert_c_location_v1 import AlertCLocationV1

# TODO update the JSON string below
json = "{}"
# create an instance of AlertCLocationV1 from a JSON string
alert_c_location_v1_instance = AlertCLocationV1.from_json(json)
# print the JSON string representation of the object
print(AlertCLocationV1.to_json())

# convert the object into a dict
alert_c_location_v1_dict = alert_c_location_v1_instance.to_dict()
# create an instance of AlertCLocationV1 from a dict
alert_c_location_v1_from_dict = AlertCLocationV1.from_dict(alert_c_location_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


