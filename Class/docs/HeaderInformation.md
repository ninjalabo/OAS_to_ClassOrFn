# HeaderInformation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confidentiality** | [**ConfidentialityValueEnum**](ConfidentialityValueEnum.md) |  | [optional] 
**allowed_delivery_channels** | [**List[InformationDeliveryServicesEnum]**](InformationDeliveryServicesEnum.md) |  | [optional] 
**information_status** | [**InformationStatusEnum**](InformationStatusEnum.md) |  | 
**get_header_information_extension** | [**ExtensionType**](ExtensionType.md) |  | [optional] 

## Example

```python
from openapi_client.models.header_information import HeaderInformation

# TODO update the JSON string below
json = "{}"
# create an instance of HeaderInformation from a JSON string
header_information_instance = HeaderInformation.from_json(json)
# print the JSON string representation of the object
print(HeaderInformation.to_json())

# convert the object into a dict
header_information_dict = header_information_instance.to_dict()
# create an instance of HeaderInformation from a dict
header_information_from_dict = HeaderInformation.from_dict(header_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


