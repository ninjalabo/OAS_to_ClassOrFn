# openapi_client.CountingSiteV1Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_counting_site_v1_counters_counter_id_get**](CountingSiteV1Api.md#api_counting_site_v1_counters_counter_id_get) | **GET** /api/counting-site/v1/counters/{counterId} | Return single counter
[**api_counting_site_v1_counters_get**](CountingSiteV1Api.md#api_counting_site_v1_counters_get) | **GET** /api/counting-site/v1/counters | Return all counters for domain
[**api_counting_site_v1_directions_get**](CountingSiteV1Api.md#api_counting_site_v1_directions_get) | **GET** /api/counting-site/v1/directions | Return all directions
[**api_counting_site_v1_domains_get**](CountingSiteV1Api.md#api_counting_site_v1_domains_get) | **GET** /api/counting-site/v1/domains | Return all domains
[**api_counting_site_v1_user_types_get**](CountingSiteV1Api.md#api_counting_site_v1_user_types_get) | **GET** /api/counting-site/v1/user-types | Return all user types
[**api_counting_site_v1_values_csv_get**](CountingSiteV1Api.md#api_counting_site_v1_values_csv_get) | **GET** /api/counting-site/v1/values.csv | Return counter values in CSV. If no year&amp;month specified, current month will be used
[**api_counting_site_v1_values_get**](CountingSiteV1Api.md#api_counting_site_v1_values_get) | **GET** /api/counting-site/v1/values | Return counter values.  If no year&amp;month specified, current month will be used.


# **api_counting_site_v1_counters_counter_id_get**
> CountersModel api_counting_site_v1_counters_counter_id_get(counter_id)

Return single counter

### Example


```python
import openapi_client
from openapi_client.models.counters_model import CountersModel
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
    api_instance = openapi_client.CountingSiteV1Api(api_client)
    counter_id = 'counter_id_example' # str | 

    try:
        # Return single counter
        api_response = api_instance.api_counting_site_v1_counters_counter_id_get(counter_id)
        print("The response of CountingSiteV1Api->api_counting_site_v1_counters_counter_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CountingSiteV1Api->api_counting_site_v1_counters_counter_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **counter_id** | **str**|  | 

### Return type

[**CountersModel**](CountersModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/geo+json;charset=UTF-8, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response |  * Access-Control-Allow-Origin -  <br>  |
**500** | 500 response |  * Access-Control-Allow-Origin -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_counting_site_v1_counters_get**
> CountersModel api_counting_site_v1_counters_get(domain_name=domain_name)

Return all counters for domain

### Example


```python
import openapi_client
from openapi_client.models.counters_model import CountersModel
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
    api_instance = openapi_client.CountingSiteV1Api(api_client)
    domain_name = 'domain_name_example' # str | Domain name (optional)

    try:
        # Return all counters for domain
        api_response = api_instance.api_counting_site_v1_counters_get(domain_name=domain_name)
        print("The response of CountingSiteV1Api->api_counting_site_v1_counters_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CountingSiteV1Api->api_counting_site_v1_counters_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_name** | **str**| Domain name | [optional] 

### Return type

[**CountersModel**](CountersModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/geo+json;charset=UTF-8, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response |  * Access-Control-Allow-Origin -  <br>  |
**500** | 500 response |  * Access-Control-Allow-Origin -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_counting_site_v1_directions_get**
> api_counting_site_v1_directions_get()

Return all directions

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
    api_instance = openapi_client.CountingSiteV1Api(api_client)

    try:
        # Return all directions
        api_instance.api_counting_site_v1_directions_get()
    except Exception as e:
        print("Exception when calling CountingSiteV1Api->api_counting_site_v1_directions_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response |  * Access-Control-Allow-Origin -  <br>  * Last-Modified -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_counting_site_v1_domains_get**
> DomainsResponseModel api_counting_site_v1_domains_get()

Return all domains

### Example


```python
import openapi_client
from openapi_client.models.domains_response_model import DomainsResponseModel
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
    api_instance = openapi_client.CountingSiteV1Api(api_client)

    try:
        # Return all domains
        api_response = api_instance.api_counting_site_v1_domains_get()
        print("The response of CountingSiteV1Api->api_counting_site_v1_domains_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CountingSiteV1Api->api_counting_site_v1_domains_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**DomainsResponseModel**](DomainsResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response |  * Access-Control-Allow-Origin -  <br>  |
**500** | 500 response |  * Access-Control-Allow-Origin -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_counting_site_v1_user_types_get**
> object api_counting_site_v1_user_types_get()

Return all user types

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
    api_instance = openapi_client.CountingSiteV1Api(api_client)

    try:
        # Return all user types
        api_response = api_instance.api_counting_site_v1_user_types_get()
        print("The response of CountingSiteV1Api->api_counting_site_v1_user_types_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CountingSiteV1Api->api_counting_site_v1_user_types_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response |  * Access-Control-Allow-Origin -  <br>  |
**500** | 500 response |  * Access-Control-Allow-Origin -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_counting_site_v1_values_csv_get**
> object api_counting_site_v1_values_csv_get(year=year, domain_name=domain_name, counter_id=counter_id, month=month)

Return counter values in CSV. If no year&month specified, current month will be used

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
    api_instance = openapi_client.CountingSiteV1Api(api_client)
    year = 'year_example' # str | Year (optional)
    domain_name = 'domain_name_example' # str | Domain name (optional)
    counter_id = 'counter_id_example' # str | Counter id (optional)
    month = 'month_example' # str | Month (optional)

    try:
        # Return counter values in CSV. If no year&month specified, current month will be used
        api_response = api_instance.api_counting_site_v1_values_csv_get(year=year, domain_name=domain_name, counter_id=counter_id, month=month)
        print("The response of CountingSiteV1Api->api_counting_site_v1_values_csv_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CountingSiteV1Api->api_counting_site_v1_values_csv_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **str**| Year | [optional] 
 **domain_name** | **str**| Domain name | [optional] 
 **counter_id** | **str**| Counter id | [optional] 
 **month** | **str**| Month | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response |  * Access-Control-Allow-Origin -  <br>  |
**500** | 500 response |  * Access-Control-Allow-Origin -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_counting_site_v1_values_get**
> List[JsonDataResponseModelInner] api_counting_site_v1_values_get(year=year, domain_name=domain_name, counter_id=counter_id, month=month)

Return counter values.  If no year&month specified, current month will be used.

### Example


```python
import openapi_client
from openapi_client.models.json_data_response_model_inner import JsonDataResponseModelInner
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
    api_instance = openapi_client.CountingSiteV1Api(api_client)
    year = 'year_example' # str | Year (optional)
    domain_name = 'domain_name_example' # str | Domain name (optional)
    counter_id = 'counter_id_example' # str | Counter id (optional)
    month = 'month_example' # str | Month (optional)

    try:
        # Return counter values.  If no year&month specified, current month will be used.
        api_response = api_instance.api_counting_site_v1_values_get(year=year, domain_name=domain_name, counter_id=counter_id, month=month)
        print("The response of CountingSiteV1Api->api_counting_site_v1_values_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CountingSiteV1Api->api_counting_site_v1_values_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **str**| Year | [optional] 
 **domain_name** | **str**| Domain name | [optional] 
 **counter_id** | **str**| Counter id | [optional] 
 **month** | **str**| Month | [optional] 

### Return type

[**List[JsonDataResponseModelInner]**](JsonDataResponseModelInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response |  * Access-Control-Allow-Origin -  <br>  |
**500** | 500 response |  * Access-Control-Allow-Origin -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

