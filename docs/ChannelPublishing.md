# ChannelPublishing

Publishing configures playlist formats and where to send video and playlist data.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**closed_caption_streams** | [**[ChannelPublishingClosedCaptionStreams]**](ChannelPublishingClosedCaptionStreams.md) | Configures how captioning information is published. | [optional] 
**feature_flags** | **[str]** | Set of string identifiers corresponding to features that this Channel is opting in. | [optional] 
**live2vod** | [**ChannelPublishingLive2vod**](ChannelPublishingLive2vod.md) |  | [optional] 
**publications** | [**[ChannelPublishingPublications]**](ChannelPublishingPublications.md) | A set of individual configurations that each can configure a specific destination and mechanism of delivery for segments and/or playlists. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


