# UpdateInfoDtoV1

Info about API data updates (update intervals, last updated times)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api** | **str** | Url of the API | 
**subtype** | **str** | More specific info about API. Ie. domain info. | [optional] 
**data_updated_time** | **datetime** | Data last updated time | 
**data_checked_time** | **datetime** | Latest check for data updates.  &lt;br&gt; &#x60;null&#x60; value indicates data being pushed to our platform or static data that is only updated when needed. | [optional] 
**data_update_interval** | **str** | Data update interval in ISO-8601 duration format &#x60;PnDTnHnMn.nS&#x60;. &lt;br&gt; &#x60;P0S&#x60; means that data is updated in nearly real time. &lt;br&gt; &#x60;null&#x60; means that data is static and updated only when needed. | [optional] 
**recommended_fetch_interval** | **str** | Recommended fetch interval for clients in ISO-8601 duration format &#x60;PnDTnHnMn.nS&#x60; | 

## Example

```python
from openapi_client.models.update_info_dto_v1 import UpdateInfoDtoV1

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateInfoDtoV1 from a JSON string
update_info_dto_v1_instance = UpdateInfoDtoV1.from_json(json)
# print the JSON string representation of the object
print(UpdateInfoDtoV1.to_json())

# convert the object into a dict
update_info_dto_v1_dict = update_info_dto_v1_instance.to_dict()
# create an instance of UpdateInfoDtoV1 from a dict
update_info_dto_v1_from_dict = UpdateInfoDtoV1.from_dict(update_info_dto_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


