# openapi_client.SourcesApi

All URIs are relative to *https://api.istreamplanet.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_source**](SourcesApi.md#get_source) | **GET** /v2/sources/{source-id} | Get Source
[**list_sources**](SourcesApi.md#list_sources) | **GET** /v2/sources | List Sources


# **get_source**
> Source get_source(source_id)

Get Source

Get a source's configuration

### Example

* OAuth Authentication (authcode):
* OAuth Authentication (m2m):

```python
import time
import openapi_client
from openapi_client.api import sources_api
from openapi_client.model.source import Source
from openapi_client.model.error_model import ErrorModel
from pprint import pprint
# Defining the host is optional and defaults to https://api.istreamplanet.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.istreamplanet.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: authcode
configuration = openapi_client.Configuration(
    host = "https://api.istreamplanet.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: m2m
configuration = openapi_client.Configuration(
    host = "https://api.istreamplanet.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sources_api.SourcesApi(api_client)
    source_id = "jUR,rZ#UM/?R,Fp^l6$ARj" # str | Unique source identifier

    # example passing only required values which don't have defaults set
    try:
        # Get Source
        api_response = api_instance.get_source(source_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SourcesApi->get_source: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**| Unique source identifier |

### Return type

[**Source**](Source.md)

### Authorization

[authcode](../README.md#authcode), [m2m](../README.md#m2m)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Content-Type - Content-Type <br>  * ETag - ETag <br>  |
**400** | Bad Request |  * Content-Type - Content-Type <br>  |
**404** | Not Found |  * Content-Type - Content-Type <br>  |
**500** | Internal Server Error |  * Content-Type - Content-Type <br>  |
**503** | Service Unavailable |  * Content-Type - Content-Type <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sources**
> SummaryList list_sources()

List Sources

Get a list of sources that are used to create channels.

### Example

* OAuth Authentication (authcode):
* OAuth Authentication (m2m):

```python
import time
import openapi_client
from openapi_client.api import sources_api
from openapi_client.model.error_model import ErrorModel
from openapi_client.model.summary_list import SummaryList
from pprint import pprint
# Defining the host is optional and defaults to https://api.istreamplanet.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.istreamplanet.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: authcode
configuration = openapi_client.Configuration(
    host = "https://api.istreamplanet.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: m2m
configuration = openapi_client.Configuration(
    host = "https://api.istreamplanet.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sources_api.SourcesApi(api_client)
    cursor = "cursor_example" # str | Current page cursor (optional)
    page_size = 100 # int | Number of items to return (optional) if omitted the server will use the default value of 100

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Sources
        api_response = api_instance.list_sources(cursor=cursor, page_size=page_size)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SourcesApi->list_sources: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| Current page cursor | [optional]
 **page_size** | **int**| Number of items to return | [optional] if omitted the server will use the default value of 100

### Return type

[**SummaryList**](SummaryList.md)

### Authorization

[authcode](../README.md#authcode), [m2m](../README.md#m2m)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Content-Type - Content-Type <br>  * Link - Link <br>  |
**400** | Bad Request |  * Content-Type - Content-Type <br>  |
**500** | Internal Server Error |  * Content-Type - Content-Type <br>  |
**503** | Service Unavailable |  * Content-Type - Content-Type <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

