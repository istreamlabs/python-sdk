# ChannelPublishingHls

HLS configures publication settings. Only one of HLS or DASH can be set.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audio_only_variants** | **str** | Defines how audio only variant streams are included in the master playlist, where the variant streams are defined by #EXT-X-STREAM-INF tag, the tag attributes provide information about the Stream. If NOT_SET - honor the deprecated &#39;exclude_audio_only&#39; flag. Later when the deprecated flag is removed, the NOT_SET would mean INCLUDE_DEFAULT The INCLUDE_DEFAULT option - only the default &#39;audio only variant stream&#39; is included in master playlist. This is the most common use case. INCLUDE_NONE - no audio only variant streams are included in the master playlist, it replaces &#39;exclude_audio_only&#39; setting. INCLUDE_ALL - include all audio only variant streams in the master playlist. | [optional] 
**gap_tags** | **str** | Allows turning gap tags ON/OFF. When turned ON - the tag &#39;#EXT-X-GAP&#39; is inserted into media playlist for a missing segment. When turned OFF - Discontinuity is inserted into the playlist for missing segment(s). The default option UNDEFINED is mapped to OFF. Note: Gap tags are always inserted for the missing thumbnail segments independently of this setting | [optional] 
**master_publish_frequency_secs** | **int** | How often the master playlist(s) should be published in seconds. A value of 0 means the master playlist will only be published once at channel start. | [optional] 
**master_url_type** | **str** | Allows specifying url type for HLS master playlists. If not provided, playlist generation will use &#39;RELATIVE&#39;. | [optional] 
**media_url_type** | **str** | Allows specifying url type for HLS media playlists. If not provided, playlist generation will use &#39;RELATIVE&#39;. | [optional] 
**partial_presentations** | [**[ChannelPublishingHlsPartialPresentations]**](ChannelPublishingHlsPartialPresentations.md) | Specify which partial presentations should be used for this presentation. Partial presentations are additional master playlists that point to a subset of the parent presentation&#39;s media streams/variant playlists. | [optional] 
**pdt_on_every_second** | **bool** | When true a #EXT-X-PROGRAM-DATE-TIME tag will be placed on every media segment in media playlists. When false, the default behavior, the PDT tag is set according to the HLS specification. | [optional] 
**signaling_formats** | **[str]** | Signaling formats specifies which SCTE-35 timeline marker formatting to use when rendering playlists. | [optional] 
**utc_in_segment_title** | **bool** | Include a UTC timestamp (that is equivalent in value to #EXT-X-PROGRAM-DATE-TIME) in the title of each media segment in media playlists. Ex. #EXTINF:6.006,LTC&#x3D;2020-01-01T12:00:00.000Z | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


