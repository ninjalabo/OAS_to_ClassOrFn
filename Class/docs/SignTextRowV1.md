# SignTextRowV1

Variable Sign text row

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**screen** | **int** | Screen number | [optional] 
**row_number** | **int** | Row number | [optional] 
**text** | **str** | Text on a row | [optional] 

## Example

```python
from openapi_client.models.sign_text_row_v1 import SignTextRowV1

# TODO update the JSON string below
json = "{}"
# create an instance of SignTextRowV1 from a JSON string
sign_text_row_v1_instance = SignTextRowV1.from_json(json)
# print the JSON string representation of the object
print(SignTextRowV1.to_json())

# convert the object into a dict
sign_text_row_v1_dict = sign_text_row_v1_instance.to_dict()
# create an instance of SignTextRowV1 from a dict
sign_text_row_v1_from_dict = SignTextRowV1.from_dict(sign_text_row_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


