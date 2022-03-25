# ChannelPublishingPublications


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audio_encoder_ids** | **[str]** | Optionally specify which audio encoders should be used for this publication. If none are specified, all audio encoders configured for the transcoder will be used. | [optional] 
**create_vods** | **bool** | Create VODs for all publish points in this publication. Note that Live2VOD must also be configured for the parent |Channel|. | [optional] 
**dash** | [**ChannelPublishingDash**](ChannelPublishingDash.md) |  | [optional] 
**drms** | **[str]** | Optionally specify which DRMs to advertise in the playlist. If specified, this must be a subset of the DRMs specified by the packager associated with this publication. If omitted or empty, all DRMs specified by the packager will be advertised. This setting can only be used for HLS playlists. | [optional] 
**dvr_window_secs** | **int** | DVR window is the max sum(duration of media segments) that will be kept in a manifest at a given time in seconds. The max supported DVR window is 10 hours. | [optional] 
**hls** | [**ChannelPublishingHls**](ChannelPublishingHls.md) |  | [optional] 
**iframe_only_encoder_ids** | **[str]** | List of video encoder IDs that should have I-Frame only playlists generated for them. | [optional] 
**master_playlist_name** | **str** | Optional master manifest name. When not supplied a default of &#39;master&#39; will be used. | [optional] 
**packager_id** | **str** | Determines how segments in this publication are packaged. Must reference a packager in &#39;packaging.packagers&#39;. However, if this is a playlist-only publication (i.e. contains publish points that specify &#39;playlist_only_for&#39;), this must remain unset as the packager will be inferred from the publication this one is providing playlists for. | [optional] 
**publish_points** | [**[ChannelPublishingPublishPoints]**](ChannelPublishingPublishPoints.md) | Publish points specify where to output. | [optional] 
**redundant_publishing** | **bool** | When redundant publishing is enabled succeeding to publish a given media segment to at least one HTTPPublishPoint in publish_points will result in that segment showing up in manifests as playable content. Will require at least two publish_points defined within the same publication. | [optional] 
**thumbnail_encoder_ids** | **[str]** | Optional: Specify what thumbnail_encoders should be in this Publication | [optional] 
**use_strict_bitrate** | **bool** | Optional, indicates whether we should pad the bitrate (false) or use what is explicitly provided (true) | [optional] 
**video_encoder_ids** | **[str]** | Optionally specify which video encoders should be used for this publication. If none are specified, all video encoders configured for the transcoder will be used. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


