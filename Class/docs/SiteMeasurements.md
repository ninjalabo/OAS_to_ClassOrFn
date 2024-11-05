# SiteMeasurements


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**measurement_site_reference** | [**MeasurementSiteVersionedReference**](MeasurementSiteVersionedReference.md) |  | 
**physical_quantities** | [**List[SiteMeasurementsIndexPhysicalQuantity]**](SiteMeasurementsIndexPhysicalQuantity.md) |  | [optional] 
**measurement_time_default** | [**MeasurementOrCalculationTime**](MeasurementOrCalculationTime.md) |  | 
**get_site_measurements_extension** | [**ExtensionType**](ExtensionType.md) |  | [optional] 

## Example

```python
from openapi_client.models.site_measurements import SiteMeasurements

# TODO update the JSON string below
json = "{}"
# create an instance of SiteMeasurements from a JSON string
site_measurements_instance = SiteMeasurements.from_json(json)
# print the JSON string representation of the object
print(SiteMeasurements.to_json())

# convert the object into a dict
site_measurements_dict = site_measurements_instance.to_dict()
# create an instance of SiteMeasurements from a dict
site_measurements_from_dict = SiteMeasurements.from_dict(site_measurements_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


