# Emissions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**emission_classification_euro** | [**EmissionClassificationEuroEnum**](EmissionClassificationEuroEnum.md) |  | [optional] 
**emission_classification_others** | **List[str]** |  | [optional] 
**emission_level** | [**LowEmissionLevelEnum**](LowEmissionLevelEnum.md) |  | [optional] 
**get_emissions_extension** | [**EmissionsExtensionType**](EmissionsExtensionType.md) |  | [optional] 

## Example

```python
from openapi_client.models.emissions import Emissions

# TODO update the JSON string below
json = "{}"
# create an instance of Emissions from a JSON string
emissions_instance = Emissions.from_json(json)
# print the JSON string representation of the object
print(Emissions.to_json())

# convert the object into a dict
emissions_dict = emissions_instance.to_dict()
# create an instance of Emissions from a dict
emissions_from_dict = Emissions.from_dict(emissions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


