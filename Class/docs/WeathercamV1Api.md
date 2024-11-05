# openapi_client.WeathercamV1Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_weathercam_presets_history_by_id**](WeathercamV1Api.md#get_weathercam_presets_history_by_id) | **GET** /api/weathercam/v1/stations/{id}/history | Weathercam presets history for given camera
[**get_weathercams_presets_history**](WeathercamV1Api.md#get_weathercams_presets_history) | **GET** /api/weathercam/v1/stations/history | Weathercams presets history for all cameras
[**weathercam_datas_by_station_id**](WeathercamV1Api.md#weathercam_datas_by_station_id) | **GET** /api/weathercam/v1/stations/{id}/data | Current data of weathercam
[**weathercam_preset_publicity_changes_after**](WeathercamV1Api.md#weathercam_preset_publicity_changes_after) | **GET** /api/weathercam/v1/publicities/changes | Weathercam presets publicity changes after given time. Result is in ascending order by presetId and lastModified -fields. 
[**weathercam_station**](WeathercamV1Api.md#weathercam_station) | **GET** /api/weathercam/v1/stations/{id} | The static information of weather camera station
[**weathercam_stations**](WeathercamV1Api.md#weathercam_stations) | **GET** /api/weathercam/v1/stations | The static information of weather camera stations
[**weathercams_datas**](WeathercamV1Api.md#weathercams_datas) | **GET** /api/weathercam/v1/stations/data | Current data of weathercams


# **get_weathercam_presets_history_by_id**
> PresetHistory get_weathercam_presets_history_by_id(id)

Weathercam presets history for given camera

### Example


```python
import openapi_client
from openapi_client.models.preset_history import PresetHistory
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
    api_instance = openapi_client.WeathercamV1Api(api_client)
    id = 'id_example' # str | Camera id

    try:
        # Weathercam presets history for given camera
        api_response = api_instance.get_weathercam_presets_history_by_id(id)
        print("The response of WeathercamV1Api->get_weathercam_presets_history_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WeathercamV1Api->get_weathercam_presets_history_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Camera id | 

### Return type

[**PresetHistory**](PresetHistory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of weathercam image history |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_weathercams_presets_history**
> CameraHistory get_weathercams_presets_history()

Weathercams presets history for all cameras

### Example


```python
import openapi_client
from openapi_client.models.camera_history import CameraHistory
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
    api_instance = openapi_client.WeathercamV1Api(api_client)

    try:
        # Weathercams presets history for all cameras
        api_response = api_instance.get_weathercams_presets_history()
        print("The response of WeathercamV1Api->get_weathercams_presets_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WeathercamV1Api->get_weathercams_presets_history: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CameraHistory**](CameraHistory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of weathercams image history |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **weathercam_datas_by_station_id**
> WeathercamStationDataV1 weathercam_datas_by_station_id(id)

Current data of weathercam

### Example


```python
import openapi_client
from openapi_client.models.weathercam_station_data_v1 import WeathercamStationDataV1
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
    api_instance = openapi_client.WeathercamV1Api(api_client)
    id = 'id_example' # str | Camera station id

    try:
        # Current data of weathercam
        api_response = api_instance.weathercam_datas_by_station_id(id)
        print("The response of WeathercamV1Api->weathercam_datas_by_station_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WeathercamV1Api->weathercam_datas_by_station_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Camera station id | 

### Return type

[**WeathercamStationDataV1**](WeathercamStationDataV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of camera station data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **weathercam_preset_publicity_changes_after**
> WeathercamStationsPresetsPublicityHistoryV1 weathercam_preset_publicity_changes_after(after=after)

Weathercam presets publicity changes after given time. Result is in ascending order by presetId and lastModified -fields. 

### Example


```python
import openapi_client
from openapi_client.models.weathercam_stations_presets_publicity_history_v1 import WeathercamStationsPresetsPublicityHistoryV1
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
    api_instance = openapi_client.WeathercamV1Api(api_client)
    after = '2013-10-20T19:20:30+01:00' # datetime | Return changes int the history after given time. Given time must be within 24 hours. Default is 24h in past (optional)

    try:
        # Weathercam presets publicity changes after given time. Result is in ascending order by presetId and lastModified -fields. 
        api_response = api_instance.weathercam_preset_publicity_changes_after(after=after)
        print("The response of WeathercamV1Api->weathercam_preset_publicity_changes_after:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WeathercamV1Api->weathercam_preset_publicity_changes_after: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **after** | **datetime**| Return changes int the history after given time. Given time must be within 24 hours. Default is 24h in past | [optional] 

### Return type

[**WeathercamStationsPresetsPublicityHistoryV1**](WeathercamStationsPresetsPublicityHistoryV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of camera history changes |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **weathercam_station**
> WeathercamStationFeatureV1Detailed weathercam_station(id)

The static information of weather camera station

### Example


```python
import openapi_client
from openapi_client.models.weathercam_station_feature_v1_detailed import WeathercamStationFeatureV1Detailed
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
    api_instance = openapi_client.WeathercamV1Api(api_client)
    id = 'id_example' # str | Weathercam station id

    try:
        # The static information of weather camera station
        api_response = api_instance.weathercam_station(id)
        print("The response of WeathercamV1Api->weathercam_station:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WeathercamV1Api->weathercam_station: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Weathercam station id | 

### Return type

[**WeathercamStationFeatureV1Detailed**](WeathercamStationFeatureV1Detailed.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.geo+json;charset=UTF-8, application/json;charset=UTF-8, application/geo+json;charset=UTF-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **weathercam_stations**
> WeathercamStationFeatureCollectionSimpleV1 weathercam_stations(last_updated=last_updated)

The static information of weather camera stations

### Example


```python
import openapi_client
from openapi_client.models.weathercam_station_feature_collection_simple_v1 import WeathercamStationFeatureCollectionSimpleV1
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
    api_instance = openapi_client.WeathercamV1Api(api_client)
    last_updated = False # bool | If parameter is given result will only contain update status. (optional) (default to False)

    try:
        # The static information of weather camera stations
        api_response = api_instance.weathercam_stations(last_updated=last_updated)
        print("The response of WeathercamV1Api->weathercam_stations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WeathercamV1Api->weathercam_stations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **last_updated** | **bool**| If parameter is given result will only contain update status. | [optional] [default to False]

### Return type

[**WeathercamStationFeatureCollectionSimpleV1**](WeathercamStationFeatureCollectionSimpleV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.geo+json;charset=UTF-8, application/json;charset=UTF-8, application/geo+json;charset=UTF-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of Camera Preset Feature Collections |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **weathercams_datas**
> WeathercamStationsDataV1 weathercams_datas(last_updated=last_updated)

Current data of weathercams

### Example


```python
import openapi_client
from openapi_client.models.weathercam_stations_data_v1 import WeathercamStationsDataV1
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
    api_instance = openapi_client.WeathercamV1Api(api_client)
    last_updated = False # bool | If parameter is given result will only contain update status. (optional) (default to False)

    try:
        # Current data of weathercams
        api_response = api_instance.weathercams_datas(last_updated=last_updated)
        print("The response of WeathercamV1Api->weathercams_datas:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WeathercamV1Api->weathercams_datas: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **last_updated** | **bool**| If parameter is given result will only contain update status. | [optional] [default to False]

### Return type

[**WeathercamStationsDataV1**](WeathercamStationsDataV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of camera station data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

