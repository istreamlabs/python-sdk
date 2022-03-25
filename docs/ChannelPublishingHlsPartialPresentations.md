# ChannelPublishingHlsPartialPresentations


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audio_encoder_ids** | **[str]** | Specify which audio encoders should be used for this presentation. If none are specified, all audio encoders configured for the parent Publication will be used. | [optional] 
**iframe_only_encoder_ids** | **[str]** | List of video encoder IDs that should have I-Frame only playlists generated for them. | [optional] 
**playlist_path** | **str** | Sub-path that will be appended onto the publish and playback base URLs of HTTP PublishPoints for published playlist files. | [optional] 
**thumbnail_encoder_ids** | **[str]** | Specify which thumbnail encoders should be used for this presentation. If none are specified, all thumbnail encoders configured for the parent Publication will be used. | [optional] 
**video_encoder_ids** | **[str]** | Specify which video encoders should be used for this presentation. If none are specified, all video encoders configured for the parent Publication will be used. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


