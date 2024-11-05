# openapi_client.BetaApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tms_data_datex2_json**](BetaApi.md#tms_data_datex2_json) | **GET** /api/beta/tms-data-datex2.json | Current data of TMS Stations in Datex2 format (Traffic Measurement System / LAM)
[**tms_data_datex2_xml**](BetaApi.md#tms_data_datex2_xml) | **GET** /api/beta/tms-data-datex2.xml | Current data of TMS Stations in Datex2 format (Traffic Measurement System / LAM)
[**tms_stations_datex2_json**](BetaApi.md#tms_stations_datex2_json) | **GET** /api/beta/tms-stations-datex2.json | The static information of TMS stations in Datex2 format (Traffic Measurement System / LAM)
[**tms_stations_datex2_xml**](BetaApi.md#tms_stations_datex2_xml) | **GET** /api/beta/tms-stations-datex2.xml | The static information of TMS stations in Datex2 format (Traffic Measurement System / LAM)
[**weather_data_history**](BetaApi.md#weather_data_history) | **GET** /api/beta/weather-history-data/{stationId} | List the history of sensor values from the weather road station
[**weather_data_history1**](BetaApi.md#weather_data_history1) | **GET** /api/beta/weather-history-data/{stationId}/{sensorId} | List the history of sensor value from the weather road station


# **tms_data_datex2_json**
> MeasuredDataPublication tms_data_datex2_json()

Current data of TMS Stations in Datex2 format (Traffic Measurement System / LAM)

### Example


```python
import openapi_client
from openapi_client.models.measured_data_publication import MeasuredDataPublication
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
    api_instance = openapi_client.BetaApi(api_client)

    try:
        # Current data of TMS Stations in Datex2 format (Traffic Measurement System / LAM)
        api_response = api_instance.tms_data_datex2_json()
        print("The response of BetaApi->tms_data_datex2_json:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BetaApi->tms_data_datex2_json: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**MeasuredDataPublication**](MeasuredDataPublication.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of TMS Stations Datex2 data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tms_data_datex2_xml**
> MeasuredDataPublication tms_data_datex2_xml()

Current data of TMS Stations in Datex2 format (Traffic Measurement System / LAM)

### Example


```python
import openapi_client
from openapi_client.models.measured_data_publication import MeasuredDataPublication
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
    api_instance = openapi_client.BetaApi(api_client)

    try:
        # Current data of TMS Stations in Datex2 format (Traffic Measurement System / LAM)
        api_response = api_instance.tms_data_datex2_xml()
        print("The response of BetaApi->tms_data_datex2_xml:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BetaApi->tms_data_datex2_xml: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**MeasuredDataPublication**](MeasuredDataPublication.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml;charset=UTF-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of TMS Stations Datex2 data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tms_stations_datex2_json**
> MeasurementSiteTablePublication tms_stations_datex2_json(state=state)

The static information of TMS stations in Datex2 format (Traffic Measurement System / LAM)

### Example


```python
import openapi_client
from openapi_client.models.measurement_site_table_publication import MeasurementSiteTablePublication
from openapi_client.models.road_station_state import RoadStationState
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
    api_instance = openapi_client.BetaApi(api_client)
    state = openapi_client.RoadStationState() # RoadStationState | Return TMS stations of given state. (optional)

    try:
        # The static information of TMS stations in Datex2 format (Traffic Measurement System / LAM)
        api_response = api_instance.tms_stations_datex2_json(state=state)
        print("The response of BetaApi->tms_stations_datex2_json:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BetaApi->tms_stations_datex2_json: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state** | [**RoadStationState**](.md)| Return TMS stations of given state. | [optional] 

### Return type

[**MeasurementSiteTablePublication**](MeasurementSiteTablePublication.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of TMS Stations Datex2 metadata |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tms_stations_datex2_xml**
> MeasurementSiteTablePublication tms_stations_datex2_xml(state=state)

The static information of TMS stations in Datex2 format (Traffic Measurement System / LAM)

### Example


```python
import openapi_client
from openapi_client.models.measurement_site_table_publication import MeasurementSiteTablePublication
from openapi_client.models.road_station_state import RoadStationState
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
    api_instance = openapi_client.BetaApi(api_client)
    state = openapi_client.RoadStationState() # RoadStationState | Return TMS stations of given state. (optional)

    try:
        # The static information of TMS stations in Datex2 format (Traffic Measurement System / LAM)
        api_response = api_instance.tms_stations_datex2_xml(state=state)
        print("The response of BetaApi->tms_stations_datex2_xml:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BetaApi->tms_stations_datex2_xml: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state** | [**RoadStationState**](.md)| Return TMS stations of given state. | [optional] 

### Return type

[**MeasurementSiteTablePublication**](MeasurementSiteTablePublication.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml;charset=UTF-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of TMS Stations Datex2 metadata |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **weather_data_history**
> List[WeatherSensorValueHistoryDto] weather_data_history(station_id, var_from=var_from, to=to)

List the history of sensor values from the weather road station

### Example


```python
import openapi_client
from openapi_client.models.weather_sensor_value_history_dto import WeatherSensorValueHistoryDto
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
    api_instance = openapi_client.BetaApi(api_client)
    station_id = 56 # int | Weather station id
    var_from = '2013-10-20T19:20:30+01:00' # datetime | Fetch history after given date time (optional)
    to = '2013-10-20T19:20:30+01:00' # datetime | Limit history to given date time (optional)

    try:
        # List the history of sensor values from the weather road station
        api_response = api_instance.weather_data_history(station_id, var_from=var_from, to=to)
        print("The response of BetaApi->weather_data_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BetaApi->weather_data_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **station_id** | **int**| Weather station id | 
 **var_from** | **datetime**| Fetch history after given date time | [optional] 
 **to** | **datetime**| Limit history to given date time | [optional] 

### Return type

[**List[WeatherSensorValueHistoryDto]**](WeatherSensorValueHistoryDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of weather station data |  -  |
**400** | Invalid parameter(s) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **weather_data_history1**
> List[WeatherSensorValueHistoryDto] weather_data_history1(station_id, sensor_id, var_from=var_from)

List the history of sensor value from the weather road station

### Example


```python
import openapi_client
from openapi_client.models.weather_sensor_value_history_dto import WeatherSensorValueHistoryDto
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
    api_instance = openapi_client.BetaApi(api_client)
    station_id = 56 # int | Weather Station id
    sensor_id = 56 # int | Sensor id
    var_from = '2013-10-20T19:20:30+01:00' # datetime | Fetch history after given time (optional)

    try:
        # List the history of sensor value from the weather road station
        api_response = api_instance.weather_data_history1(station_id, sensor_id, var_from=var_from)
        print("The response of BetaApi->weather_data_history1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BetaApi->weather_data_history1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **station_id** | **int**| Weather Station id | 
 **sensor_id** | **int**| Sensor id | 
 **var_from** | **datetime**| Fetch history after given time | [optional] 

### Return type

[**List[WeatherSensorValueHistoryDto]**](WeatherSensorValueHistoryDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of weather station data |  -  |
**400** | Invalid parameter |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

