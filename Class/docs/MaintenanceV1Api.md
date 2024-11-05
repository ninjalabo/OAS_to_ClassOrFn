# openapi_client.MaintenanceV1Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**find_latest_maintenance_trackings**](MaintenanceV1Api.md#find_latest_maintenance_trackings) | **GET** /api/maintenance/v1/tracking/routes/latest | Road maintenance tracking routes latest points
[**find_maintenance_trackings**](MaintenanceV1Api.md#find_maintenance_trackings) | **GET** /api/maintenance/v1/tracking/routes | Road maintenance tracking routes
[**get_maintenance_tracking**](MaintenanceV1Api.md#get_maintenance_tracking) | **GET** /api/maintenance/v1/tracking/routes/{id} | Road maintenance tracking route with tracking id
[**get_maintenance_tracking_domains**](MaintenanceV1Api.md#get_maintenance_tracking_domains) | **GET** /api/maintenance/v1/tracking/domains | Road maintenance tracking domains
[**get_maintenance_tracking_tasks**](MaintenanceV1Api.md#get_maintenance_tracking_tasks) | **GET** /api/maintenance/v1/tracking/tasks | Road maintenance tracking tasks


# **find_latest_maintenance_trackings**
> MaintenanceTrackingLatestFeatureCollectionV1 find_latest_maintenance_trackings(end_from=end_from, x_min=x_min, y_min=y_min, x_max=x_max, y_max=y_max, task_id=task_id, domain=domain)

Road maintenance tracking routes latest points

### Example


```python
import openapi_client
from openapi_client.models.maintenance_tracking_latest_feature_collection_v1 import MaintenanceTrackingLatestFeatureCollectionV1
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
    api_instance = openapi_client.MaintenanceV1Api(api_client)
    end_from = '2013-10-20T19:20:30+01:00' # datetime | Return routes which have completed onwards from the given time (inclusive). Default is -1h from now and maximum -24h. (optional)
    x_min = 19 # float | Minimum x coordinate (longitude) Coordinates are in WGS84 format in decimal degrees. Values between 19.0 and 32.0.<br>xMin coordinate will be rounded to nearest integer that is less than or equal to given value (optional) (default to 19)
    y_min = 59 # float | Minimum y coordinate (latitude). Coordinates are in WGS84 format in decimal degrees. Values between 59.0 and 72.0.<br>yMin coordinate will be rounded to nearest half that is less than or equal to given value (optional) (default to 59)
    x_max = 32 # float | Maximum x coordinate (longitude). Coordinates are in WGS84 format in decimal degrees. Values between 19.0 and 32.0.<br>xMax coordinate will be rounded to nearest integer greater than or equal to given value (optional) (default to 32)
    y_max = 72 # float | Maximum y coordinate (latitude). Coordinates are in WGS84 format in decimal degrees. Values between 59.0 and 72.0.<br>yMax coordinate will be rounded to nearest half that is greater than or equal to given value (optional) (default to 72)
    task_id = ['task_id_example'] # List[str] | Task ids to include. Any route containing one of the selected tasks will be returned. (optional)
    domain = ["state-roads"] # List[str] | Data domains. If domain is not given default value of \"state-roads\" will be used. (optional) (default to ["state-roads"])

    try:
        # Road maintenance tracking routes latest points
        api_response = api_instance.find_latest_maintenance_trackings(end_from=end_from, x_min=x_min, y_min=y_min, x_max=x_max, y_max=y_max, task_id=task_id, domain=domain)
        print("The response of MaintenanceV1Api->find_latest_maintenance_trackings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MaintenanceV1Api->find_latest_maintenance_trackings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_from** | **datetime**| Return routes which have completed onwards from the given time (inclusive). Default is -1h from now and maximum -24h. | [optional] 
 **x_min** | **float**| Minimum x coordinate (longitude) Coordinates are in WGS84 format in decimal degrees. Values between 19.0 and 32.0.&lt;br&gt;xMin coordinate will be rounded to nearest integer that is less than or equal to given value | [optional] [default to 19]
 **y_min** | **float**| Minimum y coordinate (latitude). Coordinates are in WGS84 format in decimal degrees. Values between 59.0 and 72.0.&lt;br&gt;yMin coordinate will be rounded to nearest half that is less than or equal to given value | [optional] [default to 59]
 **x_max** | **float**| Maximum x coordinate (longitude). Coordinates are in WGS84 format in decimal degrees. Values between 19.0 and 32.0.&lt;br&gt;xMax coordinate will be rounded to nearest integer greater than or equal to given value | [optional] [default to 32]
 **y_max** | **float**| Maximum y coordinate (latitude). Coordinates are in WGS84 format in decimal degrees. Values between 59.0 and 72.0.&lt;br&gt;yMax coordinate will be rounded to nearest half that is greater than or equal to given value | [optional] [default to 72]
 **task_id** | [**List[str]**](str.md)| Task ids to include. Any route containing one of the selected tasks will be returned. | [optional] 
 **domain** | [**List[str]**](str.md)| Data domains. If domain is not given default value of \&quot;state-roads\&quot; will be used. | [optional] [default to [&quot;state-roads&quot;]]

### Return type

[**MaintenanceTrackingLatestFeatureCollectionV1**](MaintenanceTrackingLatestFeatureCollectionV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of maintenance tracking latest routes |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_maintenance_trackings**
> MaintenanceTrackingFeatureCollectionV1 find_maintenance_trackings(end_from=end_from, end_before=end_before, created_after=created_after, created_before=created_before, x_min=x_min, y_min=y_min, x_max=x_max, y_max=y_max, task_id=task_id, domain=domain)

Road maintenance tracking routes

### Example


```python
import openapi_client
from openapi_client.models.maintenance_tracking_feature_collection_v1 import MaintenanceTrackingFeatureCollectionV1
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
    api_instance = openapi_client.MaintenanceV1Api(api_client)
    end_from = '2013-10-20T19:20:30+01:00' # datetime | Return routes which have completed onwards from the given time (inclusive). Default is 24h in past and maximum interval between from and to is 24h. (optional)
    end_before = '2013-10-20T19:20:30+01:00' # datetime | Return routes which have completed before the given end time (exclusive). Default is now and maximum interval between from and to is 24h. (optional)
    created_after = '2013-10-20T19:20:30+01:00' # datetime | Return routes which have been created after the given time (exclusive). Maximum interval between createdFrom and createdTo is 24h. (optional)
    created_before = '2013-10-20T19:20:30+01:00' # datetime | Return routes which have been created before the given time (exclusive). Maximum interval between createdFrom and createdTo is 24h. (optional)
    x_min = 19 # float | Minimum x coordinate (longitude) Coordinates are in WGS84 format in decimal degrees. Values between 19.0 and 32.0.<br>xMin coordinate will be rounded to nearest integer that is less than or equal to given value (optional) (default to 19)
    y_min = 59 # float | Minimum y coordinate (latitude). Coordinates are in WGS84 format in decimal degrees. Values between 59.0 and 72.0.<br>yMin coordinate will be rounded to nearest half that is less than or equal to given value (optional) (default to 59)
    x_max = 32 # float | Maximum x coordinate (longitude). Coordinates are in WGS84 format in decimal degrees. Values between 19.0 and 32.0.<br>xMax coordinate will be rounded to nearest integer greater than or equal to given value (optional) (default to 32)
    y_max = 72 # float | Maximum y coordinate (latitude). Coordinates are in WGS84 format in decimal degrees. Values between 59.0 and 72.0.<br>yMax coordinate will be rounded to nearest half that is greater than or equal to given value (optional) (default to 72)
    task_id = ['task_id_example'] # List[str] | Task ids to include. Any tracking containing one of the selected tasks will be returned. (optional)
    domain = ["state-roads"] # List[str] | Data domains. If domain is not given default value of \"state-roads\" will be used. (optional) (default to ["state-roads"])

    try:
        # Road maintenance tracking routes
        api_response = api_instance.find_maintenance_trackings(end_from=end_from, end_before=end_before, created_after=created_after, created_before=created_before, x_min=x_min, y_min=y_min, x_max=x_max, y_max=y_max, task_id=task_id, domain=domain)
        print("The response of MaintenanceV1Api->find_maintenance_trackings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MaintenanceV1Api->find_maintenance_trackings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_from** | **datetime**| Return routes which have completed onwards from the given time (inclusive). Default is 24h in past and maximum interval between from and to is 24h. | [optional] 
 **end_before** | **datetime**| Return routes which have completed before the given end time (exclusive). Default is now and maximum interval between from and to is 24h. | [optional] 
 **created_after** | **datetime**| Return routes which have been created after the given time (exclusive). Maximum interval between createdFrom and createdTo is 24h. | [optional] 
 **created_before** | **datetime**| Return routes which have been created before the given time (exclusive). Maximum interval between createdFrom and createdTo is 24h. | [optional] 
 **x_min** | **float**| Minimum x coordinate (longitude) Coordinates are in WGS84 format in decimal degrees. Values between 19.0 and 32.0.&lt;br&gt;xMin coordinate will be rounded to nearest integer that is less than or equal to given value | [optional] [default to 19]
 **y_min** | **float**| Minimum y coordinate (latitude). Coordinates are in WGS84 format in decimal degrees. Values between 59.0 and 72.0.&lt;br&gt;yMin coordinate will be rounded to nearest half that is less than or equal to given value | [optional] [default to 59]
 **x_max** | **float**| Maximum x coordinate (longitude). Coordinates are in WGS84 format in decimal degrees. Values between 19.0 and 32.0.&lt;br&gt;xMax coordinate will be rounded to nearest integer greater than or equal to given value | [optional] [default to 32]
 **y_max** | **float**| Maximum y coordinate (latitude). Coordinates are in WGS84 format in decimal degrees. Values between 59.0 and 72.0.&lt;br&gt;yMax coordinate will be rounded to nearest half that is greater than or equal to given value | [optional] [default to 72]
 **task_id** | [**List[str]**](str.md)| Task ids to include. Any tracking containing one of the selected tasks will be returned. | [optional] 
 **domain** | [**List[str]**](str.md)| Data domains. If domain is not given default value of \&quot;state-roads\&quot; will be used. | [optional] [default to [&quot;state-roads&quot;]]

### Return type

[**MaintenanceTrackingFeatureCollectionV1**](MaintenanceTrackingFeatureCollectionV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of maintenance tracking routes |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_maintenance_tracking**
> MaintenanceTrackingFeatureV1 get_maintenance_tracking(id)

Road maintenance tracking route with tracking id

### Example


```python
import openapi_client
from openapi_client.models.maintenance_tracking_feature_v1 import MaintenanceTrackingFeatureV1
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
    api_instance = openapi_client.MaintenanceV1Api(api_client)
    id = 56 # int | Tracking id

    try:
        # Road maintenance tracking route with tracking id
        api_response = api_instance.get_maintenance_tracking(id)
        print("The response of MaintenanceV1Api->get_maintenance_tracking:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MaintenanceV1Api->get_maintenance_tracking: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Tracking id | 

### Return type

[**MaintenanceTrackingFeatureV1**](MaintenanceTrackingFeatureV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of maintenance tracking routes |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_maintenance_tracking_domains**
> List[MaintenanceTrackingDomainDtoV1] get_maintenance_tracking_domains()

Road maintenance tracking domains

### Example


```python
import openapi_client
from openapi_client.models.maintenance_tracking_domain_dto_v1 import MaintenanceTrackingDomainDtoV1
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
    api_instance = openapi_client.MaintenanceV1Api(api_client)

    try:
        # Road maintenance tracking domains
        api_response = api_instance.get_maintenance_tracking_domains()
        print("The response of MaintenanceV1Api->get_maintenance_tracking_domains:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MaintenanceV1Api->get_maintenance_tracking_domains: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[MaintenanceTrackingDomainDtoV1]**](MaintenanceTrackingDomainDtoV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of maintenance tracking domains |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_maintenance_tracking_tasks**
> List[MaintenanceTrackingTaskDtoV1] get_maintenance_tracking_tasks()

Road maintenance tracking tasks

### Example


```python
import openapi_client
from openapi_client.models.maintenance_tracking_task_dto_v1 import MaintenanceTrackingTaskDtoV1
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
    api_instance = openapi_client.MaintenanceV1Api(api_client)

    try:
        # Road maintenance tracking tasks
        api_response = api_instance.get_maintenance_tracking_tasks()
        print("The response of MaintenanceV1Api->get_maintenance_tracking_tasks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MaintenanceV1Api->get_maintenance_tracking_tasks: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[MaintenanceTrackingTaskDtoV1]**](MaintenanceTrackingTaskDtoV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of maintenance tracking tasks |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

