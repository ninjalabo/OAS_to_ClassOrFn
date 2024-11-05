# openapi_client.InfoV1Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**data_updated_infos**](InfoV1Api.md#data_updated_infos) | **GET** /api/info/v1/update-times | Infos about apis data update times


# **data_updated_infos**
> UpdateInfosDtoV1 data_updated_infos()

Infos about apis data update times

This API returns info about data update intervals, when data is last updated and how often should API to be called by client.  For `dataUpdateInterval` field the `P0S` value has special meaning that data is updated nearly in real time.  `null` value indicates static data and it is only updated when needed.

### Example


```python
import openapi_client
from openapi_client.models.update_infos_dto_v1 import UpdateInfosDtoV1
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.InfoV1Api(api_client)

    try:
        # Infos about apis data update times
        api_response = api_instance.data_updated_infos()
        print("The response of InfoV1Api->data_updated_infos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfoV1Api->data_updated_infos: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**UpdateInfosDtoV1**](UpdateInfosDtoV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of info data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

