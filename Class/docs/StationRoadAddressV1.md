# StationRoadAddressV1

Road station road address

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**road_number** | **int** | Road number (values 1–99999) | [optional] 
**road_section** | **int** | Road section (values 1–999) | [optional] 
**distance_from_road_section_start** | **int** | Distance from start of the road portion [m] | [optional] 
**carriageway** | **str** | Carriageway &lt;br&gt;ONE_CARRIAGEWAY:                                0 &#x3D; One carriageway road section &lt;br&gt;DUAL_CARRIAGEWAY_RIGHT_IN_INCREASING_DIRECTION: 1 &#x3D; Dual carriageway&#39;s right carriageway on increasing direction &lt;br&gt;DUAL_CARRIAGEWAY_LEFT_IN_INCREASING_DIRECTION:  2 &#x3D; Dual carriageway&#39;s left carriageway on increasing direction (upstream) | [optional] 
**side** | **str** | Road address side information &lt;br&gt;* UNKNOWN: 0 &#x3D; Unknown, &lt;br&gt;* RIGHT    1 &#x3D; On the right side of the carriageway in the increasing direction, &lt;br&gt;* LEFT:    2 &#x3D; On the left side of the carriageway in the increasing direction, &lt;br&gt;* BETWEEN: 3 &#x3D; Between the carriageways, &lt;br&gt;* END:     7 &#x3D; At the end of the road, &lt;br&gt;* MIDDLE:  8 &#x3D; In the middle of the carriageway / on the carriageway, &lt;br&gt;* CROSS:   9 &#x3D; Across the road | [optional] 
**contract_area** | **str** | Road contract area | [optional] 
**contract_area_code** | **int** | Road contract area code | [optional] 

## Example

```python
from openapi_client.models.station_road_address_v1 import StationRoadAddressV1

# TODO update the JSON string below
json = "{}"
# create an instance of StationRoadAddressV1 from a JSON string
station_road_address_v1_instance = StationRoadAddressV1.from_json(json)
# print the JSON string representation of the object
print(StationRoadAddressV1.to_json())

# convert the object into a dict
station_road_address_v1_dict = station_road_address_v1_instance.to_dict()
# create an instance of StationRoadAddressV1 from a dict
station_road_address_v1_from_dict = StationRoadAddressV1.from_dict(station_road_address_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


