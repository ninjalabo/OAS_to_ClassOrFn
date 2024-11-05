# openapi_client.VariableSignV1Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_variable_sign_v1_images_text_get**](VariableSignV1Api.md#api_variable_sign_v1_images_text_get) | **GET** /api/variable-sign/v1/images/{text} | Generate svg-image from given text
[**api_variable_sign_v1_signs_datex2_get**](VariableSignV1Api.md#api_variable_sign_v1_signs_datex2_get) | **GET** /api/variable-sign/v1/signs.datex2 | Return all variables signs as datex2
[**get_code_descriptions**](VariableSignV1Api.md#get_code_descriptions) | **GET** /api/variable-sign/v1/signs/code-descriptions | Return all code descriptions.
[**variable_sign_by_path**](VariableSignV1Api.md#variable_sign_by_path) | **GET** /api/variable-sign/v1/signs/{deviceId} | Return the latest value of a variable sign
[**variable_sign_history**](VariableSignV1Api.md#variable_sign_history) | **GET** /api/variable-sign/v1/signs/history | Return the history of variable sign data
[**variable_signs**](VariableSignV1Api.md#variable_signs) | **GET** /api/variable-sign/v1/signs | Return the latest data of variable signs. If deviceId is given, latest data for that sign will be returned, otherwise return the latest data for each sign from the last 7 days.


# **api_variable_sign_v1_images_text_get**
> object api_variable_sign_v1_images_text_get(text)

Generate svg-image from given text

### Example


```python
import openapi_client
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
    api_instance = openapi_client.VariableSignV1Api(api_client)
    text = 'text_example' # str | 

    try:
        # Generate svg-image from given text
        api_response = api_instance.api_variable_sign_v1_images_text_get(text)
        print("The response of VariableSignV1Api->api_variable_sign_v1_images_text_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VariableSignV1Api->api_variable_sign_v1_images_text_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/svg+xml, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response |  * Access-Control-Allow-Origin -  <br>  |
**400** | 400 response |  * Access-Control-Allow-Origin -  <br>  |
**500** | 500 response |  * Access-Control-Allow-Origin -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_variable_sign_v1_signs_datex2_get**
> object api_variable_sign_v1_signs_datex2_get()

Return all variables signs as datex2

### Example


```python
import openapi_client
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
    api_instance = openapi_client.VariableSignV1Api(api_client)

    try:
        # Return all variables signs as datex2
        api_response = api_instance.api_variable_sign_v1_signs_datex2_get()
        print("The response of VariableSignV1Api->api_variable_sign_v1_signs_datex2_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VariableSignV1Api->api_variable_sign_v1_signs_datex2_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response |  * Access-Control-Allow-Origin -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_code_descriptions**
> VariableSignDescriptions get_code_descriptions()

Return all code descriptions.

### Example


```python
import openapi_client
from openapi_client.models.variable_sign_descriptions import VariableSignDescriptions
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
    api_instance = openapi_client.VariableSignV1Api(api_client)

    try:
        # Return all code descriptions.
        api_response = api_instance.get_code_descriptions()
        print("The response of VariableSignV1Api->get_code_descriptions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VariableSignV1Api->get_code_descriptions: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**VariableSignDescriptions**](VariableSignDescriptions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **variable_sign_by_path**
> VariableSignFeatureCollectionV1 variable_sign_by_path(device_id)

Return the latest value of a variable sign

### Example


```python
import openapi_client
from openapi_client.models.variable_sign_feature_collection_v1 import VariableSignFeatureCollectionV1
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
    api_instance = openapi_client.VariableSignV1Api(api_client)
    device_id = 'device_id_example' # str | 

    try:
        # Return the latest value of a variable sign
        api_response = api_instance.variable_sign_by_path(device_id)
        print("The response of VariableSignV1Api->variable_sign_by_path:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VariableSignV1Api->variable_sign_by_path: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  | 

### Return type

[**VariableSignFeatureCollectionV1**](VariableSignFeatureCollectionV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of variable sign data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **variable_sign_history**
> List[TrafficSignHistoryV1] variable_sign_history(device_id, effective_date=effective_date)

Return the history of variable sign data

### Example


```python
import openapi_client
from openapi_client.models.traffic_sign_history_v1 import TrafficSignHistoryV1
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
    api_instance = openapi_client.VariableSignV1Api(api_client)
    device_id = 'device_id_example' # str | Id of sign.
    effective_date = '2013-10-20T19:20:30+01:00' # datetime | When a date is given, return only history for that day.  This is date of UTC-0 time. (optional)

    try:
        # Return the history of variable sign data
        api_response = api_instance.variable_sign_history(device_id, effective_date=effective_date)
        print("The response of VariableSignV1Api->variable_sign_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VariableSignV1Api->variable_sign_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Id of sign. | 
 **effective_date** | **datetime**| When a date is given, return only history for that day.  This is date of UTC-0 time. | [optional] 

### Return type

[**List[TrafficSignHistoryV1]**](TrafficSignHistoryV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of variable sign history |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **variable_signs**
> VariableSignFeatureCollectionV1 variable_signs(device_id=device_id)

Return the latest data of variable signs. If deviceId is given, latest data for that sign will be returned, otherwise return the latest data for each sign from the last 7 days.

### Example


```python
import openapi_client
from openapi_client.models.variable_sign_feature_collection_v1 import VariableSignFeatureCollectionV1
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
    api_instance = openapi_client.VariableSignV1Api(api_client)
    device_id = 'device_id_example' # str | If parameter is given list only latest value of given sign (optional)

    try:
        # Return the latest data of variable signs. If deviceId is given, latest data for that sign will be returned, otherwise return the latest data for each sign from the last 7 days.
        api_response = api_instance.variable_signs(device_id=device_id)
        print("The response of VariableSignV1Api->variable_signs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VariableSignV1Api->variable_signs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| If parameter is given list only latest value of given sign | [optional] 

### Return type

[**VariableSignFeatureCollectionV1**](VariableSignFeatureCollectionV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of variable sign data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

