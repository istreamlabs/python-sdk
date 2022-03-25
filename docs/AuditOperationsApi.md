# openapi_client.AuditOperationsApi

All URIs are relative to *https://api.istreamplanet.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_channel_timeline**](AuditOperationsApi.md#get_channel_timeline) | **GET** /v2/channels/{channel-id}/timeline | Get Channel Timeline


# **get_channel_timeline**
> ChannelTimelineEntryList get_channel_timeline(channel_id)

Get Channel Timeline

Returns up to twenty items from the event timeline for a channel, sorted in reverse-chronological order.

### Example

* OAuth Authentication (authcode):
* OAuth Authentication (m2m):

```python
import time
import openapi_client
from openapi_client.api import audit_operations_api
from openapi_client.model.channel_timeline_entry_list import ChannelTimelineEntryList
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
    api_instance = audit_operations_api.AuditOperationsApi(api_client)
    channel_id = "" # str | Unique channel identifier
    offset = 1 # int | Number of items to skip when calling a paginated API (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Channel Timeline
        api_response = api_instance.get_channel_timeline(channel_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AuditOperationsApi->get_channel_timeline: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Channel Timeline
        api_response = api_instance.get_channel_timeline(channel_id, offset=offset)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AuditOperationsApi->get_channel_timeline: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| Unique channel identifier |
 **offset** | **int**| Number of items to skip when calling a paginated API | [optional]

### Return type

[**ChannelTimelineEntryList**](ChannelTimelineEntryList.md)

### Authorization

[authcode](../README.md#authcode), [m2m](../README.md#m2m)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Content-Type - Content-Type <br>  * ETag - ETag <br>  * Link - Link <br>  |
**400** | Bad Request |  * Content-Type - Content-Type <br>  |
**404** | Not Found |  * Content-Type - Content-Type <br>  |
**500** | Internal Server Error |  * Content-Type - Content-Type <br>  |
**501** | Not Implemented |  * Content-Type - Content-Type <br>  |
**503** | Service Unavailable |  * Content-Type - Content-Type <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
