# Channel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ingest** | [**ChannelIngest**](ChannelIngest.md) |  | 
**transcode** | [**ChannelTranscode**](ChannelTranscode.md) |  | 
**created** | **datetime** | Date and time the channel was created. | [optional] [readonly] 
**id** | **str** | External Channel ID provided at channel creation time | [optional] [readonly] 
**labels** | **[str]** | Optional labels for a channel. Any included labels must be at least 1 character long, but no greater than 256 characters. The maximum number of labels is 10. | [optional] 
**modified** | **datetime** | Date and time the channel was last modified. | [optional] [readonly] 
**name** | **str** | A friendly human-readable name for the channel. This will get displayed in user interfaces. | [optional] 
**packaging** | [**ChannelPackaging**](ChannelPackaging.md) |  | [optional] 
**publishing** | [**ChannelPublishing**](ChannelPublishing.md) |  | [optional] 
**region** | **str** | Region represents the general geolocation for transcoding and stream egress from iStreamPlanet. If no region is provided at channel creation time, then &#39;US_WEST&#39; is used. | [optional] 
**resource_class** | **str** | If the ResourceClass is unspecified the channel will default to run in the &#39;DYNAMIC&#39; ResourceClass. Note that changing the ResourceClass for a running channel is supported and will be performed with no downtime. | [optional] 
**self** | **str** | Self link for the channel. | [optional] [readonly] 
**signaling** | [**ChannelSignaling**](ChannelSignaling.md) |  | [optional] 
**tags** | [**ChannelTags**](ChannelTags.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


