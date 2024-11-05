# ForecastSectionPropertiesV1

Forecast Section Properties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Forecast section identifier ie. 00004_342_01435_0_274.569:  1. Road number 5 characters ie. 00004,  2. Road section 3 characters ie. 342,  3. Start distance 5 characters ie. 000,  4. Carriageway 1 character,  5. Measure value of link start point. Varying number of characters ie. 274.569,  Refers to Digiroad content at https://aineistot.vayla.fi/digiroad/ | [optional] 
**description** | **str** | Forecast section description | [optional] 
**road_section_number** | **int** | Road section number | [optional] 
**road_number** | **int** | Forecast section road number | [optional] 
**length** | **int** | Forecast section length in meters | [optional] 
**road_segments** | [**List[RoadSegmentDtoV1]**](RoadSegmentDtoV1.md) | Forecast section road segments. Refers to https://aineistot.vayla.fi/digiroad/ | [optional] 
**link_ids** | **List[int]** | Forecast section link indices. Refers to https://aineistot.vayla.fi/digiroad/ | [optional] 
**data_updated_time** | **datetime** | Data last updated date time | 

## Example

```python
from openapi_client.models.forecast_section_properties_v1 import ForecastSectionPropertiesV1

# TODO update the JSON string below
json = "{}"
# create an instance of ForecastSectionPropertiesV1 from a JSON string
forecast_section_properties_v1_instance = ForecastSectionPropertiesV1.from_json(json)
# print the JSON string representation of the object
print(ForecastSectionPropertiesV1.to_json())

# convert the object into a dict
forecast_section_properties_v1_dict = forecast_section_properties_v1_instance.to_dict()
# create an instance of ForecastSectionPropertiesV1 from a dict
forecast_section_properties_v1_from_dict = ForecastSectionPropertiesV1.from_dict(forecast_section_properties_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


