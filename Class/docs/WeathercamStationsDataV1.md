# WeathercamStationsDataV1

Weathercam stations' data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_updated_time** | **datetime** | Time when data was last updated | 
**stations** | [**List[WeathercamStationDataV1]**](WeathercamStationDataV1.md) | Stations data | [optional] 

## Example

```python
from openapi_client.models.weathercam_stations_data_v1 import WeathercamStationsDataV1

# TODO update the JSON string below
json = "{}"
# create an instance of WeathercamStationsDataV1 from a JSON string
weathercam_stations_data_v1_instance = WeathercamStationsDataV1.from_json(json)
# print the JSON string representation of the object
print(WeathercamStationsDataV1.to_json())

# convert the object into a dict
weathercam_stations_data_v1_dict = weathercam_stations_data_v1_instance.to_dict()
# create an instance of WeathercamStationsDataV1 from a dict
weathercam_stations_data_v1_from_dict = WeathercamStationsDataV1.from_dict(weathercam_stations_data_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


