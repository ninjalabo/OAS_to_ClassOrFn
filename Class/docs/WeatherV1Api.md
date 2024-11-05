# openapi_client.WeatherV1Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**forecast_section_by_id**](WeatherV1Api.md#forecast_section_by_id) | **GET** /api/weather/v1/forecast-sections/{id} | The static information of weather forecast sections
[**forecast_section_forecasts_by_id**](WeatherV1Api.md#forecast_section_forecasts_by_id) | **GET** /api/weather/v1/forecast-sections/{id}/forecasts | Current data of weather forecast sections
[**forecast_section_simple_by_id**](WeatherV1Api.md#forecast_section_simple_by_id) | **GET** /api/weather/v1/forecast-sections-simple/{id} | The static information of simple weather forecast sections
[**forecast_section_simple_forecasts_by_id**](WeatherV1Api.md#forecast_section_simple_forecasts_by_id) | **GET** /api/weather/v1/forecast-sections-simple/{id}/forecasts | Current data of simple weather forecast sections
[**forecast_sections**](WeatherV1Api.md#forecast_sections) | **GET** /api/weather/v1/forecast-sections | The static information of weather forecast sections
[**forecast_sections_forecasts**](WeatherV1Api.md#forecast_sections_forecasts) | **GET** /api/weather/v1/forecast-sections/forecasts | Current data of detailed weather forecast sections
[**forecast_sections_simple**](WeatherV1Api.md#forecast_sections_simple) | **GET** /api/weather/v1/forecast-sections-simple | The static information of simple weather forecast sections
[**forecast_sections_simple_forecasts**](WeatherV1Api.md#forecast_sections_simple_forecasts) | **GET** /api/weather/v1/forecast-sections-simple/forecasts | Current data of simple weather forecast sections
[**weather_data**](WeatherV1Api.md#weather_data) | **GET** /api/weather/v1/stations/data | Current data of weather stations
[**weather_data_by_id**](WeatherV1Api.md#weather_data_by_id) | **GET** /api/weather/v1/stations/{id}/data | Current data of one weather station
[**weather_sensors**](WeatherV1Api.md#weather_sensors) | **GET** /api/weather/v1/sensors | The static information of available sensors of weather stations
[**weather_station_by_road_station_id**](WeatherV1Api.md#weather_station_by_road_station_id) | **GET** /api/weather/v1/stations/{id} | The static information of one weather station
[**weather_stations**](WeatherV1Api.md#weather_stations) | **GET** /api/weather/v1/stations | The static information of weather stations


# **forecast_section_by_id**
> ForecastSectionFeatureV1 forecast_section_by_id(id, simplified=simplified)

The static information of weather forecast sections

### Example


```python
import openapi_client
from openapi_client.models.forecast_section_feature_v1 import ForecastSectionFeatureV1
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
    api_instance = openapi_client.WeatherV1Api(api_client)
    id = 'id_example' # str | Section id
    simplified = False # bool | If parameter is given with true value, result geometry will be smaller in size. (optional) (default to False)

    try:
        # The static information of weather forecast sections
        api_response = api_instance.forecast_section_by_id(id, simplified=simplified)
        print("The response of WeatherV1Api->forecast_section_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WeatherV1Api->forecast_section_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Section id | 
 **simplified** | **bool**| If parameter is given with true value, result geometry will be smaller in size. | [optional] [default to False]

### Return type

[**ForecastSectionFeatureV1**](ForecastSectionFeatureV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.geo+json;charset=UTF-8, application/json;charset=UTF-8, application/geo+json;charset=UTF-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of Forecast Sections |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forecast_section_forecasts_by_id**
> ForecastSectionWeatherDtoV1 forecast_section_forecasts_by_id(id)

Current data of weather forecast sections

### Example


```python
import openapi_client
from openapi_client.models.forecast_section_weather_dto_v1 import ForecastSectionWeatherDtoV1
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
    api_instance = openapi_client.WeatherV1Api(api_client)
    id = 'id_example' # str | Section id

    try:
        # Current data of weather forecast sections
        api_response = api_instance.forecast_section_forecasts_by_id(id)
        print("The response of WeatherV1Api->forecast_section_forecasts_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WeatherV1Api->forecast_section_forecasts_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Section id | 

### Return type

[**ForecastSectionWeatherDtoV1**](ForecastSectionWeatherDtoV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.geo+json;charset=UTF-8, application/json;charset=UTF-8, application/geo+json;charset=UTF-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of Forecast Sections |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forecast_section_simple_by_id**
> ForecastSectionFeatureSimpleV1 forecast_section_simple_by_id(id)

The static information of simple weather forecast sections

### Example


```python
import openapi_client
from openapi_client.models.forecast_section_feature_simple_v1 import ForecastSectionFeatureSimpleV1
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
    api_instance = openapi_client.WeatherV1Api(api_client)
    id = 'id_example' # str | Section id

    try:
        # The static information of simple weather forecast sections
        api_response = api_instance.forecast_section_simple_by_id(id)
        print("The response of WeatherV1Api->forecast_section_simple_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WeatherV1Api->forecast_section_simple_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Section id | 

### Return type

[**ForecastSectionFeatureSimpleV1**](ForecastSectionFeatureSimpleV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.geo+json;charset=UTF-8, application/json;charset=UTF-8, application/geo+json;charset=UTF-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of simple forecast sections |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forecast_section_simple_forecasts_by_id**
> ForecastSectionWeatherDtoV1 forecast_section_simple_forecasts_by_id(id)

Current data of simple weather forecast sections

### Example


```python
import openapi_client
from openapi_client.models.forecast_section_weather_dto_v1 import ForecastSectionWeatherDtoV1
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
    api_instance = openapi_client.WeatherV1Api(api_client)
    id = 'id_example' # str | Section id

    try:
        # Current data of simple weather forecast sections
        api_response = api_instance.forecast_section_simple_forecasts_by_id(id)
        print("The response of WeatherV1Api->forecast_section_simple_forecasts_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WeatherV1Api->forecast_section_simple_forecasts_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Section id | 

### Return type

[**ForecastSectionWeatherDtoV1**](ForecastSectionWeatherDtoV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.geo+json;charset=UTF-8, application/json;charset=UTF-8, application/geo+json;charset=UTF-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of Forecast Sections |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forecast_sections**
> ForecastSectionFeatureCollectionV1 forecast_sections(last_updated=last_updated, simplified=simplified, road_number=road_number, x_min=x_min, y_min=y_min, x_max=x_max, y_max=y_max)

The static information of weather forecast sections

### Example


```python
import openapi_client
from openapi_client.models.forecast_section_feature_collection_v1 import ForecastSectionFeatureCollectionV1
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
    api_instance = openapi_client.WeatherV1Api(api_client)
    last_updated = False # bool | If parameter is given result will only contain update status. (optional) (default to False)
    simplified = False # bool | If parameter is given with true value, result geometry will be smaller in size. (optional) (default to False)
    road_number = 56 # int | Road number (optional)
    x_min = 19 # float | Minimum x coordinate (longitude) Coordinates are in WGS84 format in decimal degrees. Values between 19.0 and 32.0. (optional) (default to 19)
    y_min = 59 # float | Minimum y coordinate (latitude). Coordinates are in WGS84 format in decimal degrees. Values between 59.0 and 72.0. (optional) (default to 59)
    x_max = 32 # float | Maximum x coordinate (longitude). Coordinates are in WGS84 format in decimal degrees. Values between 19.0 and 32.0. (optional) (default to 32)
    y_max = 72 # float | Maximum y coordinate (latitude). Coordinates are in WGS84 format in decimal degrees. Values between 59.0 and 72.0. (optional) (default to 72)

    try:
        # The static information of weather forecast sections
        api_response = api_instance.forecast_sections(last_updated=last_updated, simplified=simplified, road_number=road_number, x_min=x_min, y_min=y_min, x_max=x_max, y_max=y_max)
        print("The response of WeatherV1Api->forecast_sections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WeatherV1Api->forecast_sections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **last_updated** | **bool**| If parameter is given result will only contain update status. | [optional] [default to False]
 **simplified** | **bool**| If parameter is given with true value, result geometry will be smaller in size. | [optional] [default to False]
 **road_number** | **int**| Road number | [optional] 
 **x_min** | **float**| Minimum x coordinate (longitude) Coordinates are in WGS84 format in decimal degrees. Values between 19.0 and 32.0. | [optional] [default to 19]
 **y_min** | **float**| Minimum y coordinate (latitude). Coordinates are in WGS84 format in decimal degrees. Values between 59.0 and 72.0. | [optional] [default to 59]
 **x_max** | **float**| Maximum x coordinate (longitude). Coordinates are in WGS84 format in decimal degrees. Values between 19.0 and 32.0. | [optional] [default to 32]
 **y_max** | **float**| Maximum y coordinate (latitude). Coordinates are in WGS84 format in decimal degrees. Values between 59.0 and 72.0. | [optional] [default to 72]

### Return type

[**ForecastSectionFeatureCollectionV1**](ForecastSectionFeatureCollectionV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.geo+json;charset=UTF-8, application/json;charset=UTF-8, application/geo+json;charset=UTF-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of Forecast Sections |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forecast_sections_forecasts**
> ForecastSectionsWeatherDtoV1 forecast_sections_forecasts(last_updated=last_updated, road_number=road_number, x_min=x_min, y_min=y_min, x_max=x_max, y_max=y_max)

Current data of detailed weather forecast sections

### Example


```python
import openapi_client
from openapi_client.models.forecast_sections_weather_dto_v1 import ForecastSectionsWeatherDtoV1
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
    api_instance = openapi_client.WeatherV1Api(api_client)
    last_updated = False # bool | If parameter is given result will only contain update status. (optional) (default to False)
    road_number = 56 # int | Road number (optional)
    x_min = 19 # float | Minimum x coordinate (longitude) Coordinates are in WGS84 format in decimal degrees. Values between 19.0 and 32.0. (optional) (default to 19)
    y_min = 59 # float | Minimum y coordinate (latitude). Coordinates are in WGS84 format in decimal degrees. Values between 59.0 and 72.0. (optional) (default to 59)
    x_max = 32 # float | Maximum x coordinate (longitude). Coordinates are in WGS84 format in decimal degrees. Values between 19.0 and 32.0. (optional) (default to 32)
    y_max = 72 # float | Maximum y coordinate (latitude). Coordinates are in WGS84 format in decimal degrees. Values between 59.0 and 72.0. (optional) (default to 72)

    try:
        # Current data of detailed weather forecast sections
        api_response = api_instance.forecast_sections_forecasts(last_updated=last_updated, road_number=road_number, x_min=x_min, y_min=y_min, x_max=x_max, y_max=y_max)
        print("The response of WeatherV1Api->forecast_sections_forecasts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WeatherV1Api->forecast_sections_forecasts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **last_updated** | **bool**| If parameter is given result will only contain update status. | [optional] [default to False]
 **road_number** | **int**| Road number | [optional] 
 **x_min** | **float**| Minimum x coordinate (longitude) Coordinates are in WGS84 format in decimal degrees. Values between 19.0 and 32.0. | [optional] [default to 19]
 **y_min** | **float**| Minimum y coordinate (latitude). Coordinates are in WGS84 format in decimal degrees. Values between 59.0 and 72.0. | [optional] [default to 59]
 **x_max** | **float**| Maximum x coordinate (longitude). Coordinates are in WGS84 format in decimal degrees. Values between 19.0 and 32.0. | [optional] [default to 32]
 **y_max** | **float**| Maximum y coordinate (latitude). Coordinates are in WGS84 format in decimal degrees. Values between 59.0 and 72.0. | [optional] [default to 72]

### Return type

[**ForecastSectionsWeatherDtoV1**](ForecastSectionsWeatherDtoV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.geo+json;charset=UTF-8, application/json;charset=UTF-8, application/geo+json;charset=UTF-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of Forecast Sections |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forecast_sections_simple**
> ForecastSectionFeatureCollectionSimpleV1 forecast_sections_simple(last_updated=last_updated, road_number=road_number, x_min=x_min, y_min=y_min, x_max=x_max, y_max=y_max)

The static information of simple weather forecast sections

### Example


```python
import openapi_client
from openapi_client.models.forecast_section_feature_collection_simple_v1 import ForecastSectionFeatureCollectionSimpleV1
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
    api_instance = openapi_client.WeatherV1Api(api_client)
    last_updated = False # bool | If parameter is given result will only contain update status. (optional) (default to False)
    road_number = 56 # int | Road number (optional)
    x_min = 19 # float | Minimum x coordinate (longitude) Coordinates are in WGS84 format in decimal degrees. Values between 19.0 and 32.0. (optional) (default to 19)
    y_min = 59 # float | Minimum y coordinate (latitude). Coordinates are in WGS84 format in decimal degrees. Values between 59.0 and 72.0. (optional) (default to 59)
    x_max = 32 # float | Maximum x coordinate (longitude). Coordinates are in WGS84 format in decimal degrees. Values between 19.0 and 32.0. (optional) (default to 32)
    y_max = 72 # float | Maximum y coordinate (latitude). Coordinates are in WGS84 format in decimal degrees. Values between 59.0 and 72.0. (optional) (default to 72)

    try:
        # The static information of simple weather forecast sections
        api_response = api_instance.forecast_sections_simple(last_updated=last_updated, road_number=road_number, x_min=x_min, y_min=y_min, x_max=x_max, y_max=y_max)
        print("The response of WeatherV1Api->forecast_sections_simple:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WeatherV1Api->forecast_sections_simple: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **last_updated** | **bool**| If parameter is given result will only contain update status. | [optional] [default to False]
 **road_number** | **int**| Road number | [optional] 
 **x_min** | **float**| Minimum x coordinate (longitude) Coordinates are in WGS84 format in decimal degrees. Values between 19.0 and 32.0. | [optional] [default to 19]
 **y_min** | **float**| Minimum y coordinate (latitude). Coordinates are in WGS84 format in decimal degrees. Values between 59.0 and 72.0. | [optional] [default to 59]
 **x_max** | **float**| Maximum x coordinate (longitude). Coordinates are in WGS84 format in decimal degrees. Values between 19.0 and 32.0. | [optional] [default to 32]
 **y_max** | **float**| Maximum y coordinate (latitude). Coordinates are in WGS84 format in decimal degrees. Values between 59.0 and 72.0. | [optional] [default to 72]

### Return type

[**ForecastSectionFeatureCollectionSimpleV1**](ForecastSectionFeatureCollectionSimpleV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.geo+json;charset=UTF-8, application/json;charset=UTF-8, application/geo+json;charset=UTF-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of simple forecast sections |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forecast_sections_simple_forecasts**
> ForecastSectionsWeatherDtoV1 forecast_sections_simple_forecasts(last_updated=last_updated, road_number=road_number, x_min=x_min, y_min=y_min, x_max=x_max, y_max=y_max)

Current data of simple weather forecast sections

### Example


```python
import openapi_client
from openapi_client.models.forecast_sections_weather_dto_v1 import ForecastSectionsWeatherDtoV1
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
    api_instance = openapi_client.WeatherV1Api(api_client)
    last_updated = False # bool | If parameter is given result will only contain update status. (optional) (default to False)
    road_number = 56 # int | Road number (optional)
    x_min = 19 # float | Minimum x coordinate (longitude) Coordinates are in WGS84 format in decimal degrees. Values between 19.0 and 32.0. (optional) (default to 19)
    y_min = 59 # float | Minimum y coordinate (latitude). Coordinates are in WGS84 format in decimal degrees. Values between 59.0 and 72.0. (optional) (default to 59)
    x_max = 32 # float | Maximum x coordinate (longitude). Coordinates are in WGS84 format in decimal degrees. Values between 19.0 and 32.0. (optional) (default to 32)
    y_max = 72 # float | Maximum y coordinate (latitude). Coordinates are in WGS84 format in decimal degrees. Values between 59.0 and 72.0. (optional) (default to 72)

    try:
        # Current data of simple weather forecast sections
        api_response = api_instance.forecast_sections_simple_forecasts(last_updated=last_updated, road_number=road_number, x_min=x_min, y_min=y_min, x_max=x_max, y_max=y_max)
        print("The response of WeatherV1Api->forecast_sections_simple_forecasts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WeatherV1Api->forecast_sections_simple_forecasts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **last_updated** | **bool**| If parameter is given result will only contain update status. | [optional] [default to False]
 **road_number** | **int**| Road number | [optional] 
 **x_min** | **float**| Minimum x coordinate (longitude) Coordinates are in WGS84 format in decimal degrees. Values between 19.0 and 32.0. | [optional] [default to 19]
 **y_min** | **float**| Minimum y coordinate (latitude). Coordinates are in WGS84 format in decimal degrees. Values between 59.0 and 72.0. | [optional] [default to 59]
 **x_max** | **float**| Maximum x coordinate (longitude). Coordinates are in WGS84 format in decimal degrees. Values between 19.0 and 32.0. | [optional] [default to 32]
 **y_max** | **float**| Maximum y coordinate (latitude). Coordinates are in WGS84 format in decimal degrees. Values between 59.0 and 72.0. | [optional] [default to 72]

### Return type

[**ForecastSectionsWeatherDtoV1**](ForecastSectionsWeatherDtoV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.geo+json;charset=UTF-8, application/json;charset=UTF-8, application/geo+json;charset=UTF-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of Forecast Sections |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **weather_data**
> WeatherStationsDataDtoV1 weather_data(last_updated=last_updated)

Current data of weather stations

### Example


```python
import openapi_client
from openapi_client.models.weather_stations_data_dto_v1 import WeatherStationsDataDtoV1
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
    api_instance = openapi_client.WeatherV1Api(api_client)
    last_updated = False # bool | If parameter is given result will only contain update status. (optional) (default to False)

    try:
        # Current data of weather stations
        api_response = api_instance.weather_data(last_updated=last_updated)
        print("The response of WeatherV1Api->weather_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WeatherV1Api->weather_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **last_updated** | **bool**| If parameter is given result will only contain update status. | [optional] [default to False]

### Return type

[**WeatherStationsDataDtoV1**](WeatherStationsDataDtoV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of weather station data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **weather_data_by_id**
> WeatherStationDataDtoV1 weather_data_by_id(id)

Current data of one weather station

### Example


```python
import openapi_client
from openapi_client.models.weather_station_data_dto_v1 import WeatherStationDataDtoV1
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
    api_instance = openapi_client.WeatherV1Api(api_client)
    id = 56 # int | TMS Station id

    try:
        # Current data of one weather station
        api_response = api_instance.weather_data_by_id(id)
        print("The response of WeatherV1Api->weather_data_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WeatherV1Api->weather_data_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| TMS Station id | 

### Return type

[**WeatherStationDataDtoV1**](WeatherStationDataDtoV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of weather station data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **weather_sensors**
> WeatherStationSensorsDtoV1 weather_sensors(last_updated=last_updated)

The static information of available sensors of weather stations

### Example


```python
import openapi_client
from openapi_client.models.weather_station_sensors_dto_v1 import WeatherStationSensorsDtoV1
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
    api_instance = openapi_client.WeatherV1Api(api_client)
    last_updated = False # bool | If parameter is given result will only contain update status. (optional) (default to False)

    try:
        # The static information of available sensors of weather stations
        api_response = api_instance.weather_sensors(last_updated=last_updated)
        print("The response of WeatherV1Api->weather_sensors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WeatherV1Api->weather_sensors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **last_updated** | **bool**| If parameter is given result will only contain update status. | [optional] [default to False]

### Return type

[**WeatherStationSensorsDtoV1**](WeatherStationSensorsDtoV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of weather station sensors |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **weather_station_by_road_station_id**
> WeatherStationFeatureDetailedV1 weather_station_by_road_station_id(id)

The static information of one weather station

### Example


```python
import openapi_client
from openapi_client.models.weather_station_feature_detailed_v1 import WeatherStationFeatureDetailedV1
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
    api_instance = openapi_client.WeatherV1Api(api_client)
    id = 56 # int | 

    try:
        # The static information of one weather station
        api_response = api_instance.weather_station_by_road_station_id(id)
        print("The response of WeatherV1Api->weather_station_by_road_station_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WeatherV1Api->weather_station_by_road_station_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**WeatherStationFeatureDetailedV1**](WeatherStationFeatureDetailedV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.geo+json;charset=UTF-8, application/json;charset=UTF-8, application/geo+json;charset=UTF-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of weather Station Feature |  -  |
**404** | Road Station not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **weather_stations**
> WeatherStationFeatureCollectionSimpleV1 weather_stations(last_updated=last_updated, state=state)

The static information of weather stations

### Example


```python
import openapi_client
from openapi_client.models.road_station_state import RoadStationState
from openapi_client.models.weather_station_feature_collection_simple_v1 import WeatherStationFeatureCollectionSimpleV1
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
    api_instance = openapi_client.WeatherV1Api(api_client)
    last_updated = False # bool | If parameter is given result will only contain update status. (optional) (default to False)
    state = openapi_client.RoadStationState() # RoadStationState | Return weather stations of given state. (optional)

    try:
        # The static information of weather stations
        api_response = api_instance.weather_stations(last_updated=last_updated, state=state)
        print("The response of WeatherV1Api->weather_stations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WeatherV1Api->weather_stations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **last_updated** | **bool**| If parameter is given result will only contain update status. | [optional] [default to False]
 **state** | [**RoadStationState**](.md)| Return weather stations of given state. | [optional] 

### Return type

[**WeatherStationFeatureCollectionSimpleV1**](WeatherStationFeatureCollectionSimpleV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.geo+json;charset=UTF-8, application/json;charset=UTF-8, application/geo+json;charset=UTF-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of weather Station Feature Collections |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

