# RestrictionV1

A single phase in a larger road work

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the restriction. | [optional] 
**restriction** | [**FeatureV1**](FeatureV1.md) |  | [optional] 

## Example

```python
from openapi_client.models.restriction_v1 import RestrictionV1

# TODO update the JSON string below
json = "{}"
# create an instance of RestrictionV1 from a JSON string
restriction_v1_instance = RestrictionV1.from_json(json)
# print the JSON string representation of the object
print(RestrictionV1.to_json())

# convert the object into a dict
restriction_v1_dict = restriction_v1_instance.to_dict()
# create an instance of RestrictionV1 from a dict
restriction_v1_from_dict = RestrictionV1.from_dict(restriction_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


