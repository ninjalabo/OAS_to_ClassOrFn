# MeasuredDataPublication


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
**measurement_site_table_references** | [**List[MeasurementSiteTableVersionedReference]**](MeasurementSiteTableVersionedReference.md) |  | 
**header_information** | [**HeaderInformation**](HeaderInformation.md) |  | 
**site_measurements** | [**List[SiteMeasurements]**](SiteMeasurements.md) |  | 
**get_measured_data_publication_extension** | [**ExtensionType**](ExtensionType.md) |  | [optional] 

## Example

```python
from openapi_client.models.measured_data_publication import MeasuredDataPublication

# TODO update the JSON string below
json = "{}"
# create an instance of MeasuredDataPublication from a JSON string
measured_data_publication_instance = MeasuredDataPublication.from_json(json)
# print the JSON string representation of the object
print(MeasuredDataPublication.to_json())

# convert the object into a dict
measured_data_publication_dict = measured_data_publication_instance.to_dict()
# create an instance of MeasuredDataPublication from a dict
measured_data_publication_from_dict = MeasuredDataPublication.from_dict(measured_data_publication_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


