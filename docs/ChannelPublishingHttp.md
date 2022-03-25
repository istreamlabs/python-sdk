# ChannelPublishingHttp

HTTP destination where media segments and playlists will be published.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**basic_auth** | [**ChannelPackagingContentProtectionSimpleBasicAuth**](ChannelPackagingContentProtectionSimpleBasicAuth.md) |  | [optional] 
**compression** | **str** | Configures whether or not (and how) to compress manifests being published to the origin. If not specified, manifests will not be compressed. | [optional] 
**cross_playback_paths** | **[str]** | Cross Playback Paths are playback paths that reference alternative content. These playback paths could reference publish points from the same publication or a completely different encoder and packager altogether. Content published to an endpoint referenced by one of these cross playback paths MUST be of the same Manifest.Type. | [optional] 
**do_not_monitor** | **bool** | (Optional) Specifies if this pubpoint should not be monitored by PLM. | [optional] 
**headers** | **{str: (str,)}** | Allows custom HTTP headers to be set via configuration for all HTTP requests. | [optional] 
**method** | **str** | Method overrides what HTTP method to specify in requests to the Publish Point. If not specified the service will default to POST. | [optional] 
**playback_base_url** | **str** | The base URL where published playlists will be able to be obtained. This is often different than the publish_base_url for CDN publishing workflows. | [optional] 
**playback_query_params** | **str** | Specifies any query parameters that will be added to playback urls. Should not include the initial &#39;?&#39; Example: &#39;foo&#x3D;bar&amp;q&#x3D;golang&#39; | [optional] 
**publish_base_url** | **str** | The base URL where generated playlists will be sent/published. Each publish point requires a unique &#39;publish_base_url&#39;. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


