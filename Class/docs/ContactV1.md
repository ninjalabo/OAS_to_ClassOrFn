# ContactV1

Sender's contact information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phone** | **str** | Phone number | [optional] 
**email** | **str** | Email | [optional] 

## Example

```python
from openapi_client.models.contact_v1 import ContactV1

# TODO update the JSON string below
json = "{}"
# create an instance of ContactV1 from a JSON string
contact_v1_instance = ContactV1.from_json(json)
# print the JSON string representation of the object
print(ContactV1.to_json())

# convert the object into a dict
contact_v1_dict = contact_v1_instance.to_dict()
# create an instance of ContactV1 from a dict
contact_v1_from_dict = ContactV1.from_dict(contact_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


