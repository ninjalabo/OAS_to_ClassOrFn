# MeasurementSite


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**measurement_site_record_version_time** | **datetime** |  | [optional] 
**measurement_equipment_reference** | **str** |  | [optional] 
**measurement_equipment_type_used** | [**MultilingualString**](MultilingualString.md) |  | [optional] 
**measurement_site_name** | [**MultilingualString**](MultilingualString.md) |  | [optional] 
**measurement_site_number_of_lanes** | **int** |  | [optional] 
**measurement_site_identification** | **str** |  | [optional] 
**measurement_specific_characteristics** | [**List[MeasurementSiteIndexMeasurementSpecificCharacteristics]**](MeasurementSiteIndexMeasurementSpecificCharacteristics.md) |  | [optional] 
**measurement_site_location** | [**LocationReference**](LocationReference.md) |  | 
**information_manager_override** | [**InternationalIdentifier**](InternationalIdentifier.md) |  | [optional] 
**get_measurement_site_extension** | [**ExtensionType**](ExtensionType.md) |  | [optional] 
**id** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.measurement_site import MeasurementSite

# TODO update the JSON string below
json = "{}"
# create an instance of MeasurementSite from a JSON string
measurement_site_instance = MeasurementSite.from_json(json)
# print the JSON string representation of the object
print(MeasurementSite.to_json())

# convert the object into a dict
measurement_site_dict = measurement_site_instance.to_dict()
# create an instance of MeasurementSite from a dict
measurement_site_from_dict = MeasurementSite.from_dict(measurement_site_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


