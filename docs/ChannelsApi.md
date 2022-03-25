# openapi_client.ChannelsApi

All URIs are relative to *https://api.istreamplanet.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_channel**](ChannelsApi.md#delete_channel) | **DELETE** /v2/channels/{channel-id} | Delete channel
[**get_channel**](ChannelsApi.md#get_channel) | **GET** /v2/channels/{channel-id} | Get Channel
[**get_playback_config**](ChannelsApi.md#get_playback_config) | **GET** /v2/channels/{channel-id}/playback | Get Channel Playback Config
[**list_channels**](ChannelsApi.md#list_channels) | **GET** /v2/channels | List channels
[**put_channel**](ChannelsApi.md#put_channel) | **PUT** /v2/channels/{channel-id} | Create/Update channel


# **delete_channel**
> delete_channel(channel_id)

Delete channel

Delete a channel and stop publishing.

### Example

* OAuth Authentication (authcode):
* OAuth Authentication (m2m):

```python
import time
import openapi_client
from openapi_client.api import channels_api
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
    api_instance = channels_api.ChannelsApi(api_client)
    channel_id = "" # str | Unique channel identifier
    if_unmodified_since = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Succeeds if the server's resource date is older or the same as the passed date. (optional)
    if_match = [
        "If-Match_example",
    ] # [str] | Succeeds if the server's resource matches one of the passed values. (optional)
    if_none_match = [
        "If-None-Match_example",
    ] # [str] | Succeeds if the server's resource matches none of the passed values. On writes, the special value * may be used to match any existing value. (optional)
    if_modified_since = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Succeeds if the server's resource date is more recent than the passed date. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delete channel
        api_instance.delete_channel(channel_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ChannelsApi->delete_channel: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete channel
        api_instance.delete_channel(channel_id, if_unmodified_since=if_unmodified_since, if_match=if_match, if_none_match=if_none_match, if_modified_since=if_modified_since)
    except openapi_client.ApiException as e:
        print("Exception when calling ChannelsApi->delete_channel: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| Unique channel identifier |
 **if_unmodified_since** | **datetime**| Succeeds if the server&#39;s resource date is older or the same as the passed date. | [optional]
 **if_match** | **[str]**| Succeeds if the server&#39;s resource matches one of the passed values. | [optional]
 **if_none_match** | **[str]**| Succeeds if the server&#39;s resource matches none of the passed values. On writes, the special value * may be used to match any existing value. | [optional]
 **if_modified_since** | **datetime**| Succeeds if the server&#39;s resource date is more recent than the passed date. | [optional]

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
**409** | Conflict |  * Content-Type - Content-Type <br>  |
**412** | Precondition Failed |  * Content-Type - Content-Type <br>  |
**500** | Internal Server Error |  * Content-Type - Content-Type <br>  |
**503** | Service Unavailable |  * Content-Type - Content-Type <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_channel**
> Channel get_channel(channel_id)

Get Channel

Get a channel's configuration

### Example

* OAuth Authentication (authcode):
* OAuth Authentication (m2m):

```python
import time
import openapi_client
from openapi_client.api import channels_api
from openapi_client.model.channel import Channel
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
    api_instance = channels_api.ChannelsApi(api_client)
    channel_id = "" # str | Unique channel identifier
    if_match = [
        "If-Match_example",
    ] # [str] | Succeeds if the server's resource matches one of the passed values. (optional)
    if_none_match = [
        "If-None-Match_example",
    ] # [str] | Succeeds if the server's resource matches none of the passed values. On writes, the special value * may be used to match any existing value. (optional)
    if_modified_since = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Succeeds if the server's resource date is more recent than the passed date. (optional)
    if_unmodified_since = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Succeeds if the server's resource date is older or the same as the passed date. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Channel
        api_response = api_instance.get_channel(channel_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ChannelsApi->get_channel: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Channel
        api_response = api_instance.get_channel(channel_id, if_match=if_match, if_none_match=if_none_match, if_modified_since=if_modified_since, if_unmodified_since=if_unmodified_since)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ChannelsApi->get_channel: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| Unique channel identifier |
 **if_match** | **[str]**| Succeeds if the server&#39;s resource matches one of the passed values. | [optional]
 **if_none_match** | **[str]**| Succeeds if the server&#39;s resource matches none of the passed values. On writes, the special value * may be used to match any existing value. | [optional]
 **if_modified_since** | **datetime**| Succeeds if the server&#39;s resource date is more recent than the passed date. | [optional]
 **if_unmodified_since** | **datetime**| Succeeds if the server&#39;s resource date is older or the same as the passed date. | [optional]

### Return type

[**Channel**](Channel.md)

### Authorization

[authcode](../README.md#authcode), [m2m](../README.md#m2m)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Content-Type - Content-Type <br>  * ETag - ETag <br>  * Last-Modified - Last-Modified <br>  |
**304** | Not Modified |  -  |
**400** | Bad Request |  * Content-Type - Content-Type <br>  |
**404** | Not Found |  * Content-Type - Content-Type <br>  |
**500** | Internal Server Error |  * Content-Type - Content-Type <br>  |
**503** | Service Unavailable |  * Content-Type - Content-Type <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_playback_config**
> ChannelPlayback get_playback_config(channel_id)

Get Channel Playback Config

Get a channel's playback configuration

### Example

* OAuth Authentication (authcode):
* OAuth Authentication (m2m):

```python
import time
import openapi_client
from openapi_client.api import channels_api
from openapi_client.model.channel_playback import ChannelPlayback
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
    api_instance = channels_api.ChannelsApi(api_client)
    channel_id = "" # str | Unique channel identifier

    # example passing only required values which don't have defaults set
    try:
        # Get Channel Playback Config
        api_response = api_instance.get_playback_config(channel_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ChannelsApi->get_playback_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| Unique channel identifier |

### Return type

[**ChannelPlayback**](ChannelPlayback.md)

### Authorization

[authcode](../README.md#authcode), [m2m](../README.md#m2m)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Content-Type - Content-Type <br>  |
**400** | Bad Request |  * Content-Type - Content-Type <br>  |
**404** | Not Found |  * Content-Type - Content-Type <br>  |
**500** | Internal Server Error |  * Content-Type - Content-Type <br>  |
**503** | Service Unavailable |  * Content-Type - Content-Type <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_channels**
> SummaryList2 list_channels()

List channels

Get a list of your channels.

### Example

* OAuth Authentication (authcode):
* OAuth Authentication (m2m):

```python
import time
import openapi_client
from openapi_client.api import channels_api
from openapi_client.model.summary_list2 import SummaryList2
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
    api_instance = channels_api.ChannelsApi(api_client)
    page_size = 100 # int | Number of items to return (optional) if omitted the server will use the default value of 100
    cursor = "cursor_example" # str | Current page cursor (optional)
    q = "q_example" # str | Search query to match against for filtering a list of channels. This searches the channel ID, name, labels, and source ID. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List channels
        api_response = api_instance.list_channels(page_size=page_size, cursor=cursor, q=q)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ChannelsApi->list_channels: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| Number of items to return | [optional] if omitted the server will use the default value of 100
 **cursor** | **str**| Current page cursor | [optional]
 **q** | **str**| Search query to match against for filtering a list of channels. This searches the channel ID, name, labels, and source ID. | [optional]

### Return type

[**SummaryList2**](SummaryList2.md)

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

# **put_channel**
> put_channel(channel_id)

Create/Update channel

Create or update an existing channel configuration.

### Example

* OAuth Authentication (authcode):
* OAuth Authentication (m2m):

```python
import time
import openapi_client
from openapi_client.api import channels_api
from openapi_client.model.put_channel_request import PutChannelRequest
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
    api_instance = channels_api.ChannelsApi(api_client)
    channel_id = "" # str | Unique channel identifier
    if_match = [
        "If-Match_example",
    ] # [str] | Succeeds if the server's resource matches one of the passed values. (optional)
    if_none_match = [
        "If-None-Match_example",
    ] # [str] | Succeeds if the server's resource matches none of the passed values. On writes, the special value * may be used to match any existing value. (optional)
    if_modified_since = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Succeeds if the server's resource date is more recent than the passed date. (optional)
    if_unmodified_since = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Succeeds if the server's resource date is older or the same as the passed date. (optional)
    validate_only = True # bool | Validate request but do not otherwise process it (optional)
    put_channel_request = PutChannelRequest(
        ingest=PutChannelRequestIngest(
            slate=ChannelIngestSlate(
                source_loss_url="https://example.com/slate.ts",
            ),
            source=PutChannelRequestIngestSource(
                audio_sources=[
                    ChannelIngestSourceAudioSources(
                        id="id_example",
                        language="language_example",
                        name="name_example",
                        selector="selector_example",
                    ),
                ],
                captions_source="ATSC_A53",
                id="s-examplej95ah2qab",
            ),
        ),
        labels=[
            "labels_example",
        ],
        name="My Channel",
        packaging=ChannelPackaging(
            packagers={
                "key": ChannelPackagingPackagers(
                    content_protection=ChannelPackagingContentProtection(
                        atlas=ChannelPackagingContentProtectionAtlas(
                            asset_id="asset_id_example",
                            company_id="company_id_example",
                            drms=[
                                "WIDEVINE",
                            ],
                            widevine_v0_pssh_box=True,
                        ),
                        bulk_file=ChannelPackagingContentProtectionBulkFile(
                            iv_rotation="RANDOM_PER_KEY",
                        ),
                        common=ChannelPackagingContentProtectionCommon(
                            scheme_type="CENC",
                        ),
                        cpix=ChannelPackagingContentProtectionCpix(
                            certificates_id="certificates_id_example",
                            content_id="content_id_example",
                            credentials_id="credentials_id_example",
                            decryption_key_id="decryption_key_id_example",
                            drms=[
                                "WIDEVINE",
                            ],
                            headers_id="headers_id_example",
                            uri="uri_example",
                        ),
                        key_rotation=ChannelPackagingContentProtectionKeyRotation(
                            interval_secs=3.14,
                            program=True,
                            program_overlap_skip_encrypt=True,
                        ),
                        sample_aes={},
                        simple=ChannelPackagingContentProtectionSimple(
                            publish_points=[
                                ChannelPackagingContentProtectionSimplePublishPoints(
                                    basic_auth=ChannelPackagingContentProtectionSimpleBasicAuth(
                                        password="password_example",
                                        username="username_example",
                                    ),
                                    compression="NONE",
                                    cross_playback_paths=[
                                        "cross_playback_paths_example",
                                    ],
                                    do_not_monitor=True,
                                    headers={
                                        "key": "key_example",
                                    },
                                    method="method_example",
                                    playback_base_url="playback_base_url_example",
                                    playback_query_params="playback_query_params_example",
                                    publish_base_url="publish_base_url_example",
                                ),
                            ],
                            require_publish="ANY",
                        ),
                    ),
                    mp2t=ChannelPackagingMp2t(
                        force_unmuxed_audio=True,
                        insert_id3_utc_time=True,
                    ),
                    mp4=ChannelPackagingMp4(
                        caption_placement="SEI_PAYLOAD",
                        insert_pssh_box=True,
                    ),
                ),
            },
        ),
        publishing=ChannelPublishing(
            closed_caption_streams=[
                ChannelPublishingClosedCaptionStreams(
                    auto_select="NO",
                    default="NO",
                    language="language_example",
                    name="name_example",
                ),
            ],
            feature_flags=[
                "feature_flags_example",
            ],
            live2vod=ChannelPublishingLive2vod(
                product_id="product_id_example",
                retention_days=1,
            ),
            publications=[
                ChannelPublishingPublications(
                    audio_encoder_ids=[
                        "audio_encoder_ids_example",
                    ],
                    create_vods=True,
                    dash=ChannelPublishingDash(
                        minimum_update_period_secs=1,
                        signaling_formats=[
                            "SCTE35_BIN_DFP",
                        ],
                        suggested_presentation_delay_secs=0,
                        url_type="RELATIVE",
                    ),
                    drms=[
                        "WIDEVINE",
                    ],
                    dvr_window_secs=0,
                    hls=ChannelPublishingHls(
                        audio_only_variants="INCLUDE_DEFAULT",
                        gap_tags="ON",
                        master_publish_frequency_secs=1,
                        master_url_type="RELATIVE",
                        media_url_type="RELATIVE",
                        partial_presentations=[
                            ChannelPublishingHlsPartialPresentations(
                                audio_encoder_ids=[
                                    "audio_encoder_ids_example",
                                ],
                                iframe_only_encoder_ids=[
                                    "iframe_only_encoder_ids_example",
                                ],
                                playlist_path="playlist_path_example",
                                thumbnail_encoder_ids=[
                                    "thumbnail_encoder_ids_example",
                                ],
                                video_encoder_ids=[
                                    "video_encoder_ids_example",
                                ],
                            ),
                        ],
                        pdt_on_every_second=True,
                        signaling_formats=[
                            "MDIALOG",
                        ],
                        utc_in_segment_title=True,
                    ),
                    iframe_only_encoder_ids=[
                        "iframe_only_encoder_ids_example",
                    ],
                    master_playlist_name="master_playlist_name_example",
                    packager_id="packager_id_example",
                    publish_points=[
                        ChannelPublishingPublishPoints(
                            http=ChannelPublishingHttp(
                                basic_auth=ChannelPackagingContentProtectionSimpleBasicAuth(
                                    password="password_example",
                                    username="username_example",
                                ),
                                compression="NONE",
                                cross_playback_paths=[
                                    "cross_playback_paths_example",
                                ],
                                do_not_monitor=True,
                                headers={
                                    "key": "key_example",
                                },
                                method="method_example",
                                playback_base_url="playback_base_url_example",
                                playback_query_params="playback_query_params_example",
                                publish_base_url="publish_base_url_example",
                            ),
                            id="id_example",
                            playlist_only_for="playlist_only_for_example",
                        ),
                    ],
                    redundant_publishing=True,
                    thumbnail_encoder_ids=[
                        "thumbnail_encoder_ids_example",
                    ],
                    use_strict_bitrate=True,
                    video_encoder_ids=[
                        "video_encoder_ids_example",
                    ],
                ),
            ],
        ),
        region="US_WEST",
        resource_class="DYNAMIC",
        signaling=ChannelSignaling(
            blackout_settings=ChannelSignalingBlackoutSettings(
                default_blackout_slate_url="https://example.com/blackout.ts",
                force_blackout_segments=[
                    "SPLICE_INSERT",
                ],
                honor_web_delivery_restriction=True,
                slates=[
                    ChannelSignalingBlackoutSettingsSlates(
                        blackout_slate_url="https://example.com/blackout.ts",
                        segments=[
                            "SPLICE_INSERT",
                        ],
                        upids=[
                            "upids_example",
                        ],
                    ),
                ],
            ),
            disable_inband_parsing=True,
            segment_settings=[
                ChannelSignalingSegmentSettings(
                    default_duration_secs=0,
                    emit_default_duration=True,
                    offset_millis=-4000,
                    segment_end_mode="MATCH_END_EVENT_ID",
                    segments=[
                        "SPLICE_INSERT",
                    ],
                    tier_filter=ChannelSignalingTierFilter(
                        explicit_tier=ChannelSignalingTierFilterExplicitTier(
                            values=[
                                1,
                            ],
                        ),
                    ),
                ),
            ],
            segments=[
                "SPLICE_INSERT",
            ],
        ),
        tags=ChannelTags(
            monitored=True,
        ),
        transcode=ChannelTranscode(
            audio_encoders=[
                ChannelTranscodeAudioEncoders(
                    audio_source_id="audio_source_id_example",
                    bit_rate=128000,
                    channels=2,
                    codec="AAC_LC",
                    id="aac128",
                    loudness=ChannelTranscodeLoudness(
                        dialog_intel=True,
                        lkfs=-31,
                        lra=3.14,
                        peak_limit=-8,
                    ),
                    sample_rate=48000,
                ),
            ],
            feature_flags=[
                "feature_flags_example",
            ],
            id3_mode="PASSTHROUGH",
            resize_mode="STRETCH",
            segmenter=ChannelTranscodeSegmenter(
                gop_duration_secs=2,
                partials_mode="GOP",
                segment_duration_secs=6,
                temi=True,
            ),
            thumbnail_encoders=[
                ChannelTranscodeThumbnailEncoders(
                    height=180,
                    id="id_example",
                    width=320,
                ),
            ],
            video_encoders=[
                ChannelTranscodeVideoEncoders(
                    bit_rate=6000000,
                    frame_rate="FR_60",
                    h264=ChannelTranscodeH264(
                        profile="BASELINE",
                    ),
                    h265=ChannelTranscodeH265(
                        profile="MAIN",
                    ),
                    height=1080,
                    id="1080p60",
                    width=1920,
                ),
            ],
        ),
    ) # PutChannelRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create/Update channel
        api_instance.put_channel(channel_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ChannelsApi->put_channel: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create/Update channel
        api_instance.put_channel(channel_id, if_match=if_match, if_none_match=if_none_match, if_modified_since=if_modified_since, if_unmodified_since=if_unmodified_since, validate_only=validate_only, put_channel_request=put_channel_request)
    except openapi_client.ApiException as e:
        print("Exception when calling ChannelsApi->put_channel: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| Unique channel identifier |
 **if_match** | **[str]**| Succeeds if the server&#39;s resource matches one of the passed values. | [optional]
 **if_none_match** | **[str]**| Succeeds if the server&#39;s resource matches none of the passed values. On writes, the special value * may be used to match any existing value. | [optional]
 **if_modified_since** | **datetime**| Succeeds if the server&#39;s resource date is more recent than the passed date. | [optional]
 **if_unmodified_since** | **datetime**| Succeeds if the server&#39;s resource date is older or the same as the passed date. | [optional]
 **validate_only** | **bool**| Validate request but do not otherwise process it | [optional]
 **put_channel_request** | [**PutChannelRequest**](PutChannelRequest.md)|  | [optional]

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
**201** | Created |  * ETag - ETag <br>  * Last-Modified - Last-Modified <br>  * Location - Location <br>  |
**204** | No Content |  * ETag - ETag <br>  * Last-Modified - Last-Modified <br>  * Location - Location <br>  |
**304** | Not Modified |  -  |
**400** | Bad Request |  * Content-Type - Content-Type <br>  |
**404** | Not Found |  * Content-Type - Content-Type <br>  |
**409** | Conflict |  * Content-Type - Content-Type <br>  |
**412** | Precondition Failed |  * Content-Type - Content-Type <br>  |
**500** | Internal Server Error |  * Content-Type - Content-Type <br>  |
**503** | Service Unavailable |  * Content-Type - Content-Type <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
