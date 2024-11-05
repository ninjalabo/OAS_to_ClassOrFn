# MeasurementSiteTablePublication


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**publication_time** | **datetime** |  | 
**publication_creator** | [**InternationalIdentifier**](InternationalIdentifier.md) |  | 
**get_payload_publication_extension** | [**ExtensionType**](ExtensionType.md) |  | [optional] 
**lang** | **str** |  | [optional] 
**extension_name** | **str** |  | [optional] 
**extension_version** | **str** |  | [optional] 
**profile_name** | **str** |  | [optional] 
**profile_version** | **str** |  | [optional] 
**header_information** | [**HeaderInformation**](HeaderInformation.md) |  | 
**measurement_site_tables** | [**List[MeasurementSiteTable]**](MeasurementSiteTable.md) |  | 
**get_measurement_site_table_publication_extension** | [**ExtensionType**](ExtensionType.md) |  | [optional] 

## Example

```python
from openapi_client.models.measurement_site_table_publication import MeasurementSiteTablePublication

# TODO update the JSON string below
json = "{}"
# create an instance of MeasurementSiteTablePublication from a JSON string
measurement_site_table_publication_instance = MeasurementSiteTablePublication.from_json(json)
# print the JSON string representation of the object
print(MeasurementSiteTablePublication.to_json())

# convert the object into a dict
measurement_site_table_publication_dict = measurement_site_table_publication_instance.to_dict()
# create an instance of MeasurementSiteTablePublication from a dict
measurement_site_table_publication_from_dict = MeasurementSiteTablePublication.from_dict(measurement_site_table_publication_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


