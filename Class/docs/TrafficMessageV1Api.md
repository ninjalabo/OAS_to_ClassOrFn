# openapi_client.TrafficMessageV1Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**area_location_regions**](TrafficMessageV1Api.md#area_location_regions) | **GET** /api/traffic-message/v1/area-geometries | Traffic messages geometries for regions
[**area_location_regions1**](TrafficMessageV1Api.md#area_location_regions1) | **GET** /api/traffic-message/v1/area-geometries/{locationCode} | Traffic messages geometries for regions
[**location_by_id**](TrafficMessageV1Api.md#location_by_id) | **GET** /api/traffic-message/v1/locations/{id} | The static information of one location
[**location_types**](TrafficMessageV1Api.md#location_types) | **GET** /api/traffic-message/v1/locations/types | The static information of location types and locationsubtypes
[**location_versions**](TrafficMessageV1Api.md#location_versions) | **GET** /api/traffic-message/v1/locations/versions | List available location versions
[**locations**](TrafficMessageV1Api.md#locations) | **GET** /api/traffic-message/v1/locations | The static information of locations
[**traffic_message_datex2**](TrafficMessageV1Api.md#traffic_message_datex2) | **GET** /api/traffic-message/v1/messages.datex2 | Active traffic messages as Datex2
[**traffic_message_datex2_by_situation_id**](TrafficMessageV1Api.md#traffic_message_datex2_by_situation_id) | **GET** /api/traffic-message/v1/messages/{situationId}.datex2 | Traffic messages by situationId as Datex2
[**traffic_message_simple**](TrafficMessageV1Api.md#traffic_message_simple) | **GET** /api/traffic-message/v1/messages | Active traffic messages as simple JSON
[**traffic_message_simple_by_situation_id**](TrafficMessageV1Api.md#traffic_message_simple_by_situation_id) | **GET** /api/traffic-message/v1/messages/{situationId} | Traffic messages history by situation id as simple JSON


# **area_location_regions**
> RegionGeometryFeatureCollectionV1 area_location_regions(last_updated=last_updated, include_geometry=include_geometry, effective_date=effective_date)

Traffic messages geometries for regions

### Example


```python
import openapi_client
from openapi_client.models.region_geometry_feature_collection_v1 import RegionGeometryFeatureCollectionV1
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
    api_instance = openapi_client.TrafficMessageV1Api(api_client)
    last_updated = True # bool | If the parameter value is true, then the result will only contain update status. (optional) (default to True)
    include_geometry = False # bool | If the parameter value is false, then the result will not contain also geometries. (optional) (default to False)
    effective_date = '2013-10-20T19:20:30+01:00' # datetime | When effectiveDate parameter is given only effective geometries on that date are returned (optional)

    try:
        # Traffic messages geometries for regions
        api_response = api_instance.area_location_regions(last_updated=last_updated, include_geometry=include_geometry, effective_date=effective_date)
        print("The response of TrafficMessageV1Api->area_location_regions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrafficMessageV1Api->area_location_regions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **last_updated** | **bool**| If the parameter value is true, then the result will only contain update status. | [optional] [default to True]
 **include_geometry** | **bool**| If the parameter value is false, then the result will not contain also geometries. | [optional] [default to False]
 **effective_date** | **datetime**| When effectiveDate parameter is given only effective geometries on that date are returned | [optional] 

### Return type

[**RegionGeometryFeatureCollectionV1**](RegionGeometryFeatureCollectionV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.geo+json;charset=UTF-8, application/json;charset=UTF-8, application/geo+json;charset=UTF-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of geometries |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **area_location_regions1**
> RegionGeometryFeatureCollectionV1 area_location_regions1(location_code, last_updated=last_updated, include_geometry=include_geometry, effective_date=effective_date)

Traffic messages geometries for regions

### Example


```python
import openapi_client
from openapi_client.models.region_geometry_feature_collection_v1 import RegionGeometryFeatureCollectionV1
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
    api_instance = openapi_client.TrafficMessageV1Api(api_client)
    location_code = 56 # int | Location code id
    last_updated = False # bool | If the parameter value is true, then the result will only contain update status. (optional) (default to False)
    include_geometry = False # bool | If the parameter value is false, then the result will not contain also geometries. (optional) (default to False)
    effective_date = '2013-10-20T19:20:30+01:00' # datetime | When effectiveDate parameter is given only effective geometries on that date are returned (optional)

    try:
        # Traffic messages geometries for regions
        api_response = api_instance.area_location_regions1(location_code, last_updated=last_updated, include_geometry=include_geometry, effective_date=effective_date)
        print("The response of TrafficMessageV1Api->area_location_regions1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrafficMessageV1Api->area_location_regions1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_code** | **int**| Location code id | 
 **last_updated** | **bool**| If the parameter value is true, then the result will only contain update status. | [optional] [default to False]
 **include_geometry** | **bool**| If the parameter value is false, then the result will not contain also geometries. | [optional] [default to False]
 **effective_date** | **datetime**| When effectiveDate parameter is given only effective geometries on that date are returned | [optional] 

### Return type

[**RegionGeometryFeatureCollectionV1**](RegionGeometryFeatureCollectionV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.geo+json;charset=UTF-8, application/json;charset=UTF-8, application/geo+json;charset=UTF-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of geometries |  -  |
**404** | Geometry not not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **location_by_id**
> LocationFeatureV1 location_by_id(id, version=version)

The static information of one location

### Example


```python
import openapi_client
from openapi_client.models.location_feature_v1 import LocationFeatureV1
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
    api_instance = openapi_client.TrafficMessageV1Api(api_client)
    id = 56 # int | 
    version = 'latest' # str | If parameter is given use this version. (optional) (default to 'latest')

    try:
        # The static information of one location
        api_response = api_instance.location_by_id(id, version=version)
        print("The response of TrafficMessageV1Api->location_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrafficMessageV1Api->location_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **version** | **str**| If parameter is given use this version. | [optional] [default to &#39;latest&#39;]

### Return type

[**LocationFeatureV1**](LocationFeatureV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.geo+json;charset=UTF-8, application/json;charset=UTF-8, application/geo+json;charset=UTF-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of location |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **location_types**
> LocationTypesDtoV1 location_types(version=version, last_updated=last_updated)

The static information of location types and locationsubtypes

### Example


```python
import openapi_client
from openapi_client.models.location_types_dto_v1 import LocationTypesDtoV1
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
    api_instance = openapi_client.TrafficMessageV1Api(api_client)
    version = 'latest' # str | If parameter is given use this version. (optional) (default to 'latest')
    last_updated = False # bool | If parameter is given result will only contain update status. (optional) (default to False)

    try:
        # The static information of location types and locationsubtypes
        api_response = api_instance.location_types(version=version, last_updated=last_updated)
        print("The response of TrafficMessageV1Api->location_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrafficMessageV1Api->location_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| If parameter is given use this version. | [optional] [default to &#39;latest&#39;]
 **last_updated** | **bool**| If parameter is given result will only contain update status. | [optional] [default to False]

### Return type

[**LocationTypesDtoV1**](LocationTypesDtoV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of location types and location subtypes |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **location_versions**
> List[LocationVersionDtoV1] location_versions()

List available location versions

### Example


```python
import openapi_client
from openapi_client.models.location_version_dto_v1 import LocationVersionDtoV1
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
    api_instance = openapi_client.TrafficMessageV1Api(api_client)

    try:
        # List available location versions
        api_response = api_instance.location_versions()
        print("The response of TrafficMessageV1Api->location_versions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrafficMessageV1Api->location_versions: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[LocationVersionDtoV1]**](LocationVersionDtoV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of location versions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **locations**
> LocationFeatureCollectionV1 locations(version=version, last_updated=last_updated)

The static information of locations

### Example


```python
import openapi_client
from openapi_client.models.location_feature_collection_v1 import LocationFeatureCollectionV1
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
    api_instance = openapi_client.TrafficMessageV1Api(api_client)
    version = 'latest' # str | If parameter is given use this version. (optional) (default to 'latest')
    last_updated = False # bool | If parameter is given result will only contain update status. (optional) (default to False)

    try:
        # The static information of locations
        api_response = api_instance.locations(version=version, last_updated=last_updated)
        print("The response of TrafficMessageV1Api->locations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrafficMessageV1Api->locations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| If parameter is given use this version. | [optional] [default to &#39;latest&#39;]
 **last_updated** | **bool**| If parameter is given result will only contain update status. | [optional] [default to False]

### Return type

[**LocationFeatureCollectionV1**](LocationFeatureCollectionV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.geo+json;charset=UTF-8, application/json;charset=UTF-8, application/geo+json;charset=UTF-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of locations |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **traffic_message_datex2**
> D2LogicalModel traffic_message_datex2(situation_type, inactive_hours=inactive_hours)

Active traffic messages as Datex2

### Example


```python
import openapi_client
from openapi_client.models.d2_logical_model import D2LogicalModel
from openapi_client.models.situation_type_v1 import SituationTypeV1
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
    api_instance = openapi_client.TrafficMessageV1Api(api_client)
    situation_type = ["TRAFFIC_ANNOUNCEMENT"] # List[SituationTypeV1] | Situation type. (default to ["TRAFFIC_ANNOUNCEMENT"])
    inactive_hours = 0 # int | Return traffic messages from given amount of hours in the past. (optional) (default to 0)

    try:
        # Active traffic messages as Datex2
        api_response = api_instance.traffic_message_datex2(situation_type, inactive_hours=inactive_hours)
        print("The response of TrafficMessageV1Api->traffic_message_datex2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrafficMessageV1Api->traffic_message_datex2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **situation_type** | [**List[SituationTypeV1]**](SituationTypeV1.md)| Situation type. | [default to [&quot;TRAFFIC_ANNOUNCEMENT&quot;]]
 **inactive_hours** | **int**| Return traffic messages from given amount of hours in the past. | [optional] [default to 0]

### Return type

[**D2LogicalModel**](D2LogicalModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8, application/xml;charset=UTF-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of traffic messages |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **traffic_message_datex2_by_situation_id**
> D2LogicalModel traffic_message_datex2_by_situation_id(situation_id, latest=latest)

Traffic messages by situationId as Datex2

### Example


```python
import openapi_client
from openapi_client.models.d2_logical_model import D2LogicalModel
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
    api_instance = openapi_client.TrafficMessageV1Api(api_client)
    situation_id = 'situation_id_example' # str | Situation id.
    latest = True # bool | If the parameter value is true, then only the latest message will be returned otherwise all messages are returned (optional) (default to True)

    try:
        # Traffic messages by situationId as Datex2
        api_response = api_instance.traffic_message_datex2_by_situation_id(situation_id, latest=latest)
        print("The response of TrafficMessageV1Api->traffic_message_datex2_by_situation_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrafficMessageV1Api->traffic_message_datex2_by_situation_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **situation_id** | **str**| Situation id. | 
 **latest** | **bool**| If the parameter value is true, then only the latest message will be returned otherwise all messages are returned | [optional] [default to True]

### Return type

[**D2LogicalModel**](D2LogicalModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8, application/xml;charset=UTF-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of traffic messages |  -  |
**404** | Situation id not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **traffic_message_simple**
> TrafficAnnouncementFeatureCollectionV1 traffic_message_simple(situation_type, inactive_hours=inactive_hours, include_area_geometry=include_area_geometry)

Active traffic messages as simple JSON

### Example


```python
import openapi_client
from openapi_client.models.situation_type_v1 import SituationTypeV1
from openapi_client.models.traffic_announcement_feature_collection_v1 import TrafficAnnouncementFeatureCollectionV1
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
    api_instance = openapi_client.TrafficMessageV1Api(api_client)
    situation_type = ["TRAFFIC_ANNOUNCEMENT"] # List[SituationTypeV1] | Situation type. (default to ["TRAFFIC_ANNOUNCEMENT"])
    inactive_hours = 0 # int | Return traffic messages from given amount of hours in the past. (optional) (default to 0)
    include_area_geometry = False # bool | If the parameter value is false, then the GeoJson geometry will be empty for announcements with area locations. Geometries for areas can be fetched from Traffic messages geometries for regions -api (optional) (default to False)

    try:
        # Active traffic messages as simple JSON
        api_response = api_instance.traffic_message_simple(situation_type, inactive_hours=inactive_hours, include_area_geometry=include_area_geometry)
        print("The response of TrafficMessageV1Api->traffic_message_simple:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrafficMessageV1Api->traffic_message_simple: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **situation_type** | [**List[SituationTypeV1]**](SituationTypeV1.md)| Situation type. | [default to [&quot;TRAFFIC_ANNOUNCEMENT&quot;]]
 **inactive_hours** | **int**| Return traffic messages from given amount of hours in the past. | [optional] [default to 0]
 **include_area_geometry** | **bool**| If the parameter value is false, then the GeoJson geometry will be empty for announcements with area locations. Geometries for areas can be fetched from Traffic messages geometries for regions -api | [optional] [default to False]

### Return type

[**TrafficAnnouncementFeatureCollectionV1**](TrafficAnnouncementFeatureCollectionV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.geo+json;charset=UTF-8, application/json;charset=UTF-8, application/geo+json;charset=UTF-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of traffic messages |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **traffic_message_simple_by_situation_id**
> TrafficAnnouncementFeatureCollectionV1 traffic_message_simple_by_situation_id(situation_id, include_area_geometry=include_area_geometry, latest=latest)

Traffic messages history by situation id as simple JSON

### Example


```python
import openapi_client
from openapi_client.models.traffic_announcement_feature_collection_v1 import TrafficAnnouncementFeatureCollectionV1
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
    api_instance = openapi_client.TrafficMessageV1Api(api_client)
    situation_id = 'situation_id_example' # str | Situation id.
    include_area_geometry = False # bool | If the parameter value is false, then the GeoJson geometry will be empty for announcements with area locations. Geometries for areas can be fetched from Traffic messages geometries for regions -api (optional) (default to False)
    latest = False # bool | If the parameter value is true, then only the latest message will be returned (optional) (default to False)

    try:
        # Traffic messages history by situation id as simple JSON
        api_response = api_instance.traffic_message_simple_by_situation_id(situation_id, include_area_geometry=include_area_geometry, latest=latest)
        print("The response of TrafficMessageV1Api->traffic_message_simple_by_situation_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrafficMessageV1Api->traffic_message_simple_by_situation_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **situation_id** | **str**| Situation id. | 
 **include_area_geometry** | **bool**| If the parameter value is false, then the GeoJson geometry will be empty for announcements with area locations. Geometries for areas can be fetched from Traffic messages geometries for regions -api | [optional] [default to False]
 **latest** | **bool**| If the parameter value is true, then only the latest message will be returned | [optional] [default to False]

### Return type

[**TrafficAnnouncementFeatureCollectionV1**](TrafficAnnouncementFeatureCollectionV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.geo+json;charset=UTF-8, application/json;charset=UTF-8, application/geo+json;charset=UTF-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval of traffic messages |  -  |
**404** | Situation id not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

