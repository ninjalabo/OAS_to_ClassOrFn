# TrafficAnnouncementFeatureV1

TrafficAnnouncement GeoJSON Feature Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | GeoJSON Object Type | 
**geometry** | [**ForecastSectionFeatureV1Geometry**](ForecastSectionFeatureV1Geometry.md) |  | 
**properties** | [**TrafficAnnouncementPropertiesV1**](TrafficAnnouncementPropertiesV1.md) |  | 

## Example

```python
from openapi_client.models.traffic_announcement_feature_v1 import TrafficAnnouncementFeatureV1

# TODO update the JSON string below
json = "{}"
# create an instance of TrafficAnnouncementFeatureV1 from a JSON string
traffic_announcement_feature_v1_instance = TrafficAnnouncementFeatureV1.from_json(json)
# print the JSON string representation of the object
print(TrafficAnnouncementFeatureV1.to_json())

# convert the object into a dict
traffic_announcement_feature_v1_dict = traffic_announcement_feature_v1_instance.to_dict()
# create an instance of TrafficAnnouncementFeatureV1 from a dict
traffic_announcement_feature_v1_from_dict = TrafficAnnouncementFeatureV1.from_dict(traffic_announcement_feature_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


