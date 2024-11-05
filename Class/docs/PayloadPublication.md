# PayloadPublication


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feed_description** | [**MultilingualString**](MultilingualString.md) |  | [optional] 
**feed_type** | **str** |  | [optional] 
**publication_time** | **datetime** |  | 
**publication_creator** | [**InternationalIdentifier**](InternationalIdentifier.md) |  | 
**payload_publication_extension** | [**ExtensionType**](ExtensionType.md) |  | [optional] 
**lang** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.payload_publication import PayloadPublication

# TODO update the JSON string below
json = "{}"
# create an instance of PayloadPublication from a JSON string
payload_publication_instance = PayloadPublication.from_json(json)
# print the JSON string representation of the object
print(PayloadPublication.to_json())

# convert the object into a dict
payload_publication_dict = payload_publication_instance.to_dict()
# create an instance of PayloadPublication from a dict
payload_publication_from_dict = PayloadPublication.from_dict(payload_publication_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


