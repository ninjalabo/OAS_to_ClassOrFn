# TrafficAnnouncementFeatureCollectionV1

GeoJSON Feature Collection of Traffic Announcements

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | GeoJSON Object Type | 
**data_updated_time** | **datetime** | Data last updated date time | 
**features** | [**List[TrafficAnnouncementFeatureV1]**](TrafficAnnouncementFeatureV1.md) | GeoJSON Feature Objects | 

## Example

```python
from openapi_client.models.traffic_announcement_feature_collection_v1 import TrafficAnnouncementFeatureCollectionV1

# TODO update the JSON string below
json = "{}"
# create an instance of TrafficAnnouncementFeatureCollectionV1 from a JSON string
traffic_announcement_feature_collection_v1_instance = TrafficAnnouncementFeatureCollectionV1.from_json(json)
# print the JSON string representation of the object
print(TrafficAnnouncementFeatureCollectionV1.to_json())

# convert the object into a dict
traffic_announcement_feature_collection_v1_dict = traffic_announcement_feature_collection_v1_instance.to_dict()
# create an instance of TrafficAnnouncementFeatureCollectionV1 from a dict
traffic_announcement_feature_collection_v1_from_dict = TrafficAnnouncementFeatureCollectionV1.from_dict(traffic_announcement_feature_collection_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


