# openapi_client.TMSV1Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tms_data**](TMSV1Api.md#tms_data) | **GET** /api/tms/v1/stations/data | Current data of TMS stations (Traffic Measurement System / LAM)
[**tms_data_by_id**](TMSV1Api.md#tms_data_by_id) | **GET** /api/tms/v1/stations/{id}/data | Current data of one TMS station (Traffic Measurement System / LAM)
[**tms_sensor_constants**](TMSV1Api.md#tms_sensor_constants) | **GET** /api/tms/v1/stations/sensor-constants | Current sensor constants and values of TMS stations (Traffic Measurement System / LAM)
[**tms_sensor_constants_by_station_id**](TMSV1Api.md#tms_sensor_constants_by_station_id) | **GET** /api/tms/v1/stations/{id}/sensor-constants | Current sensor constants and values of one TMS station (Traffic Measurement System / LAM)
[**tms_sensors**](TMSV1Api.md#tms_sensors) | **GET** /api/tms/v1/sensors | The static information of available sensors of TMS stations (Traffic Measurement System / LAM)
[**tms_station_by_road_station_id**](TMSV1Api.md#tms_station_by_road_station_id) | **GET** /api/tms/v1/stations/{id} | The static information of one TMS station (Traffic Measurement System / LAM)
[**tms_stations**](TMSV1Api.md#tms_stations) | **GET** /api/tms/v1/stations | The static information of TMS stations (Traffic Measurement System / LAM)


# **tms_data**
> TmsStationsDataDtoV1 tms_data(last_updated=last_updated)

Current data of TMS stations (Traffic Measurement System / LAM)

### Example


```python
import openapi_client
from openapi_client.models.tms_stations_data_dto_v1 import TmsStationsDataDtoV1
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
    api_instance = openapi_client.TMSV1Api(api_client)
    last_updated = False # bool | If parameter is given result will only contain update status. (optional) (default to False)

    try:
        # Current data of TMS stations (Traffic Measurement System / LAM)
        api_response = api_instance.tms_data(last_updated=last_updated)
        print("The response of TMSV1Api->tms_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TMSV1Api->tms_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **last_updated** | **bool**| If parameter is given result will only contain update status. | [optional] [default to False]

### Return type

[**TmsStationsDataDtoV1**](TmsStationsDataDtoV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of TMS station data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tms_data_by_id**
> TmsStationDataDtoV1 tms_data_by_id(id)

Current data of one TMS station (Traffic Measurement System / LAM)

### Example


```python
import openapi_client
from openapi_client.models.tms_station_data_dto_v1 import TmsStationDataDtoV1
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
    api_instance = openapi_client.TMSV1Api(api_client)
    id = 56 # int | TMS Station id

    try:
        # Current data of one TMS station (Traffic Measurement System / LAM)
        api_response = api_instance.tms_data_by_id(id)
        print("The response of TMSV1Api->tms_data_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TMSV1Api->tms_data_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| TMS Station id | 

### Return type

[**TmsStationDataDtoV1**](TmsStationDataDtoV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of TMS station data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tms_sensor_constants**
> TmsStationsSensorConstantsDataDtoV1 tms_sensor_constants(last_updated=last_updated)

Current sensor constants and values of TMS stations (Traffic Measurement System / LAM)

### Example


```python
import openapi_client
from openapi_client.models.tms_stations_sensor_constants_data_dto_v1 import TmsStationsSensorConstantsDataDtoV1
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
    api_instance = openapi_client.TMSV1Api(api_client)
    last_updated = False # bool | If parameter is given result will only contain update status (optional) (default to False)

    try:
        # Current sensor constants and values of TMS stations (Traffic Measurement System / LAM)
        api_response = api_instance.tms_sensor_constants(last_updated=last_updated)
        print("The response of TMSV1Api->tms_sensor_constants:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TMSV1Api->tms_sensor_constants: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **last_updated** | **bool**| If parameter is given result will only contain update status | [optional] [default to False]

### Return type

[**TmsStationsSensorConstantsDataDtoV1**](TmsStationsSensorConstantsDataDtoV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of sensor constants and values |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tms_sensor_constants_by_station_id**
> TmsStationSensorConstantDtoV1 tms_sensor_constants_by_station_id(id)

Current sensor constants and values of one TMS station (Traffic Measurement System / LAM)

### Example


```python
import openapi_client
from openapi_client.models.tms_station_sensor_constant_dto_v1 import TmsStationSensorConstantDtoV1
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
    api_instance = openapi_client.TMSV1Api(api_client)
    id = 56 # int | TMS Station id

    try:
        # Current sensor constants and values of one TMS station (Traffic Measurement System / LAM)
        api_response = api_instance.tms_sensor_constants_by_station_id(id)
        print("The response of TMSV1Api->tms_sensor_constants_by_station_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TMSV1Api->tms_sensor_constants_by_station_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| TMS Station id | 

### Return type

[**TmsStationSensorConstantDtoV1**](TmsStationSensorConstantDtoV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of sensor constants and values |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tms_sensors**
> TmsStationSensorsDtoV1 tms_sensors(last_updated=last_updated)

The static information of available sensors of TMS stations (Traffic Measurement System / LAM)

### Example


```python
import openapi_client
from openapi_client.models.tms_station_sensors_dto_v1 import TmsStationSensorsDtoV1
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
    api_instance = openapi_client.TMSV1Api(api_client)
    last_updated = False # bool | If parameter is given result will only contain update status. (optional) (default to False)

    try:
        # The static information of available sensors of TMS stations (Traffic Measurement System / LAM)
        api_response = api_instance.tms_sensors(last_updated=last_updated)
        print("The response of TMSV1Api->tms_sensors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TMSV1Api->tms_sensors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **last_updated** | **bool**| If parameter is given result will only contain update status. | [optional] [default to False]

### Return type

[**TmsStationSensorsDtoV1**](TmsStationSensorsDtoV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of TMS station sensors |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tms_station_by_road_station_id**
> TmsStationFeatureDetailedV1 tms_station_by_road_station_id(id)

The static information of one TMS station (Traffic Measurement System / LAM)

### Example


```python
import openapi_client
from openapi_client.models.tms_station_feature_detailed_v1 import TmsStationFeatureDetailedV1
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
    api_instance = openapi_client.TMSV1Api(api_client)
    id = 56 # int | 

    try:
        # The static information of one TMS station (Traffic Measurement System / LAM)
        api_response = api_instance.tms_station_by_road_station_id(id)
        print("The response of TMSV1Api->tms_station_by_road_station_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TMSV1Api->tms_station_by_road_station_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**TmsStationFeatureDetailedV1**](TmsStationFeatureDetailedV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.geo+json;charset=UTF-8, application/json;charset=UTF-8, application/geo+json;charset=UTF-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of TMS Station Feature |  -  |
**404** | Road Station not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tms_stations**
> TmsStationFeatureCollectionSimpleV1 tms_stations(last_updated=last_updated, state=state)

The static information of TMS stations (Traffic Measurement System / LAM)

### Example


```python
import openapi_client
from openapi_client.models.road_station_state import RoadStationState
from openapi_client.models.tms_station_feature_collection_simple_v1 import TmsStationFeatureCollectionSimpleV1
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
    api_instance = openapi_client.TMSV1Api(api_client)
    last_updated = False # bool | If parameter is given result will only contain update status. (optional) (default to False)
    state = openapi_client.RoadStationState() # RoadStationState | Return TMS stations of given state. (optional)

    try:
        # The static information of TMS stations (Traffic Measurement System / LAM)
        api_response = api_instance.tms_stations(last_updated=last_updated, state=state)
        print("The response of TMSV1Api->tms_stations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TMSV1Api->tms_stations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **last_updated** | **bool**| If parameter is given result will only contain update status. | [optional] [default to False]
 **state** | [**RoadStationState**](.md)| Return TMS stations of given state. | [optional] 

### Return type

[**TmsStationFeatureCollectionSimpleV1**](TmsStationFeatureCollectionSimpleV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.geo+json;charset=UTF-8, application/json;charset=UTF-8, application/geo+json;charset=UTF-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of TMS Station Feature Collections |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

