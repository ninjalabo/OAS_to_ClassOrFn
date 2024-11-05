# ForecastConditionReasonDtoV1

Forecast that is used is Vaisala’s weather forecast which is initialised from the weather model that performs best for Finland for a period under study. Majority of the times the initialisation is done from ECMWF model data. Then Vaisala meteorologists also manually edit the data to fix certain known errors in the model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**precipitation_condition** | **str** | Precipitation condition:&lt;br&gt; 0 &#x3D; no data available,&lt;br&gt; 1 &#x3D; rain intensity lt 0.2 mm/h,&lt;br&gt; 2 &#x3D; rain intensity ge 0.2 mm/h,&lt;br&gt; 3 &#x3D; rain intensity ge 2.5 mm/h,&lt;br&gt; 4 &#x3D; rain intensity ge 7.6 mm/h,&lt;br&gt; 5 &#x3D; snowing intensity ge 0.2 cm/h,&lt;br&gt; 6 &#x3D; snowing intensity ge 1 cm/h,&lt;br&gt; 7 &#x3D; snowing intensity ge 3 cm/h&lt;br&gt; (lt &#x3D; lower than, ge &#x3D; greater or equal) | [optional] 
**road_condition** | **str** | The state of the road | [optional] 
**wind_condition** | **str** | The strength of wind | [optional] 
**freezing_rain_condition** | **bool** | Tells if there is freezing rain: true/false | [optional] 
**winter_slipperiness** | **bool** | Tells if it is slippery: true/false | [optional] 
**visibility_condition** | **str** | Visibility | [optional] 
**friction_condition** | **str** | The amount of friction on the road | [optional] 

## Example

```python
from openapi_client.models.forecast_condition_reason_dto_v1 import ForecastConditionReasonDtoV1

# TODO update the JSON string below
json = "{}"
# create an instance of ForecastConditionReasonDtoV1 from a JSON string
forecast_condition_reason_dto_v1_instance = ForecastConditionReasonDtoV1.from_json(json)
# print the JSON string representation of the object
print(ForecastConditionReasonDtoV1.to_json())

# convert the object into a dict
forecast_condition_reason_dto_v1_dict = forecast_condition_reason_dto_v1_instance.to_dict()
# create an instance of ForecastConditionReasonDtoV1 from a dict
forecast_condition_reason_dto_v1_from_dict = ForecastConditionReasonDtoV1.from_dict(forecast_condition_reason_dto_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


