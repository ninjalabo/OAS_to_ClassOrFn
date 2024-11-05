# MeasurementSiteTable


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**measurement_site_table_identification** | **str** |  | [optional] 
**measurement_sites** | [**List[MeasurementSite]**](MeasurementSite.md) |  | 
**information_manager** | [**InternationalIdentifier**](InternationalIdentifier.md) |  | [optional] 
**get_measurement_site_table_extension** | [**ExtensionType**](ExtensionType.md) |  | [optional] 
**id** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.measurement_site_table import MeasurementSiteTable

# TODO update the JSON string below
json = "{}"
# create an instance of MeasurementSiteTable from a JSON string
measurement_site_table_instance = MeasurementSiteTable.from_json(json)
# print the JSON string representation of the object
print(MeasurementSiteTable.to_json())

# convert the object into a dict
measurement_site_table_dict = measurement_site_table_instance.to_dict()
# create an instance of MeasurementSiteTable from a dict
measurement_site_table_from_dict = MeasurementSiteTable.from_dict(measurement_site_table_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


