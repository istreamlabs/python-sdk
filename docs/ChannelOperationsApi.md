# openapi_client.ChannelOperationsApi

All URIs are relative to *https://api.istreamplanet.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clear_dvr_window**](ChannelOperationsApi.md#clear_dvr_window) | **DELETE** /v2/channels/{channel-id}/dvr-window | Clear DVR Window
[**get_signals**](ChannelOperationsApi.md#get_signals) | **GET** /v2/channels/{channel-id}/signal | Get Signals
[**insert_id3**](ChannelOperationsApi.md#insert_id3) | **POST** /v2/channels/{channel-id}/id3 | Insert ID3
[**insert_scte35**](ChannelOperationsApi.md#insert_scte35) | **POST** /v2/channels/{channel-id}/scte35 | Insert SCTE-35
[**preview_image**](ChannelOperationsApi.md#preview_image) | **GET** /v2/channels/{channel-id}/preview-image | Get Preview Image
[**program_end**](ChannelOperationsApi.md#program_end) | **POST** /v2/channels/{channel-id}/program-end | Program End
[**program_start**](ChannelOperationsApi.md#program_start) | **POST** /v2/channels/{channel-id}/program-start | Program Start
[**signal**](ChannelOperationsApi.md#signal) | **POST** /v2/channels/{channel-id}/signal | Generic Signal
[**slate_in**](ChannelOperationsApi.md#slate_in) | **POST** /v2/channels/{channel-id}/slate | Slate in
[**slate_out**](ChannelOperationsApi.md#slate_out) | **DELETE** /v2/channels/{channel-id}/slate | Slate out
[**splice_end**](ChannelOperationsApi.md#splice_end) | **POST** /v2/channels/{channel-id}/splice-end | Splice Insert End
[**splice_start**](ChannelOperationsApi.md#splice_start) | **POST** /v2/channels/{channel-id}/splice-start | Splice Insert Start


# **clear_dvr_window**
> clear_dvr_window(channel_id)

Clear DVR Window

Clears the DVR window for the channel by removing all video segments in the manifest from before the request.  This sets the earliest time a player can rewind to this point.

### Example

* OAuth Authentication (authcode):
* OAuth Authentication (m2m):

```python
import time
import openapi_client
from openapi_client.api import channel_operations_api
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
    api_instance = channel_operations_api.ChannelOperationsApi(api_client)
    channel_id = "" # str | Unique channel identifier

    # example passing only required values which don't have defaults set
    try:
        # Clear DVR Window
        api_instance.clear_dvr_window(channel_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ChannelOperationsApi->clear_dvr_window: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| Unique channel identifier |

### Return type

void (empty response body)

### Authorization

[authcode](../README.md#authcode), [m2m](../README.md#m2m)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad Request |  * Content-Type - Content-Type <br>  |
**404** | Not Found |  * Content-Type - Content-Type <br>  |
**500** | Internal Server Error |  * Content-Type - Content-Type <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_signals**
> SegmentList get_signals(channel_id)

Get Signals

Returns the active signals for a channel.

### Example

* OAuth Authentication (authcode):
* OAuth Authentication (m2m):

```python
import time
import openapi_client
from openapi_client.api import channel_operations_api
from openapi_client.model.segment_list import SegmentList
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
    api_instance = channel_operations_api.ChannelOperationsApi(api_client)
    channel_id = "" # str | Unique channel identifier

    # example passing only required values which don't have defaults set
    try:
        # Get Signals
        api_response = api_instance.get_signals(channel_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ChannelOperationsApi->get_signals: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| Unique channel identifier |

### Return type

[**SegmentList**](SegmentList.md)

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
**406** | Not Acceptable |  * Content-Type - Content-Type <br>  |
**500** | Internal Server Error |  * Content-Type - Content-Type <br>  |
**503** | Service Unavailable |  * Content-Type - Content-Type <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_id3**
> InsertMetadataResult insert_id3(channel_id)

Insert ID3

Inserts the provided UTF-8 text metadata in the output stream embedded in a TXXX frame of a ID3 tag.

### Example

* OAuth Authentication (authcode):
* OAuth Authentication (m2m):

```python
import time
import openapi_client
from openapi_client.api import channel_operations_api
from openapi_client.model.insert_metadata_request import InsertMetadataRequest
from openapi_client.model.insert_metadata_result import InsertMetadataResult
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
    api_instance = channel_operations_api.ChannelOperationsApi(api_client)
    channel_id = "" # str | Unique channel identifier
    accept = "Accept_example" # str | List of accepted Content-Type headers (optional)
    insert_metadata_request = InsertMetadataRequest(
        payload="payload_example",
    ) # InsertMetadataRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Insert ID3
        api_response = api_instance.insert_id3(channel_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ChannelOperationsApi->insert_id3: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Insert ID3
        api_response = api_instance.insert_id3(channel_id, accept=accept, insert_metadata_request=insert_metadata_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ChannelOperationsApi->insert_id3: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| Unique channel identifier |
 **accept** | **str**| List of accepted Content-Type headers | [optional]
 **insert_metadata_request** | [**InsertMetadataRequest**](InsertMetadataRequest.md)|  | [optional]

### Return type

[**InsertMetadataResult**](InsertMetadataResult.md)

### Authorization

[authcode](../README.md#authcode), [m2m](../README.md#m2m)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Content-Type - Content-Type <br>  |
**400** | Bad Request |  * Content-Type - Content-Type <br>  |
**404** | Not Found |  * Content-Type - Content-Type <br>  |
**409** | Conflict |  * Content-Type - Content-Type <br>  |
**500** | Internal Server Error |  * Content-Type - Content-Type <br>  |
**503** | Service Unavailable |  * Content-Type - Content-Type <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_scte35**
> insert_scte35(channel_id)

Insert SCTE-35

Inserts a SCTE-35 formatted binary payload into the channel.

### Example

* OAuth Authentication (authcode):
* OAuth Authentication (m2m):

```python
import time
import openapi_client
from openapi_client.api import channel_operations_api
from openapi_client.model.scte35 import Scte35
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
    api_instance = channel_operations_api.ChannelOperationsApi(api_client)
    channel_id = "" # str | Unique channel identifier
    scte35 = Scte35(
        payload="/DAvAAAAAAAAAP/wBQb/d2+7OgAZAhdDVUVJAAAD6ACACAic1fd1d2+7OjABAeo2v/g=",
    ) # Scte35 |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Insert SCTE-35
        api_instance.insert_scte35(channel_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ChannelOperationsApi->insert_scte35: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Insert SCTE-35
        api_instance.insert_scte35(channel_id, scte35=scte35)
    except openapi_client.ApiException as e:
        print("Exception when calling ChannelOperationsApi->insert_scte35: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| Unique channel identifier |
 **scte35** | [**Scte35**](Scte35.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

[authcode](../README.md#authcode), [m2m](../README.md#m2m)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad Request |  * Content-Type - Content-Type <br>  |
**404** | Not Found |  * Content-Type - Content-Type <br>  |
**500** | Internal Server Error |  * Content-Type - Content-Type <br>  |
**503** | Service Unavailable |  * Content-Type - Content-Type <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **preview_image**
> preview_image(channel_id)

Get Preview Image

Get a static image of what your channel is outputting.  Valid Accept headers are: image/jpeg

### Example

* OAuth Authentication (authcode):
* OAuth Authentication (m2m):

```python
import time
import openapi_client
from openapi_client.api import channel_operations_api
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
    api_instance = channel_operations_api.ChannelOperationsApi(api_client)
    channel_id = "" # str | Unique channel identifier
    accept = "Accept_example" # str | List of accepted Content-Type headers (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Preview Image
        api_instance.preview_image(channel_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ChannelOperationsApi->preview_image: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Preview Image
        api_instance.preview_image(channel_id, accept=accept)
    except openapi_client.ApiException as e:
        print("Exception when calling ChannelOperationsApi->preview_image: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| Unique channel identifier |
 **accept** | **str**| List of accepted Content-Type headers | [optional]

### Return type

void (empty response body)

### Authorization

[authcode](../README.md#authcode), [m2m](../README.md#m2m)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  * Content-Type - Content-Type <br>  |
**404** | Not Found |  * Content-Type - Content-Type <br>  |
**406** | Not Acceptable |  * Content-Type - Content-Type <br>  |
**500** | Internal Server Error |  * Content-Type - Content-Type <br>  |
**501** | Not Implemented |  * Content-Type - Content-Type <br>  |
**503** | Service Unavailable |  * Content-Type - Content-Type <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **program_end**
> program_end(channel_id)

Program End

Inserts a 'program end' SCTE-35 message into the channel.  This route should only be used for non-overlapping program markers.  If you want overlapping program makers please use Generic Signal instead.

### Example

* OAuth Authentication (authcode):
* OAuth Authentication (m2m):

```python
import time
import openapi_client
from openapi_client.api import channel_operations_api
from openapi_client.model.program_signal import ProgramSignal
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
    api_instance = channel_operations_api.ChannelOperationsApi(api_client)
    channel_id = "" # str | Unique channel identifier
    program_signal = ProgramSignal(
        event_id=1234,
    ) # ProgramSignal |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Program End
        api_instance.program_end(channel_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ChannelOperationsApi->program_end: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Program End
        api_instance.program_end(channel_id, program_signal=program_signal)
    except openapi_client.ApiException as e:
        print("Exception when calling ChannelOperationsApi->program_end: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| Unique channel identifier |
 **program_signal** | [**ProgramSignal**](ProgramSignal.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

[authcode](../README.md#authcode), [m2m](../README.md#m2m)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad Request |  * Content-Type - Content-Type <br>  |
**404** | Not Found |  * Content-Type - Content-Type <br>  |
**409** | Conflict |  * Content-Type - Content-Type <br>  |
**500** | Internal Server Error |  * Content-Type - Content-Type <br>  |
**503** | Service Unavailable |  * Content-Type - Content-Type <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **program_start**
> program_start(channel_id)

Program Start

Inserts a 'program start' SCTE-35 message into the channel.  This route should only be used for non-overlapping program markers.  If you want overlapping program makers please use Generic Signal instead.

### Example

* OAuth Authentication (authcode):
* OAuth Authentication (m2m):

```python
import time
import openapi_client
from openapi_client.api import channel_operations_api
from openapi_client.model.program_signal import ProgramSignal
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
    api_instance = channel_operations_api.ChannelOperationsApi(api_client)
    channel_id = "" # str | Unique channel identifier
    program_signal = ProgramSignal(
        event_id=1234,
    ) # ProgramSignal |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Program Start
        api_instance.program_start(channel_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ChannelOperationsApi->program_start: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Program Start
        api_instance.program_start(channel_id, program_signal=program_signal)
    except openapi_client.ApiException as e:
        print("Exception when calling ChannelOperationsApi->program_start: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| Unique channel identifier |
 **program_signal** | [**ProgramSignal**](ProgramSignal.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

[authcode](../README.md#authcode), [m2m](../README.md#m2m)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad Request |  * Content-Type - Content-Type <br>  |
**404** | Not Found |  * Content-Type - Content-Type <br>  |
**409** | Conflict |  * Content-Type - Content-Type <br>  |
**500** | Internal Server Error |  * Content-Type - Content-Type <br>  |
**503** | Service Unavailable |  * Content-Type - Content-Type <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **signal**
> signal(channel_id)

Generic Signal

Inserts a SCTE-35 message into the channel.

### Example

* OAuth Authentication (authcode):
* OAuth Authentication (m2m):

```python
import time
import openapi_client
from openapi_client.api import channel_operations_api
from openapi_client.model.generic_signal_list import GenericSignalList
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
    api_instance = channel_operations_api.ChannelOperationsApi(api_client)
    channel_id = "" # str | Unique channel identifier
    generic_signal_list = GenericSignalList([
        GenericSignal(
            duration=30000,
            event_id=1234,
            segment_type="program",
            signal_type="start",
            slate_uri="https://www.example.com/logo.ts",
            type="none",
            upids=["03:ABCD0001000H","08:0A42235B81BC70FC","06:0000-0001-2C52-0000-P-0000-0000-0"],
        ),
    ]) # GenericSignalList |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Generic Signal
        api_instance.signal(channel_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ChannelOperationsApi->signal: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Generic Signal
        api_instance.signal(channel_id, generic_signal_list=generic_signal_list)
    except openapi_client.ApiException as e:
        print("Exception when calling ChannelOperationsApi->signal: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| Unique channel identifier |
 **generic_signal_list** | [**GenericSignalList**](GenericSignalList.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

[authcode](../README.md#authcode), [m2m](../README.md#m2m)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**207** | Multi-status response; see body for details |  -  |
**400** | Bad Request |  * Content-Type - Content-Type <br>  |
**404** | Not Found |  * Content-Type - Content-Type <br>  |
**500** | Internal Server Error |  * Content-Type - Content-Type <br>  |
**503** | Service Unavailable |  * Content-Type - Content-Type <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slate_in**
> slate_in(channel_id)

Slate in

Replaces the current video source with a slate image or video.

### Example

* OAuth Authentication (authcode):
* OAuth Authentication (m2m):

```python
import time
import openapi_client
from openapi_client.api import channel_operations_api
from openapi_client.model.error_model import ErrorModel
from openapi_client.model.slate import Slate
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
    api_instance = channel_operations_api.ChannelOperationsApi(api_client)
    channel_id = "" # str | Unique channel identifier
    slate = Slate(
        duration=30000,
        uri="https://www.example.com/logo.ts",
    ) # Slate |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Slate in
        api_instance.slate_in(channel_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ChannelOperationsApi->slate_in: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Slate in
        api_instance.slate_in(channel_id, slate=slate)
    except openapi_client.ApiException as e:
        print("Exception when calling ChannelOperationsApi->slate_in: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| Unique channel identifier |
 **slate** | [**Slate**](Slate.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

[authcode](../README.md#authcode), [m2m](../README.md#m2m)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad Request |  * Content-Type - Content-Type <br>  |
**404** | Not Found |  * Content-Type - Content-Type <br>  |
**409** | Conflict |  * Content-Type - Content-Type <br>  |
**500** | Internal Server Error |  * Content-Type - Content-Type <br>  |
**503** | Service Unavailable |  * Content-Type - Content-Type <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slate_out**
> slate_out(channel_id)

Slate out

Removes any active slate and show the source video content.

### Example

* OAuth Authentication (authcode):
* OAuth Authentication (m2m):

```python
import time
import openapi_client
from openapi_client.api import channel_operations_api
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
    api_instance = channel_operations_api.ChannelOperationsApi(api_client)
    channel_id = "" # str | Unique channel identifier

    # example passing only required values which don't have defaults set
    try:
        # Slate out
        api_instance.slate_out(channel_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ChannelOperationsApi->slate_out: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| Unique channel identifier |

### Return type

void (empty response body)

### Authorization

[authcode](../README.md#authcode), [m2m](../README.md#m2m)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad Request |  * Content-Type - Content-Type <br>  |
**404** | Not Found |  * Content-Type - Content-Type <br>  |
**409** | Conflict |  * Content-Type - Content-Type <br>  |
**500** | Internal Server Error |  * Content-Type - Content-Type <br>  |
**503** | Service Unavailable |  * Content-Type - Content-Type <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **splice_end**
> splice_end(channel_id)

Splice Insert End

Inserts a 'splice insert end' SCTE-35 message into the channel.

### Example

* OAuth Authentication (authcode):
* OAuth Authentication (m2m):

```python
import time
import openapi_client
from openapi_client.api import channel_operations_api
from openapi_client.model.splice_insert_end_signal import SpliceInsertEndSignal
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
    api_instance = channel_operations_api.ChannelOperationsApi(api_client)
    channel_id = "" # str | Unique channel identifier
    splice_insert_end_signal = SpliceInsertEndSignal(
        event_id=1234,
    ) # SpliceInsertEndSignal |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Splice Insert End
        api_instance.splice_end(channel_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ChannelOperationsApi->splice_end: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Splice Insert End
        api_instance.splice_end(channel_id, splice_insert_end_signal=splice_insert_end_signal)
    except openapi_client.ApiException as e:
        print("Exception when calling ChannelOperationsApi->splice_end: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| Unique channel identifier |
 **splice_insert_end_signal** | [**SpliceInsertEndSignal**](SpliceInsertEndSignal.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

[authcode](../README.md#authcode), [m2m](../README.md#m2m)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad Request |  * Content-Type - Content-Type <br>  |
**404** | Not Found |  * Content-Type - Content-Type <br>  |
**409** | Conflict |  * Content-Type - Content-Type <br>  |
**500** | Internal Server Error |  * Content-Type - Content-Type <br>  |
**503** | Service Unavailable |  * Content-Type - Content-Type <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **splice_start**
> splice_start(channel_id)

Splice Insert Start

Inserts a 'splice insert start' SCTE-35 message into the channel.

### Example

* OAuth Authentication (authcode):
* OAuth Authentication (m2m):

```python
import time
import openapi_client
from openapi_client.api import channel_operations_api
from openapi_client.model.splice_insert_start_signal import SpliceInsertStartSignal
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
    api_instance = channel_operations_api.ChannelOperationsApi(api_client)
    channel_id = "" # str | Unique channel identifier
    splice_insert_start_signal = SpliceInsertStartSignal(
        duration=30000,
        event_id=1234,
        slate_uri="https://www.example.com/logo.ts",
        upids=["03:ABCD0001000H","08:0A42235B81BC70FC","06:0000-0001-2C52-0000-P-0000-0000-0"],
    ) # SpliceInsertStartSignal |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Splice Insert Start
        api_instance.splice_start(channel_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ChannelOperationsApi->splice_start: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Splice Insert Start
        api_instance.splice_start(channel_id, splice_insert_start_signal=splice_insert_start_signal)
    except openapi_client.ApiException as e:
        print("Exception when calling ChannelOperationsApi->splice_start: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| Unique channel identifier |
 **splice_insert_start_signal** | [**SpliceInsertStartSignal**](SpliceInsertStartSignal.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

[authcode](../README.md#authcode), [m2m](../README.md#m2m)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad Request |  * Content-Type - Content-Type <br>  |
**404** | Not Found |  * Content-Type - Content-Type <br>  |
**409** | Conflict |  * Content-Type - Content-Type <br>  |
**500** | Internal Server Error |  * Content-Type - Content-Type <br>  |
**503** | Service Unavailable |  * Content-Type - Content-Type <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
